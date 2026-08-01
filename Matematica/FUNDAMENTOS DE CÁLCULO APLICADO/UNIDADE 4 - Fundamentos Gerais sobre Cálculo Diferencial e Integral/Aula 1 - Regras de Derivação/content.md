## Ponto de Partida

Desejamos boas-vindas a você, estudante! Nesta aula, prosseguindo com o estudo das derivadas, vamos explorar as regras de derivação, utilizadas com bastante frequência na resolução de problemas.

Quando exploramos o conceito de derivada por meio de sua definição, é necessário calcular um limite. Se este limite existe, podemos então dizer que a função é diferenciável e identificar sua derivada. Por outro lado, quando lidamos com funções já diferenciáveis, podemos utilizar as regras de derivação para encontrar suas expressões analíticas com base em propriedades conhecidas previamente, sem a necessidade do cálculo do limite. Além das regras básicas como a regra da soma, diferença, multiplicação por constante e a regra da potência, existem outras que podem ser aplicadas para investigar as características das funções diferenciáveis. Ainda, é também essencial compreender o comportamento das derivadas das funções mais comuns, tais como as funções exponenciais, logarítmicas e trigonométricas, as quais são frequentemente utilizadas em diversas áreas da Matemática e das Ciências.

> Diante desse tema, considere as funções:
>
> 𝑓⁡(𝑥) =3⁢cos⁡(𝑥)/𝑒𝑥
>
> 𝑔⁡(𝑥) =4⁢ln⁡(𝑥) +7⁢3√𝑥2
>
> ℎ⁡(𝑥) =(1−2⁢𝑥3)⁢(𝑥2−𝑥3)
>
> Que estratégias podemos aplicar para calcular a derivada de 1ª ordem para cada uma das funções apresentadas? Calcule as derivadas de cada função identificando as propriedades e regras utilizadas em cada caso.

Dê continuidade em seus estudos e confira quais são os conceitos necessários para cumprir a tarefa proposta.

---

## Vamos Começar!

O conceito de derivada é fundamental na modelagem de fenômenos que envolvem taxas de variação, especialmente no caso instantâneo. Um exemplo notável é a determinação da velocidade instantânea de um móvel, que está diretamente relacionada à derivada da função posição correspondente. Além disso, graficamente, a derivada de uma função em um ponto pode ser interpretada como a inclinação, ou coeficiente angular, da reta tangente ao gráfico da função nesse ponto específico.

Para definir uma derivada, é crucial que o limite correspondente exista, permitindo a determinação tanto da derivada no ponto quanto da função derivada, juntamente com suas características e notações específicas.

Embora a derivada esteja intrinsecamente ligada ao cálculo de limites por definição, podemos obter regras de derivação por meio da consideração de limites mais gerais, o que nos permite aplicá-las em diversas situações sem a necessidade de recalcular limites repetidamente, desde que as funções envolvidas sejam diferenciáveis. Vejamos a seguir algumas regras que podem ser aplicadas nesse estudo.

### Regras de derivação

Além das regras de derivação envolvendo constantes, potências, soma, diferença, multiplicação por escalar, também podemos definir regras de derivação para produto e quociente de funções, conforme apresentado a seguir.

**Regra do produto:** Se 𝑓 e 𝑔 forem funções diferenciáveis em um conjunto 𝑋, então o produto 𝑓⁡𝑔 também é diferenciável, com:

> 𝑑/𝑑⁢𝑥⁢(𝑓⁡(𝑥)⁢𝑔⁡(𝑥)) =[𝑑/𝑑⁢𝑥⁢(𝑓⁡(𝑥))]⁢𝑔⁡(𝑥) +𝑓⁡(𝑥)⁢[𝑑/𝑑⁢𝑥⁢(𝑔⁡(𝑥))]

Podemos ainda representar a regra da forma (𝑓⁡𝑔)'⁢(𝑥) =𝑓'⁡(𝑥)⁢𝑔⁡(𝑥) +𝑓⁡(𝑥)⁢𝑔'⁡(𝑥), empregando a notação linha na representação das derivadas.

**Regra do quociente:** Se 𝑓 e 𝑔 forem funções diferenciáveis em 𝑋, com 𝑔⁡(𝑥) ≠0, então o quociente 𝑓⁡/𝑔 também é diferenciável, com:

> 𝑑/𝑑⁢𝑥⁢(𝑓⁡(𝑥)/𝑔⁡(𝑥)) = ([𝑑/𝑑⁢𝑥⁢(𝑓⁡(𝑥))]⁢𝑔⁡(𝑥)−𝑓⁡(𝑥)⁢[𝑑/𝑑⁢𝑥⁢(𝑔⁡(𝑥))]) / [𝑔⁡(𝑥)]2

Podemos ainda representar a regra da forma (𝑓⁡/𝑔)'(𝑥) =(𝑓'⁡(𝑥)⁢𝑔⁡(𝑥)−𝑓⁡(𝑥)⁢𝑔'⁡(𝑥))/(𝑔⁡(𝑥))2, utilizando a notação linha na representação das derivadas.

Vejamos como determinar a derivada da função 𝑞⁡(𝑥) =(3⁢𝑥2−1)/𝑥3. Podemos empregar duas estratégias diferentes nesse caso:

**Opção 1:** podemos interpretar a função 𝑞 como um produto de funções da forma (𝑥) =(3⁢𝑥2−1)⁢𝑥−3 e, nesse caso, aplicar a regra do produto tomando 𝑓⁡(𝑥) =3⁢𝑥2 −1 e 𝑔⁡(𝑥) =𝑥−3. Assim, 𝑓'⁡(𝑥) =6⁢𝑥 e 𝑔'⁡(𝑥) =(−3)⁢𝑥−4, e:

> 𝑞'⁡(𝑥) =𝑓'⁡(𝑥)⁢𝑔⁡(𝑥) +𝑓⁡(𝑥)⁢𝑔'⁡(𝑥) =(6⁢𝑥)⁢(𝑥−3) +(3⁢𝑥2−1)⁢((−3)⁢𝑥−4)=6⁢𝑥−2 +(−3)⁢(3⁢𝑥−2−𝑥−4) =6⁢𝑥−2 −9⁢𝑥−2 +3⁢𝑥−4 =−3⁢𝑥−2 +3⁢𝑥−4=−3/𝑥2 +3/𝑥4

Logo, 𝑞'⁡(𝑥) =−3/𝑥2 +3/𝑥4.

**Opção 2:** podemos aplicar a regra do quociente tomando 𝑓⁡(𝑥) =3⁢𝑥2 −1 e 𝑔⁡(𝑥) =𝑥3. Desse modo, 𝑓'⁡(𝑥) =6⁢𝑥, (𝑔⁡(𝑥))2 =𝑥6 e 𝑔'⁡(𝑥) =3⁢𝑥2, logo:

> 𝑞'⁡(𝑥) =(𝑓'⁡(𝑥)⁢𝑔⁡(𝑥)−𝑓⁡(𝑥)⁢𝑔'⁡(𝑥)) / (𝑔⁡(𝑥))2 = ((6⁢𝑥)⁢(𝑥3)−(3⁢𝑥2−1)⁢(3⁢𝑥2)) / 𝑥6 = (6⁢𝑥4−3⁢(3⁢𝑥4−𝑥2)) / 𝑥6 = (6⁢𝑥4−9⁢𝑥4+3⁢𝑥2) / 𝑥6 = (−3⁢𝑥4+3⁢𝑥2) / 𝑥6 = (−3⁢𝑥4)/𝑥6 + (3⁢𝑥2)/𝑥6 =−3/𝑥2 +3/𝑥4

Portanto, 𝑞'⁡(𝑥) =−3/𝑥2 +3/𝑥4.

Além dessas duas possibilidades, note que podemos simplificar a lei de formação da função q da seguinte forma:

> 𝑞⁡(𝑥) =(3⁢𝑥2−1)/𝑥3 = 3⁢𝑥2/𝑥3 −1/𝑥3 = 3/𝑥 −1/𝑥3 =3⁢𝑥−1 −𝑥−3

Com isso, a derivada de q pode ser obtida da seguinte forma:

> 𝑞 ′(𝑥) =3⁢(−1)⁢𝑥−2 −(−3)⁢𝑥−4 =−3⁢𝑥−2 +3⁢𝑥−4 =−3/𝑥2 +3/𝑥4

Além dessas possibilidades, podemos simplificar a lei de formação de 𝑞 como segue:

> 𝑞⁡(𝑥) =(3⁢𝑥2−1)/𝑥3 = 3⁢𝑥2/𝑥3 −1/𝑥3 = 3/𝑥 −1/𝑥3 =3⁢𝑥−1 −𝑥−3

Assim, a derivada será:

> 𝑞'⁡(𝑥) =3⁢((−1)⁢𝑥−2) −(−3)⁢𝑥−4 =−3⁢𝑥−2 +3⁢𝑥−4 =−3/𝑥2 −3/𝑥4

Dessa forma, podemos calcular as derivadas de funções que são apresentadas na forma de produtos e quocientes, sabendo que essas regras podem ser articuladas com as demais regras, como a soma e a diferença de funções, por exemplo.

É importante destacar que a regra da potência pode ser aplicada também para expoentes não inteiros. Veja o caso da função 𝑓⁡(𝑥) =3√𝑥4 =𝑥4/3. Calculando a primeira derivada teremos:

> 𝑓'⁡(𝑥) =4/3⁢𝑥(4/3)−1 =4/3⁢𝑥1/3 =4/3⁢3√𝑥

Além das regras já vistas, vamos analisar a regra direcionada a funções compostas, denominada regra da cadeia.

### Regra da cadeia

Se 𝑔 for derivável em 𝑥 e 𝑓 for derivável em 𝑔⁡(𝑥), então a composição 𝑓 ∘𝑔 será derivável em 𝑥. Além disso, a derivada da função composta (𝑓∘𝑔)⁡(𝑥) =𝑓⁡(𝑔⁡(𝑥)) será dada por:

> (𝑓⁡(𝑔⁡(𝑥))' =𝑓'⁡(𝑔⁡(𝑥)) ⋅𝑔'⁡(𝑥)

Se 𝑦 =𝑓⁡(𝑢) e 𝑢 =𝑔⁡(𝑥), a regra da cadeia assume a forma:

> 𝑑⁢𝑦/𝑑⁢𝑥 = 𝑑⁢𝑦/𝑑⁢𝑢 ⋅𝑑⁢𝑢/𝑑⁢𝑥

A demonstração da regra da cadeia pode ser encontrada na seção 3.4, página 181, do livro *Cálculo: volume 1*, de Stewart, Clegg e Watson, o qual está disponível em Minha Biblioteca.

Considere a função ℎ⁡(𝑥) =(𝑥2+1)7. A função ℎ pode ser entendida como a composta ℎ =𝑓 ∘𝑔 em que 𝑓⁡(𝑢) =𝑢7 e 𝑔⁡(𝑥) =𝑥2 +1. Sabemos que 𝑓'⁡(𝑢) =7⁢𝑢6 e 𝑔'⁡(𝑥) =2⁢𝑥, pela regra da potência, da soma e da constante. Aplicando a regra da cadeia obtemos:

> ℎ'⁡(𝑥) =(𝑓⁡(𝑔⁡(𝑥))' =[7⁢(𝑥2+1)6] ⋅(2⁢𝑥) =14⁢𝑥⁢(𝑥2+1)6

Portanto, ℎ'⁡(𝑥) =14⁢𝑥⁢(𝑥2+1)6.

A regra da cadeia aplicada a uma função composta (𝑓 ∘𝑔)⁡(𝑥) =𝑓⁡(𝑔⁡(𝑥))assume a forma (𝑓⁡(𝑔⁡(𝑥))' =𝑓'(𝑔⁡(𝑥) ⋅𝑔'⁡(𝑥). Se pensarmos em 𝑓 como a função “de fora” e 𝑔 como a função “de dentro”, então a derivada da função composta pode ser entendida como a derivada da função “de fora”, aplicada na função “de dentro”, multiplicada pela derivada da função “de dentro”

Com a regra da cadeia podemos avaliar as derivadas de funções compostas por meio da articulação com as demais regras de derivação, em conjunto com as derivadas conhecidas para as funções pertencentes às principais categorias, como polinomiais, exponenciais, etc. Logo, complementando esse estudo, vejamos a seguir derivadas de algumas funções importantes.

---

## Siga em Frente...

### Derivadas de funções exponenciais e logarítmicas

Seja a função exponencial 𝑓⁡(𝑥) =𝑏𝑥. Pela definição de derivada temos:

> 𝑓'⁡(𝑥) = lim ℎ→0 ⁡(𝑏𝑥+ℎ−𝑏𝑥)/ℎ = lim ℎ→0 ⁡(𝑏𝑥⁢(𝑏ℎ−1))/ℎ =𝑏𝑥 ⋅lim ℎ→0 ⁡(𝑏ℎ−1)/ℎ

Como lim ℎ→0 ⁡(𝑏ℎ−1)/ℎ = lim ℎ→0 ⁡(𝑏0+ℎ−𝑏0)/ℎ =𝑓'⁡(0), se 𝑓 for diferenciável em zero, então será diferenciável em todos os reais, com 𝑓'⁡(𝑥) =𝑏𝑥⁢𝑓'⁡(0). Adotando 𝑏 =𝑒, tal que lim ℎ→0 ⁡(𝑒ℎ−1)/ℎ =1, então, nesse caso, 𝑓′⁡(0) =1 e 𝑓'⁡(𝑥) =𝑒𝑥, ou seja, 𝑑/𝑑⁢𝑥⁢(𝑒𝑥) =𝑒𝑥, que corresponde à regra de derivação da função exponencial de base e.

Por outro lado, para uma base 𝑏 qualquer, com 𝑏 >0 e 𝑏 ≠1, considerando a igualdade 𝑏 =𝑒ln⁡𝑏, proveniente das propriedades das potências e logaritmos, então 𝑏ℎ =𝑒(ln⁡𝑏)ℎ e 𝑓'⁡(𝑥) =𝑏𝑥 ⋅lim ℎ→0 ⁡(𝑒(ln⁡𝑏)ℎ−1)/ℎ.

Adotando a mudança de variáveis (ln⁢𝑏)ℎ =𝑡, então ℎ =𝑡/ln⁡𝑏. Logo, lim ℎ→0 ⁡(𝑒ℎ−1)/ℎ =1 e:

> lim ℎ→0 ⁡(𝑒(ln⁡𝑏)ℎ−1)/ℎ = lim 𝑡→0 ⁡(𝑒𝑡−1)/(𝑡/ln⁡𝑏) = lim 𝑡→0 ⁡(ln⁡𝑏⋅(𝑒𝑡−1)/𝑡) =ln⁡𝑏 ⋅lim 𝑡→0 ⁡(𝑒𝑡−1)/𝑡 =ln⁡𝑏 ⋅1 =ln⁡𝑏

Portanto, podemos concluir que 𝑑/𝑑⁢𝑥⁢(𝑏𝑥) =𝑏𝑥 ⋅ln⁡𝑏. Por exemplo, 𝑑/𝑑⁢𝑥⁢(2𝑥) =2𝑥 ⋅ln⁡2.

Também podemos calcular a derivada de funções logarítmicas, considerando a existência da função logarítmica natural. Porém, como as funções exponenciais e logarítmicas podem ser associadas entre si por meio do conceito de função inversa, então podemos empregar essa relação também para a determinação das derivadas.

Se uma função 𝑓 é definida em um intervalo 𝐼, de tal forma que sua derivada 𝑓'⁡(𝑥) existe e não se anula em 𝐼, então sua inversa 𝑓−1 é também derivável em qualquer ponto de seu domínio. Para determinar o valor da derivada de 𝑓−1 em um ponto 𝑏, ou (𝑓−1)⁢(𝑏), podemos empregar a seguinte relação: (𝑓−1)'⁢(𝑏) =1/𝑓'⁡(𝑓−1⁡(𝑏)), ou seja, (𝑓−1)'⁢(𝑏) corresponde ao recíproco de 𝑓' calculado em 𝑎 =𝑓−1⁡(𝑏).

Diante dessa relação, seja 𝑓⁡(𝑥) =𝑒𝑥, sendo sua inversa 𝑓−1⁡(𝑥) =ln⁡𝑥. Da regra anterior, e sabendo que 𝑓'⁡(𝑥) =𝑒𝑥, obtemos:

> 𝑑/𝑑⁢𝑥⁢(ln⁡𝑥) =(𝑓−1)'⁢(𝑥) =1/𝑓'⁡(𝑓−1⁡(𝑥)) =1/𝑒𝑓−1⁡(𝑥) =1/𝑒ln⁡𝑥 =1/𝑥

Agora, vejamos as funções na forma 𝑓⁡(𝑥) =log𝑏⁡(𝑥). Pela mudança de base sabemos que log𝑏⁡(𝑥) =ln⁡𝑥/ln⁡𝑏, sendo ln⁡𝑏 constante. Calculando a derivada temos:

> 𝑑/𝑑⁢𝑥⁢(log𝑏⁡(𝑥)) =𝑑/𝑑⁢𝑥⁢(ln⁡𝑥/ln⁡𝑏) =1/ln⁡𝑏 ⋅𝑑/𝑑⁢𝑥(ln⁡𝑥)=1/ln⁡𝑏⋅1/𝑥=1/(𝑥⁢ln⁡𝑏)

Outras funções que podem ser estudadas diante do conceito de derivada são as trigonométricas, como destacado a seguir.

### Derivadas de funções trigonométricas

Para as derivadas de funções trigonométricas precisamos conhecer identidades trigonométricas e limites importantes, como lim 𝑥→0 ⁡sen⁡(𝑥)/𝑥 =1 e lim 𝑥→0 ⁡(1−cos⁡(𝑥))/𝑥 =0. Vejamos o caso da função 𝑓⁡(𝑥) =sen⁡(𝑥) utilizando a definição de derivada via limite:

> 𝑓'⁡(𝑥) = lim ℎ→0 ⁡(sen⁡(𝑥+ℎ)−sen⁡(𝑥))/ℎ = lim ℎ→0 ⁡(sen⁡(𝑥)⁢cos⁡(ℎ)+sen⁡(ℎ)⁢cos⁡(𝑥)−sen⁡(𝑥))/ℎ = lim ℎ→0 ⁡[sen⁡(𝑥)⁢((cos⁡(ℎ)−1)/ℎ)+cos⁡(𝑥)⁢(sen⁡(ℎ)/ℎ)]= lim ℎ→0 ⁡[cos⁡(𝑥)⁢(sen⁡(ℎ)/ℎ)−sen⁡(𝑥)⁢((1−cos⁡(ℎ))/ℎ)]=(cos⁡(𝑥))⁢lim ℎ→0 ⁡(sen⁡(ℎ)/ℎ)−(sen⁡(𝑥))⁢lim ℎ→0 ⁡((1−cos⁡(ℎ))/ℎ) =cos⁡(𝑥) ⋅1 −sen⁡(𝑥) ⋅0=cos⁡(𝑥)

Logo, 𝑑/𝑑⁢𝑥⁢(sen⁡(𝑥)) =cos⁡(𝑥). De forma análoga, 𝑑/𝑑⁢𝑥⁢(cos⁡(𝑥)) =−sen⁡(𝑥).

Para as demais funções trigonométricas temos os seguintes resultados:

| | |
|---|---|
| 𝑑/𝑑⁢𝑥⁢(𝑡⁢𝑔⁡(𝑥)) =sec2⁡(𝑥) | 𝑑/𝑑⁢𝑥⁢(𝑐⁡𝑜⁢𝑡⁢𝑔⁡(𝑥)) =−𝑐⁡𝑜⁢𝑠⁢𝑠⁢𝑒⁢𝑐2⁡(𝑥) |
| 𝑑/𝑑⁢𝑥⁢(𝑠⁢𝑒⁢𝑐⁡(𝑥)) =sec⁡(𝑥) ⋅𝑡⁢𝑔⁡(𝑥) | 𝑑/𝑑⁢𝑥⁢(𝑐⁡𝑜⁢𝑠⁢𝑠⁢𝑒⁢𝑐⁡(𝑥)) =−𝑐⁡𝑜⁢𝑠⁢𝑠⁢𝑒⁢𝑐⁡(𝑥) ⋅𝑐⁡𝑜⁢𝑡⁢𝑔⁡(𝑥) |

Além da definição, podemos determinar cada uma dessas derivadas utilizando as regras de derivação em conjunto com as definições dessas razões trigonométricas que dependem apenas de seno e cosseno. Por exemplo, como 𝑡⁢𝑔⁡(𝑥) =sen⁡(𝑥)/cos⁡(𝑥), podemos aplicar a regra do quociente para determinar que 𝑑/𝑑⁢𝑥⁢(𝑡⁢𝑔⁡(𝑥)) =1/cos2⁡(𝑥) =sec2⁡(𝑥).

De posse das funções derivadas, podemos determinar também as derivadas em pontos, substituindo o valor de 𝑥 nas expressões pelo ponto desejado e efetuando os cálculos necessários, lembrando que a unidade usualmente utilizada para 𝑥 nas funções trigonométricas é o radiano, sendo necessário configurar as calculadoras científicas para esse uso.

As regras de diferenciação são estratégias importantes para o cálculo de derivadas, desde que as funções envolvidas atendam aos critérios necessários para a existência dos limites correspondentes.

---

## Vamos Exercitar?

Com base nas regras de derivação, vamos analisar as funções apresentadas e calcular as respectivas derivadas de 1ª ordem.

**Seja 𝑓⁡(𝑥) =3⁢cos⁡(𝑥)/𝑒𝑥.**

Como essa função é representada por um quociente entre as funções 𝑝⁡(𝑥) =3⁢cos⁡(𝑥) e 𝑞⁡(𝑥) =𝑒𝑥, podemos empregar a regra do quociente, em conjunto com os conhecimentos sobre derivadas das funções trigonométricas e exponenciais. Sabemos que 𝑝'⁡(𝑥) =−3⁢sen⁡(𝑥) e 𝑞'⁡(𝑥) =𝑒𝑥, logo:

> 𝑓'⁡(𝑥) =𝑑/𝑑⁢𝑥⁢(3⁢cos⁡(𝑥)/𝑒𝑥) = (𝑑/𝑑⁢𝑥⁢[3⁢cos⁡(𝑥)]⋅𝑒𝑥−3⁢cos⁡(𝑥)⋅[𝑑/𝑑⁢𝑥⁢(𝑒𝑥)]) / (𝑒𝑥)2 = (3⋅𝑑/𝑑⁢𝑥⁢(cos⁡(𝑥))⋅𝑒𝑥−3⁢cos⁡(𝑥)⋅[𝑑/𝑑⁢𝑥⁢(𝑒𝑥)]) / (𝑒𝑥)2 = (3⋅(−sen⁡(𝑥))⋅𝑒𝑥−3⁢cos⁡(𝑥)⋅𝑒𝑥) / (𝑒𝑥⋅𝑒𝑥) = (−3⁢sen⁡(𝑥)−3⁢cos⁡(𝑥)) / 𝑒𝑥

Sendo assim, 𝑓'⁡(𝑥) =𝑑/𝑑⁢𝑥⁢(𝑓⁡(𝑥)) = (−3⁢sen⁡(𝑥)−3⁢cos⁡(𝑥)) / 𝑒𝑥.

**Seja 𝑔⁡(𝑥) =4⁢ln⁡(𝑥) +7⁢3√𝑥2.**

Nesse caso, temos uma soma de funções, bem como uma composição de funções na segunda parcela. Adotando 𝑟⁡(𝑥) =4⁢ln⁡(𝑥), 𝑠⁡(𝑥) =7⁢3√𝑥 e 𝑡⁡(𝑥) =𝑥2, temos que 𝑔⁡(𝑥) =𝑟⁡(𝑥) +(𝑠∘𝑡)⁢(𝑥). Nesse caso, observe que:

> 𝑟'⁡(𝑥) =𝑑/𝑑⁢𝑥⁢(4⁢ln⁡(𝑥)) =4⁢𝑑/𝑑⁢𝑥⁢(ln⁡(𝑥)) =4/𝑥

Ainda, para a função composta devemos aplicar a regra da cadeia. Nesse caso, observe que 𝑠'⁡(𝑡) =𝑑/𝑑⁢𝑥⁢(7⁢3√𝑥) =7⁢𝑑/𝑑⁢𝑥⁢(𝑥1/3) =7 ⋅(1/3⁢𝑥1/3−1) =7/3 ⋅𝑥−2/3 =7/3 ⋅1/𝑥2/3 e, também, 𝑡'⁡(𝑥) =2⁢𝑥, logo:

> (𝑠∘𝑡)'⁡(𝑥) =𝑑/𝑑⁢𝑥(𝑠⁡(𝑡⁡(𝑥)) ⋅𝑑/𝑑⁢𝑥⁢(𝑡⁡(𝑥)) =7/3 ⋅1/(𝑥2)2/3 ⋅2⁢𝑥 =14⁢𝑥/(3⁢(𝑥2)2/3)

Portanto,

> 𝑔'⁡(𝑥) =4/𝑥 +14⁢𝑥/(3⁢(𝑥2)2/3)

**Seja ℎ⁡(𝑥) =(1−2⁢𝑥3)⁢(𝑥2−𝑥3)⁢ℎ⁡(𝑥) =(1−2⁢𝑥3)⁢(𝑥2−𝑥3).**

Para calcular a derivada de ℎ⁡(𝑥) podemos empregar diferentes procedimentos. Uma possibilidade é aplicar a distributividade, expressar ℎ⁡(𝑥) como um polinômio e aplicar as propriedades da soma, multiplicação por escalar e potência. Vamos resolver pela regra do produto considerando 𝑎⁡(𝑥) =1 −2⁢𝑥3 e 𝑏⁡(𝑥) =𝑥2 −𝑥3. Sabemos que 𝑎'⁡(𝑥) =−6⁢𝑥2 e 𝑏'⁡(𝑥) =2⁢𝑥 −3⁢𝑥2, logo:

> ℎ'⁡(𝑥) =[𝑑/𝑑⁢𝑥⁢(1−2⁢𝑥3)] ⋅(𝑥2−𝑥3) +(1−2⁢𝑥3) ⋅[𝑑/𝑑⁢𝑥⁢(𝑥2−𝑥3)]=(−6⁢𝑥2) ⋅(𝑥2−𝑥3) +(1−2⁢𝑥3) ⋅(2⁢𝑥−3⁢𝑥2)=−6⁢𝑥4 +6⁢𝑥5 +2⁢𝑥 −3⁢𝑥2 −4⁢𝑥4 +6⁢𝑥5 =2⁢𝑥 −3⁢𝑥2 −10⁢𝑥4 +12⁢𝑥5

**Dessa forma, podemos concluir que ℎ'⁡(𝑥) =2⁢𝑥 −3⁢𝑥2 −10⁢𝑥4 +12⁢𝑥5**, o que conclui a tarefa proposta.
