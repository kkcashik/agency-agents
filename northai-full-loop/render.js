const {chromium}=require('playwright');const {spawn}=require('child_process');
const [,,mode,a,b,out]=process.argv;const FPS=30;
(async()=>{
 const br=await chromium.launch();const p=await br.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+process.cwd()+'/index.html?v='+mode);await p.waitForFunction('window.READY');
 const ff=spawn('ffmpeg',['-y','-f','image2pipe','-framerate',FPS,'-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p','-r',FPS,out],{stdio:['pipe','ignore','ignore']});
 for(let f=+a;f<+b;f++){await p.evaluate(t=>window.render(t),f/FPS);const buf=await p.screenshot({type:'jpeg',quality:95});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
 ff.stdin.end();await new Promise(r=>ff.on('close',r));await br.close();})();
