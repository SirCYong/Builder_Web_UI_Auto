from Page.random_time import zldtest, close_mysql


def run_sql():
    con, curs = zldtest()
    sql = '''select * from workflow_request'''
    curs.execute(sql)
    con.commit()
    close_mysql(con, curs)
    pass



if __name__ == '__main__':
    run_sql()