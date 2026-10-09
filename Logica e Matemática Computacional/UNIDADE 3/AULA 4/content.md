# Aula 4 — Inferência Lógica

## Ponto de Partida

Olá, estudante! Dando continuidade ao nosso estudo de lógica computacional, chegou um momento muito importante no qual aprenderemos a fazer demonstrações lógicas. O raciocínio usado para fazer uma dedução lógica é similar ao usado para construir sequências lógicas em um algoritmo, pois, em ambos os casos, é necessário escrever uma sequência correta de passos, tanto em termos de sintaxe, quanto em relação ao raciocínio e às regras necessárias para alcançar o resultado desejado.

> Dando continuidade ao processo seletivo para a vaga de trainee, nessa última fase do processo, os contratantes querem testar seu raciocínio lógico, bem como seu conhecimento sobre as regras de dedução da Lógica Formal. Você recebeu dois argumentos:
>
> 1. Se o papel de tornassol ficar vermelho, então a solução é ácida. O papel de tornassol ficou vermelho. Portanto, a solução é ácida.
> 2. Se treino, eu venço o campeonato de xadrez. Se não jogo vôlei, então eu treino xadrez. Não venci o campeonato de xadrez. Portanto, joguei vôlei.
>
> Seu desafio é traduzir para forma simbólica os dois argumentos e provar a veracidade, usando as regras de dedução da Lógica Formal. Cada passo na sequência de demonstração deve ser comentado, para que os avaliadores tenham certeza de que você conhece o processo. Quantos passos serão necessários para demonstrar cada argumento? Será possível fazer uma demonstração usando somente regras de inferência? Sabendo que é mais importante conhecer o processo do que decorar regras, os avaliadores permitiram que você usasse a Internet para consultar as regras de equivalência e inferência lógica.

Para vencer esse desafio, você verá nesta seção as regras para avaliar um argumento e verificar se ele é válido ou não. Também aprenderá como estruturar a sequência de demonstração, desenvolvendo, assim, o raciocínio e dando um passo a mais na direção de se tornar um grande desenvolvedor.

Vamos em frente!

---

## Vamos Começar!

### Regras de equivalência de dedução para a lógica proposicional

As regras de dedução são divididas em dois tipos: **regras de equivalência** e **regras de inferência**. Lembrando que duas fbfs (fórmulas bem-formuladas) são equivalentes, quando todas as combinações possíveis de entradas geram o mesmo resultado de saída para ambas as fbfs, as regras de equivalência serão usadas quando uma fbf (que pode ser uma hipótese ou resultado de uma regra) pode ser substituída por outra fbf, mantendo o resultado lógico. Por exemplo, se considerarmos a fbf que traduz uma das leis de De Morgan: **¬(A ∨ B) ⇔ ¬A ∧ ¬B**, em uma situação adequada podemos substituir a fbf ¬(A ∨ B) por ¬A ∧ ¬B, pois ambas são equivalentes. No Quadro 1 estão elencadas as regras de equivalência que iremos utilizar.

| Expressão (fbf) | Equivalente (fbf) | Nome/abreviação |
|---|---|---|
| P ∨ Q<br>P ∧ Q | Q ∨ P<br>Q ∧ P | Comutatividade/com |
| (P ∨ Q) ∨ R<br>(P ∧ Q) ∧ R | P ∨ (Q ∨ R)<br>P ∧ (Q ∧ R) | Associatividade/ass |
| ¬(P ∨ Q)<br>¬(P ∧ Q) | ¬P ∧ ¬Q<br>¬P ∨ ¬Q | Leis de De Morgan/De Morgan |
| P → Q | ¬P ∨ Q | Condicional/cond |
| P | ¬(¬P) | Dupla negação/dn |
| P ↔ Q | (P → Q) ∧ (Q → P) | Definição de equivalência/que |

*Quadro 1 | Conjuntos de regras de dedução (equivalência)*

> **Nota de revisão:** na extração do material, a linha das Leis de De Morgan saiu como "¬P ∨ Q / ¬P ∧ Q", o que está errado. As formas corretas — como a própria aula escreve no parágrafo acima — são **¬(P ∨ Q) ⇔ ¬P ∧ ¬Q** e **¬(P ∧ Q) ⇔ ¬P ∨ ¬Q** (nega cada parte e troca ∨ por ∧, e vice-versa). Conferido com Gersting (2017, Tabela 1.11), que é a fonte citada na aula.

O Quadro 1 nos traz seis conjuntos de regras de dedução, sua utilização será da seguinte forma: Se tivermos uma expressão como da linha 1, Q ∨ P, quando necessário, podemos substitui-la por P ∨ Q, pois essas fbfs são equivalentes e trata-se da propriedade da comutatividade. O contrário também é válido, quando aparecer P ∨ Q, podemos substituir por Q ∨ P. Esse processo de substituir uma fbf por outra, é o mesmo para todas as demais regras apresentadas.

> **Nota de revisão:** no original, a frase "O contrário também é válido" repetia o mesmo sentido (Q ∨ P → P ∨ Q). Ajustado para o sentido inverso (P ∨ Q → Q ∨ P), que é o que a frase quer dizer.

---

## Siga em Frente...

### Regras de inferência de dedução para a lógica proposicional

Além das regras de equivalência, o processo de dedução lógica também possui as **regras de inferência**. Na inferência, dada uma determinada fbf, ela poderá ser substituída por outra que atenda à regra de inferência. Veja que aqui não é necessário ser uma tautologia (e realmente não será), mas é preciso seguir as regras da inferência.

#### Modus Ponens (MP)

A primeira regra de inferência que vamos estudar é chamada **Modus Ponens (MP)**. Essa regra envolve uma implicação e uma conjunção e possui a seguinte estrutura: **(P → Q) ∧ P → Q**. Vejamos um exemplo para ficar mais clara a regra. Considerando o seguinte argumento: Se João receber seu salário, ele irá ao cinema, vamos separar as proposições P, Q, portanto:

- **P**: João recebe o salário.
- **Q**: João vai ao cinema.

Agora vamos representar cada parte da fórmula de Modus Ponens:

- **(P → Q)**: Se João receber seu salário, ele irá ao cinema.
- **P**: João recebe o salário.

Ao fazer a conjunção entre a primeira parte com a segunda, conseguimos inferir a conclusão, pois, se João receber seu salário, ele irá ao cinema E João recebeu o salário, logo podemos inferir (concluir) que João vai ao cinema.

A regra de Modus Ponens também pode ser representada pelo esquema:

$$\begin{array}{l} P \rightarrow Q \\ P \\ \hline Q \end{array}$$

Aqui fica claro que quando se tem uma implicação e o antecedente é verdade, então a conclusão é o consequente.

#### Modus Tollens (MT)

Outra importante regra de inferência é o **Modus Tollens (MT)**. Essa regra, além de envolver uma implicação e uma conjunção, também envolve a negação de uma das proposições. Sua estrutura é dada pela fbf: **(P → Q) ∧ ¬Q → ¬P**. Vejamos um exemplo. Considere o seguinte argumento:

Se João desligar o interruptor, então a lâmpada se apaga. Vamos separar as proposições P, Q, portanto:

- **P**: João desliga o interruptor.
- **Q**: A lâmpada apaga.

Agora vamos representar cada parte da fórmula de Modus Tollens:

- **(P → Q)**: Se João desligar o interruptor, então a lâmpada se apaga.
- **¬Q**: A lâmpada não apagou.

Ao fazer a conjunção entre a primeira parte com a segunda, conseguimos inferir a conclusão. Pois, se João desligar o interruptor, a lâmpada se apaga E a lâmpada não se apagou, logo podemos inferir (concluir) que João não desligou o interruptor.

A regra de Modus Tollens também pode ser representada pelo esquema:

$$\begin{array}{l} P \rightarrow Q \\ \neg Q \\ \hline \neg P \end{array}$$

Aqui fica claro que quando se tem uma implicação e o consequente não é verdade, então a conclusão é que o antecedente também não aconteceu.

#### Silogismo Hipotético (SH)

Outra importante regra é o **Silogismo Hipotético (SH)**. Nessa regra, além de existirem implicações e conjunções nas hipóteses, a conclusão também é uma implicação. Sua estrutura é dada pela fbf: **(P → Q) ∧ (Q → R) → (P → R)**. Vejamos um exemplo. Considere o seguinte argumento: Se as árvores começam a florir, então começa a primavera. Se começa a primavera, então as árvores dão frutos. Vamos separar as proposições P, Q, R portanto:

- **P**: As árvores começam a florir.
- **Q**: A primavera começa.
- **R**: As árvores dão frutos.

Agora vamos representar cada parte da fórmula de Silogismo Hipotético:

- **(P → Q)**: Se as árvores começam a florir, então começa a primavera.
- **(Q → R)**: Se começa a primavera então as árvores dão frutos.

Ao fazer a conjunção entre a primeira parte com a segunda, conseguimos inferir a conclusão. Pois, se as árvores começam a florir, então começa a primavera E se começa a primavera então as árvores dão frutos, logo podemos inferir (concluir) que se as árvores começam a florir, então darão frutos.

A regra de Silogismo Hipotético também pode ser representada pelo esquema:

$$\begin{array}{l} P \rightarrow Q \\ Q \rightarrow R \\ \hline P \rightarrow R \end{array}$$

Veja que a consequente de uma proposição é a antecedente na outra e, por isso, o resultado pode ser inferido do antecedente da primeira para a consequente da segunda proposição.

#### Resumo das regras de inferência

O Quadro 2 apresenta um resumo de algumas das principais regras de inferências. Além das regras já apresentadas, estão elencadas mais três regras: a **conjunção**, na qual dadas duas proposições elas podem ser unidas por essa operação; a **simplificação**, que faz o contrário da conjunção, separa duas proposições; e a **adição**, que adiciona uma nova proposição a uma já existente por meio de uma disjunção.

| De | Podemos deduzir | Nome/abreviação |
|---|---|---|
| P, P → Q | Q | Modus Ponens/MP |
| P → Q, ¬Q | ¬P | Modus Tollens/MT |
| P → Q, Q → R | P → R | Silogismo Hipotético/SH |
| P, Q | P ∧ Q | Conjunção/conj |
| P ∧ Q | P, Q | Simplificação/simp |
| P | P ∨ Q | Adição/ad |

*Quadro 2 | Regras de inferência*

> **Nota de revisão:** o Quadro 2 saiu **embaralhado** na extração — a coluna da esquerda repetia as expressões do Quadro 1 e os resultados de Conjunção e Adição estavam trocados. O quadro acima foi reconstruído a partir das regras descritas na própria aula e de Gersting (2017, Tabela 1.12), fonte citada no Saiba mais. Os cabeçalhos "De / Podemos deduzir" são os que o Assimile abaixo menciona. Também corrigido no parágrafo acima: a adição usa **disjunção** (P ⊢ P ∨ Q), não conjunção.

> **Assimile:** Nas regras de equivalência, as colunas podem ser usadas nos dois sentidos. Já nas regras de inferência, só existe um sentido: a fbf da coluna "De" pode ser substituída pela coluna de "Podemos deduzir", mas o contrário não é verdade. Em outras palavras, "Ao contrário das regras de equivalência, as regras de inferência não funcionam em ambas as direções".

### Exemplo de demonstração

Agora que já conhecemos as principais regras de dedução lógica, vamos utilizar esse método para mostrar que o argumento **(¬A ∨ B) ∧ (B → C) → (A → C)** é válido. O primeiro passo é identificar as hipóteses e a conclusão. A fórmula do argumento ($P_1 \land P_2 \land P_3 \land \dots \land P_n \rightarrow C$) nos diz que as hipóteses são ligadas pela conjunção e a conclusão é ligada pela última implicação lógica. Outro detalhe importante é que as hipóteses podem ser fbf e não somente proposições simples. Portanto, para nosso caso temos:

- **Hipótese 1**: (¬A ∨ B)
- **Hipótese 2**: (B → C)
- **Conclusão**: (A → C)

Veja que na conclusão temos uma implicação, isso já nos dá indícios de que conseguiremos usar o silogismo hipotético. Vamos à sequência de demonstração.

| Passo | fbf | Justificativa |
|:---:|---|---|
| 1 | ¬A ∨ B | hip |
| 2 | B → C | hip |
| 3 | A → B | 1, cond |
| 4 | A → C | 2, 3, SH |

> **Nota de revisão:** no original, o passo 4 citava "(3, **4**, SH)" — uma linha não pode usar a si mesma. O correto é **(2, 3, SH)**, como o próprio texto explica a seguir ("entre as linhas 3 e 2").

Em quatro passos conseguimos demonstrar que o argumento é válido. Nos passos 1 e 2 elencamos as hipóteses. No passo 3, consultamos as regras de equivalência no Quadro 1, e usamos a regra de equivalência do condicional, ou seja, trocamos a hipótese ¬A ∨ B por A → B já que são equivalentes. Na linha 4, consultamos as regras de inferência no Quadro 2 e aplicamos o silogismo hipotético entre as linhas 3 e 2, ou seja, substituímos (A → B) ∧ (B → C) por A → C. Como chegamos exatamente a fbf da conclusão, provamos a validade do argumento.

As regras de dedução lógica devem ser consultadas a todo momento no processo de demonstração. Não existe uma receita, somente a prática nos auxilia a desenvolvermos o raciocínio. Podemos fazer uma analogia do processo de demonstração com a atividade do programador. Na programação sequencial, temos uma entrada e uma saída desejável, portanto, implementamos uma sequência lógica de passos para chegar a esse resultado. É trabalho do desenvolvedor descobrir qual a sequência de proposições (comandos) que farão a transformação dos dados de entrada, para a saída. Cada linha do programa tem que seguir as regras de sintaxe da linguagem de programação, bem como a lógica necessária para alcançar o resultado. Portanto, praticar esse raciocínio de sequência lógica é um passo importante na formação do profissional de tecnologia.

---

## Vamos Exercitar?

Chegou a hora de resolver seu último desafio do processo seletivo para a vaga de trainee em uma grande empresa de tecnologia. Você recebeu como desafio, avaliar dois argumentos, mostrando se eles são válidos ou não. Para isso, você deve usar as regras de dedução lógica. Relembrando os dois argumentos que lhe foram passados:

> a. Se o papel de tornassol ficar vermelho, então a solução é ácida. O papel de tornassol ficou vermelho. Portanto, a solução é ácida.
>
> b. Se treino, eu venço o campeonato de xadrez. Se não jogo vôlei, então eu treino xadrez. Não venci o campeonato de xadrez. Portanto, joguei vôlei.

Nessa etapa do desafio, você foi autorizado a usar a internet para consultar as regras de equivalência e inferência lógica.

Localizada uma fonte segura de informações, agora é preciso traduzir os argumentos para a forma simbólica e fazer a demonstração lógica.

### Argumento (a)

> Se o papel de tornassol ficar vermelho, então a solução é ácida. O papel de tornassol ficou vermelho. Portanto, a solução é ácida.

Vamos traduzir o argumento para proposições:

- **P**: O papel de tornassol fica vermelho.
- **Q**: A solução é ácida.

Agora é possível traduzir o argumento para forma simbólica: **(P → Q) ∧ P → Q**. Agora podemos começar a sequência de demonstração, iniciando pela enumeração das hipóteses, seguida da aplicação de regras de dedução:

| Passo | fbf | Justificativa |
|:---:|---|---|
| 1 | P → Q | hip |
| 2 | P | hip |
| 3 | Q | 1, 2, MP |

No item 1 tem-se a primeira hipótese P → Q. No segundo item, a segunda hipótese, lembrando que cada hipótese é conectada pela conjunção e, que cada uma delas pode ser fbf. Após elencar as hipóteses, consultamos o Quadro 2 e vimos que era possível aplicar a regra de Modus Ponens, ao aplicá-la na linha 3, chegamos exatamente na conclusão do argumento, logo esse argumento é **válido**.

> **Nota de revisão:** o original diz "consultamos o **Quadro 1**" — mas o Modus Ponens está no **Quadro 2** (regras de inferência).

### Argumento (b)

> Se treino, eu venço o campeonato de xadrez. Se não jogo vôlei, então eu treino xadrez. Não venci o campeonato de xadrez. Portanto, joguei vôlei.

Proposições:

- **P**: Eu treino.
- **Q**: Eu venci o campeonato de xadrez.
- **R**: Eu jogo vôlei.

Forma simbólica do argumento: **(P → Q) ∧ (¬R → P) ∧ ¬Q → R**.

Sequência de demonstração:

| Passo | fbf | Justificativa |
|:---:|---|---|
| 1 | P → Q | hip |
| 2 | ¬R → P | hip |
| 3 | ¬Q | hip |
| 4 | ¬P | 1, 3, MT |
| 5 | ¬¬R | 2, 4, MT |
| 6 | R | 5, dn |

> **Nota de revisão:** no original, os símbolos de negação saíram como "←" e "←←" (erro de extração), e o passo 6 citava "(**6**, dn)" — o correto é **(5, dn)**, como o texto abaixo explica.

Para demonstrar esse argumento, foram necessários seis passos, sendo três deles as hipóteses. Após elencar as hipóteses, consultamos o Quadro 2 e vimos que era possível aplicar a regra de Modus Tollens entre os itens 1 e 3, com isso obtivemos o resultado ¬P no item 4. Também vimos que podíamos aplicar a mesma regra entre os itens 2 e 4, com isso obtivemos o resultado ¬¬R no item 5. Por fim, consultado o Quadro 1 vimos que podíamos aplicar a dupla negação no item 5 e obtivemos R no item 6. Como R é a conclusão, demonstramos que o argumento é **válido**.

Com essas demonstrações, finalizamos o desafio aplicando a lógica proposicional com suas formas e regras para resolver os mais diversos problemas.

Agora é só esperar o resultado positivo da empresa!

---

## Saiba mais

Inferência lógica é fundamental para a compreensão da disciplina Lógica e Matemática Computacional. A seguir, algumas indicações para um estudo profundo sobre o tema.

1. **Fundamentos da lógica**: Leitura do capítulo 1 do livro. Nas páginas 26 e 27 você encontrará as Tabelas 1.11 e 1.12 contendo as regras de equivalência e inferência.
   > GERSTING, J. L. **Fundamentos matemáticos para a ciência da computação**. Rio de Janeiro: Grupo GEN, 2016.

2. O capítulo 5 deste livro aborda de uma forma muito clara as regras de inferência de dedução para a lógica proposicional.
   > BISPO FILHO, C. A. F.; CASTANHEIRA, L. B.; SOUZA FILHO, O. M. **Introdução à lógica matemática**. São Paulo: Cengage Learning, 2017.

## Referências

- BISPO FILHO, C. A. F.; CASTANHEIRA, L. B.; SOUZA FILHO, O. M. Introdução à lógica matemática. São Paulo: Cengage Learning, 2017.
- GERSTING, J. L. Fundamentos matemáticos para a ciência da computação: 7. ed. Rio de Janeiro: LTC, 2017.
- ROSEN, K. H. Matemática discreta e suas aplicações. Grupo A, 2010.
- SILVA, F. S. C. da; FINGER, M.; MELO, A. C. V. de. Lógica para computação. 2. ed. Cengage Learning Brasil, 2018.
