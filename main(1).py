year=int(input("enter year:"))

if(year%400==0) and (year%100==0):
	print(format(year),"is leap year")
elif(year%4==0) and (year%100!=0):
	print(format(year),"is leap year")
else:
	print(format (year),"is not leap year")