# Exercícios de Revisão — Unidade 4

## Questão 1 ✅

Considere o seguinte código Python que usa a biblioteca Pandas para ler dados de uma página da web:

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
max_episodes = 1000  # Defina o número máximo de episódios
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
        if average_reward == 1:  # Pode ajustar esse valor conforme necessário
            print(f'Solved after {episode} episodes!')
            break
```

**Pergunta:** Qual tipo de treinamento é feito no enunciado?

**Resposta assinalada:** Treinamento por reforço em um ambiente dinâmico. ✅

**Comentário:**
- a) Incorreta. Não há evidência de treinamento de um modelo de classificação neste exemplo.
- b) Incorreta. Este exemplo aborda treinamento por reforço, não supervisionado.
- **c) Correta. O código realiza treinamento por reforço em um ambiente dinâmico.**
- d) Incorreta. Não há evidência de agrupamento de dados neste exemplo.
- e) Incorreta. Este exemplo não aborda treinamento não supervisionado.

## Questão 2 ✅

Os tipos de treinamento são estratégias fundamentais no desenvolvimento de modelos de Machine Learning, determinando como o algoritmo aprenderá com os dados disponíveis. Cada abordagem tem características distintas e aplicações específicas, proporcionando flexibilidade para diferentes contextos.

**Pergunta:** O que caracteriza o treinamento supervisionado em Machine Learning?

**Resposta assinalada:** O modelo é alimentado com um conjunto de dados rotulado, consistindo em pares de entrada e saída esperada. ✅

**Comentário:**
- a) Incorreta. Isso caracteriza o treinamento não supervisionado.
- b) Incorreta. Isso caracteriza o treinamento por reforço.
- **c) Correta. O treinamento supervisionado envolve o modelo sendo alimentado com um conjunto de dados rotulado, consistindo em pares de entrada e saída esperada.**
- d) Incorreta. Isso caracteriza o treinamento não supervisionado.
- e) Incorreta. Isso caracteriza o treinamento por reforço.

## Questão 3 ✅

Os widgets desempenham um papel fundamental no desenvolvimento de interfaces de usuário interativas. No contexto do KivyMD (Material Design Components for Kivy), os widgets são os blocos de construção essenciais para criar aplicativos visualmente atraentes.

`MDTabs` é um widget poderoso do KivyMD projetado para facilitar a organização de conteúdo em diferentes abas. Isso é particularmente útil quando você precisa exibir várias seções ou funcionalidades em um aplicativo sem sobrecarregar a tela principal.

**Pergunta:** Qual é o papel fundamental dos widgets no desenvolvimento de interfaces de usuário interativas, conforme mencionado no texto-base?

**Resposta assinalada:** Facilitar a organização de conteúdo em diferentes abas. ✅

**Comentário:**
- a) Incorreta. O texto não menciona desenvolvimento exclusivo para dispositivos Android.
- **b) Correta. O texto destaca que o `MDTabs`, como widget do KivyMD, é projetado para facilitar a organização de conteúdo em diferentes abas.**
- c) Incorreta. O texto não menciona substituição de linguagem Python.
- d) Incorreta. O texto não sugere criar apenas interfaces simples e estáticas.
- e) Incorreta. O `MDTabs` é projetado para evitar sobrecarregar a tela principal com conteúdo.

## Questão 4 ✅

As assertions são expressões utilizadas para verificar as condições de verdade durante a execução do código. Elas são fundamentais para a detecção precoce de erros, garantindo que as suposições sobre o comportamento do programa sejam atendidas.

**Pergunta:** Qual é o papel das assertions no código apresentado e por que são consideradas fundamentais?

**Resposta assinalada:** As assertions são fundamentais para evitar erros durante a execução do código. ✅

**Comentário:**
- a) Incorreta. As assertions não são usadas para criar funções de divisão; elas são usadas para verificar condições durante a execução.
- **b) Correta. As assertions são fundamentais para evitar erros durante a execução do código, garantindo que as suposições sobre o comportamento do programa sejam atendidas.**
- c) Incorreta. As assertions não garantem que o código seja executado sem falhas; pelo contrário, elas são usadas para detectar condições de erro.
- d) Incorreta. As assertions são expressões úteis na programação para verificar condições.
- e) Incorreta. As assertions não são exclusivas para detecção de erros em loops; elas podem ser usadas em várias partes do código.

## Questão 5 ✅

Observe o código:

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

**Pergunta:** O que indica a condição `if __name__ == '__main__':` no exemplo apresentado?

**Resposta assinalada:** Garante que a suíte de testes seja executada apenas se o script for executado diretamente (não importado como módulo). ✅

**Comentário:**
- a) Incorreta. A condição `if __name__ == '__main__':` não está relacionada à definição da função `add`.
- b) Incorreta. A condição não se refere à execução da classe `TestAddition` apenas quando importada como módulo.
- c) Incorreta. A condição não está relacionada à execução da classe `TestAddition`.
- **d) Correta. A condição garante que a suíte de testes seja executada apenas se o script for executado diretamente.**
- e) Incorreta. A condição não está diretamente relacionada à chamada explícita da função `unittest.main()`.
