"""Hello World Multi Linguas.

  Dependendo da Lingua configurada no 
  ambiente o programa exibe a mensagem 
  correspondente.

  Como usar:

  Tenho a variavel LANG devidamente configurada. ex:

  export LANG=pt_BR

  Execuçao: 
  python2 hello.py
  ou
  ./hello.py
  
  """
""" Metadados"""
"""__(2 underline) é chamado comumente de DUNDER"""
__version__ = "0.0.1"
__author__  = "Malu Oliveira"
__license__ = "Unlicense"

import os


current_language = os.getenv("LANG","en_US")[:5]
msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bounjour, Monde!"    
    
print(msg)
