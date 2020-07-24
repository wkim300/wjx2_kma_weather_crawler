import sys
import time
import datetime
from datetime import timedelta

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib

import json
import csv


# swjcities = ['강원도 북강릉(104)', '강원도 강릉(105)', '강원도 속초(90)', '강원도 동해(106)',
#     '강원도 영월(121)', '강원도 원주(114)', '강원도 인제(211)', '강원도 정선군(217)',
#     '강원도 철원(95)', '강원도 북춘천(93)', '강원도 춘천(101)', '강원도 태백(216)',
#     '강원도 대관령(100)', '강원도 홍천(212)', '경기도 동두천(98)', '경기도 수원(119)',
#     '경기도 양평(202)', '경기도 이천(203)', '경기도 파주(99)', '경상남도 거제(294)',
#     '경상남도 거창(284)', '경상남도 김해시(253)', '경상남도 남해(295)', '경상남도 밀양(288)',
#     '경상남도 산청(289)', '경상남도 양산시(257)', '경상남도 의령군(263)', '경상남도 진주(192)',
#     '경상남도 창원(155)', '경상남도 북창원(255)', '경상남도 통영(162)', '경상남도 함양군(264)',
#     '경상남도 합천(285)', '경상북도 경주시(283)', '경상북도 구미(279)', '경상북도 문경(273)',
#     '경상북도 봉화(271)', '경상북도 상주(137)', '경상북도 안동(136)', '경상북도 영덕(277)',
#     '경상북도 영주(272)', '경상북도 영천(281)', '경상북도 울릉도(115)', '경상북도 울진(130)',
#     '경상북도 의성(278)', '경상북도 청송군(276)', '경상북도 포항(138)', '광역/특별시 광주(156)',
#     '광역/특별시 대구(143)', '광역/특별시 대전(133)', '광역/특별시 부산(159)',
#     '광역/특별시 서울(108)', '광역/특별시 세종(239)', '광역/특별시 울산(152)',
#     '광역/특별시 강화(201)', '광역/특별시 백령도(102)', '광역/특별시 인천(112)',
#     '전라남도 강진군(259)', '전라남도 고흥(262)', '전라남도 광양시(266)', '전라남도 목포(165)',
#     '전라남도 보성군(258)', '전라남도 순천(174)', '전라남도 흑산도(169)', '전라남도 여수(168)',
#     '전라남도 영광군(252)', '전라남도 완도(170)', '전라남도 장흥(260)', '전라남도 진도군(268)',
#     '전라남도 해남(261)', '전라북도 고창군(251)', '전라북도 고창(172)', '전라북도 군산(140)',
#     '전라북도 남원(247)', '전라북도 부안(243)', '전라북도 순창군(254)', '전라북도 임실(244)',
#     '전라북도 장수(248)', '전라북도 전주(146)', '전라북도 정읍(245)', '제주도 성산(188)',
#     '제주도 서귀포(189)', '제주도 제주(184)', '제주도 고산(185)', '충청남도 금산(238)',
#     '충청남도 보령(235)', '충청남도 부여(236)', '충청남도 서산(129)', '충청남도 천안(232)',
#     '충청남도 홍성(177)', '충청북도 보은(226)', '충청북도 추풍령(135)', '충청북도 제천(221)',
#     '충청북도 청주(131)', '충청북도 충주(127)']

swjcities = ['강원도 춘천(101)','경기도 수원(119)', '경상남도 거제(294)', '경상북도 문경(273)',
    '광역/특별시 광주(156)', '전라남도 영광군(252)', '전라북도 정읍(245)', '제주도 성산(188)',
    '충청남도 보령(235)', '충청북도 보은(226)']

# swjcities = ['강원도 춘천(101)','경기도 수원(119)', '충청북도 보은(226)']

swjcitynum_list=[]
swjcityname_list=[]

for swji in range(0,len(swjcities)) :

    # swjcityname = swjcities[swji][swjcities[swji].find(' ')+1:]
    swjcityname = swjcities[swji]
    swjindex1 = swjcityname.find('(')
    swjindex2 = swjcityname.find(')')
    swjcitynum = swjcityname[swjindex1+1:swjindex2]

    swjcitynum_list.append(swjcitynum)
    swjcityname_list.append(swjcityname[0:swjindex1])


swjurl = 'https://data.kma.go.kr/apiData/getData'

def swjparam(pagenum, TargetYr, swjcitynum_param) :
    
    swjparams = '?' + urlencode({
        quote_plus("type"): "json",
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "HR",
        quote_plus("startDt"): str(TargetYr)+"0101",
        quote_plus("startHh"): "00",
        quote_plus("endDt"): str(TargetYr)+"1231",
        quote_plus("endHh"): "23",
        quote_plus("stnIds"): str(swjcitynum_param),
        quote_plus("schListCnt"): "900",
        # quote_plus("schListCnt"): "24",
        quote_plus("pageIndex"): str(pagenum),
        quote_plus("apiKey"): "XwYDQmezGv/fV1d/9NO68o5td/%2Bj3VoOQOaWMgF0xv%2B25yk%2BlxzS8quxVjBQ8VqW"
    })
    return swjparams


swjvarlist = ['tm', 'ta', 'hm', 'pa', 'wd','ws', 'icsr']
missingvalues = {"ta":99.9 , "hm":999, "pa":9999.99, "wd":999, "ws":999, "icsr":0}

# for swjc in swjvarlist : 
#     locals()['swj' + swjc] = []

for swjcity in swjcitynum_list :

    # for swjj in swjvarlist : 
    #     locals()['swj' + swjj + str(swjcity)] = []
    varname = 'swjraw' + str(swjcity)
    locals()[varname] = []

    for swjyear in range(2015,2020) :

        for swjpage in range(1,11) :

            swjparams = swjparam(swjpage, swjyear, swjcity)
            # print(swjurl+unquote(swjparams))

            swjreq = urllib.request.Request(swjurl+unquote(swjparams))
            
            swjdata=[]
            while len(swjdata) < 1 : 
                print('Year : ' + str(swjyear) + ' // City : ' + str(swjcity) + ' // Page : ' + str(swjpage) + "of 10")
                response_body = urlopen(swjreq, timeout = 120).read()
                swjdata = json.loads(response_body)[3]['info']
                time.sleep(0.1)

            # response_body = urlopen(swjreq, timeout = 120).read()
            # print('Year : ' + str(swjyear) + ' // City : ' + str(swjcity) + ' // Page : ' + str(swjpage) + "of 10")
            # swjdata = json.loads(response_body)[3]['info']
            
            locals()[varname].append(swjdata)

            # for swjvar in swjvarlist : 
            #     for swji in range(0, len(swjdata)) : 
                    # try : 
                    #     locals()['swj' + swjvar + str(swjcity)].append(swjdata[swji][swjvar.upper()])
                    # except KeyError :
                    #     locals()['swj' + swjvar + str(swjcity)].append(missingvalues[swjvar])

            # time.sleep(0.1)
    
    
    varname_all = varname + '_all'
    locals()[varname_all] = []

    for swjvar in swjvarlist : 
        varname2 = varname + '_' + swjvar
        
        locals()[varname2] = []
        

        for swji in range(0, len(locals()[varname])) : 
            for swjk in range(0, len(locals()[varname][swji])) : 
                # locals()[varname2].append(locals()[varname][swji][swjk][swjvar.upper()])
                try : 
                    locals()[varname2].append(locals()[varname][swji][swjk][swjvar.upper()])
                except KeyError :
                    locals()[varname2].append(missingvalues[swjvar])

        locals()[varname_all].append(locals()[varname2])
        del locals()[varname2]
    
    varname_all2 = varname_all+'2'
    locals()[varname_all2] = [list(locals()[varname_all2]) for locals()[varname_all2] in zip(*locals()[varname_all])]
    del locals()[varname_all]

    # pre_hournum = 23
    # locals()[varname_all2 + '_err_index'] = []
    # locals()[varname_all2 + '_diff_index'] = []
    # for swji in range(0,len(locals()[varname_all2])) : 
    #     current_hournum = locals()[varname_all2][swji][0][11:13]
    #     hourdiff = int(current_hournum) - pre_hournum
    #     if ((hourdiff != -23) and (hourdiff != 1)) : 
    #         locals()[varname_all2 + '_err_index'].append(swji)
    #         locals()[varname_all2 + '_diff_index'].append(hourdiff)
    #     pre_hournum = int(current_hournum)


    # datetime method start
    locals()[varname_all2 + '_err_index'] = []
    locals()[varname_all2 + '_diff_index'] = []
    for swji in range(1,len(locals()[varname_all2])) : 
        
        current_hournum = datetime.datetime.strptime(locals()[varname_all2][swji][0], '%Y-%m-%d %H:%M')
        pre_hournum = datetime.datetime.strptime(locals()[varname_all2][swji-1][0], '%Y-%m-%d %H:%M')

        td = current_hournum - pre_hournum

        hourdiff = (td.seconds)/3600

        if (hourdiff != 1) : 
            locals()[varname_all2 + '_err_index'].append(swji)
            locals()[varname_all2 + '_diff_index'].append(int(hourdiff))
        pre_hournum = current_hournum
    # datetime method end


# for swjvar in swjvarlist : 
#     for swjcity in swjcitynum_list : 
#         locals()['swj' + swjvar].append(locals()['swj'+swjvar+str(swjcity)])
#         locals()['swj' + swjvar + '_all'] = [list(locals()['swj' + swjvar + '_all']) for locals()['swj' + swjvar + '_all'] in zip(*locals()['swj' + swjvar])]
#         # locals()['swj' + swjvar + '_all'] = []
#         # locals()['swj' + swjvar] = []

'''awefawefawefawef'''        