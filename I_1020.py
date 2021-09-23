# Idade em dias
from math import floor

idade = int(input())
anos = floor(idade / 365)
resto_anos = idade % 365
meses = floor(resto_anos / 30)
dias = resto_anos % 30

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')