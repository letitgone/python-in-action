# 文思刷数据--attribute3
# @Author ZhangGJ
# @Date 2021/03/24 11:22

import cx_Oracle
import pymysql
from pymysql.cursors import DictCursor
import json

oracle_conn = cx_Oracle.connect("Hifm", "123456", "localhost:1111/test")

oracle_curs = oracle_conn.cursor()
oracle_sql = "SELECT asset_code FROM cux.CUX_FA_AMS_ASSET_ADD where attribute4 = 'HIFM' and  attribute3 = 'Y' "

mysql_conn = pymysql.connect(host='localhost', port=3306, user='root',
                             passwd='123456', db='123', charset='utf8')
mysql_cur = mysql_conn.cursor(DictCursor)

rr = oracle_curs.execute(oracle_sql)
oracle_row = oracle_curs.fetchmany()
for add in oracle_row:
    print(f"===========ORACLE台账CODE:{add}")
    mysql_sql = "select financial_no, assetfinances_attributes ->> '$.planuseYearFinance.value' as planuseYearFinance from assetfinances where financial_no = %s"
    mysql_cur.execute(mysql_sql, add)
    asset_ledger_dict = mysql_cur.fetchone()
    print(f"===========MYSQL台账属性:{asset_ledger_dict}")
    planuseYearFinance = asset_ledger_dict.get('planuseYearFinance')
    num = int(planuseYearFinance)
    asset_code = asset_ledger_dict.get('financial_no')
    oracle_update_sql = "update CUX.CUX_FA_AMS_ASSET_ADD set LIFE_IN_MONTHS = :num where ASSET_CODE = :asset_code "
    oracle_curs.execute(oracle_update_sql, {'num': num, 'asset_code': asset_code})
    print(f"===========更新ORACLE LIFE_IN_MONTHS属性！")

mysql_cur.close()
mysql_conn.commit()
mysql_conn.close()

oracle_curs.close()
oracle_conn.commit()
oracle_conn.close()
