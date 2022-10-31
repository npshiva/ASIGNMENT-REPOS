class MultiFunctions():
    def Subfields():
        print("Sub-Fields in AI are: ")
        subFields=["machine learning", "neural networks", "Vision", "Robotics", "Speech processing", "Natural language processing"]
        for List in subFields:
            print(List)




    def OddEven():
        num=int(input("Enter the number: "))
        if ((num%2)==0):
            print(num, "is even number")
            message="even number"
        else:
            print(num, "is odd number")
            message="odd number"
     


    def Eligible():
        Gender=str(input("Your Gender: "))
        Age=int(input("Your age: "))
        if ((Gender=="Male") and (Age>=21)):
            print("Eligible")
            msg="Eligible"
        elif ((Gender=="Female") and (Age>=18)):
            print("Eligible")
            msg="Eligible"
        else:
            print("Not Eligible")
            msg="Not Eligible"
            return msg
       
    
    

    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total : ",Total)
        Percentage_cal=(Total/500)*100
        print("Percentage : ",Percentage_cal)
        return Percentage_cal
    



    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        Area=(Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",Area)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth2=int(input("Breadth: "))
        Perimeter=Height1+Height2+Breadth2
        print("Perimeter formula: Height1+Height2+Breadth2")
        print("Perimeter of triangle: ",Perimeter)
        return Area
        
    