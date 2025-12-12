def Grade_Boundries():
    Grade=input(" Enter the exam percentage: ")
    if Grade.isdigit() : 
      Grade=int(Grade) 
      if Grade>=0 and Grade<=100 :
         if Grade >= 90: 
             print("Your Grade is : A* ")
         elif Grade >= 80:
             print("Your Grade is : A ")
         elif Grade >= 70:
             print("Your Grade is : B ")
         elif Grade >= 60:
             print("Your Grade is : C ")
         elif Grade >= 50:
             print("Your Grade is : D ")
         else:
             print("You Failed! Your Grade is : F ")
      else:
          print("invalid percentage,please try again") 
          Grade_Boundries()
    else:
          print("Please enter integers")
          Grade_Boundries()

def Repeating():
   Complete=str(input("Do you want to insert another grade ? "))  
   Complete=Complete.upper().strip() 
   if Complete ==("YES"):
        Grade_Boundries()
        Repeating()
   else:
        print("Thank you! ")

Name = input("Please enter your name ")
print(f"Hello {Name}, Hope you're doing well ")
Grade_Boundries()
Repeating()

