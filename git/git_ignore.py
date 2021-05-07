# @Author ZhangGJ
# @Date 2021/05/06 18:36
import os


def git_ignore(file_path):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    print(file_name_list)
    for file_name in file_name_list:
        project_path = file_path + '/' + file_name
        path = project_path + '/' + '.gitignore'
        # if not os.path.exists(path):
        #     os.system('shell/cp_ignore.sh ' + file_path + ' ' + project_path)
        #     print(f'ignore: {file_name}')
        # with open(path, 'a') as w:
        #     w.write('\nDockerfile\n')
        os.system('shell/git_ignore_shell.sh ' + file_path + ' ' + file_name)


if __name__ == '__main__':
    hifm_file_path = '/Users/zhanggj/Downloads/idea-project/hifm'
    git_ignore(hifm_file_path)
    print("Success!")
