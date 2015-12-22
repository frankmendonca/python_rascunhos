# coding=UTF-8

import sys
import subprocess as sb
import unittest


class MinhaClasse(object):

    def print(self, *args):
        print(*args, end='\n\n')

    def show_python_version(self):
        self.print('[ Python version {0} ]'.format(sys.version))

    def ping(self, url):
        with sb.Popen('ping -n 1 ' + url, stdout=sb.PIPE) as ps:
            return ps.wait() == 0

    def executar(self, func, args):
        retorno = func(args)

        self.print('Executou... {0}({1!r}) => {2}'.format(
            func.__name__, args, retorno))


###


class MeuTeste(unittest.TestCase):

    def test_ping_ok(self):
        self.assertTrue(MinhaClasse().ping('uol.com.br'))

    def test_ping_nok(self):
        self.assertFalse(MinhaClasse().ping('uol123'))


###


if __name__ == '__main__':
    minhaClasse = MinhaClasse()
    minhaClasse.show_python_version()
    minhaClasse.executar(minhaClasse.ping, 'uol.com.br')

    unittest.main()
