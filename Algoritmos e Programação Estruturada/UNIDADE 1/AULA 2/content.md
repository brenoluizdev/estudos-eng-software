# Aula 2 — Conceitos Básicos de Linguagens de Programação

## Ponto de Partida

Uma **linguagem de programação** é um conjunto de regras e símbolos usado para escrever códigos que o computador pode executar. Ela serve como uma ferramenta para os programadores comunicarem instruções precisas ao computador, permitindo que desenvolvam software e aplicativos para uma ampla gama de propósitos.

> Você está trabalhando em uma empresa que se dedica à criação de softwares educacionais. Sua responsabilidade é treinar os estagiários recém-contratados para trabalhar com o desenvolvimento de sistemas na empresa. Esses estagiários não possuíam experiência prévia com algoritmos ou linguagens de programação, porém você já os auxiliou com os conceitos introdutórios de algoritmos e as formas de representação por meio de linguagem natural e fluxogramas.
>
> Para continuar despertando o interesse dos estagiários, você irá apresentar a eles a linguagem de programação C. E para isto, irá desenvolver um programa que permita o cálculo da média de dois valores digitados pelo usuário.
>
> Para concluir este desafio, será importante enfatizar aos estagiários o processo básico de criação de algoritmos, consistindo na definição da **entrada**, do **processamento** e da **saída**.

Agora é o momento de iniciar esta jornada. Preste muita atenção na aula e tenha um excelente estudo!

---

## Vamos Começar!

Olá! Com o conhecimento sobre algoritmos e como criá-los por meio de linguagem natural e fluxogramas, o próximo é a representação por meio de uma linguagem de programação. Portanto, você irá agora se aprofundar no estudo da linguagem de programação C.

### Linguagem de programação e criação de algoritmos

A linguagem de programação é o meio de comunicação de ideias entre o computador e os indivíduos, da mesma forma como as linguagens naturais são utilizadas em nossas interações cotidianas. As primeiras linguagens de computador utilizadas foram as linguagens de máquina e a linguagem Assembly, a partir da década de 1940. Desde então, várias linguagens surgiram, juntamente com o desenvolvimento de novos paradigmas de linguagens de programação.

Cada linguagem de programação destinada à criação de programas possui uma **sintaxe** particular, que se refere à forma como o programa é codificado. A sintaxe de uma linguagem de programação pode ser descrita como a descrição precisa de todos os programas gramaticalmente corretos nessa linguagem.

Um **programa de computador** pode ser definido como um conjunto de instruções ordenadas, em que você fornece comandos ao computador e ele executa tarefas específicas de acordo com as instruções fornecidas. Ou seja, é uma série de instruções organizadas de forma a resolver um problema específico. Esse programa pode ser desenvolvido em módulos distintos e/ou subprogramas.

Para criar um programa de computador, é necessário seguir certos passos:

1. Definir e analisar o problema a ser resolvido, destacando os pontos mais importantes.
2. Definir os **dados de entrada**: coleta de informações.
3. Definir o **processamento**, ou seja, quais cálculos serão executados e as suas restrições. O processamento é responsável pela transformação dos dados de entrada em informações de saída.
4. Definir os **dados de saída**, ou seja, o que será gerado após o processamento: apresentação de todas as informações resultantes do processamento de dados em um dispositivo periférico (monitor, por exemplo).
5. Criar um algoritmo ou um diagrama de fluxo.
6. Testar o algoritmo realizando simulações.

Em um contexto geral, a sequência de instruções para criação de um programa de computador é da seguinte maneira:

1. Definição de bibliotecas.
2. Início do programa.
3. Definição das variáveis e de possíveis atribuições.
4. Instrução de leitura dos dados.
5. Instrução do formato de escrita.
6. Demais instruções e funções.
7. Fim do programa.

### Estrutura básica da Linguagem C

A linguagem C foi criada por **Dennis Ritchie em 1972**, e com a popularização dos microcomputadores, um grande número de programas em C foi criado. Desta forma, um programa desenvolvido em um computador poderia ser executado em outro (**portabilidade**), porém, gerava algumas discrepâncias. Então a **ANSI** (*American National Standards Institute*) padronizou de uma vez por todas a linguagem C.

Vamos analisar o código do Quadro 1, que apresenta a estrutura básica de um programa na linguagem C:

```c
#include <stdio.h>
int main(){
    printf("Hello World!");
    return 0;
}
```

*Quadro 1 | Exemplo básico de programa na linguagem C.*

As primeiras linhas de programação são definidas pelas **bibliotecas**, que incorporam ao nosso programa um conjunto de funções e instruções previamente estabelecidas que não são nativas da linguagem de programação, e que podem ser usadas pelo programa.

Veja alguns exemplos de biblioteca em linguagem de programação C:

| Biblioteca | Finalidade | Utilização |
|---|---|---|
| **stdio** | Funções de entradas e saídas, como é o caso da função `printf` e `scanf` que vamos aprender mais à frente. | `#include <stdio.h>` |
| **stdlib** | Funções envolvendo alocação de memória, controle de processos, conversões e outras. | `#include <stdlib.h>` |
| **string** | Manipulação de strings. | `#include <string.h>` |
| **time** | Manipulação de horas e datas. | `#include <time.h>` |
| **math** | Operações matemáticas. | `#include <math.h>` |

Após a definição das bibliotecas, o programa é inicializado pela **função principal** (`main`). Esta função é delimitada pela utilização de chaves, onde a `{` (chave aberta) indica o início de uma função em C e a `}` (chave fechada) indica o término das funções. Toda a sequência lógica de instruções do programa (declarações de variáveis, leitura de dados, instruções, saída de dados etc.) deve ser definida dentro do `main()`.

Veja que no exemplo do Quadro 1 usamos o tipo `int` antes de `main()`, e isto significa que retornará um número do tipo inteiro. Ao final da função, o `return 0;` indica que a função principal (e neste caso o programa como um todo) terminou e retornou um valor inteiro 0. Mas, para que é importante retornar um valor 0 ao final de qualquer programa? Normalmente, usamos o valor 0 como padrão (`return 0`) para indicar ao sistema operacional que a função foi concluída sem erros. Se ocorrer algum erro durante a execução de `int main()`, um valor inteiro diferente de 0 será retornado. Se você definir sua função apenas como `main()`, nenhum valor será retornado ao final da execução. No entanto, essa prática não é recomendada, pois não seria possível verificar explicitamente se a função foi executada corretamente, sem erros.

Para prosseguir com nossos estudos, vamos explorar conceitualmente as variáveis. Não se preocupe! Na próxima aula, abordaremos esse tema com mais profundidade. As **variáveis** são áreas reservadas na memória para armazenar dados, sendo que cada uma possui um nome único para identificação.

Os tipos de variáveis mais comumente utilizados são:

| Tipo | Descrição |
|---|---|
| **Inteiro** (`int`) | armazena os números inteiros (negativos ou positivos). |
| **Real** (`float`) | permite armazenar valores de pontos flutuantes e frações. Quando se necessita do dobro de dados numéricos é utilizado o tipo `double` ou `long double`. |
| **Caractere** (`char`) | permite armazenar caracteres, números e símbolos especiais. São delimitadas por aspas simples (`'`). |

Veja o seguinte exemplo no Quadro 2:

```c
#include <stdio.h>
int main(){
    int num;
    int num2 = 5;
    float num3;
    char caractere;
    num = 10;
    num3 = 2.5;
    caractere = 'a';
    return 0;
}
```

*Quadro 2 | Exemplo de variáveis na linguagem C.*

O exemplo mostra a declaração de algumas variáveis, seguido da atribuição de valores a elas. Note que uma variável pode ser declarada e ao mesmo tempo ter um valor atribuído a ela, como é o caso em `int num2 = 5`. Outro ponto de atenção consiste na atribuição de um valor para a variável do tipo `char`, no qual o caractere `'a'` é atribuído entre aspas simples (seguindo a sintaxe da linguagem C).

---

## Siga em Frente...

### Entrada e Saída de Dados

#### `printf()`

A função `printf()` é um comando de **saída** que está presente na biblioteca `stdio.h`, e é utilizada quando se pretende exibir ("imprimir") alguma informação na tela do computador.

A sua sintaxe é definida por:

```c
printf("texto e/ou códigos de controle", listas de argumentos);
```

Além de texto, o `printf()` pode exibir valores de variáveis. Porém deve seguir o seguinte formato conforme o exemplo a seguir:

```c
valor1 = 10;
printf("O valor encontrado foi %d", valor1);
```

**Resultado do trecho de código:** `O valor encontrado foi 10`

Perceba que o valor da variável `valor1` foi posicionado no local do `%d`. O `%d` é um código de controle para um dado do tipo inteiro.

A Tabela 1 a seguir apresenta os principais códigos de acordo com os tipos de variáveis declaradas.

| Código | Função |
|---|---|
| `%d` | Exibe/lê um número inteiro |
| `%f` | Exibe/lê um número em ponto flutuante (decimal) |
| `%c` | Exibe/lê um caractere |
| `%s` | Exibe/lê uma sequência de caracteres (string) |
| `%e` | Exibe/lê um número em notação científica |

*Tabela 1 | Códigos de controle utilizados em funções de entrada e saída.*

No `printf()` você pode pular linhas com o comando `\n` e pode também obter um resultado numérico determinando a quantidade de casas decimais.

Veja o exemplo a seguir:

```c
printf("\n Resposta: a = %.2f e b = %.2f\n", a, b);
```

Neste exemplo, antes de apresentar a frase o programa pulou uma linha (`\n`), o `%f` é utilizado quando os dados numéricos são flutuantes, ou seja, valores fracionados. E quando usamos `%.2f` significa que o valor será arredondado em duas casas decimais, por exemplo: 2,45.

#### `scanf()`

A função `scanf()`, também presente na biblioteca `stdio.h`, opera como um comando de **entrada**, permitindo a inserção de dados via teclado. A informação inserida é então armazenada em um espaço específico da memória, designado pelo nome e tipo específico da variável. Sua sintaxe é definida por um código de controle (sempre entre aspas duplas) e pela lista de argumento:

```c
scanf("códigos de controle", lista de argumentos);
```

O `scanf()` utiliza os mesmos códigos de controle listados na Tabela 1. Veja o seguinte exemplo:

```c
int var;
scanf("%d", &var);
```

Neste exemplo, o computador ficará esperando que o usuário digite um valor numérico inteiro (devido ao uso do código `%d`) para ser armazenado na variável inteira `var`. O operador `&` é utilizado em conjunto com a função `scanf()` para indicar o **endereço** de uma variável. Isso ocorre porque a função `scanf()` necessita de referências de memória das variáveis nos quais os valores de entrada serão armazenados.

Segue um exemplo de programa em C utilizando `scanf()` e `printf()` no Quadro 3:

```c
#include <stdio.h>
int main(){
    int num;
    printf("Digite um número: ");
    scanf("%d", &num);
    printf("Você digitou: %d", num);
    system("pause");
    return 0;
}
```

*Quadro 3 | Exemplo de programa em C utilizando `scanf` e `printf`.*

Neste exemplo simples, o programa aguarda que o usuário digite um valor numérico inteiro, que será armazenado na variável `num` e em seguida é exibido na tela com o `printf`. Perceba que aqui temos o uso da instrução `system("pause")`, que pausa o fluxo de execução do programa naquele ponto para que o resultado seja visualizado.

> **Nota de revisão:** a função `system()` é declarada em `stdlib.h`, que não foi incluída no Quadro 3. Para compilar sem avisos, adicione `#include <stdlib.h>`. Além disso, `system("pause")` só funciona no Windows (é um comando do `cmd`).

---

## Vamos Exercitar?

Agora é a hora de aplicar todo o conhecimento adquirido nesta aula! Lembrando que a sua tarefa aqui é escrever na linguagem C um programa que calcule a média entre dois valores de entrada digitados pelo usuário, e exiba o resultado com duas casas após a vírgula.

1. O primeiro passo é analisar o problema e identificar quais serão as variáveis de entrada e seus respectivos tipos: serão dois números em ponto flutuante, portanto teremos `float num1, num2;`.
2. Em seguida, pensamos no processamento necessário para ler dois valores digitados e calcular a média. A leitura dos dados poderá ser feita com o `scanf()`, e o cálculo da média por meio de uma expressão matemática simples: `media = (num1 + num2)/2` (precisaremos de uma variável do tipo `float` para armazenar o resultado desta operação).
3. Com relação à saída, podemos utilizar o `printf()` para exibir o resultado da variável `media`.
4. Como vamos utilizar `printf()` e `scanf()`, não podemos nos esquecer de incluir a biblioteca `stdio.h`!

Sendo assim, segue o algoritmo em C:

```c
#include <stdio.h>
int main(){
    float num1, num2, media;
    printf("Digite o primeiro numero: ");
    scanf("%f", &num1);
    printf("Digite o segundo numero: ");
    scanf("%f", &num2);
    media = (num1 + num2)/2;
    printf("Media = %.2f", media);
    return 0;
}
```

---

## Saiba mais

Para entender melhor o conceito de uma linguagem de programação e a estrutura fundamental da linguagem C, sugerimos a leitura do **Capítulo 1 - Introdução** do livro *Linguagem C: Completa e Descomplicada*, disponível na Biblioteca Virtual.

> BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 1, p. 2-24.

Com relação aos conceitos de variáveis, entrada e saída em C, o **Capítulo 2 - Lendo e escrevendo nas variáveis**, do mesmo livro, complementa bem o assunto.

> BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 2, p. 25-47.

Para auxiliar no desenvolvimento de programas na linguagem C, uma ótima prática é verificar a documentação da linguagem para entender em detalhes os principais tipos de funções e elementos utilizados. Para isso, sugerimos a consulta da seguinte documentação sempre que achar necessário. Nela você encontra todas as bibliotecas utilizadas na linguagem e como utilizar suas principais funções: **Referência da Linguagem C**.

---

## Referências

- BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023.
- CORMEN, T. H. **Desmistificando algoritmos**. 1. ed. Rio de Janeiro: Elsevier, 2014.
- DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023.
- MENÉNDEZ, A. **Simplificando algoritmos**. 1. ed. Rio de Janeiro: LTC, 2023.
- PIVA JUNIOR, D. **Algoritmos e programação de computadores**. 2. ed. Rio de Janeiro: Elsevier, 2019.
