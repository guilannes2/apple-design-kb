# Components / Navigation and search

## Path controls (slug: path-controls)

O que governa: um path control mostra o caminho no sistema de arquivos de um arquivo ou pasta selecionado, como o path bar do Finder.

Por que: o objetivo é dar contexto de localização hierárquica (disco raiz, pastas pai, item selecionado) de forma compacta, e permitir tanto visualizar quanto navegar ou selecionar um novo item por meio dessa hierarquia.

Faça e evite:
- Use o path control no corpo da janela, não no frame da janela.
- Path controls não são feitos para toolbars nem barras de status (o path bar do Finder fica no corpo da janela, na parte de baixo, não na barra de status).
- Na variante standard, se a lista for longa demais para caber, o controle esconde nomes entre o primeiro e o último item.
- Se tornar o controle editável na variante standard, a pessoa pode arrastar um item para o controle para selecioná-lo e exibir seu caminho.
- Na variante pop up, se tornar o controle editável, o menu ganha um comando Choose adicional para selecionar um item; também é possível arrastar um item para o controle.

Especificações exatas: o texto não traz números, medidas ou valores.

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS. É um componente exclusivo de macOS (AppKit, NSPathControl).

Ligações com outros artigos: File management.

<!-- visual:path-controls -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_path-controls, folha 0001), códigos conferidos; sem vídeo.
- A abertura mostra o path control como cadeia horizontal de segmentos, cada um com ícone e nome, unidos por setas, abaixo de um ícone de documento que dá o contexto do arquivo, separado por uma linha horizontal (img 0837).
- Rótulos de anotação ligados por linhas verticais finas nomeiam o papel de cada elo: disco raiz, pasta pai e item selecionado (img 0837).
- Cada segmento usa um ícone que indica o tipo de local: disco para a raiz, pasta para a pasta pai e arquivo para o item selecionado (img 0837).
- A variante padrão aparece como uma path bar do Finder em cinza claro, com quatro locais em sequência e rótulos placeholder, ícone de disco no primeiro e de pasta nos outros três, separados por setas para a direita (img 0838).
- A variante pop-up é um único segmento compacto em cinza claro, com ícone de pasta azul, título e um par de setas para cima e para baixo na borda final, em vez da cadeia linear (img 0839).
<!-- /visual:path-controls -->

## Search fields (slug: search-fields)

O que governa: o search field é um campo de texto editável que permite buscar um conjunto de conteúdo por termos específicos, combinando ícone de busca, botão Clear e texto de placeholder.

Por que: a Apple trata busca como algo que deve se sentir responsivo e contextual, cada plataforma tem um padrão de acesso à busca compatível com seus objetivos e layout, e o texto de placeholder e as sugestões existem para reduzir esforço cognitivo de quem busca, ajudando a pessoa a entender o escopo antes mesmo de digitar.

Faça e evite:
- Use texto de placeholder para indicar o que pode ser buscado, reforçando o escopo da busca ou educando sobre o tipo de conteúdo acessível.
- Se possível, comece a busca imediatamente quando a pessoa digita, para dar sensação de resposta contínua.
- Considere mostrar termos de busca sugeridos, como buscas recentes antes de começar a digitar ou sugestões preditivas enquanto a pessoa digita.
- Simplifique os resultados: mostre os mais relevantes primeiro para minimizar rolagem, e considere categorizá-los.
- Considere permitir filtrar resultados, por exemplo com uma scope bar na área de conteúdo dos resultados.
- Use uma scope bar para filtrar entre categorias de busca claramente definidas, ajudando a mover de um escopo mais amplo para um mais restrito.
- Parta de um escopo mais amplo por padrão e deixe a pessoa refiná-lo conforme necessário.
- Use tokens para filtrar por termos ou itens comuns de busca; um token ganha tratamento visual que indica que pode ser selecionado e editado como item único.
- Considere combinar tokens com sugestões de busca, já que as pessoas podem não saber quais tokens existem.

Especificações exatas: o texto não traz números de pt, px ou ms.

Diferenças por plataforma:
- Sem considerações adicionais para visionOS.
- iOS: há três posições principais para o ponto de entrada da busca: como aba em uma tab bar, em uma toolbar (no topo ou na base), ou inline com o conteúdo. Como aba, existem dois estilos: tab padrão (leva a uma página de destino de busca com o campo no topo, boa para explorar conteúdo rico, como no exemplo da Apple TV) e aparência de botão (foca o campo e mostra o teclado imediatamente, ideal para busca rápida e transitória). Em uma toolbar inferior, o campo pode aparecer expandido ou como botão que anima para um campo de busca acima do teclado; posicionar embaixo é preferível quando a busca é prioridade (exemplos: Settings, Mail, Notes). Em uma toolbar superior (navigation bar), a busca aparece como botão de toolbar; usar no topo quando é importante não cobrir conteúdo na base ou quando não há toolbar inferior (exemplo: Wallet). Como campo inline, colocar a busca junto do conteúdo que ela pesquisa reforça a relação entre os dois, útil quando o app tem mais de um campo de busca e a localização importa para o escopo (exemplo: Music, biblioteca); quando no topo, posicionar acima da lista que pesquisa e considerar fixá-lo à toolbar superior durante a rolagem.
- iPadOS e macOS: a colocação e o comportamento do campo de busca são semelhantes entre as duas plataformas, e se o app existir em ambas, manter a experiência consistente. Colocar o campo na borda final (trailing) da toolbar para muitos usos comuns, especialmente apps com split views que buscam em várias colunas de informação (Mail, Notes, Voice Memos); essa posição aproveita bem o espaço porque permite navegar resultados mantendo a seleção visível na detail view. Incluir busca no topo da sidebar quando filtrar conteúdo ou navegação ali (exemplo: Settings, que filtra a sidebar e expõe seções em múltiplos níveis). Incluir busca como item na sidebar ou tab bar quando se quer uma área dedicada à descoberta, útil quando a busca vem acompanhada de sugestões ricas, categorias ou conteúdo que precisa de mais espaço (exemplos: Music, TV). Em uma área dedicada de busca, considere focar o campo automaticamente ao navegar até a área, exceto no iPad quando só há teclado virtual disponível, caso em que é melhor deixar o campo sem foco para não cobrir a view inesperadamente com o teclado. Levar em conta o redimensionamento da janela: no iPad o campo redimensiona fluidamente como no Mac, mas em views compactas é importante manter a busca disponível onde for mais útil contextualmente (exemplo: Notes e Mail posicionam a busca acima da coluna de lista de conteúdo quando redimensionam para uma view compacta).
- tvOS: a tela de busca é uma tela de teclado especializada que ajuda a inserir texto de busca, exibindo resultados abaixo do teclado em uma view totalmente customizável. Fornecer sugestões é importante porque, em tvOS, as pessoas normalmente não querem digitar muito; sugestões populares e específicas de contexto, incluindo buscas recentes quando disponíveis, melhoram a experiência.
- watchOS: ao tocar o campo de busca, o sistema exibe um controle de entrada de texto que cobre a tela inteira; o app só volta ao campo de busca depois que a pessoa toca Cancel ou Search.

Ligações com outros artigos: Searching, Token fields (para o componente relacionado no macOS).

<!-- visual:search-fields -->
### O que as ilustrações mostram
Base: 3 folhas de ilustrações vistas (hig-img_search-fields, folhas 0001 a 0003), códigos conferidos; sem vídeo.
- A abertura diagrama o campo de busca com placeholder, cursor de texto na borda inicial e ícone de microfone na borda final, com setas de medida de largura e altura e linhas pontilhadas delimitando a área de texto; é a única anotação de dimensão da página (img 0983).
- No Mail do iPhone, a scope bar de dois segmentos fica acima do campo preenchido, e logo abaixo dele uma lista de sugestões em forma de token (ícone, rótulo em cinza e termo em preto), com o teclado aberto; callouts com linha e texto nomeiam a scope bar e os tokens (img 0984).
- Busca como aba da tab bar é mostrada em par: primeiro como quinto item dentro do mesmo agrupamento arredondado, sem distinção das outras abas; depois como botão circular separado, fora do grupo, na borda final da tela (img 0985, img 0986).
- Na toolbar inferior do iPhone, o campo de busca ocupa o centro de uma barra flutuante, entre um botão de filtro à esquerda e um botão de composição à direita (img 0987).
- Na toolbar superior do iPhone, a busca vira botão de lupa agrupado com o de mais opções à direita, com o botão de adicionar separado desse grupo e o voltar na borda inicial (img 0988).
- No iPad, o campo fica na borda final da toolbar superior, com um menu de sugestões logo abaixo e a primeira sugestão realçada em cinza (img 0989).
- No macOS, o campo preenchido ganha botão de limpar, e as sugestões abaixo levam ícone de lupa, com a primeira realçada em amarelo alaranjado (img 0990).
- Na sidebar do iPad, o campo de busca com microfone fica logo abaixo do cabeçalho e acima da lista de itens com miniatura (img 0991).
- Numa tab bar superior do iPad, a busca entra como item dedicado de lupa, realçado em azul, na borda direita da mesma barra das abas (img 0992).
- No tvOS, a tela de busca tem fundo escuro, campo no topo, teclado alfabético horizontal com a tecla focada em branco, uma fileira de cinco pílulas de sugestão logo abaixo e, embaixo, uma grade de resultados em cartões com imagem circular ou quadrada, primeira linha em negrito e segunda linha secundária (img 0993).
- A busca como aba é comparada num par quase idêntico que muda só a posição da aba de busca, e a busca na toolbar é comparada entre a barra inferior e a superior; a página não usa selos de certo ou errado (img 0985 e img 0986; img 0987 e img 0988).
Divergências registradas: na img 0993 não foi possível identificar uma scope bar como controle separado; a fileira de sugestões e o teclado ocupam o espaço em que o texto oficial descreve a scope bar.
<!-- /visual:search-fields -->

## Sidebars (slug: sidebars)

O que governa: a sidebar aparece na borda inicial (leading) de uma view e permite navegar entre áreas do app ou coleções de conteúdo de nível superior, como pastas e playlists.

Por que: sidebars exigem bastante espaço vertical e horizontal; quando o espaço é limitado ou se quer dedicar mais tela a outras informações ou funcionalidades, um controle mais compacto como a tab bar pode oferecer melhor navegação. Para muitos apps não é preciso escolher entre tab bar ou sidebar, pois existe um estilo de tab bar que oferece as duas coisas.

Faça e evite:
- Estenda conteúdo visualmente rico por baixo da sidebar. Em iOS, iPadOS e macOS, sidebars podem flutuar sobre o conteúdo na camada Liquid Glass; para reforçar a separação, pode-se estender o conteúdo sob a sidebar deixando-o rolar horizontalmente ou aplicando um background extension effect, que espelha o conteúdo adjacente para dar a impressão de esticá-lo por baixo da sidebar.
- Quando possível, permita que a pessoa personalize o conteúdo da sidebar, já que ela navega para as áreas mais importantes do app e a pessoa pode decidir quais são essas áreas e em que ordem aparecem.
- Agrupe a hierarquia com disclosure controls se o app tem muito conteúdo, para manter o espaço vertical da sidebar administrável.
- Considere usar símbolos familiares (SF Symbols) para representar itens na sidebar; se precisar de ícone customizado, prefira criar um custom symbol em vez de usar imagem bitmap.
- Considere permitir esconder a sidebar, usando as interações específicas de cada plataforma que as pessoas já conhecem (por exemplo, gesto de deslizar da borda no iPadOS, botão de mostrar/ocultar ou comandos de menu View no macOS); em visionOS, a janela geralmente se expande para acomodar a sidebar, então raramente é preciso escondê-la. Evite esconder a sidebar por padrão, para que continue descobrível.
- Em geral, mostre no máximo dois níveis de hierarquia na sidebar; quando a hierarquia de dados é mais profunda que dois níveis, considere uma interface de split view com uma lista de conteúdo entre os itens da sidebar e a detail view.
- Se precisar incluir dois níveis de hierarquia na sidebar, use rótulos sucintos e descritivos para titular cada grupo, omitindo palavras desnecessárias.
- Garanta que as cores dos ícones da sidebar sirvam a um propósito claro. Por padrão, os ícones usam a app accent color; no macOS, a pessoa pode mudar a cor de destaque do sistema, e espera que todos os ícones da sidebar reflitam essa escolha. Cores fixas, usadas com moderação, podem esclarecer o significado de um ícone ou chamar atenção para ele (exemplo: o ícone VIP no Mail usa amarelo para se destacar dos demais).

Especificações exatas: o texto não traz números de pt, px ou ms; a única quantificação é qualitativa ("no máximo dois níveis de hierarquia").

Diferenças por plataforma:
- Sem considerações adicionais para tvOS; não suportado em watchOS.
- iOS, iPadOS: ao usar o estilo sidebarAdaptable de tab view para apresentar uma sidebar, é possível escolher exibir sidebar ou tab bar quando o app abre; ambas as variações incluem um botão para alternar entre elas. Esse estilo também adapta sua aparência conforme a plataforma e responde automaticamente à rotação e ao redimensionamento da janela. Para exibir apenas sidebar, sem conversão, usar NavigationSplitView (para apresentar a sidebar no painel primário de um split view) ou UISplitViewController. Considere usar tab bar primeiro, pois oferece mais espaço para destacar conteúdo e flexibilidade para navegar entre as áreas principais; se precisar expor mais áreas do que cabem na tab bar, a aparência conversível em sidebar da tab bar pode dar acesso a conteúdo usado com menos frequência. Se não estiver usando SwiftUI para criar a sidebar, é possível usar a aparência UICollectionLayoutListConfiguration.Appearance.sidebar de um collection view list layout.
- macOS: a altura das linhas, o texto e o tamanho dos glifos da sidebar dependem do tamanho geral, que pode ser small, medium ou large; o tamanho pode ser definido programaticamente, mas a pessoa também pode mudá-lo selecionando um tamanho de ícone de sidebar diferente nas configurações gerais. Considere esconder e revelar a sidebar automaticamente quando a janela container é redimensionada (exemplo: reduzir a janela do visualizador do Mail pode colapsar a sidebar automaticamente para dar mais espaço ao conteúdo da mensagem). Evite colocar informações ou ações críticas na parte de baixo da sidebar, pois as pessoas costumam reposicionar a janela de forma que esconde a borda inferior.
- visionOS: se a hierarquia do app for profunda, considere usar uma sidebar dentro de uma aba de uma tab bar, onde a sidebar pode apoiar navegação secundária dentro da aba; nesse caso, é preciso impedir que seleções na sidebar mudem qual aba está aberta.

Ligações com outros artigos: Split views, Tab bars, Layout.

<!-- visual:sidebars -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações vistas, todos os códigos conferidos; a página não tem vídeo.
- A ilustração de construção desenha o topo de uma sidebar como componente: cabeçalho de seção com chevron de recolher, botão de alternar a sidebar no canto superior direito e três linhas de item com ícone de pasta à esquerda, rótulo no meio e estrela à direita (img 1047).
- Sobre essa ilustração, linhas guia tracejadas verticais alinham os ícones de pasta e os de estrela nas três linhas, e uma seta vertical de duas pontas à direita anota a altura ou o espaçamento de uma linha de item; as guias de alinhamento e a medida de espaçamento entre itens são o que a imagem acrescenta (img 1047).
- O primeiro item aparece destacado em vermelho sólido, indicando seleção, numa ilustração toda em tons de vermelho e rosa em degradê (img 1047).
- Uso incorreto, marcado com X cinza: num iPad, a imagem de flores no topo da área de conteúdo para exatamente na borda da sidebar, sem nenhuma transição (img 1048 com img 1049).
- Uso correto, marcado com check verde: a mesma tela, com os mesmos itens, título e texto, mas a imagem continua borrada e espelhada atrás dos itens da sidebar até a borda da janela; a única diferença entre o par está na área por trás da sidebar, o que mostra o efeito de extensão de fundo como continuidade borrada, e não recorte (img 1050 com img 1051).
- A sidebar de iPad desse par traz o ícone de colapsar a sidebar, a seta de voltar e três itens, cada um com ícone (img 1048, img 1050).
- No visionOS, o app Music usa um painel translúcido de vidro sobre o ambiente desfocado, com uma faixa estreita só de ícones à esquerda, depois a sidebar com cabeçalho "Library" e seus itens, e abaixo um grupo "Playlists" expansível com seta e subitens, dos quais o selecionado aparece destacado (img 1052).
- Ao lado dessa sidebar, um painel secundário traz cabeçalho de playlists, contagem de playlists, campo de busca próprio e grade de miniaturas de playlist (img 1052).
Divergências registradas: as notas registram que a img 1047 acrescenta guias de alinhamento e medida de espaçamento que a descrição oficial não detalha, e que a img 1052 mostra uma faixa estreita só de ícones à esquerda da sidebar que a descrição oficial não menciona.
<!-- /visual:sidebars -->

## Tab bars (slug: tab-bars)

O que governa: a tab bar permite navegar entre as seções de nível superior de um app, ajudando as pessoas a entender os diferentes tipos de informação ou funcionalidade que o app oferece e a alternar rapidamente entre seções preservando o estado de navegação de cada uma.

Por que: a tab bar existe para representar a hierarquia do app de forma estável e previsível; ela não deve ser confundida com um mecanismo de ações, e sua consistência visual (sempre visível, botões nunca desabilitados ou escondidos) é o que garante que a pessoa nunca perca a noção de onde está no app.

Faça e evite:
- Use tab bar para dar suporte à navegação, não para fornecer ações; se precisar de controles que atuam sobre elementos da view atual, use toolbars.
- Garanta que a tab bar fique visível quando a pessoa navega entre seções, pois escondê-la faz a pessoa esquecer em que área do app está; a exceção é quando uma view modal cobre a tab bar, já que um modal é temporário e autocontido.
- Use o número apropriado de abas necessário para ajudar na navegação; pese a complexidade de abas adicionais contra a necessidade de acesso frequente a cada seção, já que é geralmente mais fácil navegar entre menos abas. Quando disponível, considere uma sidebar ou uma tab bar que se adapta a sidebar como alternativa para apps com estrutura de informação complexa.
- Evite abas em overflow: dependendo do tamanho e orientação do dispositivo, o número de abas visíveis pode ser menor que o total; se o espaço horizontal limitar o número de abas visíveis, a aba final vira uma aba More em iOS e iPadOS, revelando os itens restantes em uma lista separada, o que dificulta o acesso e a percepção do conteúdo escondido, então limite os cenários em que isso ocorre.
- Não desabilite nem esconda botões da tab bar, mesmo quando o conteúdo está indisponível, pois isso torna a interface instável e imprevisível; se uma seção estiver vazia, explique por que o conteúdo está indisponível.
- Inclua rótulos de aba para ajudar na navegação, usando palavras únicas sempre que possível.
- Considere usar SF Symbols para ícones de tab bar familiares e escaláveis, que se adaptam automaticamente a diferentes contextos (a tab bar pode ser regular ou compact conforme dispositivo e orientação); em views compactas os ícones aparecem acima dos rótulos, em views regulares aparecem lado a lado; prefira símbolos ou ícones preenchidos (filled) para consistência com a plataforma.
- Use um badge (um oval vermelho com texto branco, número ou ponto de exclamação) para indicar informação crítica disponível em uma aba; reserve badges para informação crítica para não diluir seu impacto e significado.
- Evite aplicar uma cor similar entre os rótulos das abas e os fundos da camada de conteúdo; se o app já tem conteúdo colorido e vibrante na camada de conteúdo, prefira uma aparência monocromática para as tab bars, ou escolha uma cor de destaque com diferenciação visual suficiente.

Especificações exatas: em tvOS, a altura da tab bar é 68 pontos, e sua borda superior fica a 46 pontos do topo da tela; nenhum dos dois valores pode ser alterado. Para apps com tab bar customizável em iPadOS, se a pessoa puder selecionar suas próprias abas, mirar em uma lista padrão de cinco ou menos para preservar continuidade entre tamanhos de view compact e regular.

Diferenças por plataforma:
- Sem considerações adicionais para macOS; não suportado em watchOS.
- iOS: a tab bar flutua sobre o conteúdo na parte inferior da tela, com seus itens sobre um fundo Liquid Glass que permite ao conteúdo por baixo transparecer. Para tab bars com um acessório anexado, como o MiniPlayer no Music, é possível escolher minimizar a tab bar e mover o acessório para ficar inline com ela quando a pessoa rola para baixo; a pessoa sai do estado minimizado tocando uma aba ou rolando até o topo da view. A tab bar pode incluir uma aba de busca dedicada na extremidade final (trailing).
- iPadOS: o sistema exibe a tab bar perto do topo da tela. É possível escolher que a tab bar apareça como elemento fixo, ou com um botão que a converte em sidebar. Para apresentar uma sidebar sem a opção de conversão em tab bar, usar um navigation split view em vez de uma tab view. Prefira tab bar para navegação, pois dá acesso às seções mais usadas; se o app for mais complexo, é possível oferecer a opção de converter a tab bar em sidebar para acessar um conjunto mais amplo de opções de navegação. É possível deixar a pessoa customizar a tab bar, selecionando itens usados com frequência para adicioná-los, ou removendo os usados com menos frequência (exemplo: no Music, a pessoa pode escolher uma playlist favorita para exibir na tab bar).
- tvOS: a tab bar é altamente customizável (é possível especificar tint, cor ou imagem de fundo da tab bar; escolher fonte para os itens, incluindo fonte diferente para o item selecionado; especificar tints para itens selecionados e não selecionados; adicionar ícones de botão como configurações e busca). Por padrão a tab bar é translúcida, e só a aba selecionada é opaca; quando a pessoa usa o controle remoto para focar na tab bar, a aba selecionada ganha uma sombra projetada (drop shadow) que enfatiza seu estado selecionado. Se houver mais itens do que cabem na tab bar, o sistema trunca o item mais à direita aplicando um efeito de esmaecimento (fade) que começa do lado direito da tab bar; se houver itens suficientes para causar rolagem, o sistema também aplica um efeito de esmaecimento truncante a partir do lado esquerdo. Por padrão, a pessoa pode rolar a tab bar para fora da tela quando a aba atual contém uma única view principal (exemplos: abas Watch Now, Movies, TV Show, Sports e Kids do app TV); a exceção é quando a tela contém um split view, como a aba Library do app TV ou uma tela de Settings, caso em que a tab bar permanece fixa no topo da view enquanto a pessoa rola o conteúdo dos painéis primário e secundário do split view. Independentemente do conteúdo de uma aba, o foco sempre retorna à tab bar no topo da página quando a pessoa pressiona Menu no controle remoto. Em apps de transmissão ao vivo, organizar as abas de forma consistente na ordem: conteúdo ao vivo, Cloud DVR ou outro conteúdo gravado, outro conteúdo.
- visionOS: a tab bar é sempre vertical, flutuando em posição fixa em relação à borda inicial (leading) da janela. Quando a pessoa olha para a tab bar, ela se expande automaticamente; para abrir uma aba específica, a pessoa olha para a aba e toca. Enquanto expandida, a tab bar pode obscurecer temporariamente o conteúdo atrás dela. Forneça um símbolo e um rótulo de texto para cada aba; o símbolo da aba está sempre visível na tab bar, e quando a pessoa olha para a tab bar o sistema revela também os rótulos, que devem ser curtos para leitura rápida. Se fizer sentido no app, considere usar uma sidebar dentro de uma aba quando a hierarquia for profunda, apoiando navegação secundária dentro da aba; nesse caso é preciso impedir que seleções na sidebar mudem qual aba está aberta.

Ligações com outros artigos: Tab views, Toolbars, Sidebars, Materials, Search fields, Notifications, Live-viewing apps, Liquid Glass color.

<!-- visual:tab-bars -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações e 2 de 2 folhas de vídeo (hig-vid_tab-bars__059, quadros q001 a q011) vistas, todos os códigos conferidos.
- A anatomia de abertura agrupa quatro abas, cada uma com ícone sobre rótulo, dentro de um contêiner em pílula, e deixa a busca como botão circular separado, só com ícone; cotas horizontais marcam a distância na ponta esquerda e o intervalo entre a pílula e o botão de busca, e uma cota vertical fica acima da terceira e da quarta abas (img 1108).
- O estado selecionado nessa anatomia é um fundo branco com ícone preto, enquanto as abas não selecionadas têm ícone vermelho escuro sobre fundo transparente (img 1108).
- Em iPhone, a mesma barra de cinco abas muda só a relação entre ícone e rótulo: na paisagem o ícone fica à esquerda do texto na mesma linha, no retrato o ícone fica empilhado acima do rótulo (img 1109).
- O diagrama de anatomia nomeia as duas partes de uma aba com chamadas "Icon" e "Label"; a aba ativa leva o ícone em azul e as demais em preto, com a busca à parte (img 1110).
- O badge aparece como pequeno círculo vermelho preso ao canto superior direito do ícone, em duas das quatro abas, sem número visível nessa instância (img 1111).
- Em iOS com acessório, o estado expandido mostra o acessório "Not Playing" como retângulo arredondado acima da barra de quatro abas; no estado minimizado a barra se reduz a um botão circular só com a aba ativa à esquerda, o acessório vira pílula alongada no centro e a busca fica em botão circular isolado à direita, tudo numa só linha (img 1112, img 1113).
- Em iPadOS, a barra horizontal perto do topo traz botão de sidebar, itens com o ativo em vermelho e busca à direita; convertida, vira sidebar vertical com os mesmos destinos mais seções "Library" e "Playlists", enquanto a tela de conteúdo por trás permanece idêntica, ou seja, muda só o contêiner de navegação (img 1114, img 1115).
- Em visionOS, a barra recolhida é uma pílula vertical translúcida de vidro fosco só com ícones, com um círculo de fundo mais claro no ícone destacado; expandida, fica mais larga e cada linha ganha o rótulo ao lado do ícone dentro de uma pílula individual, com fundos levemente diferentes entre as linhas sugerindo estados distintos, como hover ou seleção (img 1116, img 1117).
- No vídeo, a barra do app de fotos começa recolhida com seis ícones sem texto (q001, q002), expande entre q002 e q003 (de 0,5 s para 1,0 s) mostrando os rótulos por extenso com a linha "Memories" em pílula destacada, e se mantém estável nesse estado até q009 (5,5 s) (folha 0001).
- A barra volta ao estado recolhido em q010 (6,0 s) e continua assim em q011; nos quadros amostrados não aparece nenhum estado intermediário entre recolhido e expandido, a mudança passa de um quadro fixo ao seguinte (folha 0002).
- O ícone que será destacado na expansão já mostra um leve círculo de fundo mais claro no estado recolhido, antes e depois da expansão (q001, q002, q010).
Divergências registradas: as notas registram que o vídeo mostra o leve destaque de fundo no ícone de "Memories" também no estado recolhido (q001, q002, q010), algo que a descrição oficial não menciona.
<!-- /visual:tab-bars -->

## Token fields (slug: token-fields)

O que governa: um token field é um tipo de campo de texto que converte texto em tokens fáceis de selecionar e manipular, como nos campos de endereço da janela de composição do Mail.

Por que: o token dá tratamento visual a um termo (como o nome de um destinatário), tornando-o um objeto manipulável (selecionável, arrastável, editável) em vez de apenas texto solto, e o menu contextual em um token existe para agregar informação ou opções de edição sem sair do fluxo de digitação.

Faça e evite:
- Agregue valor com um menu de contexto, já que as pessoas costumam se beneficiar de opções adicionais ou informações sobre um token (exemplo: no Mail, o menu contextual de um token de destinatário tem comandos para editar o nome, marcar como VIP e ver o cartão de contato).
- Considere fornecer formas adicionais de converter texto em tokens; por padrão, o texto vira token quando a pessoa digita vírgula, e é possível especificar atalhos adicionais, como pressionar Return.
- Considere customizar o atraso que o sistema usa antes de mostrar tokens sugeridos; por padrão as sugestões aparecem imediatamente, mas sugestões rápidas demais podem distrair quem está digitando, então considere ajustar o atraso para um nível confortável.

Especificações exatas: o texto não traz números, medidas ou valores de atraso; menciona apenas que por padrão as sugestões aparecem imediatamente e que a vírgula é o gatilho padrão de conversão.

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS, visionOS e watchOS. É um componente exclusivo de macOS (AppKit, NSTokenField).

Ligações com outros artigos: Text fields, Search fields, Context menus.

<!-- visual:token-fields -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido; a página não tem vídeo.
- A ilustração conceitual põe no mesmo campo, entre a lupa à esquerda e o botão circular de limpar à direita, um token em pílula rosa clara com ícone de pessoa e nome, seguido de texto solto ainda não convertido; o contraste entre objeto formatado e texto livre é o que a imagem ensina (img 1160).
- Na janela de composição do Mail no Mac, o campo "To:" mostra dois destinatários já convertidos em pílulas azul claro e um terceiro nome ainda sendo digitado como texto comum, com lista suspensa de sugestões logo abaixo, duas opções de endereço e a primeira destacada em azul (img 1161).
- No momento seguinte, o terceiro nome já virou pílula completa e aparece selecionado, abrindo um menu contextual próprio do token (img 1162).
- Esse menu organiza as opções em blocos separados por divisórias: o endereço atual com check e ações de editar, remover e copiar; depois adicionar aos VIPs e bloquear o remetente; depois remover da lista de destinatários anteriores e adicionar aos contatos; e por fim buscar pelo nome (img 1162).
- Nas capturas reais os tokens são pílulas retangulares de canto arredondado em azul claro, visualmente distintas do texto normal do campo, o mesmo formato de pílula da ilustração conceitual (img 1160, img 1161, img 1162).
<!-- /visual:token-fields -->

## O que este grupo revela sobre o jeito Apple

1. Componentes exclusivos de macOS (path-controls, token-fields) mostram que a Apple aceita fragmentar a paridade de plataforma quando o padrão de interação (arrastar itens, editar em linha, convenções de sistema de arquivos) só faz sentido no modelo de janelas e mouse do Mac; ambos são "Not supported" em todas as outras plataformas.
2. A Apple prefere adaptar um único componente a vários contextos em vez de multiplicar componentes: a tab bar que se converte em sidebar (sidebarAdaptable, tabBarOnly) aparece tanto em sidebars quanto em tab-bars como a solução recomendada para apps que precisam de navegação compacta e também de navegação rica, evitando forçar uma escolha binária.
3. Busca é tratada como um problema de posicionamento contextual, não de componente único: search-fields dedica a maior parte do artigo a onde colocar o campo (tab, toolbar, inline, sidebar) conforme o layout do app, em vez de prescrever um único lugar correto.
4. Liquid Glass é citado como camada visual compartilhada entre sidebars e tab-bars (ambos "flutuam" sobre o conteúdo com fundo translúcido), revelando uma linguagem de material unificada entre componentes de navegação distintos.
5. A Apple é consistente em nunca esconder ou desabilitar controles de navegação primária: tab-bars proíbe esconder ou desabilitar botões de aba mesmo com conteúdo indisponível, e sidebars recomenda não esconder a sidebar por padrão, refletindo um princípio maior de previsibilidade espacial da navegação.
6. Personalização pelo usuário é valorizada, mas com limites de continuidade: sidebars sugere permitir customizar o conteúdo da sidebar, e tab-bars permite customizar as abas mas recomenda um padrão de cinco ou menos abas para manter continuidade visual entre tamanhos de tela.
7. Cor como sinal funcional, não decorativo: sidebars adverte para os ícones respeitarem a app accent color (ou a cor de sistema escolhida no macOS) e reservar cor fixa só para destacar itens específicos (exemplo do VIP amarelo no Mail); tab-bars pede evitar cor de rótulo parecida com o fundo de conteúdo. Ambos tratam cor como veículo de significado que a pessoa controla, não como escolha estética isolada do app.
8. Hierarquia rasa é o padrão preferido: sidebars recomenda no máximo dois níveis visíveis antes de introduzir um split view adicional, reforçando a preferência da Apple por navegação achatada em vez de árvores profundas.
9. tvOS recebe tratamento à parte em quase todo o grupo (search-fields, tab-bars), com mecânicas próprias de foco por controle remoto, truncamento por fade e pinagem de tab bar em split views, mostrando que a interação "apontar e focar" da Apple TV exige regras de navegação estruturalmente diferentes das de toque ou clique.
10. visionOS trata a sidebar e a tab bar como elementos que respondem ao olhar (expansão ao olhar, toque para confirmar) e evita esconder a sidebar por padrão porque a janela se adapta ao espaço, um padrão de interação que não tem equivalente direto nas demais plataformas citadas no grupo.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/path-controls.md: 26 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/search-fields.md: 101 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sidebars.md: 64 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/tab-bars.md: 89 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/token-fields.md: 30 linhas lidas, até o fim: sim.
