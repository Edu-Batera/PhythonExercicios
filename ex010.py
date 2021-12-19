real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.70 #cotação do dia 18/12/2021
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(real, dolar))