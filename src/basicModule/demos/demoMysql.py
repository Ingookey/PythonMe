
def runMysq():
    import pymysql
    ## ��ӡ���ݿ�İ汾��Ϣ
    db = pymysql.connect("localhost", "root", "hsq888", "testschema")   # �����ݿ�����
    cursor = db.cursor()        # ʹ�� cursor()��������һ���α����cursor
    cursor.execute("SELECT VERSION()")    # ʹ�� execute()����ִ�� SQL ��ѯ 
    data = cursor.fetchone()    # ʹ�� fetchone()������ȡ��������
    print ("Database version : %s " % data)
    db.close()
    
    ## ������
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")   # �����ݿ�����
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE") # ʹ�� execute()����ִ�� SQL������������ɾ��
    # ʹ��Ԥ������䴴����
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)
    db.close()'''
    
    ## �������ݵĲ���
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")   # �����ݿ�����
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
        cursor.execute(sql)  # ִ��SQL�������
        db.commit()          # �ύ�����ݿ�ִ��
    except:
        db.rollback()        # �������������ع�
    db.close()'''
    
    ## ��ѯ���ݿ�
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE \
           WHERE INCOME > '%d'" % (1000)
    try:
        cursor.execute(sql)
        results = cursor.fetchall() # ��ȡ���м�¼�б�
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
    
    ## �������ݿ�
    '''db = pymysql.connect("localhost", "root", "hsq888", "testschema")
    cursor = db.cursor()
    
    # SQL �������
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                              WHERE SEX = '%c'" % ('M')
    try:
        cursor.execute(sql)
        db.commit()  # �ύ�����ݿ�ִ��
    except:
        db.rollback()
    
    db.close()'''
    
    ## ɾ�������ݵĲ���
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