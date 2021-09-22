n = int(input())
while(n > 0):

	inp = input().split()

	for i in range(n):
		d={}
		c = 0

		for j in inp:
			d[c] = int(j)
			c= c+1

	p = 0


	if(d[c-1] >d[0]):
		 	last= True # I am going down 
			
	else:
			last = False	#I am going up 
	

	down= False

	for r in range(0, len(d)-1 ):

		if(d[r] > d[r + 1]):
			down = True
		else:
			down = False
		

		if(last != down):
			p = p +1

		last = down

	print(p+1)
	n = int(input())
		

		 	
