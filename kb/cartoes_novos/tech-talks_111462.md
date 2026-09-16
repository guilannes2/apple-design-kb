## Raise the bar with iPhone Duo (id: tech-talks_111462, 15.7 min)

Base: transcrição (quadros ainda não vistos). Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111462/.

Tese central: No iPhone Duo, primeiro iPhone com várias telas e proporção mais larga, os controles que normalmente ficam no topo e na base (barra de navegação, toolbar e tab bar) passam para a lateral, onde ficam mais fáceis de alcançar e deixam o espaço vertical para o conteúdo; são os mesmos componentes adaptados a outro layout. Para aproveitar isso, o app precisa ser recompilado com os SDKs novos, usar as barras dos contêineres do sistema, preparar os itens personalizados para o eixo vertical e declarar prioridades de overflow para que o sistema se adapte.

O processo de design que a Apple descreve:
1. Entender o aparelho e o princípio: a silhueta mais larga dá espaço horizontal, os controles vão para o lado, a posição se mantém ao abrir para a tela interna em paisagem e, ao abrir em retrato, a tela maior volta ao layout familiar com barras horizontais.
2. Habilitar o novo comportamento: recompilar o app com os SDKs mais recentes e usar as barras fornecidas pelos contêineres de navegação, em vez de barras montadas à mão.
3. Entender onde o conteúdo é posicionado: navegação, toolbar e tab bar convivem numa região compartilhada, com regras próprias para Split View, inspetores, sheets e idiomas da direita para a esquerda.
4. Auditar a configuração atual da toolbar e garantir que os controles sigam a ordem recomendada, de cima para baixo.
5. Preparar o conteúdo da toolbar para o eixo vertical: fornecer título e ícone de cada item, ajustar o eixo quando o padrão não servir, reduzir itens só de texto e adaptar as custom views.
6. Gerenciar o overflow: decidir se toolbar ou tab bar comprime primeiro, consolidar o overflow próprio do app num único menu gerenciado pelo sistema e atribuir prioridades de visibilidade.
7. Avaliar se o app ou uma sheet específica deve desativar a barra vertical.
8. Fechamento: a ideia nasceu de perguntar se as barras precisavam mesmo ficar no topo e na base; o roteiro final repete quatro passos (recompilar com os SDKs novos, auditar as barras, atualizar itens personalizados, atribuir prioridades de overflow).

Princípios enunciados e o porquê:
- Todo designer é engenheiro e todo engenheiro é designer. O porquê: é preciso entender os dois lados para construir um app ótimo.
- Controles de topo e base vão para a lateral na proporção larga. O porquê: aproveita a largura, preserva espaço vertical para o conteúdo e deixa os controles mais fáceis de alcançar.
- A posição das barras se mantém ao abrir o aparelho para a tela interna em paisagem, e em retrato a tela maior volta às barras horizontais familiares. A fala não dá um porquê específico; apenas lembra que são os mesmos componentes, adaptados a outro layout.
- Manter os controles associados ao seu contêiner, mesmo sendo tentador mudar o eixo de todos. A fala o apresenta como resumo das regras anteriores: em layouts complexos, itens só vão para o eixo vertical quando o contêiner está na borda da tela.
- Inspetores expandidos não recebem barra vertical própria, já que a coluna Detail já tem uma. O porquê: evitar confusão.
- A barra fica do mesmo lado do aparelho em idiomas da direita para a esquerda; o conteúdo se adapta ao redor dela e ela permanece fixa. O porquê: a barra é alinhada ao hardware.
- Na vertical, os itens mantêm uma hierarquia clara de cima para baixo, com navegação principal no topo e ações proeminentes em seguida.
- Manter o posicionamento dos controles consistente. O porquê: nem toda pose usa barras verticais, e as pessoas não devem ter que reaprender onde ficam as ações.
- Barras verticais combinam melhor com itens só de símbolo. O porquê: diferente das horizontais (altura fixa, largura flexível), as verticais têm largura fixa e altura flexível.
- Fornecer de antemão todas as informações do item e deixar o sistema escolher a representação para cada contexto. O porquê: mesmo um item de imagem precisa de título, porque o sistema o usa quando o item vai para o overflow ou para uma forma expandida.
- Itens relacionados ficam no mesmo eixo. O porquê: um item que alterna entre símbolo e texto, como o botão de editar, não deve ir para a barra vertical mesmo que o símbolo coubesse nela.
- Minimizar itens só de título e custom views com texto e imagem. O porquê: assim mais conteúdo pode ir para a vertical, e na maioria dos casos esses itens podem usar a representação em símbolo.
- Perguntar se o texto só reforça o símbolo ou carrega informação própria. O porquê: se é suplementar, o símbolo sozinho geralmente comunica a ação com clareza; se traz informação significativa, o controle deve ficar na barra horizontal.
- Barras de acessório continuam presas ao teclado, sem ir para o eixo vertical (a fala não dá o porquê).
- O app não deve criar espaçamento adicional, seja a barra horizontal ou vertical (a fala não dá o porquê aqui e remete ao vídeo da Maria na DubDub25, termo incerto na transcrição automática).
- Em experiências focadas em navegação, a toolbar comprime primeiro. O porquê: os destinos principais continuam acessíveis. É o comportamento padrão.
- Em experiências orientadas a tarefas, a tab bar comprime primeiro. O porquê: preservar as ações acessadas com frequência.
- Consolidar o overflow próprio do app num único menu gerenciado pelo sistema; nem todo menu existente deve virar overflow.
- As reticências são o símbolo padrão de overflow no iPhone, então devem ser reservadas para esse uso, sem trazer símbolos de outras plataformas, e outros menus devem ganhar um símbolo distinto. A razão dada é apenas ser o símbolo padrão.
- Ao atribuir prioridades, pensar no que as pessoas acessam com mais frequência: ações usadas com frequência devem estar entre as últimas a ir para o overflow. Da mesma forma, controles que mostram status importante, como itens com badge, ficam visíveis por mais tempo. O porquê, para estes: preservar a leitura rápida (glanceability).
- A maioria dos apps é boa candidata à barra vertical, mas há casos em que vale desativar a barra. O porquê: num app de página única com layout pesado embaixo, o layout horizontal pode deixar o conteúdo se expandir por inteiro; numa sheet cheia de controles com um único item, a barra vertical reduziria o espaço disponível.
- Resultado buscado: conteúdo com sensação de espaço e controles acessíveis, a mesma experiência familiar feita para um iPhone totalmente novo.

Técnicas concretas de construção de interface, com números exatos quando falados:
- A fala não dá valores numéricos de interface (pontos, tamanhos, espaçamentos, durações). Os números ditos são contextuais: imaginar as barras girando 90 graus numa pilha vertical; API de badge adicionada no iOS 26; vídeo da Maria na DubDub25 (termo incerto na transcrição automática); What's new in SwiftUI da WWDC 26.
- Habilitação: recompilar com os SDKs mais recentes. Para outros comportamentos habilitados na recompilação, a fala indica a sessão Prepare Your App for iPhone Duo.
- Contêineres em SwiftUI: usar o modificador toolbar junto com Navigation Stack ou Navigation Split View; usar Tab View.
- Contêineres em UIKit: preferir UINavigationController e UITabBarController, que gerenciam as próprias barras; definir os toolbar items no view controller e colocá-lo num navigation controller, em vez de criar uma UIToolbar personalizada. Em barras personalizadas, o conteúdo de subcomponentes como UIToolBar, UINavigationBar ou UITabBar não é considerado.
- Região compartilhada: navegação, toolbar e tab bar coexistem numa região compartilhada, em combinações que dependem do layout.
- Split View: só a coluna Detail participa da barra vertical; itens das outras colunas continuam horizontais. Inspetores expandidos não ganham barra própria.
- Sheets: na tela externa, se a sheet já tem toolbar, ela aparece na vertical; na tela interna, ficam centralizadas por padrão com itens horizontais. Com a Preferred Placement API, uma sheet posicionada à esquerda fica sem barra vertical e uma posicionada à direita recebe uma.
- Idiomas da direita para a esquerda: a barra fica do mesmo lado do aparelho e o conteúdo se adapta em volta.
- Ordem dos itens: topo reservado para navegação principal, como voltar ou fechar, seguida de ações proeminentes, como concluir (done). Com navigation controller, o botão voltar é adicionado automaticamente.
- Botões personalizados de voltar ou fechar: em SwiftUI, placement cancellation action; em UIKit, leading item com leftItemSupplementsBackButton em false, que é o padrão.
- Ações proeminentes: em SwiftUI, placement top bar pinned trailing; em UIKit, pinned trailing group.
- Os demais itens mantêm o agrupamento original, com um espaçador vertical separando visualmente os posicionamentos de topo e de base, mesmo unificados numa só barra.
- Representação dos itens: o app informa ícone e título. Nas barras de topo e base o item prefere mostrar o ícone (botão de compartilhar); sem ícone, mostra o texto (botão de editar); no overflow, mostra título e ícone. Isso não muda com barras verticais.
- Escolha de eixo pelo sistema: itens descritos na fala como Text-only items with an icon (termo incerto na transcrição automática), como voltar e compartilhar, passam para o eixo vertical; itens só de texto, como editar, continuam no eixo horizontal. Usar Label em SwiftUI ou as propriedades de título e imagem de UIBarButtonItem já prepara o item.
- Por padrão, SwiftUI e UIKit inferem o eixo pelo conteúdo do item. Para ajustar, há a nova AxisBehavior API.
- Botão de editar do sistema fica na barra horizontal automaticamente. Item personalizado que alterna entre símbolo e texto: usar o comportamento de eixo horizontal only.
- Custom view em UIKit ou view mais complexa em SwiftUI fica horizontal por padrão; se tiver representação vertical, definir o comportamento de eixo preferido vertical para permitir que vá para a barra vertical.
- Badge: em vez de manter a contagem inline, usar badge no ícone para transformar um item com texto e símbolo num item só de símbolo; adotar a API de badge do iOS 26 para aparência padrão do sistema em todos os aparelhos.
- Custom views na vertical: devem caber na largura fixa da barra ou ter um layout adaptado à vertical; considerar ajustar métricas para a representação vertical.
- Detectar a barra vertical: ler a propriedade de ambiente ou trait toolbar vertical edge, dentro da content view ou da custom view do item. O valor é preenchido quando os itens podem ficar no eixo vertical e é nil ou unspecified quando não podem.
- Material: como as horizontais, a barra vertical não tem scroll edge effect por padrão, mas ganha fundo quando o ajuste de acessibilidade Reduzir Transparência está ativo; o conteúdo das custom views deve continuar legível em qualquer caso.
- Espaçadores: flexíveis têm tamanho zero no eixo vertical por padrão; fixos continuam respeitando o tamanho mínimo.
- Se as barras ainda não foram atualizadas para o novo design, ou os itens ainda não foram agrupados nas bordas leading e trailing, a fala diz que é o momento de fazer.
- Overflow: na tela externa em paisagem os itens transbordam mais porque há menos espaço vertical; a barra também transborda quando surgem elementos concorrentes, como o teclado ou picture in picture em OpenPortrait (termo incerto na transcrição automática).
- Toolbar compression behavior API: configura, por view, se toolbar ou tab bar comprime primeiro.
- Menu de overflow do sistema: toolbar overflow menu em SwiftUI; additional overflow items em UIKit.
- Prioridade de visibilidade: toolbar visibility priority permite atribuir a cada item prioridade alta, baixa ou personalizada, controlando a ordem em que colapsam. Priorizar primeiro por grupos e depois, se preciso, dentro de cada grupo. APIs de visibility priority existem em SwiftUI e UIKit.
- Desativar a barra vertical: APIs toolbar vertical behavior e preferred vertical bar behavior.

Exemplos citados:
- App da Maria: já era redimensionável, mas as barras continuavam horizontais. Ensina que falta recompilar com os SDKs novos e usar as barras dos contêineres.
- Notes usa toolbar, Clock usa tab bar e Fitness usa toolbar e tab bar. Ensina que a região compartilhada recebe combinações diferentes conforme o layout.
- Botões de compartilhar e editar: mostram como o sistema escolhe entre ícone e texto e em que eixo cada item fica.
- Botão de editar do Clock, que alterna entre símbolo e texto: não vai para a barra vertical, porque itens relacionados devem ficar no mesmo eixo.
- Botão personalizado de seleção: usa o comportamento de eixo horizontal only.
- View de bússola no canto superior direito: custom view que suporta representação vertical e por isso recebe o comportamento de eixo preferido vertical.
- Caixa de entrada com contagem inline trocada por badge: vira item só de símbolo, adequado à barra vertical.
- Botão de carrinho com o valor total em dólares: o texto carrega informação própria, então fica na barra horizontal.
- Painel de ações personalizado: esconde os títulos e fica um pouco mais curto quando há barra vertical, liberando espaço para outro conteúdo.
- Vista de podcast: experiência de navegação em que a toolbar comprime primeiro, o padrão.
- App Games: experiência orientada a tarefas em que a tab bar comprime primeiro.
- Compor no Mail e nova nota no Notes: ações frequentes que devem estar entre as últimas a ir para o overflow.
- Calculadora: app de página única com layout pesado embaixo, candidato a manter o layout horizontal.
- Sheet cheia de controles com só o botão de fechar: candidata a desativar a barra vertical para não reduzir o espaço.
- Piada de encerramento: perguntado se havia mais alguma coisa, a resposta é que está no menu de overflow.

Citações:
"What if bars didn't have to be at the top and the bottom?"
