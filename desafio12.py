preço = float(input('Moça qual é o preço deste produto? R$ '))
desconto = preço - (preço * 5 / 100)
print('O produto que custava {:.2f}, na promoção com 5% de desconto ele custara {:.2f}'.format(preço, desconto))