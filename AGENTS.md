# Guia para assistentes de IA neste repositório

Este arquivo instrui qualquer assistente de IA (Claude, ChatGPT, Copilot, Cursor, etc.) sobre como
ajudar de forma útil neste repositório. Ele é público — vale tanto para o dono do repositório quanto
para qualquer pessoa que o abra com sua própria IA.

## O que é este repositório

Anotações de estudo que acompanham o curso de Engenharia de Software (Anhanguera/UNOPAR). O conteúdo
cobre disciplinas do curso — atualmente Fundamentos de Cálculo Aplicado e Linguagem de Programação
(Python) — mais um acervo de provas antigas coletadas de fontes públicas para treino (`estudos/`).
Quem estuda a partir deste repositório, com a ajuda de uma IA, pode ser qualquer pessoa: o mantenedor
original, um colega de turma, ou alguém que encontrou o repositório publicamente — não presuma nível
prévio de conhecimento específico de ninguém.

## Como ensinar

- **Calibre pelo nível de quem está estudando, não presuma.** Se a pessoa já demonstrar domínio de
  lógica de programação ou de outra linguagem, não repita o básico de if/for/while/variáveis — vá
  direto ao que é específico da disciplina/linguagem em questão (sintaxe de C, ponteiros, matemática
  discreta, pandas, etc.). Se for claramente iniciante, explique os fundamentos com calma. Quando não
  tiver como saber, pergunte ou comece pelo nível mais básico do módulo e ajuste a partir da resposta.
- Prefira o método socrático: antes de entregar a resposta pronta, faça perguntas guiadas que levem a
  pessoa a pensar, especialmente em exercícios.
- Ao corrigir código escrito por quem está estudando, aponte tanto erros de sintaxe quanto problemas
  conceituais (ex.: vazamento de memória, off-by-one, mutabilidade incorreta).
- Prefira explicações curtas com exemplo de código executável a parágrafos longos de teoria.
- Ao gerar exercício de prática, siga o formato das provas da instituição: múltipla escolha com 5
  alternativas (uma correta, quatro com justificativa do erro) ou completar trecho de código — não
  invente formatos diferentes sem que seja pedido.

## Pesquisa e enriquecimento de conteúdo

Quando for explicar ou aprofundar um conceito:

- Busque bons exemplos práticos (não só teóricos) na internet para ilustrar o conceito, em vez de
  inventar exemplos genéricos.
- Procure imagens e vídeos de referência (diagramas, visualizações, aulas curtas) e **linke a fonte**
  em vez de tentar reproduzir o conteúdo original. Prefira fontes confiáveis (documentação oficial,
  canais didáticos reconhecidos).
- Nunca invente citação, referência bibliográfica ou URL. Se não tiver certeza de uma fonte, diga isso
  explicitamente em vez de inventar um link plausível.

## Estrutura e convenções de arquivo

Cada disciplina segue esta estrutura (uma pasta por disciplina, `UNIDADE N/AULA N/` dentro):

| Arquivo/pasta | Papel | Pode editar? |
|---|---|---|
| `content.md` | Conteúdo original da aula (extraído do material da instituição) | **Não.** É a fonte bruta — reformatações visuais pontuais (ver histórico do repo) foram exceção pedida explicitamente pelo usuário, não a regra. |
| `solutions/guia-de-estudo.md` | Material de apoio extra (explicação didática + exercícios + gabarito) gerado para complementar a aula | Sim — é o lugar certo para adicionar material extra |
| `EXERCICIOS DAS UNIDADES/exercicioN.md` | Histórico de questões já respondidas (provas/quizzes da LMS), com gabarito comentado | Não editar o conteúdo — só formatação visual, como já feito |
| `simulados/` | Simulados gerados sob demanda (ver seção abaixo) | Sim — é aqui que novos simulados entram |

Peça confirmação ao usuário antes de editar `content.md` diretamente — é o comportamento padrão deste
repositório, mesmo que pareça uma melhoria de formatação.

## Como gerar simulados sob demanda

Quando o usuário pedir um **simulado** de uma disciplina/unidade (ex.: "faz um simulado da Unidade 2
de Linguagem de Programação"), siga este processo:

1. **Leia as fontes da unidade pedida** antes de escrever qualquer questão:
   - todos os `content.md` das aulas da unidade (conceitos e exemplos de código cobertos);
   - o(s) `exercicioN.md` correspondente(s) em `EXERCICIOS DAS UNIDADES/`, para calibrar nível de
     dificuldade, estilo de pergunta e tópicos que a instituição já cobrou.
2. **Gere questões originais**, no mesmo estilo/dificuldade das provas reais, mas **não copie
   perguntas ou alternativas já existentes em `exercicioN.md`** — são histórico do que já caiu, o
   simulado deve treinar o mesmo tipo de raciocínio com perguntas novas.
3. **Formato de saída** — salve em `<Disciplina>/simulados/simulado-NN-<tema-curto>.md` (numeração
   sequencial dentro da pasta `simulados/` daquela disciplina; se não existir, crie a pasta):
   - Por padrão, gere um **HTML autocontido e interativo** (sem backend, correção instantânea no
     navegador), seguindo a estrutura de referência em
     `Fundamentos de Calculo Aplicado/simulados/simulado-01-geral.html` (cabeçalho com metadados da
     prova, barra de progresso, cada questão com alternativas clicáveis, feedback imediato certo/errado
     com explicação, resumo final de pontuação). Reaproveite o mesmo CSS/estrutura desse arquivo como
     ponto de partida em vez de recriar do zero.
   - Se o usuário pedir algo rápido/só-texto, use o formato Markdown já usado em
     `Linguagem de Programação/EXERCICIOS DAS UNIDADES/` (questão em `##`, alternativas em lista,
     correta em negrito) — mais rápido de gerar e de revisar.
4. **Não invente conteúdo que não foi ensinado** na unidade — se uma questão exige algo fora do que os
   `content.md` da unidade cobrem, avise o usuário em vez de incluir a questão.
5. Ao terminar, informe ao usuário quantas questões foram geradas e de quais aulas/tópicos vieram.

## Acervo `estudos/` (provas de terceiros)

A pasta `estudos/provas` e `estudos/transcricoes` reúne transcrições de provas antigas encontradas
publicamente (Studocu, fóruns de alunos) — não são criação do usuário. A proveniência de cada
documento está registrada em `estudos/provas/INDEX.md`. Se for adicionar um novo documento a esse
acervo:

- registre a fonte, data, autor/uploader e nível de confiança na tabela do `INDEX.md`, seguindo o
  mesmo formato das entradas existentes;
- nunca invente ou complete trechos que não estavam disponíveis na fonte — marque explicitamente o que
  não foi possível coletar (ver "Metodologia e limites" no `INDEX.md`);
- PDFs brutos de provas pagas/paywalled não entram no repositório (ver `.gitignore`) — só a
  transcrição em Markdown do texto renderizado.

## Sobre este arquivo vs. `CLAUDE.md`

Este repositório também tem um `CLAUDE.md` na raiz, mas ele é local (`.gitignore`) e não aparece no
GitHub — contém preferências pessoais do usuário para o Claude Code. Este `AGENTS.md` é a versão
pública e genérica das mesmas diretrizes de ensino, para qualquer IA que alguém use ao navegar este
repositório público.
