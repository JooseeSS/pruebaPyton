def highest_number (num1, num2, num3) :
    if num1 >= num2 and num1 >=num3:
        highest=num1
    elif  num2 >= num1 and num2 >=num3 :
        highest=num2
        
    else:
        highest=num3
           
    return highest

first_num = int(input("introduce el primer numero"))
second_num = int(input("introduce el segundo numero"))
third_num = int(input("introduce el tercer numero"))

print("the highest is " + str(highest_number(first_num, second_num, third_num)))

