import pymysql


password = "mysqltrysqlnewmysqlsthsql530530%:)ok"
with pymysql.connect(
    host="localhost", user="root", password=password, port=3306, db="school"
) as db:
    cursor = db.cursor()

    update_age_sql = "UPDATE students SET age = %s WHERE name = %s"
    try:
        # 自动转换类型
        cursor.execute(update_age_sql, (19, "Bob"))
        db.commit()
    except Exception as e:
        db.rollback()
        print(e.args)
