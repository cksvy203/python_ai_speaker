import requests
import sys


# 함수 정의부
def clova_stt(clova_id, clova_secret, stype, data):
    if stype == 'file':
        filename = data
        with open(filename, "rb") as fp:
            audio = fp.read()
    else:
        audio =data
        
    headers = {
        "X-NCP-APIGW-API-KEY-ID": clova_id,
        "X-NCP-APIGW-API-KEY": clova_secret,
        "Content-Type": "application/octet-stream"
    }
    #네이버 클로바 API 언어
    lang = "Kor" # 언어 코드 ( Kor )

    # 클로바 음성 url
    clova_speech_url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    # 클로바 음성 api 요청
    res = requests.post(clova_speech_url, headers=headers, data=audio)
    # 요청에 실패했다면,
    if res.status_code != 200:
        text=""
        print("error! because ",  res.json())
    else: # 성공했다면,
    	#print("음성인식 결과 : ", res.text)
        #print("시작위치 : ", res.text.index('{"type":"finalResult"'))
        #print("종료위치 : ", res.text.rindex('}')+1)
        #print("추출한 정보 : ", res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1])
        result = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        text = json.loads(result).get('value')

    return text

# 함수 호출부
clova_id = "rar2f3xqjq"
clova_secret = "GEN2mz8q0NbRbcdNySHc8D5jPJbifRANJLgqexG4"
AUDIO_FILE = "C:/Users/WIN10/Desktop/python_ai_speaker/hello.mp3"
text = clova_stt(clova_id, clova_secret, "file", AUDIO_FILE)
print(text)