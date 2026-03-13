print("\nWelcome to the Pattern Generator and Number Analyzer!")
while True:
  

 print("\nSelect an option: ")
 a = int(input("1.Generate a pattern \n2.Analyze a Range of number \n3.Exit\nEnter your choice: "))
   
   
 match a:
    case 1:
        sub = int(input("\nSelect 1 to print left aligned triangle: \nSelect 2 to print a pyramid: \nSelect 3 to print right aligned triangle: \nEnter your choice: "))
        match sub:
           case 1:
                     for i in range(1,6):
                      for j in range(i):
                       print("*",end="")
                      print()
           case 2:
                for i in range(1,6):
                 print(" "*(6-i), end=" ")    #pyramid
                 for j in range(i):
                  print("*", end = " ")
                 print()
           case 3:
              for i in range(1,6):
               for j in range(i,6):
                print(" ", end="")
               for k in range(1,i+1):
                print("*", end="")
               print()
    case 2:
      m = int(input("Enter the start of the range: "))
      n = int(input("Enter the end of the range: "))
      for i in range(m , n+1):
       if i%2 == 0:
        print(f"Number {i} is Even")
       else:
        print(f"Number {i} is Odd")
      s = 0
      for i in range(m,n+1):
        s = s+i
      print(f"Sum of all numbers from {m} to {n} is: {s}")
      
    case 3:
      print("Exiting the program. Goodbye!")
      break


    
            
      
      
          
           
                