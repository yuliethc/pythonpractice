def data():
    """ Input first and last name, combine to one string and print 
        Also, input the city and state and print."""
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    fullname = fname + " " + lname
    city = input("Enter the city where you live: ")
    state = input("Enter the state where you live: ")
    fullname = fname + " " + lname
    location = city + "," + state



    print("Your name is:", fullname)
    print("Your location is:", location)

data();
