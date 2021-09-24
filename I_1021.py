from math import floor

valor = round(float(input()), 2)

if valor < 0 or valor > 1000000.00:
    exit()

notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
quantidade = []

for nota in notas:
    resultado = floor(valor / nota)
    valor -= (resultado * nota)
    valor = round(valor, 2)
    if 0.01 > valor > 0:
        valor = 0.01
    quantidade.append(resultado)

print(f'NOTAS:\n'
        f'{quantidade[0]} nota(s) de R$ 100.00\n'
        f'{quantidade[1]} nota(s) de R$ 50.00\n'
        f'{quantidade[2]} nota(s) de R$ 20.00\n'
        f'{quantidade[3]} nota(s) de R$ 10.00\n'
        f'{quantidade[4]} nota(s) de R$ 5.00\n'
        f'{quantidade[5]} nota(s) de R$ 2.00\n'
        'MOEDAS:\n'
        f'{quantidade[6]} moeda(s) de R$ 1.00\n'
        f'{quantidade[7]} moeda(s) de R$ 0.50\n'
        f'{quantidade[8]} moeda(s) de R$ 0.25\n'
        f'{quantidade[9]} moeda(s) de R$ 0.10\n'
        f'{quantidade[10]} moeda(s) de R$ 0.05\n'
        f'{quantidade[11]} moeda(s) de R$ 0.01')
