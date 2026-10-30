# Aula 5 — Encerramento da Unidade: Funções e Passagem de Parâmetros

## Ponto de Chegada

Olá, estudante! Para desenvolver a competência desta Unidade, que é **"conhecer os métodos de funções, recursividade, passagem de dados e parâmetros em algoritmos"**, você deve explorar conceitos fundamentais em programação, concentrando seus estudos em funções e passagem de parâmetros em linguagem C.

### Procedimentos e funções

Comece por compreender a sintaxe de procedimentos e funções. Aqui, aprenderemos como organizar blocos de código para realizar tarefas específicas, tornando o programa mais modular e fácil de manter. Entenderemos como declarar, chamar e definir procedimentos e funções, e como estas estruturas contribuem para a **modularização** do código.

### Escopo

Além disso, estude sobre o escopo de uma função e a distinção entre **variáveis globais e locais**. Compreender o escopo é crucial para evitar conflitos entre variáveis e garantir que elas sejam acessíveis somente onde necessário. Isso não apenas promove a clareza do código, mas também evita potenciais erros decorrentes de variáveis com nomes idênticos em contextos diferentes.

### Passagem de parâmetros

Ao avançar nos estudos, é importante compreender a passagem de parâmetros, que são conceitos fundamentais para a comunicação eficiente entre funções. Explore tanto a **passagem por valor** quanto a **passagem por referência**, entendendo suas implicações no comportamento do programa. Isso proporcionará uma compreensão mais profunda de como os dados são transmitidos e manipulados em diferentes contextos.

### Recursividade

Finalmente, estude a fundo as **funções recursivas**! Entenda o que são e como utilizá-las para resolver problemas que podem ser decompostos em subproblemas semelhantes. A recursividade, quando aplicada corretamente, pode simplificar a lógica do código e oferecer soluções elegantes para desafios complexos.

| Conceito | Ideia-chave | Exemplo |
|---|---|---|
| **Procedimento** | função sem retorno (`void`) | `void imprimir(int v[])` |
| **Função** | retorna um valor do tipo declarado | `int somar(int a, int b)` |
| **Variável local** | existe só dentro da função | `int x;` dentro de `main` |
| **Variável global** | visível em todo o programa | `int x;` antes de `main` |
| **Por valor** | a função recebe uma cópia | `testar(n1, n2)` |
| **Por referência** | a função recebe o endereço | `testar(&n1, &n2)` |
| **Recursão** | a função chama a si mesma até o caso base | `fatorial(n - 1)` |

Compreendendo esses tópicos essenciais, você terá dominado os conceitos, os recursos e as ferramentas fundamentais voltadas para o desenvolvimento de softwares!

---

## É Hora de Praticar!

### Estudo de Caso: Sistema bancário simples

> Realize a implementação de um sistema bancário simples em linguagem C, em que cada cliente possui uma conta com saldo. Desenvolva funções que realizem operações bancárias básicas, como depósito, saque e transferência, utilizando conceitos avançados de passagem de parâmetros.

| Requisito | Descrição |
|---|---|
| **Definição da Estrutura** | declare uma estrutura chamada `Conta` que contenha informações como número da conta, nome do titular e saldo. |
| **Função para Depósito** | crie uma função chamada `realizarDeposito` que permita ao cliente realizar um depósito em sua conta. A função deve receber como parâmetros a estrutura da conta e o valor a ser depositado. |
| **Função para Saque** | implemente a função `realizarSaque` que permita ao cliente fazer um saque de sua conta. A função deve validar se há saldo suficiente antes de efetuar o saque. |
| **Função para Transferência** | desenvolva a função `realizarTransferencia` que permita transferir um valor de uma conta para outra. A função deve receber as estruturas de ambas as contas e o valor a ser transferido. |
| **Apresentação de Resultados** | no programa principal (`main`), crie duas instâncias da estrutura `Conta` para representar duas contas diferentes. Solicite ao usuário que realize operações como depósito, saque e transferência entre as contas. Utilize as funções desenvolvidas para efetuar as operações e apresente o saldo final das contas após cada transação. |
| **Tratamento de Erros** | implemente mecanismos de tratamento de erros, como a verificação de saldo insuficiente durante saques e transferências, e mensagens explicativas para o usuário. |

### Reflita

- Como a escolha entre usar um procedimento ou uma função pode afetar a estrutura e o fluxo do seu código?
- Como a escolha entre passagem por valor e por referência pode impactar a eficiência e o comportamento de um programa?
- Em que situações as funções recursivas podem ser mais vantajosas do que soluções iterativas?

---

## Resolução do Estudo de Caso

O código a seguir apresenta uma sugestão de resultado para o problema:

```c
#include <stdio.h>

struct Conta {
    int numero;
    char titular[50];
    float saldo;
};

void realizarDeposito(struct Conta *conta, float valor) {
    conta->saldo += valor;
}

int realizarSaque(struct Conta *conta, float valor) {
    if (conta->saldo >= valor) {
        conta->saldo -= valor;
        return 1; // Saque bem-sucedido
    } else {
        printf("Saldo insuficiente para realizar o saque.\n");
        return 0; // Saque mal-sucedido
    }
}

int realizarTransferencia(struct Conta *origem, struct Conta *destino, float valor) {
    if (realizarSaque(origem, valor)) {
        realizarDeposito(destino, valor);
        return 1; // Transferência bem-sucedida
    } else {
        printf("Transferência mal-sucedida.\n");
        return 0; // Transferência mal-sucedida
    }
}

int main() {
    // Criação de duas instâncias da estrutura Conta
    struct Conta contas[2] = {{1, "Cliente1", 1000.0},{2, "Cliente2", 500.0}};

    int op, cc, cc2;
    float valor = 0;

    do{
        printf("\n BOLSOFURADO BANK \n\n");

        printf(" Saldo Conta 1: R$%.2f\n", contas[0].saldo);
        printf(" Saldo Conta 2: R$%.2f\n\n", contas[1].saldo);

        printf(" 1 - Deposito\n");
        printf(" 2 - Saque\n");
        printf(" 3 - Transferencia\n");
        printf(" 4 - Sair\n");

        printf("\n Escolha uma opção: ");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            printf("\n Qual a conta para deposito? ");
            scanf("%d", &cc);
            printf(" Qual o valor? ");
            scanf("%f", &valor);
            realizarDeposito(&contas[cc-1], valor);
            break;

        case 2:
            printf("\n Qual a conta para saque? ");
            scanf("%d", &cc);
            printf(" Qual o valor? ");
            scanf("%f", &valor);
            realizarSaque(&contas[cc-1], valor);
            break;

        case 3:
            printf("\n Qual a conta de origem? ");
            scanf("%d", &cc);
            printf(" Qual a conta de destino? ");
            scanf("%d", &cc2);
            printf(" Qual o valor? ");
            scanf("%f", &valor);
            realizarTransferencia(&contas[cc-1], &contas[cc2-1], valor);
            break;

        default:
            break;
        }

    } while(op < 4);

    return 0;
}
```

Repare em como o código aplica os conceitos da unidade:

- As três operações recebem `struct Conta *` — **passagem por referência** — para que a alteração do saldo valha na conta original, e não numa cópia.
- `realizarTransferencia` **reutiliza** `realizarSaque` e `realizarDeposito` (modularização): se o saque falhar, nada é depositado.
- `realizarSaque` e `realizarTransferencia` retornam `1`/`0` (funções), enquanto `realizarDeposito` não retorna nada (procedimento).

> 💡 Pontos a melhorar como exercício: o número da conta digitado não é validado (`cc = 3` acessa `contas[2]`, fora do vetor), valores negativos são aceitos em depósito/saque, e o laço `while(op < 4)` continua para entradas como `0` ou negativos.

> Não há uma resposta correta. Inclusive, fica o desafio para implementar em cada opção os mecanismos de tratamento de erros, como a verificação de saldo insuficiente durante saques e transferências, e mensagens explicativas para o usuário.

---

## Assimile

O infográfico a seguir ilustra e identifica os conceitos vistos nesta unidade.

![Infográfico: funções e passagem de parâmetros](image.png)

---

## Referências

- BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023.
- CORMEN, T. H. **Desmistificando algoritmos**. 1. ed. Rio de Janeiro: Elsevier, 2014.
- DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023.
- MENÉNDEZ, A. **Simplificando algoritmos**. 1. ed. Rio de Janeiro: LTC, 2023.
- PIVA JUNIOR, D. **Algoritmos e programação de computadores**. 2. ed. Rio de Janeiro: Elsevier, 2019.
