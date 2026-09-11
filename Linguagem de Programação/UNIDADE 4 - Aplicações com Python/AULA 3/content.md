# Aula 3 — Testes em Python: Assertions, Doctests e Unittest

## Ponto de Partida

Os testes em Python desempenham um papel fundamental no desenvolvimento de softwares, garantindo que o código seja robusto, confiável e atenda aos requisitos esperados. Existem várias abordagens e ferramentas pelas quais é possível realizar testes, proporcionando uma cobertura completa das funcionalidades do programa.

As **assertions** são utilizadas para verificar condições essenciais durante a execução do código. São cruciais para a detecção precoce de bugs, bem como para a garantia da consistência do código.

Os **doctests** oferecem uma abordagem única, incorporando testes diretamente na documentação do código-fonte. Isso não apenas fornece exemplos de uso atualizados na documentação, mas também serve como uma verificação automatizada para assegurar que os exemplos apresentados estejam corretos.

O **unittest** é uma estrutura mais abrangente para testes em Python. Ele permite a organização de testes em classes e métodos, facilitando a manutenção e a execução seletiva de testes. As assertions fornecidas pelo unittest são mais robustas, oferecendo uma ampla gama de verificações. Esse mecanismo é ideal para projetos maiores, nos quais uma estrutura de teste mais formal é necessária para garantir a qualidade do código.

> Para ter domínio sobre os testes que serão estudados nesta aula, suponha que você precise criar uma função que calcule a soma de uma lista de número e, em seguida, deva aplicar os três testes mencionados para saber se a função está correta.

## Vamos Começar!

### Assertions

As assertions são expressões utilizadas para verificar as condições de verdade durante a execução do código. Elas são fundamentais para a detecção precoce de erros, assegurando que as suposições sobre o comportamento do programa sejam atendidas. Confira, a seguir, um exemplo simples de como as assertions podem ser empregadas:

```python
def divide(x, y):
    assert y != 0,
    return x / y


result = divide(6, 0)
print(result) # AssertionError: Divisão por zero!
```

O código cria uma função divisão, a qual, como bem sabemos, tem uma particularidade: a divisão por zero. Nesse caso, o algoritmo avisa sobre o erro.

### Doctests

O `doctest` é um módulo em Python que permite incorporar testes diretamente na documentação do código, aproveitando os exemplos presentes na documentação para verificar se o código funciona conforme o esperado. Vamos considerar o seguinte trecho de código com doctests:

```python
def square(x):
    Retorna o quadrado de um número.

    Exemplos:
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    """
    return x * x

import doctest
doctest.testmod()
```

```text
TestResults(failed=0, attempted=3)
```

A função `square` é acompanhada por uma string de documentação que inclui exemplos de uso. Esses exemplos estão formatados de maneira especial, usando o prompt `>>>`, que indica um bloco de código Python.

Quando você executa `doctest.testmod()`, o módulo doctest procura todas as strings de documentação no seu código que contenham blocos de código `>>>` e executa esses blocos como testes. Ele compara a saída real desses blocos com o resultado esperado fornecido nos comentários.

No caso do exemplo anterior, `doctest.testmod()` executará a função `square(3)` e verificará se o resultado é igual a 9, executará `square(-2)` e verificará se o resultado é 4, e assim por diante.

Se todos os testes passarem, o doctest não produzirá nenhuma saída. Se houver uma discrepância entre a saída real e a esperada, o doctest imprimirá uma mensagem indicando onde ocorreu o problema.

A principal vantagem do doctest é que ele permite que você mantenha exemplos na documentação e, ao mesmo tempo, os utilize como testes automatizados. Isso ajuda a garantir que a documentação esteja sempre em sincronia com o código real. Além disso, quando você executa os testes, obtém uma validação automática dos exemplos apresentados na documentação.

## Siga em Frente...

### Módulo unittest

O módulo `unittest` disponibiliza uma estrutura de teste mais avançada, viabilizando a organização de testes em classes e métodos, além de fornecer assertions mais poderosas. Confira, a seguir, um exemplo simples de uso do unittest:

```python
import unittest


def add(a, b):
    return a + b


class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == '__main__':
    import unittest
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

print()
```

A função `add` simplesmente soma dois números e cria uma classe que herda de `unittest.TestCase`. Isso indica que essa classe contém testes unitários. Dentro da classe de teste, você define métodos de teste. Cada método de teste deve começar com a palavra-chave `test`. Dentro desses métodos, você usa assertivas (como `self.assertEqual`) para verificar se o comportamento esperado do código é atendido. A condição `if __name__ == '__main__':` garante que a suíte de testes seja executada somente se o script for executado diretamente (não se for importado como um módulo em outro script). `unittest.main()` executa todos os testes definidos na classe `TestAddition`.

## Vamos Exercitar?

Vamos pensar no problema apresentado no início desta aula. Para isso, considere uma função que calcula a soma de uma lista de números.

```python
# assert
def sum_numbers(numbers):
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-1, 0, 1]) == 0
    assert sum([]) == 0
    return sum(numbers)

teste = sum_numbers([1, 2, 3, 5])
print(teste)
```

```python
# doctest
def sum_numbers(numbers):
    Soma os números em uma lista.

    Exemplos:
    >>> sum_numbers([1, 2, 3, 4])
    10
    >>> sum_numbers([-1, 0, 1])
    0
    >>> sum_numbers([])
    0
    """
    return sum(numbers)


if __name__ == :
    import doctest
    doctest.testmod()
```

```python
# unittest
import unittest

def sum_numbers(numbers):
    return sum(numbers)


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)

    def test_sum_numbers_mixed(self):
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers([]), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```

Nesse código, criamos a função `sum_number`. A ideia é testar os três tipos de teste que estudamos nesta etapa de aprendizagem e aplicá-los ao caso investigado. Observe que cada situação foi resolvida de um modo distinto. O importante é sempre analisar qual a melhor solução para o problema em que estamos atuando.

Espero que você tenha gostado da solução! Lembre-se de que a prática é importante! Mude alguma parte do código e diversifique seu conhecimento!

## Saiba mais

1. Para obter mais informações sobre testes com Python, a leitura da documentação do Python é essencial.

2. Como mencionado anteriormente, uma leitura interessante para quem está começando a programar em Python é a do livro *Python 3: conceitos e aplicações: uma abordagem didática*.
   > BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book.

3. Outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. Use a cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

## Referências

- BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/books/9788536530253. Acesso em: 21 out. 2023.
- BARRY, P. Use a cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- LEMBURG, M. PEP 249 - Python database API specification v.2.0. Python Enhancement Proposals, 12 abr. 1999. Disponível em: https://peps.python.org/pep-0249/#description. Acesso em: 31 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- UNITTEST – Unit testing framework. Python 3.12.2 Documentation, [s. d.]. Disponível em: https://docs.python.org/3/library/unittest.html. Acesso em: 16 nov. 2023.
