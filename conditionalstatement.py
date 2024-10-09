age = int(input("What is the attendee's age?" ))
member = input("Is the attendee a member?")

if age < 18:
    if member == "Yes":
        print("total fee is 450.00 pesos")
    else:
        print("total fee is 650.00 pesos")
      
elif age >=18 and age<=65:
    if member == "Yes":
        print("total fee is 550.00 pesos")
    else:
        print("total fee is 750 pesos")

elif age >=65:
    if member: "Yes"
    print("total fee is 400 pesos")

else: 
    print("total fee is 600 pesos")