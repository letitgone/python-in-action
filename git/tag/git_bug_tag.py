# @Author ZhangGJ
# @Date 2021/03/25 18:05
import os
import time


def hifm_git_tag(service_names, now_branch, tag_name):
    for service_name in service_names:
        os.system(
            'shell/tag/hifm_git_tag_shell.sh ' + service_name + ' ' + now_branch + ' ' + tag_name)


def wake_git_tag(service_names, now_branch, tag_name):
    for service_name in service_names:
        os.system(
            'shell/tag/wake_git_tag_shell.sh ' + service_name + ' ' + now_branch + ' ' + tag_name)


if __name__ == '__main__':
    name = 'ghac' + '-' + time.strftime('%Y%m%d%H%M', time.localtime())
    hifm = ['hifm-server-asset-manage', 'hifm-server-ghac-custom']
    wake = ['wake-common',
            'wake-mybatis-asset-spring-boot-starter',
            'wake-mybatis-spring-boot-starter',
            'wake-redis-spring-boot-starter',
            'wake-rocketmq-spring-boot-starter',
            'wake-security-spring-boot-starter',
            'wake-swagger-spring-boot-starter',
            'wake-tool-spring-boot-starter']

    # 租户名
    # 从哪个分支创建tag
    # hifm_git_tag(hifm, 'ghac-202104131153-temp', name)
    wake_git_tag(wake, 'ghac-202104131153-temp', name)
