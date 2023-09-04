from gtts import gTTS #module gtts is used
from playsound import playsound #module playsound is used
audio="speech.mp3"
language='en'
sp=gTTS(text="nani is a good boy",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("********Audio is playing*********")
