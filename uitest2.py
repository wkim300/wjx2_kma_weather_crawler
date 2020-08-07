import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox

import time
import datetime
from datetime import timedelta
import copy

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus

import urllib
import json
import csv

# from PyQt5.QtCore import pyqtSignal, pyqtSlot
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

    def swjlistFn(self) : 
        '''aefaef'''
        text_selected = self.swjlist.currentItem().text()
        self.swjcityname = text_selected[text_selected.find(' ')+1:]
    
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
            quote_plus("pageIndex"): str(swjpage),
            quote_plus("apiKey"): "XwYDQmezGv/fV1d/9NO68o5td/%2Bj3VoOQOaWMgF0xv%2B25yk%2BlxzS8quxVjBQ8VqW"
        })
        return swjparams

    def testbtnFn(self) :
        try : 
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
        except AttributeError : 
            '''awefawef'''
            QMessageBox.about(self,'오류 알림', '좌측 리스트에서 지역을 먼저 선택해주세요        ')
        

    def swjbtn1Fn(self) :

        self.swjlist.setDisabled(True)
        self.testbtn.setDisabled(True)
        self.testbtn.setStyleSheet("background-color: rgb(180, 180, 180)")
        self.swjdate.setDisabled(True)

        
        swjurl = 'https://data.kma.go.kr/apiData/getData'

        swjDaysize = 366 if self.isleapyear(self.TargetYr) == True else 365
        self.maxday = swjDaysize

        varname = 'swjraw' + str(self.swjcitynum)
        locals()[varname] = []

        for swji in range(1,11) :

            swjparams = self.swjparam(swji)
            # print(swjurl+unquote(swjparams))

            self.swjlabel.setText(str(swji) + "/10" + " : 기상청 API 서버 데이터 조회중..")
            self.swjlabel.repaint()
            swjreq = urllib.request.Request(swjurl+unquote(swjparams))
            
            self.swjdata=[]
            while len(self.swjdata) < 1 : 
                print('Year : ' + str(self.TargetYr) + ' // City : ' + str(self.swjcitynum) + ' // Page : ' + str(swji) + "of 10")
                response_body = urlopen(swjreq, timeout = 120).read()
                self.swjdata = json.loads(response_body)[3]['info']
                time.sleep(0.1)
            
            locals()[varname].append(self.swjdata)
            
            QApplication.processEvents()
            swjprogress = (swji/10)*100
            self.swjpbar.setValue(swjprogress)
            self.swjpbar.repaint()

        varname_all = varname + '_all'
        locals()[varname_all] = []

        swjvarlist = ['tm', 'ta', 'hm', 'pa', 'wd','ws', 'icsr']
        missingvalues = {"ta":99.9 , "hm":999, "pa":9999.99, "wd":999, "ws":999, "icsr":0}
        
        for swjvar in swjvarlist : 
            varname2 = varname + '_' + swjvar
            
            locals()[varname2] = []
            

            for swji in range(0, len(locals()[varname])) : 
                for swjk in range(0, len(locals()[varname][swji])) : 
                    try : 
                        locals()[varname2].append(locals()[varname][swji][swjk][swjvar.upper()])
                    except KeyError :
                        locals()[varname2].append(missingvalues[swjvar])

            locals()[varname_all].append(locals()[varname2])
            del locals()[varname2]
        
        varname_all2 = varname_all+'2'
        locals()[varname_all2] = [list(locals()[varname_all2]) for locals()[varname_all2] in zip(*locals()[varname_all])]
        del locals()[varname_all]

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


        ### Missing value insert    
        varname_all3 = varname_all+'3'

        missingvals = [99.9, 999, 9999.99, 999, 999, 0]
        num_prev_inserted = 0

        locals()[varname_all3] = copy.deepcopy(locals()[varname_all2])

        missing_hours_txt = []
        for swja in range(0,len(locals()[varname_all2 + '_err_index'])) : 
                
            num_miss = locals()[varname_all2 + '_diff_index'][swja]
            index_miss = locals()[varname_all2 + '_err_index'][swja] + num_prev_inserted
            time_prev = datetime.datetime.strptime(locals()[varname_all3][index_miss-1][0], '%Y-%m-%d %H:%M')
            
            list_insert = []
            # missing_hours_txt = []
            for swjb in range(1,num_miss) : 
                time_insert = time_prev + datetime.timedelta(hours=swjb)
                time_insert_char = datetime.datetime.strftime(time_insert, '%Y-%m-%d %H:%M')
                missing_hours_txt.append(time_insert_char)
                list_insert.append([time_insert_char] + missingvals)

            list_insert.reverse()

            for swjc in list_insert : 
                locals()[varname_all3].insert(index_miss, swjc)
                num_prev_inserted+=1
        ### insert end

        self.swjraw2 = locals()[varname_all3]
        
        self.swjlabel.setText("기상청 API 조회 완료")
        msgtxt = ''
        linenum = 1
        if len(missing_hours_txt) > 0 :
            for swjmsg in missing_hours_txt : 
                msgtxt = msgtxt + str(linenum) + '. ' + swjmsg + '                                            √' + '\n'
                linenum = linenum + 1
            msgtxt = msgtxt + '\n※ 누락된 시간들의 데이터는 EnergyPlus에서 정의된\n   EPW 누락 데이터 양식에 따라 삽입되었습니다.'
            QMessageBox.about(self, "서버 원본데이터 중 누락된 시간대가 있습니다", msgtxt)
        else : 
            pass


        self.swjbtn2.setEnabled(True)
        self.swjbtn2.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.swjbtn3.setEnabled(True)
        self.swjbtn3.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.swjlist.setEnabled(True)
        self.swjdate.setEnabled(True)
        
        self.testbtn.setEnabled(True)
        self.testbtn.setStyleSheet("background-color: rgb(255, 255, 255)")

        
        # print(self.maxday)
        

##################################################################################################################################


    
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

        swjvarlist = ['ta', 'hm', 'pa', 'wd','ws', 'icsr']
        missingvalues = {"ta":99.9 , "hm":999, "pa":9999.99, "wd":999, "ws":999, "icsr":0}
        # PA는 나중에 단위환산(*100)을 하므로
        # 원래의 missing value에 단위환산계수를 나눈 값을 지정

        self.swjraw3 = [list(self.swjraw3) for self.swjraw3 in zip(*self.swjraw2)]
        # Row-matrix인 swjraw2를 Transpose하여 TA, HM 등 각 변수별로 하나의 List에 위치하도록 조정

        self.swjraw3[6] = [num*277.7778 for num in self.swjraw3[6]]
        self.swjraw3[3] = [num_pa*100 for num_pa in self.swjraw3[3]]
        # 일사량, 현지기압 단위변환

        ### EPW파일용 리스트 조립
        swjdatapart2[6] = self.swjraw3[1] # TA
        swjdatapart2[8] = self.swjraw3[2] # HM
        swjdatapart2[9] = self.swjraw3[3] # PA
        swjdatapart2[13] = self.swjraw3[6] # ICSR
        swjdatapart2[20] = self.swjraw3[4] # WD
        swjdatapart2[21] = self.swjraw3[5] # WS

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

        self.swjlabel.setText("Post process done.")

###################################################################################################################################

    def swjbtn3Fn(self) :

        self.swjraw4 = [list(self.swjraw4) for self.swjraw4 in zip(*self.swjraw3)]
        # 단위변환이 완료된 swjraw3을 CSV-write 하기 위해 다시 Row-matrix로 Transpose하여 swjraw4를 생성

        swjcurrenttime = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
        swjheader = ['Time', 'Tair', 'Humidity', 'Pressure', 'WindDirection', 'WindSpeed', 'GlobalRadiation']
        swjfilename = "output_weather_" + str(self.TargetYr) + "Yr_" + self.swjcityname + "_" + swjcurrenttime + ".csv"
        f = open(swjfilename,'w', encoding='utf-8', newline='')
        wr = csv.writer(f)

        wr.writerow(swjheader)

        for swji in range(0,len(self.swjraw4)):
            wr.writerow(self.swjraw4[swji])

        
        self.swjlabel.setText("CSV Out Done.")

        f.close()

        

        self.swjlabel.setText("CSV file closed.")        



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()