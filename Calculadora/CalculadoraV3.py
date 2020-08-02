##calculaora
##byVinicius Ferreira Santos

##função
def subtracao (x,y):
	r = x-y
	print('O valor da sua operação é %a'%(r))

def soma (x,y):
	r = x+y
	print('O valor da sua operação é %a'%(r))

def divisao (x,y):
	r = x/y
	print('O valor da sua operação é %a'%(r))

def multiplicacao (x,y):
	r = x*y
	print('O valor da sua operação é %a'%(r))


print('*****************************Calculadora Python*********************************************\n\n')


print('1 - Subtração')
print('2 - Soma')
print('3 - Divisão')
print('4 - Multiplicação\n\n')

operacao = input('Informe qual operação deseja fazer !!!  1/2/3/4\n\n')
numero1 = float(input('\nInforme o primeiro número/\n\n'))
numero2 = float(input('\ninforme o segundo número\n\n'))

print('\n')


if operacao == '1':
	subtracao(numero1,numero2)
elif operacao == '2':
	soma(numero1,numero2)
elif operacao == '3':
	divisao(numero1,numero2)
elif operacao == '4':
	multiplicacao(numero1,numero2)





