#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This test check is backend is running without error
"""

import os
import time
import shlex
import subprocess
import requests
import unittest2


class TestStart(unittest2.TestCase):
    def test_start_application_uwsgi(self):
        """ Start alignak backend with uwsgi"""

        os.getcwd()
        print ("Launching application with UWSGI ...")

        test_dir = os.path.dirname(os.path.realpath(__file__))
        print("Dir: %s" % test_dir)

        print("Starting Alignak Backend...")
        fnull = open(os.devnull, 'w')
        pid = subprocess.Popen(
            shlex.split('uwsgi --plugin python -w alignakbackend:app --socket 0.0.0.0:5000 '
                        '--protocol=http --enable-threads --pidfile /tmp/uwsgi.pid')
        )
        time.sleep(1)

        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        # get token
        response = requests.post('http://127.0.0.1:5000/login', json=params, headers=headers)
        resp = response.json()
        assert resp['token']

        subprocess.call(['uwsgi', '--stop', '/tmp/uwsgi.pid'])
        time.sleep(1)

    def test_start_application(self):
        """ Start application stand alone"""
        print('test application default start')

        fnull = open(os.devnull, 'w')

        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(os.path.join(dir_path, "../alignak_backend"))
        print("Launching application default...")
        process = subprocess.Popen(
            shlex.split('python ../alignak_backend/main.py')
        )
        print('PID = ', process.pid)
        time.sleep(2.0)
        print("Killing application ...")
        process.terminate()
