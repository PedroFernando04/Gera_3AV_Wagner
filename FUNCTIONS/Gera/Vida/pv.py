import random, os

def pv(classe, Const):
    print("\nAgora vamos calcular a vida do personagem")
    print("(A vida é definida por um dado de vida + Constituição do personagem)\n")
    print("A quantidade de lados do dado de vida é definido pela classe do personagem, sendo: \n")
    print("Guerreiro  |  10")
    print("Ladino     |  8")
    print("Curandeiro |  8")
    print("Mago       |  6")
    print("Bardo      |  8")
    print("Druida     |  8")
    
    #Despoluir tela
    input("\n[Pressione qualquer tecla para seguir]\n")
    os.system('cls')


    if classe == 'Guerreiro':
        dvariavel = 10

    elif classe == 'Mago':
        dvariavel = 6

    else:
        dvariavel = 8

    dadovida = random.randint(0, dvariavel)

    vida = dadovida + Const

    print(f"Baseado na classe de seu personagem, você tem direito a um dado de {dvariavel} lados\n")

       
    print(f"Sua rolagem de um d{dvariavel} resultou em {dadovida}\n")
    
    print(f"{dadovida}(dado de vida) + {Const} (Constituição)\n")
    print(f"Logo o PV do personagem é de: {vida}\n")
    input("\n[Pressione qualquer tecla para seguir]\n")

    return vida
#Teste da Função
#pv(1 , 8)
