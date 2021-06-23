# @Author ZhangGJ
# @Date 2021/03/25 18:05
import os


def git_branch(file_path, from_branch, new_branch):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    print(file_name_list)
    for file_name in file_name_list:
        os.system(
            'shell/git_create_branch_shell.sh ' + file_path + ' ' + file_name + ' ' + from_branch + ' ' + new_branch)


if __name__ == '__main__':
    hifm_file_path = '/Users/zhanggj/Downloads/idea-project/hifm'
    wake_starter_file_path = '/Users/zhanggj/Downloads/idea-project/wake-starter'
    # 租户名
    git_branch(hifm_file_path, 'huobi', 'pactera')
    git_branch(wake_starter_file_path, 'huobi', 'pactera')
    print("Success!")
