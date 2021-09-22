inpt = input().split()	
n = int(inpt[0])
b = int(inpt[1])
while(n > 0):
	
	number = []	
	for i in range (n):
			number.append(i);

	rm = input().split()
	
	l = []
	for i in rm:
 		l.append(int(i))
		
	for j in l:
		for k in l:
			if( k-j >= 0 and k-j < n):
				print(k-j)
				if(len(number) <= 0):	
					break
				number.remove(k-j)
			
	
	print(number)
	if(len(number) > 0 ):
		print("N")
	else:
		print("Y")		

	inpt = input().split()	
	n = int(inpt[0])
	b = int(inpt[1])
