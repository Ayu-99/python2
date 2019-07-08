from gtts import gTTS
tts = gTTS('Hello', lang='en')
tts.save('hello2.mp3')
print("File created")

