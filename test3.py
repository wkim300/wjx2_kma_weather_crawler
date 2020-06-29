

import time
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import csv


### REST API REQUEST구문 기본설정부분 

def swjparam(pagenum):
    
    swjpage = pagenum

    swjparams = '?' + urlencode({
        quote_plus("type"): "json",
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "HR",
        quote_plus("startDt"): "20190101",
        quote_plus("startHh"): "00",
        quote_plus("endDt"): "20191231",
        quote_plus("endHh"): "23",
        quote_plus("stnIds"): "108",
        quote_plus("schListCnt"): "24",
        quote_plus("pageIndex"): str(swjpage),
        quote_plus("apiKey"): "XwYDQmezGv/fV1d/9NO68o5td/%2Bj3VoOQOaWMgF0xv%2B25yk%2BlxzS8quxVjBQ8VqW"
    })
    
    return swjparams

##########################################



### KMA OPEN API 조회

swjdata = {}
swjurl = 'https://data.kma.go.kr/apiData/getData'

for swji in range(1,4):

    swjparams = swjparam(swji)

    swjreq = urllib.request.Request(swjurl+unquote(swjparams))

    response_body = urlopen(swjreq, timeout = 60).read()
    response_body
    swjdata[swji] = json.loads(response_body)
    
    print("Day" + str(swji))
    
    time.sleep(0.5)

#########################################################################




### 파싱된 JSON을 측정값별 리스트 분리

swjta=[] # 기온 T air
swjhm=[] # 습도 Humidity
swjwd=[] # 풍향 Wind direction
swjws=[] # 풍속 Wind speed
swjicsr=[] # 전일사량
swjpa = [] # 현지기압 pascal





swjvarlist = ['ta', 'hm', 'pa', 'wd','ws', 'icsr']

# for varnames in swjvarlist:
#     locals()['swj'+varnames] = varnames.upper()


for swjday in range(1,366):
    for swjhour in range(0,24):
                
        for swjvars in swjvarlist:
            try :
                globals()['swj'+swjvars].append(swjdata[swjday][3]['info'][swjhour][swjvars.upper()])
            except KeyError :
                globals()['swj'+swjvars].append(0)




### 온도, 습도, 현지기압, 풍향, 풍속, 전일사량 합치기 및 transpose

swjicsr = [num*277.7778 for num in swjicsr]

swj2 = [swjta, swjhm, swjpa, swjwd, swjws, swjicsr]
swj3 = [list(swj3) for swj3 in zip(*swj2)]

###################################################################



### CSV out 

swjheader = ['Tair', 'Humidity', 'Pressure', 'WindDirection', 'WindSpeed', 'GlobalRadiation']

f = open('output_weather.csv','w', encoding='utf-8', newline='')
wr = csv.writer(f)

wr.writerow(swjheader)

for swji in range(0,len(swj3)):
    wr.writerow(swj3[swji])

##########################################################################

print("CSV Out Done.")

f.close()

print("CSV file closed.")