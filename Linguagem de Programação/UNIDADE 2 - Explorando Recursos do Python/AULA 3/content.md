# Aula 3 — Orientação a Objetos: Classes e Herança em Python

## Ponto de Partida

Quando pensamos em programação, devemos nos atentar à **orientação a objetos**, um paradigma essencial nesse contexto, pois organiza o código em torno de objetos, cada um representando entidades do mundo real.

Nesta etapa de aprendizagem, descobriremos, em Python, como criar **classes**, que são os modelos para a construção de objetos, e de que maneira é possível definir atributos e métodos dentro delas.

Discutiremos, também, sobre a **herança** em Python, a qual permite que classes-filhas herdem atributos e métodos de classes-pai, promovendo a reutilização de código e a criação de hierarquias de classes.

Você obterá uma compreensão sólida sobre esses conceitos fundamentais relativos à orientação a objetos e estará pronto para criar estruturas de código mais organizadas e reutilizáveis em Python.

> Imagine, agora, a seguinte situação: você precisa criar um algoritmo que, a partir de características imputadas, mostre um resumo e o status de um veículo. Você também deve fazer algo semelhante para promover uma subdivisão dessa classe veículos. Vamos, juntos, resolver essa demanda?

## Vamos Começar!

### Introdução à orientação a objetos

Na indústria de software, a evolução é constante, com tecnologias que mudam rapidamente, mas os conceitos fundamentais do paradigma de programação orientada a objetos permanecem sólidos e são cruciais. Compreender esses conceitos é essencial, pois permite que você os implemente em qualquer tecnologia adotada pela sua empresa, independentemente de mudanças frequentes.

A programação orientada a objetos tem suas raízes fincadas na década de 1960, mas só ganhou destaque a partir de 1990. Uma linguagem de programação é considerada orientada a objetos quando incorpora os princípios de abstração e suporta o uso de **encapsulamento**, **herança** e **polimorfismo**.

No entanto, para entender completamente a programação orientada a objetos, é importante compreender o que são objetos e qual é o papel das classes.

Os programas são construídos em torno de objetos, que são as unidades fundamentais. Uma classe atua como um modelo para um objeto. Pode-se pensar em uma classe como o projeto de uma casa, no qual um arquiteto define todos os detalhes da estrutura. A classe organiza os dados e comportamentos que os objetos de uma classe específica terão.

Confira, a seguir, um exemplo de classe:

**Classe: Pessoa**

Atributos (dados):

- Nome:
- Idade:
- Gênero:

Métodos (comportamentos):

- Cumprimentar: saúda como "Olá, meu nome é".
- Aniversário: aumenta a idade em 1.

**Objeto 1: Pessoa1**

Atributos (dados):

- Nome: João
- Idade: 30
- Gênero: Masculino

Métodos (comportamentos):

- Cumprimentar: saúda como "Olá, meu nome é João".
- Aniversário: aumenta a idade em 1.

Nesse exemplo, a classe "Pessoa" define os atributos (nome, idade, gênero) e métodos (cumprimentar, aniversário) que o objeto "Pessoa1" pode usar.

Cada objeto tem seus próprios atributos, mas compartilha os mesmos métodos da classe. Isso demonstra como a programação orientada a objetos modela entidades do mundo real.

Para as classes, temos os seguintes "componentes" principais:

- **Atributos**: são os dados que representam o estado do objeto, como nome e idade.
- **Métodos**: definem o comportamento do objeto, indicando as ações que ele pode executar, como cumprimentar ou fazer login.
- **Encapsulamento**: combina atributos e métodos em uma entidade, permitindo controlar o acesso a atributos por meio de métodos.
- **Herança**: possibilita que uma classe herde atributos e métodos de outra, promovendo o reúso de código e a organização hierárquica, como na relação entre as classes pessoa, funcionário e cliente.
- **Polimorfismo**: refere-se à capacidade de várias classes responderem de forma diferente a uma mesma mensagem, graças à herança e às respostas específicas de cada classe às mensagens.

### Classes em Python

Python é uma linguagem que oferece suporte ao paradigma orientado a objetos, viabilizando a implementação de encapsulamento, herança e polimorfismo. A criação de uma classe em Python é feita com a palavra reservada "class", seguida do nome da classe, e em um bloco indentado são definidos os atributos e métodos.

```python
# Define uma classe chamada Pessoa.
class Pessoa:

    # O método __init__ é um construtor, chamado quando um objeto da classe é criado.
    # Ele inicializa os atributos da classe.
    def __init__(self, nome, idade, genero):

        # self é uma convenção em Python que se refere à própria instância da classe.
        # Os parâmetros nome, idade e gênero são passados durante a criação do objeto.
        # Eles são usados para inicializar os atributos da instância.
        self.nome = nome # Atribui o valor de nome ao atributo nome da instância.
        self.idade = idade # Atribui o valor de idade ao atributo idade da instância.
        self.genero = genero # Atribui o valor de gênero ao atributo gênero da instância.

    # O método cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar(self):
        return f”Olá, meu nome é {self.nome}.”

    # O método aniversário aumenta a idade da pessoa em 1.
    def aniversario(self):
        self.idade += 1

# Cria uma instância da classe “Pessoa” com os valores “João”, 30 e “Masculino” para nome, idade e gênero, respectivamente.
pessoa1 = Pessoa(“João”, 30, “Masculino”)

# Chama o método “cumprimentar” na instância pessoa1 e imprime a saudação.
print(pessoa1.cumprimentar()) # Saída: “Olá, meu nome é João.”

# Acessa o atributo idade da instância pessoa1 e imprime sua idade.
print(f”Idade: {pessoa1.idade}”) # Saída: “Idade: 30”

# Chama o método “aniversário” na instância pessoa1 para aumentar sua idade em 1.
pessoa1.aniversario()

# Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade.
print(f”Nova idade: {pessoa1.idade}”) # Saída: “Nova idade: 31”
```

Nesse exemplo, criamos a classe "Pessoa" com os atributos nome, idade e gênero, bem como os métodos cumprimentar e aniversário. Depois, construímos uma instância da classe "pessoa1" e demonstramos como acessar os atributos e chamar os métodos dessa instância.

O construtor da classe `__init__()` é capaz de receber um valor diferente para cada objeto, o que é de suma importância na construção da classe. Note que nesse caso determinamos dois tipos diferentes de atributos: duas strings (nome e gênero) e um int (idade).

### Herança em Python

A herança é um dos pilares fundamentais da programação orientada a objetos, pois permite que uma classe (a classe-filha) herde características e comportamentos de outra classe (a classe-pai). Em Python, essa técnica é amplamente suportada e flexível, possibilitando que uma classe-filha herde de múltiplas classes-pai, processo que configura um conceito conhecido como herança múltipla.

A sintaxe para criar uma classe-filha que herda de uma classe-pai é simples e legível. A classe-filha é definida após o nome da classe-pai, entre parênteses.

Acompanhe, a seguir, a forma básica:

```python
class ClasseFilha(ClassePai):
    # Definição da classe-filha


class ClasseFilha(ClassePai1, ClassePai2, ClassePai3):
    # Definição da classe-filha
```

## Siga em Frente...

### Benefícios da herança

- **Reutilização de código**: a herança permite que você reutilize o código existente, aproveitando a estrutura e a funcionalidade de classes-pai em suas subclasses.
- **Extensibilidade**: você pode estender ou adicionar comportamentos específicos às classes-filhas sem modificar as classes-pai, mantendo a coesão e a organização do código.
- **Hierarquia de classes**: é possível criar uma hierarquia de classes na qual classes-filhas podem herdar características comuns de classes-pai e, por sua vez, serem herdadas por outras classes.

Imagine um cenário no qual tenhamos uma classe-pai chamada "Animal" com atributos e métodos gerais para representar qualquer animal. Podemos criar classes-filhas, como "Cachorro" e "Gato," que herdam essas características gerais, mas que também podem ter comportamentos específicos, como latir e miar, respectivamente. Dessa forma, aproveitamos a reutilização de código e estendemos funcionalidades de acordo com a necessidade.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return “Latir”

class Gato(Animal):
    def fazer_barulho(self):
        return “Miar”


# Criando objetos das classes-filhas
rex = Cachorro(“Rex”)
whiskers = Gato(“Whiskers”)

# Chamando o método fazer_barulho em objetos
print(f”{rex.nome} faz: {rex.fazer_barulho()}”) # Saída: “Rex faz: Latir”
print(f”{whiskers.nome} faz: {whiskers.fazer_barulho()}”) # Saída: “Whiskers faz: Miar”
```

Nesse exemplo, criamos objetos "rex" e "whiskers" das classes-filhas "Cachorro" e "Gato", respectivamente. Em seguida, chamamos o método `fazer_barulho()` em cada objeto para determinar o som que cada animal faz. Isso ilustra a herança em ação, quando as classes-filhas herdam o método da classe-pai, mas podem fornecer suas próprias implementações.

## Vamos Exercitar?

Agora é a hora de criar nossa classe e fazer a aplicação dos conhecimentos obtidos nesta aula. Vamos lá! Primeiro, devemos trazer as características (atributos) da classe veículo: marca, modelo e ano. Para os métodos, vamos adicionar a velocidade a partir da aceleração e diminuir a velocidade por meio da frenagem. Por fim, mostraremos os atributos e a velocidade atual do veículo.

```python
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f”Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h”


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        # Carros podem acelerar mais rápido.
        self.velocidade += incremento + self.potencia


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f”Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} km/h”


# Criando objetos
carro1 = Carro(“Toyota”, “Corolla”, 2022, 150)
bicicleta1 = Bicicleta(“Trek”, “Mountain Bike”, 2021, “MTB”)


# Acelerando e verificando o status
carro1.acelerar(50)
bicicleta1.acelerar(20)


# Exibindo o status dos veículos
print(“Status do Carro:”)
print(carro1.status())


print(“\nStatus da Bicicleta:”)
print(bicicleta1.status())
```

Temos a classe-pai "Veiculo", com atributos e métodos gerais; a classe-filha "Carro", que herda de "Veiculo" e inclui a potência no método de aceleração; e a classe-filha "Bicicleta", que herda de "Veiculo" e inclui o tipo no método de status. Criamos objetos de carros e bicicletas, e demonstramos como eles podem herdar atributos e métodos da classe-pai, enquanto as classes-filhas podem fornecer suas próprias implementações.

Gostou dessa solução? Espero que sim! Rode esse código no colab, faça modificações e "brinque" com ele. Lembre-se de que a prática é extremamente importante para alcançar melhorias.

## Saiba mais

1. O livro *Introdução à computação usando Python: um foco no desenvolvimento de aplicações* apresenta uma introdução à programação, ao desenvolvimento de aplicações de computador e à ciência da computação. Logo, para você, que está iniciando seu aprendizado em Python, essa obra representa uma leitura importante.
   > PERKOVIC, L. **Introdução à computação usando Python: um foco no desenvolvimento de aplicações**. Rio de Janeiro: LTC, 2016.

2. Outra leitura interessante para quem está começando a programar em Python é a do livro *Começando a programar em Python para leigos*.
   > MUELLER, J. P. **Começando a programar em Python para leigos**. Rio de Janeiro: Alta Books, 2020. E-book.

3. Por fim, outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. **Use a Cabeça! Python**. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

## Referências

- 9. CLASSES. Python 3.12.2 Documentation, 8 fev. 2020. Disponível em: https://docs.python.org/pt-br/3/tutorial/classes.html. Acesso em: 25 out. 2023.
- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- GOOGLE COLAB. Página inicial, [s. d.]. Disponível em: https://colab.research.google.com/. Acesso em: 25 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- MUELLER, J. P. Começando a programar em Python para leigos. Rio de Janeiro: Alta Books, 2020. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555202298. Acesso em: 12 out. 2023.
- PERKOVIC, L. Introdução à computação usando Python: um foco no desenvolvimento de aplicações. Rio de Janeiro: LTC, 2016.
