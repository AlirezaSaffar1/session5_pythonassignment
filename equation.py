import math
def equation():
    print("Welcome to second degree equation solver.")
    while True:
        user_input = input("what do you want?    1.start    2.exit    ")
        if user_input == "1" :
            a = float(input("enter a: "))
            b = float(input("enter b: "))
            c = float(input("enter c: "))
            delta = b**2 - 4*a*c

            if a == 0:
                print("this is not a second degree equation")
            else:
                if delta < 0:
                    print("your equation doesn't have real roots")
                elif delta == 0 :
                    x = -b / (2*a)
                    print("your equation has one conj root:" , x)
                elif delta > 0:
                    x1 = (-b + math.sqrt(delta)) / (2*a)
                    x2 = (-b - math.sqrt(delta)) / (2*a)
                    print("your equation has two real roots: " , x1 , x2)
        elif user_input == "2":
            print("Goodbye!")
            break
        else:
            print("Error!")
equation()                                      