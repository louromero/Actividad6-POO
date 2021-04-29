from FechaHora import FechaHora

def cargarFechas():
    print("-------FECHA 1--------")
    dia = int(input("Ingrese Dia: "))
    mes = int(input("Ingrese Mes: "))
    anio = int(input("Ingrese Año: "))
    hora= int(input("Ingrese Hora: "))
    minuto = int(input("Ingrese Minutos: "))
    segundo = int(input("Ingrese Segundos: "))
    print(" ")
    r1 = FechaHora(dia,mes,anio,hora,minuto,segundo)
    r1.Mostrar()

    print("-------FECHA 2----------")
    d = int(input("Ingrese Dia: "))
    ms = int(input("Ingrese Mes: "))
    a = int(input("Ingrese Año: "))
    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    print(" ")
    r2 = FechaHora(d,ms,a,h,m,s)
    #r2 = FechaHora(0,0,0,hora,minuto,segundo)
    r2.Mostrar()
    Menu(r1,r2)

def imprimir():
    print(" ")
    print("---------- MENU --------")
    print("1. Sumar.")
    print("2. Restar.")
    print("3. Mostrar cual es el mayor.")
    print("4. Salir")
    print(" ")

def Menu(r1,r2):
    print("--------------------------------------------------------")
    print("El primer conjunto es: ")
    r1.Mostrar()
    print("El segundo conjunto es: ")
    r2.Mostrar()
    print("--------------------------------------------------------")
    band=True
    while band:
        imprimir()
        opcion=int(input("Ingrese Opcion: "))
        if opcion==1:
            print(" ")
            print("SUMA: ")
            r=r1+r2
            r.Mostrar()
            

        elif opcion==2:
            print(" ")
            print("RESTA: ")
            r=r1-r2
            r.Mostrar()
            

        elif opcion==3:
            print(" ")
            print("EL MAYOR ES (respecto a edades): ")
            comparacion=r1 > r2
            if comparacion==True:
                r1.Mostrar()
            else:
                r2.Mostrar()

        elif opcion==4:
            print(" ")
            print("Chau :)")
            band=False
        else:
            print("Opcion no valida.")

if __name__=='__main__':
    cargarFechas()