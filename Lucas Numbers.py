#Lucas Numbers
a=input("Enter the number you wanna check is prime or not:")
if a.isdigit()==False or int(a)<1:
	print("""Better check that number again. The concept of "being prime" breaks down on what you just entered!""")
else:
	b=1
	c=0
	d=3
	e=int(a)-2
	if a=="1":
		print("No!It isn't!")
	elif a=="2":
		print("Yes, it is.")
	else:
		while c<e:
			f=b+d
			b=d
			d=f
			c+=1
		g=int(f)-1
		if int(g)%int(a)==0:
			print("Might be.....")
		else:
			print("Definitely not!")