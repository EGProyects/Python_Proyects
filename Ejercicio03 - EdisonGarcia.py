#Desarrolle un programa que capture una lista de listas de personas con su nombre y apellido, edad y tipo de sangre. 
#Se debe validar este último dato de acuerdo a la lista proporcionada a continuación:  tipos_de_sangre_permitidos = ["A+", "B+", "A-", "B-", "O+", "O-", "AB+", "AB-"]. 
#Una vez capturada la información, el programa debe permitir lo siguiente:

#Mostrar el listado capturado.
#Filtrar personas por tipo de sangre y devolver las personas correspondientes a dicho tipo de sangre.

lista_pacientes = []
'''
Esta funcion permite tomar la informacion de registro de los pacientes y agregarlo a una lista de listas
'''
def registro_paciente():
    nombre_completo = str(input('Favor ingrese el nombre y apellido de la persona que desea registrar: '))
    edad = int(input('Favor ingrese la edad, en numeros, de la persona: '))
    sangre = str(input('Favor ingresar el tipo de sangre de la persona (A+, B+, A-, B-, O+, O-, AB+, AB-): '))
    while (sangre != 'A+' and sangre != 'B+' and sangre != 'A-' and sangre != 'B-' and sangre != 'O+' and sangre != 'O-' and sangre != 'AB+' and sangre != 'AB-'):
        print('El tipo de sangre ingresado no es valido.')
        sangre = str(input('Favor ingresar el tipo de sangre de la persona (A+, B+, A-, B-, O+, O-, AB+, AB-): '))
    info_paciente = [nombre_completo, edad, sangre]
    lista_pacientes.append(info_paciente)
registro = str(input('Desea registrar a alguien? (si/no) '))
'''
Este loop realiza el procesamiento de registro de los pacientes hasta que el usuario decida que no va a registrar mas usuarios'
'''
while registro == 'si' or registro == 'Si' or registro == 'SI':
    registro_paciente()
    registro = str(input('Desea registrar a alguien mas? (si/no) '))
'''
Esta loop con condicional relaciona la lista_pacientes para poder hallar el tipo de sangre de cada uno y poder filtrar los pacientes con ese criterio
'''
info_sangre = str(input('Desea verificar el tipo de sangre de los pacientes? (si/no) '))
while info_sangre == 'si' or info_sangre == 'Si' or info_sangre == 'SI':
    sangre_deseada = str(input('Accesando al registro de sangre. Si el registro no tiene pacientes con el tipo de sangre, le resurgira la pregunta. Favor indicar el tipo de sangre deseada de los paciente(s). (A+, B+, A-, B-, O+, O-, AB+, AB-): '))
    for paciente in lista_pacientes:
        if paciente[2] == sangre_deseada:
            print(paciente)
    info_sangre = str(input('Desea verificar el tipo de sangre de los pacientes? (si/no) '))
'''
Esta condicional con loop permite ver la lista de pacientes mas claramente al imprimirla en estilo columna 
'''
info_pacientes = str(input('Desea acceder a los registros de informacion de los pacientes? (si/no) '))
if info_pacientes == 'si' or info_pacientes == 'Si' or info_pacientes == 'SI':
    for pacientes in lista_pacientes:
        print(pacientes)
    print('Gracias por utilizar nuestros servicios!')
else:
    print('Gracias por utilizar nuestros servicios!')

    
        
