# Verificação de cobertura e fidelidade da base de conhecimento

Data: 15/09/2026. Escopo: /Users/guilhermelannes/Downloads/apple-design-kb/kb/ (18 arquivos em kb/hig, 18 em kb/videos) contra groups.json e os textos de origem em text/hig e text/transcripts. Nenhum arquivo da base foi alterado.

## Resumo

| Verificação | Resultado |
|---|---|
| Slugs HIG ausentes em kb/hig | 0 de 173 |
| Ids de vídeo ausentes em kb/videos | 0 de 188 |
| Arquivos marcados como não lidos até o fim | 0 de 355 entradas |
| Afirmações conferidas | 20 (12 HIG, 8 vídeos) |
| Afirmações que não conferem | 0 |
| Afirmações de ter visto telas, quadros ou vídeos | 0 |

## 1. Cobertura

Método: script Python leu groups.json (18 grupos HIG com 173 slugs únicos; 18 grupos de vídeo com 188 ids únicos), concatenou os arquivos de cada pasta e procurou cada slug e cada id, primeiro por substring e depois com fronteira de palavra. As duas buscas deram o mesmo resultado.

Slugs HIG ausentes: nenhum.
Ids de vídeo ausentes: nenhum.

Checagem adicional: todos os 173 slugs têm arquivo em text/hig e todos os 188 ids têm arquivo em text/transcripts.

## 2. Evidência de leitura

Todos os 36 arquivos têm a seção. Em kb/videos/04_wwdc2018.md o título está sem acento ("## Evidencia de leitura"), por isso uma busca pelo título acentuado não o encontra; o conteúdo existe e está completo.

Resultado do cruzamento por grupo: cada slug e cada id do grupo aparece listado na seção de evidência do arquivo correspondente (355 entradas no total).

Arquivos marcados como não lidos até o fim: nenhum. Todas as 355 entradas trazem "até o fim: sim".

Checagem adicional: o número de linhas declarado em cada entrada foi comparado com a contagem real do arquivo de origem (wc -l, tolerância de uma linha). Nenhuma divergência.

Observações registradas pelos próprios arquivos, que não são leitura incompleta:
1. kb/videos/11_wwdc2022-parte-1.md informa que wwdc2022_110342 e wwdc2022_10037 trazem "Duração: 0.0 min" no cabeçalho e marca a duração como não informada.
2. meet-with-apple_270 e meet-with-apple_274 têm só 4 linhas na origem (cabeçalho, sem transcrição); kb/videos/00_meet-with-apple.md declara "Sem transcrição disponível" para ambos, o que confere com a origem.

## 3. Fidelidade

### Parte HIG

| # | Afirmação na base | Arquivo da base | Fonte | Resultado | Trecho de origem |
|---|---|---|---|---|---|
| 1 | Permitir ampliar texto em pelo menos 200% (140% em watchOS) | 01_foundations-parte-1.md | text/hig/accessibility.md | confere | "enlarge text by at least 200 percent (or 140 percent in watchOS apps)" |
| 2 | Contraste mínimo de 4,5:1 para texto até 17 pts | 01_foundations-parte-1.md | text/hig/accessibility.md | confere | "Up to 17 pts, All, 4.5:1" (linha de tabela) |
| 3 | Camada de escurecimento de 35% sob Liquid Glass clear em fundo brilhante | 02_foundations-parte-2.md | text/hig/materials.md | confere | "a dark dimming layer of 35% opacity" |
| 4 | Aumentar cerca de 2 pontos a fonte RTL ao lado de latim em maiúsculas | 02_foundations-parte-2.md | text/hig/right-to-left.md | confere | "increase the RTL font size by about 2 points" |
| 5 | Centros de componentes visionOS a pelo menos 60 pontos, com 16 pontos ou mais entre eles | 02_foundations-parte-2.md | text/hig/spatial-layout.md | confere | "centers are at least 60 points apart, leaving 16 points or more" |
| 6 | Ícone de atividade customizado centrado em área de cerca de 70x70 pixels | 07_components-menus-and-actions.md | text/hig/activity-views.md | confere | "center it in an area measuring about 70x70 pixels" |
| 7 | Altura da menu bar é 24 pt | 07_components-menus-and-actions.md | text/hig/the-menu-bar.md | confere | "The menu bar's height is 24 pt." |
| 8 | Título de janela com menos de 15 caracteres (seção Toolbars) | 07_components-menus-and-actions.md | text/hig/toolbars.md | confere | "keep the title under 15 characters long" |
| 9 | Accessory view de alerta visionOS: altura máxima 154 pt, raio de canto 16 pt | 09_components-presentation.md | text/hig/alerts.md | confere | "maximum height of 154 pt and a 16-pt corner radius" |
| 10 | Janela visionOS padrão 1280x720 pt, a cerca de dois metros, largura aparente de cerca de três metros | 09_components-presentation.md | text/hig/windows.md | confere | "a window measures 1280x720 pt ... about two meters ... about three meters" |
| 11 | App Clip Card: imagem 1800x1200 px, título até 30 e subtítulo até 56 caracteres | 14_technologies-parte-1.md | text/hig/app-clips.md | confere | "1800x1200 px PNG or JPEG"; "no more than 30 characters ... no more than 56" |
| 12 | Tag NFC de 35 mm exige código impresso de pelo menos 1,37 polegada (3,48 cm) | 14_technologies-parte-1.md | text/hig/app-clips.md | confere | "at least 1.37 inches (3.48 cm) in diameter" |

### Parte vídeos

| # | Afirmação na base | Arquivo da base | Fonte | Resultado | Trecho de origem |
|---|---|---|---|---|---|
| 13 | Tela de referência de 375 por 667 pontos, resolução do iPhone 6 | 02_wwdc2014-2016.md | text/transcripts/wwdc2016_805.md | confere | "375 by 667 points, because this is the resolution of an iPhone 6" |
| 14 | No Top Shelf, a pessoa fica sobre um pôster por 5 segundos antes do trailer | 05_wwdc2019-parte-1.md | text/transcripts/wwdc2019_211.md | confere | "we hold on a poster image for five seconds" |
| 15 | Pixelmator Photo: modelo Core ML treinado com mais de 20 milhões de pares, mais de 32 ajustes | 05_wwdc2019-parte-1.md | text/transcripts/wwdc2019_104.md | confere | "over 20 million image pairs ... over 32 different adjustments" |
| 16 | Daltonismo afeta quase 5% da população; mirar 4,5:1 com Increase Contrast | 09_wwdc2021-parte-1.md | text/transcripts/wwdc2021_10275.md | confere | "affects almost 5% of the world's population"; "aspire to a minimum of 4.5:1" |
| 17 | Máximo de 10 App Shortcuts, recomendação de 2 a 5; disambiguation para 5 valores ou menos | 11_wwdc2022-parte-1.md | text/transcripts/wwdc2022_10169.md | confere | "The maximum you can create is 10 ... two to five high-quality app shortcuts" |
| 18 | Mais de 700 novos símbolos, biblioteca acima de 4.000 | 11_wwdc2022-parte-1.md | text/transcripts/wwdc2022_10157.md | confere | "over 700 ... 4,000 unique symbols" |
| 19 | Lua: 350.000 triângulos após redução; quase 60.000 e 110.000 removidos no culling; 180.000 depois | 15_wwdc2025-parte-1.md | text/transcripts/wwdc2025_305.md | confere | "down to just 350,000"; "just under 60,000 are removed"; "110,000 triangles were Culled"; "now just 180,000" |
| 20 | Histerese usualmente de 10 pontos no iOS; Music usa 100% de damping no toque e 80% no deslize | 04_wwdc2018.md | text/transcripts/wwdc2018_803.md | confere | "hysteresis, and is usually 10 points in iOS"; "we use 100% damping"; "we use 80%" |

### Verificações adicionais (fora da amostra de 20, todas conferem)

| Afirmação | Fonte | Trecho de origem |
|---|---|---|
| Botão Sign in with Apple: fonte do título é 43% da altura; altura é 233% da fonte (16_technologies-parte-3.md) | text/hig/sign-in-with-apple.md | "the title's font size would be 43% of the button's height" |
| Imagem de arraste após cerca de 3 pontos (03_patterns-parte-1.md) | text/hig/drag-and-drop.md | "as soon as people drag a selection about three points" |
| Tooltip com no máximo 60 a 75 caracteres (03_patterns-parte-1.md) | text/hig/offering-help.md | "a maximum of 60 to 75 characters" |
| tvOS: atraso mínimo de 0,5 s para overlay; thumbnails de 160 px (03_patterns-parte-1.md) | text/hig/playing-video.md | "minimum delay of 0.5 seconds"; "each measure 160 px in width" |
| Complicação circular 40mm: imagem 42x42 pt (12_components-system-experiences.md) | text/hig/complications.md | "Image, 42x42 pt (84x84 px @2x)" |
| Tamanhos de botão macOS 28x28/20x20 e tvOS 66x66/56x56 (00_getting-started.md) | text/hig/designing-for-games.md | "macOS, 28x28 pt, 20x20 pt"; "tvOS, 66x66 pt, 56x56 pt" |
| Lowe's: time de três pessoas numa empresa de 300 mil associados, fala de Steve Lindgren (00_meet-with-apple.md) | text/transcripts/meet-with-apple_208.md | "Lowe's has 300,000 associates"; "really three core members" |
| Canvas de 1024px para iPhone, iPad e Mac; Watch 1088px (15_wwdc2025-parte-1.md) | text/transcripts/wwdc2025_361.md | "the same 1024px canvas"; "Watch is now 1088px" |
| Área mínima de alvo ocular de 60 pontos (13_wwdc2023.md) | text/transcripts/wwdc2023_10073.md | "minimum area that your element needs for eye target is 60 points" |
| "15-second highlights" no botão Share do controle (09_wwdc2021-parte-1.md) | text/transcripts/wwdc2021_10081.md | "15-second highlights" |
| Citação "Do not delegate critical thinking to these tools." (17_wwdc2026.md) | text/transcripts/wwdc2026_227.md | frase idêntica na linha 14 |
| New York Times: ler a história levaria "way more than two to five seconds" (02_wwdc2014-2016.md) | text/transcripts/wwdc2015_802.md | "way more than two to five seconds" |

## 4. Honestidade

Buscas feitas em kb/ (excluindo "framework"): "vi ", "vimos", "assisti", "assistimos", "observei", "olhei", "no vídeo aparece", "mostra na tela", "aparece na tela", "na tela aparece", "o quadro mostra", "nos quadros", "no quadro", "captura de tela", "screenshot", "olhando o vídeo", "frames do", "nos frames", "imagem do vídeo", "slide", "ao vivo".

Afirmações de ter visto telas, quadros ou vídeos: nenhuma.

Ocorrências que parecem visuais mas são texto da própria base ou descrição tirada da fala, conferidas na transcrição:
1. kb/hig/12_components-system-experiences.md:526, "o que aparece na tela": trata da regra da Siri, não de observação.
2. kb/videos/14_wwdc2024.md:55, citação "Notice how the two screens cast light effects on their surroundings": frase literal da transcrição wwdc2024_10116, não observação própria.
3. kb/videos/11_wwdc2022-parte-1.md:121, "demonstração ao vivo do slider de Variable Color": a transcrição wwdc2022_10158 narra a demo ("pull the slider all the way down").
4. kb/videos/08_wwdc2020-parte-2.md:64, estudo de caso com Starstruck e Sneaky Sasquatch: ambos nomeados na fala de wwdc2020_10020.
5. kb/videos/14_wwdc2024.md:256, 280 e 291, construções "ao vivo" de efeitos: a transcrição wwdc2024_10151 narra a construção passo a passo (RippleModifier, shader Ripple).
6. Ocorrências de "visualmente", "ao vivo" em sentido de conteúdo ao vivo (live viewing) e "slide" (Slide Over, slides do Keynote) em kb/hig e kb/videos: vocabulário do conteúdo, sem afirmação de visualização.

Uma inferência de leitura, não visual, fica registrada: kb/videos/14_wwdc2024.md:291 afirma que em wwdc2024_10151 "não há apps de terceiros reais citados". Não foi feita varredura completa da transcrição para confirmar a ausência.

## 5. Correção em 15/09/2026, depois da checagem estrita por cartão

A checagem de cobertura acima procurou cada id em qualquer lugar do arquivo. Isso deixou passar um vídeo cujo id só aparecia na lista de evidência de leitura, sem cartão próprio. A checagem foi refeita exigindo um título próprio no formato "## título (id: ..., duração)" para cada vídeo e "## título (slug: ...)" para cada página do HIG.

Resultado da checagem estrita:
1. HIG: os 173 slugs têm título próprio. Quatro páginas de índice de coleção (presentation, content, navigation-and-search, status) têm corpo curto porque a própria página não tem texto além da lista.
2. Vídeos: faltava o cartão de wwdc2023_10115 (Design with SwiftUI, com transcrição oficial). Oito vídeos com mídia e sem transcrição oficial tinham cartão vazio ou nenhum cartão: meet-with-apple_270, meet-with-apple_274, tech-talks_111461, tech-talks_111462, tech-talks_111463, tech-talks_111466, wwdc2020_20022 e wwdc2026_8012.
3. Os nove cartões foram escritos a partir da transcrição inteira (oficial no caso de wwdc2023_10115, automática local com Whisper nos outros oito, marcada assim no próprio cartão) e cada um passou por um verificador que confrontou todas as afirmações com a transcrição. Nenhuma afirmação foi removida por falta de base, exceto duas (uma em wwdc2020_20022 e uma em wwdc2026_8012); as demais correções foram de sentido ou de precisão.
4. Depois da inserção: nenhum vídeo com mídia sem cartão, nenhum cartão curto, nenhum cartão duplicado. Os 13 vídeos sem mídia no site continuam só listados, sem cartão, porque não há transcrição nem vídeo.
5. Durações erradas por erro meu na coleta, não do site. Na montagem da tabela de vídeos, as durações da lista do tópico Design foram associadas ao vídeo vizinho, fora de ordem. O site mostra a duração certa ao lado de cada vídeo. Comprovação: nos 108 vídeos em que a duração registrada divergia, a duração do arquivo baixado é idêntica à do arquivo no servidor da Apple, e os 443 links de mídia carregam o número do próprio vídeo, então nenhum vídeo foi trocado nem baixado pela metade. Correção aplicada: a duração passou a vir do arquivo medido (175 vídeos com mídia) e, nos vídeos sem mídia, da lista do tópico Design casada por título. Foram corrigidos o manifesto, o índice de vídeos, os cabeçalhos das transcrições e os títulos dos cartões.
