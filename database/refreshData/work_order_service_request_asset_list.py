# 工单列表服务请求刷资产列表(资产维修)
# @Author ZhangGJ
# @Date 2021/04/21 10:01
import json

import pymysql
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123123',
                       db='123', charset='utf8')
cur = conn.cursor(DictCursor)

service_request_id = 5073

service_request_query = 'select * from service_request where service_request_id = %s'
cur.execute(service_request_query, service_request_id)

service_request = cur.fetchone()
service_request_dict = dict(service_request)
service_request_attributes = service_request_dict.get('service_request_attributes')
service_request_attribute = json.loads(service_request_attributes)
service_request_attribute = dict(service_request_attribute)
assetIds = service_request_attribute.get('assetIds')
asset_id_list = assetIds.split(',')
asset_list = []
del service_request_attribute['assetList']
for asset_id in asset_id_list:
    asset_query = 'SELECT\
    	a.id,\
    	a.name,\
    	a.asset_id AS assetId,\
    	p.NAME AS location,\
    	ac.NAME AS categoryName,\
    	asset_attributes ->> "$.purchasedate.value" AS purchasedate\
    FROM\
    	assets a\
    	LEFT JOIN places p ON a.asset_attributes ->> "$.location.value" = p.id\
    	LEFT JOIN asset_categorys ac ON a.category_id = ac.id\
    WHERE\
    	a.id = %s'
    cur.execute(asset_query, asset_id)
    asset = cur.fetchone()
    asset_list = [asset]
service_request_attribute['assetList'] = asset_list

service_request_attribute_str = json.dumps(service_request_attribute, ensure_ascii=False)
service_request_update = 'update service_request set service_request_attributes = %s where service_request_id = %s'
rows = cur.execute(service_request_update, (service_request_attribute_str, service_request_id))
print(f"rows: {rows}")

cur.close()
conn.commit()
conn.close()
