import random


def run():
    menu = str("""
*****************************************
         BIENVENIDO A PY.GAME 
*****************************************

COMENCEMOS

Introduce un número entre 1 y 100

    : """)    

    number_random = random.randint(1,100)
    number_user = int(input(menu)) 
    intento = 0
    while number_user != number_random:
        if number_user > number_random:
            print(""" 
             
            ### ERROR ### 
            
            Escribe un número MENOR 
            
            """)
            intento += 1
            
        else:
            print(""" 
            
            ### ERROR ### 
            
            Escribe un número MAYOR 
            
            """)
            intento += 1       
        number_user= int(input("Elige otro número: "))
    
    if intento < 3:
        gamer = "Eres de los mejores"
    else:
        gamer= "Puedes hacerlo mejor"    

    
    print("""
    
    ¡GANASTE!

    Lo lograste en """ + str(intento) + " intentos. " + gamer )


if __name__=='__main__':
    run()