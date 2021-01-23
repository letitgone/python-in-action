# @Author ZhangGJ
# @Date 2021/01/12 15:43

import pymysql
import pandas as pd
from sqlalchemy import create_engine

conn = pymysql.connect(host='114.115.207.20', port=3506, user='root', passwd='Seeyouagain2020.',
                       db='hifm_center', charset='utf8')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

role_id_query = "SELECT id FROM ghac.roles WHERE role_code != 'ROLE_001';"
row = cur.execute(role_id_query)  # 返回受影响的行数
role_ids = cur.fetchmany(row)  # 返回数据,返回的是tuple类型
for role_id in role_ids:
    print(role_id['id'])
    insert = cur.execute(
        "INSERT INTO ghac.`role_function` ( `function_id`, `role_id`, `created_at` ) "
        "SELECT id, %s, now() FROM ghac.functions WHERE identify = 'administrator';",
        role_id['id'])
cur.close()
conn.commit()
conn.close()


# engine = create_engine('mysql+pymysql://root:Seeyouagain2020.@114.115.207.20:3506/hifm_center')
#
# role_id_query = "SELECT id FROM ghac.roles WHERE role_code != 'ROLE_001';"
# role_ids = pd.read_sql_query(role_id_query, con=engine)
# role_ids.
# for role_id in role_ids:
#     print(role_id.)
#     insert_sql = "INSERT INTO `role_function` ( `function_id`, `role_id`, `created_at` ) " \
#                  "SELECT id, role_id, now() FROM functions WHERE identify = 'administrator';"
#     print(f"insert role_id:{role_id}")
