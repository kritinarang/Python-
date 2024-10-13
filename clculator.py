while(True):
    x=int(input("enter 1st number\n"))
    y=int(input("enter 2nd number\n"))
    op=input("enter \n+ for addition\n- for subtraction\n* for multiplication\n / for divide\n")
    if op=="+":
        print("addition is ",x+y)
    elif op=="-":
        print("subration is ",x-y)
    elif op=="*":
        print("multiplication is ",x*y)
    elif op=="/":
        print("division is ",x/y)
    else:
        print("invalid input")
    loop=input("do you want to continue y or n")
    if loop=="n" or loop=="N":
        break