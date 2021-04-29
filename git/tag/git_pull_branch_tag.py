# @Author ZhangGJ
# @Date 2021/04/13 10:20
import os
import time


def hifm_branch_tag(service_name, tag_name, temp_branch_name):
    os.system(
        'shell/tag/hifm_git_pull_branch_tag.sh ' + service_name + ' ' + tag_name + ' ' + temp_branch_name)


def wake_branch_tag(service_name, tag_name, temp_branch_name):
    os.system(
        'shell/tag/wake_git_pull_branch_tag.sh ' + service_name + ' ' + tag_name + ' ' + temp_branch_name)


# def hifm_service_tag_info():
#     return {
#         # 'hifm-server-asset-manage': 'huobi-3.3.2.20210315',
#         # 'hifm-server-ghac-custom': 'ghac-202103291613',
#         # 'hifm-gateway': 'huobi-3.3.2.20210315',
#         'hifm-common': 'huobi-3.3.2.20210315',
#     }


def wake_service_tag_info():
    return {
        'wake-common': 'ghac-temp',
        # 'wake-mybatis-asset-spring-boot-starter': 'huobi-202103291430',
        # 'wake-mybatis-spring-boot-starter': 'ghac-20210311',
        # 'wake-redis-spring-boot-starter': 'huobi-202103291430',
        # 'wake-rocketmq-spring-boot-starter': 'huobi-202103291430',
        # 'wake-security-spring-boot-starter': 'huobi-202103291430',
        # 'wake-swagger-spring-boot-starter': 'huobi-202103291430',
        # 'wake-tool-spring-boot-starter': 'huobi-202103291430',
    }


def base_info():
    """需要修改租户"""
    tenant_code = 'ghac'
    now_time = time.strftime('%Y%m%d%H%M', time.localtime())
    return tenant_code + '-' + now_time + '-temp'


if __name__ == '__main__':
    name = base_info()
    print(f'Branch name: {name}')
    # for key, value in hifm_service_tag_info().items():
    #     hifm_branch_tag(key, value, name)
    #     print(f'{key} Success!')
    for key, value in wake_service_tag_info().items():
        wake_branch_tag(key, value, name)
        print(f'{key} Success!')
    print("complete!")
