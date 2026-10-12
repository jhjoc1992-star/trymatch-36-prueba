from playwright.sync_api import sync_playwright
from pathlib import Path
import json
p='file:///mnt/data/TRYMATCH_REV_10/public/index.html'
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for n in [2,3,4,5,6]:
  for w,h in [(915,412),(740,360),(1280,720)]:
   page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.set_content(Path('/mnt/data/TRYMATCH_REV_10/public/index.html').read_text())
   state={'type':'state','code':'TEST','me':0,'phase':'playing','players':[{'name':'Jugador '+str(i),'avatar':'🦊','bot':i>0,'online':True} for i in range(n)],'settings':{'delay':8,'mode':'simple','difficulty':'normal'},'paused':False,'game':{'turn':0,'turnNo':1,'center':[{'id':i,'removed':False,'revealed':None} for i in range({2:12,3:9,4:8,5:6,6:6}[n])],'hands':[[1,2,2,3,4,5,6,7,8,9,10,11][:({2:12,3:9,4:7,5:6,6:5}[n])]]+[([None]*({2:12,3:9,4:7,5:6,6:5}[n])) for _ in range(n-1)],'counts':[({2:12,3:9,4:7,5:6,6:5}[n])]*n,'revealed':[],'triples':[[] for _ in range(n)],'swapped':False,'winner':None,'notice':'', 'lockUntil':0}}
   page.evaluate('s=>{S=s;me=0;render()}',state)
   seats=page.locator('.seat'); boxes=[seats.nth(i).bounding_box() for i in range(seats.count())]
   overlap=[]
   for i,a in enumerate(boxes):
    for j,b in enumerate(boxes[:i]):
     x=max(0,min(a['x']+a['width'],b['x']+b['width'])-max(a['x'],b['x']))
     y=max(0,min(a['y']+a['height'],b['y']+b['height'])-max(a['y'],b['y']))
     if x*y>20:overlap.append((i,j,round(x*y)))
   if n==6 and w==915:page.screenshot(path='/mnt/data/TRYMATCH_REV_10_VISTA_915.png')
   print('layout',n,w,h,'overlap',overlap,'errors',errors)
   page.close()
 browser.close()
