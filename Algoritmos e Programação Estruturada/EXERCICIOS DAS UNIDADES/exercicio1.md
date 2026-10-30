# Exercícios de Revisão — Unidade 1

## Questão 1 ✅

Analise as afirmativas a seguir a respeito dos símbolos utilizados na construção de diagramas de blocos para algoritmos.

**I.** O símbolo a seguir significa um terminal, em que representa o início ou o fim de um fluxo lógico.

![Símbolo da afirmativa I](image.png)

**II.** O símbolo a seguir significa exibição, em que mostra o resultado de uma ação, geralmente através da tela de um computador.

![Símbolo da afirmativa II](image-1.png)

**III.** O símbolo a seguir significa decisão/condicional, em que representa os desvios condicionais nas operações de tomada de decisão e laços condicionais.

![Símbolo da afirmativa III](image-2.png)

**Pergunta:** Neste contexto, é correto o que se afirma em:

**Resposta assinalada:** II, apenas. ✅

**Comentário:**

- **I. Incorreta.** O símbolo terminal é:

  ![Símbolo terminal](image-3.png)

- **II. Correta.** O texto confere com o símbolo ilustrado.
- **III. Incorreta.** O símbolo de decisão/condicional é:

  ![Símbolo de decisão/condicional](image-4.png)

## Questão 2 ✅

Considere o seguinte trecho de código em linguagem C:

```c
#include <stdio.h>

int main() {
    short int x;
    unsigned float y;
    char z;
    x = 5;
    y = 3.14;
    z = 'A';
    printf("O valor de x é %d, o valor de y é %f e o valor de z é %c", x, y, z);
    return 0;
}
```

Avalie as afirmações a seguir referentes ao trecho de código acima:

- **I.** A variável `x` é do tipo inteiro e ocupa 4 bytes de memória.
- **II.** A variável `y` é do tipo ponto flutuante e ocupa 8 bytes de memória.
- **III.** A variável `z` é do tipo caractere e ocupa 1 byte de memória.
- **IV.** O valor de `x` será impresso como "5", o valor de `y` será impresso como "3.14" e o valor de `z` será impresso como "A".
- **V.** Se a linha `y = 3.14;` fosse alterada para `y = 3;`, o valor de `y` ainda seria impresso sem a ocorrência de erros.

**Pergunta:** Neste contexto, é correto o que se afirma em:

**Resposta assinalada:** III, IV e V, apenas. ✅

**Comentário:**

- **I. Falsa.** Na linguagem C, um `int` geralmente ocupa 4 bytes de memória, porém o uso do modificador `short` faz com que a variável inteira `x` ocupe somente 2 bytes.
- **II. Falsa.** Uma variável do tipo `float` em C normalmente ocupa 4 bytes de memória, mesmo que o modificador `unsigned` seja utilizado, já que ele apenas diz que a variável irá armazenar apenas valores positivos (incluindo zero).
- **III. Verdadeira.** Uma variável do tipo `char` em C ocupa 1 byte de memória.
- **IV. Verdadeira.** As variáveis serão impressas como indicado nos especificadores de formato `%d`, `%f` e `%c` na função `printf`.
- **V. Verdadeira.** Mesmo que uma variável `float` receba um valor inteiro, esta irá imprimi-lo normalmente com o `%f`, sem gerar erros.

> **Nota de revisão:** o gabarito trata `unsigned float` como válido, mas em C **os modificadores `unsigned`/`signed` só se aplicam a tipos inteiros** (`char`, `short`, `int`, `long`). `unsigned float y;` é **erro de compilação** (GCC: *"both 'unsigned' and 'float' in declaration specifiers"*), então, a rigor, o programa nem compila. Além disso, `%f` imprime `3.140000` (6 casas), não "3.14" como diz a afirmativa IV. A resposta assinalada corresponde ao raciocínio esperado pela instituição (tamanhos dos tipos e especificadores), mas fique atento a esses dois detalhes.

## Questão 3 ✅

Analise as afirmativas a seguir a respeito dos códigos de controle utilizados nas funções de entrada e saída em C:

- **I.** `%i` é utilizado para exibir um número inteiro.
- **II.** `%f` é utilizado para exibir um número em ponto flutuante (decimal).
- **III.** `%c` é utilizado para exibir um caractere.
- **IV.** `%s` é utilizado para exibir uma sequência de caracteres.
- **V.** `%nc` é utilizado para exibir um número em notação científica.

**Pergunta:** Neste contexto, é correto o que se afirma em:

**Resposta assinalada:** II, III e IV, apenas. ✅

**Comentário:**

- **I. Incorreta.** `%d` é que é utilizado para exibir um número inteiro.
- **II. Correta.** `%f` é utilizado para exibir um número em ponto flutuante (decimal).
- **III. Correta.** `%c` é utilizado para exibir um caractere.
- **IV. Correta.** `%s` é utilizado para exibir uma sequência de caracteres.
- **V. Incorreta.** `%e` é que é utilizado para exibir um número em notação científica.

> **Nota de revisão:** a afirmativa I foi considerada incorreta porque o material da disciplina só apresenta `%d` para inteiros. Na linguagem C real, porém, **`%i` também exibe inteiros** no `printf` (é equivalente a `%d`; a diferença só aparece no `scanf`, onde `%i` aceita entradas em octal/hexadecimal como `012` ou `0x1A`). Para a prova, siga o gabarito; na prática, saiba que `%i` funciona.

## Questão 4 ✅

Sobre a representação de algoritmos em linguagem natural, analise as afirmativas a seguir:

- **I.** A principal vantagem da representação de algoritmos por meio da linguagem natural é a clareza e compreensão intuitiva.
- **II.** A principal desvantagem é a necessidade de aprender um novo idioma para programar.
- **III.** A linguagem natural facilita de maneira direta e eficaz a descrição de problemas e suas respectivas soluções.

**Pergunta:** Neste contexto, é correto o que se afirma em:

**Resposta assinalada:** III, apenas. ✅

**Comentário:**

- **I. Incorreta.** A representação por linguagem natural deixa a possibilidade de ambiguidades e interpretações diversas, não sendo, portanto, uma representação clara.
- **II. Incorreta.** A vantagem da linguagem natural é justamente o fato de não ser necessário aprender um novo idioma para entender os algoritmos.
- **III. Correta.** A linguagem natural facilita de maneira direta e eficaz a descrição de problemas e suas respectivas soluções, pois não necessita de aprender nenhum tipo de estrutura ou códigos específicos.

## Questão 5 ✅

**Pergunta:** Qual é a importância da divisão de um algoritmo em três componentes principais: entrada, processamento e saída?

**Resposta assinalada:** A divisão em entrada, processamento e saída é importante porque permite uma compreensão mais abrangente das etapas necessárias para resolver um problema por meio de um algoritmo. ✅

**Comentário:**

- **"A divisão em entrada, processamento e saída é importante porque torna o algoritmo mais complexo e difícil de compreender."** Incorreta, pois a divisão em entrada, processamento e saída tem o objetivo de tornar o algoritmo mais claro e compreensível, facilitando a compreensão das etapas envolvidas na resolução de um problema.
- **"A divisão em entrada, processamento e saída não é relevante na criação de algoritmos, pois o importante é apenas a sequência de passos."** Incorreta. A divisão em entrada, processamento e saída é fundamental na criação de algoritmos, pois ajuda a organizar as etapas e a compreender o fluxo de informações e a transformação de dados.
- **"A divisão em entrada, processamento e saída é importante apenas em algoritmos de culinária, como o da receita de bolo."** Incorreta. A divisão em entrada, processamento e saída é relevante em algoritmos de diversas áreas, não se limitando apenas a receitas de culinária. Ela é uma abordagem geral na criação de algoritmos para resolver uma ampla gama de problemas.
- **"A divisão em entrada, processamento e saída é uma convenção estabelecida pela ANSI para que todos os algoritmos possam seguir a mesma padronização de sintaxe."** Incorreta. A divisão em entrada, processamento e saída não define nenhum tipo de padronização de sintaxe.
- **"A divisão em entrada, processamento e saída é importante porque permite uma compreensão mais abrangente das etapas necessárias para resolver um problema por meio de um algoritmo."** ✅ Correta. A divisão em entrada, processamento e saída é fundamental porque ajuda a compreender as diferentes fases do algoritmo, desde a aquisição dos dados de entrada até a geração do resultado desejado.
