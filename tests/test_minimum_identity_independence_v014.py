import ast,hashlib,inspect,json,os,tempfile,unittest
from pathlib import Path
from tools.minimum_identity_independence_v014 import *
A=b'mii-conformance:v1\ncondition=ALPHA\npayload=A';B=b'mii-conformance:v1\ncondition=ALPHA\npayload=B'
def c(**kw):
 d=dict(semantic_case_id='SEM_ONLY',frozen_bytes=A,materialized_bytes=A,executed_bytes=A,declared_object_id='ALPHA',convenience_identity_match=True,custody_override=None);d.update(kw);return Case(**d)
class T(unittest.TestCase):
 def test_schema_hashes(self):verify_schemas()
 def test_alias_resolution(self):
  o={'version':ORACLE_VERSION,'objects':{'R':{'bytes':A.decode(),'sha256':hashlib.sha256(A).hexdigest()},'SECRET':{'bytes':B.decode(),'sha256':hashlib.sha256(B).hexdigest()}},'critical_clean_controls':[],'critical_failures':[{'id':'E','frozen':'R','materialized':'R','executed':'SECRET','declared_condition':'ALPHA','convenience_identity_match':True}],'diagnostic_cases':[]}
  x=resolve_case(o,'E');self.assertEqual(x.executed_bytes,B)
  with tempfile.TemporaryDirectory() as td:self.assertNotIn(b'SECRET',prepare('chi_3',x,Path(td)).view_bytes)
 def test_forbidden_extra(self):
  with tempfile.TemporaryDirectory() as td:
   p=prepare('chi_0',c(),Path(td));v=json.loads(p.view_bytes);v['oracle_mismatch']=True
   with self.assertRaises(ConformanceError):validate('chi_0',v)
 def test_handles(self):
  with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
   x=prepare('chi_0',c(),Path(a)).attestation['case_handle'];y=prepare('chi_0',c(),Path(b)).attestation['case_handle'];self.assertRegex(x,r'^[0-9a-f]{64}$');self.assertNotEqual(x,y)
 def test_stateless(self):
  with tempfile.TemporaryDirectory() as td:
   p=prepare('chi_3',c(),Path(td));self.assertEqual(evaluate('chi_3',p.view_bytes,Cost()),evaluate('chi_3',p.view_bytes,Cost()))
 def test_purity(self):
  tree=ast.parse(inspect.getsource(evaluate));txt=ast.dump(tree)
  for x in ('open','socket','subprocess','environ','getenv','chdir','time','secrets'):self.assertNotIn(x,txt)
 def test_chi1_unresolved(self):
  with tempfile.TemporaryDirectory() as td:
   p=prepare('chi_1',c(),Path(td));self.assertEqual(evaluate('chi_1',p.view_bytes,p.cost),'IDENTITY_UNRESOLVED')
 def test_chi2_chi3_authority_split(self):
  fake=hashlib.sha256(A).hexdigest();x=c(executed_bytes=B,custody_override=fake)
  with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
   p2=prepare('chi_2',x,Path(a));p3=prepare('chi_3',x,Path(b));self.assertEqual(evaluate('chi_2',p2.view_bytes,p2.cost),'IDENTITY_PASS');self.assertEqual(evaluate('chi_3',p3.view_bytes,p3.cost),'IDENTITY_MISMATCH')
 def test_lifecycle(self):
  with tempfile.TemporaryDirectory() as td:
   p=prepare('chi_3',c(),Path(td));self.assertEqual(tuple(p.life.events),Life.ORDER[:3]);f=run('chi_3',p);self.assertEqual(p.life.events[-1],Life.ORDER[3]);self.assertEqual(score(p,f,False),1);self.assertEqual(p.life.events[-1],Life.ORDER[4])
 def test_referee_early_reject(self):
  with tempfile.TemporaryDirectory() as td:
   p=prepare('chi_0',c(),Path(td));f=Frozen('IDENTITY_PASS',b'{}',hashlib.sha256(b'{}').hexdigest())
   with self.assertRaises(ConformanceError):score(p,f,False)
 def test_persist_cumulative(self):
  with tempfile.TemporaryDirectory() as td:
   co=Cost();s=Store(Path(td),co);s.write('x',b'abcde');s.write('x',b'xy');s.truncate('x',1);self.assertEqual(s.retained(),1);s.delete('x');self.assertEqual(s.retained(),0);self.assertEqual(co.C_persist_bytes,7)
 def test_view_bytes(self):
  with tempfile.TemporaryDirectory() as td:
   p=prepare('chi_0',c(),Path(td));self.assertEqual(p.cost.C_view_bytes,len(p.view_bytes))
 def test_missing_not_zero(self):self.assertFalse(Cost().is_complete())
 def test_aggregate(self):
  cs=[]
  for _ in range(6):x=Cost();x.mark_view(b'abc');cs.append(x)
  self.assertEqual(aggregate(cs),(18,0,0,0,0,0));cs[0].complete['C_persist_bytes']=False
  with self.assertRaises(ConformanceError):aggregate(cs)
 def test_pareto(self):
  vs={'a':(1,1,1,1,1,1),'b':(2,2,2,2,2,2),'c':(0,3,1,1,1,1)};self.assertTrue(dominates(vs['a'],vs['b']));self.assertEqual(pareto(vs),{'a','c'})
if __name__=='__main__':unittest.main()
