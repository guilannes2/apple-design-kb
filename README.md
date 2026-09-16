# Apple Design KB

Uma base de conhecimento sobre como a Apple pensa, desenha e constrói interfaces, destilada da própria Apple: as 173 páginas das Human Interface Guidelines e os 188 vídeos de design publicados em developer.apple.com/design, incluindo o que aparece na tela desses vídeos e nas ilustrações das diretrizes. Vem com uma skill que tranca o modelo de linguagem dentro desse design system: nada de fora entra, nada é inventado, e nenhuma regra da Apple é quebrada.

A base está em português. Ela existe para ser usada por pessoas e por agentes de IA que precisem desenhar, revisar ou construir uma interface no padrão da Apple, com a fonte de cada afirmação indicada.

## Para que serve

Você instala a skill no modelo de linguagem com que trabalha e passa a construir sistemas com o acabamento da Apple. O modelo fica sob quatro leis:

1. Só o design system da Apple. Componentes, navegação, tipografia, cor, materiais, espaçamento, movimento, escrita e acessibilidade vêm da base. Nada de outro design system, tema padrão de biblioteca ou estética própria.
2. Proibido inventar. Sem resposta na base, o modelo pesquisa nas páginas da própria Apple e cita a URL. Sem resultado, ele diz que a Apple não publica regra sobre aquilo e marca a proposta como inferência.
3. Nunca quebrar uma regra da Apple. Antes de entregar, toda tela passa por um checklist de 38 perguntas e por uma lista de 37 anti-padrões que a Apple condena. O modelo não implementa pedido que viola uma regra: mostra a regra, cita a fonte e oferece a alternativa da Apple.
4. Toda decisão tem fonte. Cada componente, valor e comportamento vem com a página das diretrizes ou a sessão que o sustenta, e a entrega termina com uma tabela de conformidade.

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

### 8. Correções de honestidade ao longo do caminho

Três erros meus foram encontrados e corrigidos, e o relatório registra cada um. Nove vídeos estavam sem cartão próprio ou com cartão vazio, porque a checagem de cobertura procurava o id em qualquer lugar do arquivo em vez de exigir um título próprio. As durações registradas na coleta estavam associadas ao vídeo vizinho, e foram refeitas medindo os arquivos, que conferem com o servidor da Apple. E a seção de limites da essência ainda dizia que as imagens não tinham sido vistas depois que já tinham.

### 9. Limpeza

Ao fim, 22 GB de vídeo e 1,1 GB de folhas e ilustrações foram apagados. Ficaram o texto, as notas do que foi visto, as sínteses, os registros e as verificações.

## O que a base não faz

- Não é uma leitura quadro a quadro literal. A amostragem é por mudança de cena, com um quadro a cada 12 segundos no mínimo. Um efeito rápido demais pode não aparecer entre dois quadros, e onde isso aconteceu a nota diz.
- Treze vídeos não têm arquivo nem transcrição no site e ficaram apenas listados.
- Movimento contínuo aparece como diferença entre quadros parados, e as notas escrevem assim.
- O conteúdo da Apple está parafraseado. Citações literais têm no máximo 15 palavras. Os textos integrais e a mídia não fazem parte deste repositório.

## Estrutura

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
