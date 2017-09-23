
def runMysq():
    import pymysql
    ## 打印数据库的版本信息
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")   # 打开数据库连接
    cursor = db.cursor()        # 使用 cursor()方法创建一个游标对象cursor
    cursor.execute("SELECT VERSION()")    # 使用 execute()方法执行 SQL 查询 
    data = cursor.fetchone()    # 使用 fetchone()方法获取单条数据
    print ("Database version : %s " % data)
    db.close()
    
    ## 创建表
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")   # 打开数据库连接
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE") # 使用 execute()方法执行 SQL，如果表存在则删除
    # 使用预处理语句创建表
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)
    db.close()'''
    
    ## 插入数据的操作
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")   # 打开数据库连接
    cursor = db.cursor()
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
    ''
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    ''
    try:
        cursor.execute(sql)  # 执行SQL插入语句
        db.commit()          # 提交到数据库执行
    except:
        db.rollback()        # 如果发生错误则回滚
    db.close()'''
    
    ## 查询数据库
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE \
           WHERE INCOME > '%d'" % (1000)
    try:
        cursor.execute(sql)
        results = cursor.fetchall() # 获取所有记录列表
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print ("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % \
                  (fname, lname, age, sex, income ))
    except:
        print ("Error: unable to fetch data")
    
    db.close()'''
    
    ## 更新数据库
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    
    # SQL 更新语句
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                              WHERE SEX = '%c'" % ('M')
    try:
        cursor.execute(sql)
        db.commit()  # 提交到数据库执行
    except:
        db.rollback()
    
    db.close()'''
    
    ## 删除表内容的操作
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    
    db.close()
    pass

if __name__ == '__main__':
    runMysq()
    input("Press any key to continue...")
    pass