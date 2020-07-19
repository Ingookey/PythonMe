# coding: utf-8

import sys
import logging
import subprocess


class RunCmd(object):
    @staticmethod
    def run_cmd(cmd=None):
        if not cmd:
            logging.error('cmd is null, do nothing')

        cmd = ' '.join(cmd)
        ret, output = subprocess.getstatusoutput(cmd)
        if ret != 0:
            logging.debug('fail, cmd: {}'.format(cmd))
            sys.exit(255)
        else:
            logging.debug('success, cmd: {} \nresult: {}'.format(cmd, output))
            sys.exit(0)
        pass
