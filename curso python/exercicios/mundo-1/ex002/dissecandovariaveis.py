a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('só tem espaços? ',a.isspace())
print('é númerico? ',a.isnumeric())
print('é alfabético? ',a.isalpha())
print('é alfanúmerico? ',a.isalnum())
print('Só ta em maiúsculas? ',a.isupper())
print('Só ta em minúsculas? ',a.islower())
print('Esta capitalizada?',a.istitle()) #capitalizada(nem maiusculas nem minusculas)