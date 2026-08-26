from __future__ import annotations
import hashlib,json,re,secrets
from dataclasses import dataclass,field
from pathlib import Path
from typing import Any,Mapping

class ConformanceError(RuntimeError): pass
HEX64=re.compile(r'^[0-9a-f]{64}$')
TERMINALS={'IDENTITY_PASS','IDENTITY_MISMATCH','IDENTITY_UNRESOLVED'}
ORACLE_VERSION='MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0.1.1'
ORACLE_BLOB='f2f46f4ad0df0086aaa40c6f2b67755050a66ad6'
PRIMARY_FIELDS=('C_view_bytes','C_capture_bytes','C_persist_bytes','C_sha256_ops','C_extract_ops','C_identity_compare_ops')
_SCHEMA_JSON={
'chi_0':'{"authority":"self-report/convenience only; no H_f/H_m/H_e bytes or hashes","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI0_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"]],"schema_id":"MII_VIEW_CHI0_V0.1"}',
'chi_1':'{"authority":"independent H_f/H_m only; H_e unavailable; H_m must not substitute for H_e","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal","executed_raw_bytes_utf8","custody_reported_executed_sha256"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI1_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"]],"schema_id":"MII_VIEW_CHI1_V0.1"}',
'chi_2':'{"authority":"custody_reported_executed_sha256 is H_e authority; do not recompute SHA256(executed_raw_bytes_utf8)","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI2_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"],["executed_raw_bytes_utf8","string"],["custody_reported_executed_sha256","hex64"]],"schema_id":"MII_VIEW_CHI2_V0.1"}',
'chi_3':'{"authority":"independently recompute SHA256(executed_raw_bytes_utf8) as H_e authority; custody-reported H_e diagnostic only","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI3_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"],["executed_raw_bytes_utf8","string"],["custody_reported_executed_sha256","hex64"]],"schema_id":"MII_VIEW_CHI3_V0.1"}' }
SCHEMAS={k:json.loads(v) for k,v in _SCHEMA_JSON.items()}
SCHEMA_SHA={'chi_0':'54214df3b4b02e8304d96a36629ac8ce6c851d61c4e5e58fcade382f28b739d3','chi_1':'b873fad1d01af7c3c57d27d68cbab0df008248780fd397c5c548e2a9477c7056','chi_2':'61e1de0a04040172faa914813b86f8b31f7396f11db176e82e67e145f253c7a8','chi_3':'bf17650e576cbd28f7c2cbb12b039b60a2885794ae812031a929fe77a52c43b1'}
def shared_sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def schema_sha(chi:str)->str:return shared_sha(json.dumps(SCHEMAS[chi],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def verify_schemas():
 for k,v in SCHEMA_SHA.items():
  if schema_sha(k)!=v: raise ConformanceError(f'schema hash mismatch {k}')
def git_blob_sha1(b:bytes)->str:return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
def load_oracle(path:Path)->dict[str,Any]:
 b=path.read_bytes()
 if git_blob_sha1(b)!=ORACLE_BLOB: raise ConformanceError('oracle blob mismatch')
 o=json.loads(b.decode())
 if o.get('version')!=ORACLE_VERSION: raise ConformanceError('oracle version mismatch')
 return o

@dataclass
class Cost:
 C_view_bytes:int|None=None; C_capture_bytes:int=0; C_persist_bytes:int=0; C_sha256_ops:int=0; C_extract_ops:int=0; C_identity_compare_ops:int=0
 complete:dict[str,bool]=field(default_factory=lambda:{'C_view_bytes':False,'C_capture_bytes':True,'C_persist_bytes':True,'C_sha256_ops':True,'C_extract_ops':True,'C_identity_compare_ops':True})
 def capture(self,b:bytes)->bytes:self.C_capture_bytes+=len(b);return bytes(b)
 def sha(self,b:bytes)->str:self.C_sha256_ops+=1;return hashlib.sha256(b).hexdigest()
 def extract(self,s:str)->bytes:self.C_extract_ops+=1;return s.encode()
 def compare(self,a:str,b:str)->bool:self.C_identity_compare_ops+=1;return a==b
 def mark_view(self,b:bytes):self.C_view_bytes=len(b);self.complete['C_view_bytes']=True
 def vector(self):return tuple(getattr(self,k) for k in PRIMARY_FIELDS)
 def is_complete(self):return self.C_view_bytes is not None and all(self.complete.values())

class Store:
 def __init__(self,root:Path,cost:Cost):
  self.root=root;self.cost=cost;root.mkdir(parents=True,exist_ok=True)
  if any(root.iterdir()):raise ConformanceError('custody root not empty at T1')
 def p(self,n:str)->Path:
  p=(self.root/n).resolve();r=self.root.resolve()
  if r!=p and r not in p.parents:raise ConformanceError('custody escape')
  return p
 def write(self,n:str,b:bytes):
  p=self.p(n);p.parent.mkdir(parents=True,exist_ok=True)
  with p.open('wb') as f:w=f.write(b)
  if w!=len(b):self.cost.complete['C_persist_bytes']=False;raise ConformanceError('partial write')
  self.cost.C_persist_bytes+=w
 def read(self,n:str)->bytes:return self.p(n).read_bytes()
 def truncate(self,n:str,size:int):
  with self.p(n).open('r+b') as f:f.truncate(size)
 def delete(self,n:str):self.p(n).unlink()
 def retained(self)->int:return sum(p.stat().st_size for p in self.root.rglob('*') if p.is_file())

@dataclass(frozen=True)
class Case:
 semantic_case_id:str; frozen_bytes:bytes; materialized_bytes:bytes; executed_bytes:bytes; declared_object_id:str; convenience_identity_match:bool|None; custody_override:str|None=None

def resolve_case(o:Mapping[str,Any],cid:str)->Case:
 rs=[r for sec in ('critical_clean_controls','critical_failures','diagnostic_cases') for r in o.get(sec,[]) if r.get('id')==cid]
 if len(rs)!=1:raise ConformanceError('case id must resolve once')
 r=rs[0];objs=o['objects']
 def obj(alias):
  x=objs[alias];b=x['bytes'].encode()
  if shared_sha(b)!=x['sha256']:raise ConformanceError('object hash mismatch')
  return b
 return Case(cid,obj(r['frozen']),obj(r['materialized']),obj(r['executed']),r['declared_condition'],r.get('convenience_identity_match'),r.get('recorder_reported_executed_sha256'))

@dataclass
class Life:
 events:list[str]=field(default_factory=list)
 ORDER=('T0_COMMON_ACTUAL_OBJECT_FIXED','T1_ARCHITECTURE_SPECIFIC_EVIDENCE_PATH_OPEN','T2_EXACT_VIEW_DISPATCHED','T3_TERMINAL_ARCHITECTURE_VERDICT_FROZEN','T4_REFEREE_ORACLE_JOIN')
 def mark(self,e:str):
  exp=self.ORDER[len(self.events)] if len(self.events)<5 else 'NO_FURTHER_EVENT'
  if e!=exp:raise ConformanceError(f'lifecycle got {e}, expected {exp}')
  self.events.append(e)
 def through(self,e:str):
  i=self.ORDER.index(e)
  if tuple(self.events)!=self.ORDER[:i+1]:raise ConformanceError(f'lifecycle not through {e}')

@dataclass(frozen=True)
class Prepared:view_bytes:bytes;attestation:dict[str,str];cost:Cost;life:Life

def _rule(name,rule,v):
 if rule.startswith('const:') and v!=rule.split(':',1)[1]:raise ConformanceError(name)
 if rule=='hex64' and (not isinstance(v,str) or not HEX64.fullmatch(v)):raise ConformanceError(name)
 if rule=='enum:ALPHA|BETA' and v not in {'ALPHA','BETA'}:raise ConformanceError(name)
 if rule=='bool|null' and v is not None and not isinstance(v,bool):raise ConformanceError(name)
 if rule=='string' and not isinstance(v,str):raise ConformanceError(name)
def validate(chi:str,v:Mapping[str,Any]):
 fs=SCHEMAS[chi]['fields_in_order'];names=[x[0] for x in fs]
 if list(v)!=names:raise ConformanceError('view fields/order')
 for n,r in fs:_rule(n,r,v[n])
 raw=json.dumps(v,separators=(',',':'),ensure_ascii=False).encode()
 for x in (b'semantic_case_id',b'case_partition',b'oracle_mismatch',b'oracle_class',b'global_ordinal',b'expected_terminal',b'previous_state',b'ALPHA_MUT'):
  if x in raw:raise ConformanceError(f'forbidden leak {x!r}')
def serialize(chi:str,v:Mapping[str,Any])->bytes:
 validate(chi,v);b=json.dumps(v,separators=(',',':'),ensure_ascii=False).encode()
 if b.startswith(b'\xef\xbb\xbf') or b.endswith(b'\n'):raise ConformanceError('serialization')
 return b
def parse(chi:str,b:bytes)->dict[str,Any]:
 if b.startswith(b'\xef\xbb\xbf') or b.endswith(b'\n'):raise ConformanceError('serialization')
 v=json.loads(b.decode(),object_pairs_hook=dict);validate(chi,v)
 if json.dumps(v,separators=(',',':'),ensure_ascii=False).encode()!=b:raise ConformanceError('noncanonical view')
 return v

def prepare(chi:str,c:Case,root:Path)->Prepared:
 verify_schemas();life=Life();life.mark(Life.ORDER[0]);h=secrets.token_hex(32)
 if not HEX64.fullmatch(h):raise ConformanceError('handle')
 life.mark(Life.ORDER[1]);cost=Cost();store=Store(root,cost);sid=SCHEMAS[chi]['schema_id']
 v={'schema_version':sid,'case_handle':h,'declared_object_id':c.declared_object_id,'convenience_identity_match':c.convenience_identity_match}
 if chi!='chi_0':
  v|={'frozen_bytes_utf8':c.frozen_bytes.decode(),'frozen_sha256':cost.sha(c.frozen_bytes),'materialized_bytes_utf8':c.materialized_bytes.decode(),'materialized_sha256':cost.sha(c.materialized_bytes)}
 if chi in {'chi_2','chi_3'}:
  store.write('executed.raw',cost.capture(c.executed_bytes));raw=store.read('executed.raw');v['executed_raw_bytes_utf8']=raw.decode();v['custody_reported_executed_sha256']=c.custody_override or cost.sha(raw)
 names=[x[0] for x in SCHEMAS[chi]['fields_in_order']];v={n:v[n] for n in names};b=serialize(chi,v);cost.mark_view(b)
 att={'case_handle':h,'schema_id':sid,'schema_sha256':SCHEMA_SHA[chi],'dispatched_view_sha256':shared_sha(b),'schema_validation':'PASS'};life.mark(Life.ORDER[2]);return Prepared(b,att,cost,life)

def evaluate(chi:str,b:bytes,cost:Cost)->str:
 v=parse(chi,b)
 if chi=='chi_0':return 'IDENTITY_PASS' if v['convenience_identity_match'] is True else 'IDENTITY_MISMATCH' if v['convenience_identity_match'] is False else 'IDENTITY_UNRESOLVED'
 hf,hm=v['frozen_sha256'],v['materialized_sha256']
 if not cost.compare(hf,hm):return 'IDENTITY_MISMATCH'
 if chi=='chi_1':return 'IDENTITY_UNRESOLVED'
 if chi=='chi_2':return 'IDENTITY_PASS' if cost.compare(hm,v['custody_reported_executed_sha256']) else 'IDENTITY_MISMATCH'
 he=cost.sha(cost.extract(v['executed_raw_bytes_utf8']));return 'IDENTITY_PASS' if cost.compare(hm,he) else 'IDENTITY_MISMATCH'

@dataclass(frozen=True)
class Frozen:terminal:str;output_bytes:bytes;output_sha256:str
def run(chi:str,p:Prepared)->Frozen:
 p.life.through(Life.ORDER[2]);t=evaluate(chi,p.view_bytes,p.cost);b=json.dumps({'terminal':t},separators=(',',':')).encode();f=Frozen(t,b,shared_sha(b));p.life.mark(Life.ORDER[3]);return f
def score(p:Prepared,f:Frozen,oracle_mismatch:bool)->int:
 p.life.through(Life.ORDER[3]);p.life.mark(Life.ORDER[4]);return int(f.terminal==('IDENTITY_MISMATCH' if oracle_mismatch else 'IDENTITY_PASS'))
def aggregate(cs:list[Cost])->tuple[int,...]:
 if len(cs)!=6 or not all(c.is_complete() for c in cs):raise ConformanceError('COST_COMPARISON_INCOMPLETE')
 return tuple(sum(int(c.vector()[i]) for c in cs) for i in range(6))
def dominates(a:tuple[int,...],b:tuple[int,...])->bool:
 if len(a)!=6 or len(b)!=6:raise ConformanceError('dimension')
 return all(x<=y for x,y in zip(a,b)) and any(x<y for x,y in zip(a,b))
def pareto(vs:Mapping[str,tuple[int,...]])->set[str]:return {n for n,v in vs.items() if not any(m!=n and dominates(w,v) for m,w in vs.items())}
