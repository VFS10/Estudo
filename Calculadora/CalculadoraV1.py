##calculaora
##byVinicius Ferreira Santos

print('*****************************Calculadora Python*********************************************\n\n')


print('1 - Subtração')
print('2 - Soma')
print('3 - Divisão')
print('4 - Multiplicação\n\n')


operacao = input('Informe qual operação deseja fazer !!!  1/2/3/4\n\n')

print('\n')
print('\n')
print('\n')
print('\n')

def subtracao ():
	numero1= input('informe o primeiro valor\n\n')
	numero2= input('informe o segundo valor\n\n')

	numero1=float(numero1)
	numero2=float(numero2)

	resultado = numero1-numero2
	print('O resultado da sua operação é')
	print(resultado)
	

def soma ():
	numero1= input('informe o primeiro valor\n\n')
	numero2= input('informe o segundo valor\n\n')

	numero1=float(numero1)
	numero2=float(numero2)

	resultado = numero1+numero2
	print('O resultado da sua operação é')
	print(resultado)

def divisao ():
	numero1= input('informe o primeiro valor\n\n')
	numero2= input('informe o segundo valor\n\n')

	numero1=float(numero1)
	numero2=float(numero2)

	resultado = numero1/numero2
	print('O resultado da sua operação é')
	print(resultado)

def multiplicacao ():
	numero1= input('informe o primeiro valor\n\n')
	numero2= input('informe o segundo valor\n\n')

	numero1=float(numero1)
	numero2=float(numero2)

	resultado = numero1*numero2
	print('O resultado da sua operação é')
	print(resultado)


if operacao == '1':
	subtracao()
elif operacao == '2':
	soma()
elif operacao == '3':
	divisao()
elif operacao == '4':
	multiplicacao()





