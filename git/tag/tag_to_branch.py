# @Author ZhangGJ
# @Date 2021/04/13 10:20
import os


def branch_tag(file_path, tag_name, new_branch_name):
    file_name_list = os.listdir(file_path)
    if '.DS_Store' in file_name_list:
        file_name_list.remove('.DS_Store')
    print(file_name_list)
    for file_name in file_name_list:
        os.system(
            '../shell/tag/tag_to_branch.sh '
            + file_path + ' ' + file_name + ' ' + new_branch_name + ' ' + tag_name)


if __name__ == '__main__':
    hifm_file_path = '/Users/zhanggj/Downloads/idea-project/hifm'
    wake_starter_file_path = '/Users/zhanggj/Downloads/idea-project/wake-starter'
    branch_tag(hifm_file_path, 'wxprison-202104081005', 'wxprison')
    branch_tag(wake_starter_file_path, 'wxprison-202104081005', 'wxprison')
    print("complete!")
