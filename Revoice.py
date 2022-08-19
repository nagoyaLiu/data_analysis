import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("10.wav") as source:
    audio = r.record(source)

text = r.recognize_google(audio,language='ja-JP')
print(text)

# f = open('voice.txt','w')
# f.write(text)
# f.close()