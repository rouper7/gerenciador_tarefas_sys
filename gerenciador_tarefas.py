import sys
import os

arquivo_tarefa=os.path.join(os.path.dirname(__file__),"tarefa.txt")

def adicionar_tarefas(tarefa):
    try:
        with open(arquivo_tarefa,"a") as file:
            file.write(f"{tarefa}\n")
        
        print(f"sua tarefa {tarefa} foi add com sucesso!!!")
    except:
        print("nenhuma tarefa foi add")

def listar_tarefas():
    with open(arquivo_tarefa,"r") as linhas:
        for linha in linhas:
            print(f'-{linha.strip()}')

def exibir_ajuda():
    #mostra como utilizar o programa
    ajuda = """
Gerenciador de Tarefas Simples
Uso:
    python gerenciador_tarefas.py -add "Nome da Tarefa"    - Adiciona uma nova tarefa| coloque entre "" se tiver 
                                                            espaços
    python gerenciador_tarefas.py -list                     - Lista todas as tarefas
    python gerenciador_tarefas.py --help                    - Mostra esta mensagem de ajuda
    python gerenciador_tarefas.py -del                      - Deleta o arquivo por completo
                                                                  
"""
    print(ajuda.strip())


import os

def deletar_arquivo(caminho):
    #Deleta o arquivo caso ele confirme.
    resposta = input(f"Tem certeza que deseja deletar o arquivo '{caminho}'? (s/n): ")
    if resposta == 's':
        try:
            os.remove(caminho)
            print(f"Arquivo '{caminho}' deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar o arquivo  {e}")
    elif resposta=='n':
        print("Operação cancelada .")
    else:
        print('apenas digite "s" ou "n" ')


def executar():
    if len(sys.argv)<2:
        exibir_ajuda()
        sys.exit(1)

    if sys.argv[1]=="-add":
        adicionar_tarefas(sys.argv[2])
    elif sys.argv[1]=="--help":
        exibir_ajuda()
    elif sys.argv[1]=="-list":
        listar_tarefas()
    elif sys.argv[1]=="-del":
        deletar_arquivo(arquivo_tarefa)
    else:
        exibir_ajuda()

if __name__=="__main__":
    executar()
