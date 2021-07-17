# @Author ZhangGJ
# @Date 2021/04/13 14:40
import os


def wake_maven_deploy(file_path, maven_profile):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    for file_name in file_name_list:
        os.system('shell/maven_deploy.sh ' + file_name + ' ' + maven_profile)
        print(f'{file_name} success')


if __name__ == '__main__':
    wake_maven_deploy('/Users/zhanggj/Downloads/idea-project/wake-starter/', 'master')
    print('Complete!')
