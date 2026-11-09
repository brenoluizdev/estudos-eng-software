# Aula 1 — Fundamentos da Análise e Modelagem de Sistemas

## Ponto de Partida

Trabalhar na área de análise de sistemas é sempre desafiador, pois um sistema nunca é igual ao outro e há constantes novidades advindas do emprego de tecnologias diferentes. Nesse universo, são necessários organização e muito empenho para produzir um software de qualidade.

Os **sistemas** são conjuntos de componentes inter-relacionados, trabalhando juntos para coletar, processar, armazenar e disseminar informações. Eles são fundamentais para entender como as informações são gerenciadas e utilizadas nas organizações. As características essenciais dos sistemas incluem a interconexão de partes, a existência de um objetivo ou propósito, a capacidade de processamento de dados e informações, e a interação com o ambiente. Compreender esses conceitos básicos é crucial para a análise, o design e a implementação eficazes de sistemas de informação, pois oferecem a base para a identificação de problemas e a busca de soluções tecnológicas apropriadas.

A **análise de sistemas** envolve a investigação detalhada de sistemas existentes ou propostos para determinar as necessidades e objetivos do usuário e desenvolver soluções estratégicas. Esses princípios incluem entender as necessidades dos usuários, identificar e resolver problemas, desenhar soluções eficazes e eficientes, e garantir a adaptabilidade e escalabilidade do sistema. O conhecimento desses princípios é vital para desenvolver sistemas que não apenas atendam aos requisitos atuais, mas também sejam flexíveis o suficiente para se adaptar às necessidades futuras.

O **analista de sistemas** é um profissional crucial na ponte entre a tecnologia e as necessidades de negócios de uma organização. Eles são responsáveis por compreender os requisitos do negócio e traduzi-los em especificações técnicas para o desenvolvimento de sistemas de informação. Isso inclui a realização de análises de requisitos, a proposição de soluções, o acompanhamento do desenvolvimento do software e a garantia de que o produto final atenda às expectativas do cliente. O papel de um analista de sistemas é fundamental para garantir que os recursos de TI sejam usados de maneira eficiente e eficaz, contribuindo para o sucesso operacional e estratégico da organização.

> Pensando nesses conceitos, suponha que você foi convidado a trabalhar como analista de sistemas em uma *software house* (empresa de desenvolvimento de sistemas) e sua primeira missão é analisar um software de um possível cliente. A empresa de desenvolvimento precisa de novas ideias para sugerir ao cliente e, quem sabe, conseguir fechar um contrato de desenvolvimento.
>
> O cliente possui uma rede de postos de coleta de exames laboratoriais no Sul do país. Sabe-se que o sistema utilizado atualmente, um desktop sem acesso à internet, já possui quase 15 anos de uso e nunca foi atualizado. Como a empresa pensa, agora, em atualizá-lo, sua missão será descobrir:
>
> 1. É mais viável atualizar o sistema existente ou criar um novo?
> 2. Quais as novas tecnologias que podem ser utilizadas em um novo sistema para uma empresa de exames laboratoriais?
> 3. Quais processos deverão ser adotados para manter o software sempre atualizado?
> 4. Qual o perfil dos profissionais envolvidos no processo da análise do sistema do cliente?
>
> Crie um relatório com as soluções encontradas para gerar um debate sobre suas ideias.

---

## Vamos Começar!

### Conceitos básicos de sistemas e suas características

Na era moderna, o uso de softwares se tornou extremamente difundido em vários aspectos da vida. Hoje em dia, é normal que as empresas exijam que seus empregados tenham competência em softwares específicos, ou providenciem treinamento para seu uso, visto que softwares são frequentemente empregados em atividades cotidianas.

Sommerville (2018) define **softwares** como *"programas de computador acompanhados de documentação associada"*, e esclarece que eles podem ser criados para clientes específicos ou para um público mais amplo. Por outro lado, Pressman (2021) descreve softwares de computador como produtos desenvolvidos e mantidos a longo prazo por profissionais de Tecnologia da Informação (TI). Ele também destaca que softwares englobam qualquer forma de mídia eletrônica e são constituídos por três elementos principais:

| Elemento | Descrição |
|---|---|
| **Instruções** | Quando executadas, fornecem os atributos e funções de desempenho desejados pelos usuários. |
| **Estruturas de dados** | Possibilitam aos programadores manipular as informações de forma mais adequada conforme a necessidade da aplicação. |
| **Documentação** | Toda a informação descritiva do software, a qual detalha a operação de uso dos programas, diagramas de funcionalidades, etc. |

Deve-se destacar que o desenvolvimento do software não ocorreu instantaneamente; ele foi fruto de uma evolução contínua, cujo conhecimento é fundamental para todos os profissionais de Tecnologia da Informação. No Quadro 1, é apresentada uma linha do tempo que ilustra a história e a evolução do software, incluindo os eventos mais significativos que marcaram essa trajetória.

#### Quadro 1 — Cronologia histórica da evolução do software

| Quando? | O quê? | Descrição |
|---|---|---|
| **Década de 1940** | Programa | O programa era executável e tinha controle total sobre o computador, sendo que o software era responsável por todo o funcionamento tanto do hardware (Sistema Operacional) quanto das operações matemáticas que teria que fazer. |
| **Décadas de 1950 e 1960** | Sistemas operacionais | Responsáveis pelo controle do hardware (realizavam a interface entre o homem e a máquina). |
| | Linguagens de programação | Surgem as linguagens de programação: COBOL, LISP, ALGOL, BASIC etc. |
| **Décadas de 1960 e 1970** | Crise do software | Houve um grande crescimento do número de sistemas e quase não havia planejamento e controle de processos de desenvolvimento de software. Devido ao desenvolvimento informal, havia atrasos e os custos superavam o orçamento estimado (surgindo a necessidade de criar métodos de engenharia de software). |
| | Paradigmas de programação | Com novas linguagens sendo criadas, nessa época o conceito de orientação a objetos é criado. |
| | Sistemas operacionais mais eficientes | O foco, no momento, era a programação desktop, de modo que foi quando surgiram o MS-DOS da Microsoft e o Macintosh da Apple. |
| **Década de 1980** | Computador desktop | A década foi marcada pelo surgimento da Microsoft e pela evolução dos computadores pessoais — desktop. |
| | Unix | O Unix (sistemas operacionais em rede) avançou pelo mundo. |
| | Evolução da internet | A internet começa a despontar como meio de comunicação. |
| **Década de 1990** | Internet | A internet é amplamente utilizada. |
| | Linux | Surge o núcleo do futuro Linux. |
| | JAVA | Nasce a linguagem JAVA, que revoluciona o paradigma da orientação a objetos. |
| **Década de 2000** | Sistemas operacionais gráficos | Geração do Windows da Microsoft (Windows XP, Windows Vista, Windows 7) e versões gráficas do LINUX. |
| | Internet | Softwares que utilizam a web como plataforma de funcionamento. |
| **Décadas de 2010 e 2020** | Computação em nuvem | Utilizada em larga escala por diversos segmentos de empresas. |
| | Aplicativos para dispositivos móveis | Com a evolução dos dispositivos móveis os softwares para aplicativos tornaram-se essenciais. |
| | Inteligência Artificial | Utilização de algoritmos para *Deep Learning* (aprendizagem profunda) e *Machine Learning* (aprendizado de máquina). |

> *Fonte: adaptado de Fonseca Filho (2007).*

Conforme apresentado no Quadro 1, é notável que, com a evolução e maior acessibilidade do hardware e software, cresce a urgência de aprimorar os softwares. Paralelamente, as exigências dos consumidores evoluem com a disponibilidade de novas tecnologias. Vejamos alguns exemplos:

- **Anos 90:** uma empresa geralmente precisava de um software e, possivelmente, de um site na internet para ganhar visibilidade. O site funcionava principalmente como um cartão de visitas virtual.
- **Década de 2000:** a necessidade evoluiu para um software com capacidade de conexão à internet, permitindo oferecer mais recursos aos clientes.
- **2010:** tornou-se essencial que a empresa dispusesse de um software, um site e um aplicativo móvel, facilitando o acesso a seus serviços em diferentes dispositivos e o armazenamento de dados na nuvem.
- **A partir de 2020:** muitas empresas começaram a explorar o uso da Inteligência Artificial para otimizar seus processos de gestão.

Esses desenvolvimentos demonstram claramente que, à medida que novas tecnologias ganham popularidade, aumenta a demanda por software sofisticado para atender às necessidades em constante mudança da sociedade.

Alterações são uma constante no ciclo de vida de um software, ocorrendo durante seu desenvolvimento, na fase de entrega, e mesmo após ser entregue. Ajustes e correções frequentemente se fazem necessários, e muitas vezes surgem pedidos para adicionar novas funcionalidades, geralmente a pedido do cliente. O software, portanto, passa por várias manutenções devido a essas novas solicitações. Após múltiplas modificações, que podem introduzir novos desafios, pode surgir a necessidade de desenvolver um novo software.

Ao longo da vida útil de um software, ele passará por diversas mudanças, que podem introduzir novos erros e aumentar a taxa de defeitos. Esse fenômeno é ilustrado na Figura 1.

![Curva de defeitos de um software ao longo do tempo](image.png)

> **Figura 1** — Curva de defeitos de um software ao longo do tempo. *Fonte: Pressman (2021).*

A Figura 1 exibe a curva de defeitos em softwares (taxa de defeitos) ao decorrer do tempo. Esse gráfico inclui uma **curva teórica** mostrando que a taxa de defeitos é inicialmente alta no começo do desenvolvimento do software, mas diminui progressivamente até se estabilizar. Contudo, na realidade, esse padrão ideal raramente se verifica, pois frequentemente são exigidos acréscimos de novas funcionalidades (solicitadas pelo cliente) ou alterações para corrigir problemas detectados. Portanto, a **curva real** é introduzida, evidenciando que, conforme mudanças são implementadas no software, ele pode se tornar mais suscetível a falhas. Essas alterações podem resultar em novos erros ou defeitos, como indicado pelos picos no gráfico, que simbolizam o aumento nas taxas de defeitos. Muitas vezes, essas melhorias precisam ser feitas de forma rápida, levando a uma negligência no processo de documentação para acelerar as mudanças. Este ciclo de modificações pode resultar em um software mais propenso a falhas e ao surgimento de mais erros.

> **Software vs. hardware:** diferentemente do hardware, que se desgasta fisicamente devido a fatores ambientais como altas temperaturas, poeira e vibrações, o software **não sofre deterioração física**. No entanto, os softwares podem se deteriorar devido às **mudanças** que são implementadas neles.

É importante notar que a taxa de defeitos no hardware pode ser influenciada não apenas por fatores ambientais, mas também por picos de processamento exigidos pelo software. Isso ocorre quando os recursos de hardware (memória, processador, placa de vídeo) não são suficientes para suportar a execução de um software específico. Um exemplo disso são jogos que demandam placas de vídeo de alta capacidade computacional; eles podem apresentar falhas devido ao superaquecimento do processador e da placa de vídeo.

---

## Siga em Frente...

### Princípios da análise de sistemas

Os fundamentos da análise de sistemas residem na importância de conduzir estudos detalhados dos processos, a fim de identificar a solução mais adequada para o desenvolvimento de um sistema. De acordo com Roth, Dennis e Wixom (2014), a análise de sistemas é ancorada em métodos e técnicas de pesquisa e especificação, visando descobrir a solução mais eficaz para um problema ou necessidade computacional específica de uma área de negócios, baseando-se nas funcionalidades identificadas pelo analista de sistemas.

Em uma visão mais generalizada das fases que envolvem os processos da análise de sistema, destacam-se, conforme Pressman (2021):

| Fase | O que acontece |
|---|---|
| **Análise** | Estudos focados na especificação do software. O objetivo é avaliar sua viabilidade, considerando o custo-benefício, estabelecer as funcionalidades necessárias do software, e definir o escopo, incluindo a alocação de recursos e a elaboração do orçamento. Os resultados obtidos nesta fase serão fundamentais para as etapas subsequentes. |
| **Projeto** | Definição lógica do software. Envolve a elaboração dos layouts de telas e relatórios, a construção da estrutura de banco de dados e a criação de diagramas gráficos para o desenvolvimento do software. |
| **Implementação** | Codificação do software, utilizando a linguagem de programação selecionada na fase de análise. |
| **Testes** | Com o objetivo de identificar erros, são conduzidos testes para verificar as funcionalidades dos componentes codificados. |
| **Documentação** | Elaboração de documentação para todos os processos e diagramas desenvolvidos em todas as etapas. Utiliza-se documentação padronizada (e adaptada por cada empresa de desenvolvimento) como meio de comunicação entre os envolvidos no desenvolvimento e como parte do contrato entre as partes interessadas na produção do software. |
| **Manutenção** | Após a implantação e início de operação do software, esta fase se dedica ao monitoramento, registro e correção de falhas, além de propor melhorias ou adicionar novas funcionalidades. |

> As fases descritas devem incluir um processo de **homologação**, que é a aprovação oficial do cliente, para validar os documentos produzidos. É essencial que o cliente compreenda que, uma vez aprovada uma etapa, quaisquer alterações posteriores afetarão os custos e poderão resultar em ajustes no cronograma, incluindo possíveis atrasos.

Sommerville (2018) e Pressman (2021) destacam alguns **princípios da análise de sistemas**, são eles:

1. É fundamental que a compreensão da informação relativa a um problema específico seja clara e compartilhada por todos os envolvidos no projeto.
2. As funcionalidades do software devem ser inicialmente definidas e descritas de maneira ampla, refinando-se progressivamente até alcançar um nível mais detalhado.
3. O comportamento do software deve ser ilustrado por meio de suas interações com o ambiente externo, incluindo usuários e outros sistemas.
4. Os diagramas que ilustram as funções e comportamentos do software devem ser estruturados em camadas, decompondo um problema complexo em partes menores para facilitar a compreensão.
5. A análise deve começar com informações essenciais e avançar até os detalhes de implementação, sem se preocupar inicialmente com a codificação específica da solução; os detalhes de implementação definirão como a solução será efetivamente realizada.

### O papel do analista de sistema

O **analista de sistemas** é o profissional encarregado de conduzir atividades de análise de sistemas, incluindo pesquisa, planejamento, coordenação de equipes de desenvolvimento e sugestão de soluções de software adequadas às necessidades de desenvolvimento ou resolução de problemas empresariais. As responsabilidades do analista de sistemas abrangem a concepção, implementação e implantação de software. A tarefa inicial é determinar as funcionalidades que o sistema deve ter, seguida pela compreensão e avaliação das necessidades e expectativas dos usuários do software, para que estas possam ser organizadas, especificadas e documentadas adequadamente (SOMMERVILLE, 2018).

O papel do analista de sistemas envolve desenvolver especificações, funcionalidades e transações, adaptando soluções para atender às demandas dos usuários. Essencialmente, esse profissional deve ter conhecimento sobre diversas áreas de negócio e, na ausência de domínio em algum tema específico, deve ser proativo em buscar informações sobre o campo de aplicação do software.

Uma habilidade importante para o analista de sistemas é possuir uma perspectiva empresarial aguçada, contribuindo assim para os processos gerenciais na criação do software. As competências valiosas para um analista de sistemas incluem:

- estar atualizado com as tecnologias;
- ter organização e método;
- visão gerencial;
- excelente habilidade de relacionamento interpessoal, entre outras.

O analista de sistemas atua como um **intermediário** entre os desenvolvedores de software e os usuários finais. Sua responsabilidade é entender as necessidades e desejos dos usuários e determinar o que é tecnicamente factível para desenvolver. O papel do analista inclui coletar informações dos usuários, interpretar esses dados e comunicá-los aos programadores de uma maneira técnica. Isso garante que o software desenvolvido esteja alinhado com as expectativas tanto do cliente quanto dos usuários finais.

Durante o desenvolvimento de um software, o analista de sistemas possui as seguintes atribuições:

- Interagir com clientes e usuários para entender suas necessidades em relação ao software.
- Avaliar custos e determinar a viabilidade do projeto de software.
- Coletar informações essenciais entrevistando os usuários do software.
- Identificar dados e requisitos essenciais para análise e desenvolvimento de soluções.
- Desenvolver a modelagem do software.
- Guiar os desenvolvedores durante todo o processo de criação do software, incluindo aspectos lógicos e de interface gráfica.
- Conduzir e monitorar os testes do software.
- Gerenciar a documentação completa do software.
- Administrar mudanças que ocorram durante o projeto.
- Estabelecer padrões para o desenvolvimento do software.
- Assegurar que a qualidade do software atenda às expectativas do cliente.
- Executar monitoramento e auditorias para identificar possíveis falhas.
- Organizar e ministrar treinamentos para os usuários do software.
- Supervisionar a implantação do software, assegurando a integração e adaptação aos sistemas do cliente.
- Oferecer consultoria técnica para entender as necessidades dos clientes em diferentes áreas de negócio.
- Pesquisar novas tecnologias e fornecedores, e buscar aperfeiçoamento profissional para a equipe de desenvolvimento.

---

## Vamos Exercitar?

Chegou o momento de resolver o desafio que lhe foi proposto no início da aula! Você está trabalhando em uma *software house* e, como primeira missão nessa empresa, você precisa avaliar um software de exames laboratoriais a fim de recomendar novas tecnologias para ele, as quais, caso aprovadas, serão utilizadas. O software em questão é de uma empresa com diversas filiais no Sul do país, que há 15 anos utiliza o mesmo software desktop (sem acesso à internet).

### 1. Atualizar o sistema ou criar um novo?

Vamos começar essa análise avaliando se é mais viável atualizar o sistema existente ou criar um novo. O atual software que a empresa utiliza é limitado ao ambiente desktop, ou seja, não é um sistema projetado para funcionar com os recursos da internet. Esse é um importante ponto, pois, se a empresa possui filiais, é crucial que ela tenha um sistema central, o qual as filiais acessem via internet, mantendo todo o sistema integrado. Veja que, mesmo sem avaliar as funcionalidades desse sistema legado, já sabemos que não é viável usá-lo.

> **Conclusão:** teremos que propor um **novo sistema** que suporte transações on-line.

### 2. Quais tecnologias podem ser utilizadas?

Para determinar as novas tecnologias a serem utilizadas em um novo sistema, deverá ser feito um trabalho de investigação para o qual recomenda-se os seguintes passos:

1. Visitar uma unidade da empresa para acompanhar o funcionamento do sistema.
2. Acompanhar o cadastramento da coleta de exames de um paciente a fim de observar o tempo gasto.
3. Verificar como é realizada a entrega dos resultados.
4. Descobrir qual a linguagem de programação utilizada e como é o funcionamento do banco de dados.

Após o trabalho investigativo, algumas tecnologias já podem ser apontadas:

- **Criação de um site e de um aplicativo** que permitam:
  - marcar o exame;
  - agendar a coleta em casa (caso o cliente assim deseje);
  - acompanhar o andamento da análise laboratorial dos exames solicitados;
  - visualizar os resultados dos exames;
  - disponibilizar os resultados para que sejam impressos pelo paciente.
- **Armazenamento do banco de dados em nuvem.** Nesse caso, você deverá consultar os três grandes *players* (Amazon, Google e Microsoft) e fazer um levantamento de custos.
- **Utilização da linguagem JAVA** como sugestão de linguagem de programação para diminuir os custos para o cliente.

### 3. Qual o perfil dos profissionais?

O ideal é ter, na equipe de desenvolvimento, analistas de sistemas com as seguintes habilidades: **conhecimento tecnológico atualizado**, **organização e método**, **visão gerencial** e **ótimo relacionamento interpessoal**. Um dos papéis do analista de sistemas é a atualização tecnológica constante, fator importante justamente nos casos em que um cliente pede ajuda para atualizar seus sistemas.

### 4. Como manter o software sempre atualizado?

E como saber quais os processos que deverão ser adotados para manter o software sempre atualizado? Imagine o seguinte cenário: após a entrega do software, foi verificado que nele poderiam ser utilizados códigos de barras e QR-Code. Na sua visão, o que precisa ser feito?

Acrescente itens à lista, crie um relatório com as soluções encontradas.

---

## Saiba mais

1. **Profissão de analista de sistemas**: leia o artigo:
   > SERASA EXPERIAN. **O que faz um analista de sistemas?** 2022.

2. **Natureza e definição do software**: leia o Capítulo 1, seções 1.1 e 1.2, do livro *Engenharia de software*, disponível na Biblioteca Virtual:
   > PRESSMAN, R. S.; MAXIM, B. R. **Engenharia de software**. Grupo A, 2021.

3. **Evolução de software**: leia o artigo:
   > AZEVEDO, D. J. P. **Evolução de Software**. Bate Byte. [s. d.]

## Referências

- FONSECA FILHO, C. História da computação: o caminho do pensamento e da tecnologia. Porto Alegre: EDIPUCRS, 2007.
- PRESSMAN, Roger S. Engenharia de software: uma abordagem profissional. 9. ed. Porto Alegre: AMGH, 2021.
- SOMMERVILLE, Ian. Engenharia de software. 10. ed. São Paulo: Pearson, 2018.
- ROTH, R. M.; DENNIS, A.; WIXOM, B. H. Análise e projeto de sistemas. 5. ed. Rio de Janeiro: LTC, 2014.
