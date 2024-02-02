from gtts import gTTS

tts = gTTS(text="음성 내용을 입력중입니다.", lang="ko")
tts.save("output.mp3")