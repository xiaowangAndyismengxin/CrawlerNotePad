import pymysql
import build_sql


password = "mysqltrysqlnewmysqlsthsql530530%:)ok"
with pymysql.connect(
    host="localhost", user="root", password=password, port=3306, db="school"
) as db:
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    print(cursor.fetchone())  # -> tuple[Any, ...] | None
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students(
            id INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(100) NOT NULL,
            AGE TINYINT UNSIGNED NOT NULL
        );
        """
    )

    insert_student_sql = build_sql.insert_sql(
        "students", ["id", "name", "age"], duplicate_key_update=True
    )
    try:
        # 自动转换类型
        cursor.execute(insert_student_sql, (6, "Andy", 29) * 2)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e.args)
