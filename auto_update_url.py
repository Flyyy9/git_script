import os


def get_git_config(cur_dir: str = './'):
    dir_list = os.listdir(cur_dir)
    for dir_one in dir_list:
        if dir_one == '.git':
            break
        else:
            return ''
    conf_file: str = os.curdir + '/.git/config'
    if os.path.exists(conf_file):
        return conf_file
    else:
        return ''


def get_ip_address():
    pass
    # import socket, fcntl, struct
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    # ret = socket.inet_ntoa(inet[20:24])


def update_conf_url(conf_file):
    try:
        f = open(conf_file)
    except FileNotFoundError:
        print('[error] ' + conf_file + ' is not find')


if __name__ == '__main__':
    '''test code'''
    gitblit_dir = 'C:/Users/faberc/Source/GitBlit'
    dir_list = os.listdir(gitblit_dir)

    for dir_one in dir_list:
        conf_file = get_git_config(dir_one)
        if conf_file == '':
            continue
        else:
            update_conf_url(conf_file)

