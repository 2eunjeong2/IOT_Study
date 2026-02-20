import pymysql

# 연결
conn = pymysql.connect(
    host = "localhost",
    user = "pi",
    password = "test1234",
    database = "sensor_db",
    charset = "utf8mb4"
)

# 커서 생성 (딕셔너리 형태로 받기)
cursor = conn.cursor(pymysql.cursors.DictCursor)

# SQL 실행
cursor.execute("SELECT * FROM sensor_data ORDER BY recorded_at DESC LIMIT 5")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()