# random rest api
# a = 'https://thiswouldbemyurl.com'
#urllib3 + poolmanager for requests

import urllib3
import json

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


api = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=종로구&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=rtt6tTRtMnd9M2bCaMZroPU33rPwsFXdLPJ4C4GtuAS9RwoOFBjSIHS1V3%2BVvUNmKALzrC0UQ%2BfesgVZ2yULmg%3D%3D&ver=1.3&_returnType=json"

# api = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=JRG&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=rtt6tTRtMnd9M2bCaMZroPU33rPwsFXdLPJ4C4GtuAS9RwoOFBjSIHS1V3%2BVvUNmKALzrC0UQ%2BfesgVZ2yULmg%3D%3D&ver=1.3&_returnType=json"

"""
print("API_UTL=", type(api_url))
api = api_url.encode('utf-8')
print("API=", type(api))
"""
print(api)

http = urllib3.PoolManager()
print
result = http.request('GET', api)
json.loads(result.data.decode('utf-8'))

with open('data.txt', 'w+') as f:
    json.dump(data, f, ensure_ascii=False)
