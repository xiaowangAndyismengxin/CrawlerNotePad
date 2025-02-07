import pymysql


password = 'mysqltrysqlnewmysqlsthsql530530%:)ok'
with pymysql.connect(host='localhost', user='root', password=password,
                     port=3306, db='game') as db:
    sql = 'SELECT * FROM player WHERE level > 97;'
    cursor = db.cursor()
    cursor.execute(sql)
    print(cursor.rowcount)
    print(type(cursor.fetchone()[-1]))
    print(cursor.fetchmany(7))
    print(cursor.fetchall())
    print(cursor.fetchone())
    cursor.execute('DESC player;')
    print(cursor.fetchall())
