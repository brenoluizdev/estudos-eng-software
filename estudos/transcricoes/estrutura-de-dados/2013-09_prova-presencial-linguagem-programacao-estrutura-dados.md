---
disciplina: Linguagem de Programação e Estrutura de Dados
curso: Análise e Desenvolvimento de Sistemas (ADS) — 3º semestre, noturno
instituição: UNOPAR
data_da_prova: 05/09/2013 (Prova Presencial, 1ª Chamada)
data_de_publicação: 05/09/2013
autor_publicador: usuário "Oráculo" (fórum analise-unopar.forumeiros.com)
fonte: https://analise-unopar.forumeiros.com/t342-prova-presencial-de-linguagem-de-programacao-e-estrutura-de-dados-05-09-2013
nível_de_confiança: alto (data, disciplina, curso e turno explícitos no post; instituição confirmada pela comunidade do fórum, dedicado a alunos de ADS da UNOPAR)
observação: >
  Conteúdo obtido de post público de fórum de alunos (sem necessidade de
  login). Notação de pseudocódigo (ex.: START, END, TOPO, REF) preservada como
  no original.
---

# Prova Presencial — Linguagem de Programação e Estrutura de Dados (UNOPAR, ADS, 3º semestre)

## Questões objetivas (01–10)

**Questão 1** — Definição de estrutura de dados.
a) Linguagem de programação para programas de computador
b) Conjunto de instruções que resolve um problema
c) Diferença entre aspectos estático e dinâmico
d) Elemento responsável pelo armazenamento e manipulação de dados
e) Comando e armazenamento explícito de dados

**Gabarito: D**

---

**Questão 2** — Definição de algoritmo.
a) Linguagem de programação
b) Elemento de armazenamento de dados
c) Diferença entre estático e dinâmico
d) Armazenamento de comando de dados
e) Conjunto de instruções que resolve um problema

**Gabarito: E**

---

**Questão 3** — Variável Y recebe informação do vetor V.
a) então UNDERFLOW
b) INICIO := INICIO + 1
c) se INICIO > FIM então INICIO := 0
d) senão Y := V[INICIO]
e) Nenhuma das anteriores

**Gabarito: D**

---

**Questão 4** — Modelo de registro para listas duplamente encadeadas
(definição de vetor em listas duplamente encadeadas).
*[alternativas completas não reproduzidas com clareza na fonte —
trecho parcialmente ilegível]*

**Gabarito: B**

---

**Questão 5** — Pilha X recebe elementos 1 a 5 inseridos sequencialmente.
Qual o elemento no topo?
a) 5
b) 4
c) 3
d) 2
e) 1

**Gabarito: A**

---

**Questão 6** — Identificação de função de algoritmo (FIFO/LIFO).
a) Inclusão em pilha
b) Exclusão em fila
c) Exclusão em pilha
d) Inclusão em fila
e) Nenhuma correta

**Gabarito: B**

---

**Questão 7** — Função de algoritmo de pilha (Y → V, inclusão em pilha).
a) Y → V, inclusão em pilha
b) Exclusão em fila
c) Exclusão em pilha
d) Inclusão em fila
e) Nenhuma correta

**Gabarito: A**

---

**Questão 8** — Definição da estrutura FIFO.
a) Pilha
b) Árvore
c) Lista
d) Fila
e) Lista encadeada

**Gabarito: D**

---

**Questão 9** — Definição de pilha.
a) Lista linear com inserção/remoção na extremidade do topo
b) Lista LILO
c) Lista FIFO
d) Inserção/remoção em posição aleatória
e) Inserção em uma extremidade, remoção na outra

**Gabarito: A**

---

**Questão 10** — Identificação de condição de OVERFLOW em inclusão em fila.
a) se INICIO = COMEÇO
b) se TOPO = N
c) se COMEÇO = N
d) se FIM = N
e) Nenhuma das anteriores

**Gabarito: D**

## Questões dissertativas (11–12)

**Questão 11** — Qual o significado da condição:
`SE (REF = NULO) OU (REF↑.PROX = NULO)`?

**Resposta esperada:** Estrutura vazia, ou REF não possui sucessor.

---

**Questão 12** — Comente as linhas 02, 05 e 07 do algoritmo de exclusão à
direita em lista duplamente encadeada:

- **Linha 02:** Identifica UNDERFLOW; não há elemento para excluir.
- **Linha 05:** O ponteiro REF.PROX passa a apontar para P.PROX.
- **Linha 07:** O ponteiro anterior de REF.PROX.ANT passa a apontar para REF.

---

## Observações de qualidade

- As alternativas completas da Questão 4 não estavam claramente legíveis na
  fonte consultada; apenas o gabarito (B) e o tema (modelo de registro para
  listas duplamente encadeadas) puderam ser confirmados.
- Notação de pseudocódigo mantida como no post original (ex.: `↑` para
  indireção de ponteiro, `.PROX`/`.ANT` para campos de nó).
