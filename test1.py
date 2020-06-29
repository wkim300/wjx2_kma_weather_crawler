

# swjheader = [['Tair', 'Humidity', 'Pressure', 'WindDirection', 'WindSpeed', 'GlobalRadiation'], ['aa', 'bb','cc','dd','ee']]



# swjheader = [ ['LOCATION,INCHON,-,KOR,IWEC Data,471120,37.48,126.55,9,70'],
#     ['DESIGN CONDITIONS,3,Climate Design Data 2013 ASHRAE Handbook,Heating,1.0,-10.1,-8.2,-20.3,0.6,-7.7,-18.4,0.7,-6.0,12.0,-1.9,10.0,-2.5,4.0,0.0,Cooling,8.0,5.7,30.9,24.6,29.6,23.8,28.5,23.1,25.7,29.0,25.1,28.0,24.5,27.2,2.8,290.0,24.8,20.0,27.5,24.2,19.3,26.9,23.6,18.6,26.4,79.9,29.0,77.2,28.1,74.8,27.3,737.0,Extremes,9.2,7.7,6.5,29.6,-12.3,32.9,2.5,1.8,-14.1,34.3,-15.6,35.3,-17.0,36.4,-18.8,37.7'],
#     ['TYPICAL/EXTREME PERIODS,6,Summer - Week Nearest Max Temperature For Period,Extreme,7/29,8/ 4,Summer - Week Nearest Average Temperature For Period,Typical,8/19,8/25,Winter - Week Nearest Min Temperature For Period,Extreme,1/ 8,1/14,Winter - Week Nearest Average Temperature For Period,Typical,2/19,2/25,Autumn - Week Nearest Average Temperature For Period,Typical,11/26,12/ 2,Spring - Week Nearest Average Temperature For Period,Typical,5/13,5/19'],
#     ['GROUND TEMPERATURES,4,0.5,,,,-0.39,1.91,6.41,10.66,18.7,22.94,24.11,21.96,17,10.81,4.72,0.7,2,,,,2.79,3.35,5.91,8.76,14.95,18.9,20.87,20.43,17.6,13.33,8.52,4.74,4,,,,6.08,5.68,6.8,8.42,12.51,15.57,17.55,18.04,16.8,14.28,11.02,8.08,,,,,,,,,,,,,,,,'],
#     ['HOLIDAYS/DAYLIGHT SAVINGS,No,0,0,32,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'],
#     ['COMMENTS 1,opyplus version 1.0.3 - copyright (c) 2020 - Openergy development team ; ###############################################################################################################################################################################################################################################################'],
#     ['COMMENTS 2,-- Ground temps produced with a standard soil diffusivity of 2.3225760E-03 {m**2/day}'],
#     ['DATA PERIODS,1,1,,Sunday,1/1,12/31']]

import csv

with open('header_base.epw', 'r') as headerf:
    swjheader = headerf.readlines()

# with open('swjweather.csv','r') as weatherf:
#     weatherdata = weatherf.readlines()

# with open('weathertest.epw', 'w') as epwf :
    
#     for headerlines in swjheader :
#         epwf.write(headerlines)

#     # for weatherlines in weatherdata :
#     #     epwf.write(weatherlines)

with open('epwdatabase.csv', 'r') as f :
    swjdatapart = []
    reader = csv.reader(f)
    for swjdatalines in reader :
        swjdatapart.append(swjdatalines)

swjdatapart2 = [list(swjdatapart2) for swjdatapart2 in zip(*swjdatapart)]

swjdatapart3 = [list(swjdatapart3) for swjdatapart3 in zip(*swjdatapart2)]

with open('csvouttest.epw','w') as swjf :
    for headerlines in swjheader :
        swjf.write(headerlines)

with open('swjdatapart_csv.csv','w', encoding='utf-8', newline='') as f :
    wr = csv.writer(f)
    for swji in range(0,len(swjdatapart3)) :
        wr.writerow(swjdatapart3[swji])

with open('swjdatapart_csv.csv','r') as f2 : 
    swjdatapart_csv = f2.readlines()

with open('csvouttest.epw', 'a') as swjf2 :
    for datalines in swjdatapart_csv : 
        swjf2.write(datalines)
