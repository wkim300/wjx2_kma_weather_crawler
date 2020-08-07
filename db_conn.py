import datetime
import sqlite3


def initialize_db(save_dir='.'):
    # DB 연결 및 저장경로 설정
    conn = sqlite3.connect(save_dir + '/wdb.db',
                           isolation_level=None)  # auto-commit
    c = conn.cursor()

    # 테이블 생성
    # Cities
    c.execute(
        "CREATE TABLE IF NOT EXISTS cities(city_id INTEGER PRIMARY KEY, city_region text, city_name text)")  # AUTOINCREMENT

    c.execute(
        "CREATE TABLE IF NOT EXISTS hourly_data(city_id INTEGER, m_date text, t_air real, h_air real, p_air real, w_dir int, w_speed real, g_rad real, PRIMARY KEY (city_id, m_date))")  # AUTOINCREMENT

    # # 삽입 날짜 생성
    # now = datetime.datetime.now()
    # nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    conn.close()


def execute_data(l, save_dir='.'):
    """[summary]
    Takes in a list of list and puts data into sqlite
    Args:
        l ([type]): [list of list of data in format:
                    [m_date text, t_air real, h_air real, p_air real, w_dir int, w_speed real, g_rad real]
                    ]
    """
    # DB 연결 및 저장경로 설정
    conn = sqlite3.connect(save_dir + '/wdb.db',
                           isolation_level=None)  # auto-commit
    c = conn.cursor()
    # nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    # Many 데이터 삽입
    c.executemany("INSERT INTO hourly_data(m_date, t_air, h_air, p_air, w_dir, w_speed, g_rad) \
        VALUES (?, ?, ?, ?, ?, ?, ?)", l)

    # 접속해제
    conn.close()


if __name__ == "__main__":
    initialize_db()

    # read weather csv file
    import pandas as pd
    # df =  pd.read_csv('119_out.csv', sep='\t')
    # lol = df.values.tolist()
    # print(lol[:5])
    
    # put in data
    # execute_data(lol)


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
    c_regions = []
    c_names = []

    for city in swjcities:
        temp_region, temp_name = city.split()
        c_regions.append(temp_region)
        c_names.append(temp_name)
    print(c_regions)
    print(c_names)