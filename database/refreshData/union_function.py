# 整合所有权限到运营平台function
# @Author ZhangGJ
# @Date 2021/04/23 17:09

import pymysql
import time
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123123',
                       charset='utf8')
cur = conn.cursor(DictCursor)

ghac_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from ghac.functions'
huobi_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from huobi.functions'
qhdbank_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from qhdbank.functions'
sinocanada_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from sinocanada.functions'
weidian_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from weidian.functions'
wxprison_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from wxprison.functions'
wxyx_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from wxyx.functions'
xz13861836988_function_query = 'select permission_type, function_type, name, identify, pid, is_show, show_parent from xz13861836988.functions'
query_list = [ghac_function_query, huobi_function_query, qhdbank_function_query,
              sinocanada_function_query, weidian_function_query, wxprison_function_query,
              wxyx_function_query, xz13861836988_function_query]
function_all_list = []
for query in query_list:
    cur.execute(query)
    function_list = cur.fetchall()
    function_all_list.extend(function_list)

conn = pymysql.connect(host='localhost', port=3506, user='root', passwd='123456',
                       charset='utf8')
cur = conn.cursor(DictCursor)
for functions in function_all_list:
    function_dict = dict(functions)
    insert_query = 'INSERT INTO hifm_operation.functions(permission_type, function_type, name, identify, pid, is_show, show_parent) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cur.execute(insert_query, (
        function_dict.get('permission_type'), function_dict.get('function_type'),
        function_dict.get('name'), function_dict.get('identify'), function_dict.get('pid'),
        function_dict.get('is_show'), function_dict.get('show_parent')))
cur.close()
conn.commit()
conn.close()
