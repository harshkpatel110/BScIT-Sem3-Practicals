sgpi = float(input("Enter SGPI: "))
if sgpi > 10:
    print("Invalid SGPI")
elif sgpi >= 9:
    print("Grade: O")
elif sgpi >= 8:
    print("Grade: A+")
elif sgpi >= 7:
    print("Grade: A")
elif sgpi >= 6:
    print("Grade: B+")
elif sgpi >= 5.5:
    print("Grade: B")
elif sgpi >= 5:
    print("Grade: C")
elif sgpi >= 4:
    print("Grade: P")
elif sgpi >= 0:
    print("Grade: F")
else:
    print("Invalid SGPI")