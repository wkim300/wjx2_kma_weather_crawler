import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
# from PyQt5.QtCore import pyqtSignal, pyqtSlot
# from PyQt5.QtWidgets import QApplication, QMainWindow
# This is WK
# This is swj
# This is wjwjwjwjwjwjwj

import time
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import json
import csv

# import requests

form_class = uic.loadUiType("uitest.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        swjwidth = self.frameGeometry().width()
        swjheight = self.frameGeometry().height()

        pixmap_ep = QPixmap("eplogo.jpg")
        pixmap_ep = pixmap_ep.scaledToHeight(60)
        self.eplogolbl.setPixmap(QPixmap(pixmap_ep))

        pixmap_db = QPixmap("dblogo.jpg")
        pixmap_db = pixmap_db.scaledToHeight(45)
        self.dblogolbl.setPixmap(QPixmap(pixmap_db))

        self.setFixedSize(swjwidth,swjheight)

        swjcities = ['강원도 북강릉(104)', '강원도 강릉(105)', '강원도 속초(90)', '강원도 동해(106)',
            '강원도 영월(121)', '강원도 원주(114)', '강원도 인제(211)', '강원도 정선군(217)',
            '강원도 철원(95)', '강원도 북춘천(93)', '강원도 춘천(101)', '강원도 태백(216)',
            '강원도 대관령(100)', '강원도 홍천(212)', '경기도 동두천(98)', '경기도 수원(119)',
            '경기도 양평(202)', '경기도 이천(203)', '경기도 파주(99)', '경상남도 거제(294)',
            '경상남도 거창(284)', '경상남도 김해시(253)', '경상남도 남해(295)', '경상남도 밀양(288)',
            '경상남도 산청(289)', '경상남도 양산시(257)', '경상남도 의령군(263)', '경상남도 진주(192)',
            '경상남도 창원(155)', '경상남도 북창원(255)', '경상남도 통영(162)', '경상남도 함양군(264)',
            '경상남도 합천(285)', '경상북도 경주시(283)', '경상북도 구미(279)', '경상북도 문경(273)',
            '경상북도 봉화(271)', '경상북도 상주(137)', '경상북도 안동(136)', '경상북도 영덕(277)',
            '경상북도 영주(272)', '경상북도 영천(281)', '경상북도 울릉도(115)', '경상북도 울진(130)',
            '경상북도 의성(278)', '경상북도 청송군(276)', '경상북도 포항(138)', '광역/특별시 광주(156)',
            '광역/특별시 대구(143)', '광역/특별시 대전(133)', '광역/특별시 부산(159)',
            '광역/특별시 서울(108)', '광역/특별시 세종(239)', '광역/특별시 울산(152)',
            '광역/특별시 강화(201)', '광역/특별시 백령도(102)', '광역/특별시 인천(112)',
            '전라남도 강진군(259)', '전라남도 고흥(262)', '전라남도 광양시(266)', '전라남도 목포(165)',
            '전라남도 보성군(258)', '전라남도 순천(174)', '전라남도 흑산도(169)', '전라남도 여수(168)',
            '전라남도 영광군(252)', '전라남도 완도(170)', '전라남도 장흥(260)', '전라남도 진도군(268)',
            '전라남도 해남(261)', '전락북도 고창군(251)', '전락북도 고창(172)', '전락북도 군산(140)',
            '전락북도 남원(247)', '전락북도 부안(243)', '전락북도 순창군(254)', '전락북도 임실(244)',
            '전락북도 장수(248)', '전락북도 전주(146)', '전락북도 정읍(245)', '제주도 성산(188)',
            '제주도 서귀포(189)', '제주도 제주(184)', '제주도 고산(185)', '충청남도 금산(238)',
            '충청남도 보령(235)', '충청남도 부여(236)', '충청남도 서산(129)', '충청남도 천안(232)',
            '충청남도 홍성(177)', '충청북도 보은(226)', '충청북도 추풍령(135)', '충청북도 제천(221)',
            '충청북도 청주(131)', '충청북도 충주(127)']
        
        for cityname in swjcities : 
            swjitem = QListWidgetItem()
            swjitem.setText(cityname)
            self.swjlist.addItem(swjitem)

        #버튼에 기능을 할당하는 코드
        self.swjbtn1.clicked.connect(self.swjbtn1Fn)
        self.swjbtn2.clicked.connect(self.swjbtn2Fn)
        self.swjbtn3.clicked.connect(self.swjbtn3Fn)
        self.testbtn.clicked.connect(self.testbtnFn)
        self.swjlist.itemClicked.connect(self.swjlistFn)

        self.swjbtn1.setDisabled(True)
        self.swjbtn1.setStyleSheet("background-color: rgb(180, 180, 180)")

        self.swjbtn2.setDisabled(True)
        self.swjbtn2.setStyleSheet("background-color: rgb(180, 180, 180)")

        self.swjbtn3.setDisabled(True)
        self.swjbtn3.setStyleSheet("background-color: rgb(180, 180, 180)")

        self.testbtn.setStyleSheet("background-color: rgb(255, 255, 255)")

        
        
        

        # swjitem.setText("aaa")
        # self.swjlist.addItem(swjitem)
        

    def swjlistFn(self) : 
        '''aefaef'''
        text_selected = self.swjlist.currentItem().text()
        self.swjcityname = text_selected[text_selected.find(' ')+1:]

        print(self.swjcityname)
    
    def isleapyear(self, swjyear) : 
        '''awefawef'''
        if ((swjyear % 4 == 0) and (swjyear % 100 != 0)) or (swjyear % 400 == 0) :
            return True
        else : 
            return False

    
    def swjparam(self, pagenum):
        
        swjpage = pagenum
        swjparams = '?' + urlencode({
            quote_plus("type"): "json",
            quote_plus("dataCd"): "ASOS",
            quote_plus("dateCd"): "HR",
            quote_plus("startDt"): str(self.TargetYr)+"0101",
            quote_plus("startHh"): "00",
            quote_plus("endDt"): str(self.TargetYr)+"1231",
            quote_plus("endHh"): "23",
            quote_plus("stnIds"): str(self.swjcitynum),
            quote_plus("schListCnt"): "900",
            # quote_plus("schListCnt"): "24",
            quote_plus("pageIndex"): str(swjpage),
            quote_plus("apiKey"): "XwYDQmezGv/fV1d/9NO68o5td/%2Bj3VoOQOaWMgF0xv%2B25yk%2BlxzS8quxVjBQ8VqW"
        })
        return swjparams

    def testbtnFn(self) :
        '''awefawef'''
        self.TargetYr = self.swjdate.date().year()
        
        self.swjyearlabel.setText("설정 연도 : " + str(self.TargetYr))
        

        swjindex1 = self.swjcityname.find('(')
        swjindex2 = self.swjcityname.find(')')
        self.swjcitynum = self.swjcityname[swjindex1+1:swjindex2]

        self.swjcitylabel.setText("설정 지역 : " + self.swjcityname)

        self.swjbtn1.setEnabled(True)
        self.swjbtn1.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.swjbtn2.setDisabled(True)
        self.swjbtn2.setStyleSheet("background-color: rgb(180, 180, 180)")

        self.swjbtn3.setDisabled(True)
        self.swjbtn3.setStyleSheet("background-color: rgb(180, 180, 180)")
        

    def swjbtn1Fn(self) :
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드
        #self.swjlabel.setText("swjbtn1 click")
        
        # global swjdata

        self.swjlist.setDisabled(True)
        
        self.testbtn.setDisabled(True)
        self.testbtn.setStyleSheet("background-color: rgb(180, 180, 180)")

        self.swjdate.setDisabled(True)

        self.swjdata = {}
        swjurl = 'https://data.kma.go.kr/apiData/getData'

        swjDaysize = 366 if self.isleapyear(self.TargetYr) == True else 365
        self.maxday = swjDaysize
        # swjDaysize = 7
        # print(swjDaysize)

        # for swji in range(1,swjDaysize+1):
        for swji in range(1,11):

            swjparams = self.swjparam(swji)
            print(swjurl+unquote(swjparams))

            self.swjlabel.setText(str(swji) + "/10" + " : 기상청 API 서버 데이터 조회중..")
            self.swjlabel.repaint()
            swjreq = urllib.request.Request(swjurl+unquote(swjparams))

            response_body = urlopen(swjreq, timeout = 120).read()
            response_body
            
            self.swjdata[swji] = json.loads(response_body)
            
            # print("Day" + str(swji))
            QApplication.processEvents()
            swjprogress = (swji/10)*100
            self.swjpbar.setValue(swjprogress)
            self.swjpbar.repaint()
            
            time.sleep(0.1)
        
        self.swjlabel.setText("기상청 API 조회 완료")

        self.swjbtn2.setEnabled(True)
        self.swjbtn2.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.swjbtn3.setEnabled(True)
        self.swjbtn3.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.swjlist.setEnabled(True)
        self.swjdate.setEnabled(True)
        
        self.testbtn.setEnabled(True)
        self.testbtn.setStyleSheet("background-color: rgb(255, 255, 255)")

        
        # print(self.maxday)
        

    
    def swjbtn2Fn(self) :
        
        ### EPW파일 베이스 부분 불러오기/전처리
        with open('header_base.epw', 'r') as headerf:
            swjheader = headerf.readlines()

        if self.isleapyear(self.TargetYr) == True : 
            with open('epwdatabase_leap.csv', 'r') as f :
                swjdatapart = []
                reader = csv.reader(f)
                for swjdatalines in reader :
                    swjdatapart.append(swjdatalines)            
        else : 
            with open('epwdatabase.csv', 'r') as f :
                swjdatapart = []
                reader = csv.reader(f)
                for swjdatalines in reader :
                    swjdatapart.append(swjdatalines)
        
        swjdatapart2 = [list(swjdatapart2) for swjdatapart2 in zip(*swjdatapart)]
        swjdatapart2[0] = [self.TargetYr for swji in swjdatapart2[0]]
        ##########

        ### JSON데이터 후처리 // API데이터 별도 집계 파일용 변수 전처리
        swjta=[] # 기온 T air
        swjhm=[] # 습도 Humidity
        swjwd=[] # 풍향 Wind direction
        swjws=[] # 풍속 Wind speed
        swjicsr=[] # 전일사량
        swjpa = [] # 현지기압 pascal

        swjvarlist = ['ta', 'hm', 'pa', 'wd','ws', 'icsr']
        # swjvarlist = ['ta', 'hm', 'pa', 'wd','ws']
        missingvalues = {"ta":99.9 , "hm":999, "pa":9999.99, "wd":999, "ws":999, "icsr":0}
        # PA는 나중에 단위환산(*100)을 하므로
        # 원래의 missing value에 단위환산계수를 나눈 값을 지정

        for swjday in range(1,11) :
        # for swjday in range(1,int(len(swjdatapart)/24)+1) :

            for swjhour in range(0,len(self.swjdata[swjday][3]['info'])) :
                # print(swjhour)
                for swjvars in swjvarlist:  # ICSR제외 나머지 missing처리
                    try :
                        locals()['swj'+swjvars].append(self.swjdata[swjday][3]['info'][swjhour][swjvars.upper()])
                    except KeyError :
                        locals()['swj'+swjvars].append(missingvalues[swjvars])




            # for swjhour in range(0,24):

            # if swjday == 10 :
            #     '''awefawef'''
            #     for swjhour in range(0,len(self.swjdata[swjday][3]['info'])):
            #         print(swjhour)
            #         for swjvars in swjvarlist:  # ICSR제외 나머지 missing처리
            #             try :
            #                 locals()['swj'+swjvars].append(self.swjdata[swjday][3]['info'][swjhour][swjvars.upper()])
            #             except KeyError :
            #                 locals()['swj'+swjvars].append(missingvalues[swjvars])
            # else : 
            #     '''awefawef'''
            #     len(self.swjdata[swjday][3]['info'])
            #     for swjhour in range(0,len(self.swjdata[swjday][3]['info'])):
            #         print(swjhour)
            #         for swjvars in swjvarlist:  # ICSR제외 나머지 missing처리
            #             try :
            #                 locals()['swj'+swjvars].append(self.swjdata[swjday][3]['info'][swjhour][swjvars.upper()])
            #             except KeyError :
            #                 locals()['swj'+swjvars].append(missingvalues[swjvars])




        swjicsr = [num*277.7778 for num in swjicsr]
        swjpa = [num_pa*100 for num_pa in swjpa]

        swj2 = [swjta, swjhm, swjpa, swjwd, swjws, swjicsr]
        self.swj3 = [list(swj3) for swj3 in zip(*swj2)]
        ##########


        ### EPW파일용 리스트 조립
        swjdatapart2[6] = swjta
        swjdatapart2[8] = swjhm
        swjdatapart2[9] = swjpa
        swjdatapart2[13] = swjicsr
        swjdatapart2[20] = swjwd
        swjdatapart2[21] = swjws

        swjdatapart3 = [list(swjdatapart3) for swjdatapart3 in zip(*swjdatapart2)]

        epwname = "KMA_Weather_Year" + str(self.TargetYr) + "_" + self.swjcityname + ".epw"

        with open(epwname,'w') as swjf :
            for headerlines in swjheader :
                swjf.write(headerlines)        

        with open('swjdatapart_csv.csv','w', encoding='utf-8', newline='') as f :
            wr = csv.writer(f)
            for swji in range(0,len(swjdatapart3)) :
                wr.writerow(swjdatapart3[swji])

        with open('swjdatapart_csv.csv','r') as f2 : 
            swjdatapart_csv = f2.readlines()

        with open(epwname, 'a') as swjf2 :
            for datalines in swjdatapart_csv : 
                swjf2.write(datalines)


        # swjallpart = []
        # swjallpart.append(swjheader)
        # swjallpart.append(swjdatapart3)
        ##########

        self.swjlabel.setText("Post process done.")


    def swjbtn3Fn(self) :

        swjcurrenttime = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
        swjheader = ['Tair', 'Humidity', 'Pressure', 'WindDirection', 'WindSpeed', 'GlobalRadiation']
        swjfilename = "output_weather_" + str(self.TargetYr) + "Yr_" + self.swjcityname + "_" + swjcurrenttime + ".csv"
        f = open(swjfilename,'w', encoding='utf-8', newline='')
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