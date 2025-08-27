#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import ftplib
import socket
import sys
from datetime import datetime


class FtpCrack(object):

    def __init__(self, host, username='', password=''):
        if not host:
            print "[*] Error: no host given"
            sys.exit(2)
        else:
            self.start = datetime.now()
            self.host = host
            self.username = username
            self.password = password
            self.ftp = None

    def _close_ftp_connection(self):
        self.ftp.quit()
        print "[*] Close FTP connection after ", datetime.now() - self.start

    def _list_ftp_directory(self):
        try:
            print "[*] List FTP directory content"
            self.ftp.dir()
        except ftplib.all_errors:
            print "[*] ERROR: Cannot list content"
        self._close_ftp_connection()

    def ftp_connect(self):
        try:
            self.ftp = ftplib.FTP(self.host)
        except (socket.error, socket.gaierror) as err:
            print "[*] Cannot connect to %s" % self.host
            print "[*] Error %s" % err
            sys.exit(2)

        print "[*] Connected to %s" % self.host

    def _ftp_anonymous_login(self):
        try:
            self.ftp.login()
        except ftplib.error_perm:
            print "[*] ERROR: cannot login anonymously"
            self._close_ftp_connection()
            sys.exit(2)

        print "[*] Anonymous login"
        self._list_ftp_directory()

    def _ftp_credential_login(self):
        print "[*] User: %s - Password: %s" % (self.username, self.password)
        try:
            self.ftp.login(self.username, self.password)
        except ftplib.error_perm:
            print "[*] ERROR: wrong credentials"
            self._close_ftp_connection()
            sys.exit(2)

        print "[*] Login with credentials"
        self._list_ftp_directory()

    def ftp_login(self):
        if not self.username or not self.password:
            self._ftp_anonymous_login()
        else:
            self._ftp_credential_login()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Brute-force FTP')
    parser.add_argument('host', help='target host or ip')
    parser.add_argument('-u', '--usr', help='login user name')
    parser.add_argument('-p', '--pwd', help='login password')
    args = parser.parse_args()

    RUN = FtpCrack(args.host, args.usr, args.pwd)
    RUN.ftp_connect()
    RUN.ftp_login()