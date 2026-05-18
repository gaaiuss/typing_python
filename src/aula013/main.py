# Callback Protocol vs Callable
from collections.abc import Callable
from resource.utils import cyan_print, sep_print
from typing import Protocol

# Me diz uma coisa, o que significa isso aqui?
type ReallyRelaxedCallable = Callable[..., None]  # (*args, **kwargs) -> None

# E isso?
type MysticCallable = Callable[[int, int, str], bool]  # (1, 2, 'a') -> true

# Podemos afirmar o seguinte:
# `ReallyRelaxedCallable` recebe qualquer coisa e retorna `None` [PONTO].
# `MysticCallable` recebe `int`, `int` e `str` e retorna `bool` [PONTO].

################################################################################
#
# Não há nada de errado em usar `Callable`, de fato, vamos usar muito mais eles
# do que os `Protocols`.
# Porém, em algum momento o nome dos argumentos vão importar. Talvez você crie
# uma função que só possa receber argumentos nomeados ou que possa ter uma
# assinatura muito complexa.
# Nesses casos os callback protocols resolvem o problema.
# Com eles é possível definir um contrato através de um protocol e depois fazer
# o que quiser com o método `__call__`.
#
################################################################################


# O callback protocol (é muito fácil de implementar)


class CallbackProtocol(Protocol):
    # Basta que você defina a assinatura da sua função no método `__call__`.
    # Por favor, nunca esqueça do `self`.
    def __call__(self, *, whatever: str) -> str: ...


################################################################################

# Funções para testar: uma tem a assinatura correta, a outra não.


def good_func(*, whatever: str) -> str:
    """Essa função cumpre o contrato ✅"""
    return whatever


def bad_func(not_good: str) -> str:
    """Essa NÃO função cumpre o contrato ❌"""
    return not_good


################################################################################

# Bora testar tudo

if __name__ == "__main__":
    sep_print()

    # 🧐 Isso aqui é só para obcecado por tipos. Não necessário.
    # Geralmente, vamos usar callback protocol com... advinha? [callbacks]
    # Mas, vai servir para nosso primeiro exemplo sem complicar as coisas
    good: CallbackProtocol = good_func
    bad: CallbackProtocol = bad_func

    # Vamos usar as funções
    same_str_good = good(whatever="Aqui está sua string de volta")
    same_str_bad = bad(not_good="Aqui está sua string de volta")

    # O Python meio que NÃO TÁ NEM AÍ (como sempre)
    cyan_print(f"{same_str_good}")  # Python ✅
    cyan_print(f"{same_str_bad}")  # Python ✅

    sep_print()


################################################################################
