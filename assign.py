def dtype_menu():
	print("Available dataypes ")
	print("1: int \n 2: float \n 3: string \n 4: list \n 5: tuple \n 6: dictionary \n 7: set ")
	dtype_val=	int(input("Enter the datatype choice of the value: "))
	return dtype_val

def my_dictionary():
    d = {}
    no_of_keys = int(input("Enter no of keys to the dictionary"))

    for i in range(no_of_keys):
        key = input("Enter the key: ")
        dtype_val = dtype_menu()
        
        if (dtype_val == 1):
            value= input("Enter the value: ")
            d[key] = int(value)		
        elif (dtype_val == 2):
            value= input("Enter the value: ")
            d[key] = float(value)		
        elif (dtype_val == 3):
            value= input("Enter the value: ")
            d[key] = value
        elif (dtype_val == 4):
            value = input('Enter the elements of the list: ').split(" ")
            temp =[]
            for i in value:
                temp.append(value)
            d[key] = temp    
        elif (dtype_val == 5):
            value = input('Enter the elements of the list: ').split(" ")
            temp_list = ()
            temp = list[temp_list]
            for i in value:
                temp.append(value)
            temp_tuple = tuple(temp)
            d[key] = temp_tuple   
            
        elif (dtype_val == 6):
             d[key] = my_dictionary()		
        elif (dtype_val == 7):
            pass		
        else:
            print("Invalid datatype encountered")
	
    print(d.items())
    return d
        
		
my_dictionary()		








keys = ['employee_id','employee_name','account_number','salary','address','awards','subjects_enrolled']
values = [1,'test',23,23.20,{'home_address' : 'Pune' , 'work_address' : 'mumbai'},['employeeOfTheYear','StarOfTheMonth'],('Physics','Chemistry')]
        
d = {}
for i in range(len(keys)):
    d[keys[i]]= values[i]   
    print(d)