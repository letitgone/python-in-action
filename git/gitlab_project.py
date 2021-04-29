# @Author ZhangGJ
# @Date 2021/01/28 16:01

import requests
import subprocess


def git(*args):
    return subprocess.check_call(['git'] + list(args))


local_url = input(f"Please input git clone local url: ")

output_file = input(f"Is output git url file: (y/n)")

output_file_url = ''
if output_file == 'y':
    output_file_url = input(f"Please input output git url local url: ")

page = [1, 2, 3, 4, 5]
lists = []
git_list = []
for i in page:
    url = 'localhost/groups/ifm/-/children.json'
    headers = {
        'Cookie': 'sidebar_collapsed=false; event_filter=all; _gitlab_session=49cd7e496dd14f6fc010c85d0f13296f',
        'X-CSRF-Token': 'te4G1M4ZlFoqPkcrH+sWStmPav2lajHkMuMk3Cn8vHvf/OBe5wQcy485xteuAzgBrIKfBwVEiFLu1ID87sJxJg=='
    }
    param = {
        'page': i
    }
    response = requests.get(url=url, params=param, headers=headers).json()
    for j in response:
        url = 'localhost' + dict(j).get('relative_path') + '.git'
        s = url.find('hifm')
        print(f"{url}\n")
        if (url.find('hifm') != -1 or url.find('hifm-server') != -1) and url.find(
                'sidecar') == -1 and url.find('hifmcloudweb') == -1 and url.find(
            'hifm-register') == -1 and url.find('hifm-server-ifm-api') == -1 and url.find(
            'hifm-server-plan-manage') == -1 and url.find('xxl') == -1 and url.find(
            'hifm-server-customization-service') == -1 and url.find(
            'hifm-server-supplier-service') == -1 and url.find(
            'hifm-server-budget-service') == -1 and url.find('hifm-server-ifm-api') == -1:
            git_list.append(
                'localhost' + dict(j).get('relative_path') + '.git')
            git("status")
            git("clone", 'localhost' + dict(j).get('relative_path') + '.git', "-b",
                'dev', local_url + '/' + dict(j).get('name'))
    lists.extend(response)
print(git_list)

if output_file == 'y':
    with open(output_file_url + '/git_urls.txt', 'w') as f:
        f.writelines(git_list)
        f.close()
