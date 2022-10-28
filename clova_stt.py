import requests
import json

# 네이버 클로바 클라이언트 정보 입력
client_id = 'rar2f3xqjq'
client_secret = 'GEN2mz8q0NbRbcdNySHc8D5jPJbifRANJLgqexG4'

# 네이버 클로바에 사용할 언어 입력
lang = 'Kor'

# 네이버 클로바 API 주소 입력
url = "https://naveropenapi.apigw-pub.fin-ntruss.com/recog/v1/stt?lang=" + lang

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}



response = requests.post(url, data=audio.get_raw_data, headers=headers)