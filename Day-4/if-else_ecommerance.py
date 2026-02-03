products=['shirts','handbags','laptop','facewash','heels']
search=input("enter the item:")

if search in products:
    print(f'{search} is found!\n Go and shop now!!!')
else:
    print(f"{search} not found!\n Look for other things")
