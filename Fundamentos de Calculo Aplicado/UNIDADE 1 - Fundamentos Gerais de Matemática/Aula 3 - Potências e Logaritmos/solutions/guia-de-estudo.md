# Guia de Estudo — Aula 3: Potências e Logaritmos

> Material de apoio (não oficial) para revisar e treinar o conteúdo de `content.md`.

## 1. O essencial, sem enrolação

### Expoente negativo — o que ele realmente faz

$a^{-n} = \dfrac{1}{a^n}$. O sinal de menos **não** torna o resultado negativo — ele "vira" a base para o denominador. Ex: $3^{-4} = \dfrac{1}{81}$ (positivo!). Erro clássico de prova: confundir `3^{-4}` com `-3^4`.

### As 5 propriedades de potência — o que cada uma faz

| # | Regra | Quando usar / intuição |
|---|---|---|
| I | $a^m \cdot a^n = a^{m+n}$ | Mesma base sendo **multiplicada** → soma os expoentes |
| II | $\dfrac{a^m}{a^n} = a^{m-n}$ | Mesma base sendo **dividida** → subtrai os expoentes |
| III | $(a^m)^n = a^{m \cdot n}$ | Potência **de** potência → multiplica os expoentes |
| IV | $(a \cdot b)^m = a^m \cdot b^m$ | Produto elevado a expoente → distribui para cada fator |
| V | $(a/b)^m = a^m / b^m$ | Quociente elevado a expoente → distribui para numerador e denominador |

Cuidado: I e II só valem se a **base for igual**. $2^3 \cdot 3^2$ **não** simplifica por essas regras — bases diferentes.

### Expoente racional = raiz disfarçada

$$a^{\frac{m}{n}} = \sqrt[n]{a^m}$$

Decore assim: **o denominador do expoente vira o índice da raiz** (o "n" de baixo da fração vai para fora da raiz), e o numerador continua sendo o expoente de dentro. Ex: $8^{2/3} = \sqrt[3]{8^2} = \sqrt[3]{64} = 4$.

### Logaritmo — a pergunta que ele responde

$\log_a b = c$ responde: **"a que expoente eu elevo `a` para chegar em `b`?"** A resposta é `c`.

$$\log_a b = c \iff a^c = b$$

| Nome | Papel |
|---|---|
| a | base (a > 0, a ≠ 1) |
| b | logaritmando (b > 0 — **log de número negativo ou zero não existe**) |
| c | o logaritmo em si (o expoente procurado) |

Por que `b > 0`? Porque uma base positiva elevada a **qualquer** expoente real nunca dá negativo nem zero. Não existe `c` tal que `2^c = -4`. É por isso que `log_2(-4)` não existe — não é uma regra arbitrária, é consequência direta da definição de potência.

Por que `a ≠ 1`? Porque `1` elevado a qualquer expoente sempre dá `1`. Se `b ≠ 1`, não haveria `c` que resolvesse; se `b = 1`, qualquer `c` resolveria (infinitas respostas) — em nenhum dos dois casos existe uma resposta única, então a base 1 é proibida por definição.

### As "consequências" — por que cada uma é óbvia depois que você entende a definição

- $\log_a a = 1$ → "a que expoente elevo a para chegar em a?" → 1 (óbvio: $a^1=a$).
- $\log_a 1 = 0$ → "a que expoente elevo a para chegar em 1?" → 0 (qualquer base elevada a 0 dá 1).
- $\log_a a^n = n$ → já está na forma "a elevado a alguma coisa", então a resposta é a própria coisa.
- $a^{\log_a x} = x$ → "eleve a ao expoente que leva a até x" → por definição, isso te devolve x. Essa identidade é usada para **desfazer** um logaritmo.

### Propriedades operatórias — de onde vêm (não são arbitrárias)

| Propriedade | Fórmula | Por que funciona |
|---|---|---|
| Produto | $\log_a(bc) = \log_a b + \log_a c$ | Espelha a Propriedade I das potências ($a^m \cdot a^n = a^{m+n}$) |
| Quociente | $\log_a(b/c) = \log_a b - \log_a c$ | Espelha a Propriedade II das potências |
| Potência | $\log_a b^k = k \log_a b$ | Espelha a Propriedade III das potências |

É por isso que o log "transforma multiplicação em soma" — essa era literalmente a motivação histórica (Napier, século XVII): fazer contas de multiplicação/divisão gigantes virarem soma/subtração, muito mais fáceis à mão.

### log vs ln

- `log` sem base escrita = base 10 (log decimal).
- `ln` = base *e* (log natural/neperiano), onde e ≈ 2,71828.

---

## 2. Exercícios (estilo prova)

### Questão 1 — Múltipla escolha
Simplifique $\dfrac{5^7}{5^3} \cdot 5^{-2}$:

**a)** $5^2$
**b)** $5^6$
**c)** $5^{12}$
**d)** $5^{-2}$
**e)** $5^9$

### Questão 2 — Múltipla escolha
O valor de $27^{2/3}$ é:

**a)** 3
**b)** 6
**c)** 9
**d)** 18
**e)** 729

### Questão 3 — Múltipla escolha
Qual das expressões abaixo **não** está definida (não existe)?

**a)** $\log_2 8$
**b)** $\log_5 1$
**c)** $\log_3(-9)$
**d)** $\log_{10} 0{,}001$
**e)** $\log_7 7$

### Questão 4 — Múltipla escolha
Sabendo que $\log_2 5 \approx 2{,}32$, o valor de $\log_2 20$ é aproximadamente (dica: $20 = 5 \cdot 4$):

**a)** 2,32
**b)** 4,32
**c)** 9,28
**d)** 6,64
**e)** 2

### Questão 5 — Problema
Resolva $\log_4 x = 3$ (encontre x usando a definição de logaritmo).

### Questão 6 — Problema (estilo "Vamos Exercitar", crescimento exponencial)
Um investimento duplica de valor a cada 5 anos. Você investiu R$ 1.000,00 hoje.

a) Escreva a expressão que dá o valor `V` do investimento após `t` períodos de 5 anos.
b) Depois de quantos períodos de 5 anos o valor chega a R$ 16.000,00?
c) Quantos anos são necessários no total para isso ocorrer?

---

## 3. Gabarito comentado

<details>
<summary>Clique para revelar as respostas</summary>

**Q1 —** $5^{7-3} \cdot 5^{-2} = 5^4 \cdot 5^{-2} = 5^{4+(-2)} = 5^2$. **Resposta: a)**

**Q2 —** $27^{2/3} = \sqrt[3]{27^2} = \sqrt[3]{729} = 9$. Atalho mais rápido: $\sqrt[3]{27}=3$ primeiro, depois eleva ao quadrado: $3^2=9$. **Resposta: c)**

**Q3 — c)** log de número negativo não existe (nenhuma base positiva elevada a qualquer expoente real dá negativo). (a) é 3, (b) é 0, (d) é −3 (pois 10⁻³=0,001), (e) é 1 — todos válidos.

**Q4 —** $\log_2 20 = \log_2(5 \cdot 4) = \log_2 5 + \log_2 4 = 2{,}32 + 2 = 4{,}32$ (usando propriedade do produto e sabendo que $\log_2 4 = 2$ porque $2^2=4$). **Resposta: b)**

**Q5 —** Por definição, $\log_4 x = 3 \iff 4^3 = x \Rightarrow x = 64$.

**Q6 —**
a) $V = 1000 \cdot 2^t$
b) $16000 = 1000 \cdot 2^t \Rightarrow 2^t = 16 \Rightarrow 2^t = 2^4 \Rightarrow t = 4$.
c) 4 períodos × 5 anos = **20 anos**.

</details>
