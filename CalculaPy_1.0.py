import os
import time

# Constantes de cores ANSI para estilizar o terminal
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
NEGRITO = "\033[1m"
RESET = "\033[0m"


def limpar_tela() -> None:
    """Limpa o terminal de acordo com o sistema operacional (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


# ---------------- OPERAÇÕES MATEMÁTICAS ---------------- #

def somar(a: float, b: float) -> float:
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        # Lançamos um erro real em vez de retornar texto
        raise ZeroDivisionError("Não é possível realizar divisão por zero.")
    return a / b


# Mapeamento centralizado de operações (Menu dinâmico)
OPERACOES = {
    "1": {"nome": "Soma", "simbolo": "+", "funcao": somar},
    "2": {"nome": "Subtração", "simbolo": "-", "funcao": subtrair},
    "3": {"nome": "Multiplicação", "simbolo": "×", "funcao": multiplicar},
    "4": {"nome": "Divisão", "simbolo": "÷", "funcao": dividir},
}


# ---------------- ENTRADAS E INTERFACE ---------------- #

def obter_numero(mensagem: str) -> float:
    """Solicita um número ao usuário, aceita vírgula e valida a entrada."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print(f"{VERMELHO}⚠ Entrada inválida! Por favor, digite um número real.{RESET}")


def exibir_cabecalho() -> None:
    print(f"{AZUL}{NEGRITO}┌───────────────────────────────────────────┐")
    print("│         CALCULADORA INTELIGENTE           │")
    print(f"└───────────────────────────────────────────┘{RESET}")


def exibir_menu() -> None:
    exibir_cabecalho()
    for chave, dados in OPERACOES.items():
        print(f"  {AMARELO}[{chave}]{RESET} {dados['nome']} ({dados['simbolo']})")
    print(f"  {AMARELO}[0]{RESET} Sair")
    print(f"{AZUL}─────────────────────────────────────────────{RESET}")


# ---------------- FLUXO PRINCIPAL ---------------- #

def main() -> None:
    while True:
        limpar_tela()
        exibir_menu()
        
        opcao = input(f"\n{NEGRITO}Escolha uma opção: {RESET}").strip()

        if opcao == "0":
            limpar_tela()
            print(f"{VERDE}Obrigado por usar a calculadora! Encerrando...{RESET}")
            time.sleep(1.5)
            break

        if opcao not in OPERACOES:
            print(f"{VERMELHO}Opção inválida! Escolha uma opção do menu.{RESET}")
            time.sleep(1.2)
            continue

        operacao = OPERACOES[opcao]
        print(f"\n{AZUL}» Operação Selecionada: {operacao['nome']}{RESET}\n")

        # Coleta dos números
        num1 = obter_numero("Digite o 1º número: ")
        num2 = obter_numero("Digite o 2º número: ")

        # Execução com captura de erro matemático
        try:
            resultado = operacao["funcao"](num1, num2)
            print(f"\n{VERDE}{NEGRITO}✔ Resultado: {num1} {operacao['simbolo']} {num2} = {resultado:g}{RESET}")
        except ZeroDivisionError as erro:
            print(f"\n{VERMELHO}{NEGRITO}✖ Erro Matemático: {erro}{RESET}")

        # Pausa para o usuário ler o resultado antes de limpar a tela
        print(f"\n{AZUL}─────────────────────────────────────────────{RESET}")
        input("Pressione [Enter] para continuar...")


if __name__ == "__main__":
    main()