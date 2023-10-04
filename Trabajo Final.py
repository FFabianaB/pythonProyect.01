"""
Trabajo final integrador. 
Alumna Buchieri Franca Fabiana. 
DNI 37107574 
Comisión 23441
"""



trabajadores={
37107574: ["Fabiana", 30, "programador", True],
40107574: ["Paula", 60, "arquitecto", False],
30107574: ["Juan", 20, "abogado", False],
20107574: ["Raul", 40, "ingeniero", True],
10107574: ["Pedro", 22, "programador", False],
}

def separador():
  print ("=" * 30)
  print ("*" * 30)
  print ("=" * 30)
  
def agregarUser():
  dni=int(input("Ingrese el DNI del nuevo usuario:\n"))
  while dni in trabajadores:
    dni=int(input("DNI en uso. Ingrese un DNI diferente:\n"))
  nombre=input("Ingrese el Nombre:\n").title()
  edad=int(input("Ingrese la Edad:\n"))
  profesion=input("Ingrese la Profesion:\n").lower()
  actividad=input("¿Se encuentra activo en el rubro? [Si/No]:\n").lower()
  while actividad not in ["s","si","n","no"]:
    actividad=input("Responder Si o No:\n").lower()
     
  if actividad  in ["si","s"]:
    actividad= True
  else:
    actividad= False
    
  trabajadores[dni] = [nombre, edad, profesion, actividad]
  print("¡Nuevo Trabajador añadido exitosamente!\n...Volviendo al menu")

def eliminarTrabajador():
    x=int(input("Ingrese el DNI del trabajador a eliminar\n"))
    if x in trabajadores:
        print(f"\n#####¡{x} Fue eliminado exitosamente!#####\n")
        del(trabajadores[x])
        menuSecundario()
    else:
        print(f"{x} No fue encontrado, volviendo al menu\n")
        menuSecundario()

def trabajadoresDesocupados():
    for clave in trabajadores:                          
        if False in trabajadores.get(clave):
            print(f"{clave}: Esta desocupado actualmente")
            
def verInfo():
    x=int(input("Ingrese el DNI del usuario para consultar su informacion\n"))
    if x in trabajadores:
        print(f"\nDNI: {x}\nNombre: {trabajadores[x][0]}\nEdad: {trabajadores[x][1]}\nProfesion: {trabajadores[x][2]}")
        if trabajadores[x][3]== True:
            print("Se encuentra activo")
        else:
            print("Se encuentra inactivo")             
    else:
        print(f"{x} No fue encontrado")
        
    preguntaFinal()

def modificarUser():
    dni=int(input("Ingrese el DNI del trabajador para EDITAR su informacion\n"))

    if dni in trabajadores:
        opcion=input("[1] Modificar Nombre\n[2] Modificar Edad\n[3] Modificar Profesion\n[4] Modificar Estado [Activo/Inactivo]\n[5] Modificar DNI\n")
        match (opcion):
            case "1": 
              trabajadores[dni][0]= input("Ingrese el nuevo Nombre...\n").title()
              print("Dato modificado correctamente")
            case "2": 
              trabajadores[dni][1]= int(input("Ingrese la nueva Edad..."))
              print("Dato modificado correctamente")
            case "3": 
              trabajadores[dni][2]= input("Ingrese el nuevo Profesion...").lower()
              print("Dato modificado correctamente")
            case "4": 
              nuevaActividad=input(f"{dni} ¿Se encuentra activo en el rubro? [Si/No]:\n").lower()
              while nuevaActividad not in ["si","s","n","no"]:
                nuevaActividad=input("Responder Si o No:\n").lower()
                
              if nuevaActividad  in ["si","s"]:
               nuevaActividad= True
              else:
               nuevaActividad= False
              trabajadores[dni][3]=nuevaActividad
              print("Dato modificado correctamente")
    
            case "5":
                nuevoDni=int(input("Ingrese el nuevo DNI..."))
                
                if nuevoDni in trabajadores:
                    print("Ese DNI ya pertenece a otro trabajador\n")
                else:
                  trabajadores[nuevoDni] = [trabajadores[dni][0],trabajadores[dni][1],trabajadores[dni][2],trabajadores[dni][3]];del(trabajadores[dni]); print("DIN modificado correctamente")
            case _:   print("Opcion no valida\n")
   
    else:
        print(f"{dni} No fue encontrado\n")

           
    preguntaFinal()

def preguntaFinal():
  x=input("\n¿Volver al menu principal? [Si/No]: \n").lower()
  while x not in ["s","si","n","no"]:
   x=input("Responder Si o No:\n").lower()
  match (x):
    case "si": menuPrincipal()
    case "s": menuPrincipal()
    case _:  print("Finalizando el programa. Gracias por utilizar")

def imprimirDiccionario():
    print("-" * 55)
    for y in trabajadores:
        print(f"{y} : {trabajadores[y]}") 
    print("-" * 55)


def profesiones():
  profesion=input("\nIngrese una profesion: \n").lower()
  listaDeProfesionales=[]
  print("Lista de profesionales:\n")
  for clave, valor in trabajadores.items():
    if valor[2] == profesion:
      listaDeProfesionales.append(clave)
       
  for clave in listaDeProfesionales:
   print(f"{clave}")

def menuReportes():
  continuar=True
  print("""
  [1] Ver la información de un trabajador según su DNI
  [2] Mostrar trabajadores desocupados (no activos)
  [3] Mostrar trabajadores según la profesión
  [4] Volver 
  """)
  while continuar:
    opcion=input("#Ingrese una opcion:\n")
    match (opcion):
      case "1": 
        print("Ver la información de un trabajador según su DNI:")
        continuar=False
        verInfo()
      case "2": 
        print("Mostrando trabajadores desocupados:\n")
        continuar=False
        trabajadoresDesocupados()
        preguntaFinal()
      case "3": 
        print("Mostrar trabajadores según la profesión")
        continuar=False
        profesiones()
        preguntaFinal()
      case "4": 
        print("Volver al menu principal")
        continuar=False
        menuPrincipal()
      case _:   print ("***Opcion no valida, ingrese otra...***")

def menuSecundario():
  continuar=True
  print("""
  ====Gestion de Trabajadores====
  [1] Ingresar nuevo Trabajador
  [2] Modificar dato de trabajador
  [3] Eliminar Trabajador 
  [4] Volver
  """)
  while continuar:
    opcion=input("*Ingrese una opcion:\n")
    match (opcion):
      case "1": 
        print("*"*10,"Ingresando nuevo Trabajador","*"*10)
        continuar=False
        agregarUser()
        menuSecundario()
      case "2": 
        print("Modificar dato de trabajador")
        continuar=False
        modificarUser()
      case "3": 
        print("Eliminar Trabajador")
        continuar=False
        eliminarTrabajador()
      case "4": 
        print("***Volver al menu principal***")
        continuar=False
        menuPrincipal()
      case _:   
        print ("***Opcion no valida, ingrese otra...***")

def menuPrincipal():
  continuar=True
  separador()
  print(" [1] Gestión de Trabajadores\n [2] Reportes\n [0] Salir")
  separador()
  print("")
  while continuar:
    opcion=input("Ingrese una opcion:\n")
    match (opcion):
      case "1": 
        continuar=False
        menuSecundario()     
      case "2":
        print ("====Reportes====")
        continuar=False
        menuReportes()
      case "0":
        print ("====salir====\n")
        imprimirDiccionario()
        print("\nFinalizando el programa. Gracias por utilizar")
        continuar=False
      case _:  print ("===Opcion no valida===")

menuPrincipal()



archivo= open("texto.txt", "w")

for y in trabajadores:
  archivo.write(f"{y} : {trabajadores[y]}\n") 

archivo.close()

