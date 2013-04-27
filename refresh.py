#!/usr/bin/env python
#-*- coding: utf8 -*-
import os
import shutil
from fl import settings
from django.core.management import setup_environ
setup_environ(settings)

from fl.settings import DATABASES
import MySQLdb

def clean_database():
    db = DATABASES['default']
    cnn = MySQLdb.connect(host=db['HOST'],
        user=db['USER'], passwd=db['PASSWORD'])
    name = db['NAME']
    try:
        cnn.query('drop database ' + name)
    except:
        pass
    cnn.query('create database ' + name + ' character set utf8')
    cnn.commit()
    os.system('echo "yes\nysyong\nysyfff@qq.com\n"|./manage.py syncdb')

if __name__ == '__main__':
    clean_database()
    
