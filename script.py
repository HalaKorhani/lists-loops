import random 


list=[]
action=True
while action==True :
   month_data={}

   salary=int(input("input your salary for the month"))
   month_data['Salary'] = salary

 
   month=input("enter the name of the month")
   month_data['Month'] = month
  
   psavings=float(input("Enter the percentage of salary for savings:"))
   month_data['Savings%'] = psavings
   
   pRent=float(input("Enter the percentage of salary for Rent:"))
   month_data['Rent%'] = pRent
   
   pelectricity= float(input("Enter the percentage of salary for electricity:"))
   month_data['Electricity%'] = pelectricity
  
   for i in range (3):
     if i==0:
      savings=(psavings/100)*salary
      month_data['Savings Amount'] = savings

     
     elif i==1:
      Rent=(pRent/100)*salary
      month_data['Rent Amount'] = Rent
    
     elif i==2:
      electricity=(pelectricity/100)*salary
      month_data['Electricity Amount'] = electricity
     
      total=savings+Rent+electricity
      month_data['Total Expenses'] = total
    
      
      remainder=salary-total
     
      month_data['remainder'] = remainder

      yearlyrent = Rent * 12
      month_data['Yearly Rent'] = yearlyrent
      
      yearlyelectricity=electricity * 12
      month_data['Yearly Electricity'] = yearlyelectricity
   

      totalsalary=pow(salary,2)
      month_data['Salary Squared'] = totalsalary

      
      additionalamount=random.uniform(1,50)
      month_data['Additional Amount'] = additionalamount
     
      remainingamount= (additionalamount) / (savings)
      month_data['Remaining Amount'] = remainingamount
      
      list.append(month_data)
    

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
      continue_input = input("Do you want to compute another month? (yes/no): ")
      if continue_input != 'yes':
        print("Exiting the program.")
        action=False
        break
        print("\nSummary of all months entered:")
for month_data in list:
    for key, value in month_data.items():
        print(f"{key}: {value}")

