import sys


def println(*args, **kwargs):
    """Faz a mesma coisa que o print, mas pula mais uma lina (\\n\\n)
    (por padrão)"""
    kwargs.setdefault('end', '\n\n')
    print(*args, **kwargs)


class Callable(object):

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def call(self):
        self.retorno = self.func(self.args, self.kwargs)
        return self.retorno

    def println_callable(self):
        println('Executou... {0}({1!r}) => {2}'.format(
            self.func.__name__, self.args, self.retorno), **self.kwargs)


def exec_and_println(func, *args, **kwargs):
    """Recebe uma funcao e seus argumentos, executa ela,
    e mostra a chamada dela e seu executado"""
    callable = Callable(func, *args, **kwargs)
    retorno = callable.call()
    callable.println_callable()

    return retorno


def show_python_version():
    println('[ Python version {0} ]'.format(sys.version))
