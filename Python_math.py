
number = int(input('number'))
number_1 = int(number / 1000)
number_2 = int(number / 100) % 10
number_3 = int(number / 10) % 10
number_4 = int(number % 10) 
result = (number_4*1000)+(number_3*100)+(number_2*10) + number_1 
print(result)