# @Author ZhangGJ
# @Date 2021/01/12 15:43

import pymysql

conn = pymysql.connect(host='localhost', port=3506, user='root', passwd='123456',
                       db='test', charset='utf8')
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