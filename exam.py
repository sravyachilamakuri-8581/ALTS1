def add(add):
    a=10;
    b=20;
    print(a+b)

def sub():
    a=10
    b=20
    print(a-b)

def mul():
    a=10
    b=20
    print(a*b)

def div():
    a=10
    b=20
    print(a/b)
print("****Welcome****")
flag="y" #assigning the flag
while (flag=="y"):
    print("1-Add")
    print("2-subtract")
    print("3-Multiplication")
    print("4-Division")
    print("5-Exit")
    choice=int(input("Enter your choice:"))
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    if choice==1:
       add()
    elif choice==2:
       sub()
    elif choice==3:
       mul()
    elif choice==4:
       div()
    else:
        print("Good Bye")
    flag=input("Do you want to flag(y/n)")
    print(flag)
    if flag=="n":
        print("thankyou")
     
