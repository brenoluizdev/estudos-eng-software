# Exercícios de Revisão — Unidade 4

## Questão 1 ✅

O escopo é dividido em duas categorias, local ou global. Quando se tem variáveis que ambas são locais, elas existem e são notadas somente dentro do corpo da função onde foram definidas. Para definir uma variável global é preciso criá-la fora da função, assim ela será visível por todas as funções do programa. Nesse contexto, analise as asserções a seguir:

- **I.** A utilização de variáveis globais permite dimensionar o uso da memória.
- **II.** As funções e procedimentos têm pouca relevância em programação.
- **III.** As variáveis locais são criadas e mantidas na memória ao fim da função.
- **IV.** As variáveis globais permanecem na memória durante todo o tempo de execução.

**Pergunta:** É correto apenas o que se afirma em:

**Resposta assinalada:** I e IV, apenas. ✅

**Comentário:**

- **I. Correto.** Variáveis globais permanecem na memória durante todo o tempo de execução, permitindo um controle mais amplo sobre o uso da memória.
- **II. Incorreto.** Funções e procedimentos são fundamentais em programação para organizar o código, promover reutilização e modularidade.
- **III. Incorreto.** Variáveis locais são criadas quando a função é chamada e são desalocadas quando a função é concluída, deixando de existir na memória.
- **IV. Correto.** Variáveis globais são criadas fora de qualquer função e permanecem na memória durante toda a execução do programa.

## Questão 2 ✅

Além de retornar valores, as funções também podem receber parâmetros de "quem" a chamou. Essa técnica é muito utilizada e pode economizar na criação de variáveis ao longo da função principal. Os tipos de parâmetros que uma função/procedimento pode receber são classificados em passagem por valor e passagem por referência. Analise o código a seguir.

```c
#include<stdio.h>

void pensar(int a, int b) {
    a = 11;
    b = 12;
}
int main() {
    int a = -11;
    int b = -12;
    pensar(a, b);
    printf(" a = %d e b = %d", a, b);
    return 0;
}
```

**Pergunta:** De acordo com o código apresentado, o que será mostrado na saída do programa?

**Resposta assinalada:** `a = -11 e b = -12`. ✅

**Comentário:**

No código foi usada a técnica de **passagem de parâmetro por valor**, ou seja, serão criadas cópias das variáveis `a` e `b` para que a função trabalhe. Nesse caso, após o final da execução da função as cópias são liberadas e o valor original das variáveis não é modificado.

## Questão 3 ✅

**Pergunta:** Em linguagem C, qual é o propósito principal da passagem por referência em uma função?

**Resposta assinalada:** Possibilitar a modificação direta dos valores originais das variáveis passadas como argumento. ✅

**Comentário:**

Na passagem por referência em C, é enviado à função o **endereço de memória** das variáveis, permitindo que a função acesse e modifique diretamente os valores originais. Isso é útil quando se deseja alterar variáveis fora do escopo da função e economizar recursos, evitando a criação de cópias desnecessárias.

## Questão 4 ✅

Observe o programa que demonstra o uso de uma função na linguagem C:

```c
#include <stdio.h>
#define pi 3.1415

float raio() {
  float r, area;
  printf("Digite o raio: ");
  scanf("%f", &r);
  area = pi * r * r;
}

int main() {
  float result;
  result = raio();
  printf("Área do círculo = %.2f ", result);
  return 0;
}
```

O programa demonstrado não compila pois possui um erro!

**Pergunta:** Escolha a alternativa correta que mostra o erro do programa.

**Resposta assinalada:** O que causa o erro do programa é a falta do `return` na função `raio()`; o correto seria adicionar a seguinte linha: `return area;` isso fará com que o valor seja repassado para a variável `result`. ✅

**Comentário:**

A função `raio()` está declarada com o tipo de retorno `float`, mas não está retornando um valor. Isso é um problema, pois o tipo de retorno da função indica que ela deveria retornar um valor do tipo `float`. Se a função não retornar nenhum valor, o tipo de retorno deve ser `void`. Portanto, a correção seria declarar a função como `void raio()` ou incluir um `return` para devolver o valor calculado. As outras alternativas apresentam interpretações incorretas ou não relacionadas ao erro específico no programa fornecido.

> **Nota de revisão:** a alternativa assinalada identifica corretamente o problema, mas a premissa "não compila" não é exata: em C, uma função não-`void` sem `return` **compila** (o GCC só emite um *warning* "control reaches end of non-void function", e só com `-Wall`). O erro aparece em **tempo de execução**: usar o valor de retorno, como em `result = raio();`, é comportamento indefinido — `result` recebe lixo. Note também que a sugestão do comentário de trocar para `void raio()` não resolveria este programa, porque o `main` usa o valor retornado; a correção certa é `return area;`.

## Questão 5 ✅

A técnica de passagem de parâmetros para uma função é extremamente usada em todas as linguagens de programação. Ao chamar uma função que espera receber parâmetros, caso todos os argumentos esperados não sejam informados, será gerado um erro de compilação. Na linguagem C, para conseguirmos acessar o valor de uma variável global, dentro de uma função que possui uma variável local com mesmo nome, devemos usar a instrução `extern`. Tomando como referência o conceito apresentado, julgue as afirmativas a seguir em (V) Verdadeiras ou (F) Falsas:

- ( ) Uma função pode retornar qualquer valor válido em C, sejam de tipos pré-definidos (`int`, `char`, `float`).
- ( ) Uma função que não retorna nada é definida colocando-se o tipo `void` como valor retornado.
- ( ) Se um comando `return` é executado, o controle é passado de volta para o trecho que chamou a função.
- ( ) Se não existir um comando `return`, o controle é passado de volta para o trecho que chamou a função após o corpo da função ser executado.

**Pergunta:** Assinale a alternativa que apresenta a sequência correta.

**Resposta assinalada:** V – V – V – V ✅

**Comentário:**

- **(V)** Uma função pode retornar qualquer valor válido em C, sejam de tipos pré-definidos (`int`, `char`, `float`). Verdadeiro. Em C, uma função pode retornar valores de qualquer tipo válido.
- **(V)** Uma função que não retorna nada é definida colocando-se o tipo `void` como valor retornado. Verdadeiro. Em C, uma função que não retorna nenhum valor é definida usando `void` como tipo de retorno.
- **(V)** Se um comando `return` é executado, o controle é passado de volta para o trecho que chamou a função. Verdadeiro. A execução da função é encerrada e o controle volta ao chamador.
- **(V)** Se não existir um comando `return`, o controle é passado de volta para o trecho que chamou a função após o corpo da função ser executado. Verdadeiro. Se não houver um comando `return`, o controle é passado de volta após a execução do corpo da função (ao atingir a `}` final).
