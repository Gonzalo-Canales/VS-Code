""" PROYECTO_01 """
#
# AGENDA CONTACTOS: Registro de contactos donde el usuario puede agregar nombre, teléfono, correo y dirección para cada contacto.
# El usuario puede modificar o eliminar los contactos existentes.
# El usuario puede buscar contactos por nombre o número de teléfono.
#
""" Creación Agenda: Lista - Diccionarios """
agenda = [] # Creación Lista Vacía
#
""" Defino FUNCIONES que trabajarán con la AGENDA """
#
""" FUNCIÓN 1: Agregar Contacto """
def agregar_contacto():
    print("🆔")
    nombre = input("Escribe el nombre del Nuevo Contacto (o escribe SALIR para terminar): \n")
    if nombre.lower() == "salir":
        print("-->> Cerrando Agenda...")
        return # Sale de la función sin agregar un Contacto
    # Si no
    print("📞")
    celular = input("Escribe el número telefónico del contacto: \n")
    #
    print("📧")
    correo = input("Escribe el correo electrónico del contacto (o ENTER si NO deseas agregar): \n")
    if not correo:
        correo = "VACÍO"
    else:
        correo = correo.lower()
    #
    print("🏠")
    add = input("Escribe la dirección del contacto (o ENTER si NO deseas agregar): \n")
    if not add:
        add = "VACÍO"
    else:
        add = add.title()
    #
    """ Agrega a la Agenda (Lista) un nuevo diccionario anidado en otro diccionario
        con Nombre, Número Telefónico, Correo electrónico y Dirección particular según se requiera"""
    agenda.append({ nombre.title(): {
                                        "number": celular,
                                        "email": correo,
                                        "address": add
                                    }
                })
    print("\n ✅ Contacto Agregado Correctamente")
#
""" FUNCIÓN 2: Buscar un Contacto a partir de Nombre o Número Telefónico """
def buscar_contacto():
    dato = input("Ingresa Nombre o Número Telefónico del Contacto que quieres BUSCAR: ").strip() # .strip() limpia la búsqueda del usuario
    encontrado = False       # No se ha encontrado aún
    for contacto in agenda:  # Bucle para buscar un contacto sin saber su posición
        for nombre, datos in contacto.items():
            if nombre.lower() == dato.lower() or datos["number"] == dato:
                print(f"""
                📝 Contacto Encontrado 📝
                🆔 Nombre: {nombre}
                📞 Número: {datos['number']}
                📧 Email: {datos['email']}
                🏠 Dirección: {datos['address']}
                """)
                encontrado = True
                return # Sale de la función luego de Encontar un Contacto
    if not encontrado:
        print("❌ Contacto NO Encontrado ❌")
#
""" FUNCIÓN 3: Modificar un Contacto a partir de un Nombre """
def modificar_contacto():
    target = input("Ingresa el nombre del contacto que quieres MODIFICAR: ").strip().title() # Cadena de .strip().title() limpia la búsqueda del usuario
    modificado = False       # No se ha modificado aún
    for contacto in agenda:
        if target in contacto:
            #
            nombre_new = input("🆔 Nuevo nombre (ENTER para mantener): ").strip().title()
            number_new = input("📞 Nuevo número (ENTER para mantener): ")
            email_new = input("📧 Nuevo email (ENTER para mantener): ")
            add_new = input("🏠 Nueva dirección (ENTER para mantener): ")
            #
            if nombre_new: # Si fue ingresado un dato
                contacto[nombre_new.title()] = contacto.pop(target)
                target = nombre_new.title()  # Actualiza el Nombre
            #
            if number_new:  # Si fue ingresado un dato
                contacto[target]["number"] = number_new
            if email_new:   # Si fue ingresado un dato
                contacto[target]["email"] = email_new
            if add_new:     # Si fue ingresado un dato
                contacto[target]["address"] = add_new.title()
            #
            print("✅ Contacto modificado con éxito")
            modificado = True
            return # Sale de la función
    # Si no encuentra el Contaco a modificar
    if not modificado:
        print("❌ Contacto NO Encontrado ❌")
#
""" FUNCIÓN 4: Eliminar un Contacto a partir de un Nombre """
def eliminar_contacto():
    target = input("Ingresa el nombre del contacto que quieres ELIMINAR: ").strip().title() # Cadena de .strip().title() para limpiar la búsqueda del usuario
    eliminado = False       # No se ha eliminado aún
    for contacto in agenda:
        if target in contacto:
            agenda.remove(contacto) # Se remueve el diccionario "contacto" para el nombre ingresado
            print(" 🗑️ Contacto ELIMINADO Correctamente 🗑️")
            eliminado = True
            return
            #
    if not eliminado:
        print("❌ Contacto NO Encontrado ❌")
#
#
#
""" Continuación del Proceso a partir de las Funciones predefinidas """
#
option = "0"
#
while option != "5":

    print ("\n")
    print ("¿QUÉ DESEA HACER?:")
    option = input("Para AGREGAR un Contacto: Digita 1 \nPara BUSCAR un Contacto: Digita 2 \nPara MODIFICAR un Contacto: Digita 3 \nPara ELIMINAR un Contacto: Digita 4 \nPara SALIR: Digita 5\n")
    print ("\n")

    if option == "1":
        agregar_contacto()

    elif option == "2":
        buscar_contacto()

    elif option == "3":
        modificar_contacto()

    elif option == "4":
        eliminar_contacto()

    elif option == "5":
        print("-->> Guardando Agenda...✅")

    else:
        print("❌ Opción no válida, intenta de nuevo.")
        print ("\n")
    #
if option == "5":
    print("-->> Cerrando...✅")
#
