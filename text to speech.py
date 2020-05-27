from gtts import gTTS
import os
text= 'heyy you, i have an good message for that is  always  believe  that  something  wonderful is about  to  happen'
lang= 'en'
speech= gTTS(text= text, lang= lang, slow= True)
speech.save('test.mp3')
os.system('start test.mp3')