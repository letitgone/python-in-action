# @Author ZhangGJ
# @Date 2021/04/04 20:57

import os


def git_pull(file_path_project_list):
    for file_path in file_path_project_list:
        file_name_list = os.listdir(file_path)
        if '.DS_Store' in file_name_list:
            file_name_list.remove('.DS_Store')
        for file_name in file_name_list:
            file_paths = file_path + file_name
            print(file_paths)
            os.system('shell/git_pull_shell.sh ' + file_paths)


if __name__ == '__main__':
    file_path_project_list = {
        '/Users/zhanggj/Downloads/idea-project/hifm/'
    }
    git_pull(file_path_project_list)
