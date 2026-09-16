# Components / Menus and actions

Grupo de índice 7 da lista hig em groups.json. Cobre os componentes que a Apple usa para expor comandos e ações: activity views, buttons, context menus, dock menus, edit menus, home screen quick actions, menus (o artigo geral), ornaments, pop up buttons, pull down buttons, the menu bar e toolbars.

## Activity views (slug: activity-views)

Uma activity view, também chamada de share sheet, apresenta um leque de tarefas que a pessoa pode executar no contexto atual: compartilhar (mensagens, redes) e ações como Copy e Print, além de acesso rápido a apps usados com frequência.

Por que: o compartilhamento e as ações relacionadas a um conteúdo são tarefas frequentes mas heterogêneas (podem envolver apps de terceiros, extensões, serviços do sistema). Centralizar tudo num único ponto de entrada familiar (o botão Share) evita que cada app reinvente sua própria versão de "compartilhar" e permite que o sistema liste, ao lado das ações do app, as ações de outros apps e do sistema, mantendo previsibilidade para quem usa.

Faça e evite:
- Evite duplicar ações que já existem na activity view, como um Print próprio; se precisar de algo parecido mas com comportamento diferente, dê um título específico (ex. "Print Transaction") em vez de reusar o nome genérico.
- Considere usar um símbolo do SF Symbols para representar a atividade personalizada; se precisar de um ícone de interface próprio, centralize-o numa área de aproximadamente 70x70 pixels.
- Escreva um título curto e descritivo para cada ação personalizada, de preferência um verbo ou uma frase verbal breve; evite incluir o nome da empresa ou do produto no título da ação (diferente da atividade de compartilhamento, que exibe o nome da empresa abaixo do ícone).
- Garanta que as atividades exibidas façam sentido no contexto atual; embora não seja possível reordenar as tarefas fornecidas pelo sistema, é possível excluir as que não se aplicam ao app (por exemplo, excluir Print se imprimir não fizer sentido).
- Use o botão Share para abrir a activity view; não crie um caminho alternativo para a mesma função, pois as pessoas já esperam encontrá-la ali.
- Para share extensions, prefira a composition view fornecida pelo sistema, que garante uma experiência de compartilhamento consistente; para action extensions, inclua o nome do app e, se precisar apresentar uma interface própria, use elementos que lembrem a interface do app.
- Simplifique e limite a interação: uma extensão de compartilhamento pode, por exemplo, postar uma imagem numa rede social com um único toque ou clique.
- Evite colocar uma modal view acima da extensão; o sistema já exibe a extensão dentro de uma modal view por padrão, e alertas acima dela devem ser exceção, não regra.
- Se necessário, forneça uma imagem que comunique o propósito da extensão: a share extension usa automaticamente o ícone do app, e a action extension deve preferir um símbolo ou ícone de interface que identifique claramente a tarefa.
- Use o app principal para indicar o progresso de uma operação longa, já que a activity view se fecha assim que a pessoa conclui a tarefa na extensão; se a tarefa demorar, continue em segundo plano e dê um jeito de checar o status no app principal. Uma notificação pode avisar sobre um problema, mas não deve ser usada só para avisar que a tarefa terminou.

Especificações exatas: ícone de interface personalizado centralizado numa área de aproximadamente 70x70 pixels. Nenhuma outra medida numérica aparece no texto.

Diferenças por plataforma: suportado, sem observações adicionais, em iOS, iPadOS e visionOS. Não suportado em macOS, tvOS ou watchOS, mas no macOS é possível criar extensões de share e action mesmo sem a activity view do sistema (acessadas por um botão Share na toolbar ou por Share num context menu, ou por um quick action num Finder window).

Ligações com outros artigos: Sheets, Popovers.

<!-- visual:activity-views -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_activity-views, folha 0001), códigos conferidos; sem vídeo.
- A abertura estiliza o share sheet dentro do contorno de um iPhone: cabeçalho com um quadrado à esquerda representando o item compartilhado e título com subtítulo, seguido de duas fileiras de ícones circulares (img 0036).
- Na versão estilizada os ícones reais de apps e contatos viram círculos genéricos monocromáticos em vermelho, e só os rótulos de texto conservam os nomes reais de apps e ações do sistema (img 0036).
- Na tela real do Notes, antes de qualquer toque, o botão Share fica no canto superior direito agrupado com o botão de mais opções (img 0037).
- O par img 0037 e img 0038 mantém a mesma nota ao fundo e muda só a presença do activity view, isolando a transição de antes e depois de tocar em Share.
- O activity view real é um cartão branco sobreposto que cobre a parte inferior do conteúdo, com cabeçalho mostrando o ícone e o título do documento compartilhado (img 0038).
- O conteúdo do cartão real se organiza em três fileiras distintas: contatos frequentes como avatares coloridos com iniciais, apps de compartilhamento com seus ícones coloridos, e ações locais sobre o documento terminando em "More" (img 0038).
- A estilização tem só duas fileiras, com apps na primeira e ações do sistema na segunda, enquanto a captura real acrescenta uma fileira própria de contatos e separa contatos, apps e ações em três faixas (img 0036 comparada a img 0038).
<!-- /visual:activity-views -->

## Buttons (slug: buttons)

Um button inicia uma ação instantânea; combina três atributos (style, content e role) para comunicar sua função com clareza.

Por que: um botão só funciona se for reconhecível e fácil de entender à primeira vista. Separar style (aparência visual), content (símbolo, texto ou ambos) e role (o significado semântico, que pode afetar a aparência) dá à Apple um vocabulário consistente para hierarquizar ações em qualquer tela, e permite que estilos do sistema já tragam estados de interação, suporte a acessibilidade e adaptação de aparência prontos, sem que cada app precise reconstruir isso.

Faça e evite:
- Dê espaço suficiente ao redor do botão para que seja possível distingui-lo visualmente do conteúdo ao redor e selecioná-lo com facilidade, qualquer que seja o método de entrada.
- Sempre inclua um press state num botão customizado; sem ele o botão parece não responder, e a pessoa fica em dúvida se o toque foi registrado.
- Use um estilo visual proeminente para a ação mais provável de uma view, aplicando a cor de destaque do app; mantenha no máximo um ou dois botões proeminentes por view, porque proeminência demais aumenta a carga cognitiva.
- Use estilo, não tamanho, para distinguir a opção preferida entre várias opções; botões do mesmo tamanho sinalizam que formam um conjunto coerente de escolhas, enquanto tamanhos diferentes deixam a interface confusa.
- Evite aplicar cor parecida entre o label do botão e o fundo da content layer; se o conteúdo já for colorido, prefira a aparência monocromática padrão dos labels de botão.
- Prefira associar ações familiares a ícones familiares (ex. o símbolo square.and.arrow.up para compartilhar); use texto quando um label curto comunica melhor que um ícone, com capitalização title-style e, de preferência, começando com um verbo.
- Role de um botão pode ser Normal (sem significado específico), Primary (o botão que a pessoa mais provavelmente escolherá, usa a cor de destaque do app e responde à tecla Return em views temporárias), Cancel (cancela a ação atual) ou Destructive (pode destruir dados, usa a cor vermelha do sistema).
- Nunca atribua o role primary a um botão que executa uma ação destrutiva, mesmo que seja a escolha mais provável, porque a proeminência visual do primary faz as pessoas escolherem sem ler.

Especificações exatas:
- Hit region mínima de 44x44 pt para qualquer botão; em visionOS, 60x60 pt.
- Padding de aproximadamente 10 pixels entre as bordas da imagem e as bordas do botão, em image buttons no macOS.
- Em visionOS, tamanhos padrão de botão: Mini 28 pt, Small 32 pt, Regular 44 pt, Large 52 pt, Extra large 64 pt (aplicáveis a formatos circular, capsule com texto, capsule com texto e ícone, e rounded rectangle, cada um com disponibilidade própria por tamanho).
- Em visionOS, centros de botões devem ficar a pelo menos 60 pts de distância entre si; se os botões tiverem 60 pts ou mais, adicionar 4 pts de padding ao redor para o hover effect não se sobrepor.

Diferenças por plataforma:
- iOS, iPadOS: um botão pode exibir um activity indicator ao lado do label original ou de um label alternativo (ex. "Checkout" vira "Checking out…") quando a ação não completa instantaneamente, escondendo a imagem do botão se houver.
- macOS: push buttons são o tipo padrão (podem ser default button e receber tint); flexible-height push buttons servem para conteúdo alto ou de altura variável, mantendo o mesmo corner radius e padding dos botões padrão; um push button que abre outra janela, view ou app recebe reticências no título; sistemas com Magic Trackpad podem suportar spring loading (force click para ativar arrastando itens selecionados sobre o botão). Square buttons (também chamados gradient buttons) contêm símbolos ou ícones, não texto, ficam próximos à view associada e não devem ser usados em toolbars nem status bars. Help buttons são circulares, contêm um ponto de interrogação, e devem se limitar a um por janela; posições recomendadas: em diálogo com botões de dispensa, no canto inferior oposto e alinhado verticalmente a eles; em diálogo sem botões de dispensa ou em janela/painel de settings, no canto inferior esquerdo ou direito. Image buttons devem ficar numa view, não na moldura da janela, e o label, se houver, fica abaixo da imagem.
- visionOS: botões têm fundo visível e som de feedback ao interagir; três formatos padrão (circle para ícone só, roundedRectangle ou capsule para texto só, capsule para ícone e texto); quatro estados visuais de interação; não suportam hover effect customizado; podem exibir tooltip ao serem olhados por um instante (menos necessário quando já têm texto); a Apple recomenda fundo com thin material quando o botão aparece sobre glass e usar o material do visionOS quando o botão flutua no espaço; evitar fundo branco com texto ou ícone preto, reservado ao estado de toggled; preferir capsule em fileira horizontal e rounded-rectangle em pilha vertical.
- watchOS: todos os botões inline usam o formato capsule e ganham um efeito de material quando colocados junto ao conteúdo; a toolbar posiciona botões nos cantos, com o sistema movendo automaticamente hora e título para acomodá-los e aplicando aparência Liquid Glass aos botões da toolbar; botões de largura total são preferidos para ações primárias; se dois botões dividirem o mesmo espaço horizontal, usar a mesma altura para ambos.
- tvOS: sem considerações adicionais além do texto geral.

Ligações com outros artigos: Pop-up buttons, Pull-down buttons, Toggles, Segmented controls, Location button, Liquid Glass color.

<!-- visual:buttons -->
### O que as ilustrações mostram
Base: 3 folhas de ilustrações (hig-img_buttons) e 2 vídeos de uma folha cada (hig-vid_buttons__006 e hig-vid_buttons__007) vistos, códigos conferidos.
- A abertura anota com setas vermelhas bidirecionais, sem números, a largura de um botão cápsula e o espaçamento horizontal entre dois botões iguais lado a lado (img 0189).
- No mesmo alerta de iOS, três botões empilhados mostram a hierarquia por papel: primário com fundo azul sólido e texto branco, destrutivo com fundo cinza claro e texto vermelho, secundário com fundo cinza claro e texto preto; o vermelho do destrutivo fica só no texto, não no fundo (img 0190).
- O estado de carregamento é um par antes e depois no mesmo componente: a cápsula cinza com "Checkout" em azul passa a "Checking out" com um spinner azul na borda inicial, mantendo forma e cor de fundo, sem mudança perceptível de tamanho (img 0191, img 0192).
- Os quatro estados de botão do visionOS usam o mesmo botão circular bege acinzentado com ícone central: em repouso e em hover o círculo interno é translúcido claro com ícone branco; selecionado inverte o contraste, com círculo interno branco sólido e ícone em contorno preto; indisponível aparece esmaecido (img 0193, img 0194, img 0195, img 0196).
- A seção de visionOS traz um check isolado em cinza neutro sobre fundo branco, em vez do selo verde de acerto usado em outras páginas (img 0197).
- No watchOS, os botões inline são cápsulas empilhadas na base da tela, com cor sólida ou gradiente que contrasta com o fundo colorido da tela para manter a leitura (img 0198).
- A toolbar do watchOS põe botões circulares nos cantos superiores (fechar e mais opções) e três controles na base, com o play central maior e mais claro que os laterais (img 0199).
- No vídeo 006, quatro botões circulares numa barra superior translúcida seguem idênticos de q001 a q005; em q006 o botão de mais opções clareia o fundo, e em q007 e q008 fica branco sólido enquanto os vizinhos permanecem cinza (hig-vid_buttons__006, folha 0001).
- O menu acionado por esse botão nasce ancorado logo abaixo dele, parcialmente cortado em q007 e inteiro em q008, com fundo translúcido azulado que aparenta vir do conteúdo por trás (hig-vid_buttons__006, folha 0001, q007 e q008).
- No vídeo 007, o botão de ícone de compartilhar aparece sozinho em q001 e q002; a tooltip "Share" surge com atraso abaixo dele em q003, ainda menor, e só em q004 atinge tamanho e opacidade finais (hig-vid_buttons__007, folha 0001).
Divergências registradas: a diferença de tom entre repouso e hover no visionOS não é clara nas capturas; a legenda oficial fala em fundo médio escuro no hover (img 0193, img 0194). Os vídeos acrescentam à descrição oficial o contraste progressivo do botão selecionado e o crescimento gradual do menu e da tooltip.
<!-- /visual:buttons -->

## Context menus (slug: context-menus)

Um context menu dá acesso a funcionalidades diretamente relacionadas a um item, sem sobrecarregar a interface principal; fica escondido até ser revelado por uma ação específica sobre um item selecionado.

Por que: um context menu não existe para funções avançadas ou raras, mas para deixar imediatamente acessíveis os comandos mais prováveis no contexto atual, sem ocupar espaço permanente na tela. Como fica oculto por padrão, a Apple exige que tudo que aparece nele também esteja acessível pela interface principal, evitando que vire o único caminho para uma funcionalidade que a pessoa talvez nunca descubra.

Faça e evite:
- Priorize relevância na escolha dos itens; não é lugar para comandos avançados ou raramente usados.
- Mantenha o menu curto; um context menu longo é difícil de escanear e rolar.
- Suporte context menus de forma consistente em todo o app; oferecê-los só em alguns lugares confunde sobre onde a função existe.
- Sempre disponibilize os mesmos itens do context menu também na interface principal (ex. na toolbar).
- Se precisar de submenus para gerenciar a complexidade, limite a um único nível, e dê um título intuitivo que ajude a prever o conteúdo sem abrir.
- Esconda itens indisponíveis em vez de esmaecê-los (dimmed); a exceção no macOS são Cut, Copy e Paste, que podem aparecer indisponíveis mesmo se não se aplicarem ao contexto.
- Posicione os itens mais usados onde a pessoa provavelmente olhará primeiro, considerando que o menu pode abrir acima ou abaixo do conteúdo selecionado.
- Mostre atalhos de teclado nos menus principais do app, não em context menus, porque eles já são um atalho para comandos específicos de tarefa.
- Siga as boas práticas de separadores para agrupar itens, evitando mais de aproximadamente três grupos num context menu.
- Em iOS, iPadOS e visionOS, avise sobre itens que podem destruir dados: liste-os no final do menu e identifique-os como destructive (o sistema pode exibi-los em vermelho).
- Um context menu raramente exibe título; inclua um título só se ele esclarecer o efeito do menu (ex. mostrar quantas mensagens foram selecionadas).
- Represente ações com ícones familiares, os mesmos usados em outros pontos do sistema para Copy, Share, Delete etc.

Especificações exatas: nenhum número explícito é dado no texto (a orientação de "cerca de três grupos" e "um nível de submenu" é qualitativa).

Diferenças por plataforma:
- iOS, iPadOS: ofereça context menu ou edit menu para um item, nunca os dois ao mesmo tempo, porque confundiria a pessoa e dificultaria para o sistema detectar a intenção. Em iPadOS, considere um context menu para criar um novo objeto (ex. Files cria uma nova pasta numa área entre arquivos e pastas existentes). Em iOS e iPadOS, o context menu pode exibir uma preview do conteúdo perto da lista de comandos, e a pessoa pode tocar na preview para abri-la ou arrastá-la; a preview deve ter o clipping path ajustado ao formato da imagem para que os contornos não pareçam mudar durante a animação.
- macOS: o context menu às vezes é chamado de "contextual menu".
- visionOS: considere um context menu em vez de um panel ou inspector window para reduzir a quantidade de janelas abertas; evite que a altura do menu exceda a altura da janela, pois um menu alto demais pode obscurecer componentes do sistema acima e abaixo da janela (controles de gerenciamento de janela e o menu Share).
- Sem considerações adicionais em tvOS; não suportado em watchOS.

Ligações com outros artigos: Menus, Edit menus, Pop-up buttons, Pull-down buttons.

<!-- visual:context-menus -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_context-menus, folha 0001), códigos conferidos; sem vídeo.
- O menu contextual nasce ancorado ao ponto de clique, logo abaixo e à direita do cursor, e não centralizado na tela (img 0398).
- A lista é vertical, com seis itens, e mistura itens com ícone geométrico na borda inicial e itens sem ícone no mesmo menu (img 0398).
- Os itens que abrem submenu são marcados apenas por uma seta para a direita na borda final, sem outro indicador, e aparecem juntos no fim da lista (img 0398).
- O item em destaque, por hover ou foco, é sinalizado por um fundo mais saturado da mesma paleta do menu, e não por uma cor de acento diferente (img 0398).
- O texto dos itens é vinho escuro sobre o fundo rosa claro do menu (img 0398).
<!-- /visual:context-menus -->

## Dock menus (slug: dock-menus)

No Mac, um secondary click no ícone do app ou jogo no Dock revela um Dock menu, que apresenta itens fornecidos pelo sistema e itens personalizados.

Por que: o Dock menu existe como um ponto de acesso rápido a comandos úteis mesmo quando o app não está em primeiro plano ou não tem janelas abertas, sem depender de o app estar visível na tela.

Faça e evite:
- Rotule os itens do Dock menu de forma sucinta e organize-os logicamente, como em qualquer menu.
- Disponibilize os itens personalizados do Dock menu também em outros lugares (como menus da menu bar ou na interface), porque nem todo mundo usa o Dock menu.
- Prefira itens personalizados de alto valor, como listar todas as janelas abertas ou recentes, e considerar ações úteis quando o app não está em primeiro plano ou não tem janelas abertas.

Especificações exatas: nenhuma.

Diferenças por plataforma: exclusivo de macOS; não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS. Em iOS e iPadOS existe um equivalente chamado Home Screen quick actions, revelado com toque e segure no ícone do app.

Ligações com outros artigos: Menus, Home Screen quick actions.

<!-- visual:dock-menus -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_dock-menus, folha 0001), códigos conferidos; sem vídeo.
- O Dock menu aparece como um balão com ponta triangular apontando de volta para o ícone de origem, posicionado acima dele, o que amarra visualmente o menu ao app (img 0469).
- No Dock estilizado, os ícones são quadrados vazios e três deles têm um pontinho vermelho abaixo marcando app aberto (img 0469).
- Os quatro itens se dividem em dois grupos por uma linha divisória, dois itens acima e dois abaixo, sendo "Show Recents" e "Open" o segundo grupo (img 0469).
- Itens que abrem submenu levam chevron para a direita, e itens de ação direta ficam sem chevron, em ambos os grupos (img 0469).
<!-- /visual:dock-menus -->

## Edit menus (slug: edit-menus)

Um edit menu permite alterar o conteúdo selecionado na view atual, além de oferecer comandos relacionados como Copy, Select, Translate e Look Up.

Por que: por ser o mecanismo padrão de edição em qualquer conteúdo selecionável (texto, imagens, arquivos, objetos como cartões de contato, gráficos ou localizações), o edit menu precisa se comportar de forma previsível e ser acionado pelos mesmos gestos que as pessoas já conhecem em cada plataforma, para que a edição pareça nativa em vez de reinventada por cada app.

Faça e evite:
- Prefira o edit menu fornecido pelo sistema; criar um menu customizado com os mesmos comandos é redundante e confuso.
- Deixe a pessoa revelar o edit menu pelas interações já conhecidas (toque e segure no touchscreen, pinça e segure em visionOS, secondary click com trackpad ou teclado conectado).
- Ofereça só os comandos relevantes ao contexto atual, removendo ou esmaecendo os que não se aplicam (ex. não mostrar Copy sem nada selecionado, nem Paste sem nada para colar).
- Liste comandos personalizados perto dos comandos do sistema equivalentes (ex. comandos de formatação depois dos comandos do sistema na seção de formato).
- Quando fizer sentido, permita selecionar e copiar texto não editável, como a legenda de uma imagem.
- Suporte undo e redo sempre que possível, já que um edit menu não exige confirmação antes de agir.
- Em geral, evite criar outros controles que dupliquem as funções do edit menu; isso só ocupa espaço que poderia ser usado para ações menos óbvias.
- Diferencie comandos de exclusão quando necessário: Delete se comporta como pressionar a tecla Delete, enquanto Cut copia o conteúdo para o pasteboard antes de excluir.
- Crie labels curtos para comandos personalizados, usando verbos ou frases verbais curtas.

Especificações exatas: nenhuma.

Diferenças por plataforma:
- iOS: o edit menu aparece em lista compacta e horizontal ao tocar e segurar ou tocar duas vezes para selecionar conteúdo; a pessoa pode tocar num chevron na borda final para expandi-lo em context menu.
- iPadOS: o layout do edit menu muda conforme a forma de revelação, horizontal e compacto com interações de toque, e diretamente como context menu quando revelado por teclado ou dispositivo apontador.
- macOS: os comandos de edição ficam acessíveis num context menu durante uma tarefa de edição e também pelo menu Edit na menu bar.
- visionOS: a pessoa usa o gesto padrão para abrir o edit menu como uma barra horizontal, ou pode abri-lo como context menu.
- Não suportado em tvOS ou watchOS, porque editar conteúdo é raro nessas experiências.

Ligações com outros artigos: Menus, Context menus, The menu bar, Undo and redo.

<!-- visual:edit-menus -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_edit-menus, folha 0001), códigos conferidos; sem vídeo.
- O edit menu é uma barra horizontal arredondada com quatro comandos em sequência (recortar, copiar, colar, apagar), separados por linhas verticais finas (img 0471).
- A barra termina num botão circular com chevron para a direita, que indica mais opções depois das ações diretas (img 0471).
- O menu surge acima do texto selecionado, e uma linha fina liga a ponta esquerda da barra à alça superior esquerda da seleção, marcando a relação de origem (img 0471).
- A seleção de texto é construída com fundo levemente destacado sobre a palavra, cursor vertical à direita dela e duas alças circulares vermelhas nas pontas, uma acima à esquerda e outra abaixo à direita (img 0471).
<!-- /visual:edit-menus -->

## Home Screen quick actions (slug: home-screen-quick-actions)

Home Screen quick actions dão à pessoa um jeito de executar ações específicas do app diretamente a partir da Home Screen, sem abrir o app primeiro.

Por que: certas ações de alto valor (buscar perto da localização atual, criar um novo item, abrir uma conversa recente) valem a pena ficar acessíveis com um único toque e segure no ícone, poupando o caminho de abrir o app e navegar até a função. Por isso a Apple recomenda reservar esse espaço só para tarefas realmente compensadoras.

Faça e evite:
- Crie quick actions só para tarefas de alto valor; é possível oferecer até quatro.
- Evite mudanças imprevisíveis nas quick actions; ações dinâmicas (baseadas em localização, atividade recente, horário do dia ou configurações) precisam mudar de um jeito que a pessoa consiga prever.
- Escreva um título sucinto que comunique instantaneamente o resultado da ação (ex. "Directions Home", "Create New Contact", "New Message"); use subtítulo se precisar de mais contexto. Não inclua o nome do app nem informação supérflua no título ou subtítulo, mantenha o texto curto para evitar truncamento e leve a localização em conta.
- Forneça um ícone de interface familiar para cada quick action, de preferência do SF Symbols; se desenhar um ícone próprio, use o Quick Action Icon Template dos Apple Design Resources.
- Não use emoji no lugar de um símbolo ou ícone de interface, porque o emoji é colorido enquanto o símbolo da quick action é monocromático e muda de aparência no Dark Mode para manter contraste.

Especificações exatas: limite de quatro quick actions por app.

Diferenças por plataforma: sem considerações adicionais em iOS ou iPadOS; não suportado em macOS, tvOS, visionOS ou watchOS (no macOS o equivalente é o Dock menu).

Ligações com outros artigos: Menus, Dock menus.

<!-- visual:home-screen-quick-actions -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_home-screen-quick-actions, folha 0001), códigos conferidos; sem vídeo.
- O menu de ações rápidas é um cartão único e claro, de cantos bem arredondados, ancorado logo acima do ícone de app que o originou (img 0543).
- O conteúdo é uma lista vertical de quatro linhas, cada uma com um símbolo geométrico simples na borda inicial e o rótulo em vermelho à direita (img 0543).
- Os outros ícones da fileira ficam desfocados de propósito, enquanto o ícone de origem aparece mais nítido, transferindo o foco da tela para o menu ativo (img 0543).
Divergências registradas: a descrição oficial fala só de itens de menu saindo de um ícone de app; a estrutura de linha com símbolo e rótulo, o cartão arredondado e o desfoque dos ícones vizinhos aparecem apenas na imagem.
<!-- /visual:home-screen-quick-actions -->

## Menus (slug: menus)

Um menu revela suas opções quando a pessoa interage com ele, funcionando como um jeito eficiente em espaço de apresentar comandos; este artigo estabelece as regras gerais de rotulagem e organização que valem para todos os tipos de menu (pop-up buttons, pull-down buttons, context menus, a menu bar etc.).

Por que: menus são onipresentes, então a maioria das pessoas já sabe usá-los; a Apple investe em manter um vocabulário consistente de rotulagem, ícones, organização, submenus e itens alternáveis (toggled) porque isso é o que faz um menu do sistema, ou de qualquer app, parecer familiar mesmo na primeira vez que alguém o abre.

Faça e evite (Labels):
- Escreva um label que descreva clara e sucintamente o item; use um verbo ou frase verbal para ações (View, Close, Select).
- Use capitalização title-style para ficar consistente com o resto da plataforma (embora um jogo possa ter estilo próprio).
- Remova artigos (a, an, the em inglês) dos labels para economizar espaço, já que raramente aumentam a compreensão.
- Mostre quando um item está indisponível, tipicamente esmaecido e sem resposta a interações; se todos os itens de um menu estiverem indisponíveis, o menu em si precisa continuar acessível.
- Acrescente reticências ao label quando a ação exigir mais informação antes de completar.

Faça e evite (Icons):
- Represente ações comuns de forma consistente, usando os ícones padrão do sistema para Share, Print, Search etc.
- Use ícones com moderação e propósito, só quando ajudam a encontrar o item mais rápido ou esclarecem o que a seleção faz; não exiba um ícone se não encontrar um que represente bem o item.
- Aplique um tratamento visual uniforme dentro do mesmo grupo: ou todos os itens do grupo têm ícone, ou nenhum tem.

Faça e evite (Organization):
- Liste os itens mais importantes ou usados com mais frequência primeiro, porque as pessoas tendem a escanear o menu de cima para baixo.
- Agrupe itens logicamente relacionados e use um separador para distingui-los visualmente.
- Mantenha comandos relacionados no mesmo grupo mesmo que tenham importância diferente entre si.
- Preste atenção ao comprimento do menu; considere dividir em menus separados ou usar um submenu se estiver longo demais. A exceção é conteúdo definido pela pessoa ou gerado dinamicamente (como History e Bookmarks no Safari), em que um menu longo com rolagem é aceitável.

Faça e evite (Submenus):
- Use submenus com moderação, já que cada um adiciona complexidade e esconde os itens que contém; considerar um submenu quando um termo aparece em mais de dois itens do mesmo grupo.
- Limite profundidade e comprimento: restrinja a um único nível hierárquico e, se o submenu tiver mais de aproximadamente cinco itens, considere criar um novo menu em vez disso.
- Mantenha um item de submenu acessível mesmo quando os itens aninhados estiverem indisponíveis.
- Prefira um submenu à indentação de itens, porque a indentação é inconsistente com o sistema.

Faça e evite (Toggled items):
- Considere um label mutável que descreva o estado atual (ex. um item que alterna entre "Show Map" e "Hide Map") em vez de dois itens separados.
- Inclua um verbo se o label mutável não for claro o suficiente sozinho (ex. "Turn HDR On" / "Turn HDR Off" em vez de só "HDR On" / "HDR Off").
- Se necessário, exiba os dois itens de ação ou estado ao mesmo tempo, em vez de um único item alternável.
- Considere usar um checkmark para mostrar que um atributo está em vigor, e ofereça um item que remova de uma vez vários atributos alternados (ex. "Plain").

Faça e evite (In-game menus): deixe os jogadores navegarem pelos menus do jogo usando o método de interação padrão da plataforma, e garanta que os menus continuem fáceis de abrir e ler em todas as plataformas suportadas, ajustando tamanho de tap target e forma de comunicar o conteúdo quando necessário.

Especificações exatas: em iOS, iPadOS e visionOS, o layout small do menu mostra uma fileira de quatro itens no topo (só símbolo ou ícone, sem label); o layout medium mostra uma fileira de três itens (símbolo ou ícone acima de um label curto); o layout large (padrão) mostra todos os itens em lista. Submenu com mais de aproximadamente cinco itens sugere criar um novo menu; menus em geral, no máximo cerca de três grupos separados por separador.

Diferenças por plataforma:
- iOS, iPadOS: três layouts possíveis (small, medium, large, descritos acima); o layout medium serve bem para cerca de três ações importantes (ex. Notes usa Scan, Lock, Pin); o layout small serve para ações intimamente relacionadas que aparecem como grupo (ex. Bold, Italic, Underline, Strikethrough), cada uma com símbolo reconhecível sem label.
- visionOS: pode usar os layouts small ou large definidos para iOS/iPadOS; é possível aplicar um breakthrough effect para manter o menu visível mesmo quando outro conteúdo o ocluir; como no macOS, um menu aberto numa janela do visionOS pode aparecer fora dos limites da janela. Prefira exibir o menu perto do conteúdo que ele controla. O efeito subtle é o padrão e mistura a apresentação com o conteúdo ao redor; prominent exibe o menu de forma mais proeminente sobre toda a cena mas pode atrapalhar e causar desconforto; none oculta totalmente o menu atrás de outro conteúdo 3D, o que pode dificultar acesso.
- Sem considerações adicionais em macOS, tvOS ou watchOS.

Ligações com outros artigos: Pop-up buttons, Pull-down buttons, Context menus, The menu bar.

<!-- visual:menus -->
### O que as ilustrações mostram
Base: 3 folhas de ilustrações vistas (hig-img_menus, folhas 0001 a 0003), códigos conferidos; sem vídeo.
- A abertura mostra um menu em cascata: três itens com atalhos de teclado alinhados à direita, um separador, e um item de submenu com seta para a direita que abre a lista secundária ao lado (img 0790).
- Dentro do submenu, o item ativo recebe preenchimento vermelho sólido e contrastante, que é a forma de sinalizar hover ou seleção momentânea (img 0790).
- Par de errado e certo com o mesmo conteúdo, os dias da semana: o errado põe um ícone arbitrário em cada dia, sem relação com o item, marcado com X em círculo cinza (img 0791, img 0792).
- O certo mostra o mesmo menu só com texto alinhado à esquerda, sem ícone algum, marcado com check em círculo verde (img 0793, img 0794).
- A regra de tratamento uniforme por grupo aparece num menu real de janela do macOS: o primeiro grupo não tem ícones e traz atalhos à direita; depois do separador, o segundo grupo tem ícone em todos os itens e seta de submenu à direita; linhas de chamada nomeiam cada grupo (img 0795).
- Um estado alternável é marcado só por um checkmark na margem esquerda do item, numa lista sem ícones, sem duplicar o item para cada estado (img 0796).
- O contraste entre img 0790 e img 0796 separa visualmente o destaque momentâneo, em cor sólida, do estado marcado persistente, em checkmark discreto.
- Os três layouts de menu do iOS e iPadOS são comparados com o mesmo conjunto de seis ações: no pequeno, quatro ações viram só ícones numa fileira compacta e as demais ficam abaixo como itens; no médio, três ações viram botões maiores com ícone e legenda e as outras seguem em lista com ícone à direita; no grande, as seis ficam numa lista vertical com texto à esquerda e ícone à direita (img 0797).
- No visionOS, o menu nasce ancorado logo abaixo do botão de mais opções, que aparece selecionado em branco sólido, sobre uma janela de app real (img 0798).
- Esse menu do visionOS combina uma fileira de três ícones no topo com uma lista de itens com ícone à direita, dividida em dois grupos por um separador (img 0798).
<!-- /visual:menus -->

## Ornaments (slug: ornaments)

Em visionOS, um ornament apresenta controles e informações relacionados a uma janela sem lotar ou obscurecer o conteúdo da janela; flutua num plano paralelo à janela e ligeiramente à frente dela no eixo z.

Por que: janelas em visionOS existem no espaço tridimensional, então a Apple criou o ornament como um jeito de manter controles frequentes num lugar consistente e previsível em relação à janela (acompanhando-a se ela se move, permanecendo inalterado se o conteúdo rola) sem competir por espaço dentro do próprio conteúdo.

Faça e evite:
- Considere um ornament para apresentar controles ou informações frequentemente necessários num local consistente que não sobrecarregue a janela; por ficar grudado à janela, a pessoa sempre sabe onde encontrá-lo (ex. Music usa um ornament para os controles de Now Playing).
- Em geral, mantenha um ornament visível; pode fazer sentido escondê-lo quando a pessoa mergulha no conteúdo da janela (assistindo a um vídeo, vendo uma foto), mas na maioria dos casos as pessoas preferem acesso constante.
- Se precisar de vários ornaments, priorize o equilíbrio visual geral da janela; considere limitar o número total para não aumentar o peso visual, e se decidir remover um ornament, pode realocar seus elementos para dentro da janela principal.
- Mantenha a largura do ornament igual ou mais estreita que a largura da janela associada, porque um ornament mais largo pode interferir numa tab bar ou noutro conteúdo vertical na lateral da janela.
- Considere usar botões sem borda (borderless) num ornament, já que o fundo padrão do ornament já é o material do visionOS, e o sistema aplica automaticamente o hover effect quando a pessoa olha para o botão.
- Use toolbars e tab bars fornecidos pelo sistema em vez de criar um ornament próprio para isso, porque no visionOS toolbars e tab bars já aparecem automaticamente como ornaments.

Especificações exatas: nenhuma.

Diferenças por plataforma: exclusivo de visionOS; não suportado em iOS, iPadOS, macOS, tvOS ou watchOS.

Ligações com outros artigos: Layout, Toolbars.

<!-- visual:ornaments -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_ornaments, folha 0001), códigos conferidos; sem vídeo.
- O ornament é desenhado como uma barra em pílula, de cantos totalmente arredondados, sobreposta à borda inferior da janela, e não dentro do corpo dela (img 0825).
- Setas de medida em vermelho cotam o ornament como componente com dimensões próprias: uma seta horizontal dupla acima dele marca a largura e uma seta vertical dupla à direita marca a altura (img 0825).
- A pílula, branca ou rosa claro, contrasta em tom com a janela em vermelho coral, que tem cantos arredondados na base (img 0825).
- Abaixo da pílula aparece um indicador de paginação, um ponto preenchido e uma barra alongada, sugerindo a página atual entre várias (img 0825).
Divergências registradas: a descrição oficial sugere uma grade de ferramenta de design ao fundo, mas na área visível da imagem a grade não aparece com clareza; só as setas de medida são visíveis.
<!-- /visual:ornaments -->

## Pop-up buttons (slug: pop-up-buttons)

Um pop-up button exibe um menu de opções mutuamente exclusivas; depois que a pessoa escolhe um item, o menu fecha e o botão pode atualizar seu conteúdo para indicar a seleção atual.

Por que: existe uma distinção deliberada entre "escolher um estado entre opções exclusivas" (pop-up button) e "escolher uma ação" (pull-down button); usar o componente certo comunica de antemão se a interação muda um valor ou dispara um comando, o que ajuda a pessoa a prever o resultado antes de tocar.

Faça e evite:
- Use um pop-up button para apresentar uma lista simples de opções ou estados mutuamente exclusivos; use um pull-down button, em vez disso, para oferecer uma lista de ações, permitir seleção múltipla ou incluir um submenu.
- Forneça uma seleção padrão útil; se a pessoa ainda não escolheu nada, o botão mostra o item padrão especificado, de preferência o que a maioria provavelmente quer.
- Dê um jeito de prever as opções do pop-up button sem abri-lo, como um label introdutório ou um label do próprio botão que descreva o efeito.
- Considere usar um pop-up button quando o espaço é limitado e não é necessário mostrar todas as opções o tempo todo, já que é um jeito eficiente em espaço de apresentar um leque amplo de escolhas.
- Se necessário, inclua uma opção Custom no menu para oferecer itens adicionais úteis só em algumas situações, evitando lotar a interface com controles usados raramente; é possível exibir um texto explicativo abaixo da lista.

Especificações exatas: nenhuma.

Diferenças por plataforma: sem considerações adicionais em iOS, macOS ou visionOS; não suportado em tvOS ou watchOS. Em iPadOS, dentro de um popover ou modal view, considere usar um pop-up button em vez de um disclosure indicator para apresentar múltiplas opções num item de lista, quando o conjunto de opções for pequeno e bem definido, permitindo escolher sem navegar até uma detail view.

Ligações com outros artigos: Pull-down buttons, Buttons, Menus.

<!-- visual:pop-up-buttons -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_pop-up-buttons, folha 0001), códigos conferidos; sem vídeo.
- A abertura diagrama o pop-up button como uma lista de quatro opções dentro de um retângulo tracejado, com a opção atual destacada num retângulo branco sólido de cantos arredondados (img 0883).
- O indicador do pop-up button é um controle de seta dupla, para cima e para baixo, dentro de um botão vermelho na borda final da linha selecionada (img 0883).
- Setas de medida anotam a largura total do menu e a altura da linha selecionada, sem tela real de app (img 0883).
- Na tela real do Calendar, o controle fechado fica numa lista agrupada padrão, com rótulos à esquerda e valores alinhados à direita, e mostra o valor atual escolhido (img 0884).
- Na mesma tela, as datas e horas de início e de fim aparecem em cápsulas cinza (img 0884).
- Aberto, o menu é um cartão branco com sombra que emerge sobre a própria lista, cobrindo parcialmente as linhas vizinhas, sem abrir painel novo (img 0885).
- A opção vigente é marcada com check, e a opção personalizada fica isolada no fim por um separador (img 0885).
- O par img 0884 e img 0885 mostra o mesmo controle primeiro fechado e depois aberto, como antes e depois.
<!-- /visual:pop-up-buttons -->

## Pull-down buttons (slug: pull-down-buttons)

Um pull-down button exibe um menu de itens ou ações diretamente relacionados ao propósito do próprio botão; depois que a pessoa escolhe um item, o menu fecha e o app executa a ação escolhida.

Por que: o pull-down button resolve o caso em que um botão precisa de variações da mesma ação (por exemplo, "Add" pode adicionar tipos diferentes de item) sem multiplicar botões na interface; por isso a Apple insiste em balancear o comprimento do menu, já que abrir o menu já é um passo extra antes de agir.

Faça e evite:
- Use um pull-down button para comandos ou itens diretamente relacionados à ação do botão (ex. um botão Add cujo menu especifica o tipo de item a adicionar; um botão Sort cujo menu escolhe o atributo de ordenação; um botão Back cujo menu escolhe um local específico para revisitar).
- Se precisar de uma lista de escolhas mutuamente exclusivas que não sejam comandos, use um pop-up button em vez disso.
- Evite colocar todas as ações de uma view num único pull-down button; as ações primárias precisam ser facilmente descobertas, não escondidas atrás de um menu que a pessoa precisa abrir antes de fazer qualquer coisa.
- Balanceie o comprimento do menu com a facilidade de uso: como é preciso interagir com o botão antes de ver o menu, listar no mínimo três itens ajuda a interação a valer a pena; para um ou dois itens, considere outros componentes (botões para ações, toggles ou switches para seleções); listar itens demais desacelera a busca por um item específico.
- Exiba um título de menu sucinto só se ele agregar significado; em geral o conteúdo do botão combinado com itens de menu descritivos já dá contexto suficiente.
- Avise quando um item do menu é destrutivo e peça confirmação; o texto vermelho destaca ações potencialmente destrutivas, e ao escolher uma delas o sistema exibe um action sheet (iOS) ou popover (iPadOS) para confirmar ou cancelar, o que ajuda a evitar perda de dados por engano.
- Inclua um ícone de interface junto a um item de menu quando isso agregar valor, de preferência usando SF Symbols para manter o alinhamento com o texto em qualquer escala.

Especificações exatas: mínimo recomendado de três itens para justificar um pull-down button.

Diferenças por plataforma: sem considerações adicionais em macOS ou visionOS; não suportado em tvOS ou watchOS. Em iOS e iPadOS, é possível revelar um menu pull-down por um gesto específico num botão (ex. desde o iOS 14, o Safari responde a toque e segure no botão Tabs mostrando um menu de ações relacionadas a abas, como New Tab e Close All Tabs); considere um botão More pull-down para apresentar itens que não precisam de posição de destaque na interface principal, pesando a conveniência do tamanho contra o impacto na descoberta, já que o ícone de reticências não necessariamente ajuda a pessoa a prever o conteúdo.

Ligações com outros artigos: Pop-up buttons, Buttons, Menus.

<!-- visual:pull-down-buttons -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_pull-down-buttons, folha 0001), códigos conferidos; sem vídeo.
- A abertura repete o diagrama do pop-up button (itens empilhados num retângulo tracejado, um deles em bloco branco sólido, setas de medida de largura e altura), mas troca a seta dupla por um chevron simples apontando para baixo (img 0915).
- Essa troca de indicador é a marca visual que separa lista de ações de escolha de valor único (img 0915).
- Na tela real do Notes, o botão More fechado fica na borda direita da barra superior, que também traz o botão de voltar e o ícone de compartilhar (img 0916).
- Aberto, o menu é um cartão branco com sombra que cobre parte do conteúdo da nota (img 0917).
- O mesmo menu mistura dois formatos: no topo, três ações rápidas em ícones lado a lado; abaixo, uma lista vertical de itens com ícone à esquerda (img 0917).
- Alguns itens da lista trazem seta de submenu, e um deles exibe texto secundário complementar ao rótulo (img 0917).
- A ação destrutiva fica por último, isolada por um separador e escrita em vermelho (img 0917).
- O par img 0916 e img 0917 mostra o mesmo botão fechado e aberto, com a mesma nota ao fundo.
<!-- /visual:pull-down-buttons -->

## The menu bar (slug: the-menu-bar)

No Mac ou num iPad, a menu bar no topo da tela exibe os menus de nível superior do app ou jogo; usuários de Mac já conhecem bem a menu bar e dependem dela para aprender o que um app faz e encontrar os comandos de que precisam.

Por que: a menu bar é o inventário completo e sempre disponível de tudo que um app pode fazer, por isso a Apple define uma ordem fixa de menus e uma estrutura interna padronizada para cada um (App, File, Edit, Format, View, menus específicos do app, Window, Help): isso permite que qualquer pessoa, mesmo usando o app pela primeira vez, saiba onde procurar um comando, e permite atribuir atalhos de teclado e dar acesso via Full Keyboard Access a comandos que talvez nem apareçam na interface principal.

Faça e evite:
- Suporte os menus padrão definidos pelo sistema e sua ordenação; em muitos casos o sistema já implementa a funcionalidade dos itens padrão (ex. Edit > Copy fica disponível automaticamente ao selecionar texto num campo padrão).
- Sempre mostre o mesmo conjunto de itens de menu; se um item não for acionável no contexto atual, desabilite a ação em vez de escondê-la, para que a pessoa continue aprendendo o que o app suporta.
- Represente ações com ícones familiares, os mesmos usados em outros pontos do sistema.
- Suporte os atalhos de teclado definidos para os itens padrão (Copy, Cut, Paste, Save, Print etc.); defina atalhos personalizados só quando necessário.
- Prefira títulos de menu curtos, de uma palavra; se precisar de mais de uma palavra, use capitalização title-style.
- Exiba sempre o item About primeiro no app menu, seguido de um separador para que fique sozinho em seu próprio grupo.
- No File menu, para "Open", inclua reticências se a pessoa precisar selecionar um item numa interface separada; em "Open Recent", liste nomes reconhecíveis (nunca caminhos de arquivo), do mais recente para o mais antigo.
- Prefira "Duplicate" a itens como "Save As", "Export" ou "Copy To", porque esses não deixam clara a relação entre o arquivo original e o novo.
- No Edit menu, torne claro o alvo de Undo e Redo (ex. "Undo Paste and Match Style", "Undo Typing"); use "Delete" (não "Erase" ou "Clear") porque equivale a pressionar a tecla Delete.
- No View menu, garanta que cada item show/hide reflita o estado atual da view correspondente (ex. "Show Toolbar" quando ela está oculta, "Hide Toolbar" quando está visível); ofereça um View menu mesmo que o app suporte só um subconjunto das funções padrão.
- Posicione os menus específicos do app entre View e Window, refletindo a hierarquia do app e ordenando do mais geral ou comum para o menos usado.
- Ofereça um Window menu mesmo que o app tenha só uma janela, incluindo os itens Minimize e Zoom para acesso via Full Keyboard Access; liste as janelas abertas em ordem alfabética, sem listar painéis ou outras modais.
- No Help menu, mantenha o número total de itens pequeno para não sobrecarregar quem busca ajuda; use um separador entre a documentação principal e itens adicionais.
- Use item de menu dinâmico (que muda de comportamento ao segurar uma tecla modificadora) com moderação, exigindo apenas uma tecla modificadora, e nunca como o único caminho para realizar uma tarefa, já que fica escondido por padrão; prefira usá-lo em menus da menu bar, não em context menus ou Dock menus, onde a descoberta é ainda mais difícil.
- Em menu bar extras, use um símbolo (ícone ou SF Symbol) para representar a extra, exiba um menu (não um popover) ao clicar, e deixe a pessoa (não o app) decidir se coloca a extra na menu bar, tipicamente via configurações; considere oferecer isso durante o setup por descoberta. Não dependa da presença da extra, já que o sistema pode escondê-la; considere também um Dock menu, que fica sempre disponível enquanto o app roda.

Especificações exatas:
- Ordem fixa dos menus na menu bar: YourAppName, File, Edit, Format, View, menus específicos do app (se houver), Window, Help; no macOS, o Apple menu fica na borda inicial e as menu bar extras na borda final.
- Nome curto do app no item "About YourAppName": preferir 16 caracteres ou menos, sem número de versão.
- A altura da menu bar é 24 pt.
- Tabela de itens padrão do app menu, na ordem: About YourAppName, Settings…, itens específicos opcionais, Services (só macOS), Hide YourAppName (só macOS), Hide Others (só macOS), Show All (só macOS), Quit YourAppName.
- Tabela de itens padrão do File menu, na ordem: New Item, Open, Open Recent, Close, Close Tab, Close File, Save, Save All, Duplicate, Rename…, Move To…, Export As…, Revert To, Page Setup…, Print….
- Tabela de itens padrão do Edit menu, na ordem: Undo, Redo, Cut, Copy, Paste, Paste and Match Style, Delete, Select All, Find (com submenus Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, Jump to Selection), Spelling and Grammar (com submenus Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, Correct Spelling Automatically), Substitutions (com submenus Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement), Transformations (com submenus Make Uppercase, Make Lowercase, Capitalize), Speech (com Start Speaking, Stop Speaking), Start Dictation, Emoji & Symbols.
- Tabela de itens padrão do Format menu: Font (submenus Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, Paste Style) e Text (submenus Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, Paste Ruler).
- Tabela de itens padrão do View menu: Show/Hide Tab Bar, Show All Tabs/Exit Tab Overview, Show/Hide Toolbar, Customize Toolbar, Show/Hide Sidebar, Enter/Exit Full Screen.
- Tabela de itens padrão do Window menu, na ordem: Minimize, Zoom, Show Previous Tab, Show Next Tab, Move Tab to New Window, Merge All Windows, Enter/Exit Full Screen (só se o app não tiver View menu), Bring All to Front, nome de cada janela específica aberta (em ordem alfabética).
- Tabela de itens do Help menu: Send YourAppName Feedback to Apple, YourAppName Help, Additional Item.

Diferenças por plataforma: não suportado em iOS (fora do contexto de iPad), tvOS, visionOS ou watchOS.
- iPadOS: a pessoa revela a menu bar movendo o ponteiro até a borda superior da tela ou deslizando para baixo a partir dela; quando visível, ocupa o mesmo espaço vertical que a status bar. Diferenças em relação ao macOS, segundo a tabela do texto: visibilidade (escondida até ser revelada, contra visível por padrão no macOS), alinhamento horizontal (centralizado, contra borda inicial no macOS), menu bar extras (não disponíveis no iPadOS), controles de janela (na menu bar quando o app está em full screen no iPadOS, nunca na menu bar no macOS), Apple menu (não disponível no iPadOS), app menu (sem About, Services e itens de visibilidade do app no iPadOS). Reserve o item Settings do app menu para abrir a página do app nas Settings do iPadOS; se o app tiver preferências internas próprias, adicione um item separado abaixo de Settings no mesmo grupo. Para apps com navegação por abas, considere adicionar cada aba como item do View menu, possivelmente com atalhos de teclado. Considere agrupar itens em submenus com mais frequência que no macOS, já que as linhas de item de menu no iPad usam mais espaço para facilitar o toque.
- macOS: o Apple menu é sempre o primeiro item na borda inicial e não pode ser modificado ou removido; quando o espaço é limitado, o sistema prioriza a exibição dos menus e das menu bar extras essenciais, podendo truncar títulos; ao entrar em full screen, a menu bar tipicamente se esconde até ser revelada.

Ligações com outros artigos: Menus, Dock menus, Standard keyboard shortcuts, Offering help, Status bars, Going full screen, Sidebars, Toolbars, Tab bars.

<!-- visual:the-menu-bar -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_the-menu-bar, folha 0001), códigos conferidos; sem vídeo.
- A abertura mostra uma barra de menus completa do macOS com os menus nome do app, arquivo, edição, formatação, visualização, janela e ajuda, e o menu de edição aberto e destacado em vermelho mais forte (img 1144).
- O menu de edição se organiza em três grupos separados por divisores: desfazer e refazer; recortar, copiar, colar e apagar; e buscar por último (img 1144).
- Cada item do menu de edição tem ícone na borda inicial, e os comandos de recortar, copiar, colar e buscar exibem o atalho de teclado à direita (img 1144).
- No iPad, em modo escuro, a barra de menus aparece centralizada no topo, entre a data e hora à esquerda e os ícones de rede e bateria à direita (img 1145).
- O menu de edição do iPad repete exatamente a estrutura do macOS, mas como painel claro flutuante sobre o fundo preto da tela (img 1144 comparada a img 1145).
- Os menu bar extras ficam no canto superior direito do Mac, como quatro ícones antes da data e hora (img 1146).
- O menu de um extra é um painel mais compacto, com três itens, um divisor antes do item que abre os ajustes, e sem atalhos de teclado ao lado dos itens (img 1146).
Divergências registradas: a descrição oficial fala em representação estilizada, mas a img 1144 mostra uma barra de menus funcional e detalhada; o estilizado se limita ao fundo em gradiente.
<!-- /visual:the-menu-bar -->

## Toolbars (slug: toolbars)

Uma toolbar dá acesso conveniente a comandos, controles, navegação e busca usados com frequência; é formada por um ou mais conjuntos de controles dispostos horizontalmente na borda superior ou inferior da view, agrupados em seções lógicas.

Por que: uma toolbar precisa equilibrar três funções ao mesmo tempo (título da view atual, navegação, e ações sobre o conteúdo), então a Apple estrutura o espaço em três zonas fixas (leading, center, trailing) com regras próprias de o que cabe em cada uma, para que a pessoa sempre saiba onde procurar voltar, o título ou uma ação, independente do app.

Faça e evite:
- Escolha os itens de forma deliberada para não sobrecarregar; defina quais itens migram para o overflow menu conforme a toolbar fica mais estreita, mas não adicione esse overflow manualmente (o sistema já faz isso automaticamente no macOS e iPadOS) nem crie layouts que causem overflow por padrão.
- Adicione um menu More para ações adicionais, priorizando as menos importantes; tente incluir tudo na toolbar primeiro e só use o More se realmente precisar.
- Em iPadOS e macOS, considere permitir customização da toolbar para incluir os itens mais comuns da pessoa, especialmente em apps com muitos itens ou usados por longos períodos.
- Reduza o uso de fundos personalizados e controles com tint na toolbar, porque podem sobrepor ou interferir nos efeitos de fundo do sistema; use a content layer para informar cor e aparência, e um ScrollEdgeEffectStyle quando precisar distinguir a área da toolbar da área de conteúdo.
- Evite aplicar cor parecida entre labels de item da toolbar e o fundo da content layer.
- Prefira componentes padrão na toolbar, cujo corner radius já é concêntrico com os cantos da barra; se criar um componente customizado, garanta a mesma concentricidade.
- Considere esconder temporariamente a toolbar para uma experiência sem distrações, de forma contextual, oferecendo um jeito confiável de restaurar os elementos escondidos.
- Dê um título útil a cada janela; se titular parecer redundante, deixe a área de título vazia. Não use o nome do app como título da janela. Escreva um título conciso, com menos de 15 caracteres, para deixar espaço para outros controles.
- Use os botões Back e Close padrão, com os símbolos padrão, sem label de texto "Back" ou "Close"; se criar uma versão customizada, garanta que continue com a mesma aparência e comportamento em todo o app.
- Forneça ações que apoiem as tarefas principais, priorizando os comandos mais prováveis; deixe claro o significado de cada controle, preferindo símbolos simples e reconhecíveis a texto (exceto para ações como edit, mal representadas por símbolos).
- Prefira símbolos fornecidos pelo sistema sem borda, já que a seção já fornece um contêiner visível e o sistema já define os estados de hover e seleção automaticamente.
- Use o estilo .prominent para ações-chave como Done ou Submit, especificando só uma ação primária, posicionada na borda final da toolbar.
- Posicione os itens nas três zonas: leading (elementos para voltar ao documento anterior, mostrar/esconder sidebar, o título da view e, ao lado, um document menu com comandos como Duplicate, Rename, Move, Export; itens dessa zona não são customizáveis para garantir disponibilidade constante), center (controles comuns e úteis, e o título da view se não estiver na leading; em macOS e iPadOS pode ser customizável pela pessoa, e colapsa automaticamente no overflow menu quando a janela encolhe), trailing (itens importantes que precisam ficar sempre disponíveis, botões que abrem inspectors próximos, campo de busca opcional, o menu More, e a ação primária como Done quando existir; permanece visível em qualquer tamanho de janela).
- Agrupe itens logicamente por função e frequência de uso; agrupe controles de navegação e ações críticas (Done, Close, Save) em seções dedicadas, familiares e visualmente distintas.
- Mantenha agrupamentos e posicionamento consistentes entre plataformas.
- Minimize o número de grupos, com no máximo cerca de três no geral.
- Mantenha ações com label de texto separadas de ações com símbolo, inserindo espaço fixo entre botões para evitar que o texto de labels diferentes pareça se fundir.

Especificações exatas: título de janela com menos de 15 caracteres; no máximo cerca de três grupos de itens na toolbar.

Diferenças por plataforma:
- iOS: priorize só os itens mais importantes na área principal da toolbar, já que o espaço é limitado, criando um menu More para o restante; use large title para ajudar a orientação durante navegação e rolagem, que por padrão transiciona para título padrão ao rolar e volta a large ao topo.
- iPadOS: considere combinar uma toolbar com uma tab bar, já que podem coexistir no mesmo espaço horizontal no topo da view, útil para navegar entre poucas áreas principais mantendo a largura total disponível para conteúdo.
- macOS: a toolbar fica na moldura superior da janela, abaixo ou integrada à title bar; títulos de janela podem aparecer inline com os controles, e itens de toolbar não têm bezel; torne todo item de toolbar disponível também como comando na menu bar, já que a toolbar pode ser customizada ou escondida e não pode ser o único lugar que apresenta um comando (o inverso não é necessário: nem todo item de menu precisa de espaço na toolbar).
- visionOS: a toolbar do sistema fica na borda inferior da janela, acima dos controles de gerenciamento de janela, num plano paralelo ligeiramente à frente da janela no eixo z; usa um variable blur no fundo da barra para manter a legibilidade dos itens conforme o conteúdo rola atrás; é possível fornecer símbolo, label de texto, ou ambos para cada item, e ao olhar para um item com símbolo o visionOS revela o label de texto; prefira a toolbar fornecida pelo sistema, otimizada para entrada por olhar e mão; evite criar uma toolbar vertical, porque tab bars já são verticais em visionOS e isso geraria confusão; tente impedir que a janela redimensione abaixo da largura da toolbar, já que visionOS não tem menu bar como rede de segurança; evite usar um pull-down menu numa toolbar, porque pode obscurecer os controles padrão da janela que ficam abaixo da borda inferior.
- watchOS: um toolbar button pode ficar nos cantos superiores ou ao longo da parte inferior; se colocado acima de conteúdo com rolagem, permanece visível enquanto o conteúdo rola por baixo; também é possível colocar um botão na própria view de rolagem, que por padrão fica escondido até a pessoa rolar para cima, aproveitando o hábito de rolar até o topo; use um scrolling toolbar button para uma ação importante que não seja a função primária da view (ex. Mail oferece New Message num toolbar button no topo do Inbox, cuja função primária é exibir a lista de mensagens).
- Sem considerações adicionais em tvOS.

Ligações com outros artigos: Sidebars, Tab bars, Layout, Buttons, Search fields, Apple Design Resources, Going full screen, Immersive experiences, Pull-down buttons, Icons, SF Symbols, Liquid Glass color.

<!-- visual:toolbars -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações vistas (hig-img_toolbars, folhas 0001 a 0006), códigos conferidos; sem vídeo.
- A abertura põe o botão de voltar isolado na borda inicial e três controles (editar, compartilhar, mais opções) numa cápsula única na borda final, com setas de régua marcando a extensão total da barra e a altura dos botões (img 1163).
- No Notes do Mac, a janela larga exibe a toolbar inteira com o menu More aberto; ao estreitar a janela, sobram poucos ícones e aparece um botão de overflow com seta dupla, cujo menu recolhe os itens que não couberam, inclusive o próprio More (img 1164, img 1165).
- Par de errado e certo no botão de voltar: a cápsula com seta e a palavra "Back" leva o selo de X cinza; o botão circular só com o símbolo leva o check verde; os selos ficam ao lado do botão, nunca sobre ele (img 1166, img 1167, img 1168, img 1169).
- O mesmo grupo de três ações aparece primeiro em texto, separado por divisores finos dentro da cápsula, e depois em símbolos (linhas de filtro, lixeira, sinal de mais), mais compacto e sem divisores visíveis (img 1170, img 1171).
- Símbolos com contorno circular próprio dentro da cápsula são contrastados com os mesmos símbolos soltos, sem borda, sobre o fundo compartilhado do grupo (img 1172, img 1173).
- A ação primária aparece como botão circular azul preenchido com check branco na borda final, separado do botão de filtro, que fica sem destaque (img 1174).
- No iPad, rótulos de zona ligados por linhas finas dividem a toolbar do Freeform em três regiões: voltar e título na borda inicial, grupo de seis ferramentas no centro, grupo de quatro ações na borda final (img 1175).
- No iPhone, o mesmo conjunto de controles é comparado numa cápsula única e em duas cápsulas, com voltar e avançar isolados da ferramenta e do mais opções (img 1176, img 1177).
- Um rótulo de texto e um símbolo dividindo a mesma cápsula são contrastados com a versão em que cada um ganha sua própria cápsula (img 1178, img 1179).
- No macOS, callouts de linha reta nomeiam a faixa superior da janela do Finder como toolbar e a borda externa como moldura da janela (img 1180).
- No visionOS, a toolbar é translúcida e fica na borda inferior da janela, com o rótulo de contagem de notas e ícones divididos por um separador; isolada, mostra quatro itens de rótulo com o selecionado em fundo mais opaco e o ambiente desfocado visível através do material (img 1181, img 1182).
- No watchOS, os botões de toolbar ocupam os cantos superiores ao redor do título azul, ou ficam em par na base da tela; e um par quase idêntico mostra a lista sem botão de ação e depois com um botão verde grande revelado entre o título e os itens, ao rolar até o topo (img 1183, img 1184, img 1185, img 1186).
Divergências registradas: na img 1174 a ação primária usa um ícone de check, e não o texto "Done" citado na descrição oficial.
<!-- /visual:toolbars -->

## O que este grupo revela sobre o jeito Apple

- Todo componente que esconde uma ação (context menu, edit menu, pull-down button, Home Screen quick action) vem acompanhado da regra de que a mesma ação precisa existir em algum lugar visível da interface principal: context-menus, edit-menus, pull-down-buttons, the-menu-bar (macOS: "torne todo item de toolbar disponível também na menu bar").
- A Apple trata "esconder um item indisponível" e "esmaecer um item indisponível" como duas técnicas distintas com contextos de uso opostos: menus normais e a menu bar esmaecem (para ensinar o que existe), context menus escondem (porque só mostram o que já é relevante): context-menus, menus, the-menu-bar.
- Existe uma distinção sistemática entre componentes de "estado mutuamente exclusivo" (pop-up buttons) e componentes de "ação ou comando" (pull-down buttons, toolbars, context menus), cada um com sua própria semântica de o que pode e não pode conter: pop-up-buttons, pull-down-buttons.
- Muitos artigos deste grupo restringem explicitamente o número de elementos simultâneos que a pessoa deve enxergar: um ou dois botões proeminentes (buttons), no máximo cerca de três grupos num context menu ou numa toolbar (context-menus, toolbars), até quatro Home Screen quick actions (home-screen-quick-actions), um único help button por janela (buttons), submenus limitados a um nível (context-menus, menus).
- A ordem estrutural importa tanto quanto o conteúdo: a menu bar tem uma sequência fixa de menus e cada menu tem uma tabela de itens em ordem definida (the-menu-bar); a toolbar tem três zonas fixas com regras próprias de customização por zona (toolbars).
- Em plataformas de entrada não convencional (visionOS), quase todo componente ganha uma camada extra de regras sobre percepção espacial: profundidade em relação à janela (ornaments, toolbars), breakthrough effect (menus), hover effect e feedback sonoro em vez de háptico (buttons, ornaments).
- A Apple prefere símbolos do sistema (SF Symbols) a texto sempre que a ação for reconhecível, reservando texto para quando um label curto comunica mais que um ícone; essa preferência aparece quase idêntica em buttons, toolbars, menus e home-screen-quick-actions.
- Ações destrutivas recebem tratamento visual e de fluxo específico e repetido: cor vermelha do sistema, posição ao final do menu, e confirmação obrigatória via alerta separado antes de executar, presente em buttons, context-menus e pull-down-buttons.
- Vários componentes deste grupo têm equivalentes diretos entre macOS e iOS/iPadOS que a Apple documenta lado a lado, tratando-os como a mesma função adaptada à plataforma: Dock menu (macOS) e Home Screen quick actions (iOS/iPadOS); a menu bar em macOS e em iPadOS, comparadas item a item numa tabela.
- A capacidade de personalização (customização de toolbar, menu bar extras, quick actions dinâmicas) vem sempre condicionada a uma âncora fixa e não customizável que garante previsibilidade mínima: a zona leading da toolbar não é customizável (toolbars), o Apple menu não pode ser modificado (the-menu-bar), e mudanças dinâmicas de quick action precisam ser previsíveis (home-screen-quick-actions).
- Extensões e integrações de terceiros (share/action extensions, menu bar extras, Dock menu) são tratadas como participantes de segunda classe deliberada: podem ser escondidas, reordenadas ou desativadas pelo sistema ou pela pessoa a qualquer momento, e por isso nenhuma delas pode ser o único caminho para uma função (activity-views, the-menu-bar).

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/activity-views.md, 46 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/buttons.md, 141 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/context-menus.md, 63 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/dock-menus.md, 25 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/edit-menus.md, 53 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/home-screen-quick-actions.md, 27 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/menus.md, 95 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/ornaments.md, 37 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pop-up-buttons.md, 42 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pull-down-buttons.md, 44 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/the-menu-bar.md, 196 linhas, lido até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/toolbars.md, 136 linhas, lido até o fim: sim

Todos os 12 arquivos do grupo foram lidos por inteiro numa única chamada da ferramenta Read cada, sem truncamento reportado pela ferramenta. Nenhum artigo deste grupo é só índice de coleção: todos os 12 têm texto próprio.

