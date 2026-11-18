"""Mix per-scene voiceover clips onto the film.
Usage: python3 mux.py 83|35   (needs vo/a1..a11.mp3 for 83, vo/b1..b6.mp3 for 35)"""
import subprocess,sys,os
mode=sys.argv[1]
cfg={'83':('a',[.8,8.3,16.4,23.2,30.4,38.4,45.4,53.4,60.4,69.2,77.6],[7,7.6,6.5,7.0,7.5,6.5,7.5,6.8,8.4,7.9,5.0],'../out/northai-full-loop-83s.mp4'),
     '35':('b',[.8,6.2,12.5,20.4,28.4,32.4],[5,6.1,7,7.5,3.9,2.6],'../out/northai-full-loop-35s.mp4')}
pre,starts,maxd,vid=cfg[mode]
def dur(f):return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
ins=[];fl=[]
for i,(s,m) in enumerate(zip(starts,maxd),1):
    f=f'{pre}{i}.mp3';d=dur(f);t=max(1.0,min(1.2,d/m))   # speed up (max 1.2x) only if a line overruns its slot
    ins+=['-i',f];fl.append(f'[{i}:a]atempo={t:.3f},adelay={int(s*1000)}|{int(s*1000)}[a{i}]')
n=len(starts)
g=';'.join(fl)+';'+''.join(f'[a{i}]' for i in range(1,n+1))+f'amix=inputs={n}:normalize=0,loudnorm=I=-16:TP=-1.5,apad[vo]'
out=vid.replace('.mp4','-vo.mp4')
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',vid,*ins,'-filter_complex',g,'-map','0:v','-map','[vo]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',out],check=True)
print(out)
