# Aula 2 — Desenvolvimento Mobile com Python e KivyMD

## Ponto de Partida

O desenvolvimento móvel revoluciona a maneira como interagimos com a tecnologia, oportunizando a criação de aplicativos que transformam nossos dispositivos em ferramentas poderosas.

O **KivyMD** emerge como um recurso robusto para o desenvolvimento móvel em Python, oferecendo uma gama diversificada de widgets e mecanismos inspirados no Material Design. Essa biblioteca dinâmica capacita desenvolvedores para a construção de aplicativos móveis visualmente atraentes, mantendo a flexibilidade e a eficiência.

Ao adotar o **MDTabs** no KivyMD, a organização estruturada de interfaces móveis ganha destaque. A utilização inteligente de widgets e abas simplifica a navegação do usuário, fornecendo uma base sólida para elaborar aplicações móveis intuitivas e eficazes.

> Para contextualizar sua aprendizagem, imagine a seguinte situação: você foi designado para desenvolver uma calculadora. A princípio, você deve replicar uma versão comum, mas, posteriormente, precisará modificá-la e criar novas funcionalidades.

## Vamos Começar!

### Introdução ao desenvolvimento mobile

O desenvolvimento mobile refere-se à criação de aplicativos para dispositivos móveis, como smartphones e tablets. Enquanto muitos desenvolvedores associam o desenvolvimento mobile a linguagens nativas específicas de plataformas – como Swift, para iOS, e Kotlin/Java, para Android –, o uso de Python tem ganhado popularidade por causa de sua versatilidade e facilidade de aprendizado.

A linguagem Python, com sua sintaxe clara e concisa, oferece uma abordagem diferenciada para o desenvolvimento mobile. Frameworks notáveis, como **Kivy**, **BeeWare** e o recente **Flutter** com suporte para Python, permitem aos desenvolvedores criar aplicativos atraentes e funcionais usando a Python como linguagem principal.

O Kivy é uma opção poderosa para o desenvolvimento mobile em Python, pois apresenta uma estrutura robusta para construir interfaces gráficas multitouch. Com suporte para várias plataformas, incluindo Android e iOS, o Kivy simplifica o processo de criação de aplicativos visualmente impressionantes, promovendo a reutilização de código entre diferentes sistemas operacionais.

Ao optar pela Python no desenvolvimento mobile, os desenvolvedores podem aproveitar os benefícios de uma comunidade ativa, uma vasta biblioteca de módulos e a agilidade proporcionada pela linguagem. No entanto, é importante estar ciente dos prováveis desafios, como o desempenho comparado a linguagens nativas e possíveis limitações de acesso a recursos específicos do dispositivo.

O uso de Python no desenvolvimento mobile abre portas para desenvolvedores que já estão familiarizados com a linguagem, possibilitando que eles ampliem seu alcance para o universo mobile. Com frameworks robustos disponíveis, a escolha entre Python e outras linguagens para desenvolvimento mobile dependerá dos requisitos específicos do projeto e das preferências da equipe de desenvolvimento.

## Siga em Frente...

### KivyMD

O KivyMD é uma extensão do Kivy, um framework Python para o desenvolvimento de aplicativos multitouch. O KivyMD estende as capacidades do Kivy ao integrar os princípios de design do Material Design do Google, concedendo uma experiência visualmente atraente e consistente em dispositivos móveis.

As principais características do KivyMD são:

- **Material Design**: o KivyMD adota os padrões de design do Material Design, oferecendo uma interface de usuário moderna, consistente e intuitiva, a qual inclui elementos como botões flutuantes, barras de navegação e efeitos de transição.
- **Componentes prontos para uso**: o framework fornece uma variedade de componentes prontos para uso, como botões, caixas de diálogo, cartões e muitos outros recursos. Esses componentes seguem as diretrizes do Material Design, otimizando a criação de interfaces visualmente atraentes.
- **Suporte a múltiplas plataformas**: assim como o Kivy, o KivyMD é multiplataforma, permitindo que os aplicativos sejam executados em diferentes sistemas operacionais, incluindo Android, iOS, Windows, Linux e macOS.

### Widgets e organização de telas utilizando o MDTabs

Os widgets desempenham um papel fundamental no desenvolvimento de interfaces de usuário interativas. No contexto do KivyMD (Material Design Components for Kivy), os widgets são blocos de construção essenciais para criar aplicativos visualmente atraentes.

O `MDTabs` é um widget poderoso do KivyMD projetado para facilitar a organização de conteúdo em diferentes abas. Isso é particularmente útil quando você precisa exibir várias seções ou funcionalidades em um aplicativo sem sobrecarregar a tela principal.

```python
# Instalação do KivyMD
!pip install kivymd

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem


Builder.load_string('''
<TabsLayout>:
    TabbedPanel:
        do_default_tab: False
        TabbedPanelItem:
            text: 'Tab 1'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Content for Tab 1'
        TabbedPanelItem:
            text: 'Tab 2'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Content for Tab 2'
''')


class TabsLayout(BoxLayout):
    pass


class TabsApp(App):
    def build(self):
        return TabsLayout()


if __name__ == '__main__':
    TabsApp().run()
```

Esse é um exemplo básico de um aplicativo Kivy com guias. O conteúdo de cada guia é um simples rótulo, mas você pode personalizá-lo e expandi-lo conforme necessário, para atender aos requisitos do seu aplicativo. Esse código foi rodado utilizando-se o Jupyter Notebook. O Google Colab não consegue gerar o aplicativo!

## Vamos Exercitar?

Vamos pensar no problema apresentado no início desta aula. Devemos criar o aplicativo de uma calculadora! Nesse caso, vamos usar novamente o Jupyter Notebook.

```python
!pip install kivymd

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

KV = '''
<CalculatorApp>:
    orientation: 'vertical'
    MDTextField:
        id: input_field
        hint_text: "Insira um número"
        helper_text_mode: "on_focus"
        input_filter: "float"
    GridLayout:
        cols: 4
        spacing: dp(10)
        MDRaisedButton:
            text: "1"
            on_press: app.on_number_press(1)
        MDRaisedButton:
            text: "2"
            on_press: app.on_number_press(2)
        MDRaisedButton:
            text: "3"
            on_press: app.on_number_press(3)
        MDRaisedButton:
            text: "+"
            on_press: app.on_operator_press("+")
        MDRaisedButton:
            text: "4"
            on_press: app.on_number_press(4)
        MDRaisedButton:
            text: "5"
            on_press: app.on_number_press(5)
        MDRaisedButton:
            text: "6"
            on_press: app.on_number_press(6)
        MDRaisedButton:
            text: "-"
            on_press: app.on_operator_press("-")
        MDRaisedButton:
            text: "7"
            on_press: app.on_number_press(7)
        MDRaisedButton:
            text: "8"
            on_press: app.on_number_press(8)
        MDRaisedButton:
            text: "9"
            on_press: app.on_number_press(9)
        MDRaisedButton:
            text: "*"
            on_press: app.on_operator_press("*")
        MDRaisedButton:
            text: "C"
            on_press: app.clear_input()
        MDRaisedButton:
            text: "0"
            on_press: app.on_number_press(0)
        MDRaisedButton:
            text: "="
            on_press: app.calculate_result()
        MDRaisedButton:
            text: "/"
            on_press: app.on_operator_press("/")
'''

class CalculatorApp(BoxLayout):
    def on_number_press(self, number):
        current_text = self.ids.input_field.text
        new_text = f{current_text}{number}
        self.ids.input_field.text = new_text

    def on_operator_press(self, operator):
        current_text = self.ids.input_field.text
        new_text = f{current_text} {operator} "
        self.ids.input_field.text = new_text

    def clear_input(self):
        self.ids.input_field.text =

    def calculate_result(self):
        try:
            result = eval(self.ids.input_field.text)
            self.ids.input_field.text = str(result)
        except Exception as e:
            self.ids.input_field.text =

class CalculatorMDApp(MDApp):
    def build(self):
        return CalculatorApp()

    def on_number_press(self, number):
        self.root.on_number_press(number)

    def on_operator_press(self, operator):
        self.root.on_operator_press(operator)

    def clear_input(self):
        self.root.clear_input()

    def calculate_result(self):
        self.root.calculate_result()

if __name__ == :
    Builder.load_string(KV)
    CalculatorMDApp().run()
```

Por meio desse código, criamos uma calculadora! Maneiro, não é? Agora, faça modificações e deixe a calculadora da forma que você achar melhor.

Espero que você tenha gostado da solução! Lembre-se de que a prática é importante! Mude alguma parte do código e diversifique seu conhecimento!

## Saiba mais

1. Kivy é uma biblioteca usada para o desenvolvimento de software com código-fonte aberto, voltado ao rápido desenvolvimento de aplicações que utilizam novas interfaces de usuário. Para saber mais detalhes, visite: https://python.org.br/mobile/.

2. Como mencionado anteriormente, uma leitura interessante para quem está começando a programar em Python é a do livro *Python 3: conceitos e aplicações: uma abordagem didática*.
   > BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. https://integrada.minhabiblioteca.com.br/#/books/9788536530253

3. Também encorajo você a conhecer o livro *Fundamentos de desenvolvimento mobile*, que apresenta conceitos e aplicações para mobile.
   > MORAIS, M. S. de F. et al. Fundamentos de desenvolvimento mobile. Porto Alegre: Grupo A, 2022. https://integrada.minhabiblioteca.com.br/#/books/9786556903057

## Referências

- BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/books/9788536530253. Acesso em: 21 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- MORAIS, M. S. de F. et al. Fundamentos de desenvolvimento mobile. Porto Alegre: Grupo A, 2022. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786556903057. Acesso em: 21 out. 2023.
- PYTHON para desenvolvimento mobile. Python Brasil, 3 jun. 2016. Disponível em: https://python.org.br/mobile/. Acesso em: 15 nov. 2023.
