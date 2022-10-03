# NOMBRE:  Edwin Calle Perez
# CARRERA: Ing. De Sistemas
# MATERIA: sis420
# funcion muestra el menu principal.
def mostrar_menu(opciones):
    print('Práctica 01:')
    print('Seleccione una opción:')
    for n in sorted(opciones):
        print(f' {n}: {opciones[n][0]}')


# recibe el valor que ingresa y valida que este en opciones, ciclo se repite si no ingresa un numero de opcion valido
def leer_opcion(opciones):
    while (a := input('Seleccione una Opción : ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo con una valida.')
    return a


# ejecuta la opcion que se ingresa
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


# la funcion que genera el menu, Muestra el menu y manda el numero de opcion para que se ejecute
def generar_menu(opciones):
    opcion = None
    while opcion != '1' or '2':
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)


def menu_principal():
    opciones = {
        '1': ('Imprimir biografía', accion1),
        '2': ('Salir', salir)
    }
    generar_menu(opciones)


# funcion que contiene, lista y diccionario con datos. que se imprimen con print
def accion1():
    linea = ('=================================\n')
    print(linea, 'BIOGRAFIA:')
    biografia = [
        'Mi nombre es Edwin, estoy cursando la materia SIS420, Inteligencia artificial de Carrera Ing. De Sistemas. En la USFX.',
        'Esta es la practica01 de la materia', 'y se esta imprimiendo esta informacion en PYCharm IDE']
    print(biografia[0], biografia[1], biografia[2])

    print('MIS DATOS:')
    mis_datos = {'Nombre': 'EDWIN', 'Apellidos': 'CALLE PEREZ','asignatura':'SIS420','Carrera': 'ING DE SISTEMAS','programa':'PYCharm'}
    print('NOMBRE:', mis_datos['Nombre'])
    print('APELLIDOS:', mis_datos['Apellidos'])
    print('MATERIA:', mis_datos['asignatura'])
    print('CARRERA:', mis_datos['Carrera'])
    print('PROGRAMADO EN:', mis_datos['programa'])
    print(linea)


# funcion que se ejecuta si selecciona opcion 2:salir , vuelve a mostrar el menu principal
def salir():
    print('\nSaliendo.............!!!!!!\n')


if __name__ == '__main__':
    menu_principal()