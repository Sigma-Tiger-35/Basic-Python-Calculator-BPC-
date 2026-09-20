#Calculator

# Loop start

while True:

    print()
    
    print("Python Calculator version 1.0\n")

    print("For Basic Calculator = 1")
    print("For Angle Unit Converter = 2")
    print("For Temperature Unit Converter = 3")

    #Input to change calculator

    cc = int(input("Choose Calculator:- "))

    if cc == 1:

        #Basic Calculator

        #Input from user for Basic Calculator

        print()
        
        print("Basic Calculator\n")

        a = float(input("Enter First Value: "))
        b = float(input("Enter Second Value: "))

        print("+ = Addition")
        print("- = Subtract")
        print("/ = Division")
        print("// = Floor Division")
        print("* = Multiplication")
        print("** = Exponent")
        print("> = Greater than")
        print("< = Less than")
        print("% = Modulo (Remainder Calculator)")
        print("== = Equal to")
        print("!= = Not Equal to")
        print(">= = Greater than or Equal to")
        print("<= = Less than or Equal to")

        x = input("Enter Operator (+, -, /, //, *, **, >, <, %, ==, !=, >=, <=): ")

        #Operators

        if x == "+":
            result = a + b
        elif x == "-":
            result = a - b
        elif x == "/":
            result = a / b
        elif x == "//":
            result = a // b
        elif x == "*":
            result = a * b
        elif x == "**":
            result = a ** b
        elif x == "%":
            result = a % b
        
        #Boolean Camparison Operators

        elif x == ">":
            result = a > b
        elif x == "<":
            result = a < b
        elif x == "==":
            result = a == b
        elif x == "!=":
            result = a != b
        elif x == ">=":
            result = a >= b
        elif x == "<=":
            result = a <= b

        #Error Invalid Operator

        else:
            result = "(Invalid Operator Error #1)"

        #printing operation

        print(f"{a} {x} {b} = {result}")
        
        print(result ," is your desired answer.")

    #Angle Unit Converter

    elif cc == 2:
        
        #Input from user

        print()

        print("Angle Unit Converter\n")

        angle = float(input("Enter Angle:- \n"))

        print("Choose Units:- \n")

        print("Convert Degrees to Radians by pressing 1")
        print("Convert Radians to Degrees by pressing 2")
        print()
        unitangle = int(input("Choose Units:- "))

        if unitangle == 1:
            Aresult = angle * 3.14159265358979323846264338327950288419716939937510/180
            print()
            print(Aresult,"Radians.")
        
        elif unitangle == 2:
            Aresult = angle * 180/3.14159265358979323846264338327950288419716939937510
            print()
            print(Aresult,"° Degrees.")
        
        else:
            print("Invalid Unit Error #4")

    #Temperature Unit Converter

    elif cc == 3:
        
        print()

        print("Temperature Unit Converter\n")

        t = float(input("Enter Magnitude (Value):- \n"))

        print("Choose Units:- \n")

        print("Convert Celsius (°C) into Fahrenheit (°F) by pressing 1")
        print("Convert Fahrenheit (°F) into Celsius (°C) by pressing 2")
        print("Convert Celsius (°C) into Kelvin (K) by pressing 3")
        print("Convert Fahrenheit (°F) into Kelvin (K) by pressing 4")
        print("Convert Kelvin (K) into Fahrenheit (°F) by pressing 5")
        print("Convert Kelvin (K) into Celsius (°C) by pressing 6")
        print()
        cu = int(input("Choose Units:- "))

        if cu == 1:
            Tresult = (t * 1.8 + 32)
            print()
            print(Tresult,"°F")
            print()
            print(Tresult,"°Fahrenheit is your desired answer.")
        
        elif cu == 2:
            Tresult = (t - 32) * 5/9
            print()
            print(Tresult,"°C")
            print()
            print(Tresult,"°Celsius is your desired answer.")
        
        elif cu == 3:
            Tresult = (t + 273.15)
            print()
            print(Tresult," K")
            print()
            print(Tresult," Kelvin is your desired answer.")

        elif cu == 4:
            Tresult = (t + 459.67) * 5/9
            print()
            print(Tresult," K")
            print()
            print(Tresult," Kelvin is your desired answer.")
        
        elif cu == 5:
            Tresult = (t * 9/5 - 459.67)
            print()
            print(Tresult,"°F")
            print()
            print(Tresult,"°Fahrenheit is your desired answer.")
        
        elif cu == 6:
            Tresult = (t - 273.15)
            print()
            print(Tresult,"°C")
            print()
            print(Tresult,"°Celsius is your desired answer.")
        
        #Error for Invalid Units

        else:
            print("Invalid Units Error #3")

    #Error For Invalid Calculator Request
    
    else:
        print("Invalid Calculator Request Error #2")
    
    #looping end request

    ask = input("Do you want to continue? (yes or no): ").lower()
    
    if ask == "no":
            
        break