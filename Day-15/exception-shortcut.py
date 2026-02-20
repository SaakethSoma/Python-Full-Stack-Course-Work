'''
try:
    a=a+'8'
    print(a[4])
except(NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError)as e:
    print(f'error occured:{e}')

else:
    print('no errors')
finally:
    print('end of block')
'''

'''
try:
    a=int(input())
    print(a[4])
except Exception as e: #just give exception it will handle all errors
    print(f'error occured:{e}')

else:
    print('no errors')
finally:
    print('end of block')
'''


try:
    a=int(input())
    if a<0:
        raise Exception("enter the positive value") #raise is used for rasing error explicitly
except Exception as e:
    print(f'error occured:{e}')
else:
    print('no errors')
finally:
    print('end of block')
    
