import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


import time
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import csv


form_class = uic.loadUiType("uitest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 할당하는 코드
        self.swjbtn1.clicked.connect(self.swjbtn1Fn)
        self.swjbtn2.clicked.connect(self.swjbtn2Fn)
        self.swjbtn3.clicked.connect(self.swjbtn3Fn)

    def swjparam(self, pagenum):
    
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

    def swjbtn1Fn(self) :
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드
        #self.swjlabel.setText("swjbtn1 click")
        
        # global swjdata

        self.swjdata = {}
        swjurl = 'https://data.kma.go.kr/apiData/getData'

        for swji in range(1,11):

            swjparams = self.swjparam(swji)

            swjreq = urllib.request.Request(swjurl+unquote(swjparams))

            response_body = urlopen(swjreq, timeout = 60).read()
            response_body
            
            self.swjdata[swji] = json.loads(response_body)
            
            # print("Day" + str(swji))
            QApplication.processEvents()
            self.swjlabel.setText("Day"+str(swji))
            self.swjlabel.repaint()
            
            

            time.sleep(0.5)
        
        


    
    def swjbtn2Fn(self) :
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드

        # global swjdata
        # global swj3

        swjta=[] # 기온 T air
        swjhm=[] # 습도 Humidity
        swjwd=[] # 풍향 Wind direction
        swjws=[] # 풍속 Wind speed
        swjicsr=[] # 전일사량
        swjpa = [] # 현지기압 pascal

        swjvarlist = ['ta', 'hm', 'pa', 'wd','ws', 'icsr']

        for swjday in range(1,366):
            for swjhour in range(0,24):
                        
                for swjvars in swjvarlist:
                    try :
                        locals()['swj'+swjvars].append(self.swjdata[swjday][3]['info'][swjhour][swjvars.upper()])
                    except KeyError :
                        locals()['swj'+swjvars].append(0)

        ### 온도, 습도, 현지기압, 풍향, 풍속, 전일사량 합치기 및 transpose

        swjicsr = [num*277.7778 for num in swjicsr]

        swj2 = [swjta, swjhm, swjpa, swjwd, swjws, swjicsr]
        self.swj3 = [list(swj3) for swj3 in zip(*swj2)]

        self.swjlabel.setText("Post process done.")


    def swjbtn3Fn(self) :
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드

        # global swj3

        swjheader = ['Tair', 'Humidity', 'Pressure', 'WindDirection', 'WindSpeed', 'GlobalRadiation']

        f = open('output_weather2.csv','w', encoding='utf-8', newline='')
        wr = csv.writer(f)

        wr.writerow(swjheader)

        for swji in range(0,len(self.swj3)):
            wr.writerow(self.swj3[swji])

        ##########################################################################

        self.swjlabel.setText("CSV Out Done.")

        f.close()

        self.swjlabel.setText("CSV file closed.")        


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()