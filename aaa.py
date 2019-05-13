from time import sleep

import pymysql

# cursor_db = db.cursor()

IDLE_INTERVAL_IN_SECONDS = 2


def get_data():
    try:
        connect = pymysql.connect("localhost", "root", "", "db_tweepy")
    except:
        # TODO: maybe we should raise new exception?
        # or leave default exception?
        print("Could not open database")
        return
    cur = connect.cursor()
    rows_count = 0
    print(rows_count)
    while True:
        cur.execute("SELECT id, nim FROM tb_mahasiswa ")
        rows_count = cur.rowcount
        if rows_count > 0:
            rows = cur.fetchall()
            for row in rows:
                print("ID = ", row[0])
                print("NIM = ", row[1])
                connect.commit()
        sleep(IDLE_INTERVAL_IN_SECONDS)

if __name__ == "__main__":
    # execute only if run as a script
    get_data()