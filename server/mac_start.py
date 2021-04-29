# @Author ZhangGJ
# @Date 2021/03/30 11:09

import os
import socket


def get_host_ip():
    global local_socket
    try:
        local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        local_socket.connect(('8.8.8.8', 80))
        local_ip = local_socket.getsockname()[0]
    finally:
        local_socket.close()

    return local_ip


if __name__ == '__main__':
    ip = get_host_ip()
    print(ip)
    os.system(
        '/Users/zhanggj/Downloads/pycharm-projects/python-in-action/shell/mac_startup.sh ' + ip)
