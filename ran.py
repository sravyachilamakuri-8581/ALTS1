start=int(input("enter the start range:"))
end=int(input("enter the end range:"))
if start>end:
    print ("start value should be greater than end value")
else :
    for x in range (start,end,3):
        print (x)
        
