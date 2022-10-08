####################Menu####################################################
print("Bienvenido dime que formula deseas hacer:")

def lista(lobby):
    lobby=["Suma[S]", "Resta[R]", "Multiplicacion[M]", "Division[D]", "Otros[O]"]
    print(" ")##########> Lo ocupo para estetica
    for lista in range (len(lobby)):##>Determino un rango
        print(lobby[lista])
        
lista(["Suma[S]", "Resta[R]", "Multiplicacion[M]", "Division[D]", "Otros[O]"])

print(" ")##########> Lo ocupo para estetica 
x=str(input("Selecciona la formula:"))
    
######>pongo "str" porque estoy pidiendo un valor no numerico
##############################Suma##########################################

if x=="S":
    print ("Seccion suma")
    def suma_one(uno,dos):
        resultado = uno+dos
        return resultado

    def valores_suma():
        x1=int(input("Primer valor"))
        y2=int(input("Segundo valor"))
        suma_one(x1,y2)
        print (suma_one(x1,y2))
    
    
    valores_suma()
#############################Suma#####################################################
if x=="R":
    print ("Seccion resta")
    def resta(uno,dos):
        resultado = uno - dos
        return resultado

    def valores_resta():
        x1=float(input("Primer valor"))##############pongo el float para que exista la posibilidad de decimales 
        y2=float(input("Segundo valor"))
        resta(x1,y2)
        print (resta(x1,y2))
    
    
    valores_resta()
###############################Resta##############################################
if x=="M":
    print ("Seccion Multiplicación")
    def multi(uno,dos):
        resultado = uno * dos
        return resultado

    def valores_multi():
        x1=int(input("Primer valor"))
        y2=int(input("Segundo valor"))
        multi(x1,y2)
        print (multi(x1,y2))
    
            
    valores_multi()
##################################Multiplicacion################################
if x=="D":
    print ("Seccion Division")
    
    a=["Decimal[D]", "Entera[E]", "Residuo[R]"]

    for lista in range (len(a)):
        print(a[lista])
        
        
    x=str(input("Deseas hacer una division:"))
    
    if x=="D":
        def Decimal(a,b):
            decimal=a/b
            return decimal
                 
        def valores_dv():
            x=float(input("Selecciona un primer numero:"))#############>ocupe el float para decimales
            y=float(input("Selecciona un segundo numero:"))
            Decimal(x,y)
            print(Decimal(x,y))
        valores_dv()
        
    if x=="E":
        def Entera(a,b):
            entera=a // b
            return entera
                 
        def valores_dve():
            x=int(input("Selecciona un primer numero:"))#############>ocupe el int para enteros
            y=int(input("Selecciona un segundo numero:"))
            
            print (Entera(x,y))
        valores_dve()
    if x=="R":
        def Residuo(a,b):
            residuo=a%b
            return residuo
                 
        def valores_dvr():
            x=float(input("Selecciona un primer numero:"))#############>ocupe el float para decimales
            y=float(input("Selecciona un segundo numero:"))
            
            print (Residuo(x,y))
        valores_dvr()
###############Division###############################################################

if x=="O":
    
    a=["Area[A]","Perimetro[P]","Contador[CO]","Serie[S]", "Matriz[MA]"]
    
    for lista in range (len(a)):##>Determino un rango
        print(a[lista])
        
    x=str(input("Selecciona la formula:"))
#############################Menu "Otros"##############################################
    print("")
    
    if x=="A":
        print ("Selecciona la figura")
        print("")
        a=["Triangulo[T]","Cuadrado[C]", "Rectangulo[R]"]##########> Es la segunda lista para no llenar de datos la primera lista
            
        for lista in range (len(a)):##>Determino un rango
            print(a[lista])
        
        x=str(input("Selecciona la formula:"))
        
        if x=="T":
            def triangulo(a,b):
                Area=(a*b)/2
                return Area
                 
            def valores_at():
                x=float(input("Selecciona tu base:"))#############>ocupe el float para decimales
                y=float(input("Selecciona tu altura:"))
                print (triangulo(x,y))
                
            valores_at()
            
        if x=="C":
            def Cuadrado(a,b):
                area=a*b
                return area
            def valores_ac():
                x=float(input("Selecciona tu base:"))#############>ocupe el float para decimales
                y=float(input("Selecciona tu altura:"))
                print (Cuadrado(x,y))
            valores_ac()
            
        if x=="R":
            def Rectangulo(a,b):
                area=a*b
                return area
            def valores_ar():
                x=float(input("Selecciona tu base:"))#############>ocupe el float para decimales
                y=float(input("Selecciona tu altura:"))
                print (Rectangulo(x,y))
            valores_ar()
###############################Area##################################################################################################################
    if x=="P":
        a=["Triangulo[T]","Cuadrado[CU]", "Rectangulo[R]" ]
            
        for lista in range (len(a)):##>Determino un rango
            print(a[lista])
        
        x=str(input("Selecciona la formula:"))
        if x=="T":
            def Triangulo(a):
                area=a*3
                print(area)
            def valores_pt():
                a=int(input("Selecciona tu base:"))
                Triangulo(a)
            valores_pt()
        if x=="CU":
            
            def Cuadrado(a):
                area=(a*a)*2
                return area
            def valores_pc():
                X=int(input("Selecciona tu base:"))
                print (Cuadrado(X))
            valores_pc()
        if x=="R":
            
            def Rectangulo(a,b):
                area=a*2+b*2
                return area
            def valores_pr():
                x=int(input("Selecciona tu lado 1:"))
                y=int(input("Selecciona tu lado 2:"))
                print (Rectangulo(x,y))
            valores_pr()
#################################################Contador####################################################################################################    
    if x=="CO":
        def contador(a,b):
            numero=a
            while a<b+1:
                print(a)
                a+=1
            
                
        def main():
            a=int(input("Selecciona tu numero minimo:"))
            b=int(input("Selecciona tu numero maximo:"))
            contador(a,b)
        main()
#############################################################Series#################################################################################################
    if x=="S":
        def series(x,y,z):
            for serie in range(x,y+1,z):
                print(serie)
                
        def main():
            x=int(input("Selecciona tu numero minimo:"))
            y=int(input("Selecciona tu numero maximo:"))
            z=int(input("Selecciona el orden de la sucesion:"))
            series(x,y,z)
        main()
#################################################################Matriz################################################################################################
    if x== "MA" and x!="A" or x!="P" or x!="CO" or x!="S":
        def crear_matriz(columnas,renglones,digito):
            matriz=[]
            for i in range ( 0,columnas):
                matriz.append([])
                for j in range ( 0,renglones):
                    matriz[i].append(digito)
            return matriz
        def ejecucion_matriz():
            c= int(input("Selecciona el numero de columnas"))
            r= int(input("Selecciona el numero de renglones"))
            d= int(input("Selecciona el numero dentro de tu matriz"))
            matriz= crear_matriz(c,r,d)
            print (matriz)
        ejecucion_matriz()
        
    elif x!="A" or x!="P" or x!="CO" or x!="S" or x!="MA":
        print("Digito no valido")
            
            
#################################Series#############################################
elif x!="S" or x!="R" or x!="M" or x!="D" or  x!="O":########################> para poder enviar al usuario si no escoje una letra correcta
    print ("Digito no valido")