import random 
list=[]
salary=int(input("input your salary for the month"))
list.append(salary)
month=input("enter the name of the month")
list.append(month)
psavings=float(input("Enter the percentage of salary for savings:"))
list.append(psavings)
pRent=float(input("Enter the percentage of salary for Rent:"))
list.append(pRent)
pelectricity= float(input("Enter the percentage of salary for electricity:"))
list.append(pelectricity)

if i==0:
   savings=(psavings/100)*salary
   list.append(savings)
elif i==1:
   Rent=(pRent/100)*salary
   list.append(Rent)
elif i==2:
   electricity=(pelectricity/100)*salary
   list.append(electricity)
   total=savings+Rent+electricity
list.append(total)

remainder=salary-total
list.append(remainder)

yearlyrent = Rent * 12
list.append(yearlyrent)
yearlyelectricity=electricity * 12
list.append(yearlyelectricity)

totalsalary=pow(salary,2)
list.append(totalsalary)
