# @Author ZhangGJ
# @Date 2021/03/25 18:05
import os


def change_branch(file_path, now_branch):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    print(file_name_list)
    for file_name in file_name_list:
        os.system(
            'shell/git_change_branch_shell.sh ' + file_path + ' ' + file_name + ' ' + now_branch)


if __name__ == '__main__':
    hifm_file_path = '/Users/zhanggj/Downloads/idea-project/hifm'
    # iot_file_path = '/Users/zhanggj/Downloads/idea-project/iot'
    wake_starter_file_path = '/Users/zhanggj/Downloads/idea-project/wake-starter'
    # iot_starter_file_path = '/Users/zhanggj/Downloads/idea-project/iot-starter'

    # imac
    # hifm_file_path = '/Users/zhanggj/Downloads/idea-projects/hifm'
    # iot_file_path = '/Users/zhanggj/Downloads/idea-project/iot'
    # wake_starter_file_path = '/Users/zhanggj/Downloads/idea-projects/wake-starter'
    # iot_starter_file_path = '/Users/zhanggj/Downloads/idea-project/iot-starter'

    # 租户名
    change_branch(hifm_file_path, 'ghac')
    # change_branch(iot_file_path, 'dev')
    change_branch(wake_starter_file_path, 'ghac')
    # change_branch(iot_starter_file_path, 'dev')
    print("Success!")
