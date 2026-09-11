# Exercícios de Revisão — Unidade 1

## Questão 1 ✅

Explorando funções em Python para compreender as funções "built-in" que estão disponíveis na linguagem. Funções "built-in" são funções pré-definidas que fazem parte da biblioteca padrão do Python.

**Pergunta:** O que são funções "built-in" em Python?

**Resposta assinalada:** Funções que fazem parte da biblioteca padrão de Python e estão prontas para uso. ✅

**Comentário:**
- A) Funções "built-in" não precisam ser definidas pelo usuário; elas já estão disponíveis na linguagem.
- B) Funções "built-in" não são utilizadas exclusivamente por desenvolvedores experientes; elas são amplamente utilizadas por todos os níveis de desenvolvedores.
- **C) Funções "built-in" em Python são funções que fazem parte da biblioteca padrão da linguagem e estão prontas para uso, sem a necessidade de definição adicional. *(CORRETA)***
- D) Funções "built-in" não são criadas apenas para fins de depuração; elas têm várias finalidades e são usadas em programas Python reais.
- E) Funções "built-in" são suportadas pela linguagem Python e fazem parte de sua funcionalidade.

## Questão 2 ✅

Você está desenvolvendo um programa em Python que requer a leitura de números de um arquivo e a impressão dos números pares encontrados.

**Pergunta:** Qual estrutura de repetição é mais apropriada para ler os números de um arquivo linha por linha e imprimir apenas os números pares?

**Resposta assinalada:** `for` ✅

**Comentário:**
- A) "if-else" é uma estrutura condicional, não uma estrutura de repetição.
- **B) A estrutura de repetição "for" é mais apropriada para percorrer os elementos de um arquivo, linha por linha, e realizar a tarefa desejada, como a impressão dos números pares. *(CORRETA)***
- C) "while" é uma estrutura de repetição adequada, mas geralmente requer mais código para realizar a leitura de um arquivo linha por linha em comparação com "for".
- D) "def" é usada para definir funções personalizadas, não para percorrer arquivos.
- E) "try-except" é usado para tratamento de exceções, não para percorrer arquivos e imprimir números pares.

## Questão 3 ✅

Observe o código:

```python
def encontrar_maior_numero(lista_numeros):
    maior = max(lista_numeros)
    return maior

numeros = [56, 72, 89, 45, 62]
maior_numero = encontrar_maior_numero(numeros)
```

**Pergunta:** Com base no código fornecido, qual é a finalidade da função `encontrar_maior_numero`?

**Resposta assinalada:** A função `encontrar_maior_numero` encontra o maior número na lista. ✅

**Comentário:**
- A) Essa alternativa é incorreta; a função encontra o maior número (MAX), não a média (AVG).
- B) Essa alternativa é incorreta; a função encontra o maior número (MAX), não o menor (MIN).
- **C) Essa alternativa descreve corretamente a finalidade da função. *(CORRETA)***
- D) Essa alternativa é incorreta; a função não verifica se a lista está vazia.
- E) Essa alternativa é incorreta; a função encontra o maior número, não calcula média ponderada.

## Questão 4 ✅

Em Python as finalidades das funções anônimas, também conhecidas como "lambda", são extremamente importante para aplicações de funções de forma pontual.

**Pergunta:** O que são funções anônimas em Python?

**Resposta assinalada:** Funções que não têm um corpo definido. ✅

**Comentário:**
- A) Funções anônimas têm um nome implícito e podem ser chamadas.
- B) Funções anônimas podem ser chamadas várias vezes, assim como funções nomeadas.
- C) Funções anônimas podem ter parâmetros, embora sejam frequentemente usadas com um único parâmetro.
- **D) Funções anônimas em Python, também conhecidas como "lambda," são funções que não têm um corpo definido explicitamente. Elas são usadas para criar funções pequenas e simples de forma concisa.**
- E) Funções anônimas podem ser usadas por desenvolvedores de todos os níveis, não apenas por desenvolvedores experientes.

## Questão 5 ✅

Imagine que você é um desenvolvedor de software e está trabalhando em um projeto de gerenciamento de tarefas. Seu objetivo é criar um aplicativo que ajude as pessoas a organizar suas atividades diárias, definir prazos e acompanhar o progresso de suas tarefas. Uma situação comum que os usuários enfrentam é a necessidade de calcular a data de vencimento de uma tarefa com base na data de início e no prazo estabelecido. Para tornar seu aplicativo ainda mais eficaz, você deseja implementar uma funcionalidade que leve em consideração os dias úteis, excluindo os fins de semana e feriados.

Suponha que um usuário do seu aplicativo esteja planejando uma tarefa que começa no dia 10 de dezembro de 2023. A tarefa tem um prazo de 7 dias úteis. Você é responsável por implementar a lógica que calculará a data de vencimento dessa tarefa, considerando os dias úteis, para que o usuário saiba exatamente quando a tarefa deve ser concluída.

**Pergunta:** Qual função built-in do Python você deve utilizar para calcular a data de vencimento dessa tarefa com precisão, levando em consideração os dias úteis?

**Resposta assinalada:** `datetime.timedelta()` ✅

**Comentário:**
- A) A função `time.sleep()` não é apropriada para calcular a data de vencimento com base em dias úteis.
- B) A função `datetime.date()` é usada para criar objetos de data, mas não considera dias úteis.
- **C) A função `datetime.timedelta()` permite a adição de um intervalo de tempo, como dias, a uma data, considerando dias úteis. É a escolha correta para calcular a data de vencimento com precisão. *(CORRETA)***
- D) Não existe uma função `calendar.calculate()` em Python.
- E) Não existe uma função `math.add()` em Python.
