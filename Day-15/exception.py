#single exception
try:
    if a>10:
        print("good")

except NameError:
    print("a is not defined")
else:
    print("no errors")

finally:
    print("end of block")
