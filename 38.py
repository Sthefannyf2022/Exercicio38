valor= int(input('Dgite o valor para a conversão'))
conversao= int(input('''Digite uma das bases para conversão:
[1]- Binario
[2]- Octal
[3]-Hexadecimal \n'''))
if conversao ==1:
   print('{} convertido para binario é {}'.format(valor, bin(valor)[2:]))
elif conversao ==2:
   print('O numero {} covertido para octal é {}'.formart(valor, oct(valor)[2:]))
elif conversao == 3:
   print('O numero {} convertido para decimal é {}'.format(valor, hex(valor)[2:]))
else: print('Opção invalida')
