# Aula 2 — Arranjos Matemáticos

## Ponto de Partida

Olá, estudante! Nesta aula, você terá a oportunidade de explorar assuntos relacionados a arranjos matemáticos.

Durante os estudos, você aprenderá o que são arranjos matemáticos e como utilizá-los tanto na matemática como em diversas áreas como:

- **Análise de algoritmos**: em ciência da computação, o desempenho de algoritmos muitas vezes depende da ordem dos elementos de entrada ou saída. Os arranjos são usados para analisar o comportamento de algoritmos em tais cenários.
- **Teoria dos números**: em algumas áreas da teoria dos números, arranjos são usados para explorar padrões e propriedades dos números inteiros.
- **Organização e estruturação**: em muitos casos, é importante organizar elementos de forma específica. Os arranjos matemáticos fornecem uma maneira de modelar e analisar essas estruturas.

Nesta aula, será introduzido assuntos relacionados aos arranjos simples, às fórmulas e aos exemplos de aplicações de arranjos simples. Por fim, será explorado arranjos com repetição. Esta seção abordará alguns princípios matemáticos relacionados à lógica. Você pode já ter se deparado com problemas do tipo:

- De quantas maneiras podemos escolher um password válido para um computador?
- Suponha que você tem quatro livros diferentes (A, B, C, D) e deseja organizá-los em uma prateleira. Quantas maneiras diferentes existem de organizar esses livros?

Esses problemas, além do raciocínio lógico, envolvem noções de listagem, contagem e agrupamentos, noções estas que teremos oportunidade de conhecer um pouco melhor nesta seção e ajudarão você a resolver seu terceiro desafio.

> Para motivar sua aprendizagem, imagine que você trabalha em uma empresa de tecnologia que ajudou a fundar, uma startup de tecnologia e mais um desafio lhe é apresentado pois, nesta empresa, existem seis funcionários (A, B, C, D, E, F) e três projetos diferentes (Projeto X, Projeto Y, Projeto Z). Você precisa alocar dois funcionários para cada projeto e deseja calcular quantas maneiras diferentes de fazer essa alocação.

Aproveite ao máximo a oportunidade de praticar o estudo relacionado aos arranjos matemáticos. Esses conceitos são de suma importância para profissionais que desenvolvem sistemas de software utilizando diferentes linguagens de programação e algoritmos, permitindo que executem suas funções técnicas de forma eficaz e alcancem resultados profissionais excepcionais.

Bons estudos!

---

## Vamos Começar!

### Arranjos simples

Arranjos matemáticos são uma categoria de conceitos na matemática que envolvem a organização e seleção de elementos de um conjunto, levando em consideração a ordem e, às vezes, as outras condições específicas. Os arranjos são frequentemente usados em problemas de contagem, probabilidade, combinatorial e estatísticas.

Arranjos são agrupamentos formados com **p** elementos de um conjunto de **n** elementos. Arranjos são trocas de posição entre os elementos. Mas no caso dos arranjos, são escolhidos p elementos para ocupar as posições ordenadas.

De acordo com Iezzi et al. (2004), dado um conjunto com n elementos distintos, chama-se **arranjo dos n elementos, tomados p a p**, a qualquer sequência ordenada de p elementos distintos escolhidos entre os n existentes. Para determinar o número de arranjos podemos utilizar a fórmula descrita na fórmula a seguir.

$$A_n^k = \dfrac{n!}{(n-k)!}$$

#### Exemplo: conjunto A = {1, 2, 3, 4}

Para ilustrar esse conceito, considere o conjunto A = {1,2,3,4}. Vamos determinar o número de arranjos desses quatro elementos (n = 4) tomados dois a dois (p = 2). Utilizando a fórmula para determinação do número de arranjos, temos que:

$$A_{4,2} = \dfrac{n!}{(n-p)!} = \dfrac{4!}{(4-2)!} = \dfrac{4!}{2!} = \dfrac{4 \cdot 3 \cdot 2 \cdot 1}{2 \cdot 1} = \dfrac{24}{2} = 12$$

De fato, discriminando todos os arranjos chegamos a 12 possibilidades:

| | | | | | |
|---|---|---|---|---|---|
| (1,2) | (1,3) | (1,4) | (2,1) | (2,3) | (2,4) |
| (3,1) | (3,2) | (3,4) | (4,1) | (4,2) | (4,3) |

Note que (2,3) é diferente de (3,2), isto é, ao trocarmos a ordem dos elementos, obtemos um novo agrupamento. Como a ordem dos elementos é relevante, podemos afirmar que os arranjos são um tipo de lista.

#### Exemplo: fila indiana com seis pessoas

Considere, por exemplo, o problema de se determinar de quantas maneiras seis pessoas A, B, C, D, E e F podem ser dispostas em uma fila indiana. Cada maneira de compor a fila é uma permutação das seis pessoas, pois qualquer fila obtida é uma sequência ordenada na qual comparecem sempre as seis pessoas. Ao utilizarmos a fórmula do número de arranjos, percebemos que neste caso n = p.

$$A_{6,6} = \dfrac{n!}{(n-p)!} = \dfrac{6!}{(6-6)!} = \dfrac{6!}{0!} = \dfrac{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{1} = 720$$

Ou seja, existem **720 maneiras** distintas para organização dessa fila.

#### Exemplo: senha de quatro algarismos distintos

> Para acessar um site, cada usuário cria uma senha com quatro algarismos, todos distintos entre si. Então, o número de senhas possíveis que esse site admite é igual a?

Sabemos que existem dez algarismos possíveis (0,1,2,3,4,5,6,7,8,9). Então, calcularemos o arranjo simples de dez algarismos tomados de quatro em quatro. Para calcular a quantidade de arranjos, temos que n = 10 e k = 4, então, basta substituir na fórmula.

$$A_{10,4} = \dfrac{10!}{(10-4)!}$$

$$A_{10,4} = \dfrac{10!}{6!}$$

$$A_{10,4} = \dfrac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6!}{6!}$$

$$A_{10,4} = 10 \cdot 9 \cdot 8 \cdot 7$$

$$A_{10,4} = 5040$$

### Arranjos com repetição

O arranjo com repetição é um tipo de agrupamento da análise combinatória.

O **arranjo com repetição** são os agrupamentos ordenados com p elementos entre n elementos de um conjunto, permitindo repetições.

Para calcular o arranjo com repetição, utilizamos a fórmula:

$$A(n,p) = n^p$$

- **n** = número de elementos do conjunto.
- **p** = quantidade de elementos por agrupamento.

Vejamos, a seguir, como aplicar a fórmula para encontrar a quantidade de arranjos com repetição que podemos formar em determinadas situações.

#### Exemplo: senha do cartão do banco

> Em um banco, a senha do cartão é composta por quatro números, que podem ser repetidos ou não, então, qual é a quantidade de senhas possíveis para esse cartão?

**Resolução:**

Sabemos que a senha é uma sequência de quatro algarismos e que a ordem é importante, logo, esse problema se trata de um arranjo com repetição.

Existem dez algarismos de zero até nove, então, n = 10, e serão escolhidos quatros deles, então, p = 4. Dessa forma, temos que:

$$AR_{10,4} = 10^4 = 10.000$$

Então, há **dez mil senhas** distintas possíveis.

---

## Siga em Frente...

### Diferença entre arranjos simples e arranjos com repetição

A diferença principal entre um "arranjo simples" e um "arranjo com repetição" está na permissão para a repetição de elementos no processo de organização ou seleção de elementos a partir de um conjunto. Aqui está a distinção entre os dois:

**Arranjos simples:**

- Em um arranjo simples, cada elemento do conjunto só pode ser escolhido uma vez em um único arranjo.
- A ordem dos elementos no arranjo é importante, o que significa que a ordem em que os elementos são organizados é considerada na contagem.
- Um elemento escolhido não pode ser escolhido novamente para a mesma posição no arranjo.
- Por exemplo, ao organizar as letras A, B e C em um arranjo simples de três elementos, as permutações seriam ABC, ACB, BAC, BCA, CAB e CBA. Não há repetição dos elementos.

**Arranjos com repetição:**

- A ordem dos elementos no arranjo ainda é importante, mas a repetição é permitida, o que significa que um elemento pode aparecer várias vezes no mesmo arranjo.
- Por exemplo, ao organizar as letras A, B e C em um arranjo com repetição de três elementos, os arranjos incluiriam AAA, AAB, AAC, ABA, ABB, ACC, BAA, BAB, BAC, BBA, BBB, BCA, CAA, CAB, CAC, CBA, CBB e CCA. Neste caso, os elementos podem se repetir.

| | Arranjo simples | Arranjo com repetição |
|---|---|---|
| A ordem importa? | Sim | Sim |
| Elementos podem se repetir? | Não | Sim |
| Fórmula | $A_n^k = \dfrac{n!}{(n-k)!}$ | $A(n,p) = n^p$ |

Resumindo, a diferença fundamental entre um arranjo simples e um arranjo com repetição está na capacidade de repetir elementos no arranjo. Em arranjos simples, cada elemento é escolhido uma única vez, enquanto em arranjos com repetição, os elementos podem ser escolhidos e repetidos em diferentes posições do arranjo. A decisão de usar um ou outro depende do contexto do problema específico que você está resolvendo e das restrições envolvidas.

---

## Vamos Exercitar?

Você se lembra que na situação-problema, você trabalha em uma startup que produz softwares para uso industrial e está analisando o seguinte cenário?

> Suponha que a startup tenha seis funcionários (A, B, C, D, E, F) e três projetos diferentes (Projeto X, Projeto Y, Projeto Z). Você precisa alocar dois funcionários para cada projeto e deseja calcular quantas maneiras diferentes de fazer essa alocação.

Neste caso, estamos interessados em calcular o número de arranjos sem repetição, uma vez que cada funcionário pode ser alocado a apenas um projeto, e a ordem em que eles são alocados não importa.

Usaremos a fórmula de arranjos sem repetição:

$$A(n,r) = \dfrac{n!}{(n-r)!}$$

- **n** é o número total de funcionários (6).
- **r** é o número de funcionários a serem alocados para cada projeto (2).

**Projeto X** — Primeiro, calculemos o número de maneiras de alocar funcionários para o Projeto X:

$$A(6,2) = \dfrac{6!}{(6-2)!} = \dfrac{6!}{4!} = \dfrac{720}{24} = 30$$

**Projeto Y** — Agora, calculamos o número de maneiras de alocar funcionários para o Projeto Y. Uma vez que dois funcionários já foram alocados ao Projeto X, temos quatro funcionários restantes para escolher dois para o Projeto Y:

$$A(4,2) = \dfrac{4!}{(4-2)!} = \dfrac{4!}{2!} = 12$$

> **Nota de revisão:** no material original esta linha aparecia como $\dfrac{24!}{2!}$ — erro de digitação; o correto é $\dfrac{4!}{2!} = \dfrac{24}{2} = 12$. O resultado não muda.

**Projeto Z** — Por fim, calculamos o número de maneiras de alocar funcionários para o Projeto Z. Como dois funcionários já foram alocados para o Projeto X e dois para o Projeto Y, restam dois funcionários para escolher para o Projeto Z:

$$A(2,2) = \dfrac{2!}{0!} = 2$$

Agora, para encontrar o total de maneiras diferentes de alocar funcionários para os três projetos, multiplicamos esses resultados, pois as alocações para cada projeto são independentes:

$$30 \times 12 \times 2 = 720$$

Portanto, existem **720 maneiras** diferentes de alocar funcionários aos projetos da empresa. Isso pode ser útil na gestão de recursos humanos e na alocação de pessoal para projetos específicos.

> **Nota de revisão:** o material original diz que "a ordem em que eles são alocados não importa", mas resolve com **arranjo** — fórmula usada justamente quando a ordem **importa**. As duas coisas não combinam:
>
> - Se a ordem dentro da dupla **importa** (ex.: um é líder e o outro é auxiliar), a resolução acima com arranjos está correta: $30 \times 12 \times 2 = 720$.
> - Se a ordem dentro da dupla **não importa** (como o texto afirma), o correto seria usar **combinação** (assunto da Aula 4): $C(6,2) \times C(4,2) \times C(2,2) = 15 \times 6 \times 1 = 90$ maneiras.
>
> Em prova, leia o enunciado com atenção para decidir se a ordem importa — é isso que define arranjo × combinação.

---

## Saiba mais

Arranjos matemáticos desempenham um papel fundamental em muitos campos da matemática, ciência, engenharia e em diversas aplicações do mundo real. A seguir, algumas indicações para um estudo profundo sobre o tema.

1. O capítulo 4 deste livro (Análise combinatória) aborda o tópico relacionado a arranjos simples de uma forma bem objetiva e clara.
   > QUILELLI, P. **Raciocínio lógico matemático para concursos**. 3. ed. Editora Saraiva, 2015.

2. Este livro aborda o tópico relacionado a permutações e arranjos simples de uma forma bem objetiva e clara.
   > ARAUJO, L. M. M. et al. **Fundamentos de matemática**. Grupo A, 2018.

## Referências

- ARAUJO, L. M. M. et al. Fundamentos de matemática. Grupo A, 2018.
- IEZZI, G. et al. Matemática: ciências e aplicações. 2. ed. São Paulo: Atual, 2004.
- QUILELLI, P. Raciocínio lógico matemático para concursos. 3. ed. Editora Saraiva, 2015.
- ROSEN, K. H. Matemática discreta e suas aplicações. Grupo A, 2010.
