# Exercícios de Revisão — Unidade 2

## Questão 1 ✅

**União de Conjuntos (A ∪ B):** A união é uma operação que cria um novo conjunto contendo todos os elementos que pertencem a pelo menos um dos conjuntos originais. Em outras palavras, é a reunião de todos os elementos de A e B sem duplicações. Pense nisso como "pegar tudo" dos dois conjuntos e colocá-los em um único conjunto combinado.

Considere cinco conjuntos numéricos:

- A = {2, 4, 6, 8, 10}
- B = {3, 6, 9, 12, 15}
- C = {5, 10, 15, 20, 25}
- D = {4, 8, 12, 16, 20}
- E = {1, 3, 5, 7, 9}

**Pergunta:** Qual é o conjunto que representa a união de todos os conjuntos A, B, C, D e E?

**Resposta assinalada:** {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 25}. ✅

**Comentário:**

Alternativa correta: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 25}. Para encontrar a união de todos os conjuntos A, B, C, D e E, você deve reunir todos os números presentes em pelo menos um desses conjuntos. Vamos fazer isso:

- A = {2, 4, 6, 8, 10}
- B = {3, 6, 9, 12, 15}
- C = {5, 10, 15, 20, 25}
- D = {4, 8, 12, 16, 20}
- E = {1, 3, 5, 7, 9}

Unindo todos esses conjuntos, obtemos: **{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 25}**

## Questão 2 ✅

A interseção de conjuntos é uma operação matemática que resulta em um novo conjunto contendo apenas os elementos que são comuns a dois ou mais conjuntos. É denotada pelo símbolo "∩". Em outras palavras, a interseção de conjuntos é a coleta de elementos que pertencem a todos os conjuntos envolvidos na operação.

Seja U o conjunto universal de todos os números inteiros entre -20 e 20. Considere os conjuntos A, B e C definidos da seguinte forma:

- A = {x | x é um múltiplo de 3 entre -15 e 15}
- B = {x | x é um número par entre -10 e 10}
- C = {x | x é um número primo entre -20 e 20}

**Pergunta:** Qual é a interseção dos conjuntos A, B e C?

**Resposta assinalada:** {vazio}. ✅

**Comentário:**

Vamos analisar os conjuntos:

- **Conjunto A:** Múltiplos de 3 entre -15 e 15 → {-15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15}
- **Conjunto B:** Números pares entre -10 e 10 → {-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10}
- **Conjunto C:** Números primos entre -20 e 20 → {-19, -17, -13, -11, -7, -5, -3, -2, 2, 3, 5, 7, 11, 13, 17, 19}

**Interseção dos Conjuntos A, B e C**

A interseção é o conjunto de elementos que estão presentes em todos os três conjuntos. Vamos identificar esses elementos:

- Os elementos de A que são múltiplos de 3 e números pares entre -10 e 10 são {-6, 0, 6}.
- Os elementos de B que são números pares e também múltiplos de 3 são {-6, 0, 6}.
- Os elementos de C que são números primos e também múltiplos de 3 são {-3, 3, 5, 7}.

Nenhum dos múltiplos de 3 primos são pares, exceto o número 2, que não está na lista de múltiplos de 3 de A. Assim, a interseção considerando todos eles é: **{vazio}**.

## Questão 3 ✅

O conjunto dos números naturais, denotado por "ℕ", é um conjunto numérico fundamental na matemática. Em notação matemática, o conjunto dos números naturais pode ser representado da seguinte forma:

ℕ = {1, 2, 3, 4, 5, ...}

**Pergunta:** Qual das seguintes alternativas representa o conjunto dos números naturais?

**Resposta assinalada:** {1, 2, 3, 4, 5, ...}. ✅

**Comentário:**

Alternativa correta: {1, 2, 3, 4, 5, ...}. Explicação: números negativos não são considerados números naturais. Os números naturais são definidos como números inteiros positivos. Eles são usados para contar objetos e representar quantidades inteiras não negativas.

## Questão 4 ✅

- **União (A ∪ B):** Combina todos os elementos de ambos os conjuntos.
- **Interseção (A ∩ B):** Contém apenas os elementos comuns a ambos os conjuntos.
- **Diferença Simétrica (A Δ B):** Inclui elementos exclusivos de cada conjunto e exclui os elementos comuns.

Considere quatro conjuntos: A, B, C e D, onde:

- A = {1, 2, 3, 4, 5}
- B = {3, 4, 5, 6, 7}
- C = {5, 6, 7, 8, 9}
- D = {7, 8, 9, 10, 11}

**Pergunta:** Encontre o conjunto que representa a união de A com a interseção de B, C e a diferença simétrica entre D e B. Ou seja, calcule:

$$A \cup ((B \cap C) \cap (D \,\Delta\, B))$$

**Resposta assinalada:** {3, 4, 5, 6, 7, 8, 9, 10, 11} ✅

**Comentário:**

**1.1: Interseção de B e C**

Temos os seguintes conjuntos: B = {3, 4, 5, 6, 7} e C = {5, 6, 7, 8, 9}. A interseção de B e C é:

B ∩ C = {5, 6, 7}

**1.2: Diferença simétrica entre D e B**

Temos os seguintes conjuntos: D = {7, 8, 9, 10, 11} e B = {3, 4, 5, 6, 7}. A diferença simétrica é:

D Δ B = {8, 9, 10, 11, 3, 4, 5, 6}

**1.3: Interseção de B ∩ C e D Δ B**

A interseção é:

(B ∩ C) ∩ (D Δ B) = {5, 6}

**União de A com a interseção calculada**

{1, 2, 3, 4, 5, 6}

## Questão 5 ✅

A operação de união de conjuntos combina todos os elementos de dois conjuntos, enquanto a operação de interseção de conjuntos identifica os elementos que são comuns a ambos os conjuntos. Essas operações são fundamentais na teoria dos conjuntos e têm várias aplicações em matemática e em muitos outros campos.

Considere três conjuntos: A, B e C. Sabendo que:

- A = {1, 2, 3, 4, 5}
- B = {3, 4, 5, 6, 7}
- C = {5, 6, 7, 8, 9}

**Pergunta:** Qual é o conjunto resultante da interseção de A e B, seguido pela união com C?

**Resposta assinalada:** {3, 4, 5, 6, 7, 8, 9} ✅

**Comentário:**

Primeiro, você encontra a interseção de A e B:

A ∩ B = {3, 4, 5}

Agora, você une o resultado com o conjunto C:

(A ∩ B) ∪ C = {3, 4, 5} ∪ {5, 6, 7, 8, 9} = {3, 4, 5, 6, 7, 8, 9}

Portanto, o conjunto resultante da interseção de A e B, seguida pela união com C, é {3, 4, 5, 6, 7, 8, 9}, o que corresponde à **alternativa B**.
