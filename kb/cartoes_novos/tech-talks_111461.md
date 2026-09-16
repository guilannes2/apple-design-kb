## Prepare your app for iPhone Duo (id: tech-talks_111461, 10.2 min)

Base: transcrição (quadros ainda não vistos). Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111461/.

Tese central: David Jackson, gerente de engenharia do time de UI Frameworks, explica que o iPhone Duo obriga o app a mudar de tamanho em cada postura (aberto, fechado, girado ou dobrado), e que por isso as boas práticas de layout flexível e adaptativo importam mais do que nunca. Um app bem feito para o aparelho decide o layout por classes de tamanho, usa os componentes padrão de navegação e apresentação, respeita áreas seguras e margens assimétricas e recorre a regiões reservadas quando precisa de interface própria.

O processo de design que a Apple descreve:
1. Entender o ponto de partida sem fazer nada: o app já funciona no iPhone Duo mesmo sem ter sido compilado com o SDK do iOS 27. Com o aparelho fechado, ocupa o espaço à esquerda da barra de status e da câmera; aberto, aparece num tamanho e numa proporção familiares.
2. Aproveitar o trabalho já feito para o redimensionamento de apps de iPhone: com o SDK do iOS 27 adotado, o app se estende à esquerda da área da barra de status na tela interna.
3. Compilar com o SDK do iOS 27.1 para ocupar a tela inteira: o app vai até a borda, e os botões padrão de navegação e de barra de ferramentas passam a se dispor na vertical, abaixo da barra de status.
4. Baixar o Xcode 27.1, escolher o simulador do iPhone Duo no Device Hub (grafado também como "DeviceHub"; termo incerto na transcrição automática) e usar os botões de controle na parte de baixo da tela para abrir, fechar, girar ou dobrar o aparelho.
5. Com o app usando a tela toda, procurar problemas de layout em cada postura e aplicar as práticas gerais de layout flexível, para que o app se redimensione corretamente em qualquer plataforma.
6. Aplicar as orientações específicas do iPhone Duo: navegação e apresentações padrão, barras, áreas seguras, margens, teste em multitarefa de tela dividida e regiões reservadas.
7. Conferir tudo com a skill de modernização de apps do Xcode, agora chamada App Precisability (termo incerto na transcrição automática).
Na recapitulação final a ordem é: baixar o Xcode 27.1, simular o app no iPhone Duo pelo DeviceHub, seguir as práticas de layout adaptativo apresentadas e experimentar a skill App Precisability.

Princípios enunciados e o porquê:
- Layout flexível é mais importante do que nunca. O porquê: o app precisa se redimensionar para caber em todas as posturas, aberto, fechado, girado ou dobrado.
- O iPhone Duo é continuação de uma adaptação antiga, não uma ruptura. O porquê: apps de iPhone já se adaptaram a novos tamanhos e formatos de tela e a regiões especiais como a Dynamic Island; o Duo traz um novo formato de tela e uma nova posição de câmera. No iOS 27 as pessoas já podem deixar o app maior do que nunca pelo espelhamento do iPhone no Mac, e abrir e fechar o Duo funciona do mesmo jeito. O app pode reagir a outros limites de classe de tamanho, mas continua sendo um app de iPhone.
- Os melhores layouts são adaptativos ao longo de uma continuidade de aparelhos. O porquê: eles não presumem tamanho de tela nem capacidade do aparelho a partir do "user interface ADM" (termo incerto na transcrição automática) e usam ferramentas como as classes de tamanho para diferenciar layouts pequenos e grandes.
- Classes de tamanho expressam a experiência que o app deve oferecer conforme o espaço disponível. O porquê: as classes horizontal e vertical estão ligadas, de forma frouxa, ao espaço disponível em cada dimensão.
- Não decidir layout pela orientação da interface, assim como não se decide pelo Idiom; usar classes de tamanho. O porquê: na tela interna a orientação se comporta de outro modo e não respeita as orientações de interface suportadas pelo app.
- Evitar referência à tela principal (main screen) no código e, se possível, a qualquer tela. O porquê: num aparelho com duas telas essa referência é ambígua e será descontinuada numa versão futura. Preferir conceitos locais.
- Usar os padrões de navegação padrão. O porquê: são uma ótima forma de se adaptar a todas as posturas do iPhone Duo, e os componentes são totalmente adaptativos.
- Respeitar as áreas seguras. O porquê: garante que os controles do app fiquem alcançáveis e que o app fique inteiramente visível.
- Não presumir que as margens internas (insets) de lados opostos são iguais; tratar cada lado separadamente. O porquê: áreas seguras costumam ser assimétricas, especialmente no iPhone Duo, onde botões verticais podem aparecer do lado esquerdo em paisagem e na multitarefa de tela dividida.
- Margens de layout também são assimétricas. O porquê: isso deixa o conteúdo de primeiro plano chegar mais perto dos botões verticais e da barra de status sem perder a margem do lado oposto.
- Testar o tratamento das áreas seguras em configurações diferentes, sem exceção para a tela dividida. O porquê: o conteúdo disposto na vertical pode aparecer de qualquer lado do app.
- O iPhone Duo é uma ótima oportunidade para suportar a orientação paisagem (dito logo depois de explicar que a orientação na tela externa se comporta como em qualquer iPhone). O porquê: as pessoas podem querer apoiar o telefone como uma tenda.

Técnicas concretas de construção de interface, com números exatos quando falados:
- A fala não dá nenhum valor numérico de interface (pontos, tamanhos, margens, raios, durações). Os números ditos são só de versão: SDK do iOS 27, SDK do iOS 27.1, Xcode 27.1, APIs de concentricidade do iOS 26 e a sessão de "WW26" (termo incerto na transcrição automática).
- Classes de tamanho: no SwiftUI, ler pelo environment; no UIKit, pela trait collection.
- Combinações de classes de tamanho no iPhone Duo. Tela externa, como nos outros iPhones: em retrato, classe vertical regular e horizontal compacta; em paisagem, vertical e horizontal compactas. Tela interna: horizontal e vertical regulares, porque o espaço extra permite mostrar mais conteúdo, como barras laterais.
- Orientação: na tela externa se comporta como em qualquer iPhone; na tela interna não respeita as orientações suportadas.
- Acesso à tela: usar environment, trait collection ou os limites (bounds) da cena; se for mesmo preciso acessar a tela, obtê-la dinamicamente a partir da window scene.
- Cantos: para a interface encaixar perfeitamente nos cantos da tela, usar as APIs de concentricidade do iOS 26, atualizadas para os formatos de tela do Duo. No SwiftUI, Concentric Rectangle; no UIKit, UI Corner Configuration.
- Tela cheia e orientação: o Duo continua respeitando a chave "UI requires full screen", mas o app ainda se redimensiona quando a pessoa abre ou fecha o aparelho. O Duo respeita as orientações suportadas, mas o app é escalado na tela interna, inclusive na multitarefa de tela dividida.
- Navegação em colunas: Navigation Split View no SwiftUI ou UI Split View Controller no UIKit. Com o aparelho fechado, as colunas se recolhem numa pilha única de navegação; aberto, as colunas aparecem lado a lado e também sobrepostas.
- Abas: Tab View no SwiftUI e UI Tab Bar Controller no UIKit se adaptam a todas as posturas. Por padrão as abas aparecem nas telas interna e externa e se dispõem na vertical quando convém. Na tela interna dá para optar por uma barra lateral com navegação mais rica: no SwiftUI, definir o default tab bar placement como sidebar; no UIKit, definir o preferred placement como sidebar.
- Sheets: na tela externa podem ter botões dispostos na vertical; na tela interna ficam centralizadas. Popovers, menus de contexto e alertas também se adaptam a cada postura.
- Barras: barras de navegação, de ferramentas e de abas ficam fora da área segura e evitam sozinhas a interface do sistema, como a barra de status, e recursos de hardware, como a câmera. Barras horizontais fornecem insets em cima e embaixo; barras verticais fornecem insets nas laterais de início e fim (leading e trailing).
- Primeiro plano dentro da área segura: controles interativos vão dentro dela. No SwiftUI o conteúdo já fica na área segura por padrão; no UIKit, com layout manual, usar os safe area insets da view, ou usar Auto Layout prendendo as views ao safe area layout guide.
- Fundo fora da área segura: elementos de fundo, como arte que vai até as bordas, podem ocupar todo o espaço e passar por trás das barras de ferramentas e das barras laterais. No SwiftUI, "ignore safe area"; no UIKit, usar os bounds da view.
- Teste de tela dividida no Device Hub: visualizar o app na tela interna, arrastar o app pelo indicador de início (home indicator) na parte de baixo até um lado da tela, esperar surgir a área para soltar e depois arrastá-lo para o outro lado.
- Regiões reservadas, novidade do iOS 27.1: API para a interface própria usar o máximo possível da tela sem colidir com a interface do sistema. No SwiftUI, "reserved region", para posicionar elementos fora da área segura com segurança maximizando o espaço útil; no UIKit, UI View Reserved Region. Indicada para barras próprias ou interfaces que vão de borda a borda, e também para interfaces que se adaptam à dobra.
- Resumo das práticas de área segura dado na fala: usar barras padrão, que se adaptam sozinhas à área segura; alinhar o conteúdo interativo ou visível de primeiro plano à área segura, deixando o fundo passar dela; considerar e testar áreas seguras e margens assimétricas; em layouts mais complexos, considerar regiões reservadas.

Exemplos citados:
- As três etapas descritas na fala para o app no iPhone Duo (sem o SDK do iOS 27, com o SDK do iOS 27, com o SDK do iOS 27.1): em cada uma o app ocupa mais espaço de tela, até chegar à borda com os botões padrão dispostos na vertical sob a barra de status.
- Espelhamento do iPhone no Mac no iOS 27: permite deixar o app maior do que nunca, e abrir e fechar o Duo funciona do mesmo jeito; o app pode reagir a outros limites de classe de tamanho, mas continua sendo um app de iPhone.
- Telefone apoiado como uma tenda: justifica aproveitar o iPhone Duo para suportar paisagem.
- Barra lateral na tela interna: exemplo do conteúdo extra que as classes regulares permitem, tanto em layout como na opção de abas como sidebar.
- Botões verticais do lado esquerdo em paisagem e na tela dividida: caso concreto de área segura assimétrica e de por que tratar cada lado separadamente.
- Arte de fundo que vai até as bordas passando por trás de barras: caso de conteúdo que pode ignorar a área segura.
- Skill de modernização de apps apresentada na sessão "Modernize Your UI Kit App" (grafada depois como "Modernize your UIKit app"; termo incerto na transcrição automática), rebatizada no Xcode 27.1 como App Precisability (termo incerto na transcrição automática) e agora com suporte a SwiftUI e ao iPhone Duo: forma eficiente de conferir se o app segue todas as práticas de layout adaptativo.
- Sessões complementares citadas: "Leverage multiple displays and screens on iPhone Duo" (sobre as telas do aparelho), "Raise the bar with iPhone Duo" (sobre conteúdo disposto na vertical) e "Strike a pose" com layouts adaptativos no iPhone Duo (sobre regiões reservadas e interface que se adapta à dobra; título dito de forma ambígua na transcrição automática).

Citações:
"The best app layouts are adaptive across a continuum of devices." (David Jackson)
