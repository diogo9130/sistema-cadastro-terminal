def validar_nome():
    nome = input("Nome: ").strip()
    while len(nome) < 3:
        print("Nome inválido. Deve conter ao menos 3 caracteres.")
        nome = input("Nome: ").strip()
    return nome.title()


def validar_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if 0 < idade < 150:
                return idade
            else:
                print("Idade inválida. Deve estar entre 1 e 149.")
        except ValueError:
            print("Digite um número válido.")


def validar_salario():
    while True:
        try:
            salario = float(input("Salário: "))
            if salario > 0:
                return salario
            else:
                print("Salário deve ser maior que zero.")
        except ValueError:
            print("Digite um valor numérico válido.")


def validar_sexo():
    while True:
        sexo = input("Sexo (f/m): ").lower()
        if sexo in ("f", "m"):
            return sexo
        print("Sexo inválido. Digite 'f' para feminino ou 'm' para masculino.")


def validar_estado_civil():
    while True:
        estado = input("Estado civil (s/c/v/d): ").lower()
        if estado in ("s", "c", "v", "d"):
            return estado
        print("Estado civil inválido. Use: s = solteiro, c = casado, v = viúvo, d = divorciado.")


def mostrar_cadastro(usuario):
    print("\n=== DADOS CADASTRADOS ===")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print("==========================\n")


def menu_visualizacao(usuario):
    while True:
        mostrar_cadastro(usuario)
        opcao = input("Gostaria de ver novamente o cadastro? (s/n): ").lower()
        if opcao == "n":
            print(f"\nObrigado por utilizar o sistema, {usuario['nome']}.")
            break
        elif opcao != "s":
            print("Resposta inválida.")


def realizar_cadastro():
    print("\nCADASTRO DE USUÁRIO")
    usuario = {
        "nome": validar_nome(),
        "idade": validar_idade(),
        "salário": validar_salario(),
        "sexo": validar_sexo(),
        "estado civil": validar_estado_civil()
    }
    return usuario


def menu_principal():
    print(
        "Bem-vindo ao sistema de cadastro.\n"
        "Regras:\n"
        "1 - Nome com mais de 2 caracteres\n"
        "2 - Idade entre 1 e 149\n"
        "3 - Salário maior que 0\n"
        "4 - Sexo: f ou m\n"
        "5 - Estado civil: s, c, v ou d\n"
    )

    usuario = realizar_cadastro()

    while True:
        opcao = input(
            f"\nCadastro concluído com sucesso, {usuario['nome']}.\n"
            "Digite:\n"
            "  [c] para visualizar\n"
            "  [a] para alterar\n"
            "  [s] para sair\n"
            "Escolha: "
        ).lower()

        if opcao == "c":
            menu_visualizacao(usuario)
        elif opcao == "a":
            print("\n== ALTERAÇÃO DO CADASTRO ==")
            usuario = realizar_cadastro()
        else:
            print(f"\nAté logo, {usuario['nome']}!")
            break


# Execução
if __name__ == "__main__":
    menu_principal()
