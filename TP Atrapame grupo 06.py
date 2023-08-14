import random, subprocess

def hacerTablero (tamaño, emojis):
    """Esta funcion se encarga de crear un tablero, llamando a las distintas funciones para que estas lo rellenen"""
    #se inicializa la matriz
    tablero = [[emojis["vacio"]]*tamaño for i in range(tamaño)]
    #se define la posicion de bueno malo y salida
    pos_exit = random.randint(0,tamaño-1)
    pos_mala = random.randint(0,tamaño-1)
    pos_bueno = random.randint(0,tamaño-1)
    while pos_exit == pos_mala:
        pos_exit = random.randint(0,tamaño-1)  
    tablero[0][pos_mala] = emojis["malo"]
    tablero[tamaño-1][pos_bueno] = emojis["bueno"]
    tablero[0][pos_exit] =emojis["salida"]
    #se rellena el tablero con obstaculos y potenciadores
    creacionfruta (tablero,emojis["fruta_costado"])
    poner_saltos(tablero,emojis["salto"])
    poner_paredes(tablero,emojis["pared"])
    return tablero,pos_exit

def poner_paredes(matriz,emoji):
    """Define e inserta las paredes aleatoriamente"""
    filas_con_pared= [random.randint(1,23) for i in range (10)]
    columnas_con_pared= [random.randint(0,24) for i in range (10)]  
    for f in range (len(matriz)):
        if f in filas_con_pared:
            pos = random.randint(0,24)
            for i in range(random.randint(2,5)):
                if pos < 24:
                    matriz[f][pos]= emoji
                    pos += 1
    for c in range (len(matriz)):
        if c in columnas_con_pared:
            pos = random.randint(1,23)
            for i in range(random.randint(2,6)):
                if pos <= 23:
                    matriz[pos][c]= emoji
                    pos += 1
                    
def poner_saltos(matriz,emoji):
    """Define e inserta los saltos aleatoriamente"""
    filas_con_salto= [random.randint(1,23) for i in range (13)]
    columnas_con_salto= [random.randint(1,24) for i in range (13)]
    for f in range (len(matriz)):
        if f in filas_con_salto:
            pos = random.randint(0,24)
            matriz[f][pos]= emoji
    for c in range (len(matriz)):
        if c in columnas_con_salto:
            pos = random.randint(1,23)
            matriz[pos][c]= emoji
                
def creacionfruta(matriz,bloque):
    """Define e inserta las frutas aleatoriamente"""
    queF= [random.randint(1,23) for i in range (16)]
    queC= [random.randint(1,24) for i in range (16)]
    for f in range (len(matriz)):
        if f in queF:
            pos=random.randint(1,24)
            matriz[f][pos]= bloque
    for c in range (len(matriz)):
        if c in queC:
            pos=random.randint(1,23)
            matriz[pos][c]= bloque
                    
def imprimir_matriz(m,f=0,c=0):
    """Se imprime la matriz de manera recursiva"""
    if len(m[f])==c:
        f+=1
        c=0
        print()
    if len(m)==f:
        return
    print("%s"%m[f][c],end=" ")
    return imprimir_matriz(m,f,c+1)

def imprimir(tablero):
    """Se limpia la terminal y se envia la matriz a la funcion recursiva imprimir_matriz()"""
    subprocess.run("clear",shell=True)
    imprimir_matriz(tablero)

def saltar(fsalto,csalto, matriz,f,c,emojis,cara,lado):
    """Verifica si hay un salto y se mueve"""
    if matriz[fsalto][csalto]==emojis["salto"]:
        if lado=="W":
            if matriz[fsalto-1][c]==emojis["vacio"]:
                matriz[fsalto-1][c]=cara
                matriz[f][c]=emojis["vacio"]
                return True
            else:
                return False
        if lado=="S":
            if cara==emojis["malo"]:
                return False
            return True
        if lado=="A":
            if matriz[fsalto-1][c-1]==emojis["vacio"]:
                matriz[fsalto-1][c-1]=cara
                matriz[f][c]=emojis["vacio"]
                return True
            else:
                return False
        if lado=="D":
            if matriz[fsalto-1][c+1]==emojis["vacio"]:
                matriz[fsalto-1][c+1]=cara
                matriz[f][c]=emojis["vacio"]
                return True
            else:
                return False 
    else:
        return "NO"    

def moverCostado(ffruta,cfruta, matriz,f,c,emojis,cara,lado):
    """Verifica si hay una fruta y se mueve"""
    try:
        if matriz[ffruta][cfruta]==emojis["fruta_costado"]:
            listaDirecciones=[-1,1]
            direccion=random.choice(listaDirecciones)
            if lado=="W":
                if matriz[ffruta][c+direccion]==emojis["vacio"]:
                    while c+direccion<0 or c+direccion>24:
                        direccion=random.choice(listaDirecciones)
                    matriz[ffruta][c+direccion]=cara
                    matriz[f][c]=emojis["vacio"]
                    return True
                else:
                    return False
            if lado=="S":
                if matriz[ffruta][c+direccion]==emojis["vacio"]:
                    while c+direccion<0 or c+direccion>24:
                        direccion=random.choice(listaDirecciones)
                    matriz[ffruta][c+direccion]=cara
                    matriz[f][c]=emojis["vacio"]
                    return True
                else:
                    return False
            if lado=="A":
                if matriz[ffruta][c-2]==emojis["vacio"] :  
                    
                    matriz[ffruta][c-2]=cara
                    matriz[f][c]=emojis["vacio"]
                    return True
                else:
                    return False
            if lado=="D":
                if matriz[ffruta][c+2]==emojis["vacio"]:  
                    
                    matriz[ffruta][c+2]=cara
                    matriz[f][c]=emojis["vacio"]
                    return True
                else:
                    return False 
        else:
            return "NO" 
    except IndexError:
        return False

def buscarCara(matriz,cara):
    """Busca la posicion del jugador, si no la encuentra devuelve False"""
    fila=col=-1
    for f in range (len(matriz)):
        for c in range (len(matriz[0])):
            if cara == matriz[f][c]:
                fila=f
                col=c
                break
    if fila!=-1:
        return fila , col
    else:
        return False

def verificar (fila,col,matriz,f,c,emojis,cara,lado):
    """Verifica y mueve al jugador si es posible"""
    try:
        if cara==emojis["malo"]: #cuando el jugador es el malo
            assert matriz[fila][col] != emojis["salida"], "Error, no puede sobrepasar al bloque" #no puede tocar la salida
        assert matriz[fila][col] != emojis["pared"], "Error, no puede sobrepasar al bloque" #no puede pasar la pared
        saltoResultado=saltar(fila,col,matriz,f,c,emojis,cara,lado) #se verifica si la posicion siguiente es un salto
        if saltoResultado==False: # si era un salto pero no se pudo mover, devuelve error
            raise IndexError
        frutaResultado=moverCostado(fila,col,matriz,f,c,emojis,cara,lado)  #se verifica si la posicion siguiente es una fruta
        if frutaResultado==False:
            raise IndexError
        if saltoResultado=="NO" and frutaResultado=="NO":
            matriz[fila][col]=cara
            matriz[f][c]=emojis["vacio"]
    except IndexError:
        return False
    except AssertionError as mensaje:
        return False

def mover(matriz,lado,cara,emojis):
    """Se realiza el movimiento, tanto del bueno como del malo y se verifican obstaculos y potenciadores"""
    f,c=buscarCara(matriz,cara)
    try:
        assert not(f==0 and lado=="W") ,("Error, no se puede la opcion",lado.upper())
        assert not(c==0 and lado=="A") ,("Error, no se puede la opcion",lado.upper())
        if lado== "W": #movimiento hacia arriba
            ok=verificar(f-1,c,matriz,f,c,emojis,cara,lado)
            if ok==False:
                raise IndexError
        if lado=="S":
            ok=verificar(f+1,c,matriz,f,c,emojis,cara,lado)
            if ok==False:
                raise IndexError
        if lado=="A":
            ok=verificar(f,c-1,matriz,f,c,emojis,cara,lado)
            if ok==False:
                raise IndexError
        if lado=="D":
            ok=verificar(f,c+1,matriz,f,c,emojis,cara,lado)
            if ok==False:
                raise IndexError
    except IndexError:
        print("Error, no se puede la opcion",lado.upper())
        return False
    except AssertionError as mensaje:
        print(mensaje)
        return False

def maloMov(matriz,emojis):
    """A partir de la posicion del bueno, se elije la del malo"""
    fM,cM=buscarCara(matriz,emojis["malo"])
    fB,cB=buscarCara(matriz,emojis["bueno"])
    if fB!=fM:
        if fB>fM:
            mov="S"
        else:
            mov="W"
    else:
        if cM>cB:
            mov="A"
        else:
            mov="D"
    return mov    

#Programa Principal

#Definicion de variables
tamaño = 25
emojis={"bueno":"\U0001F920","malo" : "\U0001F479","salida" : "\U0001F6AA","pared": "\U0001F6A7","vacio" : "\U000026AA","salto" : "\U0001F53A","fruta_costado" : "\U0001F34F","bandera":"\U0001F3C1"}
movimientos = ("W","S","A","D")

#comienza un nuevo juego cada vez que empieza este while
querer="S"
while querer=="S":
    titulo=emojis["bandera"]+"ATRÁPAME"+emojis["bandera"]
    print("\n",titulo.center(100),"\n")        
    instrucciones="El jugador "+emojis["bueno"]+": debe moverse por el tablero para llegar a la salida "+emojis["salida"]+" sin que "+emojis["malo"]+"lo atrape. El jugador "+emojis["bueno"]+": tiene 3 vidas. Solo es posible agarrar a un potenciador por vez. \
        \nPOTENCIADORES:\n"+emojis["salto"]+": sube una posición \n"+emojis["fruta_costado"]+": se mueve una posicion al costado\
        \nOBSTACULOS:\n"+emojis["pared"]+": le bloqueará el paso\n"+emojis["malo"]+": te persigue, si te atrapa perdes una vida\
        \nCONTROLES:\nW = Arriba\nS = Abajo\nA = Izquierda\nD = Derecha\
        \n\n\n\n\t\tPresione enter para comenzar..."
    print(instrucciones)
    input()
    #se pide la informacion del usuario, se resetea la cant de movimientos realizados hasta ganar la jugada
    user=input("UserName: ")
    edad=input("Edad: ")
    contMov=0
    #se crea el tablero
    tablero,pos_exit=hacerTablero(tamaño,emojis)
    imprimir(tablero)
    #como es una jugada nueva, se resetea la cant de vidas
    vidas=3
    while(tablero[0][pos_exit]==emojis["salida"]): #si la salida sigue estando en su posicion, entra al while
        contMov+=1 
        #Se pide al usuario ingresar un movimiento, y se realizara hasta que este sea valido
        mov = input("Movimiento: ")
        mov = mov.upper()
        while mov not in movimientos:
            print ("Movimiento Invalido, ingreselo nuevamente")
            mov=input("Movimiento: ")
            mov = mov.upper()
        verif=mover(tablero,mov,emojis["bueno"],emojis)
        if verif== False:
            continue
        imprimir(tablero)
        #se verifica si el malo sigue existiendo en el tablero, es decir, si murio
        murio=buscarCara(tablero, emojis["malo"])
        #si murio el malo, en realidad quiere decir que el bueno murio y pierde una vida
        if murio== False:
            vidas-=1
            f,c=buscarCara(tablero, emojis["bueno"])
            tablero[f][c]=emojis["malo"]
            imprimir(tablero)
            print("<<<< Perdiste una vida, Te quedan ",vidas," vidas >>>>")
            if vidas==0:
                print("<<<< Perdiste el juego >>>>")
                respuesta=input("Queres seguir jugando? (S/N)")
                if respuesta.upper()=="N":
                    break
                else:
                    vidas=3
                    tablero,pos_exit=hacerTablero(tamaño,emojis)
                    imprimir(tablero)
                    continue
            input("Para seguir jugando pulse enter...")
            subprocess.run("clear",shell=True)
            tablero,pos_exit=hacerTablero(tamaño,emojis)
            imprimir(tablero)
            continue
        else: #se verifica si el bueno esta en la posicion donde era la salida
            imprimir(tablero)
            f,c=buscarCara(tablero,emojis["bueno"])
            if f==0 and c==pos_exit:
                subprocess.run("clear",shell=True)
                texto="<<<< ¡¡Ganaste!! >>>>"
                print(texto.center(70))
                try:
                    archivo=open("usersWinners.txt","at")
                    archivo.write("Usuario: "+user+" Edad: "+edad+" Cantidad de movimientos: "+str(contMov)+"\n")
                except OSError:
                    print("No se puede leer las instrucciones")
                finally:
                    try:
                        archivo.close()
                    except NameError:
                        pass
                querer=input("Desea seguir jugando? (S/N) " )
                querer=querer.upper()
                while querer not in ["S", "N"]:
                    querer=input("Desea seguir jugando? (S/N) " )
                    querer=querer.upper()
                break
        # Jugada del malo 
        mov=maloMov(tablero,emojis)
        verif=mover(tablero,mov,emojis["malo"],emojis)
        while verif==False:
            mov= random.choice(movimientos)
            verif= mover(tablero,mov,emojis["malo"],emojis)
            imprimir(tablero)
        imprimir(tablero)
        murio=buscarCara(tablero, emojis["bueno"])
        if vidas==0:
            subprocess.run("clear",shell=True)
            print("<<<< Perdiste el juego >>>>")
            respuesta=input("Queres seguir jugando? (S/N)")
            if respuesta.upper()=="N":
                break
            else:
                vidas=3
                tablero,pos_exit,listaPozos=hacerTablero(tamaño,emojis)
                imprimir(tablero)
                continue
        if murio== False:
            vidas-=1
            print("<<<< Perdiste una vida, Te quedan ",vidas," vidas >>>>")
            if vidas==0:
                print("<<<< Perdiste el juego >>>>")
                respuesta=input("Queres seguir jugando? (S/N)")
                if respuesta.upper()=="N":
                    break
                else:
                    vidas=3
                    tablero,pos_exit=hacerTablero(tamaño,emojis)
                    imprimir(tablero)
                    continue
            input("Para seguir jugando pulse enter...")
            subprocess.run("clear",shell=True)
            tablero,pos_exit=hacerTablero(tamaño,emojis)
            imprimir(tablero)