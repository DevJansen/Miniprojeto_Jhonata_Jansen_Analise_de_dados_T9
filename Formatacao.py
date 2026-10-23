
from rich.console import Console

console = Console()

def numero_br(valor, casas=0):
    texto = f"{valor:,.{casas}f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return texto
