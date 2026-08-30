import json, sys, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

TASK_IDS = ['070dd51e','08573cc6','0becf7df','0d87d2a6','18419cfa','20981f0e','29700607','2b01abd0','42a15761','4acc7107','4cd1b7b2','54db823b','58743b76','642248e4','66e6c45b','696d4842','712bf12e','73c3b0d8','782b5218','79fb03f4','7c8af763','7ee1c6ea','85b81ff1','85fa5666','8ee62060','917bccba','9356391f','93c31fbe','94414823','95a58926','96a8c0cd','9c56f360','9def23fe','9f27f097','a934301b','ac0c5833','baf41dbf','bb52a14b','bd14c3bf','bf32578f','c35c1b4c','c62e2108','c87289bb','d37a1ef5','d492a647','da515329','dc2aa30b','dd2401ed','e1d2900e','ecaa0ec1','ef26cbf6','f3cdc58f','f45f5ca7','f5c89df1','f823c43c','f83cb3f6','f9a67cb5','fc754716']

COLORS = {
    0:(0,0,0), 1:(0,116,217), 2:(255,65,54), 3:(46,204,64), 4:(255,220,0),
    5:(170,170,170), 6:(240,18,190), 7:(255,133,27), 8:(127,219,255), 9:(135,12,37)
}

def font(size=24):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

F=font(24); FS=font(18); FB=font(30)

def render_grid(grid, max_px=420):
    h=len(grid); w=len(grid[0]) if h else 1
    cell=max(4,min(32,max_px//max(h,w)))
    im=Image.new('RGB',(w*cell+1,h*cell+1),'white'); d=ImageDraw.Draw(im)
    for r,row in enumerate(grid):
        for c,v in enumerate(row):
            x=c*cell; y=r*cell
            d.rectangle([x,y,x+cell,y+cell],fill=COLORS[int(v)],outline=(80,80,80) if cell>=10 else COLORS[int(v)])
    return im

def changed_stats(inp,out):
    hi,wi=len(inp),len(inp[0]); ho,wo=len(out),len(out[0])
    same=(hi==ho and wi==wo)
    if same:
        changed=sum(inp[r][c]!=out[r][c] for r in range(hi) for c in range(wi))
        add=sum(inp[r][c]==0 and out[r][c]!=0 for r in range(hi) for c in range(wi))
        rem=sum(inp[r][c]!=0 and out[r][c]==0 for r in range(hi) for c in range(wi))
        recol=sum(inp[r][c]!=0 and out[r][c]!=0 and inp[r][c]!=out[r][c] for r in range(hi) for c in range(wi))
    else: changed=add=rem=recol=None
    return {'in_shape':[hi,wi],'out_shape':[ho,wo],'same_shape':same,'changed':changed,'add':add,'remove':rem,'recolor':recol}

def render_task(tid, task, outdir):
    pairs=[('TRAIN',i,p) for i,p in enumerate(task['train'])] + [('TEST',i,p) for i,p in enumerate(task['test'])]
    rows=[]; stats=[]
    for kind,i,p in pairs:
        inp=render_grid(p['input']); out=render_grid(p['output'])
        stats.append({'kind':kind,'index':i,**changed_stats(p['input'],p['output'])})
        label=f'{kind} {i}: {len(p["input"])}x{len(p["input"][0])} -> {len(p["output"])}x{len(p["output"][0])}'
        row_h=max(inp.height,out.height)+70
        row=Image.new('RGB',(1100,row_h),'white'); d=ImageDraw.Draw(row)
        d.text((10,5),label,fill='black',font=FS)
        row.paste(inp,(10,40)); d.text((480,45),'→',fill='black',font=FB); row.paste(out,(550,40))
        rows.append(row)
    H=60+sum(r.height for r in rows); im=Image.new('RGB',(1100,H),'white'); d=ImageDraw.Draw(im)
    d.text((10,10),tid,fill='black',font=FB)
    y=60
    for r in rows: im.paste(r,(0,y)); y+=r.height
    im.save(outdir/f'{tid}.png')
    return stats

def main(root,outdir):
    root=Path(root); outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    allstats={}
    for tid in TASK_IDS:
        p=root/f'{tid}.json'
        task=json.loads(p.read_text())
        allstats[tid]=render_task(tid,task,outdir)
    (outdir/'task_stats.json').write_text(json.dumps(allstats,indent=2))
    (outdir/'task_ids.txt').write_text('\n'.join(TASK_IDS)+'\n')
    print(json.dumps({'rendered':len(TASK_IDS),'outdir':str(outdir)},indent=2))

if __name__=='__main__': main(sys.argv[1],sys.argv[2])
