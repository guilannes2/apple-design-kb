# Diferenças entre plataformas

Cópia literal da seção 4 da essência (`kb/00_ESSENCIA_APPLE.md`). Uma interface é desenhada para a plataforma em que vai rodar, nunca portada de outra.

## Diferenças entre plataformas que mudam decisões de design

A regra de fundo é tratar cada plataforma com a mesma intenção e o mesmo cuidado, derivando as decisões de como o dispositivo é usado (`hig/00 design-principles`, Flexibility; `hig/00`, insight 1). Abaixo, só o que efetivamente muda uma decisão.

### iPhone (iOS)
- Uso na mão, em movimento, de minutos a mais de uma hora; controles mais fáceis de alcançar no meio e embaixo da tela; limitar controles visíveis; permitir swipe para voltar e para ações em linhas de lista (`hig/00 designing-for-ios`).
- Tab bar flutua sobre o conteúdo na base, em Liquid Glass, e pode minimizar ao rolar; busca pode ser aba dedicada na borda trailing ou campo na toolbar inferior, que sobe acima do teclado (`hig/08 tab-bars`, `search-fields`; `vid/15 wwdc2025_323`; `vid/17 wwdc2026_292`). A busca foi para a base por alcance do polegar (`vid/00 meet-with-apple_208`).
- Modal se dispensa por botão na toolbar superior ou swipe para baixo; sheets com detents e grabber; em compact, popovers dão lugar a sheets (`hig/03 modality`; `hig/09 sheets`, `popovers`).
- Switch só dentro de linha de lista; fora dela, botão que se comporta como toggle; não use slider para volume (`hig/10 toggles`, `sliders`).
- Ofereça context menu ou edit menu para um item, nunca os dois (`hig/07 context-menus`).
- Launch screen obrigatório e quase idêntico à primeira tela (`hig/03 launching`).
- Na geometria do iPhone X: preencher a tela inteira, respeitar safe areas, manter controles centralizados em paisagem, não enfeitar o Home indicator (`vid/01 tech-talks_801`).

### iPad (iPadOS)
- Tela grande e múltiplas entradas combinadas: minimize modais e transições de tela cheia, mostre mais conteúdo, mantenha contexto (renomear inline em vez de modal) (`hig/00 designing-for-ipados`; `vid/07 wwdc2020_10206`).
- Um bom app de iPad não é meio-termo entre iPhone e Mac (`vid/07 wwdc2020_10206`).
- Tab bar no topo, conversível em sidebar; na dúvida, comece pela tab bar; sidebar quando há conteúdo muito aninhado (`hig/08 tab-bars`; `vid/14 wwdc2024_10147`; `vid/15 wwdc2025_208`).
- Janelas redimensionáveis livremente; cada documento em sua janela, com nome descritivo; controles de janela na borda leading da toolbar (`hig/09 windows`; `vid/15 wwdc2025_208`).
- Menu bar escondida até ser revelada, centralizada; nunca esconder itens de menu, esmaecer (`hig/07 the-menu-bar`; `vid/15 wwdc2025_208`).
- Ponteiro: em 2020, precisão adaptativa, círculo de 19 pt e magnetismo (`vid/07 wwdc2020_10640`); no iPadOS 26, rastreamento um para um, sem magnetismo, com realce em vidro (`vid/15 wwdc2025_208`).
- Atalhos de teclado para todas as ações comuns; Full Keyboard Access cuida da navegação de controles (`vid/07 wwdc2020_10206`; `hig/13 keyboards`, `focus-and-selection`).
- Apple Pencil marca no instante do toque, sem modo; hover mostra prévia, nunca dispara ação (`hig/13 apple-pencil-and-scribble`).
- Navegação estilo navegador só para hierarquias complexas; tabelas voltam a ser listas em compact (`vid/11 wwdc2022_10009`).

### Mac (macOS)
- Uso estacionário, várias janelas e apps, entradas de alta precisão: mais densidade, menos níveis aninhados, janelas redimensionáveis, atalhos de teclado, personalização (`hig/00 designing-for-macos`).
- A menu bar é o inventário completo de comandos, em ordem fixa (App, File, Edit, Format, View, menus do app, Window, Help); todo item de toolbar também existe como comando de menu; itens indisponíveis são desabilitados, não escondidos (`hig/07 the-menu-bar`, `toolbars`).
- Controles nas bordas não trazem benefício ergonômico; fluxo de cima para baixo; nada crítico embaixo da janela (`vid/05 wwdc2019_809`; `hig/15 mac-catalyst`).
- Cor mais neutra; a cor de destaque escolhida pela pessoa prevalece; sidebar translúcida (`hig/01 color`; `vid/05 wwdc2019_809`; `vid/08 wwdc2020_10104`).
- Sem Dynamic Type; corpo de 13 pt (`hig/02 typography`).
- Controles Mini, Small e Medium seguem retângulo arredondado para alta densidade; Large e X-Large usam capsule (`vid/16 wwdc2025_356`).
- Usuários esperam context menu em todo objeto (`hig/15 mac-catalyst`); estados de janela Main, Key e Inactive com aparências distintas (`hig/09 windows`); settings em janela própria com Command-vírgula (`hig/04 settings`).

### Apple TV (tvOS)
- Visto a oito pés ou mais, com controle remoto: sistema de foco, arte de borda a borda, animações sutis, legível à distância (`hig/00 designing-for-tvos`).
- Foco não se indica só por cor; itens crescem ao ganhar foco, então o espaçamento precisa prever isso; até cinco estados visuais por item focável; evite ponteiro (`hig/01 color`, `layout`; `hig/06 lockups`; `hig/13 focus-and-selection`).
- Content first: algo já tocando ao abrir, menos passos, metadados só quando há interesse (`vid/05 wwdc2019_211`).
- Minimize entrada de texto; peça login e cadastro em outro dispositivo (`hig/03 managing-accounts`; `hig/10 text-fields`).
- Back abre a tela pai; em jogo ativo, abre menu de pausa; diferencie press de tap e ignore taps acidentais durante vídeo ao vivo (`hig/13 remotes`).
- Sem sons para alertas e notificações (`hig/03 playing-audio`).

### Apple Vision Pro (visionOS)
- O dispositivo leva o conteúdo até a pessoa; conforto visual e físico é prioridade; escolha o nível mínimo de imersão para cada momento e comece no Shared Space (`hig/00 designing-for-visionos`; `hig/01 immersive-experiences`; `vid/13 wwdc2023_10072`).
- Olhos miram, mãos selecionam; alvos de 60 pt; formas arredondadas; hover do sistema aplicado fora do processo do app, por privacidade (`hig/13 eyes`; `vid/13 wwdc2023_10073`; `vid/16 wwdc2025_303`).
- Conteúdo no campo de visão, em paisagem, ancorado no espaço e não na cabeça, além do alcance do braço; texto plano; profundidade sutil e com propósito; escala dinâmica (`hig/02 spatial-layout`; `vid/13 wwdc2023_10072`, `wwdc2023_10078`).
- Não há modo escuro; o glass se adapta à luz; tipografia mais pesada (`hig/02 materials`; `vid/13 wwdc2023_10076`).
- Tab bar vertical à esquerda da janela; toolbar na borda inferior como ornamento; não crie toolbar vertical; sheets centralizadas; botão de fechar no canto superior esquerdo (`hig/08 tab-bars`; `hig/07 toolbars`, `ornaments`; `vid/13 wwdc2023_10076`).
- Não existe modo de tela cheia; a expansão vem da janela ou da Digital Crown (`hig/03 going-full-screen`).
- Encontrar o "key moment" que só existe espacialmente, em vez de portar o app iOS numa janela (`vid/13 wwdc2023_10072`; `vid/14 wwdc2024_10086`).
- Som é esperado; um app sem som pode parecer quebrado (`hig/03 playing-audio`).

### Apple Watch (watchOS)
- Interações de relance, de menos de um minuto (`hig/00 designing-for-watchos`); em 2015 a meta falada era cerca de cinco segundos (`vid/02 wwdc2015_802`); em 2023, cerca de dez segundos no máximo com informação de relance (`vid/13 wwdc2023_10309`).
- "Apple Watch is not a miniature iPhone": subconjunto essencial, hierarquia rasa (`vid/02 wwdc2015_802`, `wwdc2015_805`); apps focados e altamente especializados (`vid/13 wwdc2023_10026`).
- Desde o watchOS 10, a Digital Crown é a navegação primária, sempre com equivalente por toque; paginação vertical preferida à horizontal; cada página com a altura de uma tela; layouts Dial, Infographic e List (`hig/13 digital-crown`; `vid/13 wwdc2023_10026`, `wwdc2023_10138`).
- No watchOS 7, menus por toque longo foram eliminados em favor de botões visíveis; ação primária nunca num menu More (`vid/07 wwdc2020_10171`).
- Evite indicadores de carregamento e de progresso indeterminado; prefira avisar por notificação ao terminar (`hig/03 feedback`, `loading`).
- Complicações, Smart Stack e notificações muitas vezes importam mais que o app; notificações foram descritas como a interação primária no relógio (`hig/00 designing-for-watchos`; `vid/04 wwdc2018_806`).
- O bezel preto funciona como padding; "bigger is better" (`vid/02 wwdc2015_805`); cor de fundo com função (`vid/13 wwdc2023_10026`).
- Apps não adicionam opções ao app Settings do sistema (`hig/04 settings`); vídeos de até 30 segundos (`hig/03 playing-video`).

### iPhone Duo
- Duas telas, várias poses e dobradiça: construa para redimensionar com size classes, margens e safe areas, sem larguras fixas; mantenha funcionalidade e posição relativa dos controles entre poses (`hig/00 designing-for-iphone-duo`).
- Toolbars, tab bars e controles de navegação vão para a lateral, no eixo vertical, exceto na tela interna em retrato; não sobrescreva esse posicionamento (`hig/00 designing-for-iphone-duo`).
- Regiões reservadas (câmeras e dobra); grades com número par de colunas; evite mudanças extremas de layout ao dobrar (`hig/00 designing-for-iphone-duo`).
- As quatro sessões técnicas sobre o iPhone Duo não têm transcrição nesta base (Seção 8).

### CarPlay
- Feito para quem dirige: nada deve exigir o iPhone, que pode estar no porta-malas; erros aparecem no CarPlay; sem reprodução automática e sem mudar o volume geral; conteúdo importante na metade superior (`hig/14 carplay`).
- A próxima geração do sistema de design do CarPlay é co-marcada com a montadora: não deve parecer só Apple nem cópia do sistema nativo (`vid/14 wwdc2024_10112`).
