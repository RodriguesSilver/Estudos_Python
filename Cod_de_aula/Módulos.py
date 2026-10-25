# Aprendendo módulos em Python3
# Módulos são comandos que adicionam funcionalidades na nossa linguagem, como mais calculos matemáticos, cores e etc.

# O comando utilizado em python para isso é o comando IMPORT
import datetime
agora = datetime.datetime.now()
print(agora)

# Para importar só um módulo de uma biblioteca se usa o comando FROM e depois o IMPORT
from math import sqrt
raiz = sqrt(25)

# Ainda é possível importar módulos não nativos do python3
# pip install emoji (no bash)
# ou simplesmente digitando "import emoji" e clicando na lampada vermelha
