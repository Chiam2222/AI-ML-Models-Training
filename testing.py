password = "staff123"
count = 3
for i in range(0,3):
    passwordEntered = input("Please enter staff password: ")
    if passwordEntered == password:
        print("Yes, correct")
        break
    else:
        count-=1
        print("Wrong password try again, you have left", count, "tries")
        if count == 0:
            print("sent email")
