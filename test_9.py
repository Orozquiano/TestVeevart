import random #importamos la libreria random para usarlo como piso inicial

def ValidarPiso(P): #Valida si el numero del piso esta correcto
    Pisos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    Validation = False
    for n in Pisos:      
        if P != n:
            Validation = False
        else:
            Validation = True
        if Validation:
            return True

def SubirBajar(P,PA): #Funcion para saber el sentido que tomara el ascensor 
    if P > PA:
        return True
    else:
        return False
        
def Ascensor():
    PisosUsers = []
    x = random.randint(1, 29)
    PisoAnterior = x
    print("Bienvenido al ascensor *Musica de ascensor de fondo* ")

    while True:
        print("Elevador en piso: "+str(PisoAnterior))
        print("Elevador se detiene")
        print("Digite el piso al que desea ir")
        PisosUsers.append(input()) #Agrega el piso al vector
        if(ValidarPiso(int(PisosUsers[0]))): #Buscamos si el ascensor esta en sentido ascendente o descendete en cullo caso sea ascendete dara True de lo contrario sera False
            if SubirBajar(int(PisosUsers[0]),int(PisoAnterior)): #Verfica si el ascensor va subiendo o va bajando comparando el piso anterio contra el piso siguiente
                print("Subiendo...")
                PisoAnterior = PisosUsers[0] #guarda el piso anterior
                del PisosUsers[0] #elimina el piso en cual esta ahora mismo
            else:
                print("Bajando")
                PisoAnterior = PisosUsers[0] #guarda el piso anterior
                del PisosUsers[0] #elimina el piso en cual esta ahora mismo
        else: #De lo contrario elimina el numero y lo vuelve a pedir 
            del PisosUsers[0] #Elimin el piso mal digilenciado
            print("Digite un numero del 1 - 29")
        

Ascensor()
        
        

    




    