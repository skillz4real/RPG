def ui()->tuple():
    """Returns tuple of bools for symboles,digits and an int for len of pwd"""

    while True:
        minchar=4
        print("Please enter Y to enable any of these options.")
        print("Or leave blank to disable.")
        print("Hit Ctrl+C at anytime to quit")
        s=bool(input("Add symboles? ").rstrip())
        d=bool(input("Add digits? ").rstrip())
        l=input("Please enter the length of your password as an integer: ").rstrip()
        try:
            l=int(l)
        except:
            print("Please enter a integer!!")
        if type(l) is not int:
            print("Let's retry!")

        elif l<4:
            print("Please input a number bigger than 4. Pro Tip you don't want a password that short!")
        else:
            return s,d,l
            
       

    
