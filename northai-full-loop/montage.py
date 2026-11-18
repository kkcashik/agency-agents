import sys
from PIL import Image
F,mode,out=sys.argv[1:4];ts=sys.argv[4:]
ims=[Image.open(f'{F}/{mode}_{t}.png').resize((432,768)) for t in ts]
w=Image.new('RGB',(432*len(ims),768));[w.paste(im,(i*432,0)) for i,im in enumerate(ims)];w.save(out)
