# 岗位数据，增加岗位类型数据
# @Author ZhangGJ
# @Date 2021/03/01 16:15

import pymysql
import time
from pymysql.cursors import DictCursor

tenant_code_list = [
    'sinocanada',
    'weidian',
    'wxyx',
    'xz13861836988',
    # 老大
    'xz13121835907',
    # FCA
    'xz13818840653',
    # 新开库
    'xz18003661831',

    'xz13529385807',
    'xz13572580613',
    'xz13684971060',
    'xz13723762046',
    'xz13823203468',
    'xz13951516894',
    'xz15261578841',
    'xz15336690549',
    'xz15710019377',
    'xz15828611664',
    'xz18165135032',
    'xz18402246648',
    'xz18515313538',
    'xz18515315059',
    'xz18515315571',
    'xz18588872074',
    'xz18611130002',
    'xz18622838920',
    'xz18702527966',
    'xz18910015543',
    'xz18910015917',
]

# for tenant_code in tenant_code_list:
conn = pymysql.connect(host='172.16.135.10', port=32000, user='root', passwd='EMTC123456++',
                       db='pactera', charset='utf8')
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
