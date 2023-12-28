# Condição de pagamentos e juros:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('NOME DA LOJA...'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] Á vista em dinheiro ou cheque, você terá 10% de desconto.
[2] Á vista no cartão você terá 10% de desconto.
[3] 2x no cartão, preço formal.
[4] 3x ou mais no cartão você será sujeito a juros de 20%''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif opção == 4:
    total: float = preço + (preço * 20 / 100)
    totParc = int(input('Quantas parcelas? '))
    parcela = total / totParc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totParc, parcela))
else:
    print('OPÇÃO INVÁLIDA!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
