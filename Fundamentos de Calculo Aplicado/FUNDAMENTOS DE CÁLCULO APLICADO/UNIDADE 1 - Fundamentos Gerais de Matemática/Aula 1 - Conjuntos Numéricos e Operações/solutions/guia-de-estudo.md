# Guia de Estudo — Aula 1: Conjuntos Numéricos e Operações

> Este arquivo é um material de apoio (não oficial) para revisar e treinar o conteúdo de `content.md`. Não substitui o material da Anhanguera.

## 1. O essencial, sem enrolação

A ideia central da aula é uma **hierarquia de inclusão**:

```
N  ⊂  Z  ⊂  Q  ⊂  R  ⊂  C
                    ↑
              I = R − Q  (irracionais ficam "fora" de Q, mas dentro de R)
```

Leia assim: todo número natural é inteiro, todo inteiro é racional, todo racional é real, todo real é complexo. `I` (irracionais) e `Q` (racionais) são **disjuntos** — nenhum número é os dois ao mesmo tempo — e juntos formam `R`.

| Conjunto | O que contém | Teste rápido para saber se um número está lá |
|---|---|---|
| ℕ | 0, 1, 2, 3... | É inteiro e não-negativo? |
| ℤ | ..., −2, −1, 0, 1, 2... | É inteiro (positivo, negativo ou zero)? |
| ℚ | tudo que vira fração a/b, a,b ∈ ℤ, b≠0 | A parte decimal é **exata ou periódica**? (ex: 0,5 ou 0,333...) |
| 𝕀 | dízimas **não** periódicas | A parte decimal é infinita e **sem padrão**? (ex: π, √2) |
| ℝ | ℚ ∪ 𝕀 | É "qualquer número da reta numérica"? |
| ℂ | a + bi, a,b ∈ ℝ | Envolve √(negativo)? |

**Pegadinha clássica de prova:** √4 = 2, que é racional (na verdade é inteiro!), mas √2 é irracional. A presença de uma raiz não significa automaticamente "irracional" — depende se o resultado é exato.

### Os sufixos ₊ ₋ * — o que cada símbolo faz

Isso aparece muito em prova de múltipla escolha e costuma confundir. A lógica é sempre a mesma, independente do conjunto (ℤ ou ℚ):

- **`+` subscrito** → remove os negativos (mantém o zero). Ex: ℤ₊ = {0, 1, 2, 3, ...}
- **`−` subscrito** → remove os positivos (mantém o zero). Ex: ℤ₋ = {0, −1, −2, ...}
- **`*` sobrescrito** → remove o zero (mantém os dois sinais). Ex: ℤ* = ℤ − {0}
- **`*` + `+`/`−` juntos** → remove o zero **e** um dos sinais. Ex: ℤ*₊ = {1, 2, 3, ...} (positivos estritos)

Pense no `*` sempre como "sem o zero" e no `+`/`−` como "só esse sinal". Combine os dois efeitos e você deduz qualquer subconjunto sem decorar.

### Divisão euclidiana — o que q e r realmente são

$$a = b \cdot q + r, \quad 0 \le r < b$$

- **q (quociente):** quantas vezes `b` cabe inteiramente em `a`.
- **r (resto):** o que sobra depois de tirar essas `q` cópias de `b`. Sempre menor que `b` — se não fosse, caberia mais uma cópia de `b`.

Quando r = 0, dizemos que `b` **divide** `a` (a é múltiplo de b). Isso é a base de tudo que vocês vão ver depois sobre MMC/MDC.

### Números complexos — por que existem

Motivação: `x² = −1` não tem solução em ℝ (nenhum número real ao quadrado dá negativo). Define-se `i` tal que `i² = −1`, e com isso qualquer número passa a ser escrito como `a + bi`.

- **a** = parte real (um número real comum)
- **b** = parte imaginária (também é um número real — o "imaginário" é o `i`, não o `b`!)
- **Afixo**: o ponto (a, b) no plano de Argand-Gauss — é só um plano cartesiano onde o eixo x virou "Re" e o eixo y virou "Im".

Erro comum: achar que a parte imaginária de `2 + 3i` é `3i`. **Não é** — é `3`. O `i` fica de fora, é só o "marcador" de qual eixo aquele número representa.

---

## 2. Exercícios (estilo prova — múltipla escolha)

### Questão 1
Classifique o número $-\dfrac{9}{3}$ da forma mais específica possível:

**a)** Apenas racional
**b)** Natural
**c)** Inteiro (e consequentemente racional e real)
**d)** Irracional
**e)** Não pertence a nenhum conjunto numérico usual

### Questão 2
Qual conjunto é representado por ℚ*₋?

**a)** {0, −1, −2, −3, ...}
**b)** {..., −2, −1, 1, 2, ...} apenas com inteiros
**c)** Todos os racionais negativos, excluindo o zero
**d)** Todos os racionais não positivos, incluindo o zero
**e)** Todos os reais negativos

### Questão 3
Ao dividir 87 por 6, qual é o quociente e o resto?

**a)** q = 14, r = 3
**b)** q = 14, r = 0
**c)** q = 15, r = −3
**d)** q = 13, r = 9
**e)** q = 14, r = 4

### Questão 4
Calcule $\dfrac{3}{4} - \dfrac{2}{5}$:

**a)** $\dfrac{1}{9}$
**b)** $\dfrac{7}{20}$
**c)** $\dfrac{15}{20}$
**d)** $\dfrac{1}{20}$
**e)** $\dfrac{5}{9}$

### Questão 5
No número complexo $z = -4 + 7i$, a parte imaginária de z é:

**a)** −4
**b)** 7i
**c)** 7
**d)** −4 + 7i
**e)** i

### Questão 6 (problema, sem múltipla escolha — pratique o método do "Vamos Exercitar")
Uma cooperativa possui um terreno de 60 hectares. $\dfrac{1}{4}$ do terreno é reserva legal e $\dfrac{1}{6}$ é ocupado por um galpão e uma estrada de acesso, ambos permanentes.

a) Que fração do terreno resta disponível para uso?
b) Se 1 hectare = 10.000 m², quantos m² estão disponíveis?

---

## 3. Gabarito comentado

<details>
<summary>Clique para revelar as respostas</summary>

**Q1 — c)** $-\frac{9}{3} = -3$, que é um número inteiro. Todo inteiro também é racional e real, mas a resposta **mais específica** é "inteiro". Não é natural (ℕ não tem negativos).

**Q2 — c)** O `*` remove o zero, o `−` mantém só os negativos. Junto: racionais negativos sem o zero. (a) é a descrição de ℤ₋ ou ℚ₋ (com zero); descarte por ter zero. (d) é ℚ₋ (com zero, sem o `*`).

**Q3 — a)** 87 = 6 · 14 + 3, pois 6·14 = 84 e 87 − 84 = 3. Confira: r deve satisfazer 0 ≤ r < 6, e 3 está nesse intervalo. (e) erra porque 6·14+4=88≠87.

**Q4 —** mmc(4,5) = 20. $\dfrac{3}{4} = \dfrac{15}{20}$, $\dfrac{2}{5} = \dfrac{8}{20}$. $\dfrac{15}{20} - \dfrac{8}{20} = \dfrac{7}{20}$. **Resposta: b)**

**Q5 — c)** A parte imaginária é o número real que multiplica `i`, ou seja, 7 — não "7i". Essa é a pegadinha mais comum do assunto.

**Q6 —**
a) $\dfrac{1}{4} + \dfrac{1}{6}$, mmc(4,6)=12: $\dfrac{3}{12}+\dfrac{2}{12}=\dfrac{5}{12}$ ocupados. Disponível: $1 - \dfrac{5}{12} = \dfrac{7}{12}$.
b) 60 hectares = 600.000 m². $\dfrac{7}{12} \cdot 600.000 = 350.000$ m² disponíveis.

</details>
