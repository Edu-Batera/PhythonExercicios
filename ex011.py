larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
área = larg*alt
print('=' * 70)
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta'.format(tinta))
print('=' * 70)