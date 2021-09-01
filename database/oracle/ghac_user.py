# @Author ZhangGJ
# @Date 2021/07/14 11:37
import cx_Oracle

oracle_conn = cx_Oracle.connect("root", "123456", "127.0.0.1")
oracle_curs = oracle_conn.cursor()
oracle_sql = "SELECT * FROM ps_ghac_ai_emp"
oracle_row = oracle_curs.fetchmany()
print(oracle_row)
oracle_curs.close()
oracle_conn.commit()
oracle_conn.close()
