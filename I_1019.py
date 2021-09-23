# Conversão de Tempo
from math import floor

N = int(input())                
h = floor((N / 60) / 60)               
resto_hora = N - (h * 60 * 60)            
m = floor(resto_hora / 60)      
resto_minuto = N % 60           
s = resto_minuto   

print(f'{h}:{m}:{s}')