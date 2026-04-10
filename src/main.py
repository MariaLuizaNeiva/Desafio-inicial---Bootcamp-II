from habitos import HabitTracker

def menu():
    tracker = HabitTracker()
    print("--- NutriLog CLI ---")
    
    while True:
        print("\n1. Registrar Água")
        print("2. Ver Status")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            qtd = int(input("Quantidade em ml: "))
            tracker.registrar_agua(qtd)
            print("Registrado com sucesso!")
        elif opcao == "2":
            print(tracker.status_agua())
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()