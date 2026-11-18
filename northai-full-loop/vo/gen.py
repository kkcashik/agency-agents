import json,subprocess,sys
V='EXAVITQu4vr4xnSDxMaL'
lines={
'a1':"Somebody needs a dentist tonight.",
'a2':"First, they have to find you. So we run your ads, your Google profile, your local SEO, and your AI search visibility.",
'a3':"Now you start showing up higher, and more searches turn into clicks.",
'a4':"Then somebody has to answer. At nine twenty-one, we do. Name, coverage, reason for the visit, in your system before they hang up.",
'a5':"Most of them aren't ready today, so we stay in touch until they are.",
'a6':"Then it goes into the calendar. Not a lead inbox. The actual schedule.",
'a7':"Booked isn't the same as arrived, so we remind them twice before the chair sits empty.",
'a8':"They leave happy, and we ask for the review that pushes you back up the results. That's the loop, starting again.",
'a9':"Six months later, when they're due for a cleaning and nobody's called, we call them. Those patients already trust you.",
'a10':"Found. Captured. Nurtured. Booked. Reminded. Reviewed. Recalled. You pay once to find a patient. The system earns from them for years.",
'a11':"NorthAI. Book a free audit at get north A I dot C A.",
'b1':"Somebody needs a dentist tonight.",
'b2':"So we run your ads, your Google profile, your local SEO and AI search, so they find you.",
'b3':"Then we answer, follow up, book, remind, and ask for the review. Automatically.",
'b4':"And six months later, when they're due and nobody's called, we call them. Patients you already have.",
'b5':"One loop. Found once, booked for years.",
'b6':"NorthAI. Book a free audit.",
}
for k,t in lines.items():
    body=json.dumps({"text":t,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":.55,"similarity_boost":.8,"style":.15,"use_speaker_boost":True}})
    r=subprocess.run(['curl','-sS','-o',k+'.mp3','-w','%{http_code}','-X','POST',f'https://api.elevenlabs.io/v1/text-to-speech/{V}?output_format=mp3_44100_128','-H','Content-Type: application/json','-d',body],capture_output=True,text=True)
    d=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',k+'.mp3'],capture_output=True,text=True).stdout.strip()
    print(k,r.stdout,d)
