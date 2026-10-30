# Exercícios de Revisão — Unidade 2

## Questão 1 ✅

**Pergunta:** Qual é a principal finalidade do comando `goto` na linguagem C?

**Resposta assinalada:** Desviar o fluxo de controle para rótulos específicos no código. ✅

**Comentário:**

- **Realizar chamadas de funções recursivas.** Incorreta. O `goto` não é usado para chamar funções recursivas; ele é usado para controlar o fluxo de execução dentro do mesmo escopo de função.
- **Criar loops e estruturas de repetição.** Incorreta. O `goto` não é usado para criar loops e estruturas de repetição. Em vez disso, loops como `for` e `while` são usados para esse fim.
- **Declarar variáveis de ponteiro.** Incorreta. O `goto` não está relacionado à declaração de variáveis de ponteiro. A declaração de variáveis de ponteiro é feita de maneira diferente em C.
- **Inicializar variáveis globais.** Incorreta. O `goto` não é usado para inicializar variáveis globais. A inicialização de variáveis globais é feita no escopo global do programa.
- **Desviar o fluxo de controle para rótulos específicos no código.** ✅ Correta. A principal finalidade do comando `goto` é desviar o fluxo de controle para rótulos específicos no código, permitindo saltos incondicionais para outras partes do programa.

## Questão 2 ✅

Quando aplicado o comando `do/while`, as ações poderão ser executadas pelo menos uma vez antes do teste condicional. Nesse caso, é possível ter uma sequência de repetição de processos, de modo que é possível ter várias opções para a solução de um problema em um programa. Analise o programa abaixo, que realiza a soma dos números positivos usando repetição com teste no final, e complete as partes que estão faltando nas linhas 5, 9 e 12.

```c
#include <stdio.h>
int main() {
    int n;
    int soma = 0;
    ________ {
        printf("Digite um número positivo para ser somado ou negativo para sair: ");
        scanf("%d", &n);
        ________ (n >= 0) {
            soma = soma + n;
        }
    } while (________)
    printf("A soma é %d ", soma);
    return 0;
}
```

**Pergunta:** Assinale a alternativa que completa corretamente as lacunas.

**Resposta assinalada:** "do"; "if"; "n >= 0". ✅

**Comentário:**

Na linha 5, usamos a estrutura `do` para permitir que as ações sejam executadas pelo menos uma vez antes do teste condicional. Na linha 9, usamos o `if` para verificar se o número digitado é positivo antes de somá-lo à variável `soma`. Na linha 12, a condição para continuar repetindo o loop é que `n` seja maior ou igual a zero. Se `n` for negativo, o loop será encerrado.

> 💡 No enunciado falta o `;` depois do `while (...)` da linha 12 — no `do-while` ele é obrigatório: `} while (n >= 0);`.

## Questão 3 ✅

Quando trabalhamos com o comando `for`, podemos encontrar três expressões separadas por ponto e vírgula. A primeira expressão é a **inicialização**, que é executada uma única vez, antes de começar o laço. A segunda é a **condição final**, em que é realizado um teste que determina se a condição é verdadeira ou falsa e, caso seja verdadeira, permanece no laço, caso falsa, encerra o laço e passa para a próxima instrução.

**Pergunta:** Qual o nome da última expressão que é executada depois dos comandos?

**Resposta assinalada:** Incremento. ✅

**Comentário:**

- **Somatório:** não é uma expressão padrão do comando `for` e não descreve uma das etapas mencionadas na descrição.
- **Finalização:** não descreve nenhuma das etapas fornecidas na descrição do comando `for`.
- **Processamento:** não é uma expressão padrão do comando `for` e não corresponde a nenhuma das etapas descritas.
- **Incremento:** ✅ descreve a última expressão do comando `for`, que é executada após os comandos em cada iteração do laço. Geralmente, é usada para aumentar ou diminuir o valor de uma variável de controle.
- **Substituição:** não é um termo comumente associado ao comando `for` e não descreve uma das etapas mencionadas.

## Questão 4 ✅

Sobre as estruturas de repetição condicional, analise as afirmativas a seguir:

- **I.** No comando `while` o programa não executará nenhuma repetição (e as ações que ali dentro estiverem programadas) sem antes testar uma condição.
- **II.** O laço `do-while` analisa a condição ao final do laço, ou seja, os comandos são executados antes do teste de condição.
- **III.** No laço `do-while` o programa não executará nenhuma repetição sem antes testar uma condição.

**Pergunta:** Neste contexto, é correto o que se afirma em:

**Resposta assinalada:** I e II, apenas. ✅

**Comentário:**

- **I. Correta.** O comando `while` em C testa a condição antes de executar o bloco de código associado a ele. Se a condição for falsa, o bloco de código não será executado.
- **II. Correta.** O `do-while` executa o bloco de código pelo menos uma vez e depois verifica a condição. Se a condição for verdadeira, o bloco de código é executado novamente.
- **III. Incorreta.** O `do-while` executa o bloco de código pelo menos uma vez, independentemente da condição. Depois, ele verifica a condição e continua a repetição se a condição for verdadeira.

## Questão 5 ✅

Analise o código do programa abaixo, em que foi utilizada a estrutura de repetição com variável de controle:

```c
#include <stdio.h>
int main(){
    int contador; // variável de controle do loop
    for (contador = 1; contador <= 10; contador++) {
        printf("%d ", contador);
    }
    return 0;
}
```

**Pergunta:** Após analisar o programa, qual é a leitura que podemos fazer da linha 4?

**Resposta assinalada:** Na primeira expressão, "contador" tem o seu valor iniciado em "1". Na segunda expressão, "contador" está condicionado a ser menor ou igual a "10". Na terceira expressão, "contador" será incrementado de 1 ao seu valor. ✅

**Comentário:**

- **Iniciado em 1; condicionado a ser igual a 10; incremento de 1.** Incorreta, pois a segunda expressão verifica se o contador é menor ou igual a 10, não igual a 10.
- **Iniciado em 1; condicionado a ser menor que 10; incremento de 1.** Incorreta, pois a segunda expressão verifica se o contador é menor ou igual a 10, não apenas menor que 10.
- **Iniciado em 1; condicionado a ser maior ou igual a 10; decremento de 1.** Incorreta, pois a segunda expressão verifica se o contador é menor ou igual a 10, não maior ou igual a 10.
- **Iniciado em 0; condicionado a ser menor ou igual a 10; incremento de 2.** Incorreta, pois o contador começa em 1, não em 0, e é incrementado em 1, não em 2.
- **Iniciado em 1; condicionado a ser menor ou igual a 10; incremento de 1.** ✅ Correta; descreve precisamente as operações realizadas na linha 4.

**Saída do programa:** `1 2 3 4 5 6 7 8 9 10`
