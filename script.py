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
for i in range (3):
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
additionalamount=random.uniform(1,50)
list.append(additionalamount)
remainingamount= (additionalamount) / (savings)
list.append(remainingamount)

print("\nResults for the month of", month, ":")
print(f"Amount allocated to savings: ${savings:.2f}")
print(f"Amount allocated to rent: ${Rent:.2f}")
print(f"Amount allocated to electricity: ${electricity:.2f}")
print(f"Total expenses (savings, rent, and electricity): ${total:.2f}")
print(f"Remainder of salary after expenses: ${remainder:.2f}")
print(f"Yearly rent cost: ${yearlyrent:.2f}")
print(f"Yearly electricity cost: ${yearlyelectricity:.2f}")
print(f"Your salary squared : ${totalsalary:.2f}")
print(f"How much would be left if the random savings of $50 is divided by the total allocated savings: {remainingamount:.2f}")
print (list)
