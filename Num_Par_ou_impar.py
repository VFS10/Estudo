
n = str(input("Qual é seu nome?...\n"))

nas = int(input(" Em que ano você nasceu?\n"))
atu = int(input("Em qual ano estamos?\n"))
ida = atu-nas

resut = ida%2
par = 0

if resut == par:
   print (n+" ,sua idade é umn úmero PAR\n")
   print (ida,"Anos")
else:
   print (n+" ,sua idade é um número IMPAR, você tem %a anos\n"%(ida))
   print (ida,"Anos")








