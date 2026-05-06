# python program to find student Grade
english = float(input("please enter the english marks:"))
math = float(input("please enter the math score: "))
computers = float(input("please enter the computer marks: "))
physics = float(input("please enter the physics marks:"))
chemistry = float(input("please enterb the chemistry marks:"))
if english>100 and math>100 and computers>100 and physics>100 and chemistry>100:
    print("one of the marks is greater than 100.... please check and enter valid value")
else:
      total = english + math + computers + physics + chemistry
      percentage = (total / 500) * 100
      print("Total Marks = %.2f" %total)
      print("Marks percentage = %.2f" %percentage)
      if(percentage >= 90):
         print("A Grade")
      elif(percentage >= 80):
         print("B Grade")
       elif(percentage >= 70):
         print("C Grade")
     elif(percentage >= 60):
         print("D Grade")
      elif(percentage >= 40):
         print("E Grade")
     else:
         print("Fail")
           
        
        
        
