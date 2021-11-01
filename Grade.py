marks = int(input("Enter your marks:"))
if(marks >=90):
    print("Congras!, Your Grade is A+")
elif(marks <90 and marks >=80):
    print("Your grade is A")   
elif(marks <80 and marks >=70):
    print("Your grade is A-")    
elif(marks <70 and marks >=65):
    print("Your grade is B+")    
elif(marks < 65 and marks >=60):
    print("Your grade is B")    
elif(marks < 60 and marks>=50):
    print("Your grade is B-")     
elif(marks <50 and marks >= 40):
    print("Your grade is C")  
else:
    print("Sorry! you are fail")      
