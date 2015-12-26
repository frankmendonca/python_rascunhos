# coding=UTF-8

import subprocess as sb
import unittest
from utils import show_python_version


class MinhaClasse(object):

    def ping(self, url):
        with sb.Popen('ping -n 1 ' + url, stdout=sb.PIPE) as ps:
            return ps.wait() == 0


class MeuTeste(unittest.TestCase):

    def test_ping_ok(self):
        self.assertTrue(MinhaClasse().ping('uol.com.br'))

    def test_ping_nok(self):
        self.assertFalse(MinhaClasse().ping('uol123'))


###


if __name__ == '__main__':
    show_python_version()

    unittest.main()
