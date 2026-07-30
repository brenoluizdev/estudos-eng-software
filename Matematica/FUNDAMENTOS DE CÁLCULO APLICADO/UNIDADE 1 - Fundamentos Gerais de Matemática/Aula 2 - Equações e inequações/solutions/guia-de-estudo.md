# Guia de Estudo — Aula 2: Equações e Inequações

> Material de apoio (não oficial) para revisar e treinar o conteúdo de `content.md`.

## 1. O essencial, sem enrolação

### Equação de 1º grau: só reorganização de termos

$ax + b = 0$. A regra de ouro para resolver qualquer equação: **o que você faz de um lado, faz do outro** (soma, subtrai, multiplica, divide — nunca por zero).

Estratégia mecânica que sempre funciona:
1. Junte todos os termos com `x` de um lado.
2. Junte todos os números soltos do outro lado.
3. Divida pelo coeficiente de `x`.

### Equação de 2º grau: Bhaskara e o que o Δ (discriminante) te conta

$ax^2 + bx + c = 0 \Rightarrow x = \dfrac{-b \pm \sqrt{\Delta}}{2a}$, onde $\Delta = b^2 - 4ac$.

O `±` não é um detalhe — ele é **o motivo pelo qual uma equação do 2º grau pode ter duas respostas**. Você aplica a fórmula duas vezes (uma com `+`, outra com `−`) e obtém `x₁` e `x₂`.

O Δ é o que decide **antes mesmo de terminar a conta** quantas soluções reais existem:

| Δ | Significado geométrico (gráfico da parábola) | Nº de raízes reais |
|---|---|---|
| Δ > 0 | a parábola corta o eixo x em 2 pontos | 2 raízes distintas |
| Δ = 0 | a parábola toca o eixo x em 1 ponto só (vértice) | 1 raiz (dupla) |
| Δ < 0 | a parábola não toca o eixo x | nenhuma raiz real |

Truque de prova: se te derem Δ < 0 e pedirem "resolva a equação", a resposta é **"não possui solução real"** — não precisa nem tentar tirar a raiz quadrada de um número negativo (isso cai em números complexos, que é assunto de outra aula/curso).

### Inequações: a regra que todo mundo esquece

Tudo funciona como equação, **exceto** por uma regra crítica:

> Multiplicar ou dividir os dois lados por um número **negativo** inverte o sinal da desigualdade.

Por quê? Pense em `2 < 5`. Multiplique os dois por −1: vira `−2` e `−5`. Na reta numérica, −2 está à **direita** de −5 (é maior!). Então `−2 > −5`. O sinal precisa inverter para a afirmação continuar verdadeira.

Isso é o erro nº 1 em prova de inequação: resolver tudo certo e esquecer de virar o `<` para `>` quando divide por número negativo.

### Inequação com duas variáveis (região no plano)

Passos:
1. Isole `y`.
2. Trace a reta correspondente à igualdade (`y = ...`) — tracejada se for `<` ou `>` (estrita), sólida se for `≤` ou `≥`.
3. Escolha um ponto de teste fora da reta (ex: origem (0,0), se ela não estiver na reta) e veja se ele satisfaz a inequação. Se sim, a região do teste é a solução; se não, é a região oposta.

---

## 2. Exercícios (estilo prova)

### Questão 1 — Múltipla escolha
Resolva $4x - 7 = x + 8$:

**a)** x = 1
**b)** x = 5
**c)** x = 15
**d)** x = −5
**e)** x = 3

### Questão 2 — Múltipla escolha
Para a equação $2x^2 - 3x - 2 = 0$, o valor do discriminante Δ é:

**a)** 9
**b)** 25
**c)** −7
**d)** 41
**e)** 7

### Questão 3 — Múltipla escolha (conceitual, sem contas)
Uma equação do 2º grau tem Δ = 0. Isso significa que:

**a)** A equação não tem solução real.
**b)** A equação tem duas soluções reais distintas.
**c)** A equação tem exatamente uma solução real (raiz dupla).
**d)** A equação é, na verdade, do 1º grau.
**e)** Não é possível afirmar nada sem saber a, b e c.

### Questão 4 — Múltipla escolha
Resolva a inequação $-2x + 6 > 10$:

**a)** x > −2
**b)** x < −2
**c)** x > 2
**d)** x < 2
**e)** x > 8

### Questão 5 — Problema (pratique o método completo)
Use Bhaskara para resolver $x^2 - 5x + 6 = 0$. Mostre Δ, x₁ e x₂.

### Questão 6 — Problema (estilo "Vamos Exercitar", igual à situação das propostas de salário)
Duas operadoras de internet oferecem planos:

| Operadora | Mensalidade fixa | Custo por GB extra consumido |
|---|---|---|
| A | R$ 80,00 | R$ 4,00 |
| B | R$ 60,00 | R$ 6,00 |

a) Para quantos GB extras consumidos as duas operadoras cobram o mesmo valor?
b) Em que condição a operadora A é mais barata que a B?

---

## 3. Gabarito comentado

<details>
<summary>Clique para revelar as respostas</summary>

**Q1 —** $4x - x = 8 + 7 \Rightarrow 3x = 15 \Rightarrow x = 5$. **Resposta: b)**

**Q2 —** a=2, b=−3, c=−2. $\Delta = (-3)^2 - 4(2)(-2) = 9 + 16 = 25$. **Resposta: b)** — note que o sinal de `c` é negativo, então `−4ac` vira **positivo** (erro comum é esquecer o duplo sinal negativo aqui).

**Q3 — c)** Δ = 0 zera a raiz quadrada na fórmula de Bhaskara, então x₁ = x₂ = −b/2a: uma única raiz, dita "dupla" porque algebricamente ainda conta duas vezes na fatoração.

**Q4 —** $-2x > 10 - 6 \Rightarrow -2x > 4$. Dividir por −2 **inverte o sinal**: $x < -2$. **Resposta: b)** — se você marcou (a), esqueceu de inverter o sinal ao dividir por número negativo.

**Q5 —** a=1, b=−5, c=6. $\Delta = 25 - 24 = 1$. $x = \dfrac{5 \pm 1}{2}$. $x_1 = \dfrac{5-1}{2}=2$, $x_2=\dfrac{5+1}{2}=3$. Confira por fatoração: (x−2)(x−3) = x²−5x+6 ✓.

**Q6 —**
a) $80 + 4x = 60 + 6x \Rightarrow 20 = 2x \Rightarrow x = 10$ GB.
b) A é mais barata quando $80 + 4x < 60 + 6x \Rightarrow 20 < 2x \Rightarrow x > 10$. Ou seja, A compensa para quem consome **mais de 10 GB extras**; para menos de 10 GB, B é mais barata.

</details>
