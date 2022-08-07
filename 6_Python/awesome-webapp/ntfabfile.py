#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Steven'

'''
Deployment tookkit.
pip install fabric3
fab build -f ntfabfile.py
'''

import os, re, tarfile
from datetime import datetime
from fabric.api import *

# c = Connection(host='192.168.31.10', user='root', port=2202)

env.user = 'root'
env.sudo_user = 'root'
# env.hosts = ['123.123.123.123']
env.host_string = '192.168.31.10' # 改成你的服务器ip

db_user = 'www-data'
db_password = 'www-data'

_TAR_FILE = 'dist-awesome.tar.gz'
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/srv/awesome'

def _current_path():
    return os.path.abspath('.')

def _now():
    return datetime.now().strftime('%y-%m-%d_%H.%M.%S')

def build():
    '''
    Build dist package.
    '''
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    if os.name == 'nt':
        local('del dist\\%s' % _TAR_FILE)                   # 删除旧压缩包
        tar = tarfile.open("dist/%s" % _TAR_FILE, "w:gz")   # 创建新压缩包

        for root,_dir,files in os.walk("www/"):             # 打包www文件夹
            if _dir == 'test':
                continue
            for f in files:
                if not (('.pyc' in f) or ('.pyo' in f)):    # 排除开发过程调试产生的文件，为了简单点实现，此处没有完全照搬廖老师的参数
                    fullpath = os.path.join(root,f)
                    tar.add(fullpath)
        
        tar.close()
    else:
        local('rm -f dist/%s' % _TAR_FILE)
        with lcd(os.path.join(_current_path(), 'www')):
            cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
            cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
            cmd.extend(includes)
            local(' '.join(cmd))