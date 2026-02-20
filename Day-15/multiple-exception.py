#multiple exception(TRY,EXCEPT,ELSE,FINALLY)
try:
    if 10/0:
        print("good")

except NameError:
    print("a is not defined")
except ValueError:
    print("enter the requested data type")
except TypeError:
    print("data types are different")
except ZeroDivisionError:
    print("cant divide with zero")
except IndexError:
    print("the index is not present")
except KeyError:
    print("in dict this key is not present")
    
else:
    print("no errors")

finally:
    print("end of block")
