'''
NAME
       Contar A, C, G, T en una secuencia

VERSION
       1.0

AUTHOR
       Paloma Lara <palomalf86@gmail.com>

DESCRIPTION
       Cuenta el numero de A, C, G, T que contiene una secuencia

CATEGORY
       an assigned category

USAGE
       program [OPTIONS]

ARGUMENTS

SOFTWARE REQUERIMENTS

IMPUT
     Requiere como imput poner una secuencia entre comillas en terminal

OUTPUT
     Indica el numero de A, C, G, T 

CREATION DATE
     28/04/2021
     
LOCALIZACION EN GIT https://github.com/larafp86/Templates



'''
#pide la secuencia
print('La secuencia de DNA es: \'por favor poner secuencia entre comillas\'')

#la asigna a la variable DNA_sequence
DNA_sequence=input()

#cuenta el numero de cada nucleotido
Num_A_in_sequence=DNA_sequence.count("A")
Num_C_in_sequence=DNA_sequence.count("C")
Num_G_in_sequence=DNA_sequence.count("G")
Num_T_in_sequence=DNA_sequence.count("T")

#imprime el resultado
print('el contenido de A es: ' + str(Num_A_in_sequence) + '\nel contenido de C es: ' + str(Num_C_in_sequence)+ '\nel contenido de G es: ' + str(Num_G_in_sequence) + '\nel contenido de T es: ' + str(Num_T_in_sequence))


