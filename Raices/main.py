import random
#a,b=np.random.random_integers(-10,10, 2)
a=random.randint(-10,10)
b=random.randint(-10,10)
print(a,b)
print('')
print('Quais sao as raices do seguente polinomio: x^2+',a+b,'x',a*b)


r1= eval(input('Raiz x1='))
r2= eval(input('Raiz x2='))

if r1==a and r2==b or r1==b and r2==a:
	print('')
	print('As duas raices estao corretas.')
	print('Sua nota e: 10')

elif r1==a or r1==b:
	print('')
	print('A raiz x1 esta correcta:',r1)
	if r1==a:
		print('A raiz',r2,'esta incorreta')
		print('A raiz x2 correta e:',b)
	elif r1==b:
		print('A raiz',r2,'esta incorreta')
		print('A raiz x2 correta e:',a)
		
	print('Sua nota e: 5')

elif r2==a or r2==b:
	print('')
	print('A raiz x1 esta correta:',r2)
	if r2==a:
		print('A raiz',r1,'esta incorreta')
		print('A raiz x2 correta e:',b)
	elif r2==b:
		print('A raiz',r1,'esta incorreta')
		print('A raiz x2 correta e:',a)	
	print('Sua nota e: 5')
elif r1!=a and r1!=b or r1!=b and r1!=a:
	print('')
	print('As duas raices estao incorretas.')
	print('A raiz x1=',a)
	print('A raiz x2=',b)
	print('Sua nota e 0')

