def registro ():
    global nome, idade, senha
    print("olá, seja bem vindo ao teste de banco de dados")

    weak_passwords = {'123', 'abc', '12345678'}

    while True:
        nome = input("Digite seu nome para login: ").strip().capitalize()
        if nome:
            break
        else:
            print("Nome inválido, por favor tente novamente.")

    
    while True:
            idade = int(input("digite sua idade: "))
            if idade >= 18 and idade <= 130:
                break
            else:
                print("idade inválida, por favor tente novamente.")

    
    while True:
        senha = input("Digite sua senha: ")
        if len(senha) >= 6 and senha not in weak_passwords:
            break
        else:
            print("Senha fraca, tente novamente")
registro()
saldo = 0
def registrocontas():
    try:
        with open("Contas.txt","w") as Contas:
            Contas.write("Nome:")
            Contas.write(nome)
            Contas.close()
    except FileNotFoundError:
        print("A Database Contas, não foi encontrado contate o programador.")
    except PermissionError:
        print("occoreu um erro de permição nessa pasta, porfavor certifique-se que o arquivo pode ser escrito nesta pasta.")
    except Exception as e:
        print(f"ERRO> {e}")
    finally:
        Contas.close()
    try:
        with open("Contas.txt", "a") as Contasa:
            Contasa.write(" Idade:")
            Contasa.write(str(idade))
    except Exception as e:
        print(f"Erro<I> {e}")
    finally:
        Contas.close()
    try:
        with open("Contas.txt","a") as Contasa:
            Contasa.write(" Senha:")
            Contasa.write(str(senha))
    except Exception as e:
        print(f"Erro<S> {e}")
    finally:
        Contas.close()
    try:
        with open("Contas.txt", "a") as Contasa:
            Contasa.write(" Saldo:")
            Contasa.write(str(saldo))
            Contasa.write("\n")
    except Exception as e:
        print(f"Erro<Sa> {e}")
    finally:
        Contas.close()
registrocontas()
def menu(saldo):
    while True:
        print("******************")
        print("1- Depositar:")
        print("2- Sacar:")
        print("3- Saldo:")
        print("4- ping")
        print("5- Alterar senha")
        print("6- Sair")
        print("******************")
        escolha = int(input("O que deseja fazer hoje? "))

        if escolha == 1:
            depositar = int(input("Quanto deseja depositar? "))
            saldo += depositar
            print(f"Seu novo saldo é de: {saldo}")
            save_balance_to_file(saldo)  
        if escolha == 2:
            retirar = int(input("Quanto deseja sacar? "))
            if retirar < saldo:
                saldo -= retirar
                print(f"O valor colocado foi sacado, seu novo saldo é de: {saldo}")
                save_balance_to_file(saldo)  
            else:
                print("Você não tem saldo suficiente para completar o saque")
        if escolha == 3:
            print(f"Seu saldo é de: {saldo}")
        if  escolha == 5 :
            confirm_antiga_senha = input("digite a sua senha atual: ")
            if confirm_antiga_senha == senha:
                print("Acesso Permitido")
                nova_senha = input("Digite sua nova senha: ")
                confirm_nova_senha = input("Confirme a nova senha: ")
                if nova_senha == confirm_nova_senha:
                    print("As senhas coincidem, mudando senha...")
                    save_new_password_to_file(nova_senha)
                else:
                    print("Acesso negado senha incorreta.")
                 
        if escolha == 4:
            print("Pong!")
        if escolha == 6:
            print("Até a próxima! Deletando Conta Por que não tenho sistema de login ainda D:")
            break
        if not int:
            print("Número de escolha incorreto, por favor, escolha as opções que aparecem usando numeros")

def save_balance_to_file(balance):
    try:
        with open("Contas.txt", "w") as contas_file:
            contas_file.write("Saldo: ")
            contas_file.write(str(balance))
    except Exception as e:
        print(f"Error saving balance to file: {e}")

def save_new_password_to_file(new_password):
    try:
        with open("Contas.txt", "a") as contas_file:
            contas_file.write("\nSenha: ")
            contas_file.write(str(new_password))
    except Exception as e:
        print(f"Error saving new password to file: {e}")

registro()
menu(saldo)