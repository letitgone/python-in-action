# 资产通用修改是否人为是否理赔json
# @Author ZhangGJ
# @Date 2021/04/21 14:49
import json

import pymysql
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

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456',
                       db='xz13818840653', charset='utf8')
cur = conn.cursor(DictCursor)
form_template_query = 'select * from form_template where form_template_code in ("AssetMaintenance","EngineeringMaintenance")'
cur.execute(form_template_query)
form_template_list = cur.fetchall()

artificial = {
    'name': '是否人为',
    'show': 1,
    'order': 4,
    'required': 1,
}
reparation = {
    'name': '是否已赔',
    'show': 1,
    'order': 5,
    'required': 1,
}

for form_template in form_template_list:
    form_template_dict = dict(form_template)
    form_template_info_str = form_template_dict.get('template_service_info')
    form_template_info = json.loads(form_template_info_str)
    form_template_info = dict(form_template_info)
    if form_template_info.__contains__('isArtificialOrPay'):
        print(f'form_template id: {form_template_dict.get("form_template_id")}')
        del form_template_info['isArtificialOrPay']
        form_template_info['artificial'] = artificial
        form_template_info['reparation'] = reparation
        new_form_template_info = json.dumps(form_template_info, ensure_ascii=False)
        form_template_update = 'update form_template set template_service_info = %s where form_template_id = %s'
        rows = cur.execute(form_template_update,
                           (new_form_template_info, form_template_dict.get("form_template_id")))
        print(f"rows: {rows}")

service_query = 'select * from service where template_code in ("AssetMaintenance", "EngineeringMaintenance")'
cur.execute(service_query)

service_list = cur.fetchall()
for services in service_list:
    service = dict(services)
    template_information = service.get('template_information')
    template_information_json = json.loads(template_information)
    template_information_json = dict(template_information_json)
    templateServiceInfo = template_information_json.get('templateServiceInfo')
    if templateServiceInfo.__contains__('isArtificialOrPay'):
        print(f'service id: {service.get("service_id")}')
        del templateServiceInfo['isArtificialOrPay']
        templateServiceInfo['artificial'] = artificial
        templateServiceInfo['reparation'] = reparation
        new_form_template_info = json.dumps(template_information_json, ensure_ascii=False)
        service_query = 'update service set template_information = %s where service_id = %s'
        rows = cur.execute(service_query, (new_form_template_info, service.get('service_id')))
        print(f"rows: {rows}")
cur.close()
conn.commit()
conn.close()
