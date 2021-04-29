# @Author ZhangGJ
# @Date 2021/03/29 07:04
import os


def wake_git_clone(file_path):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    for file_name in file_name_list:
        git_url = 'git clone -b dev http://username:code@localhost/ifm/' + file_name + '.git;'
        print(git_url)


def iot_git_clone(file_path):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    for file_name in file_name_list:
        git_url = 'git clone -b dev http://username:code@localhost/iot-cloud/' + file_name + '.git;'
        print(git_url)


if __name__ == '__main__':
    hifm_file_path = '/Users/zhanggj/Downloads/idea-projects/hifm'
    iot_file_path = '/Users/zhanggj/Downloads/idea-projects/iot'
    wake_starter_file_path = '/Users/zhanggj/Downloads/idea-projects/wake-starter'
    iot_starter_file_path = '/Users/zhanggj/Downloads/idea-projects/iot-starter'
    wake_git_clone(hifm_file_path)
    print("==========================================================")
    iot_git_clone(iot_file_path)
    print("==========================================================")
    wake_git_clone(wake_starter_file_path)
    print("==========================================================")
    iot_git_clone(iot_starter_file_path)
    print("==========================================================")
