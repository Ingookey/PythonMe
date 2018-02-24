import pymysql


def runMysql():
    '''
    db = pymysql.connect("localhost", "root", "hsq888",
                         "testschema")   # �����ݿ�����
    cursor = db.cursor()        # ʹ�� cursor()��������һ���α����cursor
    cursor.execute("SELECT VERSION()")    # ʹ�� execute()����ִ�� SQL ��ѯ
    data = cursor.fetchone()    # ʹ�� fetchone()������ȡ��������
    print("[runMysql] Database version : {}".format(data))
    db.close() #'''

    # create table in database.
    '''
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    # ʹ�� execute()����ִ�� SQL������������ɾ��
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # ʹ��Ԥ������䴴����
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)
    db.close()  # '''

    # insert data into table
    '''
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
        ('Mac', 'Mohan', 20, 'M', 2000)
    ''
    sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    ''
    try:
        cursor.execute(sql1)
        db.commit()          # �ύ�����ݿ�ִ��
    except:
        db.rollback()        # �������������ع�
    db.close()  # '''

    # query table
    '''
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE \
           WHERE INCOME > '%d'" % (1000)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()  # ��ȡ���м�¼�б�
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" %
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")
    db.close()  # '''

    # update table
    #'''
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                              WHERE SEX = '%c'" % ('M')
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()  # '''

    # delete content in table
    #'''
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
    pass  # '''


if __name__ == '__main__':
    runMysql()
    input("Press any key to continue...")
    pass
