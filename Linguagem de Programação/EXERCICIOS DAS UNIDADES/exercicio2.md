# Exercícios de Revisão — Unidade 2

## Questão 1 ✅

Em Python, módulos e bibliotecas desempenham um papel fundamental na organização e reutilização de código. Módulos são arquivos Python que contêm definições de funções, classes e variáveis, enquanto bibliotecas são coleções de módulos que oferecem funcionalidades específicas.

**Pergunta:** Qual das seguintes afirmações é verdadeira em relação a módulos e bibliotecas em Python?

**Resposta assinalada:** Um módulo é uma coleção de funções e classes, enquanto uma biblioteca é uma coleção de vários módulos relacionados. ✅

**Comentário:**
- A) Está incorreta, pois uma biblioteca pode conter vários módulos, não é um único arquivo Python.
- B) Está incorreta, pois módulos não são apenas arquivos de texto simples; eles podem conter funções, classes e variáveis.
- C) Está incorreta, pois módulos não são equivalentes a funções individuais; eles podem conter várias funções e classes.
- D) Está incorreta, pois módulos e bibliotecas são termos distintos em Python, e a diferença entre eles é significativa.
- **E) Em Python, um módulo é um arquivo Python que pode conter definições de funções, classes e variáveis. Por outro lado, uma biblioteca é uma coleção de módulos que oferecem funcionalidades específicas. As bibliotecas reúnem módulos relacionados para fornecer um conjunto abrangente de recursos. *(CORRETA)***

## Questão 2 ✅

O polimorfismo em programação orientada a objetos refere-se à capacidade de diferentes classes responderem de forma diferente à mesma mensagem. Isso é possível graças à herança e às respostas específicas de cada classe às mensagens. O polimorfismo permite que você trate objetos de diferentes classes de maneira uniforme, desde que respondam a mensagens comuns.

**Pergunta:** O que é polimorfismo em programação orientada a objetos?

**Resposta assinalada:** Polimorfismo é a capacidade de diferentes classes responderem de forma diferente à mesma mensagem, permitindo tratar objetos de diferentes classes de maneira uniforme. ✅

**Comentário:**
- A) Está incorreta, pois polimorfismo não se relaciona à quantidade de construtores em uma classe.
- **B) O polimorfismo permite que objetos de diferentes classes possam ser tratados de maneira uniforme se eles responderem a mensagens comuns, mesmo que a resposta seja específica para cada classe. *(CORRETA)***
- C) Está incorreta, pois polimorfismo não envolve a ocultação de atributos e métodos.
- D) Está incorreta, pois polimorfismo não está relacionado à criação de classes em Python.
- E) Está incorreta, pois polimorfismo não está relacionado à criação de listas em Python.

## Questão 3 ✅

Python é conhecido por sua comunidade ativa e por ter uma vasta biblioteca de módulos e pacotes de terceiros disponíveis para uso. Esses módulos de terceiros são criados por desenvolvedores independentes e podem ser facilmente integrados aos projetos Python para estender suas funcionalidades. Muitos desses módulos são gerenciados e distribuídos por meio do Python Package Index (PyPI), que facilita o processo de instalação e atualização.

**Pergunta:** Qual é uma das principais vantagens de usar módulos de terceiros em Python?

**Resposta assinalada:** Módulos de terceiros permitem que os desenvolvedores ampliem as funcionalidades de seus projetos sem precisar desenvolver tudo do zero. ✅

**Comentário:**
- A) Está incorreta, pois muitos módulos de terceiros são confiáveis e amplamente utilizados na comunidade Python.
- B) Está incorreta, pois os módulos de terceiros não são incorporados ao núcleo do Python; eles são desenvolvidos independentemente.
- C) Está incorreta, pois os módulos de terceiros podem variar em complexidade, e muitos oferecem funcionalidades avançadas.
- **D) Uma das principais vantagens de usar módulos de terceiros em Python é a capacidade de estender as funcionalidades de seus projetos sem precisar reinventar a roda. Desenvolvedores podem aproveitar os módulos de terceiros para economizar tempo e recursos. *(CORRETA)***
- E) Está incorreta, pois a maioria dos módulos de terceiros em Python é de código aberto e gratuita, embora possa haver exceções com módulos específicos que são pagos. No entanto, a maioria é de código aberto e gratuita.

## Questão 4 ✅

A herança é um conceito fundamental na programação orientada a objetos que permite que as classes herdem características e comportamentos de outras classes. Em Python, você pode criar classes-filhas que herdam atributos e métodos de classes-pai. Isso promove a reutilização de código e a organização hierárquica das classes. A herança é uma maneira poderosa de criar classes especializadas que compartilham características comuns de outras classes.

**Pergunta:** Suponha que temos uma classe-pai chamada "Animal" com um método "fazer_barulho()" que retorna o som que um animal faz. Se criarmos uma classe-filha chamada "Cachorro" que herda de "Animal" e define um método "fazer_barulho()" que retorna "Latir," qual será o resultado da chamada ao método "fazer_barulho()" em uma instância da classe "Cachorro"?

**Resposta assinalada:** O método "fazer_barulho()" em uma instância de "Cachorro" retornará "Latir." ✅

**Comentário:**
- A) Está incorreta, pois "Miar" não é o som que um cachorro faz.
- B) Está incorreta, pois "Zurro" não é o som que um cachorro faz.
- **C) Quando uma classe-filha herda de uma classe-pai e redefine um método com o mesmo nome, o método da classe-filha é chamado quando esse método é invocado em uma instância da classe-filha. Portanto, uma instância de "Cachorro" chamará o método "fazer_barulho()" definido na classe "Cachorro," que retorna "Latir."**
- D) Está incorreta, pois o método retornará um valor (nesse caso, "Latir").
- E) Está incorreta, pois não há motivo para gerar um erro se a herança e a redefinição de método forem feitas corretamente.

## Questão 5 ✅

Analise as afirmações a seguir:

1. As tuplas em Python são objetos mutáveis.
2. A função `in()` em Python é usada para verificar se um elemento está presente em uma sequência.
3. A utilização de tuplas ou sequência não faz diferença na programação, visto que ambas têm a mesma função e aplicação.

**Pergunta:** Selecione a opção que descreve corretamente a relação entre as afirmações.

**Resposta assinalada:** Apenas II é verdadeira. ✅

**Comentário:**
- A) Está incorreta, pois: I – Tuplas são imutáveis e III – Apesar das tuplas e sequencias serem semelhantes, sequencias são mutáveis e tuplas não.
- B) Está incorreta, pois: I – Tuplas são imutáveis.
- C) Está incorreta, pois: I – Tuplas são imutáveis.
- **D) Está correta, a função `in` é usada para verificar a presença de um elemento em uma sequência.**
- E) Está incorreta, pois III – Apesar das tuplas e sequencias serem semelhantes, sequencias são mutáveis e tuplas não.
