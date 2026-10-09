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
