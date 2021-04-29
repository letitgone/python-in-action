# @Author ZhangGJ
# @Date 2021/03/25 18:05
import os
import time


def git_tag(file_path, tenant_code, now_branch, now_time):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    print(file_name_list)
    for file_name in file_name_list:
        tag_name = tenant_code + '-' + now_time
        os.system(
            '/Users/zhanggj/Downloads/pycharm-projects/python-in-action/git/shell/git_tag_shell.sh ' + file_path + ' ' + file_name + ' ' + now_branch + ' ' + tag_name + ' ' + tenant_code)


if __name__ == '__main__':
    hifm_file_path = '/Users/zhanggj/Downloads/idea-project/hifm'
    wake_file_path = '/Users/zhanggj/Downloads/idea-project/wake-starter'
    now_time = time.strftime('%Y%m%d%H%M', time.localtime())

    # 租户名
    # 从哪个分支创建tag
    git_tag(hifm_file_path, 'huobi', 'release', now_time)
    git_tag(wake_file_path, 'huobi', 'release', now_time)
