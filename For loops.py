for i in range(1,11):
  print(i)
Members = ["Marwan","Esraa","Kassem","Farida","Mazen"]
for j in Members:
    print(f" Weclome, {j}!")
for x in range (0,1000,5):
   print(x)
#to make numbered list from the array
for bambaz, j in enumerate(Members):
   print(f"{bambaz + 1}.{j}")
#you can use any variable it depends mainly on enumerate

#nested loops 
for m in range(2):
   for n in range(3):
      print(f" 1st number={m},2nd number={n}")
