import speech_recognition as sr
import requests

#Clova STT
client_id = "rar2f3xqjq"
client_secret = "GEN2mz8q0NbRbcdNySHc8D5jPJbifRANJLgqexG4"
lang = "Kor" # 언어 코드 ( Kor )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
data = open('C:/Users/WIN10/Desktop/python_ai_speaker/hello.mp3', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)

#함수 정의부
def get_speech():
    # 마이크에서 음성을 추출하는 객체
    recognizer = sr.Recognizer()

    # 마이크 설정
    microphone = sr.Microphone(sample_rate=16000)

    # 마이크 소음 수치 반영
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("소음 수치 반영하여 음성을 청취합니다. {}".format(recognizer.energy_threshold))

        #음성 수집
        with microphone as source:
            print("듣고 있어요, 찬표님.")
            result = recognizer.listen(source)
            audio = result.get_raw_data()

            return audio

            #함수 호출부
            audio = get_speech()
            text = clova_stt("stream", audio)
            print("음성 인식 결과 : " + text)