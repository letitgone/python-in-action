# 服务请求刷数据：申领资产分类的数据结构
# @Author ZhangGJ
# @Date 2021/02/03 16:54

import pymysql
from pymysql.cursors import DictCursor
import json
import pandas as pd
from sqlalchemy import create_engine

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123123',
                       db='test', charset='utf8')
cur = conn.cursor(DictCursor)

service_request_query = "select sr.* from service_request sr LEFT JOIN service s on sr.service_id " \
                        "= s.service_id where s.template_code = 'AssetClaim' "
cur.execute(service_request_query)
service_request_list = cur.fetchall()
for service_request in service_request_list:
    service_request_attributes = dict(service_request).get('service_request_attributes')
    condition = json.loads(service_request_attributes)
    if ('categoryName' in condition) and ('numberClaim' in condition) and (
            'assetCategoryName' in condition) and ('assetCategoryId' in condition):
        service_request_attributes = json.loads(service_request_attributes)
        del service_request_attributes['categoryName']
        assetCategoryId = service_request_attributes.pop('assetCategoryId')
        numberClaim = service_request_attributes.pop('numberClaim')
        assetCategoryName = service_request_attributes.pop('assetCategoryName')
        assetCategoryDict = {
            'assetCategoryId': assetCategoryId,
            'numberClaim': numberClaim,
            'assetCategoryName': assetCategoryName
        }
        assetCategoryList = [assetCategoryDict]
        service_request_attributes['assetCategory'] = json.loads(json.dumps(assetCategoryList))
        service_request_attributes = json.dumps(service_request_attributes)
        update_rows = cur.execute(
            "update service_request set service_request_attributes = %s where service_request_id "
            "= %s",
            (service_request_attributes, dict(service_request).get('service_request_id')))
        print(update_rows)
        print('Update successful!')
cur.close()
conn.commit()
conn.close()
