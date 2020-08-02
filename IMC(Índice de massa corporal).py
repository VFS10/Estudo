print ("Vamos calcular seu IMC!\n")
nome = str(input("Qual seu Nome?\n"))
peso = int(input("Qual seu Peso?\n"))
altura = float(input("Qual sua altura?\n"))


imc = peso/(altura*altura)


if imc < 10:
		print (nome+" ,seu IMC refere-se a Desnutrição Grau 5 !")

if (imc >= 10) and (imc <= 12.9):
	print (nome+" ,seu IMC refere-se a Desnutrição Grau 4!")

elif (imc >= 13) and (imc <= 15.9):
		print (nome+" ,seu IMC refere-se a Desnutrição Grau 3!")

elif (imc >= 16) and (imc <= 16.9):
		print (nome+" ,seu IMC refere-se a Desnutrição Grau 2!")

elif (imc >= 17) and (imc <= 18.4):
		print (nome+" ,seu IMC refere-se a Desnutrição Grau 1!")

elif (imc >= 18,5) and (imc <= 24.9):
		print (nome+" ,seu IMC refere-se a Normal!!!!\n")
		print ("Parabéns "+nome)

elif (imc >= 25) and (imc <= 29.9):
		print (nome+" ,seu IMC refere-se a Pré-obesidade!")

elif (imc >= 30) and (imc <= 34.5):
		print (nome+" ,seu IMC refere-se a Obesidade Grau 1!")

elif (imc >= 35) and (imc <= 39.9):
		print (nome+" ,seu IMC refere-se a Obesidade Grau 2!")

elif imc > 40:
		print (nome+" ,seu IMC refere-se a Obesidade Grau 1!")