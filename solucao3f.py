import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'num2words'])

from num2words import num2words
lista = []

for i in range(1000):
    if num2words(i, lang='pt_BR').startswith("d"):
        lista.append(i)

print(lista[7])