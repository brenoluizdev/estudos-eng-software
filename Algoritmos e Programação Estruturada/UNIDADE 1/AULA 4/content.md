# Aula 4 — Operadores e Expressões

## Ponto de Partida

A base fundamental de um computador reside na capacidade de receber dados, processá-los e apresentar os resultados. Portanto, é fundamental entender o processamento de dados utilizando operações e expressões matemáticas, combinando-as com o uso de operadores lógicos.

> Com o intuito de manter a progressão do treinamento e contribuir com o avanço tanto teórico quanto prático, proponha à sua equipe de estagiários o desenvolvimento de um programa em C que calcule a média da quantidade de produtos vendidos anualmente por uma empresa de varejo com base nos dados apresentados na Tabela 1. Qual é a média de produtos vendidos em 2020, 2021 e 2022? É possível identificar qual ano teve a média mais alta? Há alguma outra abordagem para comparar os dados? Certifique-se de apresentar o programa resultante para toda a equipe.

| Tipo de produto | 2020 | 2021 | 2022 |
|---|:---:|:---:|:---:|
| **TV** | 800 | 950 | 725 |
| **Notebook** | 650 | 550 | 700 |
| **Smartphone** | 1500 | 1800 | 2100 |

*Tabela 1 | Relação de produtos vendidos por ano (quantidade de produtos vendidos por ano).*

Agora é o momento de iniciar esta jornada. Preste muita atenção na aula e tenha um excelente estudo!

---

## Vamos Começar!

Olá! Com o conhecimento sobre algoritmos e como criá-los por meio de linguagem natural e fluxogramas, o próximo é a representação por meio de uma linguagem de programação. Portanto você irá agora aprofundar no estudo da linguagem de programação C.

### Operadores Aritméticos

Vamos começar a aprimorar nossos algoritmos com as operações aritméticas. Veja na Tabela 2 algumas operações disponíveis nas linguagens de programação e seus respectivos exemplos.

| Operador | Descrição | Exemplo | Resultado |
|:---:|---|---|---|
| `+` | Soma | `8 + 4` | 12 |
| `-` | Subtração | `8 - 4` | 4 |
| `*` | Multiplicação | `8 * 4` | 32 |
| `/` | Divisão | `8 / 4` | 2 |
| `=` | Atribuição | `x = 8` | x = 8 |
| `%` | Módulo | `8 % 4` | 0 |

*Tabela 2 | Operadores aritméticos.*

Quando trabalhamos com operadores em programação, a **ordem de precedência** desempenha um papel crucial. Os operadores aritméticos seguem a seguinte ordem de execução:

1. Parênteses.
2. Potenciação e radiciação.
3. Multiplicação, divisão e módulo.
4. Adição e subtração.

Dentre as operações aritméticas descritas na Tabela 2, a operação de **módulo** (`%`) é usada para calcular o resto da divisão de um número, considerando apenas a parte inteira do quociente. Por exemplo, a divisão inteira de 43 por 3 (`43 / 3`) resulta no valor 14, com resto igual a 1. Portanto, a operação `43 % 3` produz como resultado o valor 1.

Ainda, os operadores aritméticos podem ser categorizados como **unários** ou **binários**. Os operadores binários são aqueles que utilizam dois componentes, e foram abordados na Tabela 2. Já os operadores unários utilizam apenas um componente. Um exemplo de operadores unários são os operadores de **incremento** (`++`) e **decremento** (`--`). Esses operadores aumentam ou diminuem "um" do valor de uma variável e podem ser utilizados de duas maneiras:

| Forma | Sintaxe | Comportamento |
|---|---|---|
| **Pré-incremento / pré-decremento** | `++x` ou `--x` | o valor é alterado **antes** e utilizado na expressão original. |
| **Pós-incremento / pós-decremento** | `x++` ou `x--` | o valor é utilizado na expressão original e **depois** é alterado. |

Veja o trecho de código no Quadro 1 que ilustra esta mecânica dos operadores `++` e `--`. Execute-o em seu computador e verifique a diferença na utilização dos operadores.

```c
#include <stdio.h>
int main(){
    int x, y;
    x = 10; y = x++;
    printf("y = x++ : valor de y => %d\n", y);
    printf("y = x++ : valor de x => %d\n\n", x);
    x = 10; y = x--;
    printf("y = x-- : valor de y => %d\n", y);
    printf("y = x-- : valor de x => %d\n\n", x);
    x = 10; y = ++x;
    printf("y = ++x : valor de y => %d\n", y);
    printf("y = ++x : valor de x => %d\n\n", x);
    x = 10; y = --x;
    printf("y = --x : valor de y => %d\n", y);
    printf("y = --x : valor de x => %d\n\n", x);
    return 0;
}
```

*Quadro 1 | Exemplo de código com operadores aritméticos.*

### Operadores Relacionais

**Operadores relacionais** são fundamentais no processamento de dados em linguagens de programação, pois permitem a comparação entre valores, o que possibilita a execução de ações com base nos resultados obtidos. Por exemplo, é possível criar um programa que some as notas de dois bimestres de um aluno e calcule a média aritmética. A partir desse resultado, se a média for superior a seis, o aluno é considerado aprovado; caso contrário, é reprovado.

Ao lidar com a comparação de valores em programação, utilizamos operadores relacionais. A Tabela 3 apresenta os operadores utilizados em diversas linguagens de programação.

| Operador | Descrição | Exemplo |
|:---:|---|---|
| `==` | Igual a | `x == y` |
| `!=` | Diferente de | `x != y` |
| `>` | Maior que | `x > y` |
| `<` | Menor que | `x < y` |
| `>=` | Maior ou igual a | `x >= y` |
| `<=` | Menor ou igual a | `x <= y` |

*Tabela 3 | Operadores relacionais.*

Os operadores relacionais são empregados na construção de **expressões booleanas**, ou seja, expressões que resultam em verdadeiro ou falso. Em linguagem C, ao realizarmos uma comparação, o resultado é interpretado como **1** (verdadeiro) ou **0** (falso).

Vamos considerar a criação de um programa que solicita dois números inteiros ao usuário e realiza algumas comparações com esses valores. No Quadro 2, é possível observar que na linha 8, comparamos se os números são iguais. Na linha 9, comparamos se o primeiro é maior que o segundo e, na linha 10, se o primeiro é menor ou igual ao segundo. Os respectivos `printf()` irão exibir na tela os valores de saída 0 ou 1 de acordo com o resultado das comparações efetuadas.

```c
#include <stdio.h>
int main(){
    int n1, n2;
    printf("Digite o primeiro numero: ");
    scanf("%d", &n1);
    printf("Digite o segundo numero: ");
    scanf("%d", &n2);
    printf("\n n1 e n2 sao iguais? %d", n1==n2);
    printf("\n n1 e maior que n2? %d", n1>n2);
    printf("\n n1 e menor ou igual a n2? %d", n1<=n2);
    return 0;
}
```

*Quadro 2 | Exemplo de código com operadores relacionais.*

---

## Siga em Frente...

### Operadores Lógicos

Além dos operadores relacionais, outro recurso fundamental no processamento de dados é a utilização de **operadores lógicos**, os quais se baseiam na lógica matemática clássica e na lógica booleana. Na Tabela 4 são apresentados os operadores lógicos que podem ser utilizados em diversas linguagens de programação.

| Operador | Descrição | Exemplo |
|:---:|---|---|
| `!` | Negação (NOT) | `!(x == y)` |
| `&&` | Conjunção (AND) | `(x > y) && (a == b)` |
| `\|\|` | Disjunção (OR) | `(x > y) \|\| (a == b)` |

*Tabela 4 | Operadores lógicos.*

Note que nos exemplos da Tabela 4 os operadores lógicos são usados em conjunto com os operadores relacionais para formar comparações mais complexas.

Aqui estão algumas características importantes a serem assimiladas:

- O operador de **negação** é usado para inverter o resultado de uma expressão.
- O operador de **conjunção** é utilizado para estabelecer condições em que todas as alternativas devem ser verdadeiras.
- O operador de **disjunção** é utilizado para criar condições em que basta uma das condições ser verdadeira para que o resultado seja verdadeiro também.

No Quadro 3, é possível observar o uso dos operadores relacionais e lógicos aplicados na comparação dos valores de três variáveis. Na linha 4, a condição estabelecida será verdadeira se o valor de `a` for igual ao valor de `b` **E** o valor de `a` for igual a `c`; como a primeira condição não é verdadeira, o resultado da expressão será 0. Na linha 5, a condição será verdadeira se uma das condições for satisfeita, portanto o resultado será 1. Por fim, na linha 6, o resultado é invertido utilizando o operador de negação.

```c
#include <stdio.h>
int main(){
    int a=5, b=10, c=5;
    printf("\n (a==b)&&(a==c) = %d", ((a==b)&&(a==c)));
    printf("\n (a==b)||(a==c) = %d", ((a==b)||(a==c)));
    printf("\n !(a==b)||(a==c) = %d", !((a==b)||(a==c)));
    return 0;
}
```

*Quadro 3 | Exemplo de código com operadores lógicos.*

Até aqui você já estudou os três tipos principais de operadores: aritméticos, relacionais e lógicos. Sendo assim, é importante destacar que entre estes três grupos também há uma ordem de precedência que é seguida na execução de expressões.

| Prioridade | Operadores |
|:---:|---|
| 1 | Parênteses para forçar uma avaliação específica. |
| 2 | Operadores unários, como os de incremento (`++`) e decremento (`--`). |
| 3 | Multiplicação (`*`), divisão (`/`) e módulo (`%`). |
| 4 | Adição (`+`) e subtração (`-`). |
| 5 | Operadores relacionais: menor que (`<`), maior que (`>`), menor ou igual (`<=`), maior ou igual (`>=`), igual (`==`) e diferente (`!=`). |
| 6 | Operadores lógicos: 'E' (`&&`), 'OU' (`\|\|`) e 'NÃO' (`!`). |

> **Nota de revisão:** em C, a negação `!` é um operador **unário** e, portanto, tem a mesma prioridade alta de `++`/`--` (nível 2), não a do nível 6. Entre os relacionais, `<`, `>`, `<=`, `>=` vêm antes de `==` e `!=`; e entre os lógicos binários, `&&` é avaliado antes de `||`.

---

## Vamos Exercitar?

Agora é a sua vez de aplicar todo o conhecimento adquirido sobre operadores! Lembre-se que foi requisitado o cálculo da média de produtos vendidos anualmente e, para isso, o primeiro passo é armazenar os dados em variáveis. É importante destacar que não há uma única abordagem para implementar essa solução, já que cada programador possui seu estilo e suas técnicas de implementação individuais (além de que há outras estruturas avançadas de programação que ainda não foram abordadas, mas que serão apresentadas mais adiante).

Vamos proceder ao armazenamento dos dados utilizando variáveis simples. Para cada produto, criaremos três variáveis (uma para cada ano), conforme o exemplo:

```c
int tv_2020, tv_2021, tv_2022;
int noteb_2020, noteb_2021, noteb_2022;
int smart_2020, smart_2021, smart_2022;
```

Serão necessárias outras três variáveis para armazenar a média de cada ano:

```c
float media_2020 = 0;
float media_2021 = 0;
float media_2022 = 0;
```

Em seguida, inseriremos manualmente os valores em todas as variáveis `produto_ano`, ou se desejar que o usuário insira os valores em vez de fornecê-los manualmente, você pode utilizar um `scanf()`.

Depois de inserir os dados, podemos prosseguir para o processamento das informações, que neste caso envolve calcular a média aritmética. Para isso, somamos os dados de cada ano, dividimos pelo número de ocorrências (três) e armazenamos na respectiva variável de média, conforme exemplificado abaixo:

```c
media_2020 = (tv_2020 + noteb_2020 + smart_2020) / 3;
```

Observe que o somatório está entre parênteses, pois a divisão tem precedência sobre a adição.

> **Nota de revisão:** como todas as variáveis da soma são `int` e o divisor `3` também é inteiro, a divisão é **inteira** — a parte decimal é descartada antes de o resultado ser guardado em `media_2020`. Para obter a média com casas decimais, divida por `3.0` (ou faça um *cast*: `(float)(tv_2020 + noteb_2020 + smart_2020) / 3`).

Após calcular as médias dos demais anos, 2021 e 2022, você pode utilizar operadores relacionais e lógicos para determinar qual ano teve a maior média. Por exemplo, para verificar se 2020 teve a maior média de produtos vendidos, você pode usar o seguinte comando:

```c
printf("2020 obteve a maior media? %d", ((media_2020 > media_2021) && (media_2020 > media_2022)));
```

Certifique-se de imprimir as médias e os testes lógicos. Complete o código com os cálculos necessários e as comparações apropriadas, conforme os exemplos dados, execute-o e verifique se todos os membros da equipe conseguem fazer o programa funcionar.

> Os operadores relacionais e lógicos podem ser incorporados em estruturas condicionais. Na próxima unidade, você aprenderá sobre esse recurso e poderá aprimorar suas implementações.

---

## Saiba mais

Para entender melhor o conceito de variáveis e como elas são utilizadas e declaradas na linguagem C, sugerimos a leitura do **Capítulo 2 - Lendo e escrevendo nas variáveis**, do livro *Linguagem C: Completa e Descomplicada*, disponível na Biblioteca Virtual.

> BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 2, p. 25-47.

Com relação aos tipos de variáveis que podemos utilizar, o **Capítulo 2 - Tipos de Dados Básicos**, do livro *Linguagem C*, complementa bem o assunto.

> DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 2, p. 21-50.

Para auxiliar no desenvolvimento de programas na linguagem C, uma ótima prática é verificar a documentação da linguagem para entender em detalhes os principais tipos de funções e elementos utilizados. Para isso, sugerimos a consulta da seguinte documentação sempre que achar necessário. Nela você encontra todas as bibliotecas utilizadas na linguagem e como utilizar suas principais funções: **Referência da Linguagem C**.

---

## Referências

- BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023.
- CORMEN, T. H. **Desmistificando algoritmos**. 1. ed. Rio de Janeiro: Elsevier, 2014.
- DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023.
- MENÉNDEZ, A. **Simplificando algoritmos**. 1. ed. Rio de Janeiro: LTC, 2023.
- PIVA JUNIOR, D. **Algoritmos e programação de computadores**. 2. ed. Rio de Janeiro: Elsevier, 2019.
