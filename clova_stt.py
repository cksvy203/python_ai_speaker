import requests
import json
import sys
from speech_recognition import speech_recognition as sr
from playsound import playsound

# 네이버 클로바 API 클라이언트 정보 입력
clova_ID = 'dfmjita8r1'
clova_key = 'xXNAhSUMvBtrKiXCLAQPxa5jkla7xSPlpkSvooVJ'

# 오디오 데이터 불러오기
data = open("wav/hello.wav", "rb")

# 네이버 클로바에 사용할 언어 입력
lang = 'Kor'

# 네이버 클로바 API 주소 입력
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    
headers = {
    "Content-Type": "application/octet-stream", 
    "X-NCP-APIGW-API-KEY-ID": clova_ID,
    "X-NCP-APIGW-API-KEY": clova_key,
}

response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code

#요청시 오류가 발생 했을때
if rescode == 200:
    print (response.text)
    print ("[울프] 안녕하세요. 찬표님, 만나서 반가워요!")
    playsound ('wav/hello.wav')
else:
    print("아쉽게도 인터넷에 연결 되어 있지 않아요. 확인후 다시 시도 해주세요! ")
    playsound("wav/failed_ethernet.wav")
    print("에러 : " + response.text)

    # 마이크에서 입력된 소리 신호를 텍스트로 변환
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("듣고있어요.")
    audio = r.listen(source)

# 마이크에서 입력된 소리를 WAV 파일로 저장
with open("mic_test/test.wav", "wb") as f:
    f.write(audio.get_wav_data())
