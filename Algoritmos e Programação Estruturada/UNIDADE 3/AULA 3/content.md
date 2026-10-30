# Aula 3 — Structs

## Ponto de Partida

Olá! Nesta aula vamos introduzir uma forma de definir tipos de dados heterogêneos: as **structs**!

> A instituição de ensino que você trabalha possui uma biblioteca e solicitou que você desenvolva um **sistema de gestão de biblioteca**. O sistema deve ser capaz de armazenar informações sobre vários livros, incluindo título, autor, ISBN, ano de publicação e quantidade disponível em estoque. Além disso, o sistema deve permitir a busca de livros por autor, verificação de disponibilidade e atualização do estoque.
>
> Nesse cenário, como você poderá realizar a estruturação dos dados?

Nesta aula vamos aprender formas de facilitar esta tarefa para que se torne realidade com muita facilidade! Preste muita atenção e tenha um excelente estudo!

---

## Vamos Começar!

### Definição e criação de structs

Já conhecemos a maneira de aprimorar a eficiência no uso de variáveis ao usar estruturas compostas, como vetores e matrizes. No entanto, essas estruturas só podem armazenar valores do mesmo tipo. Além dessas estruturas homogêneas, as linguagens de programação oferecem **estruturas compostas heterogêneas**, conhecidas como **"structs"**, ou **registros**.

Assim como associamos vetores e matrizes a tabelas, podemos associar uma estrutura a um **formulário de cadastro com vários campos**. Por exemplo, o cadastro de um cliente pode ser realizado inserindo o nome, a idade, o CPF e o endereço em uma struct.

Na linguagem C, a criação de uma estrutura deve ser feita antes da função `main()` e deve seguir a seguinte sintaxe:

```c
struct <nome> {
    <tipo> <nome_da_variavel1>;
    <tipo> <nome_da_variavel2>;
    ...
};
```

Aqui, `<nome>` é o nome da estrutura, como cliente, carro, fornecedor etc., e as variáveis internas são os **campos** nos quais desejamos armazenar informações dessa estrutura. Na prática, uma estrutura funciona como um "tipo de dado" e seu uso sempre será atribuído a uma ou mais variáveis. Veja a seguir um exemplo de criação de uma struct em C:

```c
struct Cadastro {
    char cpf[11];
    char nome[30];
    int idade;
    char rua[50];
    int numero;
};
```

Observe que os elementos que compõem a estrutura são definidos de maneira semelhante às variáveis (sejam elas variáveis simples ou compostas). Tal como na declaração de variáveis, os nomes das variáveis (**membros**) de uma estrutura devem ser únicos entre si. No entanto, diferentes estruturas podem ter membros com identificadores idênticos.

Após a definição da estrutura, nós podemos utilizá-la como um novo tipo de dado no programa principal, declarando variáveis do tipo da estrutura definida, conforme o trecho a seguir:

```c
struct Cadastro cliente1;
```

No trecho acima, a variável `cliente1` é do tipo `Cadastro`, portanto, ela possui dentro dela todos os membros de cadastro, como `cpf`, `nome`, `idade`, `rua` e `numero`, por exemplo. Perceba que, por `Cadastro` ser um tipo definido pelo programador, você precisa usar a palavra `struct` antes do tipo da nova variável criada.

Por fim, veja no trecho de código logo a seguir que também podemos definir variáveis após a definição da estrutura. Isso pode ser feito colocando os nomes das variáveis após o fechamento das chaves (`}`) da estrutura e antes do ponto e vírgula (`;`).

```c
struct Cadastro {
    char cpf[11];
    char nome[30];
    int idade;
    char rua[50];
    int numero;
} cliente1, cliente2;
```

> **Nota de revisão:** o texto original se referia à variável como "pessoa1", mas o código declara `cliente1`; o texto foi ajustado. Observe também que `char cpf[11]` só comporta 10 dígitos + `'\0'` — para guardar os 11 dígitos de um CPF como string, use `char cpf[12]` (mesmo problema discutido na Aula 1 desta unidade).

### Manipulação de dados em structs

Após a criação de uma struct e definição de uma variável do tipo de estrutura, podemos acessar seus campos (ou variáveis) utilizando o **operador `.` (ponto)**. Este operador é empregado para referenciar os campos da estrutura pertencentes à variável declarada. Veja no Quadro 1 um exemplo de utilização de structs em C que ilustra como os campos da estrutura `Aluno` podem ser facilmente acessados.

```c
#include <stdio.h>
#include <string.h>

struct Aluno {
    int numMat;
    char nome[30];
    char sexo;
    int idade;
};

int main(){
    struct Aluno aluno1;

    // Inserindo dados no aluno1
    aluno1.numMat = 1000;
    strcpy(aluno1.nome, "Joao");
    aluno1.sexo = 'M';
    aluno1.idade = 19;

    // Imprimindo os dados do aluno1
    printf("Número de matrícula: %d\n", aluno1.numMat);
    printf("Nome: %s\n", aluno1.nome);
    printf("Sexo: %c\n", aluno1.sexo);
    printf("Idade: %d\n", aluno1.idade);

    return 0;
}
```

*Quadro 1 | Exemplo de struct em C.*

Note que o campo `nome` é um vetor de caracteres, portanto, é uma string. Em C, temos a biblioteca `string.h` que possui diversas funções para manipulação de strings. Neste código utilizamos a função `strcpy`, que copia o valor do segundo parâmetro (`"Joao"`) para o primeiro (`aluno1.nome`).

> 💡 Por que não `aluno1.nome = "Joao";`? Em C, vetores **não podem ser atribuídos** com `=` depois de declarados — é preciso copiar caractere a caractere, que é o que `strcpy` faz.

Caso se faça necessário ler uma entrada de dados do usuário, basta usar o `scanf` normalmente como fazemos com variáveis comuns, e de forma independente para cada variável da estrutura, respeitando o tipo de cada uma para o código de controle. Veja o trecho de código a seguir que lê os valores para os campos `numMat` e `nome` da variável `aluno1`.

```c
scanf("%d", &aluno1.numMat);
fgets(aluno1.nome, 30, stdin);
```

> **Nota de revisão:** no original, a segunda linha era `fgets(aluno1.numMat, 30, stdin);` — mas `numMat` é `int`, e o texto diz que a linha lê o campo `nome`. Corrigido para `aluno1.nome`.

Uma outra maneira de atribuir valores a uma variável de estrutura é inicializando-a diretamente em sua declaração. Para isso, ao declarar a variável do tipo da estrutura, podemos definir uma lista de valores separados por vírgula e delimitados pelo operador de chaves (`{ }`). Devemos prestar atenção na **ordem**, pois o primeiro valor da inicialização será atribuído ao primeiro membro da estrutura (`numMat`), e assim por diante. Por exemplo:

```c
struct Aluno aluno2 = { 2000, "Maria", 'F', 18 };
```

Ainda, elementos não mencionados durante a inicialização são definidos como 0 (ou como uma string vazia `""`, no caso de strings). No exemplo a seguir o campo `sexo` é inicializado com o caractere nulo (`'\0'`) e `idade` com zero.

```c
struct Aluno aluno2 = { 2000, "Maria" };
```

---

## Siga em Frente...

### Uso de structs em algoritmos

Imagine agora que você precise trabalhar com dados de cinco alunos, conforme a estrutura `Aluno` já definida anteriormente. A princípio, poderíamos criar cinco variáveis do tipo aluno, como:

```c
struct Aluno a1, a2, a3, a4, a5;
```

Mas isso não é muito prático. Sendo assim, a representação desses cinco registros pode ser ainda mais simplificada se usarmos o conceito de vetores:

```c
struct Aluno alunos[5];
```

Dessa forma, é criado um **vetor de estruturas**, em que cada posição do vetor é uma estrutura do tipo `Aluno`. A declaração de um vetor de estruturas se assemelha à declaração de um vetor de um tipo básico.

Quando temos um vetor de estruturas, acessamos cada uma e seus membros da seguinte forma:

```c
alunos[0].idade;
alunos[1].idade;
alunos[2].idade;
```

Veja que o operador de ponto (`.`) vem **depois** dos colchetes (`[ ]`) do índice do vetor. É importante manter a ordem estabelecida, já que o índice do vetor indica a posição específica que desejamos acessar, na qual cada posição é representada por uma estrutura. Somente após a definição das estruturas contidas no vetor é que podemos acessar os campos correspondentes.

### `typedef`

Em C, a palavra-chave **`typedef`** é usada para criar um novo nome para um tipo existente. Isso pode tornar a declaração de tipos complexos mais legível e facilitar a manutenção do código. Usar `typedef` não cria um novo tipo, apenas cria um novo nome para um tipo existente. Veja a sintaxe a seguir:

```c
typedef <tipo_de_dado_existente> <novo_nome_do_tipo>;
```

Na sintaxe, o campo `tipo_de_dado_existente` pode ser qualquer tipo, desde `int` até tipos definidos pelo usuário com structs.

Em structs o `typedef` pode ser utilizado para eliminar o uso da palavra `struct` antes da declaração de uma variável do tipo definido pela estrutura. Por exemplo:

```c
typedef struct {
    char nome[20];
    int idade;
} Aluno;
```

No trecho anterior temos uma definição de estrutura, em que ela será referenciada no programa principal apenas como `Aluno`.

```c
Aluno aluno1;
```

Em termos de significado, não há nenhuma mudança, sendo apenas uma simplificação.

| Sem `typedef` | Com `typedef` |
|---|---|
| `struct Aluno { ... };` | `typedef struct { ... } Aluno;` |
| `struct Aluno aluno1;` | `Aluno aluno1;` |

---

## Vamos Exercitar?

Prezado estudante, é hora de aplicar todo o conhecimento adquirido até aqui! Lembre-se que você precisa desenvolver um sistema capaz de armazenar informações sobre vários livros, além de permitir a busca de livros por autor, verificação de disponibilidade e atualização do estoque.

Para resolver esta tarefa, vamos criar uma estrutura `Livro`, contendo os atributos título, autor, ISBN, ano de publicação e quantidade disponível em estoque. Em seguida, no programa principal vamos instanciar um vetor desta estrutura de acordo com o número de livros que a escola possui em estoque. Veja no Quadro 2 uma das possíveis soluções:

```c
#include <stdio.h>
#include <string.h>
#define NUM_LIVROS 3

typedef struct{
    char titulo[100];
    char autor[50];
    char ISBN[13];
    int anoPublicacao;
    int estoque;
} Livro;

int main() {
    Livro livros[NUM_LIVROS] = {
        {"Memórias de um Futuro Esquecido", "Martelo de Assis", "1231231231239", 1899, 10},
        {"O Silêncio dos Inocentes Gritando", "Franz Kafta", "4564564564569", 1915, 5},
        {"A Menina que Roubava Livros e os Devolvia com Juros", "Dan Brownie", "7897897897899", 1949, 8}
    };

    // Realizar uma busca por autor
    char autorProcurado[50];
    fflush(stdin); // limpa o buffer de leitura
    printf("Digite o nome do autor para procurar livros: ");
    fgets(autorProcurado, 50, stdin);
    autorProcurado[strcspn (autorProcurado, "\n")] = 0; // remove o \n ao final da string
    printf("Livros por %s:\n", autorProcurado);
    for (int i = 0; i < NUM_LIVROS; i++) {
        if (strcmp(livros[i].autor, autorProcurado) == 0) {
            printf("Título: %s\n", livros[i].titulo);
            printf("ISBN: %s\n", livros[i].ISBN);
            printf("Ano de Publicação: %d\n", livros[i].anoPublicacao);
            printf("Estoque Disponível: %d\n", livros[i].estoque);
            printf("\n");
        }
    }

    // Verificar disponibilidade de um livro
    char ISBNProcurado[13];
    fflush(stdin);
    printf("Digite o ISBN do livro para verificar a disponibilidade: ");
    fgets(ISBNProcurado, 13, stdin);
    ISBNProcurado[strcspn (ISBNProcurado, "\n")] = 0; // remove o \n ao final da string
    for (int i = 0; i < NUM_LIVROS; i++) {
        if (strcmp(livros[i].ISBN, ISBNProcurado) == 0) {
            printf("O livro %s está disponível em estoque: %d\n", livros[i].titulo, livros[i].estoque);
            break;
        }
    }
    return 0;
}
```

*Quadro 2 | Código de resolução.*

Nesta solução inicializamos o vetor `livros` diretamente em sua declaração. Veja que cada elemento `Livro` do vetor `livros` é colocado como uma lista entre chaves (`{}`), dentro de outro grupo externo de chaves. Outro detalhe importante é a linha com `strcspn`, em que utilizamos essa função para remover a quebra de linha (`\n`) que é inserida em uma string sempre que usamos uma leitura com o `fgets`. Se este `\n` permanecer na string, a comparação com o `strcmp` não funcionaria, pois a string original no vetor `livros` não possui esta quebra de linha ao final.

| Função (`string.h`) | O que faz |
|---|---|
| `strcpy(dest, orig)` | copia a string `orig` para `dest`. |
| `strcmp(s1, s2)` | compara duas strings; retorna `0` se forem iguais. |
| `strcspn(s, conj)` | retorna o comprimento do segmento inicial de `s` que **não** contém nenhum caractere de `conj` — ou seja, o índice do primeiro `\n` no exemplo. |

> **Nota de revisão:** o ISBN tem 13 dígitos, mas os campos `ISBN[13]` e `ISBNProcurado[13]` não reservam espaço para o `'\0'`:
> - `"1231231231239"` cabe exatamente em `char[13]` **sem** terminador, então `strcmp`/`printf("%s")` sobre `livros[i].ISBN` leem além do campo;
> - `fgets(ISBNProcurado, 13, stdin)` lê no máximo **12** caracteres, então um ISBN de 13 dígitos nunca vai ser encontrado.
>
> A correção é declarar os dois com tamanho **14** (e, no `fgets`, usar 14 ou `sizeof ISBNProcurado`).

> Lembre-se de que não há uma única resposta correta, e ainda é possível otimizar este código! Que tal colocar as opções de pesquisa por autor e ISBN dentro de um `switch-case`, criando assim um menu de seleção? Ainda, você pode incluir outra opção neste menu para possibilitar a alteração dos dados dos livros ou ainda a inclusão de novos livros. Aceita o desafio?

---

## Saiba mais

Para entender melhor o conceito de estruturas em C, sugerimos a leitura do **Capítulo 11 - Estruturas**, do livro *Linguagem C*, disponível na Biblioteca Virtual.

> DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 11, p. 266-281.

Também sugerimos a leitura do **Capítulo 8 - Tipos definidos pelo programador**, do livro *Linguagem C: Completa e Descomplicada*, disponível na Biblioteca Virtual, para complementar os estudos sobre estruturas em C, além de aprender sobre enumerações (`enum`) e uniões (`union`).

> BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 8, p. 140-157.

Para auxiliar no desenvolvimento de programas na linguagem C, uma ótima prática é verificar a documentação da linguagem para entender em detalhes os principais tipos de funções e elementos utilizados. Para isso, sugerimos a consulta da seguinte documentação sempre que achar necessário. Nela, você encontra todas as bibliotecas utilizadas na linguagem e como utilizar suas principais funções: **Referência da Linguagem C**.

---

## Referências

- BACKES, A. **Linguagem C**: completa e descomplicada. 2. ed. Rio de Janeiro: LTC, 2023. cap. 4, p. 67-87.
- DAMAS, L. **Linguagem C**. 10. ed. Rio de Janeiro: LTC, 2023. cap. 3, p. 51-79.
- PIVA JUNIOR, D. **Algoritmos e programação de computadores**. 2. ed. Rio de Janeiro: Elsevier, 2019.
