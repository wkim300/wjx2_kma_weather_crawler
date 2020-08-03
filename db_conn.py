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
        VALUES (?, ?, ?, ?, ?, ?)", l)

    # 접속해제
    conn.close()


if __name__ == "__main__":
    initialize_db()
