const {chromium}=require('playwright');
(async()=>{
 const [,, mode, out, ...ts]=process.argv;
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>console.log('LOG',m.text()));
 await p.goto('file://'+process.cwd()+'/index.html?v='+mode);await p.waitForFunction('window.READY');
 for(const t of ts){await p.evaluate(t=>window.render(t),+t);await p.screenshot({path:`${out}/${mode}_${t}.png`});}
 await b.close();})();
