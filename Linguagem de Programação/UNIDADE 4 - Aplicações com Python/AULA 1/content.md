# Aula 1 — Desenvolvimento de Sistemas Web com Python

## Ponto de Partida

Python é uma linguagem de programação amplamente utilizada no desenvolvimento web, segmento que envolve a criação de aplicativos e sites para a internet. Esse processo abrange tanto o lado do cliente (**front-end**) quanto o lado do servidor (**back-end**), utilizando linguagens como HTML, CSS e JavaScript, além de frameworks como React, Django ou Flask. Nesse contexto, a linguagem Python age como um "mediador" dessas interações.

O front-end é a interface visível para os usuários. Desenvolvedores front-end utilizam HTML, CSS e JavaScript, frequentemente integrando frameworks como React, Angular ou Vue.js para criar interatividade. A Python também é utilizada, por exemplo, em projetos que envolvem a construção de interfaces usando Dash ou Flask.

O back-end é responsável pela lógica, processamento e armazenamento de dados. Desenvolvedores back-end usam linguagens como Python, Java ou Node.js, além de frameworks como Django, Flask ou Express, para criar a lógica do servidor e gerenciar interações com o banco de dados.

> Vamos imaginar que você esteja participando de um curso de desenvolvimento web e sua primeira tarefa seja criar uma página de perfil pessoal.

## Vamos Começar!

### Visão geral sobre o desenvolvimento de sistemas para a web

O desenvolvimento de sistemas para a web com Python se apresenta como uma jornada empolgante, que combina a versatilidade dessa linguagem de programação com as demandas dinâmicas da internet moderna. A linguagem Python, conhecida por sua legibilidade, facilidade de aprendizado e vasta comunidade de desenvolvedores, tem se destacado tanto no front-end quanto no back-end, oferecendo soluções abrangentes para a criação de aplicativos web robustos e eficientes.

No início, as páginas web eram estáticas e limitadas em sua interatividade. Com o tempo, a necessidade de interfaces mais dinâmicas e funcionais levou ao desenvolvimento de linguagens e frameworks voltados para a web. A Python entrou nesse cenário, inicialmente no back-end, ganhando destaque com frameworks como **Django** e **Flask**.

O desenvolvimento web é dividido principalmente em duas partes: front-end e back-end. O front-end lida com a interface do usuário, enquanto o back-end gerencia a lógica, o processamento de dados e a interação com o banco de dados. A linguagem Python é versátil o suficiente para ser utilizada em ambos os contextos (front-end e back-end), proporcionando uma integração suave e eficiente entre essas camadas.

A Python possui uma gama de frameworks e bibliotecas dedicados ao desenvolvimento web. Django, um framework full-stack, é reconhecido pela sua robustez e convenções claras. Flask, uma estrutura mais leve, é apreciada pela sua flexibilidade. Ambos os recursos são excelentes escolhas para o back-end. Além disso, bibliotecas front-end como React, Vue.js e Angular podem ser facilmente integradas à linguagem Python.

O desenvolvimento web moderno destaca a importância das **APIs** (Interfaces de Programação de Aplicações) para otimizar a comunicação entre o front-end e o back-end. A Python, com frameworks como FastAPI e Django Rest Framework, oferece soluções poderosas para criar APIs escaláveis e bem documentadas.

A tecnologia web está em constante evolução. O uso de arquiteturas sem servidor, microsserviços, containers e orquestradores como **Kubernetes** tornou-se comum. Python, com suas características de legibilidade e flexibilidade, se integra facilmente a essas tecnologias, permitindo que os desenvolvedores permaneçam atualizados com as últimas tendências dessa área.

O desenvolvimento web com Python não está isento de desafios. A escalabilidade, a segurança e a necessidade de interfaces mais ricas são considerações constantes. No entanto, esses desafios também proporcionam oportunidades para aprimorar habilidades e explorar soluções inovadoras.

Em resumo, o desenvolvimento de sistemas para a web com Python viabiliza uma abordagem completa e poderosa. Seja construindo uma aplicação web simples ou um sistema complexo, a linguagem Python proporciona ferramentas e recursos para enfrentar os desafios do desenvolvimento web moderno.

Com uma comunidade ativa e uma série de recursos disponíveis, a Python continua a ser uma escolha excelente para aqueles que querem mergulhar no mundo dinâmico do desenvolvimento web.

### Front-end e back-end

O front-end de uma aplicação web é a interface com a qual os usuários interagem diretamente. A partir de agora, vamos descobrir como criar uma experiência front-end simples usando Python no Google Colab.

O HTML é a espinha dorsal do conteúdo na web. Podemos criar elementos HTML usando Python no Colab e, em seguida, incorporá-los em nossa página.

Vamos criar uma página HTML básica:

```python
# Criando uma página HTML usando Python
html_code =

<!DOCTYPE html>
<html>
<head>
<title>Exemplo de Front-end com Python</title>
</head>
<body>
<h1>Olá, mundo!</h1>
<p>Esta é uma página web criada usando Python no Google Colab.</p>
</body>
</html>

# Exibindo a página HTML
from IPython.display import HTML
HTML(html_code)
```

```text
Olá, mundo!

Esta é uma página web criada usando Python no Google Colab.
```

Nesse exemplo, geramos uma página HTML usando uma string Python e a exibimos no Colab. Isso demonstra como podemos incorporar HTML no Colab para criar conteúdo front-end.

O back-end de uma aplicação web lida com a lógica, o processamento de dados e a interação com o servidor. Vamos entender, então, como criar um back-end simples usando Python no Google Colab.

O `Flask` é um framework web leve para Python. Embora não seja a escolha ideal para ambientes de produção no Colab, podemos usá-lo para criar um exemplo básico de servidor back-end:

```python
!ngrok authtoken 2YE2L21rdpK3IO8oTpHoTCL9z7h_xxsYeAHKwXUzQjWLZduY
# usar esse código de autenticação

# Em outra célula rodar:
!pip install flask flask-ngrok

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def index():
    return 'Olá, esta é a rota principal do back-end!'


if __name__ == '__main__':
    app.run()
```

```text
* Serving Flask app '__main__'
* Debug mode: off
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
* Running on http://e399-34-141-146-10.ngrok-free.app #muda quando rodamos de novo
* Traffic stats available on http://127.0.0.1:4040
```

A célula apresentada anteriormente cria um aplicativo Flask e o expõe publicamente usando o `ngrok` para criar um túnel. Isso permite que você acesse seu servidor Flask temporário a partir de um link gerado pelo ngrok.

Esses exemplos ilustram a integração do front-end e do back-end usando Python no Google Colab. Para projetos mais complexos, considere o uso de ambientes de desenvolvimento web dedicados, mas, para experimentação e demonstração, o Colab dispõe uma plataforma interativa e prática.

## Siga em Frente...

### Primeiras páginas web

Vamos, agora, melhorar nossa página feita com HTML no Colab!

```python
# Exemplo de HTML com botão usando Python
html_code =

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Minha Primeira Página Web</title>
<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f8f8;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .container {
        text-align: center;
        padding: 40px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    }

    h1 {
        color: #3498db;
        font-size: 2em;
        margin-bottom: 20px;
    }

    p {
        color: #555;
        font-size: 1.2em;
    }

    button {
        background-color: #3498db;
        color: #fff;
        font-size: 1.2em;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #2980b9;
    }
</style>
</head>
<body>
<div class="container">
    <h1>Olá, Mundo!</h1>
    <p>Esta é minha primeira página web criada com Python no Colab. Bem-vindo ao mundo da programação web!</p>
    <button onclick="alert('Botão clicado!')">Clique em Mim</button>
</div>
</body>
</html>

# Exibindo a página HTML
from IPython.display import HTML
HTML(html_code)
```

Alteramos as cores de fundo, texto e sombra para tornar a página mais atraente. Ajustamos o tamanho da fonte e o espaçamento para melhorar a legibilidade. Centralizamos os elementos na tela usando o Flexbox. Adicionamos uma sombra sutil e bordas arredondadas ao container para um visual mais moderno. Adicionamos um botão com um estilo básico. O botão aciona um alerta simples quando clicado.

## Vamos Exercitar?

Vamos pensar no problema apresentado no início desta aula. Imagine que você esteja participando de um curso de desenvolvimento web e sua primeira tarefa seja criar uma página de perfil pessoal.

```python
from IPython.display import HTML

html_code =

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Perfil</title>
</head>
<body style="font-family: 'Arial', sans-serif; background-color: #f8f8f8; margin: 0; padding: 0;">

    <header style="text-align: center; background-color: #3498db; color: #fff; padding: 20px;">
        <h1 style="margin: 0;">Anderson Inácio Salata de Abreu</h1>
        <p style="margin: 5px 0;">Desenvolvedor Web</p>
    </header>

    <section style="margin: 20px; text-align: center;">
        <img src="content/sua_foto.jpg" alt="Sua Foto" style="border-radius: 50%; margin-bottom: 20px;">
        <div id="informacoes-pessoais" style="max-width: 400px; margin: 0 auto;">
            <p>Cidade: Sorocaba </p>
            <p>País: Brasil</p>
            <p>Interesses: Web Development, Programação, etc.</p>
        </div>
    </section>

    <section style="margin: 20px; text-align: center;">
        <h2>Habilidades</h2>
        <ul style="list-style: none; padding: 0;">
            <li>Linguagens: Python, HTML, CSS, JavaScript</li>
            <li>Ferramentas: Git, VS Code</li>
        </ul>
    </section>

    <section style="margin: 20px; text-align: center;">
        <h2>Projeto Recente</h2>
        <p>Trabalhando em um site pessoal para mostrar meu portfólio.</p>
    </section>

    <footer style="text-align: center; margin-top: 20px;">
        <a href="https://www.linkedin.com/in/andersonsalata/" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">LinkedIn</a>
    </footer>

</body>
</html>

# Exibindo a página HTML
HTML(html_code)
```

Nesse código, criamos um site com algumas informações pessoais utilizando HTML. Além disso, como "mediador", usamos o Python no Colab!

Espero que você tenha gostado da solução! Lembre-se de que a prática é importante! Mude alguma parte do código e diversifique seu conhecimento!

## Saiba mais

1. O Jupyter Notebook fornece um ambiente no qual você pode trabalhar com facilidade o seu código na linguagem Python. Para saber mais detalhes, visite: jupyter.

2. Como mencionado anteriormente, uma leitura interessante para quem está começando a programar em Python é a do livro *Python 3: conceitos e aplicações: uma abordagem didática*.
   > BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book.

3. O Django, enquanto framework, se destaca como uma ferramenta consolidada, simplificando significativamente o processo de criação de aplicações web. Sua vantagem reside na capacidade de facilitar o desenvolvimento sem depender de um ambiente de execução robusto, concedendo, ao mesmo tempo, a flexibilidade de integração rápida com servidores compatíveis para a distribuição de aplicações de modo eficiente e descomplicado.
   > MACIEL, F. M. B. Python e Django: desenvolvimento web moderno e ágil. Rio de Janeiro: Alta Book, 2018. E-book.

## Referências

- BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/books/9788536530253. Acesso em: 21 out. 2023.
- MACIEL, F. M. B. Python e Django: desenvolvimento web moderno e ágil. Rio de Janeiro: Alta Book, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555200973. Acesso em: 21 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- TERUEL, E. C. HTML 5: guia prático. São Paulo: Érica, 2013. E-book.
- TRY JUPYTER. Jupyter, [s. d.]. Disponível em: https://jupyter.org/try. Acesso em: 15 nov. 2023.
