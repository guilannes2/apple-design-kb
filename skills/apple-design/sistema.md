# O sistema visual da Apple: valores e regras

Cópia literal da seção 3 da essência (`kb/00_ESSENCIA_APPLE.md`): tipografia, cor, materiais, layout e espaçamento, ícones e símbolos, movimento, háptica e som, escrita e acessibilidade. Os números aqui são os únicos que a skill pode usar sem pesquisar.

## O sistema

Regras e números consolidados. Quando duas fontes divergem num número, as duas aparecem, com a indicação de qual é diretriz e qual é fala.

### 3.1 Tipografia

Famílias e regras gerais
- Duas famílias do sistema: San Francisco (SF Pro, SF Compact, SF Mono, variantes arredondadas e por script, como SF Arabic) e New York, serifada; ambas em formato variável com tamanhos ópticos dinâmicos (`hig/02 typography`). Em 2022 a SF ganhou o eixo de largura: Condensed, Compressed e Expanded, além de Regular; para a maioria dos casos, dois ou três estilos bastam (`vid/11 wwdc2022_110381`).
- Fonte do sistema por plataforma: SF Pro em iOS, iPadOS, macOS, tvOS e visionOS; SF Compact no watchOS, com SF Compact Rounded nas complicações (`hig/02 typography`).
- Prefira os pesos Regular, Medium, Semibold e Bold; evite Ultralight, Thin e Light, sobretudo em texto pequeno; fontes finas pedem tamanhos maiores que o recomendado (`hig/02 typography`; `hig/01 accessibility`).
- Minimize o número de tipografias; tipografias demais obscurecem a hierarquia (`hig/02 typography`). Em 2017 a recomendação falada era usar de dois a três text styles por tela (`vid/03 wwdc2017_812`).
- Use os text styles do sistema em vez de tamanhos "no olho": eles carregam hierarquia e suporte automático a Dynamic Type (`hig/02 typography`; `vid/15 wwdc2025_359`).
- Não embuta as fontes do sistema no app; em mockups fiéis, ajuste o tracking, porque em execução o sistema ajusta o tracking a cada tamanho (`hig/02 typography`).
- Fonte customizada: legível em todos os tamanhos, com Dynamic Type e Bold Text implementados manualmente; costuma funcionar bem para títulos com a fonte do sistema no corpo (`hig/01 branding`; `hig/02 typography`). Tipografia deve ser funcional antes de expressiva (`vid/17 wwdc2026_251`). Para escolher uma, parta do uso pretendido e da impressão desejada, entenda estrutura e contraste, compare candidatas no mesmo tamanho de ponto e não escolha pelo nome combinar com o tema (`vid/03 wwdc2017_815`).

Tamanhos padrão e mínimos (`hig/01 accessibility`; `hig/02 typography`; `hig/00 designing-for-games`)

| Plataforma | Padrão | Mínimo |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

A sessão de jogos de 2024 repete os mesmos números para iPhone, iPad (17 e 11) e Mac (13 e 10) e recomenda usar scroll views em vez de reduzir o tipo quando falta espaço (`vid/14 wwdc2024_10085`). Widgets: 11 pt ou mais (`hig/12 widgets`).

Dynamic Type no iOS e iPadOS, tamanho Large (padrão), em tamanho e leading, pontos (`hig/02 typography`)
- Large Title 34/41; Title 1 28/34; Title 2 22/28; Title 3 20/25; Headline 17/22; Body 17/22; Callout 16/21; Subhead 15/20; Footnote 13/18; Caption 1 12/16; Caption 2 11/13.
- No maior tamanho de acessibilidade (AX5): Body 53/62, Large Title 60/70.
- macOS (sem Dynamic Type): Body 13/16, Headline 13/16 em Bold, Large Title 26/32 (`hig/02 typography`; `vid/08 wwdc2020_10104`, text styles centrados no corpo de 13 pt, sem controle deslizante de tamanho no sistema).
- tvOS: Title 1 76/96, Body 29/36, Caption 2 23/30 (`hig/02 typography`).
- watchOS, tamanho Large (40, 41 e 42 mm): Body 16/18,5, Large Title 36/38,5 (`hig/02 typography`).

Regras de escala e leitura
- Suporte ampliação de texto de pelo menos 200%, ou 140% no watchOS (`hig/01 accessibility`).
- Se o texto pode crescer, deve crescer; use a largura disponível; não trunque; escale glifos junto com o texto (`vid/05 wwdc2019_244`). Em tamanhos grandes, troque layouts lado a lado por empilhados e reduza colunas; mantenha elementos primários no topo (`hig/02 typography`; `vid/08 wwdc2020_10020`).
- Não aumente títulos de abas junto com o conteúdo quando isso não for importante (`hig/02 typography`).
- Tight leading reduz a altura de linha em 2 pt e loose leading aumenta 2 pt no iOS e macOS; no watchOS o ajuste é de 1 pt (exemplo falado: Body com linha de 22 pt vai a 20 ou 24) (`vid/07 wwdc2020_10175`). Não use tight leading com três ou mais linhas (`hig/02 typography`).
- Tracking anda em par com o tamanho óptico: na SF Pro vai de +41 milésimos de em a 6 pt até 0 a partir de 80 pt (`hig/02 typography`). A troca entre desenho Text e Display acontece hoje entre 17 e 28 pt; antes o corte era 20 pt. Para strings truncadas, prefira o aperto automático de tracking ao kerning manual (`vid/07 wwdc2020_10175`).
- Readability margins limitam o comprimento de linha, porque linhas que vão até a margem padrão ficam longas demais para o olho (`vid/03 wwdc2017_812`).
- visionOS: pesos mais fortes (Body em Medium em vez de Regular; títulos em Bold em vez de Semibold) e tracking levemente maior; texto branco por padrão; texto sem fundo em negrito e sem sombra; texto 2D, não 3D; texto voltado para a pessoa (billboarding); Extra Large Title 1 e 2 para layouts editoriais (`hig/02 typography`; `vid/13 wwdc2023_10076`, `wwdc2023_10072`).
- Idiomas da direita para a esquerda: a diretriz fala em cerca de 2 pt a mais na fonte RTL ao lado de latim em maiúsculas (`hig/02 right-to-left`); a sessão sobre árabe fala em 10% a mais e em tracking zero quando a fonte não é otimizada, com opacidade aplicada à palavra inteira (`vid/12 wwdc2022_110441`).
- Mac Catalyst com idioma iPad: o texto de 17 pt vira 13 pt (escala de 77%) (`hig/15 mac-catalyst`; `vid/05 wwdc2019_809`).

### 3.2 Cor

- Use cor para comunicar, não para decorar; não use a mesma cor para significados diferentes (`hig/01 color`).
- Cores do sistema já trazem variantes clara, escura e de contraste aumentado; cor customizada precisa das quatro variantes; mesmo apps de um só modo precisam fornecer claro e escuro para a adaptatividade do Liquid Glass (`hig/01 color`).
- Cor semântica descreve o propósito, não o valor (`vid/05 wwdc2019_808`; `vid/15 wwdc2025_359`). Não fixe valores de cor do sistema no código e não redefina a semântica, como usar a cor de separador para texto (`hig/01 color`).
- Nunca use só cor para diferenciar, indicar interatividade ou transmitir informação essencial; acrescente forma ou texto; suporte Differentiate Without Color (`hig/01 color`, `accessibility`; `vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`).
- Contraste: texto até 17 pt, 4,5:1; texto de 18 pt ou em negrito, 3:1 (critério WCAG AA usado pelo Accessibility Inspector) (`hig/01 accessibility`). Dark Mode: mínimo 4,5:1 e, para cores customizadas em texto pequeno, buscar 7:1 (`hig/01 dark-mode`). Tint colors: 4,5:1 ou mais (`vid/05 wwdc2019_808`). A sessão de 2021 chama os 4,5:1 com Increase Contrast de "regra aproximada", porque combinações que passam ainda podem ser difíceis de ler (`vid/09 wwdc2021_10275`).
- Cor de destaque com critério: reserve para ações primárias e indicadores de status (badge de não lido, aba selecionada) (`hig/01 branding`). No Liquid Glass, aplique cor ao fundo da ação primária, não a símbolos e texto, e não a vários controles de uma vez (`hig/01 color`). Tint só para transmitir significado, como uma chamada para ação, nunca por efeito visual (`vid/15 wwdc2025_323`, `wwdc2025_284`). Tintar todos os elementos faz nada se destacar (`vid/16 wwdc2025_219`).
- Sobre conteúdo colorido, prefira toolbars e tab bars monocromáticas; evite cor de rótulo parecida com o fundo do conteúdo (`hig/01 color`; `hig/07 buttons`, `toolbars`; `hig/08 tab-bars`).
- Para expressar marca por cor, leve a cor para a camada de conteúdo, onde ela rola sob os controles de vidro (`hig/01 branding`; `vid/17 wwdc2026_251`, mover a cor das barras para o conteúdo).
- Dark Mode: não ofereça ajuste de aparência próprio do app; teste Auto, Increase Contrast e Reduce Transparency; iOS usa fundos base (recuam) e elevated (avançam) (`hig/01 dark-mode`). Pense em luzes diminuídas, não em cores invertidas (`vid/05 wwdc2019_808`). Em 2026, não suportar Dark Mode é descrito como experiência negativa num dispositivo tão pessoal (`vid/17 wwdc2026_251`). Dark Mode não é suportado em visionOS nem em watchOS (`hig/01 dark-mode`).
- Preenchimentos e a maioria dos separadores são semitransparentes; há seis cinzas opacos para quando a transparência cria ilusões ópticas (`vid/05 wwdc2019_808`).
- Cor tem significado cultural: vermelho é perigo em algumas culturas e positivo em outras; branco é luto em alguns lugares e pureza em outros; no Stocks com região China continental, ganho aparece em vermelho (`hig/01 color`, `inclusion`; `vid/09 wwdc2021_10275`).
- Cor ampla: Display P3 a 16 bits por canal, exportada em PNG, com perfil de cor em cada imagem (`hig/01 color`, `images`). Pergunte antes se o conteúdo pede P3; converta perfil, nunca atribua (`vid/03 wwdc2017_821`).
- Por plataforma: no macOS, a cor de destaque escolhida pela pessoa substitui a do app, e as interfaces devem ser mais neutras (`hig/01 color`; `vid/05 wwdc2019_809`); no tvOS, não indique foco só por cor (`hig/01 color`); no visionOS, cor com moderação sobre o vidro, preferindo texto e símbolos brancos e cor em fundos ou botões inteiros (`hig/01 color`; `vid/13 wwdc2023_10076`); no watchOS, cor de fundo com função, não adorno (`hig/01 color`; `vid/13 wwdc2023_10026`, `wwdc2023_10138`); no CarPlay, paleta limitada, mesma cor nunca para interativo e não interativo, e teste em carro real (`hig/14 carplay`).
- Elementos de cor fixa não se alteram: Activity rings (Move 250,17,79; Exercise 166,255,0; Stand 0,255,246), sempre sobre preto (`hig/11 activity-rings`); indicadores de page control não devem ser coloridos (`hig/09 page-controls`).

### 3.3 Materiais

- Liquid Glass forma uma camada funcional de controles e navegação que flutua acima do conteúdo; não se usa na camada de conteúdo (use materiais padrão ali), exceto em controles transitórios como sliders e toggles durante a interação (`hig/02 materials`). Aplicá-lo a uma table view de conteúdo compete com o resto e confunde a hierarquia (`vid/16 wwdc2025_219`).
- Use com moderação; é uma camada interativa sob a ponta dos dedos, então limite-a aos elementos mais importantes e prefira controles do sistema (`hig/02 materials`; `vid/15 wwdc2025_284`).
- Nunca vidro sobre vidro; elementos em cima do Liquid Glass usam preenchimento, transparência e vibrância (`vid/16 wwdc2025_219`). Vidros próximos em contêineres diferentes se comportam de modo inconsistente; agrupe-os num contêiner comum (`vid/15 wwdc2025_323`, `wwdc2025_284`).
- Duas variantes que nunca se misturam. Regular: a versátil, adaptativa, indicada quando o fundo pode prejudicar a legibilidade (alertas, sidebars, popovers com texto). Clear: só sobre conteúdo rico em mídia, com camada de escurecimento de 35% sobre conteúdo claro (`hig/02 materials`); a sessão de 2025 exige três condições juntas: conteúdo rico em mídia, o escurecimento não prejudicar o conteúdo, e conteúdo acima ousado e brilhante (`vid/16 wwdc2025_219`).
- O material se adapta: elementos pequenos alternam entre claro e escuro conforme o que passa atrás; elementos grandes, como menus e sidebars, não alternam, porque seria distrativo; ao crescer, o vidro simula maior espessura (`vid/16 wwdc2025_219`). No UIKit, vidro maior fica mais opaco (`vid/15 wwdc2025_284`).
- Materiais padrão no iOS: ultra thin, thin, regular (padrão) e thick. Escolha pelo significado semântico, nunca pela cor aparente; mais espesso dá contraste, mais fino preserva contexto; evite quaternary sobre thin e ultra thin (`hig/02 materials`; `vid/05 wwdc2019_808`). Use cores vibrantes do sistema sobre materiais (`hig/02 materials`).
- Scroll edge effect não é decorativo: só atrás de interface flutuante, um por view. Soft é o padrão no iOS e iPadOS; hard é mais comum no macOS e em interfaces densas, texto interativo e cabeçalhos fixos; os dois não se misturam (`hig/09 scroll-views`; `vid/16 wwdc2025_356`). Use-o no lugar de fundo sólido sob controles (`hig/01 layout`).
- Remova fundos e bordas customizados de barras; hierarquia vem de layout e agrupamento (`vid/16 wwdc2025_356`; `vid/15 wwdc2025_284`; `hig/07 toolbars`).
- Acessibilidade modifica o material automaticamente: Reduced Transparency deixa o vidro mais fosco, Increased Contrast o torna predominantemente preto ou branco com borda, Reduced Motion remove a elasticidade (`vid/16 wwdc2025_219`).
- visionOS: janelas usam glass, que se adapta à luz do ambiente e não tem modo escuro; evite janelas opacas; material mais escuro separa seções, mais claro chama atenção para elementos interativos; não empilhe materiais claros (`hig/02 materials`; `hig/09 windows`; `vid/13 wwdc2023_10076`).
- macOS: sidebar translúcida, nunca cor sólida, imagem ou padrão, porque a vibração sinaliza qual janela tem o foco (`vid/05 wwdc2019_809`).
- watchOS: materiais dão contexto em modais de tela cheia e não devem ser removidos (`hig/02 materials`); há quatro materiais de fundo, Ultra Thin a Thick (`vid/13 wwdc2023_10138`).

### 3.4 Layout e espaçamento

Princípios
- Ordene por importância: o que importa perto do topo e da borda inicial (`hig/01 layout`).
- Alinhamento comunica relação; indentação comunica subordinação; agrupe com espaço negativo, contêineres ou separadores (`hig/01 layout`). Proximidade, agrupamento e mapeamento seguem os princípios de 2017 (`vid/03 wwdc2017_802`).
- Decida layout por size class, não por dispositivo ou orientação; mantenha a mesma funcionalidade quando a size class muda (`hig/01 layout`; `vid/03 wwdc2017_812`).
- Respeite safe areas, margens e guias do sistema (`hig/01 layout`; `vid/01 tech-talks_801`).
- Estenda conteúdo de fundo sob sidebars e barras com background extension effect (`hig/01 layout`; `vid/16 wwdc2025_356`).
- Concentricidade: raio interno somado ao padding dá o raio externo (`vid/13 wwdc2023_10076`). Três formas: fixed (raio constante), capsule (raio igual a metade da altura) e concentric (raio do pai menos o padding) (`vid/16 wwdc2025_356`).
- Mudanças de layout por redimensionamento não devem ser destrutivas: volte ao estado inicial quando possível (`vid/15 wwdc2025_208`).
- macOS: nada crítico na parte inferior da janela, porque a pessoa costuma empurrar essa borda para fora da tela (`hig/01 layout`; `hig/08 sidebars`; `hig/09 windows`; `vid/05 wwdc2019_809`).

Alvos de toque e controles (`hig/01 accessibility`; `hig/00 designing-for-games`; `hig/07 buttons`)

| Plataforma | Padrão | Mínimo |
|---|---|---|
| iOS, iPadOS | 44 x 44 pt | 28 x 28 pt |
| macOS | 28 x 28 pt | 20 x 20 pt |
| tvOS | 66 x 66 pt | 56 x 56 pt |
| visionOS | 60 x 60 pt | 28 x 28 pt |
| watchOS | 44 x 44 pt | 28 x 28 pt |

- Padding ao redor de controles: cerca de 12 pt com bezel e cerca de 24 pt sem bezel (`hig/01 accessibility`; `hig/13 pointing-devices`; `vid/07 wwdc2020_10640`).
- A área de toque pode ser maior que a área visual, e deve ser em controles pequenos (`vid/04 wwdc2018_804`).
- visionOS: centros a pelo menos 60 pt de distância, com 16 pt ou mais entre elementos (`hig/01 layout`; `hig/02 spatial-layout`; `hig/13 eyes`). Um botão de 44 pt precisa de 8 pt ao redor; pilhas de botões, 16 pt; itens de lista e menu, 4 pt de padding; ornamentos sobrepõem a borda inferior da janela em 20 pt (`vid/13 wwdc2023_10076`). Botões com 60 pt ou mais ganham 4 pt de padding para o hover não se sobrepor; tamanhos padrão Mini 28, Small 32, Regular 44, Large 52, Extra large 64 pt (`hig/07 buttons`). Para objetos 3D a um metro, 60 pt correspondem a cerca de 2,5 graus, ou 4,4 cm (`vid/16 wwdc2025_303`).
- watchOS: no máximo três botões com glifo ou dois com texto lado a lado (`hig/01 layout`). A fala de 2015 dava 80 x 80 px para controles circulares no relógio de 42 mm e nunca mais de três botões lado a lado (`vid/02 wwdc2015_805`).

Medidas de estrutura
- tvOS: safe area com 60 pt no topo e na base e 80 pt nas laterais (`hig/01 layout`); a sessão de 2019 falou em 90 pt nas laterais e 60 pt em cima e embaixo (`vid/05 wwdc2019_211`). Grades de foco com 40 pt de espaço horizontal e 100 pt vertical mínimo, de 860 pt por coluna em duas colunas a 160 pt em nove (`hig/01 layout`). Tab bar com 68 pt de altura a 46 pt do topo (`hig/08 tab-bars`). Split view com um terço e dois terços (`hig/06 split-views`).
- macOS: menu bar com 24 pt; nome do app no item About com 16 caracteres ou menos (`hig/07 the-menu-bar`); divisor fino de split view com 1 pt (`hig/06 split-views`).
- Toolbar: título com menos de 15 caracteres; cerca de três grupos no máximo; zonas leading, center e trailing; uma única ação primária proeminente na trailing (`hig/07 toolbars`). Tab view do Mac: no máximo seis abas (`hig/06 tab-views`). Tab bar customizável do iPad: lista padrão de cinco ou menos (`hig/08 tab-bars`). Tab bar do visionOS: até seis itens (`vid/13 wwdc2023_10076`).
- Segmented control: até cinco a sete segmentos em interfaces largas, cerca de cinco no iPhone (`hig/10 segmented-controls`). Radio buttons em grupos de dois a cinco (`hig/10 toggles`). Page control: acima de cerca de dez pontos fica difícil de contar (`hig/09 page-controls`).
- Sheets: detents large e medium, este com cerca de metade da altura (`hig/09 sheets`).
- Widgets: margem padrão de 16 pt e 11 pt para agrupamentos internos (`hig/12 widgets`; `vid/07 wwdc2020_10103`); no widget pequeno, no máximo quatro peças de informação (`vid/07 wwdc2020_10103`). Live Activities: margem de 14 pt na Lock Screen, compartilhada com notificações; raio da Dynamic Island de 44 pt (`hig/12 live-activities`; `vid/13 wwdc2023_10194`).
- Snippets: a diretriz dá altura máxima de 400 pt para a view customizada (`hig/12 snippets`); a sessão de 2025 recomenda não passar de 340 pt (`vid/16 wwdc2025_281`).
- visionOS: janela padrão de 1280 x 720 pt, posicionada a cerca de dois metros, com largura aparente de cerca de três metros (`hig/09 windows`); leitura prolongada a pelo menos um metro (`hig/13 eyes`); limite de cerca de 1,5 m a partir da cabeça nos estilos progressive e full; progressive de 120 a 360 graus (`hig/01 immersive-experiences`); accessory view de alerta com até 154 pt de altura e raio de 16 pt (`hig/09 alerts`).
- iPhone X: 375 x 812 pt, 145 pt a mais de altura que a tela de 4,7 polegadas (`vid/01 tech-talks_801`). Apple Watch Series 7: 176 x 215 pt (41 mm) e 198 x 242 pt (45 mm) de área ativa (`vid/01 tech-talks_10884`).
- Arraste: imagem de arraste após cerca de 3 pt de movimento (`hig/03 drag-and-drop`); swipe reconhecido após histerese de cerca de 10 pt (`vid/04 wwdc2018_803`). Ponteiro do iPadOS (2020): círculo de 19 pt; botões de toolbar com 37 pt de altura (`vid/07 wwdc2020_10640`).

### 3.5 Ícones e símbolos

Ícone de app
- Tamanhos: 1024 x 1024 px para iOS, iPadOS e macOS (retângulo arredondado) e visionOS (círculo); 1088 x 1088 px no watchOS (círculo); 800 x 480 px no tvOS, com duas a cinco camadas e parallax (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`).
- Camadas sem máscara aplicada, conteúdo centralizado; o sistema aplica máscara, realces especulares, sombras e desfoque; não inclua chanfros, sombras ou brilhos "assados" (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`). No Icon Composer, até quatro grupos (`vid/15 wwdc2025_361`).
- Simplicidade: um conceito com poucas formas; texto só se essencial; prefira ilustração a foto; não replique a interface nem hardware Apple (`hig/01 app-icons`). Metáfora, simplicidade, conexão e linhagem; teste na Home Screen, dentro de pasta e em tamanho pequeno, apertando os olhos (`vid/03 wwdc2017_822`).
- Aparências consistentes entre padrão, escuro, claro translúcido e tintado, sem trocar elementos entre variantes (`hig/01 app-icons`); no modo mono, pelo menos um elemento branco (`vid/15 wwdc2025_361`).
- Com o novo material: evite objetos 3D realistas e perspectivas complexas, prefira vista frontal; translucidez com moderação ("Less is more"); evite bordas afiadas e linhas finas; prefira os gradientes System Light e System Dark a branco ou preto puros (`vid/16 wwdc2025_220`).

Ícones de interface e glifos
- Simplificados, com metáforas familiares; consistentes em tamanho, detalhe, peso e perspectiva; peso casado com o texto adjacente; alinhamento óptico com padding quando preciso; formato vetorial; rótulo de acessibilidade para ícones customizados (`hig/01 icons`).
- Desenhe glifos como conjunto: normalize peso óptico e espessura de linha; posicione pelo centro óptico, como o Play deslocado alguns pixels à direita; teste em contexto e no dispositivo (`vid/03 wwdc2017_823`).
- Prefira conceitos universais e figuras humanas neutras em gênero (`hig/01 icons`, `inclusion`; `vid/03 wwdc2017_819`, `wwdc2017_823`).
- Use o mesmo símbolo para a mesma ação em todos os dispositivos; quando não há atalho visual claro (Select, Edit), use texto; para ações muito relacionadas, o símbolo aparece uma vez para o grupo (`vid/16 wwdc2025_356`). Reserve reticências para overflow (`hig/00 designing-for-iphone-duo`).
- Respeite as convenções de cada plataforma mesmo com estilo próprio, como o ícone de compartilhar (`vid/17 wwdc2026_251`; `vid/03 wwdc2017_802`).

SF Symbols
- Nove pesos, de ultralight a black, casados com os pesos da SF; três escalas relativas à cap height (`hig/02 sf-symbols`); small cerca de 20% menor e large cerca de 30% maior que medium (`vid/07 wwdc2020_10207`).
- Especifique em pontos tipográficos, como texto; não force largura e altura; alinhe pela baseline ao lado de texto (`vid/05 wwdc2019_206`; `vid/07 wwdc2020_10207`).
- Modos de renderização: monochrome, hierarchical, palette e multicolor; escolha pela intenção e confirme no contexto, mesmo com o modo automático (`hig/02 sf-symbols`; `vid/09 wwdc2021_10349`; `vid/11 wwdc2022_10157`). Variable color representa mudança ao longo do tempo, não profundidade (`hig/02 sf-symbols`; `vid/11 wwdc2022_10157`).
- Outline combina com texto, toolbars, navigation bars e listas; fill dá ênfase em tab bars do iOS, swipe actions e seleção; símbolo em círculo ajuda em tamanho pequeno (`hig/02 sf-symbols`; `vid/09 wwdc2021_10097`). Forneça a versão outline; o sistema escolhe fill na tab bar (`vid/14 wwdc2024_10147`; `vid/09 wwdc2021_10349`).
- Proibido usar SF Symbols em ícones de app, logotipos ou marcas (`hig/02 sf-symbols`).
- Símbolos customizados partem de um símbolo existente e do template, com paths fechados, mesma quantidade e ordem de paths entre variantes; três desenhos geram as demais variantes por interpolação (`hig/02 sf-symbols`; `vid/09 wwdc2021_10250`; `vid/13 wwdc2023_10257`).
- A biblioteca foi descrita com mais de 1.000 símbolos em 2019, mais de 3.000 em 2021, mais de 4.000 em 2022, mais de 5.000 em 2023, mais de 6.000 em 2024 e mais de 7.000 em 2026 (`vid/05 wwdc2019_206`; `vid/09 wwdc2021_10097`; `vid/11 wwdc2022_10157`; `vid/13 wwdc2023_10197`; `vid/14 wwdc2024_10188`; `vid/17 wwdc2026_251`).

### 3.6 Movimento

- Movimento com propósito, nunca pela animação em si; opcional, complementado por háptica e som; feedback breve e preciso; evite animar interações frequentes, que o sistema já anima; deixe a pessoa cancelar em vez de esperar (`hig/02 motion`).
- Fluidez vem de comportamento, não de animação prescrita: resposta instantânea; gestos redirecionáveis e interrompíveis; entrada e saída pelo mesmo caminho; a interface cresce na direção do estado final; bordas elásticas, nunca parada seca; rastreamento um para um; conteúdo move com o dedo em posição relativa (`vid/04 wwdc2018_803`).
- Molas: dois parâmetros de design, damping e response; comece com 100% de damping; use quique (o exemplo cita 80%) só quando o gesto de origem tem momento; projete o ponto final pela velocidade (`vid/04 wwdc2018_803`). Em 2026 a sessão de agentes descreve ease e spring com stiffness, damping e mass (`vid/17 wwdc2026_227`).
- Confirmação de toque instantânea; animações lentas ou em fade fazem o controle parecer lento (`vid/04 wwdc2018_804`). Duplo toque atrasa o toque simples em cerca de meio segundo (`vid/04 wwdc2018_803`).
- Continuidade: a transição zoom mantém os mesmos elementos visíveis (`vid/14 wwdc2024_10145`); um botão pode se transformar no menu que abre (`vid/00 meet-with-apple_208`; `vid/15 wwdc2025_284`); elementos de vidro materializam modulando a luz em vez de simples fade (`vid/16 wwdc2025_219`); no watchOS, o mesmo objeto é animado entre páginas para dar permanência (`vid/13 wwdc2023_10026`).
- Limites de duração: animações de Live Activities e de atualização de widgets até 2 segundos (`hig/12 live-activities`, `widgets`); overlays interativos no tvOS com atraso mínimo de 0,5 s para pausar (`hig/03 playing-video`); jogos entre 30 e 60 fps (`hig/02 motion`); cena de AR atualizada 60 vezes por segundo (`hig/14 augmented-reality`).
- Reduce Motion: reduza animações automáticas e repetitivas; aperte as molas; acompanhe o gesto; evite animar profundidade no eixo z; troque transições em x, y e z por fades; evite animar blur (`hig/01 accessibility`); ofereça cross-fade (`vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`); em hover customizado, ofereça alternativa em cross-fade (`vid/14 wwdc2024_10152`).
- visionOS: evite movimento na periferia; objetos grandes em movimento ficam translúcidos; reposicione com fade; não gire o mundo; ofereça referencial estacionário; evite oscilação sustentada perto de 0,2 Hz (`hig/02 motion`). Evite conteúdo preso à cabeça, prefira lazy follow; alinhe o horizonte; mantenha o ponto de expansão lento e dentro do campo de visão; transições de escuro para claro mais lentas (`vid/13 wwdc2023_10078`).
- Hover no visionOS: efeitos instantâneos, com atraso ou em rampa; atraso evita cintilação; efeitos que revelam conteúdo pedem atrasos maiores; mantenha elementos de ancoragem; comece de um elemento visível; evite movimento inesperado e não aplique em views de uso intenso como botões de toolbar (`vid/14 wwdc2024_10152`; `vid/16 wwdc2025_303`).
- Indicadores de progresso sempre em movimento e com ritmo uniforme; não alterne entre spinner e barra (`hig/11 progress-indicators`).
- Animação de símbolos com intenção: Bounce para confirmação, Scale para foco persistente, Pulse para atividade contínua, Replace para mudança de estado; em excesso, distraem (`hig/02 sf-symbols`; `vid/13 wwdc2023_10197`; `vid/14 wwdc2024_10188`).

### 3.7 Háptica e som

Háptica
- Use os padrões do sistema pelo significado documentado; mantenha relação causal consistente; complemente visual e som, casando intensidade e nitidez com a animação; não exagere; prefira hápticos curtos; torne-os opcionais; não atrapalhe câmera, giroscópio ou microfone (`hig/03 playing-haptics`).
- Padrões: no iOS, notification, impact e selection; no Magic Trackpad, alignment, level change e generic; no watchOS, Notification, Up, Down, Success, Failure, Retry, Start, Stop e Click (`hig/03 playing-haptics`).
- Blocos customizados: eventos transient e continuous, com intensity e sharpness de 0 a 1 (`hig/03 playing-haptics`; `vid/05 wwdc2019_520`, `wwdc2019_810`).
- Causalidade, harmonia e utilidade; muitas vezes a decisão certa é não adicionar (`vid/05 wwdc2019_810`; `vid/10 wwdc2021_10278`, "Don't add feedback just because you can"). A densidade da háptica deve casar com a densidade visual (`vid/10 wwdc2021_10278`).
- Sincronia é percebida: deslocar o som em 10 ms em relação à háptica muda a experiência; a mesma vibração parece mais precisa com um som nítido (`vid/03 wwdc2017_803`).
- Sem tato real (toque direto no visionOS, controles virtuais de jogo), compense com feedback visual e sonoro em cada contato; controles de toque têm estado de pressão, som e háptica (`hig/13 game-controls`; `vid/13 wwdc2023_10073`; `vid/14 wwdc2024_10085`, `wwdc2024_10094`).

Som
- O volume do sistema governa a saída; o app só ajusta níveis relativos; escolha a categoria de áudio pelo uso real; não repropósito controles de áudio (`hig/03 playing-audio`).
- Nunca comunique informação importante só por som (`hig/03 playing-audio`; `hig/12 notifications`).
- Som de notificação: reconhecível como daquele app, alinhado à estética, discreto e repetível (a equipe convive com o som por uma semana), limpo. Som de interface: raro, mais baixo que o de notificação, sempre desligável. Teste no dispositivo final e com fones (`vid/03 wwdc2017_803`).
- Blocos do som: timbre, frequência (agudo sugere objeto pequeno), duração (sons repetidos, curtos) e volume (sons de interface, sutis); cliques de botão soam melhor em dois tempos, ao pressionar e ao soltar; estados intermediários podem não precisar de som (`vid/04 wwdc2018_804`).
- visionOS: prefira ter som, porque um app sem som pode parecer quebrado; use áudio espacial, fixo ou rastreado; varie sons repetitivos (`hig/03 playing-audio`); randomize tom e amplitude; cure a melhor versão da realidade, não a mais literal (`vid/13 wwdc2023_10271`).
- Números: áudio no watchOS a 64 kbps HE-AAC (`hig/03 playing-audio`); tvOS não toca sons para acompanhar alertas e notificações (`hig/03 playing-audio`).

### 3.8 Escrita

Voz, tom e clareza
- Defina a voz pelo público e pelo vocabulário familiar; ajuste o tom ao contexto, sério numa queda detectada e celebratório numa conquista (`hig/02 writing`). A voz da Apple é guiada por clareza, simplicidade, amigabilidade e ajuda; qualidades sobem ou descem conforme a situação, nunca zeram (`vid/14 wwdc2024_10140`).
- Seja claro, use menos palavras, leia em voz alta, escreva para todos, sem jargão; considere o propósito de cada tela (`hig/02 writing`; `vid/11 wwdc2022_10037`, PACE).
- Remova preenchimentos ("simply", "quickly"), interjeições e desculpas que não acrescentam sentido; evite repetição; lidere com o porquê ("To get reservation updates, enter your phone number."); mantenha uma lista de palavras com termo escolhido, termos evitados e definição (`vid/15 wwdc2025_404`).
- Refira-se à pessoa como "você"; evite "o usuário"; reserve "nós" para a empresa ou evite-o, sobretudo em erros (`hig/01 inclusion`; `hig/02 writing`).
- Linguagem neutra em gênero, sem expressões coloquiais de origem excludente, humor com cautela (`hig/01 inclusion`; `vid/11 wwdc2022_10037`).
- Termos de implementação não vazam para a interface: "HealthKit", "NFC", "tag", "scene", "popover" e "panel" são trocados por linguagem de quem usa (`hig/15 healthkit`, `nfc`; `hig/09 windows`, `popovers`, `panels`).

Padrões de rótulos e mensagens
- Botões orientados à ação, quase sempre com verbo ("Send" funciona melhor que "Let's do it!"); evite "Click here"; use "tap" em dispositivos de toque; capitalização consistente por tipo de elemento; em fluxos, "Get Started", depois "Continue" ou "Next" de forma consistente, e "Done" no fim (`hig/02 writing`).
- Erros: perto do problema, sem culpar, dizendo como corrigir ("Choose a password with at least 8 characters" em vez de "That password is too short"); sem "oops" (`hig/02 writing`). Estados vazios com próximo passo (`hig/02 writing`).
- Alertas: o que aconteceu, por que a pessoa está vendo, como seguir (`vid/03 wwdc2017_813`). Título que descreve a situação, nunca só "Error", em até duas linhas; frase completa em sentence case com pontuação, fragmento em title case sem ponto; botões de uma ou duas palavras com verbo; "OK" só em alerta informativo; nunca "Yes" e "No"; sempre "Cancel" para cancelar (`hig/09 alerts`). Nomeie a ação específica: "Cancel Subscription" e "Keep Subscription" (`vid/11 wwdc2022_10037`).
- Menus: verbo para ações, title case, sem artigos, reticências quando a ação pede mais informação; rótulos alternáveis como "Show Map" e "Hide Map" (`hig/07 menus`). Toolbar: título útil com menos de 15 caracteres, nunca o nome do app (`hig/07 toolbars`).
- Tooltips: 60 a 75 caracteres, começando por verbo, sentence case, sem ponto final (`hig/03 offering-help`). Tips: uma ou duas frases; título com frase de ação direta; se o recurso exige mais de três ações, é complexo demais para um tip (`hig/03 offering-help`; `vid/13 wwdc2023_10229`).
- Purpose strings de permissão: frase breve, completa, específica, na voz ativa, em sentence case, terminando em ponto (`hig/02 privacy`).
- Notificações: título curto em title case sem ponto; corpo em frases completas; sem nome ou ícone do app; texto genérico ("New comment") para quando prévias estão ocultas (`hig/12 notifications`).
- Voz e Siri: diálogo curto, na língua falada; perguntas específicas ("Which soup?" em vez de "Which one?"); sem nome do app, sem nome da pessoa, sem primeira pessoa; ouça o diálogo várias vezes (`hig/16 siri`; `vid/06 wwdc2019_806`; `vid/07 wwdc2020_10071`). Prompts como pergunta, não como rótulo ("When is the deadline?") (`vid/09 wwdc2021_10283`).
- Rótulos de Action button com até três palavras, verbo no presente (`hig/13 action-button`); títulos de App Clip Card até 30 caracteres e subtítulos até 56 (`hig/14 app-clips`); erros do Apple Pay até 128 caracteres (`hig/14 apple-pay`).
- Machine learning: linguagem de consequência ("Suggest less pop music" em vez de "dislike"); atribuições factuais ("Because you've read nonfiction", não "love") (`hig/15 machine-learning`). IA generativa: feedback específico durante a geração, não "Processing" genérico (`hig/14 generative-ai`).
- Nomes de funcionalidades: pertencem ao conjunto, cumprem a expectativa, funcionam em qualquer idioma; teste dizendo o nome numa frase cotidiana (`vid/17 wwdc2026_290`).
- Localização muda comprimento, direção e abreviações do texto; prefira termos que se traduzem de forma parecida ("photo" em vez de "picture") (`vid/11 wwdc2022_10037`; `vid/03 wwdc2017_819`).

### 3.9 Acessibilidade

- Uma interface acessível é intuitiva, perceptível e adaptável (`hig/01 accessibility`).
- Visão: Dynamic Type em todos os tamanhos, inclusive os de acessibilidade; contraste mínimo; variantes de contraste aumentado; nunca só cor; VoiceOver descrevendo interface e conteúdo (`hig/01 accessibility`). Rótulos de VoiceOver descritivos ("Account settings, button" em vez do nome do glifo) (`vid/09 wwdc2021_10275`); descreva imagens com significado, exclua as decorativas, agrupe imagem e legenda, avise mudanças de layout, suporte o rotor (`hig/16 voiceover`). Bold Text engrossa também elementos não textuais com função de legibilidade (`vid/09 wwdc2021_10275`).
- Audição: legendas, subtítulos, audiodescrição e transcrições; háptica e sinais visuais para quem não percebe o áudio (`hig/01 accessibility`).
- Mobilidade: controles grandes e espaçados; gestos simples; alternativa a todo gesto, como um botão além do swipe; rótulos para Voice Control; suporte a Switch Control, AssistiveTouch e Full Keyboard Access (`hig/01 accessibility`). Tolerância a erro, sem timeouts quando Switch Control está ativo, e dados privados expostos pelo menor tempo possível (`vid/07 wwdc2020_10019`).
- Cognição: ações simples e familiares; evite elementos com temporizador que se autodispensam; no Assistive Access, divida fluxos em telas de uma interação e confirme duas vezes ações difíceis de reverter (`hig/01 accessibility`).
- Movimento e luz: Reduce Motion, controle de reprodução automática, Dim Flashing Lights (`hig/01 accessibility`); Auto-play Video Previews e Prefer Cross-fade Transitions (`vid/05 wwdc2019_244`).
- Respeite as preferências de exibição da pessoa mesmo quando o efeito afetado faz parte da identidade visual do app (`vid/08 wwdc2020_10020`).
- Gráficos: rótulos de acessibilidade com contexto, Audio Graphs, navegação por teclado e Switch Control, nunca exigir interação para informação crítica (`hig/05 charts`); rótulos por extenso, data antes do valor ("June 1, 36 pancakes") (`vid/11 wwdc2022_110340`).
- Formulários: sem limite de caracteres e sem proibir hífens ou acentos em nomes; campo único de nome completo; gênero com espectro amplo e opção de privacidade (`vid/09 wwdc2021_10275`).
- visionOS: sempre mais de uma forma de interagir; gestos customizados não recebem entrada de mão com VoiceOver ativo (`hig/13 eyes`; `hig/16 voiceover`); modo de uma mão e sistemas de interação alternativos (`vid/14 wwdc2024_10094`, `wwdc2024_10096`).
- Números falados nas sessões, como contexto e não como diretriz: 285 milhões de pessoas cegas ou com baixa visão (`vid/03 wwdc2017_811`); mais de 300 milhões com alguma forma de daltonismo (`vid/06 wwdc2019_802`); daltonismo em quase 5% da população (`vid/09 wwdc2021_10275`); um terço das pessoas com algum grau de sensibilidade a movimento (`vid/05 wwdc2019_244`); pessoas com deficiência são 15% da população mundial (`vid/10 wwdc2021_10304`); cerca de uma em sete pessoas tem alguma deficiência (`vid/16 wwdc2025_316`).
