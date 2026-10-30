# Aula 2 — Matrizes

## Ponto de Partida

Olá! Nesta aula vamos introduzir uma segunda estrutura muito importante e amplamente utilizada: as **matrizes**!

> A instituição de ensino que você trabalha solicitou que você desenvolva um sistema de gerenciamento de notas melhorado. O sistema deve ser capaz de armazenar as notas dos alunos em diferentes disciplinas e calcular a **média das notas de cada aluno** em cada disciplina, além de calcular a **média geral** de cada aluno em todas as disciplinas. Antes, esse controle era feito por meio de uma tabela manual, mas não era muito prático. Sendo assim, qual estrutura você poderá utilizar para resolver esta tarefa?

Agora vamos lá, preste muita atenção e tenha um excelente estudo!

---

## Vamos Começar!

### Motivação e definição

Considere a Tabela 1 que exibe dados fictícios relacionados às temperaturas máximas e mínimas da cidade de São Paulo durante 5 dias. Essa tabela representa uma estrutura de dados matricial com 5 linhas e 2 colunas. Se desejarmos criar um programa que calcule a média dessas temperaturas, seria necessário armazenar esses valores em uma **variável composta bidimensional**, também conhecida como **matriz**.

| Temperatura mínima | Temperatura máxima |
|:---:|:---:|
| 14º | 25º |
| 12º | 24º |
| 15º | 27º |
| 17º | 29º |
| 18º | 30º |

*Tabela 1 | Temperaturas máximas e mínimas de 5 dias em São Paulo.*

Perceba que neste exemplo, poderíamos facilmente criar dois vetores, um para as mínimas e outro para as máximas. Mas da mesma forma que vimos não ser tão interessante criar várias variáveis do mesmo tipo para armazenar um conjunto de valores homogêneos, neste caso também não seria o mais ideal criar vários vetores. Portanto, podemos criar uma matriz, que nada mais é do que **um conjunto de vetores** — assim como um vetor é um conjunto de variáveis primitivas.

Em resumo, cada linha de uma matriz é considerada um vetor de $n$ números, e a matriz é um vetor de $m$ vetores-linha, formando assim uma matriz $m \times n$ ($m$ linhas, $n$ colunas). Veja o exemplo na Tabela 2.

| | Coluna 0 | Coluna 1 | ... | Coluna n-1 |
|---|---|---|---|---|
| **Linha 0** | `M[0][0]` | `M[0][1]` | ... | `M[0][n-1]` |
| **Linha 1** | `M[1][0]` | `M[1][1]` | ... | `M[1][n-1]` |
| **Linha 2** | `M[2][0]` | `M[2][1]` | ... | `M[2][n-1]` |
| ... | ... | ... | ... | ... |
| **Linha m-1** | `M[m-1][0]` | `M[m-1][1]` | ... | `M[m-1][n-1]` |

*Tabela 2 | Exemplo da estrutura de uma matriz.*

> **Nota de revisão:** no original, a tabela usava `M[m][n]` como último elemento e trazia `M[0][0]` na posição de `M[2][1]` (erro de digitação). Como os índices em C começam em zero, uma matriz $m \times n$ vai de `M[0][0]` até `M[m-1][n-1]` — a tabela acima já está corrigida.

### Inicialização e utilização

Para criar uma matriz em C, a sintaxe utilizada é a seguinte:

```c
<tipo> <nome_da_matriz>[linhas][colunas];
```

E aqui estão alguns exemplos de declaração de matrizes. Na primeira linha, uma estrutura com 3 linhas e 2 colunas é criada. Na segunda linha, temos a criação da estrutura correspondente à Tabela 1, com 5 linhas e 2 colunas. Por fim, na terceira linha vemos uma matriz de 3 linhas e 2 colunas sendo criada e inicializada. Perceba que colocamos os valores em subconjuntos entre chaves, em que cada um representa uma linha da matriz.

```c
int coordenadas[3][2];
float temperaturas[5][2];
int valores[3][2] = {{2, 3}, {5, 7}, {9, 11}};
```

Para manipular matrizes bidimensionais, é necessário especificar dois índices, na qual a atribuição de valores é feita da seguinte forma:

```c
matriz[M][N] = valor;
```

Aqui, `M` representa a **linha** na qual o valor será armazenado e `N` representa a **coluna**. Assim como nos vetores, os índices de uma matriz em C sempre começam a partir de zero.

Vamos declarar uma matriz em C para armazenar as notas do primeiro e segundo bimestre de três alunos. No Quadro 1, na linha 3, declaramos uma matriz denominada `notas` com 3 linhas e 2 colunas, o que implica no armazenamento de 6 valores no total (produto das linhas pelo número de colunas). Nas linhas 5 e 6, são armazenadas as notas do primeiro aluno. É importante notar que as linhas (primeiro índice) permanecem fixas, enquanto as colunas (segundo índice) são alteradas para registrar as notas dos respectivos alunos. Este procedimento é repetido para o segundo e terceiro aluno, que são armazenados na segunda e terceira linha da matriz, respectivamente.

```c
#include <stdio.h>
int main(){
    float notas[3][2];
    //aluno 1
    notas[0][0] = 9.5;
    notas[0][1] = 10;
    //aluno 2
    notas[1][0] = 4.5;
    notas[1][1] = 6.2;
    //aluno 3
    notas[2][0] = 7;
    notas[2][1] = 8.5;
    return 0;
}
```

*Quadro 1 | Exemplo de matriz em C.*

A Figura 1 representa a estrutura de dados que é criada na memória para o código apresentado no Quadro 1. É possível observar que as linhas foram utilizadas para representar os diferentes alunos, enquanto as colunas foram utilizadas para armazenar as notas referentes aos bimestres.

| `notas` | `[0]` — 1º bimestre | `[1]` — 2º bimestre |
|---|:---:|:---:|
| **`[0]`** — aluno 1 | 9.5 | 10 |
| **`[1]`** — aluno 2 | 4.5 | 6.2 |
| **`[2]`** — aluno 3 | 7 | 8.5 |

*Figura 1 | Estrutura matricial do exemplo do Quadro 1. (A imagem original não foi preservada na extração; a tabela acima reproduz a mesma estrutura.)*

> **Nota de revisão:** no original, a última atribuição era `notas[2][1] = 8,5;` — com vírgula, o operador vírgula atribui `8` e descarta o `5`. Corrigido para `8.5`.

Para armazenar valores inseridos pelo usuário em uma matriz, usamos a função `scanf()`, indicando os dois índices que selecionam a posição na qual desejamos armazenar o valor. Da mesma forma, para imprimir valores, também utilizamos os dois índices para especificar a posição do elemento a ser impresso. Segue um exemplo prático:

```c
printf("Digite uma nota: ");
scanf("%f", &nota[1][0]);
printf("Nota digitada: %.2f", nota[1][0]);
```

Neste exemplo, a nota inserida pelo usuário será armazenada na linha 1, coluna 0 da matriz. Posteriormente, o valor armazenado nessa posição será exibido na tela com duas casas decimais, conforme especificado no comando da linha 3.

E ainda com base no Quadro 1, como poderíamos deixar a inserção de dados a cargo do usuário e de forma otimizada? Simples! Utilizando **dois laços de repetição `for` aninhados**, um para percorrer as linhas e outro para percorrer as colunas em cada uma das linhas. Veja o exemplo no Quadro 2.

```c
#include <stdio.h>
int main(){
    float notas[3][2];
    for (int i=0; i<3; i++) {
        for (int j=0; j<2; j++) {
            printf("digite a nota %d do aluno %d:", j+1,i+1);
            scanf("%f", &notas[i][j]);
        }
    }
    return 0;
}
```

*Quadro 2 | Exemplo utilizando laços `for` aninhados para ler dados em uma matriz.*

---

## Siga em Frente...

### Operações com Matrizes

Neste momento vamos abordar alguns exemplos de utilização de matrizes para reforçar o conteúdo aprendido até aqui! Vamos lá?

#### Soma das diagonais

Primeiramente, vamos aprender a manipular os índices de uma matriz dentro de laços `for` aninhados. Para isso, considere o seguinte exemplo: ler uma matriz quadrada 3x3 e retornar a soma dos elementos de sua diagonal principal e diagonal secundária. O Quadro 3 apresenta o algoritmo que resolve este problema.

```c
#include <stdio.h>
int main(){
    int matriz[3][3];
    int i, j, sDiagPrinc = 0, sDiagSec = 0;
    // Leitura da matriz
    printf("Digite os elementos da matriz 3x3:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            scanf("%d", &matriz[i][j]);
        }
    }
    // Cálculo da soma da diagonal principal e secundária
    for (i = 0, j = 2; i < 3, j >=0; i++, j--) {
        sDiagPrinc += matriz[i][i];
        sDiagSec += matriz[i][j];
    }
    printf("Soma dos elementos da diagonal principal: %d\n", sDiagPrinc);
    printf("Soma dos elementos da diagonal secundaria: %d\n", sDiagSec);
    return 0;
}
```

*Quadro 3 | Exemplo com matrizes.*

> **Nota de revisão:** no material original, as aspas dos `printf`/`scanf` deste quadro vieram corrompidas (ex.: `printf“"...\”")`, `scanf“"%”"`) e a variável estava declarada como `I` maiúsculo; o código acima foi reconstruído. Repare também que a condição `i < 3, j >= 0` usa o operador vírgula (só `j >= 0` é considerado — ver Aula 3 da Unidade 2); aqui funciona porque as duas condições ficam falsas juntas, mas o correto seria `&&`.

O primeiro conjunto de laços `for` é responsável por ler os elementos da matriz, percorrendo todos os elementos, em que `i` faz a indexação das linhas, e `j` das colunas. Já o segundo laço `for` é responsável por calcular a soma das diagonais.

- A **diagonal principal** de uma matriz é aquela cujo índice da linha é igual ao índice da coluna, portanto somamos os elementos da matriz que possuem o mesmo valor de índice (`matriz[i][i]`).
- A **diagonal secundária** seriam os seguintes elementos: `matriz[0][2]`, `matriz[1][1]` e `matriz[2][0]`. Perceba que enquanto o índice de linhas aumenta de um em um, o índice de colunas diminui de um em um. Então uma possível solução seriam duas variáveis de controle dentro de um mesmo `for`, uma para linha e outra para coluna, conforme vemos no Quadro 3.

#### Multiplicação de matrizes

Outro exemplo clássico é relacionado à **multiplicação de matrizes**. Veja no Quadro 4 um programa em C que lê duas matrizes e suas respectivas dimensões, verifica se a multiplicação entre elas é possível e, se for o caso, calcula e exibe o produto das matrizes.

$$C_{ij} = \sum_{k=0}^{n-1} A_{ik} \cdot B_{kj} \qquad (A_{m \times n} \cdot B_{n \times q} = C_{m \times q})$$

```c
#include <stdio.h>
int main() {
    int m, n, p, q, i, j, k;
    int soma = 0;

    printf("Digite as dimensões da primeira matriz (m x n): ");
    scanf("%d %d", &m, &n);
    printf("Digite as dimensões da segunda matriz (p x q): ");
    scanf("%d %d", &p, &q);

    // Verificação se a multiplicação é possível
    if (n != p) {
        printf("A multiplicação entre as matrizes não é possível.\n");
        return 0;
    }

    // Declaração e entrada dos elementos das matrizes
    int matriz1[m][n], matriz2[p][q], resultado[m][q];
    printf("Digite os elementos da primeira matriz:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matriz1[i][j]);
        }
    }
    printf("Digite os elementos da segunda matriz:\n");
    for (i = 0; i < p; i++) {
        for (j = 0; j < q; j++) {
            scanf("%d", &matriz2[i][j]);
        }
    }

    // Cálculo do produto das matrizes
    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {
            for (k = 0; k < p; k++) {
                soma += matriz1[i][k] * matriz2[k][j];
            }
            resultado[i][j] = soma;
            soma = 0;
        }
    }

    printf("O produto das matrizes é:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {
            printf("%d\t", resultado[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

*Quadro 4 | Multiplicação de matrizes.*

> 💡 As matrizes `matriz1[m][n]` etc. são declaradas com tamanhos lidos em tempo de execução — são **VLAs** (*variable length arrays*), recurso do C99. Isso não contradiz a ideia de vetor "estático" da aula anterior: depois de criada, a matriz não muda de tamanho.

---

## Vamos Exercitar?

Prezado estudante, é hora de aplicar todo o conhecimento adquirido até aqui! Para desenvolver o sistema de gerenciamento de notas, podemos usar matrizes para armazenar os dados das notas dos alunos por disciplina e realizar os cálculos necessários. Nesta lógica, **cada linha da matriz representa um aluno, e as colunas as respectivas disciplinas**. Veja no Quadro 5 uma das possíveis soluções:

```c
#include <stdio.h>
#define NUM_ALUNOS 3
#define NUM_DISCIPLINAS 3

int main(){
    float notas[NUM_ALUNOS][NUM_DISCIPLINAS] = {{7.5, 8.0, 9.0}, {6.5, 7.0, 8.0}, {8.0, 7.5, 8.5}};
    float mediasAluno[NUM_ALUNOS];
    float mediaGeral, soma = 0;

    // Calcula a média das notas de cada aluno em cada disciplina
    for (int i = 0; i < NUM_ALUNOS; i++) {
        float soma = 0;
        for (int j = 0; j < NUM_DISCIPLINAS; j++) {
            soma += notas[i][j];
        }
        mediasAluno[i] = soma / NUM_DISCIPLINAS;
    }

    // Calcula a média geral de cada aluno em todas as disciplinas
    for (int i = 0; i < NUM_ALUNOS; i++) {
        soma += mediasAluno[i];
    }
    mediaGeral = soma / NUM_ALUNOS;

    // Imprime as médias de cada aluno em cada disciplina
    for (int i = 0; i < NUM_ALUNOS; i++) {
        printf("Média do aluno %d: %.2f\n", i + 1, mediasAluno[i]);
    }
    // Imprime a média geral de todos os alunos
    printf("Média geral de todos os alunos: %.2f\n", mediaGeral);

    return 0;
}
```

*Quadro 5 | Código de resolução.*

> 💡 Repare que existem **duas** variáveis chamadas `soma`: a declarada dentro do primeiro `for` *sombreia* (esconde) a de fora durante aquele laço. Por isso a `soma` externa ainda vale 0 quando o segundo `for` começa.

Nesta solução utilizamos uma diretiva chamada **`#define`**. Em C, ela é usada para criar **constantes simbólicas**. Ela é uma construção do pré-processador e não uma função da linguagem em si. Com ela, você pode fornecer um nome a um valor constante antes de o programa ser compilado. Ela substitui todas as ocorrências desse nome no código pelo valor constante especificado. No caso desta solução, a linha `#define NUM_ALUNOS 3` cria uma constante simbólica `NUM_ALUNOS` com o valor 3. Em todo o programa, sempre que `NUM_ALUNOS` é usado, ele será substituído por 3 durante a fase de pré-processamento. Isso torna o código mais legível e facilita a manutenção, uma vez que você pode ajustar o valor da constante em um único local, se necessário, em vez de ter que alterar cada ocorrência do valor diretamente.

> Lembrando que não há uma única resposta correta. Há vários caminhos para se chegar no mesmo resultado! Modifique e tente otimizar ao máximo os seus programas.

---

## Saiba mais

Para entender melhor o conceito de matrizes em C, sugerimos a leitura do **Capítulo 6 - Vetores**, do livro *Linguagem C*, disponível na Biblioteca Virtual.

> DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 6, p. 129-151.

Também sugerimos a leitura do **Capítulo 6 - Vetores e matrizes - arrays**, do livro *Linguagem C: Completa e Descomplicada*, disponível na Biblioteca Virtual, para complementar os estudos sobre matrizes em C.

> BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 6, p. 109-129.

Para auxiliar no desenvolvimento de programas na linguagem C, uma ótima prática é verificar a documentação da linguagem para entender em detalhes os principais tipos de funções e elementos utilizados. Para isso, sugerimos a consulta da seguinte documentação sempre que achar necessário. Nela você encontra todas as bibliotecas utilizadas na linguagem e como utilizar suas principais funções: **Referência da Linguagem C**.

---

## Referências

- BACKES, André. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 4, p. 67-87.
- DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 3, p. 51-79.
- PIVA JUNIOR, D. **Algoritmos e programação de computadores**. 2. ed. Rio de Janeiro: Elsevier, 2019.
