import json
import os

ARQUIVO_TAREFAS = "tasks.json"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as file:
            return json.load(file)
    return []

def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(ARQUIVO_TAREFAS, "w") as file:
        json.dump(tarefas, file, indent=4)

def listar_tarefas(tarefas):
    """Exibe a lista de tarefas."""
    if not tarefas:
        print("✅ Nenhuma tarefa pendente!")
    else:
        print("\n📌 Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i}. {status} {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista."""
    descricao = input("Digite a nova tarefa: ").strip()
    if descricao:
        tarefas.append({"descricao": descricao, "concluida": False})
        salvar_tarefas(tarefas)
        print("✅ Tarefa adicionada com sucesso!")

def remover_tarefa(tarefas):
    """Remove uma tarefa da lista."""
    listar_tarefas(tarefas)
    try:
        index = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= index < len(tarefas):
            del tarefas[index]
            salvar_tarefas(tarefas)
            print("🗑️ Tarefa removida com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

def marcar_como_concluida(tarefas):
    """Marca uma tarefa como concluída."""
    listar_tarefas(tarefas)
    try:
        index = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= index < len(tarefas):
            tarefas[index]["concluida"] = True
            salvar_tarefas(tarefas)
            print("🎉 Tarefa concluída!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

def menu():
    """Exibe o menu de opções e gerencia as ações do usuário."""
    tarefas = carregar_tarefas()
    
    while True:
        print("\n📌 Gerenciador de Tarefas")
        print("1️⃣ Listar tarefas")
        print("2️⃣ Adicionar tarefa")
        print("3️⃣ Remover tarefa")
        print("4️⃣ Marcar como concluída")
        print("5️⃣ Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            marcar_como_concluida(tarefas)
        elif opcao == "5":
            print("👋 Saindo... Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
