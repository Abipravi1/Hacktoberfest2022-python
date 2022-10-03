print("String Array Operations in Python")

array = []
choice=0;
n = int(input("Enter the number of elements string array : "))
for i in range(n):
    array.append(input())
while(choice!=6):
    print("The current array is",array)
    
    print("Choose the operation you want to perform on the string array")
    choice = int(input("1.Append 2.Count 3.Index 4.Insert 5.Print 6.Quit"))
    
    if(choice==1):
        try:
            array.append(input("Enter the string to append"))
        except:
            print("Could not perform the operation")
    if(choice==2):
        temp=input("Enter the element to count")
        try:
            print("The count is:",array.count(temp))
        except:
            print("The element is not in the array")
    if(choice==3):
        temp=input("Enter the element to find index the array")
        try:
            print("Array index is:",array.index(temp))
        except:
            print("The element is not in the array")
    if(choice==4):
        try:
            array.insert(int(input("Enter the index value: ")),input("Enter the element to insert"))
        except:
            print("Could not perform operation with the above input")
    if(choice==5):
        print("The current array is",array)

