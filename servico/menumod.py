from servicos.moderador import *
from servico.exclusao import exluir_mod

def verifmod(conn, id_usuario):
    try:
        # Corrigido o erro de digitação de cursor para cursor
        with conn.cursor() as cursor:
            query = """SELECT mod FROM gera.usuarios WHERE id_usuario = %s"""
            cursor.execute(query, (id_usuario,))
            resultado = cursor.fetchone()  # Recupera o resultado da consulta
            
            if resultado:
                mod = resultado[0]  # O campo "mod" é retornado na primeira posição da tupla
                return mod  # Retorna o valor de "mod", que será True ou False
            else:
                print("Usuário não encontrado!")
                return False  # Caso não encontre o usuário, retorna False
    except Exception as e:
        print(f"Erro ao verificar o moderador: {e}")
        return False
    
def menumod (conn):
        try:
             with conn.cursor() as cursor:
                print("Bem-vindo, moderador do Gera Ficha!\n")
                while True:
                    print("O que você deseja?")
                    print("1 - Visualizar itens")
                    print("2 - Inserir itens")
                    print("3 - Alterar itens")
                    print("4 - Deletar personagem")
                    print("5 - Buscar personagem")
                    print("6 - Sair")

                    opc = int(input("O que gostaria de fazer: "))

                    match opc:
                        case 1:
                            visualizar_dados(conn)
                        case 2:
                            inserir_dados(conn)
                        case 3:
                            alterar_dados(conn)
                        case 4:
                            exluir_mod(conn) 
                        case 5:
                            buscarperso(conn)
                        case 6:
                            break
                        case _:
                            print("Opção inválida. Tente novamente.")
        except Exception as e:
            print (e)