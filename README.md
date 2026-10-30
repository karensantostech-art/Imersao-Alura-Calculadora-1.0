# 🧮 CalculaPy 1.0 - Calculadora em Python

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

Uma calculadora de terminal elegante, modular e robusta desenvolvida em Python utilizando o Google IA Studio. O **CalculaPy** realiza as quatro operações fundamentais com foco em uma experiência de usuário (UX) fluida, interface visual limpa no terminal e prevenção de falhas de execução.

---

## 📸 Demonstração da Interface

```text
┌───────────────────────────────────────────┐
│         CALCULADORA INTELIGENTE           │
└───────────────────────────────────────────┘
  [1] Soma (+)
  [2] Subtração (-)
  [3] Multiplicação (×)
  [4] Divisão (÷)
  [0] Sair
─────────────────────────────────────────────
```

# ✨ Principais Funcionalidades

Operações Básicas: Soma (+), Subtração (-), Multiplicação (×) e Divisão (÷).

### Prevenção de Travamentos:
  * Tratamento nativo contra divisão por zero (ZeroDivisionError).
  * Validação de dados de entrada: impede que textos ou caracteres inválidos quebrem a execução (ValueError).

### UX Aprimorada:
  * Aceita decimais formatados tanto no padrão brasileiro (com vírgula: 5,5) quanto internacional (com ponto: 5.5).
  * Terminal interativo estilizado com cores ANSI.
  * Limpeza automática de tela (cls/clear) entre cálculos.
  * Formatação inteligente de resultados (exibe inteiros sem zeros desnecessários, ex: 4 em vez de 4.0).

### Arquitetura Modular:
  * Uso de dicionário de operações (Dispatch Table), eliminando cadeias excessivas de if/elif/else.
  * Funções com Type Hints (anotações de tipo) para melhor legibilidade e manutenibilidade.

# Tecnologias Utilizadas

O projeto foi construído utilizando O Google AI Studio, que utilizou exclusivamente a biblioteca 
padrão do Python, sem dependências externas adicionais:

* `Python 3`: Linguagem principal do projeto.
* `os`: Utilizado para detecção do sistema operacional e limpeza do terminal.
* `time`: Utilizado para pequenos intervalos visuais nas mensagens de feedback ao usuário.

# 🚀 Como Executar o Projeto

## Pré-requisitos

* Certifique-se de ter o Python 3.8+ instalado no seu computador.
* Ter o Git instalado (opcional, para clonar o repositório).

### Passo a Passo

#### 1. Obter o Código

**Via Git :**
```bash
git clone https://github.com/karensantostech-art/Imersao-Alura-Calculadora-1.0.git
cd Imersao-Alura-Calculadora-1.0
```

* Ou baixe o arquivo ZIP diretamente pelo botão verde **Code > Download ZIP** no GitHub e descompacte a pasta no seu computador.*

#### 2. Executar a Aplicação
No terminal ou prompt de comando (dentro da pasta do projeto), execute:

* **No Windows:**
  ```bash
  python CalculaPy_1.0.py
  ```
  *(caso tenha mais de uma versão, pode usar `py CalculaPy_1.0.py`)*

* **No Linux / macOS:**
  ```bash
  python3 CalculaPy_1.0.py
  ```

# 📁 Estrutura do Código

```text
CalculaPy_1.0.py
│
├── Configurações Visuais    # Códigos ANSI para cores e estilos
├── Operações Matemáticas   # Funções puras (somar, subtrair, multiplicar, dividir)
├── Estrutura de Despacho   # Dicionário dinâmico mapeando opções e símbolos
├── Funções de Interface    # Validação de entradas (obter_numero) e menus
└── Fluxo Principal         # Loop do programa com tratamento de erros
```

## 👩‍💻 Autoria e Aprendizado

Desenvolvido com foco na aplicação da IA no Desenvolvimento de Software,sendo o desafio 1 da Imersão DEV na Era da IA da Alura, abrangendo:

* Elaboração de prompts.
* Lógica de Programação.
* Google AI Studio.
* Python






