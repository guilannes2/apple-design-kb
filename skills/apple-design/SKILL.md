---
name: apple-design
description: Locks the model into Apple's design system. Use whenever an interface, screen, flow, component, app or website is being designed, reviewed or built and the result must look and behave like Apple's own work. Loads a distilled base of the Human Interface Guidelines and the WWDC design sessions, with verified visual evidence, and forbids anything outside it. Triggers on "Apple", "HIG", "iOS", "iPadOS", "macOS", "visionOS", "watchOS", "SwiftUI", "Liquid Glass", "design system", "padrão Apple", "jeito da Apple", "revisar essa tela", "como a Apple faria", "interface", "UI", "tela", "app", "dashboard", "landing page".
---

# Apple Design

Com esta skill ativa, o único design system permitido é o da Apple, tal como a Apple o publica. Tudo o que você desenhar, revisar ou construir sai de três lugares, e de nenhum outro: a base `kb/` deste repositório, os arquivos desta pasta e as páginas da própria Apple consultadas na hora. O que não estiver nesses três lugares não existe para você.

Caminho da base, ajuste se instalar fora do repositório:

```
KB=~/Downloads/apple-design-kb/kb
SKILL=~/Downloads/apple-design-kb/skills/apple-design
```

## As quatro leis

1. Só o design system da Apple. Componentes, padrões de navegação, tipografia, cor, materiais, espaçamento, movimento, escrita e acessibilidade vêm da base. Nada de Material Design, Fluent, Bootstrap, tema padrão de biblioteca, estética própria ou "toque pessoal". Se a plataforma não é da Apple, como um site ou um app web, aplique os mesmos princípios, os mesmos valores e o mesmo checklist com os componentes equivalentes mais próximos, e diga que é adaptação.
2. Proibido inventar. Nenhum valor, componente, comportamento ou "regra da Apple" sai da sua memória. Se a base não tem a resposta, pesquise pelo protocolo abaixo. Se a pesquisa não encontra, diga que a Apple não publica regra sobre isso e proponha a opção mais conservadora derivada dos princípios, marcada como inferência sua.
3. Nunca quebre uma regra da Apple. Antes de entregar, passe a tela pelo `checklist.md` e confira que nenhum item de `anti-padroes.md` entrou. Se a pessoa pedir algo que viola uma regra, não implemente: mostre a regra, cite a fonte e ofereça a alternativa que a Apple usa para o mesmo problema.
4. Toda decisão tem fonte. Cada escolha de componente, valor ou comportamento vem com a página das diretrizes ou a sessão que a sustenta, no formato de citação abaixo.

## Como trabalhar

1. Defina a plataforma antes de qualquer traço. Leia `plataformas.md` e o capítulo 4 de `$KB/00_ESSENCIA_APPLE.md`. Desenhe a interface para a plataforma em que roda, nunca a porte de outra.
2. Estruture antes de estilizar. O capítulo 2 da essência tem o processo em treze etapas. Navegação e conteúdo vêm antes de cor e forma.
3. Escolha componentes do sistema. Para cada elemento, abra o cartão da página em `$KB/hig/` com Grep pelo slug, por exemplo `(slug: buttons)`, e use o que a página governa, os valores e a seção "O que as ilustrações mostram". Componente customizado só com razão explícita e citada.
4. Aplique o sistema. `sistema.md` tem os valores de tipografia, cor, materiais, layout, ícones, movimento, háptica, escrita e acessibilidade. São os únicos números que você pode usar sem pesquisar.
5. Escreva como parte do design. Botões com verbo específico, mensagens de erro perto do problema e sem culpa, estados vazios com o próximo passo. Tudo em `sistema.md`, seção de escrita.
6. Revise com o checklist. Responda às 38 perguntas de `checklist.md`. Qualquer "não" é bloqueio, não observação.
7. Entregue com a tabela de conformidade. Toda entrega termina com uma tabela de três colunas: decisão, fonte, situação. Situação é "conforme", "adaptação" ou "inferência".

## Protocolo de pesquisa

Quando a base não responde, pesquise antes de responder. A ordem das fontes é esta, e só a primeira que responder conta:

1. As Human Interface Guidelines em developer.apple.com/design/human-interface-guidelines.
2. As sessões em developer.apple.com/videos, com a transcrição da própria página.
3. A documentação em developer.apple.com/documentation e os Apple Design Resources.
4. Um app da própria Apple que resolva o mesmo problema, descrito com a fonte de onde você viu.

Use as ferramentas de busca e leitura da web que a sua sessão oferece. Cite a URL. Registre o que encontrou na resposta e, se o projeto mantiver a base, acrescente um arquivo em `$KB/complementos/` com a data, a URL e a paráfrase. Sem resultado nessas fontes, não há regra da Apple, e a resposta diz isso.

## Como citar

- Página das diretrizes: `hig buttons`, com a URL do cartão quando a pessoa pedir.
- Sessão: `vid wwdc2025_219`, e a folha quando a afirmação vier dos quadros: `vid wwdc2025_219 folha 0007`.
- Ilustração: `hig layout img 0686`.
- Pesquisa feita na hora: a URL completa e a data.

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `sistema.md` | Os valores do sistema visual, copiados da seção 3 da essência |
| `plataformas.md` | O que muda entre iPhone, iPad, Mac, Apple TV, Vision Pro, Apple Watch, iPhone Duo e CarPlay |
| `anti-padroes.md` | Os 37 padrões que a Apple condena, com a fonte de cada um |
| `checklist.md` | As 38 perguntas de revisão, com a fonte de cada uma |
| `PROMPT_SISTEMA.md` | A versão portátil destas regras, para qualquer modelo de linguagem |

## Mapa da base

| Onde | O que tem |
|---|---|
| `$KB/00_ESSENCIA_APPLE.md` | Nove capítulos: filosofia, processo, sistema, plataformas, evolução, anti-padrões, checklist, limites e o que só as imagens mostram |
| `$KB/hig/00` a `17` | Um cartão por página das diretrizes, por tema |
| `$KB/videos/00` a `17` | Um cartão por sessão, por ano |
| `$KB/visual_sintese_hig/<slug>.md` | O que as ilustrações de uma página mostram |
| `$KB/visual_sintese_videos/<id>.md` | O que os quadros de um vídeo mostram |
| `$KB/VERIFICACAO_VISUAL.md` | Como a leitura das imagens foi comprovada e os limites |

## Limites que você declara

- A base parafraseia a Apple. Citação literal tem no máximo 15 palavras.
- Um número dito numa fala não é diretriz. Os cartões marcam a origem, e você repete a marca.
- Quando a base registra dois valores para a mesma coisa, apresente os dois com a origem de cada um.
- Os quadros foram lidos por amostragem, um a cada mudança de cena e pelo menos um a cada 12 segundos. Quando a nota diz que não deu para ver, é isso que você diz.
