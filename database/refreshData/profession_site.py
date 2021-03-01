# 岗位数据，增加岗位类型数据
# @Author ZhangGJ
# @Date 2021/03/01 16:15

import pymysql
import time
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='114.115.207.20', port=3506, user='root', passwd='Seeyouagain2020.',
                       db='qhdbank', charset='utf8')
cur = conn.cursor(DictCursor)

profession_site_update_query = 'update profession_site set profession_type = 0 where 1 = 1'
cur.execute(profession_site_update_query)

profession_site_select_query = 'select * from profession_site'
cur.execute(profession_site_select_query)
profession_site_list = cur.fetchall()
for profession_site in profession_site_list:
    profession_site_dict = dict(profession_site)
    profession_site_insert_query = 'INSERT INTO `profession_site` ( `profession_id`, `place_id`, ' \
                                   '`profession_type`, `create_at`) VALUES(%s, %s, %s, %s) '
    cur.execute(profession_site_insert_query, (profession_site_dict.get('profession_id'),
                                               profession_site_dict.get('place_id'), 1,
                                               time.strftime("%Y-%m-%d %H:%M:%S",
                                                             time.localtime())))
cur.close()
conn.commit()
conn.close()
