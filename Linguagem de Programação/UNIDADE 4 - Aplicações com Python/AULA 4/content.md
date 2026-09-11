# Aula 4 — Machine Learning e a Biblioteca TensorFlow

## Ponto de Partida

**Machine learning (ML)** é um campo da inteligência artificial que se concentra no desenvolvimento de algoritmos e modelos que permitem que um sistema aprenda padrões a partir de dados e faça previsões ou tome decisões mesmo que não seja explicitamente programado para tal. Em vez de seguir instruções específicas, os modelos de ML são alimentados com dados e ajustam seus parâmetros para que se adaptem da melhor maneira possível a esses dados. Tal método de aprendizado possibilita que os modelos generalizem e tomem decisões em novos dados.

No processo de machine learning, o treinamento é crucial para permitir que o modelo aprenda padrões com base nos dados. Existem vários tipos de treinamento, cada um com características distintas.

**TensorFlow** é uma biblioteca de código aberto desenvolvida pela Google que facilita a implementação de modelos de machine learning e deep learning.

Sua estrutura flexível viabiliza a criação e o treinamento de modelos complexos, sendo amplamente utilizada na comunidade de aprendizado de máquina.

> **Desafio da aula:** imagine que você seja o gerente de uma pequena loja que vende produtos exclusivos. Ao analisar o histórico de vendas ao longo de um ano, você percebeu que as vendas variam à medida que os meses se passam. Para tomar decisões mais informadas sobre o estoque e as estratégias de marketing, você opta por explorar a possibilidade de prever as vendas futuras.

## Vamos Começar!

### Teoria de machine learning

Machine learning (ML) – Aprendizado de Máquina, em português – é um campo da inteligência artificial que se concentra no desenvolvimento de algoritmos e modelos capazes de aprender padrões a partir de dados. O propósito central do ML é capacitar computadores para que realizem tarefas específicas mesmo que não sejam explicitamente programados para tais ações, permitindo que eles evoluam e melhorem com a experiência. O processo de aprendizado envolve a exposição a conjuntos de dados, nos quais o sistema identifica padrões, correlações e regras, preparando-se para realizar previsões ou tomar decisões em novos dados.

Existem diversas abordagens no campo de ML, como: **aprendizado supervisionado**, em que o modelo é treinado com dados rotulados; **aprendizado não supervisionado**, no qual o modelo busca por padrões em dados não rotulados; e o **aprendizado por reforço**, em que o modelo interage com um ambiente dinâmico, aprendendo com as recompensas obtidas. O machine learning tem aplicações abrangentes, que envolvem desde o reconhecimento de imagens até a tomada de decisões complexas em setores como finanças e saúde. Trata-se de um campo em constante evolução, impulsionado por avanços tecnológicos e pela crescente disponibilidade de dados, tornando-se uma ferramenta essencial em diversas áreas.

Alguns dos modelos e algoritmos de ML mais utilizados são:

1. **Árvores de decisão**: modelo que toma decisões com base em condições.
2. **Redes neurais**: inspiradas no funcionamento do cérebro, são usadas para problemas complexos.
3. **Support Vector Machine (SVM)**: usado para classificação e regressão.
4. **K-Means**: algoritmo de agrupamento utilizado no aprendizado não supervisionado.

### Tipos de treinamento

Os tipos de treinamento são estratégias fundamentais no desenvolvimento de modelos de machine learning, pois determinam como o algoritmo aprenderá com os dados disponíveis. Cada abordagem tem características distintas e aplicações específicas, proporcionando flexibilidade para diferentes contextos.

No **treinamento supervisionado**, o modelo é alimentado com um conjunto de dados rotulado, que consiste em pares de entrada e saída esperadas. O objetivo é que o modelo aprenda a mapear entradas para saídas corretas. Um exemplo prático pode ser observado na classificação de e-mails como "spam" ou "não spam".

Ao contrário do supervisionado, o **treinamento não supervisionado** lida com dados não rotulados. O modelo é desafiado a encontrar padrões e estruturas intrínsecas aos dados sem informações prévias sobre as saídas. Como exemplo prático, podemos citar o agrupamento de clientes com base em padrões de compra.

O **treinamento por reforço** envolve um agente interagindo com um ambiente dinâmico. O modelo aprende a realizar ações que maximizem as recompensas ao longo do tempo. Exemplo prático: treinar um agente de IA para jogar um jogo e ganhar pontos ao realizar as ações corretas.

## Siga em Frente...

### TensorFlow

`TensorFlow` é uma biblioteca de código aberto desenvolvida pela Google que facilita a implementação de modelos de machine learning e deep learning. Sua estrutura flexível permite a criação e o treinamento de modelos complexos, sendo amplamente utilizada na comunidade de aprendizado de máquina.

A seguir, vamos analisar três exemplos dessa biblioteca: uma para treinamento supervisionado, outro para treinamento não supervisionado e, por fim, um para treinamento por reforço.

#### Supervisionado

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dados de exemplo
X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Treinamento do modelo
model.fit(X_train, y_train, epochs=1000, verbose=0)

# Previsão
X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)
print(“Predição:”, prediction[0][0])

plt.ylabel('Notas')
plt.show()
```

#### Não supervisionado

```python
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Dados de exemplo
X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

# Modelo Autoencoder Simples
input_layer = Input(shape=(2,))
encoded = Dense(units=1)(input_layer)
decoded = Dense(units=2)(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento do modelo não supervisionado
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

# Previsão
prediction_unsupervised = autoencoder.predict(X_unsupervised)
print(“Predição Não Supervisionada:”, prediction_unsupervised)
```

#### Por reforço

```python
import tensorflow as tf
import gym

# Ambiente CartPole do Gym
env = gym.make('CartPole-v1')

# Modelo Simples para Aprendizado por Reforço
model_reinforcement = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

model_reinforcement.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Treinamento por Reforço (exemplo fictício)
max_episodes = 1000 # Defina o número máximo de episódios
for episode in range(max_episodes):
    state = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        next_state, reward, done, _ = env.step(action)
        target = reward + 0.95 * tf.reduce_max(model_reinforcement.predict(next_state.reshape(1, -1)))
        target_f = model_reinforcement.predict(state.reshape(1, -1))
        target_f[0][action] = target
        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)
        state = next_state

    # Condição de parada
    if episode % 10 == 0:
        average_reward = sum(reward for _ in range(10)) / 10.0
        print(f'Episode {episode}, Average Reward: {average_reward}')

        # Adicionando uma condição de parada
        if average_reward == 1: # Pode ajustar esse valor conforme necessário
            print(f'Solved after {episode} episodes!')
            break
```

## Vamos Exercitar?

Vamos pensar no problema apresentado no início desta aula. Para isso, criaremos um modelo de previsão.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

# Crie dados fictícios de vendas ao longo do tempo
np.random.seed(42)
meses = np.arange(1, 13)
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])

# Crie um DataFrame
dados = pd.DataFrame({'Mes': meses, 'Vendas': vendas})

# Visualize os dados
plt.scatter(dados['Mes'], dados['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Dados de Vendas ao Longo do Tempo')
plt.show()

# Normalização dos dados de treinamento
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Divida os dados em conjunto de treinamento e teste
X = dados[['Mes']]
y = dados['Vendas']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crie e treine o modelo de regressão linear usando TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)), # Camada de entrada
    tf.keras.layers.Dense(units=8, activation='relu'), # Camada escondida com ativação ReLU
    tf.keras.layers.Dense(units=1) # Camada de saída
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Treine o modelo por mais épocas
model.fit(X_train, y_train, epochs=500, verbose=0)

# Faça previsões no conjunto de teste
predictions = model.predict(X_test)

# Desfaça a normalização para avaliar o desempenho
min_sales = dados['Vendas'].min()
max_sales = dados['Vendas'].max()

predictions_inverse = predictions * (max_sales - min_sales) + min_sales
y_test_inverse = y_test * (max_sales - min_sales) + min_sales

# Visualize as previsões em relação aos dados reais
plt.scatter(X_test, y_test_inverse, label='Dados Reais')
plt.plot(X_test, predictions_inverse, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsões de Vendas com Regressão Linear (TensorFlow)')
plt.legend()
plt.show()

# Avalie o desempenho do modelo
erro_mse = mean_squared_error(y_test_inverse, predictions_inverse)
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

# Faça uma previsão para o próximo mês
proximo_mes_scaled = scaler.transform(np.array([[13]]))
previsao_proximo_mes_scaled = model.predict(proximo_mes_scaled)
previsao_proximo_mes = scaler.inverse_transform(previsao_proximo_mes_scaled)[0, 0]
print(f'Previsão de Vendas para o Próximo Mês: {previsao_proximo_mes:.2f}')
```

Utilizamos um modelo de treinamento supervisionado e criamos a previsão de venda para o próximo ano. Lembre-se de que para esse caso empregamos dados fictícios, porém a ideia a ser considerada para o desenvolvimento de outras construções é semelhante.

Espero que você tenha gostado da solução! Lembre-se de que a prática é importante! Mude alguma parte do código e diversifique seu conhecimento!

## Saiba mais

1. Na obra indicada para leitura a seguir, você terá contato com os primeiros conceitos de ciência de dados (data science) e ainda reforçará seu conhecimento sobre machine learning. Para acessar o conteúdo recomendado, clique no link a seguir.
   > AMÍLCAR NETTO; MACIEL, F. **Python para data science e machine learning descomplicado**. Rio de Janeiro: Alta Books, 2021. E-book.

2. Como mencionado anteriormente, uma leitura interessante para quem está começando a programar em Python é a do livro *Python 3: conceitos e aplicações: uma abordagem didática*.
   > BANIN, S. L. **Python 3: conceitos e aplicações: uma abordagem didática**. São Paulo: Érica, 2018. E-book.

3. Também encorajo você a conhecer a comunidade do TensorFlow, que, como já disse, é altamente rica em informações e aplicações dessa biblioteca. Para saber mais detalhes, visite: TensorFlow.

## Referências

- AMÍLCAR NETTO; MACIEL, F. Python para data science e machine learning descomplicado. Rio de Janeiro: Alta Books, 2021. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555203172/. Acesso em: 21 out. 2023.
- BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/books/9788536530253. Acesso em: 21 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- TENSORFLOW. Página inicial, [s. d.]. Disponível em: https://www.tensorflow.org/?hl=pt-br. Acesso em: 16 nov. 2023.
