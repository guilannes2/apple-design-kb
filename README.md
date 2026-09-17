# Apple Design KB

<img src="docs/assets/capa.png" alt="Apple Design KB" width="100%">

> **In English:** a knowledge base on how Apple thinks, designs and builds interfaces, distilled from Apple's own published material: the 173 pages of the Human Interface Guidelines and the 188 design sessions at developer.apple.com/design, including what appears on screen in those videos and in the illustrations. It ships with a skill that locks a language model inside Apple's design system: nothing from outside gets in, nothing is invented, no Apple rule gets broken. The base is in Portuguese; every card links to its Apple source.

Uma base de conhecimento sobre como a Apple pensa, desenha e constrói interfaces, destilada da própria Apple: as 173 páginas das Human Interface Guidelines e os 188 vídeos de design publicados em developer.apple.com/design, incluindo o que aparece na tela desses vídeos e nas ilustrações das diretrizes. Vem com uma skill que tranca o modelo de linguagem dentro desse design system: nada de fora entra, nada é inventado, e nenhuma regra da Apple é quebrada.

A base está em português. Ela existe para ser usada por pessoas e por agentes de IA que precisem desenhar, revisar ou construir uma interface no padrão da Apple, com a fonte de cada afirmação indicada.

<p>
<img src="docs/assets/badge_videos.svg" height="72" alt="175 vídeos assistidos por inteiro">
<img src="docs/assets/badge_horas.svg" height="72" alt="63,3 horas de vídeo em 26.869 quadros">
<img src="docs/assets/badge_folhas.svg" height="72" alt="3.624 folhas conferidas">
<img src="docs/assets/badge_erros.svg" height="72" alt="0 códigos errados">
<img src="docs/assets/badge_sinteses.svg" height="72" alt="333 sínteses visuais">
</p>

## Fontes

Tudo aqui foi destilado de material que a Apple publica em aberto:

- Apple Design, a página de entrada: https://developer.apple.com/design/
- Human Interface Guidelines, as 173 páginas: https://developer.apple.com/design/human-interface-guidelines/
- As sessões de design em vídeo, com transcrição oficial: https://developer.apple.com/videos/design/
- Apple Design Resources, os kits de interface citados nas sessões: https://developer.apple.com/design/resources/

Cada cartão em `kb/hig/` e `kb/videos/` traz a URL exata da página ou da sessão de origem na linha "Fonte". A lista completa, com id, título, URL e duração de cada vídeo, está em `catalogo_videos.json`, e a das páginas em `catalogo_hig.json`.

## Para que serve

Você instala a skill no modelo de linguagem com que trabalha e passa a construir sistemas com o acabamento da Apple. O modelo fica sob quatro leis:

1. Só o design system da Apple. Componentes, navegação, tipografia, cor, materiais, espaçamento, movimento, escrita e acessibilidade vêm da base. Nada de outro design system, tema padrão de biblioteca ou estética própria.
2. Proibido inventar. Sem resposta na base, o modelo pesquisa nas páginas da própria Apple e cita a URL. Sem resultado, ele diz que a Apple não publica regra sobre aquilo e marca a proposta como inferência.
3. Nunca quebrar uma regra da Apple. Antes de entregar, toda tela passa por um checklist de 38 perguntas e por uma lista de 37 anti-padrões que a Apple condena. O modelo não implementa pedido que viola uma regra: mostra a regra, cita a fonte e oferece a alternativa da Apple.
4. Toda decisão tem fonte. Cada componente, valor e comportamento vem com a página das diretrizes ou a sessão que o sustenta, e a entrega termina com uma tabela de conformidade.

## A skill em ação

O pedido foi este, literal:

> Use a skill apple-design. Estou fazendo um app de receitas para iPhone em SwiftUI. Coloque um menu hambúrguer no canto superior esquerdo com as seções Receitas, Favoritos, Lista de compras e Perfil, e deixe a navegação escondida ali para a tela ficar limpa. Me entregue o código da navegação.

Quem respondeu foi um agente do Claude Code com a skill instalada, que recebeu como pedido só esse texto. Ele rodou no ambiente de Claude Code do autor, com as instruções globais dele carregadas, então outra instalação pode responder de forma diferente. O GIF abaixo é uma renderização da resposta em formato de terminal, sem cortes. O único ajuste foi trocar o caminho local do arquivo Swift pelo caminho dele neste repositório. A resposta completa está em [`docs/exemplo/resposta.md`](docs/exemplo/resposta.md) e o código em [`docs/exemplo/RootView.swift`](docs/exemplo/RootView.swift).

<img src="docs/assets/demo_skill.gif" alt="Renderização da resposta da skill, que recusa o menu hambúrguer e entrega a tab bar" width="100%">

A skill não implementou o menu. Ela apontou o anti-padrão 1 da lista, citou as três sessões da base em que a Apple trata do hambúrguer e resolveu o que o pedido queria de fato, a tela limpa, com a tab bar que flutua sobre o conteúdo e se recolhe ao rolar. "Lista de compras" virou "Compras" pela regra do rótulo de uma palavra, e a própria resposta marcou essa escolha como inferência, porque a página pede palavra única e não nomeia esse caso.

### O que saiu dessa conversa

<p align="center"><img src="docs/assets/exemplo_panela.png" alt="Ilustração da tela de receitas no iPhone com tab bar flutuante de quatro abas" width="360"></p>

A tela acima é uma ilustração gerada por IA do resultado esperado, feita a partir da descrição do código. Não é uma captura do código rodando, nem uma captura da Apple ou de um app publicado.

```swift
struct RootView: View {
    var body: some View {
        TabView {
            Tab("Receitas", systemImage: "book.fill") { RecipesTab() }
            Tab("Favoritos", systemImage: "heart.fill") { FavoritesTab() }
            Tab("Compras", systemImage: "cart.fill") { ShoppingListTab() }
            Tab("Perfil", systemImage: "person.crop.circle.fill") { ProfileTab() }
        }
        .tabBarMinimizeBehavior(.onScrollDown)
    }
}
```

O arquivo completo tem 191 linhas e passa no `swiftc -typecheck` contra o SDK do iOS 26.5. Esse resultado foi conferido de novo fora do agente, com o mesmo compilador, SDK e target.

Toda entrega termina com a tabela de conformidade. Esta é a da resposta, sem alteração:

| Decisão | Fonte | Situação |
|---|---|---|
| Recusar o menu hambúrguer | `vid wwdc2021_10126`; `vid wwdc2017_802`; `vid wwdc2025_359` | conforme |
| Tab bar com as 4 seções de nível superior | `hig tab-bars` | conforme |
| Tab bar sempre visível, nunca desabilitada | `hig tab-bars` | conforme |
| `NavigationStack` por aba, estado preservado | `hig tab-bars` | conforme |
| `tabBarMinimizeBehavior(.onScrollDown)` para a tela limpa | `hig tab-bars`; `vid wwdc2025_323` | conforme |
| Ação "Nova receita" na toolbar, fora da tab bar | `hig tab-bars`; `vid wwdc2025_359` | conforme |
| Título de navegação como resposta a "onde estou" | `vid wwdc2025_359` | conforme |
| Rótulos de uma palavra, símbolos preenchidos | `hig tab-bars` | conforme |
| `ContentUnavailableView` nas seções vazias | `hig tab-bars`; `vid wwdc2025_359` | conforme |
| Cores semânticas do sistema, nada fixo no código | `vid wwdc2025_359` | conforme |
| "Compras" como rótulo curto de "Lista de compras" | `hig tab-bars` pede palavra única, não nomeia este caso | inferência |

### O que a nossa checagem achou nessa resposta

A resposta passou pelo mesmo tratamento do resto da base: dois agentes céticos tentaram refutar cada afirmação contra os cartões e contra o arquivo Swift. De 45 afirmações, 33 se sustentaram. Quatro dos problemas foram conferidos de novo direto nos arquivos e ficam registrados aqui, porque a resposta acima está publicada sem correção:

- Em "o piso de conforto é cinco abas ou menos", o número está mal aplicado. A página de tab bars dá esse número para a tab bar customizável do iPadOS, não para o iPhone. Quatro abas não contrariam a base, mas o número não vale para este caso.
- A minimização da tab bar ao rolar aparece com duas fontes, `hig tab-bars` e `vid wwdc2025_323`. Só a sessão sustenta a frase. A página das diretrizes descreve a minimização apenas para tab bar com acessório anexado.
- O estado vazio com próximo passo está citado em `vid wwdc2025_359`. A fonte certa na base é `hig writing`.
- A resposta fala em oito nomes de SF Symbols conferidos. O arquivo tem sete.

Dois desses achados viraram regra na skill depois dessa rodada: um número vale só para a plataforma e o contexto em que a fonte o dá, e numa citação dupla cada fonte tem que sustentar a frase sozinha.

## Instalar

Clone o repositório e escolha o seu ambiente.

Claude Code. Copie a pasta da skill para as suas skills e ajuste o caminho da base no início do arquivo:

```bash
git clone https://github.com/guilannes2/apple-design-kb.git
cp -r apple-design-kb/skills/apple-design ~/.claude/skills/apple-design
```

A skill dispara sozinha quando a conversa trata de interface, tela, app, iOS, macOS, SwiftUI, HIG ou padrão Apple. Você também pode chamar `/apple-design`.

Codex, Cursor, Windsurf e outros com arquivo de regras. Copie o conteúdo de `skills/apple-design/PROMPT_SISTEMA.md` para o arquivo de regras do projeto, como `AGENTS.md` ou `.cursor/rules`, e mantenha a pasta `kb/` acessível ao modelo.

ChatGPT, Gemini, Claude no navegador ou qualquer modelo sem acesso a arquivos. Cole `skills/apple-design/PROMPT_SISTEMA.md` como instrução de sistema ou no início da conversa. Ele funciona sozinho, com os pisos numéricos e as proibições. Para o material completo, anexe `kb/00_ESSENCIA_APPLE.md`.

## Por onde começar a ler

1. `kb/00_ESSENCIA_APPLE.md` é a síntese. Tem nove capítulos: a filosofia, o processo do problema à tela, o sistema visual, as diferenças entre plataformas, a evolução por período, os anti-padrões, um checklist de revisão, os limites da base e o que só as imagens mostram.
2. `kb/hig/` tem um cartão por página das diretrizes, em 18 arquivos por tema. Cada cartão diz o que a página governa, por quê, o que fazer e evitar, os números exatos quando existem e, no fim, o que as ilustrações daquela página mostram.
3. `kb/videos/` tem um cartão por sessão, em 18 arquivos por ano. Cada cartão traz a tese, o processo descrito, os princípios com o porquê, as técnicas com os valores ditos, os exemplos, até duas citações curtas e o que os quadros do vídeo mostram.
4. `skills/apple-design/` tem a skill, os valores do sistema, as plataformas, os anti-padrões, o checklist e o prompt portátil.

## O que a Apple ensina, em resumo

Treze princípios de primeira ordem. Propósito antes de tudo. O conteúdo em primeiro lugar, com a interface e a marca cedendo. Familiaridade e consistência, com o componente do sistema como padrão e o customizado como exceção justificada. Clareza e simplicidade, que não são minimalismo. Agência, perdão e controle nas mãos da pessoa. Feedback imediato e causal. Responsabilidade com privacidade e dados mínimos. Flexibilidade e inclusão desde o primeiro rascunho. O corpo, o contexto e o dispositivo como régua. Craft, ou seja, nada é aleatório. Deleite como soma, não como decoração. Moderação, porque interrupção, cor, efeito e som são créditos escassos. Honestidade de estado e de linguagem.

### Os treze princípios, em cartões

<p>
<img src="docs/assets/principios/01.png" width="24%" alt="Princípio 1 de 13">
<img src="docs/assets/principios/02.png" width="24%" alt="Princípio 2 de 13">
<img src="docs/assets/principios/03.png" width="24%" alt="Princípio 3 de 13">
<img src="docs/assets/principios/04.png" width="24%" alt="Princípio 4 de 13">
<img src="docs/assets/principios/05.png" width="24%" alt="Princípio 5 de 13">
<img src="docs/assets/principios/06.png" width="24%" alt="Princípio 6 de 13">
<img src="docs/assets/principios/07.png" width="24%" alt="Princípio 7 de 13">
<img src="docs/assets/principios/08.png" width="24%" alt="Princípio 8 de 13">
<img src="docs/assets/principios/09.png" width="24%" alt="Princípio 9 de 13">
<img src="docs/assets/principios/10.png" width="24%" alt="Princípio 10 de 13">
<img src="docs/assets/principios/11.png" width="24%" alt="Princípio 11 de 13">
<img src="docs/assets/principios/12.png" width="24%" alt="Princípio 12 de 13">
<img src="docs/assets/principios/13.png" width="24%" alt="Princípio 13 de 13">
</p>

Um processo em treze etapas, do problema à tela: perguntar por que a coisa deve existir, definir para quem, listar tudo o que o app poderia fazer e depois cortar, estruturar navegação e conteúdo, começar pelo que já se sabe, gerar muitas alternativas antes de criticar, prototipar subindo a fidelidade aos poucos, mostrar a pessoas reais no dispositivo, e só então o design visual, a escrita, o som e a háptica, a acessibilidade atravessando tudo e a comunicação do trabalho.

O sistema: tipografia, cor, materiais, layout e espaçamento, ícones e símbolos, movimento, háptica e som, escrita e acessibilidade, com os valores que a Apple publica e com a indicação de quando um número vem de uma fala e não das diretrizes.

As plataformas: o que muda de decisão entre iPhone, iPad, Mac, Apple TV, Vision Pro, Apple Watch, iPhone Duo e CarPlay.

A evolução do pensamento de design da Apple por período, de 2014 a 2026, 37 anti-padrões que a Apple condena com todas as letras e um checklist de 38 perguntas para revisar uma tela.

O que só as imagens mostram. Este capítulo saiu de uma leitura que os textos não tinham: 3.072 folhas de quadros dos vídeos e 552 folhas de ilustrações das diretrizes, vistas uma a uma. São 60 itens em oito seções, cada um com a imagem ou o quadro que o sustenta. Alguns exemplos:

- Medida de componente é ensinada como relação, com setas duplas cotando largura, altura e respiro, e o número só aparece onde existe contrato com o sistema ou com terceiros, como nas máscaras do Game Center e nos botões do Apple Pay.
- O alvo de toque é maior que o desenho pintado, e a folga dobra quando o botão não tem moldura própria: 12 pontos de cada lado no botão com bezel, 24 no símbolo pequeno e no botão só de texto.
- A área segura do tvOS aparece com valores diferentes na prancha das diretrizes e no slide da sessão de 2019, e a base mantém a divergência à vista em vez de escolher um lado.
- A camada de anotação tem cor própria e nunca se confunde com a interface: rosa e vermelho nas diretrizes, amarelo nas sessões.
- Comparações de certo e errado usam sempre a mesma gramática visual, e a Apple monta as próprias demonstrações com objetos físicos, barras de status congeladas e mosaicos de miniaturas no fecho.

## O processo, em um diagrama

```mermaid
flowchart LR
    A[developer.apple.com/design] --> B[173 páginas do HIG em JSON do DocC]
    A --> C[188 páginas de vídeo com transcrição e tempo]
    B --> D[Cartões por página, 18 arquivos]
    C --> E[Cartões por sessão, 18 arquivos]
    D --> F[Verificação de cobertura e fidelidade do texto]
    E --> F
    C --> G[175 vídeos baixados do servidor da Apple]
    G --> H[26.869 quadros por mudança de cena, um a cada 12 s no mínimo]
    H --> I[3.072 folhas de 9 quadros, com tempo e código carimbado]
    B --> J[1.342 ilustrações e 61 vídeos de demonstração]
    J --> K[552 folhas de 4 imagens, com contexto da página e código]
    I --> L[Agentes veem cada folha e anotam o código]
    K --> L
    L --> M[Conferência recalcula o código a partir da chave secreta]
    M --> N[333 sínteses visuais, cada uma com verificador cético]
    N --> O[Sínteses inseridas nos cartões e nos artigos]
    O --> P[Capítulo 9 da essência: o que só as imagens mostram]
    P --> Q[Skill apple-design]
```

### Como se prova que uma folha foi vista

```mermaid
flowchart LR
    S[Chave secreta fora da base] --> H1[Código de 5 caracteres por folha, derivado da chave, do id e do número]
    H1 --> IMG[Código impresso na própria imagem da folha]
    IMG --> AG[Agente abre a folha, descreve os quadros e copia o código]
    AG --> LOG[Registro por folha: id, número, código lido]
    S --> RE[Script recalcula o código esperado]
    LOG --> CMP{Bate?}
    RE --> CMP
    CMP -->|sim| OK[Folha conferida]
    CMP -->|não| NO[Folha rejeitada e relida]
```

Resultado da conferência: 3.072 folhas de vídeo e 552 do HIG, nenhuma rejeitada.

### A evolução do pensamento de design da Apple, pelo que as sessões dizem

```mermaid
timeline
    title 2014 a 2026, um tema por ano
    2014 a 2016 : Método e prototipagem, apps falsos testados com pessoas : O Apple Watch força uma mentalidade própria
    2017 : Os fundamentos nomeados, human interface em vez de user interface : Safe Area chega com o iPhone X
    2018 : Fluidez, intenção e qualidade : Interromper vira privilégio
    2019 : Dark Mode com cores semânticas, materiais e SF Symbols : Som e háptica viram design
    2020 : iPad com identidade própria, ponteiro e sidebar : Widgets e App Clips, o app como camada contextual
    2021 : Inclusão como processo : Descobribilidade no lugar de tutoriais
    2022 : Gráficos, escrita com método PACE e abas que refletem hierarquia
    2023 : visionOS e o design espacial : O maior redesenho do relógio
    2024 : Amadurecimento espacial : Tab bar e sidebar viram a mesma estrutura
    2025 : Liquid Glass unifica a linguagem entre plataformas
    2026 : Princípios reescritos em nove, com Forgiveness : IA como responsabilidade de quem projeta
```

Cada linha dessa timeline vem do capítulo 5 da essência, com as sessões que a sustentam citadas lá.

## Como a base foi feita

O pedido era claro: destilar tudo o que está em developer.apple.com/design, assistir aos vídeos e não afirmar que algo foi visto sem que tenha sido. O processo abaixo é o que aconteceu, com os números medidos.

### 1. Coleta

O site foi varrido respeitando o `robots.txt`, com um intervalo entre pedidos. As páginas das diretrizes vêm como JSON do DocC, o mesmo formato que alimenta o site, e foram convertidas para Markdown. As páginas de vídeo trazem a transcrição oficial com o tempo de cada frase, e os arquivos de vídeo ficam no servidor da própria Apple, em MP4 ou em streaming HLS. Ao todo: 173 páginas, 188 vídeos, 167 transcrições oficiais.

### 2. Destilação do texto

Trinta e seis agentes escreveram os cartões, um agente por grupo de páginas ou de sessões, cada um obrigado a registrar no fim do arquivo quais fontes leu e se leu até o fim. Um verificador cruzou cada cartão com a fonte: cobertura dos 173 slugs e dos 188 ids, vinte afirmações conferidas contra o texto original, e uma busca por qualquer frase que dissesse ter visto uma tela. Nenhuma afirmação de leitura visual apareceu nessa fase, porque nenhuma imagem tinha sido vista ainda.

### 3. Os vídeos viram folhas de quadros

Os 175 vídeos com arquivo foram baixados do servidor da Apple e transformados em quadros com o ffmpeg: um quadro a cada mudança de cena e pelo menos um a cada 12 segundos. Deu 26.869 quadros de 63,3 horas de vídeo. Os quadros foram montados em folhas de contato de nove quadros, cada um com o tempo no vídeo, e cada folha recebeu o trecho da transcrição correspondente ao seu intervalo. Oito vídeos sem transcrição oficial ganharam transcrição local com o Whisper, marcada como não oficial no cartão. Cada vídeo foi apagado assim que virou folhas.

### 4. As ilustrações das diretrizes

As 1.342 ilustrações e os 61 vídeos de demonstração das páginas foram baixados, com a versão escura quando a página trata de cor, modo escuro, materiais ou ícones. Cada ilustração foi montada numa folha de quatro imagens junto com a seção da página, o texto que a antecede, a legenda e a descrição oficial em texto alternativo, para que quem olhasse pudesse dizer o que a imagem acrescenta ao texto e onde diverge dele.

### 5. A prova de leitura

Cada folha, de vídeo ou de ilustração, recebeu na própria imagem um código de cinco caracteres derivado de uma chave secreta guardada fora da base. O código só se obtém olhando a figura. O agente que abriu a folha anotou o código junto com as notas, e um script recalculou o código esperado e comparou. Resultado: 3.072 folhas de vídeo e 552 do HIG, todas com o código batendo. Nenhuma divergência.

A leitura foi feita em dezessete ondas de agentes, cada um com até 25 folhas, obrigado a descrever só o que estava na imagem, a citar os quadros que mudam entre si e a marcar como ilegível o que não desse para ler. Um vídeo só conta como assistido quando todas as folhas dele têm o código conferido.

### 6. Sínteses e verificação adversarial

Para cada vídeo e cada página com imagem, um agente escreveu a síntese do que os quadros ou as ilustrações mostram, com a referência de cada item. Um segundo agente, instruído a derrubar o primeiro, confrontou item por item com as notas e corrigiu exageros, referências erradas e conteúdo que vinha da fala em vez da imagem. Nas 158 páginas do HIG foram 206 correções e 8 itens removidos. Nos 175 vídeos, as correções somaram centenas, sempre registradas. Em 222 sínteses ficou anotada uma divergência entre o que a imagem mostra e a descrição oficial da Apple.

### 7. Integração e essência

As sínteses entraram nos cartões, e cada cartão passou a dizer quantas folhas foram vistas. Catorze agentes extraíram os padrões recorrentes das 333 sínteses, um consolidou tudo no capítulo "O que só as imagens mostram" e um verificador conferiu os 60 itens, corrigindo 20 deles.

## Estrutura

<img src="docs/assets/mapa_base.png" alt="Mapa da base: essência ao centro, HIG e vídeos ao lado, sínteses, notas e skill abaixo" width="100%">

```
kb/
  00_ESSENCIA_APPLE.md      síntese em nove capítulos
  VERIFICACAO_TEXTO.md      cobertura e fidelidade da camada de texto
  VERIFICACAO_VISUAL.md     método de prova e números da camada visual
  INDICE_VISUAL.md          status de leitura de cada vídeo e página
  hig/                      18 arquivos, um cartão por página das diretrizes
  videos/                   18 arquivos, um cartão por sessão
  visual/                   notas folha a folha de cada vídeo
  visual_hig/               notas folha a folha de cada página
  visual_sintese_hig/       síntese visual por página
  visual_sintese_videos/    síntese visual por vídeo
  essencia_visual/          padrões extraídos para o capítulo 9
  visual_logs/              registros de leitura e códigos esperados
skills/apple-design/
  SKILL.md                  a skill para o Claude Code
  PROMPT_SISTEMA.md         a versão portátil, para qualquer modelo
  sistema.md                valores do sistema visual
  plataformas.md            diferenças entre plataformas
  anti-padroes.md           os 37 anti-padrões, com fonte
  checklist.md              as 38 perguntas de revisão, com fonte
catalogo_hig.json           as 173 páginas
catalogo_videos.json        os 188 vídeos, com URL, duração e situação
*.py                        os scripts do processo, na ordem descrita acima
```

## Reproduzir

Os scripts rodam com Python 3, ffmpeg, yt-dlp e, para os vídeos sem transcrição, o whisper.cpp com o modelo large-v3-turbo. A ordem é `crawl.py`, `to_text.py`, `timed_transcripts.py`, `media_pipeline.py`, `hig_images.py`, `hig_sheets.py`, depois as ondas de leitura por agentes, `verify_codes.py`, `assemble_visual.py`, os scripts de integração, `relatorio_visual.py` e `limpeza_final.py`. O processo inteiro rodou num MacBook de 16 GB, e a leitura das folhas e as sínteses usaram cerca de 77 milhões de tokens em agentes do Claude Code.

## Uso e direitos

Material de estudo sobre design de interfaces, derivado de conteúdo público da Apple. As diretrizes, os vídeos e as ilustrações pertencem à Apple. Esta base não substitui a fonte: cada cartão traz a URL da página ou da sessão de origem.
