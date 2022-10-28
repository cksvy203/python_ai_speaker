import speech_recognition as sr

# 마이크에서 입력된 소리 신호를 텍스트로 변환
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("듣고있어요.")
    audio = r.listen(source)

# 마이크에서 입력된 소리를 WAV 파일로 저장
with open("test.wav", "wb") as f:
    f.write(audio.get_wav_data())

    # 오디오를 raw 데이터 형식으로 불러오기
    audio.get_raw_data()