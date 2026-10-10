# Exercícios de Revisão — Unidade 3

## Questão 1 ✅

Premissas são declarações ou proposições iniciais que são aceitas como verdadeiras e formam a base lógica para argumentos ou conclusões em lógica matemática e raciocínio. As premissas são usadas para construir argumentos lógicos e deduzir conclusões com base nessas premissas. Em um argumento válido, se as premissas são verdadeiras, então a conclusão também deve ser verdadeira. Portanto, as premissas desempenham um papel fundamental na lógica matemática, fornecendo as regras ou condições a partir das quais as conclusões são derivadas.

**Premissas:**

- Se um animal tem penas, então é uma ave.
- Se um objeto é um quadrado, então tem quatro lados.

Com base nas premissas acima, avalie as seguintes asserções e a relação proposta entre elas.

> I. Se um animal não tem penas, então não é uma ave.
>
> **PORQUE**
>
> II. A negação de uma proposição condicional é uma proposição válida em lógica matemática.

**Pergunta:** A respeito dessas asserções, assinale a alternativa correta.

**Resposta assinalada:** As asserções I e II são proposições verdadeiras e a II justifica a I. ✅

**Comentário:**

Alternativa correta: As asserções I e II são proposições verdadeiras e a II justifica a I. As asserções I e II são verdadeiras, e a asserção II fornece uma justificativa lógica para a asserção I. A negação de uma proposição condicional é uma proposição válida em lógica matemática.

> **Nota de revisão:** o gabarito considera a asserção I correta, mas ela **não decorre** da premissa — é um erro clássico chamado **falácia da negação do antecedente**.
>
> Com P = "tem penas" e Q = "é uma ave", a premissa é **P → Q**. A asserção I diz **¬P → ¬Q** (a *inversa*), que **não é equivalente** a P → Q:
>
> | P | Q | P → Q | ¬P → ¬Q |
> |:---:|:---:|:---:|:---:|
> | V | V | V | V |
> | V | F | F | V |
> | F | V | **V** | **F** |
> | F | F | V | V |
>
> Na 3ª linha as duas diferem: o caso "não tem penas, mas é ave" (P = F, Q = V) **não contradiz a premissa** — ela só fala do que acontece quando o animal **tem** penas — mas contradiz a asserção I. Para a lógica, basta esse caso ser possível para a dedução não valer.
>
> A asserção II também é imprecisa: "¬P → ¬Q" não é a **negação** da condicional (a negação de P → Q é **P ∧ ¬Q**), e sim a **inversa**.
>
> **Forma correta:** o que se pode concluir de P → Q é a **contrapositiva ¬Q → ¬P** — "*se um animal não é uma ave, então não tem penas*". Pelo raciocínio lógico, a alternativa correta seria a que indica que **as asserções I e II são falsas** (as alternativas não foram copiadas da plataforma, então não dá para indicar a letra). Se for cobrada de novo, avalie as alternativas com essa análise em mente.

## Questão 2 ✅

O silogismo hipotético em lógica e matemática computacional é um tipo de argumento condicional que segue a forma "se... então...". Ele estabelece uma relação entre um antecedente (condição) e um consequente (conclusão), afirmando que se a condição for verdadeira, a conclusão também será verdadeira. É uma estrutura fundamental para a dedução e argumentação lógica na construção de provas e algoritmos.

Dado o silogismo hipotético a seguir:

> "Se chover, então o jogo de futebol será adiado."

**Pergunta:** Qual das seguintes alternativas é uma conclusão válida baseada no silogismo acima?

**Resposta assinalada:** O jogo de futebol não foi adiado, portanto não está chovendo. ✅

**Comentário:**

Alternativa correta: O jogo de futebol não foi adiado, portanto não está chovendo.

- *Está chovendo, portanto, o jogo de futebol foi adiado.* **Incorreto.** O silogismo hipotético não nos diz o que acontece quando está chovendo, portanto, não podemos concluir que o jogo foi adiado apenas com base na chuva.
- *Não está chovendo, portanto, o jogo de futebol foi adiado.* **Incorreto.** Da mesma forma, o silogismo não nos diz o que acontece quando não está chovendo, portanto, não podemos concluir que o jogo foi adiado nessa situação.
- *O jogo de futebol foi adiado, portanto está chovendo.* **Incorreto.** Não podemos afirmar que está chovendo apenas com base na informação de que o jogo foi adiado, porque outras razões podem levar ao adiamento do jogo.
- ***O jogo de futebol não foi adiado, portanto não está chovendo.* Correto.** A partir do silogismo, podemos concluir que se o jogo de futebol não foi adiado, então não está chovendo. Isso segue a estrutura do silogismo hipotético.
- *O jogo de futebol foi adiado, portanto está chovendo.* **Incorreto.** Podemos concluir que está chovendo se o jogo de futebol foi adiado, mas não podemos afirmar que o jogo foi adiado apenas com base na informação de que está chovendo.

> **Nota de revisão:** a **resposta está correta**, mas o enunciado e o comentário têm erros de conceito:
>
> 1. **O nome da regra está errado.** "Se chover, o jogo será adiado" é uma condicional simples (P → Q). Concluir "não foi adiado, logo não choveu" (¬Q → ¬P) é **Modus Tollens**, não silogismo hipotético. O **silogismo hipotético** encadeia duas condicionais: P → Q e Q → R, logo P → R.
> 2. **A 1ª alternativa é válida, ao contrário do que o comentário diz.** "Está chovendo, portanto o jogo foi adiado" é **Modus Ponens** (P → Q e P, logo Q) — é uma conclusão válida. A condicional diz exatamente o que acontece quando chove.
> 3. A alternativa "O jogo de futebol foi adiado, portanto está chovendo" aparece **duas vezes** no comentário, e a segunda explicação é contraditória. Ela é **inválida** (falácia da afirmação do consequente): o jogo pode ter sido adiado por outro motivo.
>
> **Resumo correto:**
>
> | Alternativa | Regra | Válida? |
> |---|---|:---:|
> | Chove → foi adiado | Modus Ponens | ✅ |
> | Não foi adiado → não chove | Modus Tollens | ✅ |
> | Foi adiado → chove | Afirmação do consequente | ❌ |
> | Não chove → foi adiado (ou não foi) | Negação do antecedente | ❌ |
>
> Como a prova só aceitava uma resposta, a marcada (Modus Tollens) é a esperada — mas saiba que a de Modus Ponens também é logicamente válida.

## Questão 3 ✅

As regras de equivalência de dedução para lógica proposicional são um conjunto de regras que permitem simplificar e transformar proposições de modo a estabelecer equivalências lógicas. Isso é feito através de regras que incluem identidade, comutatividade, associatividade, distributividade, negação dupla e implicação material. Essas regras são fundamentais para demonstrar que duas expressões lógicas são logicamente equivalentes.

**Premissas:** Considere as seguintes premissas:

1. P ⍰ (Q ⍰ R)
2. (P ⍰ Q) ⍰ (P ⍰ R)

**Pergunta:** Usando as regras de equivalência de dedução, determine qual das seguintes alternativas é logicamente equivalente à expressão (P ⍰ Q) ⍰ (P ⍰ R):

**Resposta assinalada:** (P ⍰ Q) ⍰ (P ⍰ R). ✅

**Comentário:**

Alternativa correta: (P ⍰ Q) ⍰ (P ⍰ R). Podemos usar a regra da distributividade para simplificar a expressão original.

> ⍰ = conectivo lógico (∧ ou ∨) que se perdeu na cópia do material e não pode ser recuperado com certeza nesta questão. Compare com a Questão 4, que tem o mesmo enunciado com os símbolos completos.

## Questão 4 ✅

As regras de equivalência de dedução para lógica proposicional são um conjunto de regras que permitem simplificar e transformar proposições de modo a estabelecer equivalências lógicas. Isso é feito através de regras que incluem identidade, comutatividade, associatividade, distributividade, negação dupla e implicação material. Essas regras são fundamentais para demonstrar que duas expressões lógicas são logicamente equivalentes.

Considere as seguintes premissas:

- P ∧ (Q ∨ R)
- (P ∧ Q) ∨ (P ∧ R)

**Pergunta:** Usando as regras de equivalência de dedução, determine qual das seguintes alternativas é logicamente equivalente à expressão (P ∧ Q) ∨ (P ∧ R).

**Resposta assinalada:** P ∧ (Q ∨ R) ✅

**Comentário:**

Para justificar a resposta, vamos revisar a expressão original e aplicar as regras de equivalência de dedução para lógica proposicional.

**Expressão Original**

$$(P \land Q) \lor (P \land R)$$

**Regras de Equivalência**

**Distributividade:** A regra da distributividade na lógica proposicional afirma que:

$$A \land (B \lor C) \equiv (A \land B) \lor (A \land C)$$

Podemos aplicar essa regra ao contrário para simplificar a expressão original.

**Aplicação da Regra**

Vamos aplicar a regra da distributividade ao contrário na expressão original, $(P \land Q) \lor (P \land R)$. Usando a regra da distributividade:

$$(P \land Q) \lor (P \land R) \equiv P \land (Q \lor R)$$

Portanto, a expressão $P \land (Q \lor R)$ é logicamente equivalente à expressão original $(P \land Q) \lor (P \land R)$.

**Análise das Alternativas**

Agora, vamos revisar cada alternativa para verificar se alguma delas é equivalente à expressão simplificada $P \land (Q \lor R)$.

- **Alternativa a — $P \land (Q \land R)$:** Esta expressão não é equivalente à expressão simplificada $P \land (Q \lor R)$. A expressão simplificada permite que P seja verdadeiro e pelo menos um de Q ou R seja verdadeiro, enquanto esta alternativa requer que P, Q e R sejam todos verdadeiros.

- **Alternativa b — $(P \lor Q) \land (P \lor R)$:** Vamos aplicar a distributividade para verificar se esta expressão é equivalente à expressão simplificada. Distribuindo, obtemos:

  $$(P \land P) \lor (P \land R) \lor (Q \land P) \lor (Q \land R)$$

  Simplificando:

  $$P \lor (P \land R) \lor (Q \land P) \lor (Q \land R)$$

  Como $P \lor (P \land R) = P$ e $P \lor (Q \land P) = P$, temos:

  $$P \lor (Q \land R)$$

  Esta expressão não é equivalente à expressão simplificada $P \land (Q \lor R)$, pois a expressão simplificada requer que P seja verdadeiro e Q ou R sejam verdadeiros, enquanto a expressão simplificada requer apenas que P seja verdadeiro.

  > **Nota de revisão:** a conclusão (não é equivalente) está certa, mas a justificativa tem um erro: onde diz "enquanto **a expressão simplificada** requer apenas que P seja verdadeiro", deveria ser "enquanto **esta alternativa**...". E P ∨ (Q ∧ R) nem exige P: ela também é verdadeira com P falso, Q e R verdadeiros. Exemplo que mostra a diferença: P = F, Q = V, R = V → P ∨ (Q ∧ R) = **V**, mas P ∧ (Q ∨ R) = **F**.

- **Alternativa c — $(P \land Q) \land (Q \land R)$:** Esta expressão não é equivalente à expressão simplificada $P \land (Q \lor R)$. A expressão simplificada permite que P seja verdadeiro e Q ou R sejam verdadeiros, enquanto esta alternativa requer que P, Q e R sejam todos verdadeiros.

- **Alternativa d — $P \lor (Q \land R)$:** Esta expressão não é equivalente à expressão simplificada $P \land (Q \lor R)$. A expressão simplificada requer que P seja verdadeiro e Q ou R sejam verdadeiros, enquanto esta alternativa permite que P seja verdadeiro ou que Q e R sejam ambos verdadeiros.

- **Alternativa e — $(P \land Q) \land (P \land R)$:** Esta expressão não é equivalente à expressão simplificada $P \land (Q \lor R)$. A expressão simplificada permite que P seja verdadeiro e Q ou R sejam verdadeiros, enquanto esta alternativa requer que P seja verdadeiro e Q e R sejam ambos verdadeiros.

**Conclusão**

A expressão equivalente correta é $P \land (Q \lor R)$.

## Questão 5 ✅

O Modus Tollens é uma regra de inferência em lógica que afirma que, se a consequência (B) de uma implicação condicional ("Se A, então B") for negada, então podemos concluir que a condição (A) também é negada. Isso é frequentemente usado para tirar conclusões a partir de negações de resultados esperados.

Dada a seguinte afirmação condicional:

> "Se João passar no exame, então ele receberá uma bolsa de estudos."

**Pergunta:** Qual das seguintes alternativas é verdadeira com base no Modus Tollens?

**Resposta assinalada:** João não recebeu uma bolsa de estudos, portanto ele não passou no exame. ✅

**Comentário:**

- Se João passar no exame (A), então ele receberá uma bolsa de estudos (B).
- João não recebeu uma bolsa de estudos (¬B).
- Portanto, João não passou no exame (¬A).

**Alternativa correta: E**
