# Aula 4 — Controle de Repetição

## Ponto de Partida

Olá! Nesta aula vamos explorar o uso das declarações **`break`** e **`continue`**, além do comando **`goto`** para nos auxiliar a controlar as estruturas de repetições em diferentes situações.

> Você trabalha em uma instituição educacional e recebeu uma tarefa relacionada à administração de disciplinas e controle de alunos matriculados. Você precisa criar um sistema que gerencia o número de alunos matriculados em cada disciplina da instituição. Nesse cenário, o programa deve permitir que o administrador insira o número de disciplinas disponíveis e, em seguida, para cada disciplina, o número de alunos matriculados. O programa deve estar preparado para controlar a entrada de dados e **interromper a contagem de disciplinas se o número total de alunos matriculados atingir um certo limite**.

Agora surge a questão: como fazer este controle de interrupção de uma forma simples e eficaz? Caro estudante, vamos em frente nos estudos desta aula que com toda certeza você conseguirá superar o desafio!

---

## Vamos Começar!

### Forçar interrupção de repetição: `break`

Em C, a declaração `break` é utilizada para **encerrar o fluxo de execução de um laço ou de um `switch`**. Ela pode ser utilizada somente dentro de uma construção de controle, como `for`, `while`, `do-while` e `switch`. O `break` é frequentemente utilizado em situações em que o programador deseja interromper imediatamente a execução de um loop ou de um bloco `switch`, e assim sair do contexto atual de execução.

Vamos analisar as características do `break` nos diferentes contextos que pode ser aplicado:

| Contexto | Comportamento |
|---|---|
| **Loop** | quando o `break` é encontrado, a execução do loop é imediatamente interrompida, e o controle é passado para a instrução que segue o loop. |
| **Switch** | o `break` é utilizado para sair do bloco `switch` quando um `case` correspondente é encontrado e executado. Se o `break` não for usado, a execução continuará nos `case`s seguintes até que um `break` seja encontrado ou até o fim do bloco `switch` ser alcançado. |

Para compreender melhor o uso do `break`, veja o exemplo no Quadro 1. Neste programa, um número secreto é predefinido como 7. O programa solicita que o usuário insira um número e verifica se este é igual ao número secreto. Se o número inserido for igual ao número secreto, o programa imprime uma mensagem de parabéns e usa `break` para sair do loop `while`. Caso contrário, o programa continua pedindo ao usuário que insira um novo número até que o número correto seja adivinhado. O uso de `break` garante que o loop seja interrompido assim que o número correto for inserido.

```c
#include <stdio.h>
int main(){
    int numero_secreto = 7;
    int tentativa;
    printf("Adivinhe o número secreto!\n");
    while (1) { // Causa um loop infinito
        printf("Insira um número: ");
        scanf("%d", &tentativa);
        if (tentativa == numero_secreto) {
            printf("Parabéns! Você adivinhou o número secreto.\n");
            break; // Sai do loop quando o número correto é adivinhado
        } else {
            printf("Tente novamente!\n");
        }
    }
    return 0;
}
```

*Quadro 1 | Exemplo de código com `break`.*

### Reiniciar repetição: `continue`

O comando `continue` é uma estrutura de controle na linguagem de programação C que é usado para **pular a execução das instruções restantes em um loop**, e então continuar com a próxima iteração desse loop. Diferente do `break`, que encerra completamente o loop, o `continue` permite ao programador pular apenas o restante do bloco de código da iteração atual dentro do loop e avançar para a próxima iteração, ignorando as instruções restantes dentro do bloco. **Mas o loop não é encerrado!**

Veja agora as características e a definição do comando `continue` na linguagem C, e tente traçar um paralelo de comparação com o comando `break` estudado anteriormente:

- **Pular iteração:** o `continue` é usado para pular a iteração atual do loop, ou seja, ele faz com que o programa ignore o restante das instruções no bloco do loop atual e avance para a próxima iteração do loop.
- **Útil para filtragem:** o `continue` é frequentemente utilizado para implementar condições de filtragem em um loop, permitindo que certas iterações sejam ignoradas com base em uma condição específica.

Vamos agora a um exemplo usando `continue`. O programa do Quadro 2 percorre os números de 1 a 20 e a cada iteração testa se o número corrente é par, e caso o seja, o programa interrompe a iteração e não imprime o número (pois irá pular o `printf` em seguida). Ao final, o programa exibe apenas os números ímpares de 1 a 20.

```c
#include <stdio.h>
int main(){
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            continue; // Pula iterações com números pares
        }
        printf("%d ", i);
    }
    return 0;
}
```

*Quadro 2 | Exemplo de código com `continue`.*

| | `break` | `continue` |
|---|---|---|
| **O que faz** | encerra o laço (ou `switch`) inteiro | pula o resto da iteração atual |
| **Para onde vai o fluxo** | primeira instrução **depois** do laço | próxima iteração (no `for`, executa o incremento antes) |
| **Vale no `switch`?** | sim | não (só em laços) |

---

## Siga em Frente...

### Fluxo de execução arbitrário: `goto`

O comando `goto` é uma instrução na linguagem C que permite realizar **desvios não estruturados** em um programa. Em outras palavras, o `goto` permite que você pule de um local específico em um programa para outro local marcado por um **rótulo**. Embora o uso de `goto` seja desencorajado na maioria das situações, em algumas circunstâncias específicas, e em problemas simples, pode ser útil para simplificar a lógica de um programa. No entanto, seu uso indiscriminado pode tornar o código mais difícil de entender e dar origem a problemas de legibilidade e manutenção.

A seguir, podemos observar a sintaxe do comando `goto` na linguagem C. Veja que o comando `goto` é seguido por um rótulo (identificador), e o rótulo é declarado seguido por dois pontos (`:`). O rótulo é uma marca que você coloca em algum lugar no seu código onde deseja que o `goto` salte. Por exemplo:

```c
goto meu_rotulo;
// ...
meu_rotulo: // O rótulo
```

Antes de irmos aos exemplos, é importante que você se atente a estas características do comando `goto`:

| Característica | Descrição |
|---|---|
| **Desvios não estruturados** | o `goto` permite que você faça desvios não estruturados, o que significa que ele pode pular para qualquer lugar no programa no qual um rótulo seja definido. |
| **Riscos de uso indevido** | o `goto` pode tornar o código complexo e difícil de entender. Uso inadequado de `goto` pode levar a problemas como loops infinitos, pontos de saída inesperados e tornar o código propenso a erros. |
| **Escopo local** | o `goto` é limitado à mesma função e não pode ser usado para desviar o controle para fora dela. |
| **Alternativas mais estruturadas** | em muitos casos, é possível substituir o `goto` por estruturas de controle mais estruturadas, como `if`, `else`, `while`, `for` e funções. Isso torna o código mais legível e mais fácil de depurar e manter. |

Veja agora o exemplo do Quadro 3, em que o `goto` é usado para direcionar o fluxo de execução para o rótulo `erro` se o número inserido não for positivo. O programa imprime uma mensagem de erro e termina. Este é um exemplo de uso cuidadoso de `goto` para manipular situações específicas, porém, é possível perceber que um simples `if-else` resolveria o problema, e ficaria muito mais simples de entender a lógica!

```c
#include <stdio.h>
int main(){
    int numero;
    printf("Insira um número positivo: ");
    scanf("%d", &numero);
    if (numero <= 0) {
        goto erro; // Vai para o rótulo 'erro' se o número não for positivo
    }

    printf("Número válido: %d\n", numero);
    return 0;

erro: // Rótulo para manipular erro
    printf("Erro: Número inválido.\n");
    return 0;
}
```

*Quadro 3 | Exemplo de código com `goto`.*

---

## Vamos Exercitar?

Prezado estudante, agora é o momento de abordar a resolução do problema requisitado pela instituição de ensino, para o qual você precisa criar um programa em linguagem C que possa administrar as disciplinas e o número de alunos matriculados.

O programa deve permitir que o administrador insira o número de disciplinas e o número de alunos matriculados em cada uma delas. Em seguida, o programa precisa verificar se o número de alunos é válido e se o limite total de alunos é atingido. Se o limite for atingido, o programa interrompe a contagem de disciplinas usando `break`. O uso de `continue` permite pular para a próxima iteração do loop se um número de alunos inválido for inserido. O programa então exibe o total de disciplinas contadas e o total de alunos matriculados.

A resolução está presente no Quadro 4.

```c
#include <stdlib.h>
#include <string.h>
int main() {
    int total_disciplinas, limite_alunos = 100, total_alunos = 0;

    printf("Sistema de contagem de alunos matriculados!\n");
    printf("Insira o número de disciplinas disponíveis: ");
    scanf("%d", &total_disciplinas);

    for (int i = 1; i <= total_disciplinas; i++) {
        int alunos_matriculados;
        printf("Insira o número de alunos matriculados na disciplina %d: ", i);
        scanf("%d", &alunos_matriculados);
        // Verifica se o número de alunos matriculados é válido
        if (alunos_matriculados < 0) {
            printf("Número de alunos inválido. Tente novamente.\n");
            i--; // Volta para a mesma disciplina
            continue; // Pula para a próxima iteração do loop
        }

        total_alunos += alunos_matriculados;

        // Verifica se o limite de alunos foi atingido
        if (total_alunos >= limite_alunos) {
            printf("Limite de alunos atingido. Encerrando contagem de disciplinas.\n");
            break; // Encerra o loop de contagem de disciplinas
        }
    }
    printf("Total de disciplinas contadas: %d\n", total_disciplinas);
    printf("Total de alunos matriculados: %d\n", total_alunos);
    return 0;
}
```

*Quadro 4 | Exemplo de solução.*

> 💡 Repare no par `i--; continue;`: como o `continue` em um `for` ainda executa o incremento `i++`, o `i--` anterior faz o laço "voltar" para a mesma disciplina.

> **Nota de revisão:** quando o `break` interrompe a contagem, a mensagem final ainda imprime `total_disciplinas` (o valor digitado no início), e não quantas disciplinas foram de fato contadas. Para mostrar o número real, seria preciso guardar o valor de `i` em uma variável declarada fora do `for`. Falta também `#include <stdio.h>` (e `<string.h>` não é usado).

> Reforçamos que não há uma única resposta correta, e o importante é chegarmos em uma solução eficaz que utiliza os conceitos aprendidos até aqui! Não se esqueça que sempre há espaço para otimizações de código, então vale a pena buscar alternativas de implementações e se atualizar sempre! Bons estudos!

---

## Saiba mais

Para entender melhor o conceito dos comandos `break`, `continue` e `goto` em C, sugerimos a leitura do **Capítulo 4 - Laços**, do livro *Linguagem C*, disponível na Biblioteca Virtual.

> DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 4, p. 80-103.

Também sugerimos a leitura do **Capítulo 5 - Comandos de repetição**, do livro *Linguagem C: Completa e Descomplicada*, disponível na Biblioteca Virtual, para complementar os estudos sobre `break`, `continue` e `goto`.

> BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 5, p. 88-108.

Para auxiliar no desenvolvimento de programas na linguagem C, uma ótima prática é verificar a documentação da linguagem para entender em detalhes os principais tipos de funções e elementos utilizados. Para isso, sugerimos a consulta da seguinte documentação sempre que achar necessário. Nela você encontra todas as bibliotecas utilizadas na linguagem e como utilizar suas principais funções: **Referência da Linguagem C**.

---

## Referências

- BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 4, p. 67-87.
- DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 3, p. 51-79.
- PIVA JUNIOR, D. **Algoritmos e programação de computadores**. 2. ed. Rio de Janeiro: Elsevier, 2019.
