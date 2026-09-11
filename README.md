# Estudos — Engenharia de Software

Anotações pessoais de estudo do curso de Engenharia de Software (Anhanguera/UNOPAR), mantidas por um
desenvolvedor profissional (React, Next.js, Node, TypeScript, Flutter) cursando os semestres iniciais.
Reúne o conteúdo das disciplinas, material de apoio didático, histórico de exercícios e simulados de
revisão gerados sob demanda.

> Este é um repositório de estudo pessoal, não material oficial da instituição. Conteúdo de aula foi
> extraído/reformatado a partir do material do curso; provas de terceiros (pasta `estudos/`) têm fonte
> e proveniência documentadas — ver [`estudos/provas/INDEX.md`](estudos/provas/INDEX.md).

## Estrutura

```
.
├── Fundamentos de Calculo Aplicado/   # Matemática discreta/cálculo aplicado à computação
│   ├── ROTEIRO-DE-ESTUDOS.md          # Plano de estudo da disciplina (vídeos recomendados etc.)
│   ├── UNIDADE N - .../AULA N - .../  # Conteúdo de cada aula
│   └── simulados/                     # Simulados de revisão (HTML interativo)
├── Linguagem de Programação/          # Python
│   ├── UNIDADE N - .../AULA N/        # Conteúdo de cada aula
│   └── EXERCICIOS DAS UNIDADES/       # Histórico de quizzes já respondidos, com gabarito
├── estudos/                           # Acervo de provas antigas de terceiros + scripts de apoio
│   ├── provas/                        # Transcrições de provas por disciplina + INDEX.md (proveniência)
│   ├── transcricoes/                  # Transcrições brutas correspondentes
│   ├── md_to_pdf.py                   # Gera PDF a partir de um Markdown do acervo
│   └── images_to_pdf.py
├── matriz-curricular.pdf              # Matriz curricular oficial do curso
├── AGENTS.md                          # Guia para qualquer IA que ajude neste repositório
└── CLAUDE.md                          # (local, não versionado) preferências pessoais para Claude Code
```

Cada aula segue o padrão `content.md` (conteúdo original) + opcionalmente `solutions/guia-de-estudo.md`
(material de apoio extra: explicação didática, exercícios, gabarito) + slides/imagens da aula.

## Usando IA para estudar neste repositório

Se você for usar um assistente de IA (Claude, ChatGPT, Copilot...) para estudar a partir deste
repositório — seja você o dono ou alguém que encontrou este repositório público — leia
[`AGENTS.md`](AGENTS.md). Ele descreve como a IA deve ensinar o conteúdo, pesquisar exemplos/imagens/
vídeos de referência, e como gerar simulados de revisão sob demanda a partir do conteúdo e dos
exercícios de cada disciplina.

## Acervo de provas (`estudos/`)

A pasta `estudos/` reúne transcrições em Markdown de provas antigas de disciplinas equivalentes,
encontradas publicamente (fóruns de alunos, Studocu), usadas como material extra de treino. Cada
documento tem sua fonte, data e nível de confiança registrados em
[`estudos/provas/INDEX.md`](estudos/provas/INDEX.md), junto com a metodologia de coleta. Nenhum PDF
pago/paywalled é versionado — apenas a transcrição textual.

## Licença

Sem licença explícita definida. O conteúdo original das aulas pertence à instituição de ensino; as
transcrições de provas de terceiros pertencem aos respectivos autores/plataformas de origem (ver
proveniência no `INDEX.md`). Se for reaproveitar algo daqui, verifique a fonte original antes.
