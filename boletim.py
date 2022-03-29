name= input('Name:')
grade= input('Grade:')
math_grade= input('Math grade:')
port_grade= input('Portuguese grade:')
socio_grade= input ('Sociology grade:')
average= (float(math_grade) + float(port_grade) + float(socio_grade)) / 3

print(name)
print(grade)
print(math_grade)
print(port_grade)
print(socio_grade)
print(average)

if average > 7: 
    print('Congrats, you are approved')
else: 
    print('Sorry, you did not pass')

