# tech-talks

## Discover the Apple Design Resources (id: tech-talks_111427, 5.6 min)

Base: transcrição e 8 de 8 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/tech-talks/111427/.

Tese central: os Apple Design Resources (UI kits para Sketch e Figma, hardware bezels, Icon Composer, SF Symbols) existem para que quem tem uma ideia de app consiga expressá-la rapidamente com alta fidelidade ao resultado final, criando uma linguagem comum entre designer e engenheiro.

O processo de design que a Apple descreve: primeiro, ir a developer.apple.com/design/resources para ver tudo o que é disponibilizado. No Figma, carregar os kits pelo asset panel da própria UI ou pela Apple Community page, onde ficam publicados os UI kits de plataforma e os templates de tecnologia. No Sketch, ativar as libraries pelo painel de configurações (Library pane), bastando marcar uma caixa. Ao montar uma tela, usar os exemplos prontos (iPhone, iPad), que trazem o componente principal já no contexto de outros elementos, economizando tempo de montagem. Para conferir a aparência em dark mode, na fala o apresentador descreve selecionar o frame com os componentes, ir ao painel de design, seção appearance, escolher o menu com o ícone de swatch book e selecionar dark, o que redesenha todos os componentes daquele frame. Recomenda-se também abrir os arquivos originais dos kits para ver os guias internos de cor, materiais e estilos de texto.

Princípios enunciados e o porquê: os kits são tratados como produto de design em si ("designers making design tools for other designers"), por isso precisam ser organizados e fáceis de usar; usar o Human Interface Guidelines em conjunto com os kits, porque os kits sozinhos não explicam onde, quando e por que usar cada componente; manter os arquivos sincronizados com mudanças do sistema operacional, notificando o usuário quando uma library muda e permitindo aceitar a atualização, para que o mockup continue sendo uma representação fiel do produto final.

Técnicas concretas de construção de interface: o vídeo é sobre onde encontrar e como carregar os recursos, não descreve valores de layout, tipografia ou cor específicos.

Exemplos citados: asset panel do Figma e Apple Community page (fontes dos UI kits e templates de tecnologia no Figma); library pane do Sketch (ativação por checkbox); exemplos de composição para iPhone e iPad dentro dos kits; alternância para dark mode dentro do Figma como teste de fidelidade visual.

Citações: "designers who are making design tools for other designers" e "everyone is really literally speaking the same language".

<!-- visual:tech-talks_111427 -->
### O que as imagens mostram
Base: 8 de 8 folhas de quadros vistas, todos os códigos conferidos.
- Ferramentas de design em uso real na tela, não descritas de fora: Figma com painel de biblioteca de assets e painel de camadas, Sketch com artboard nomeado por modelo de iPhone e painel de biblioteca, e o Icon Composer com um painel de propriedades listando modo de renderização, gradientes, cor e fundo (folhas 0001 e 0003).
- Par claro e escuro do mesmo componente: a mesma folha de compartilhamento reaparece com texto, ícones e posições idênticos, invertendo só fundo e cor de texto, e o painel de camadas nomeia o segundo frame como versão escura (folha 0004, q0031 para q0034).
- Anatomia dessa folha de compartilhamento: cabeçalho com título e botão de fechar, fileira de avatares circulares com nome abaixo, grade de ícones de ação e lista textual de ações com ícone à esquerda, terminando em um botão de editar ações (folha 0004).
- Estrutura das páginas de recursos: barra horizontal de ícones de categoria por plataforma e por tipo de recurso, com cartões de download agrupados por sistema logo abaixo (folha 0002), e, na seção de molduras de produto, blocos em grade de três colunas com nome em negrito, formatos disponíveis e data e tamanho em cinza pequeno (folha 0001).
- Template fixo das páginas de diretriz: título grande do componente, parágrafo de definição, caixa lateral de plataformas suportadas com ícones de dispositivo e um cartão de exemplo em fundo gradiente que troca de cor conforme o componente, rosa em tabelas, laranja em botões suspensos, laranja e rosa em popovers (folha 0005, q0038 a q0041).
- Galeria de kits na página da comunidade: cartões de cor sólida diferente cada um, com pictograma branco de contorno ao centro, título em negrito abaixo e métricas pequenas no rodapé, em grade de cinco colunas, misturando kits por plataforma e cartões de tecnologias específicas (folha 0003).
- Extensão real do catálogo de exemplos, que a fala só menciona de longe: dezenas de miniaturas organizadas em grade por categoria de componente, a maioria em wireframe monocromático com poucas variações já coloridas, incluindo teclado em iPhone e iPad lado a lado e telas de bloqueio com cartões de notificação sobrepostos (folha 0006, q0046 a q0052).
- Seletor de cor do Sketch aberto sobre o mockup de iPhone em dois momentos, com grade quadriculada de matizes, barra de espectro completa, amostras recentes na base e controle de opacidade (folhas 0003 e 0004); no Icon Composer o controle de cor aparece em outra forma, como ajustes de gradiente com campo primário e percentual (folha 0001).
- Painéis de estilo dentro do arquivo do Sketch: amostras circulares grandes de cor em linha, escala de cinzas ao lado e um bloco de estilos de texto repetido em coluna clara e coluna escura (folha 0005).
- Mockup de tela inicial fiel ao sistema real: grade de ícones sobre papel de parede em degradê, dock de quatro ícones e barra de busca no rodapé, com widgets listados no painel de camadas ao lado (folha 0004).
- O próprio site sugerindo o material que documenta: o banner de destaque tem fundo de gradiente azul translúcido cortado por uma faixa diagonal mais clara, com título, subtítulo e dois links de texto abaixo (folha 0002).
- Único fluxo de captura de dado mostrado no vídeo: a janela do Feedback Assistant com barra lateral de itens salvos, formulário de campos rotulados empilhados, dois menus suspensos de triagem, zona de arrastar arquivo e botão de envio em roxo sólido contra um secundário em cinza (folha 0007).
- Slide de título em fundo cinza claro com texto preto alinhado à esquerda, contraste maior que os slides escuros vistos no outro vídeo do lote (folha 0002).
Proporção visual: predominam capturas de ferramenta e de site em tela cheia, intercaladas com o apresentador sentado à mesa com laptop e caderno, e a folha 0008 traz apenas um quadro de corte final sem interface.
Divergências ou limites registrados: na folha 0008 as notas registram que os demais lugares da grade de quadros estão vazios porque o vídeo termina logo depois, restando um único quadro real de transição, sem interface a descrever.
<!-- /visual:tech-talks_111427 -->

## Prepare your app for iPhone Duo (id: tech-talks_111461, 10.2 min)

Base: transcrição e 9 de 9 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111461/.

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

<!-- visual:tech-talks_111461 -->
### O que as imagens mostram
Base: 9 de 9 folhas de quadros vistas, todos os códigos conferidos.

- A comparação lado a lado do mesmo conteúdo em versões diferentes de SDK é o recurso de abertura, sempre com legenda de rodapé nomeando a versão: lista em coluna única sob "pre-iOS 27.0 SDK built apps" (folha 0001, q0005 e q0006), grade de duas colunas com um cartão a mais sob "iOS 27.0 SDK built apps" (folha 0001, q0008 e q0009) e grade de quatro cartões sob "iOS 27.1 SDK built apps" (folha 0002, q0010). O rótulo textual na tela fixa uma diferença que a fala descreve só em palavras.
- Size class é explicada primeiro por geometria abstrata, sem nenhum app real: retângulos cinza com setas de medida coloridas, laranja para a dimensão horizontal e azul para a vertical, com os rótulos compact e regular (folha 0004, q0028 e q0030), além de duas formas cinza sem rótulo, uma dobrada em ângulo como livro entreaberto e outra fechada com cantos arredondados (q0029). Antes disso, um retângulo simples ganha setas e os rótulos horizontal e vertical para ancorar o vocabulário (folha 0003, q0024 para q0025).
- Os painéis de código aparecem pareando SwiftUI e UIKit no mesmo quadro ou em sequência imediata, ao lado do render do aparelho ou da forma que o representa: environment de size class contra trait collection (folha 0003, q0024 e q0025), ConcentricRectangle contra UICornerConfiguration (folha 0005, q0037 para q0038), defaultTabBarPlacement contra a propriedade equivalente do tab bar controller (folha 0005, q0045; folha 0006, q0046), safeAreaInsets contra ignoresSafeArea (folha 0006, q0052 a q0054).
- Cor sólida e camada semitransparente marcam regiões da tela de dois modos distintos. O verde preenche a tela inteira, com cantos coincidindo com o contorno do aparelho, para demonstrar concentricidade sem conteúdo de app em volta (folha 0005, q0037 e q0038). O azul é camada semitransparente sobre o conteúdo e muda de significado entre quadros: primeiro cobre toda a área de conteúdo (folha 0006, q0052 e q0053), depois vai de borda a borda no fundo (folha 0007, q0055 e q0056) e por fim encolhe para uma faixa estreita só na borda esquerda (folha 0007, q0057), tornando visível a assimetria que a fala descreve.
- Um slide de medidas coloca duas setas rotuladas apontando para dentro do mesmo aparelho, "Layout Margin" sobre faixa roxa à esquerda e "Safe Area Inset" sobre faixa azul à direita (folha 0007, q0058), separando na imagem dois conceitos que a fala trata em frases seguidas.
- Uma ferramenta de design no Mac, com janela nomeada "iPhone", reaparece duas vezes para prototipar as poses do aparelho com o mesmo conteúdo: aberto, fechado ao lado de um painel preto sólido e todo aberto em formato de livro (folha 0002, q0011 a q0013), e depois a mesma tela de detalhe em pose aberta e comprimida em pose fechada (folha 0007, q0060 e q0061). É uma etapa de construção que a fala não detalha além de mencionar o Device Hub do Xcode.
- Os componentes de navegação ganham legenda de rodapé nomeando o que está em cena, "NavigationSplitView" e "TabView", sobre pares de mockups do Mail e de um app de saúde em dois tamanhos de aparelho (folha 0005, q0042 a q0045).
- A adaptação das sheets aparece na diferença entre quadros consecutivos: a folha sobreposta troca de conteúdo e um dos aparelhos passa a mostrar botões dispostos verticalmente na borda esquerda da tela (folha 0006, q0046 para q0047).
- Recursos recém-lançados são marcados dentro do próprio slide: selo retangular "NEW" no canto superior direito do slide que traz o rótulo de código UIViewReservedRegion (folha 0008, q0064 e q0065) e selo circular verde "27.1" no slide de codificação com agente (folha 0008, q0069 e q0070).
- A tela mostra uma interface de agente de código integrada ao editor que a fala não nomeia nesse trecho: ao lado do código Swift, o quadro seguinte ganha um balão de prompt com uma instrução de boas práticas de redimensionamento e a linha de status "Updating main screen references" (folha 0008, q0069 para q0070).
- As regras são entregues como listas curtas em tipografia branca sobre preto, com os itens surgindo aos poucos: "Orientation" passa de um para três itens (folha 0004, q0032 para q0033), "Screen" ganha o segundo item (q0034 para q0035), o resumo de área segura fecha em três pontos (folha 0008, q0067) e o encerramento lista três ações concretas (folha 0009, q0073).
- A lista de tópicos "Getting Started", "Flexible Layout" e "iPhone Duo Layout" funciona como marcador de capítulo, reaparecendo com o item corrente em negrito e os demais apagados (folha 0001, q0004; folha 0002, q0015), orientação que a fala não verbaliza a cada corte.
- A história do redimensionamento é visual: uma grade de seis miniaturas da mesma tela de Mail em formatos e proporções diferentes, incluindo o dobrável aberto, recebe depois o título "Evolution of iPhone apps" com um iPhone retangular reto destacado e semitransparente ao centro (folha 0002, q0017 e q0018).

Proporção visual: dos 75 quadros registrados, dezesseis mostram apenas o apresentador, em cortes curtos entre blocos; o restante são slides de tópico, renders de aparelho com app real, painéis de código, janelas de ferramenta de design e alguns quadros de abertura e de transição.

Divergências ou limites registrados: a folha 0008 anota que o rótulo "Agentic Coding" aparece na tela sem ser dito na fala do trecho, sendo uma adição visual do slide; a síntese das folhas anota que a ferramenta de design no Mac não é descrita em detalhe pela fala, que menciona apenas o Device Hub do Xcode.
<!-- /visual:tech-talks_111461 -->

## Design for iPhone Duo (id: tech-talks_111466, 10.8 min)

Base: transcrição e 13 de 13 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111466/.

Tese central: Dois designers do time de design da Apple, Marcos e Vince, apresentam o iPhone Duo, o primeiro iPhone dobrável, e defendem que o app deve parecer uma experiência única que se adapta aos diferentes tamanhos de tela e posições do aparelho. Para isso, em vez de um layout sob medida para cada posição, o caminho é mirar em duas size classes, levar os controles para a lateral e manter o app livremente redimensionável.

O processo de design que a Apple descreve:
1. A fala não descreve um processo interno de design em etapas; conta apenas que o time aprendeu muito ao adaptar os próprios apps ao iPhone Duo. O que segue é a ordem do roteiro da sessão.
2. Entender primeiro os princípios do aparelho: fechado, compacto e familiar; aberto, a maior tela já feita num iPhone; e as posições de uso (parcialmente dobrado como um livro, apoiado na mesa como um laptop com a tela interna voltada para a pessoa, ou em pé apoiado nas bordas).
3. Entender como o sistema reorganiza a interface: controles na lateral nas telas externa e interna, conteúdo afastado da dobra quando o aparelho está parcialmente dobrado, nova tela dividida 50/50 e picture in picture fixado no topo.
4. Adaptar o app mirando em duas size classes, com layout margins e horizontal safe area insets, sem desenhar um layout para cada posição.
5. Avaliar se vale um layout opcional para a posição apoiada na mesa, mantendo os mesmos controles e a mesma hierarquia.
6. Mapear os controles existentes do app de iPhone para a coluna lateral e tratar as exceções.
7. Resolver a assimetria da tela externa escolhendo entre deslocar o conteúdo, centralizar na tela inteira ou combinar as duas abordagens.
8. Escolher uma estratégia para a tela interna: split view, conteúdo otimizado para a tela larga ou tab bar apresentada como sidebar.
9. Conferir o comportamento de sheets em cada posição e usar componentes do sistema para herdar o desvio da dobra.

Princípios enunciados e o porquê:
- Fechado, o aparelho é compacto e familiar e cabe confortavelmente na mão; aberto, revela a maior e mais imersiva tela já feita num iPhone. O porquê: é a melhor tela possível para apps e conteúdo num aparelho que ainda cabe no bolso.
- Várias formas de segurar e apoiar o aparelho. O porquê: dá flexibilidade e deixa a pessoa usar o aparelho do jeito que quiser, em qualquer situação.
- Na tela externa, botões e controles que normalmente ficam no topo e na base passam para o lado direito. O porquê: maximiza o espaço vertical, fica mais fácil alcançar com o polegar direito e cria à esquerda uma área contínua para o conteúdo, comparável à de um iPhone com proporção tradicional. Na tela interna os controles também vão para a lateral, pelo mesmo motivo de espaço vertical e alcance.
- Com o aparelho parcialmente dobrado como um livro, o conteúdo sai da região central. O porquê: textos e imagens ficam mais fáceis de ler longe da curva, botões e elementos interativos ficam mais fáceis de acertar nas laterais, e a curva vira um divisor natural do layout.
- Em retrato, parcialmente dobrado, os elementos interativos descem para a metade de baixo. O porquê: ficam mais fáceis de alcançar e o aparelho continua estável sobre a superfície.
- A nova tela dividida é construída sobre o gesto de home do iPhone. O porquê: parece fluida e familiar; as duas metades funcionam de forma independente, então dá para manter uma tarefa de um lado enquanto se usa o outro.
- Na tela dividida, os controles ficam na borda externa; um app do lado esquerdo leva os controles para a borda esquerda. O porquê: ficam ao alcance do polegar e longe da região central.
- Não desenhar um layout para cada posição; mirar nas size classes e evitar larguras fixas, breakpoints ou métricas atreladas a uma tela específica. O porquê: as pessoas usam o aparelho em muitas posições e o app precisa ficar bem em todas; quem já usa essas ferramentas deve ter um app que já se adapta.
- Um layout especial para a posição na mesa precisa ter os mesmos controles e a mesma hierarquia geral das outras posições. O porquê: não se deve atrelar funcionalidade a uma posição específica.
- Barras horizontais só permanecem na tela interna em retrato. O porquê: ali há espaço vertical de sobra para o conteúdo.
- Na tela externa, a maior parte do conteúdo precisa de deslocamento. O porquê: para não ficar escondida atrás dos controles.
- Algumas interfaces ainda devem centralizar na tela inteira, sem deslocamento. O porquê: isso funciona bem para interfaces imersivas, muito visuais e que não rolam, desde que haja certeza de que os controles da direita não vão bloquear elementos interativos.
- Na tela interna, não entregar apenas um app de iPhone esticado.
- A hierarquia não deve mudar entre as telas externa e interna, e a funcionalidade não deve ficar limitada a uma posição. O porquê: as pessoas podem abrir e fechar o aparelho com frequência enquanto usam o app, então ele precisa ser previsível e consistente por dentro e por fora.
- A tab bar como sidebar não serve para todo app. O porquê: funciona melhor em apps densos em informação.
- Manter elementos interativos fora da região da curva sempre que possível. O porquê: o time descobriu que botões são difíceis de tocar quando caem exatamente na dobra. Conteúdo rolável não precisa evitar essa região.

Técnicas concretas de construção de interface, com números exatos quando falados:
- A fala não dá valores de interface em pontos, pixels, tamanhos de fonte, cores ou durações. Os números ditos são contagens estruturais: a divisão 50/50 da tela dividida, as duas size classes, o layout de duas colunas e as três opções para a tela interna.
- Size classes: compact width na tela externa e regular width na tela interna. Evitar larguras fixas, breakpoints e métricas de uma tela específica. Construir com layout margins e horizontal safe area insets e pensar o app como livremente redimensionável.
- Tela externa fechada: mais larga e mais baixa que a de um iPhone tradicional. A coluna lateral direita abriga a barra superior, as toolbars do app e controles de navegação como o botão de voltar, além da barra de status redesenhada e da Dynamic Island, que se expande verticalmente quando chegam Live Activities.
- Espaço vertical compartilhado: os controles do app dividem a coluna lateral com elementos dinâmicos do sistema (Live Activities e barra de status). Sem espaço suficiente, os controles do app recolhem automaticamente num menu de overflow.
- Mapeamento dos controles do app de iPhone: botões da toolbar do topo vão para o topo do espaço vertical; botões da toolbar de baixo vão para a base; a tab bar continua alinhada embaixo. Exceção: itens largos demais para o espaço da direita, como um botão de texto ou um "segment to control" (termo incerto na transcrição automática), ficam na barra de navegação.
- Barras horizontais: mantidas apenas na tela interna em retrato.
- Dobra: conteúdo sai do centro com o aparelho parcialmente dobrado; em retrato, os elementos interativos vão para a metade de baixo.
- Tela dividida: arrastar um app para o lado cria a divisão 50/50 em duas metades independentes; controles na borda externa de cada metade.
- Picture in picture: o vídeo pode ser fixado no topo da tela e o app atual se redimensiona verticalmente para o espaço restante; ao dobrar parcialmente, o vídeo passa a ocupar metade da tela, e os apps se ajustam verticalmente aos diferentes tamanhos de vídeo em tempo real.
- Layout opcional para a posição na mesa, pensado para uso sem as mãos: mídia no topo e controles tocáveis numa base estável embaixo.
- Layouts assimétricos na tela externa, que a fala chama de "layers" (termo incerto na transcrição automática), com três abordagens: (a) deslocar o conteúdo, o que acontece sozinho quando o app se alinha às horizontal safe area insets; (b) centralizar na tela inteira sem deslocamento, para interfaces imersivas, muito visuais e sem rolagem; (c) combinar uma imagem de fundo ou cabeçalho de largura total com conteúdo rolável em primeiro plano recuado, mantendo todo elemento interativo dentro da área rolável para que nada fique coberto.
- Tela interna, três opções: split views que mostram vários níveis da hierarquia do app ao mesmo tempo; conteúdo otimizado para a tela larga, por exemplo uma pilha vertical que se reorganiza em duas colunas quando há mais espaço horizontal; e, para apps com tab bar, apresentar a tab bar como sidebar.
- Sheets na tela externa: por padrão os controles da sheet também vão para a lateral. Dá para impedir isso desativando a barra vertical na sheet, o que funciona bem para sheets com um único botão de toolbar; nesse caso a sheet para logo antes da câmera frontal e a barra de status se reposiciona.
- Sheets na tela interna, em paisagem e em retrato: usam as barras horizontais padrão. Com o aparelho parcialmente dobrado, as sheets deslizam para o lado para não repousar na dobra.
- Desvio da dobra: comportamento que empurra elementos interativos para longe da dobra quando o aparelho está parcialmente dobrado, embutido em componentes do sistema como sheets, alerts, menus, botões de toolbar e outros. Usar esses componentes sempre que possível para ganhar o mesmo comportamento no app. Conteúdo rolável não precisa evitar a região.

Exemplos citados:
- Posições de uso (livro parcialmente dobrado, laptop sobre a mesa, em pé sobre as bordas): ensinam que o app precisa funcionar em muitas configurações sem um design para cada uma.
- Tela dividida para manter uma tarefa de um lado enquanto se usa a outra metade: ensina que as metades são independentes e que os controles vão para a borda externa.
- Vídeo em picture in picture fixado no topo, que cresce até metade da tela ao dobrar: ensina que os apps precisam se ajustar verticalmente em tempo real.
- Uso sem as mãos com o aparelho sobre a mesa, com mídia em cima e controles embaixo: ensina que um layout por posição é opcional e não pode mudar controles nem hierarquia.
- Os próprios apps da Apple adaptados ao iPhone Duo: o time aprendeu que várias abordagens funcionam bem conforme o estilo do conteúdo.
- App Saúde (Health) com a tab bar apresentada como sidebar na tela interna: ensina que a sidebar funciona melhor em apps densos em informação.
- Sheet com um único botão de toolbar e a barra vertical desativada: ensina quando vale impedir que os controles da sheet migrem para a lateral.

Citações:
"Apps should feel like a single experience adapting to the different display sizes and poses."
"You don't want to tie functionality to a specific pose."

<!-- visual:tech-talks_111466 -->
### O que as imagens mostram
Base: 13 de 13 folhas de quadros vistas, todos os códigos conferidos.

- A coluna de controles presa à borda direita não é mostrada uma vez e explicada, é repetida quase idêntica em vários apps do sistema: e-mail com lixeira, arquivar, responder e compor empilhados (folha 0003, q0019, q0020 e q0023), chamadas com os controles dentro de uma cápsula vertical (q0021), lembretes com a barra de ícones fora do bloco de conteúdo (q0026), FaceTime com botões circulares e o de encerrar em vermelho no fim da coluna (folha 0004, q0028) e o player de música (folha 0012, q0108). A fala enuncia o padrão de forma geral; a imagem mostra que ele é o mesmo em pelo menos cinco apps.
- As medidas aparecem desenhadas sobre a captura real, não em diagrama separado: faixa cinza sólida entre as colunas de texto rotulada "Layout Margin" (folha 0006, q0050) e faixa azul cobrindo a borda direita rotulada "Horizontal Safe Area Inset" (folha 0006, q0051; folha 0009, q0076, esta com o rótulo escrito fora da moldura do aparelho). De um quadro para o outro a anotação troca de cor e de posição, saindo do centro do texto para a borda da tela.
- As duas classes de tamanho são nomeadas por escrito sob os aparelhos, "Compact Width" em tela única estreita e "Regular Width" em tela larga com lista e mensagem lado a lado, com o mesmo conteúdo de e-mail nas duas (folha 0006, q0049).
- A grade de seis renders do mesmo app em todas as poses, fechado em retrato, fechado em paisagem, aberto reto e dobrado em ângulos variados, aparece duas vezes no vídeo com conteúdos diferentes, e-mail e editor de lista (folha 0006, q0047 e q0048; folha 0011, q0093 e q0094). É o argumento visual de uma interface única adaptável, sem redesenho por pose.
- A reorganização ao dobrar é mostrada por quadros consecutivos com o mesmo conteúdo: o vídeo em tela cheia passa a ocupar a metade superior com a conversa embaixo (folha 0005, q0043 para q0044), os controles do player descem para a metade inferior (folha 0004, q0031 para q0032) e a miniatura do participante de FaceTime muda de posição (folha 0004, q0028 para q0029).
- O padrão de tela dividida é nomeado na tela com o rótulo "Split View" sob a captura (folha 0010, q0084), enquanto os demais exemplos aparecem sem rótulo em Mapas, Mensagens, Música, Saúde e Fotos (folhas 0004, 0005, 0010, 0011 e 0012), inclusive comparado em dois tamanhos de aparelho com a divisão mantendo a proporção (folha 0010, q0087).
- Nos pares de tela dividida cada metade ancora os próprios controles na borda externa, o app da esquerda à esquerda e o da direita à direita (folha 0005, q0037 a q0040), e a troca de posição entre os dois apps mantém essa ancoragem (q0039 para q0040).
- A barra lateral no lugar da barra de abas aparece em um único app, o de saúde, com lista vertical de categorias com ícone e texto na coluna esquerda e o cartão de pontuação de sono à direita (folha 0010, q0090; folha 0011, q0091).
- O caso da interface imersiva sem deslocamento é mostrado por contraste direto: o app de nível com círculo verde centralizado em aparelho estreito passa a preencher a tela inteira de verde no aparelho aberto e largo (folha 0009, q0077 para q0078), enquanto os demais exemplos mantêm o conteúdo recuado para longe dos controles.
- O ganho de largura reorganiza o conteúdo em mais colunas: a mesma tela de edição de lista ganha colunas adicionais de ícones ao passar de aparelho estreito para largo (folha 0011, q0097 para q0098) e depois divide o espaço com a lista de tarefas correspondente quando o aparelho é dobrado (q0099).
- Faixas de destaque marcam grupos de controle dentro da coluna lateral: uma faixa cinza recai exatamente sobre os quatro ícones de ação na base, separando esse grupo do restante (folha 0008, q0067 para q0068), e um botão em pílula branca "Select" surge no canto superior em quadro seguinte (q0070 para q0071).
- A hierarquia tipográfica por opacidade aparece na tela de música: a linha atual da letra em branco pleno e as seguintes em cinza claro, sem nenhum controle de reprodução visível no quadro (folha 0006, q0054).
- O hardware é apresentado sem interface alguma, em renders de estúdio sobre fundo branco neutro, mostrando a geometria do aparelho, o entalhe da câmera frontal e, em aproximação, a borda arredondada e um botão (folha 0002, q0017 e q0018).
- Cartões de título pretos com duas linhas, uma em cinza e outra em branco, abrem o vídeo e reaparecem idênticos na virada de seção (folha 0001, q0004; folha 0006, q0046).

Proporção visual: dos 112 quadros registrados, vinte e sete mostram apenas os apresentadores, sozinhos ou os dois juntos; os outros três quartos são renders de aparelho com apps reais em uso, comparações anotadas, telas do sistema, cartões de título, renders de hardware e transições borradas.

Divergências ou limites registrados: a folha 0007 anota que a faixa cinza cobrindo a metade inferior de um dos aparelhos não pode ser interpretada com certeza só pela imagem; a folha 0012 anota que a fala trata de sheets enquanto os quadros mostram telas divididas de outros apps, sem relação direta visível; a folha 0002 anota que os renders de hardware não têm relação direta de conteúdo com a frase sobre controles dita no mesmo trecho.
<!-- /visual:tech-talks_111466 -->

## Raise the bar with iPhone Duo (id: tech-talks_111462, 15.7 min)

Base: transcrição e 20 de 20 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111462/.

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

<!-- visual:tech-talks_111462 -->
### O que as imagens mostram
Base: 20 de 20 folhas de quadros vistas, todos os códigos conferidos.

- A tese do vídeo é demonstrada com o mesmo app em dois eixos: o app de escalada aparece com a barra de abas horizontal no rodapé e depois com os mesmos três ícones empilhados na borda direita, na mesma ordem, com cabeçalho e lista inalterados (folha 0003, q0023 e q0027). Só a barra muda de eixo, nada mais.
- O certo e o errado são marcados dentro do código, com check verde no bloco que usa contêiner de navegação e X vermelho no bloco que instancia a barra de ferramentas diretamente, e ao lado o app de água mostrando a barra vertical fina que resulta do caminho aprovado (folha 0004, q0034 e q0035).
- A justaposição de código e resultado é sistemática, uma folha atrás da outra: comentário nomeando a API, trecho com realce de sintaxe e o mockup correspondente ao lado (folhas 0004, 0007, 0008, 0010, 0011, 0012, 0014, 0016, 0018 e 0019). Em um caso o realce azul muda de trecho entre quadros consecutivos enquanto o mockup do Mail fica idêntico, dirigindo o olho para a linha em questão (folha 0007, q0061 para q0062).
- O agrupamento dentro da barra vertical é mostrado isolado, sem app em volta: fechar e enviar colados no topo, um espaçador vertical vazio e um ícone solto abaixo (folha 0008, q0067), em quadro vizinho ao do código de grupo fixado ao fim da barra, que aparece junto do mockup do Mail (q0066).
- A permanência da barra do mesmo lado em idioma da direita para a esquerda é mostrada por dois calendários lado a lado, um em inglês e outro em árabe: o texto do conteúdo espelha, a coluna de ícones fica na borda direita nos dois (folha 0007, q0055).
- A diferença entre item de texto e item de símbolo aparece em comparação de aparelhos: no comum, "Edit" em texto e o ícone de compartilhar convivem na barra horizontal do topo; no dobrável, o de compartilhar migra para a barra vertical lateral e "Edit" fica onde estava (folha 0010, q0082 a q0085), com o código de rótulo com imagem ao lado.
- Uma instrução ganha um cartão tipográfico só dela, texto branco grande centralizado sobre preto, entrando por fade de baixo contraste para branco pleno: "Provide titles." (folha 0010, q0088 para q0089).
- O item que alterna entre texto e símbolo é mostrado nos dois estados: o relógio mundial passa do botão "Edit" em texto para um círculo laranja de confirmação, e cada linha da lista ganha um indicador vermelho de remoção (folha 0011, q0095 para q0096); em quadro posterior, o código que força o eixo horizontal para esse tipo de botão aparece ao lado de outro app, o de planejamento de viagem (q0099).
- A troca de contagem inline por badge é feita por um par de quadros com o resto do layout congelado: o ícone de caixa de entrada mostra um número solto ao lado e depois um badge circular vermelho sobre o próprio ícone (folha 0012, q0107 para q0108). O mesmo badge reaparece na barra vertical do calendário (folha 0018, q0159).
- APIs novas recebem um selo circular verde "NEW" acrescentado ao quadro seguinte, sem mudar o código mostrado (folha 0014, q0119 para q0120), e depois sobreposto ao mockup do aparelho (q0122).
- Um único quadro abandona o mockup de tela e usa metáfora espacial: controles em cápsulas soltas flutuando em perspectiva sobre um piso quadriculado, agrupados por proximidade, com o botão vermelho de play à parte (folha 0009, q0074). Não há equivalente em nenhuma outra folha.
- As reticências recebem tratamento de símbolo reservado: um quadro inteiro com três pontos ampliados sobre preto, sem mais nada (folha 0017, q0145), e depois o mesmo símbolo na base de um painel vertical de cinco ícones de viagem, separado dos demais por um leve espaço (folha 0017, q0150).
- Os casos de desativar a barra vertical vêm em comparação de aparelhos: a calculadora passa de grade numérica vertical compacta no aparelho comum para uma faixa horizontal alargada no dobrável, com a mesma contagem de botões (folha 0019, q0164), e o painel de formatação de texto mantém o conteúdo centrado com a barra lateral reduzida a três ícones (folha 0019, q0165 e q0166).
- O caso do inspetor é mostrado com um editor de formas: a barra lateral some, o canvas ganha destaque e então abre um painel "Properties" à direita com campos rotulados à esquerda e valores à direita, opacidade em 100 por cento e coordenadas de posição (folha 0006, q0046 a q0048). Na mesma folha, o diálogo de nova lista aparece com barra vertical quando ocupa a tela toda e com barra horizontal no topo quando vira painel ao lado de uma coluna lateral (folha 0006, q0052 e q0053).
- Slides de agenda em preto e branco, sem ícone, com o tópico corrente em branco e os demais em cinza, aparecem quatro vezes ao longo do vídeo (folha 0003, q0019 e q0025; folha 0008, q0071; folha 0015, q0131), e o encerramento repete o padrão com o título e três ações surgindo abaixo dele (folha 0020, q0172 para q0173).

Proporção visual: dos 175 quadros registrados, cerca de noventa e cinco mostram apenas as apresentadoras, sozinhas ou as duas em conversa; o restante são mockups de app em aparelho comum e dobrável, blocos de código, slides de agenda e quadros isolados de hardware e de metáfora espacial.

Divergências ou limites registrados: a síntese das folhas anota que a duplicação de mockups lado a lado e a justaposição de código e resultado são escolhas editoriais da apresentação que a fala não descreve, tratando apenas de eixo e orientação em palavras; a folha 0013 registra um par de quadros sem diferença de conteúdo, apenas repetição do mesmo par de mockups.
<!-- /visual:tech-talks_111462 -->

## Strike a pose with adaptive layouts on iPhone Duo (id: tech-talks_111463, 18.0 min)

Base: transcrição e 15 de 15 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111463/.

Tese central: No iPhone Duo, a dobradiça e as câmeras criam reserved regions, e o bom design depende de saber quando adaptar: mover, redimensionar ou reorganizar o que já existe (o padrão de displacement) para manter conteúdo e controles visíveis, alcançáveis e desobstruídos em qualquer pose. Para isso a Apple apresenta a API de reserved regions, para layouts montados à mão, e os arrangements (split e overlay), contêineres de layout para duas views, sempre adaptando só quando isso melhora a experiência.

O processo de design que a Apple descreve:
1. Entender o aparelho: várias telas, cada uma com sua própria size class, o que deve soar familiar para quem já projeta para redimensionamento; recursos de hardware (a dobradiça e as duas câmeras das telas externa e interna) moldam o espaço disponível e são chamados de reserved regions, a serem tratados como qualquer outra área a que o layout já se adapta.
2. Entender cada tela: na externa, a câmera está sempre presente e toolbars e tab bars do sistema ficam na vertical dentro da nova safe area; na interna, a interface pode se adaptar à dobra ou à nova câmera FaceTime quando ativa; com o aparelho parcialmente dobrado como um livro, a dobra divide a tela interna em várias regiões usáveis.
3. Saber quando adaptar: muitas interfaces fluem naturalmente em volta das reserved regions; outras pedem uma abordagem intencional, o displacement.
4. Escolher o escopo do deslocamento: de um botão a um contêiner inteiro ou partes maiores do layout.
5. Decidir para onde o elemento vai, guiado pelo seu propósito e pela pose do aparelho (como livro ou apoiado na mesa), priorizando o que é contextual quando mais de uma região serve.
6. Considerar como o elemento se adapta ao novo entorno: posição e tamanho são as mudanças mais comuns, mas outras propriedades visuais também podem mudar.
7. Implementar com a API de reserved regions em SwiftUI ou UIKit, consultando regiões de divisão e de oclusão, ativas ou inativas.
8. Aproveitar os componentes do sistema que já se adaptam à dobra e, para layouts de duas views, usar arrangements, escolhendo entre split e overlay e reconhecendo quando um arrangement não é a ferramenta certa.
9. Roteiro final de preparação: auditar os layouts centralizados do app; considerar se dá para transformá-los em layout de duas colunas ou qual padrão de displacement faz sentido; usar contêineres e apresentações padrão do sistema, que trazem muito comportamento de graça; em layouts personalizados de split horizontal ou de overlay, considerar a arrangement view para cuidar do layout em todos os aparelhos suportados; identificar os controles de maior prioridade posicionados manualmente e adotar a Reserved Regions API para o displacement próprio onde for preciso.
10. Para usar a dobradiça além do layout, há outra API que responde ao estado de dobra, tratada na sessão Leverage Multiple Displays and Scenes on iPhone Duo.

Princípios enunciados e o porquê:
- Conteúdo e controles que atravessam a dobra se comportam como uma foto espalhada pelas duas páginas de um livro. O porquê: perto da lombada, partes da imagem ficam difíceis de ver e ela deixa de ser lida como uma imagem contínua.
- Na tela interna, se o visor da câmera FaceTime é central na experiência, manter conteúdo e controles importantes fora dessa área (a fala não dá um porquê além disso).
- Displacement ajusta o frame dos elementos existentes conforme o espaço disponível. O porquê: manter o conteúdo importante visível, alcançável e desobstruído, mesmo com o aparelho parcialmente dobrado.
- Escolher o escopo que combina com o conteúdo: um elemento que se adapta de forma independente se move sozinho; elementos que funcionam juntos se movem juntos. O porquê: preservar a relação entre eles.
- Cuidado com movimento excessivo. O porquê: afastar muito um elemento de sua origem enfraquece a relação visual entre os dois.
- Conteúdo de rolagem contínua (artigos, feeds, documentos e listas) não se desloca. O porquê: essas experiências já se adaptam pela rolagem, e movê-las entre as regiões pode interromper a continuidade.
- O propósito do conteúdo decide para onde ele vai, e esse lugar pode mudar conforme o aparelho é usado.
- Com o aparelho dobrado como livro, alertas vão para o lado trailing. O porquê: ficam mais perto de onde vão aparecer quando o aparelho fechar e a experiência continuar na tela externa.
- Com o aparelho apoiado na mesa, a região de cima serve para conteúdo que ganha com visibilidade à distância, e a de baixo para controles interativos. O porquê: o alerta continua fácil de encontrar em cima, e embaixo os elementos tocáveis têm uma superfície mais estável para o toque.
- Quando várias regiões servem, priorizar o contextual, como no iPhone a busca focada fica sobre o teclado (a fala dá o exemplo, não uma razão separada).
- Action sheets, alerts, menus e popovers são experiências contextuais leves que podem aparecer sobre uma reserved region; o objetivo principal é mantê-los totalmente visíveis, e o sistema os reposiciona automaticamente.
- O que todos os exemplos têm em comum é mover, redimensionar ou reorganizar o que já existe; manter conteúdo, funcionalidade e layouts disponíveis. O porquê: as pessoas devem ter acesso à experiência completa, seja qual for a forma como usam o iPhone Duo.
- Regiões inativas servem para decisões de alto nível sobre o app, como preferir número par de colunas em grids quando há uma division region, ativa ou não (a fala não dá o porquê).
- Ao escolher um arrangement, seguir primeiro os padrões que o app já usa. O porquê: HStack e VStack se traduzem naturalmente no split, e ZStack no overlay, com suporte embutido ao iPhone Duo.
- Sem padrão existente, usar overlay quando há relação clara de primeiro plano e fundo entre as views. O porquê, no exemplo dado: como o conteúdo de fundo pode ser rolado por cima do overlay, não há problema em ele ficar parcialmente encoberto às vezes.
- Usar split quando a relação é de principal e detalhe. O porquê: é importante que nenhuma das duas views fique encoberta.
- Não colocar contêineres de navegação, como Navigation Split View, dentro de uma arrangement view. O porquê: arrangement views não fornecem infraestrutura de navegação.
- Não colocar arrangement views dentro de List e Scroll View. O porquê dado é apenas a natureza dessas views roláveis.
- Layouts adaptativos devem mover, redimensionar e adaptar só quando isso torna a experiência melhor, para o app parecer pensado para cada pose.

Técnicas concretas de construção de interface, com números exatos quando falados:
- Números ditos: split 50/50 das colunas no Reminders; a division region da dobra, com o aparelho aberto e plano, fica inativa e com largura zero; arrangements fornecidos pelo sistema disponíveis no iOS 27.1; arrangement organiza duas views. A fala não dá valores de pontos, margens ou durações.
- Tela externa: câmera sempre presente; system toolbars e tab bars dispostas na vertical dentro da nova safe area (remete à sessão Raise the Bar with iPhone Duo).
- Deslocamento básico: um elemento centralizado com o aparelho aberto passa, ao dobrar, para a região que atende seu propósito.
- Menu de contexto: ao selecionar uma foto num álbum, em vez de centralizar o menu na região trailing, foto e menu se movem juntos e se alinham em volta da dobra.
- Busca: com o aparelho aberto, o campo aproveita o espaço extra; ao dobrar, largura e posição se adaptam para ficar sobre a view que está sendo buscada.
- Split view do sistema: mantém as duas colunas visíveis ajustando a largura e posicionando-as num split 50/50.
- Grid personalizado: preservar as margens externas e aumentar o espaçamento em volta da dobradiça, mantendo cada contêiner dentro de sua região, para que todos os itens do grid continuem interativos ao dobrar.
- Reserved regions em SwiftUI: consultar com um geometry proxy vindo de um geometry reader ou do "non-geometry change modifier" (termo incerto na transcrição automática), usando o novo método reserved region do geometry proxy para obter as regiões da view.
- Reserved regions em UIKit: método reserved region disponível em UIView.
- A propriedade frame de uma reserved region permite incorporá-la ao layout próprio.
- Estado: uma região pode estar ativa ou inativa; por padrão só as ativas são retornadas, e as inativas são obtidas com a opção de consulta include inactive do método reserved region.
- Division reserved region: representa a dobra, porque divide uma área maior em várias menores; só fica ativa quando o aparelho está dobrado.
- Occlusion region: não divide áreas, oclui; funciona como frames menores dentro dos bounds da view. A câmera FaceTime é uma occlusion region, consultada passando o tipo occlusion ao método reserved region; fica ativa quando a câmera está ativa.
- Componentes do sistema que se adaptam à dobra: contêineres de navegação como navigation stacks, navigation split views e "tap views" (termo incerto na transcrição automática); contêineres de conteúdo como List e Scroll View.
- Arrangements: contêineres de layout situados entre os de navegação e os de conteúdo, que organizam duas views segundo um conjunto de regras. As entradas consideradas são a size class horizontal e vertical, a proporção largura sobre altura e a presença de division regions ativas; as saídas são se a view aparece e, se aparece, qual o seu frame. Essa função de entradas para saídas é o arrangement.
- SwiftUI: adicionar uma arrangement view dentro do navigation stack, passando uma view primária e uma secundária.
- UIKit: usar UIArrangementViewController como root view controller do UINavigationController e configurar os view controllers primário e secundário.
- Estilo: configurado com o modificador arrangement view style; o padrão é split.
- Split arrangement: divide os bounds entre a view primária e a secundária; por padrão divide na horizontal quando a view é mais larga que alta e na vertical quando é mais alta que larga.
- Restringir eixos: método axes do split arrangement style. Se o split não pode dividir no eixo primário, a arrangement view mostra só uma view; no exemplo, com a view mais alta que larga e divisão só horizontal, aparece apenas o player.
- UIKit para o mesmo caso: método update arrangement do UIArrangementViewController com o tipo UI split arrangement configurado com eixo horizontal.
- Overlay arrangement: ao contrário do split, que prefere lado a lado, prefere posicionar o conteúdo uma view acima ou abaixo da outra; ao dobrar o aparelho, passa a preferir a primária e a secundária lado a lado.
- Z-index do overlay em SwiftUI: propriedade de ambiente overlay arrangement Z-index, que muda conforme o aparelho é dobrado e desdobrado; no exemplo, usada para alternar entre a versão recolhida e a expandida da view up next.
- Z-index do overlay em UIKit: método StateForViewPlacement do UIArrangementViewController e propriedade Z-index do estado retornado.

Exemplos citados:
- Controles de janela do iPadOS: exemplo de área a que os layouts já se adaptam, como devem ser tratadas as reserved regions.
- Livro com uma foto espalhada pelas duas páginas: mostra por que conteúdo que atravessa a dobra perde leitura.
- Álbum de fotos com menu de contexto: elementos que funcionam juntos se movem juntos e se alinham em volta da dobra.
- Alerta na pose de livro (lado trailing) e na pose apoiada na mesa (região de cima): o destino depende do uso do aparelho.
- Controles de mídia na região de baixo com o aparelho na mesa: controles tocáveis ganham superfície estável.
- Campo de busca no iPhone e no iPhone Duo: priorizar o contextual.
- Reminders: split view do sistema ajustado para 50/50.
- Design de fitness em grid: margens externas preservadas e espaçamento maior em volta da dobradiça.
- Grid com número par de colunas quando há division region: uso de regiões inativas para decisões de alto nível.
- App Podcasts no iPad e no iPhone Duo: a transcrição divide o layout ao meio; ao escondê-la no iPhone Duo dobrado, a view now playing não volta ao centro como no iPad e fica restrita à região esquerda definida pela dobra, mantendo os controles alcançáveis e desobstruídos; com o aparelho girado para retrato, não há split e a transcrição aparece inline. Também é o exemplo de relação principal e detalhe que pede split.
- App de notas de áudio do Harry, com player e up next: demonstra split com eixo restrito, overlay com estado recolhido e Z-index; a resposta final é split, porque a lista up next detalha o estado de reprodução em vez de ser fundo do player. Em um trecho a fala chama o app de "Audio Node app" (termo incerto na transcrição automática).
- Accessibility Reader: controles em primeiro plano e conteúdo legível ao fundo, caso de overlay.
- Sessões citadas: Raise the Bar with iPhone Duo e Leverage Multiple Displays and Scenes on iPhone Duo.

Citações:
"great design for iPhone Duo hinges on knowing when to adapt."
"Adaptive layouts help your app feel thoughtfully designed for every pose."

<!-- visual:tech-talks_111463 -->
### O que as imagens mostram
Base: 15 de 15 folhas de quadros vistas, todos os códigos conferidos.
- O mesmo app aparece em painel único com o aparelho achatado e em duas colunas alinhadas às metades físicas quando dobrado, com a dobradiça atuando como divisor do layout: Translate e Reminders (folha 0006, q0049 a q0053) e o app de podcast (folha 0010, q0082 a q0084). As imagens dão o antes e o depois tela a tela, enquanto a fala descreve o comportamento em termos gerais.
- Notes e o gravador de áudio já aparecem em duas colunas, sem par achatado equivalente nas notas: o Notes em um único quadro, com a tela renderizada sobre a curvatura da dobra (folha 0001, q0009), e o gravador com lista e forma de onda em dois quadros que diferem pelo ângulo da dobra e pelo contador de tempo, não pelo número de colunas (folha 0002, q0016 e q0017).
- Elementos flutuantes se reposicionam para a faixa da dobradiça em vez de ficarem centralizados: o diálogo "New Folder" do Música está no centro com a tela achatada (folha 0005, q0040), passa por um quadro de transição borrado (q0041) e reaparece sobre a dobra com o aparelho em dois ângulos diferentes (q0037, q0038). No mesmo intervalo, os controles de transporte do player de vídeo saem de sobre a imagem (q0043) e viram um grupo compacto na faixa da dobradiça, abaixo do vídeo (q0044).
- Anatomia de componentes registrada nas capturas: menu de contexto do Fotos como lista vertical com ícone à esquerda de cada ação e o item destrutivo em vermelho no fim (folha 0004, q0031); diálogo modal com campo de texto e dois botões lado a lado sobre fundo desfocado (q0036); grade de cartões do Reminders em 2 colunas por 3 linhas, com cor distinta por categoria, que ao dobrar se separa em cartões de um lado e lista do outro (folha 0006, q0052 e q0053).
- Uma grade que atravessa a dobra fica registrada sem rótulo de certo ou errado: a grade "Countries" do Fotos continua pelas duas metades, sem reposicionamento aparente do conteúdo (folha 0004, q0032 para q0033), no mesmo intervalo em que o card de título diz "Be mindful of excessive movement." (q0030).
- O código é construído linha a linha, com destaque azul temporário e selo circular verde "NEW": GeometryReader vazio, depois a consulta de regiões de divisão destacada com o selo, depois a mesma linha já sem destaque, depois uma segunda linha mapeando as regiões para frames (folha 0007, q0060 a q0063). A perda do destaque no quadro seguinte é o sinal visual de que a linha passou a fazer parte do código assentado.
- Duas variações da mesma chamada de API aparecem em sequência para tipos diferentes de região: a versão com o parâmetro de incluir regiões inativas (folha 0008, q0064) e a versão de oclusão (q0067), acompanhadas de um diagrama minimalista de tela com recorte em pílula no canto superior direito representando a câmera (q0069).
- O diagrama de contêineres do sistema se monta em camadas, uma por quadro: primeiro "Navigation Containers" com três ícones azuis nomeados, depois "Content Containers" com dois ícones vermelhos, depois "Layout Containers" em verde inserido entre as duas faixas anteriores, com selo NEW (folha 0009, q0073, q0078 e q0079). A cor codifica a família de contêiner, e cada ícone desenha o próprio componente, com barra na base para o de abas e duas colunas para o de split.
- O conceito abstrato de arrangement também é construído em três etapas de diagrama: caixa azul de entradas com um único botão, depois três botões de entrada ao lado de uma caixa verde de saídas vazia, depois a seta ligando entradas a saídas já preenchidas com visibilidade e frames (folha 0010, q0086 a q0088).
- Código e diagrama dividem a tela em duas colunas, e o diagrama muda mesmo quando o código não muda: as caixas de primária e secundária aparecem lado a lado, depois empilhadas sem alteração visível no código, depois o código ganha a restrição de eixo destacada, e por fim o diagrama passa a mostrar apenas a caixa primária, com o equivalente em UIKit destacado (folha 0011, q0094 a q0099).
- A troca de estilo é mostrada sobre o mesmo screenshot: split e depois overlay no app "Queue" sem mudança aparente na captura (folha 0012, q0101 e q0102), e em seguida a lógica de z-index e o enum de recolhido e expandido sendo montados no código enquanto o screenshot alterna entre só a barra do player e a lista completa com o player integrado no topo (q0103 a q0106).
- Rótulos didáticos ficam fora da moldura do aparelho, ao lado da área que identificam, anotando a mesma captura sem alterar a interface: "Foreground" e "Background" sobre a tela do Notes, com a barra de player realçada por um retângulo (folha 0013, q0114 e q0115), e "Player" e "Transcript" sobre a tela do podcast (q0116).
- Cards de título em texto branco sobre preto funcionam como índice paralelo à fala, com hierarquia por tamanho e peso: os dois padrões de adaptação (folha 0003, q0022), "Scope" (q0027), "Properties" (folha 0006, q0048), "Follow your existing app patterns." (folha 0013, q0110) e "Next steps" (folha 0014, q0125).
- A lista final de recomendações é construída item a item, mantendo os anteriores inalterados (folha 0014, q0126; folha 0015, q0127 e q0128), e o nome de API dentro dela é diferenciado do texto corrido por fonte monoespaçada com fundo destacado.
- Ilustrações abstratas sobre grade fina representam região reservada sem interface real: retângulo com um quadrado arredondado ao centro (folha 0003, q0026) e o retângulo com recorte de câmera já citado (folha 0008, q0069). Nessas duas folhas o resto dos quadros é card de título, bloco de código e plano dos apresentadores, sem captura de app real ao lado.
- O único still de produto mostra o aparelho fechado como um livro, visto de canto, corpo metálico claro, duas lentes empilhadas na quina externa e a hora 9:41 parcialmente visível na dobra (folha 0001, q0007).
Proporção visual: a maior parte dos quadros é tela, ou seja, captura de app, bloco de código, diagrama ou card de título, e a minoria é plano dos apresentadores em estúdio; há folhas inteiras sem nenhum apresentador em cena (folhas 0006 e 0011), e os planos humanos ficam mais densos na abertura e no fecho (folhas 0001, 0002, 0014 e 0015), sem desaparecer nas folhas do meio.
Divergências ou limites registrados: um quadro preto traz texto fantasma quase ilegível, lido com incerteza pelas notas (folha 0003, q0025); um bloco de código UIKit aparece com texto sobreposto e borrado, difícil de ler por completo (folha 0012, q0100); dois quadros mostram um retângulo cinza sem rótulo nem conteúdo, apontado nas notas como possível transição ou placeholder que não carregou (folha 0014, q0122 e q0123); e entre dois quadros da folha 0011 o diagrama muda de lado a lado para empilhado sem alteração visível no código.
<!-- /visual:tech-talks_111463 -->

## Meet Apple Watch Series 7 (id: tech-talks_10884, 15.2 min)

Base: transcrição e 10 de 10 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/tech-talks/10884/.

Tese central: o Apple Watch Series 7 ganhou áreas de conteúdo ativo maiores e um display com efeito de wraparound sutil nas bordas, e por isso os apps devem ficar maiores, mais claros e mais rápidos de entender num relance (larger, clearer, more glanceable).

O processo de design que a Apple descreve, apresentado por três designers (Deena Khattab, Jennifer Patton e Matthew Koonce): primeiro mapear as diferenças de hardware (dois novos tamanhos de case, curvatura do display, bezel mais fino, corner radius maior); a partir dessas diferenças, derivar três princípios de design; depois mostrar, com exemplos de apps do sistema e trechos de código SwiftUI, como aplicar cada princípio em margens, tipografia, cor, botões e teclado.

Princípios enunciados e o porquê: ampliar os componentes de UI para aproveitar a área de conteúdo maior, o que melhora a usabilidade; revisar tipografia e cor para criar hierarquia de informação mais clara; revisar navegação e wayfinding para reforçar o senso de lugar em um relance rápido, já que o Apple Watch sempre foi pensado para experiências leves e glanceable.

Técnicas concretas de construção de interface, com números exatos quando falados:
Layout: dois tamanhos de case, 41 mm e 45 mm; área de conteúdo ativo de 176 por 215 pontos no 41 mm e 198 por 242 pontos no 45 mm; por causa da curvatura maior nos cantos, o conteúdo precisa recuar para dentro; status bars mais altas, acompanhadas de uma margem de scroll clearance maior na base da tela; margens de layout generosas no Series 7. Na fala, o apresentador descreve o uso do modificador .scenePadding em SwiftUI para aplicar a margem padrão do sistema, recomendado só para conteúdo de texto que seria distorcido ou cortado nas bordas (como o preço atual de uma ação e o texto "Nasdaq" no exemplo do app Stocks); um gráfico (chart) do mesmo layout foi deixado sem esse modificador, porque pode ir até a borda da tela.
Hierarquia e navegação: large titles chegaram ao watchOS neste ano; em table views com scroll, o título grande transiciona para a status bar durante o scroll; tanto o nível raiz quanto subviews recebem o título grande; em views fixas que não rolam, o título pode ser trazido para dentro da área de conteúdo (caso Timer) ou removido quando desnecessário, desvinculando o título da navegação por botão Back; em outras views fixas, a status bar continua sendo o melhor lugar para o título (caso World Clock detail). Em SwiftUI, por padrão no watchOS 8 todos os títulos de navegação são grandes e tingidos pela accent color do app; o modificador .navigationBarTitleDisplayMode desativa o título grande numa view específica, e views subsequentes na hierarquia herdam esse modo.
Cor: a cor deve ajudar na wayfinding, na hierarquia de informação e sinalizar a personalidade do app. A accent color é configurada no asset catalog e passa a colorir automaticamente as navigation bars; no exemplo do Mail, o listItemTint foi definido como a accent color do app a 30 por cento de opacidade.
Botões: sistema de botões retangulares arredondados para views com scroll e botões pinned (fixados na base) para views fixas; no Series 7 o esquema de cor do botão secundário foi simplificado e botões lado a lado passaram de uma forma de lozenge dividido para pill shapes lado a lado; a forma do botão pinned foi desenhada a partir da curvatura do próprio display, para harmonizar com o hardware; a altura dos botões permanece igual em dispositivos anteriores ao Series 7, então nenhuma mudança de layout é necessária para adotá-los. Em SwiftUI, botões usam por padrão um bordered button style com automatic border shape: forma de capsule fora de uma scroll view e rounded rectangle dentro dela; existe também o estilo bordered prominent, que aplica a accent color ao botão (usado em Alarms).
Tipografia: Series 7 usa os mesmos tamanhos de tipo padrão do Series 6, large para 40 mm e 41 mm, extra large para 44 mm e 45 mm, ganhando mais caracteres por linha que dispositivos anteriores; três tamanhos de tipo maiores foram adicionados para acessibilidade, chamados AX1, AX2 e AX3; um recurso de Smart Type Suggestions no setup identifica se a pessoa já usa tipo grande no iPhone e sugere um tamanho equivalente no watch.
Símbolos e escrita: recomenda-se complementar rótulos de texto com SF Symbols; em apps de navegação por lista, usar símbolos outlined na accent color do app, alinhando estilo e cor de símbolo entre plataformas por consistência e acessibilidade (exemplos: Mail, Phone).
Interação e teclado: por causa da área de tela maior, foi adicionado um teclado completo, desenhado sem bordas ao redor das teclas, para incentivar o swipe to type e evitar a sensação de que é fácil errar o toque; a tecla de apagar foi tirada de dentro do teclado e movida para o campo de texto, liberando espaço; o teclado permite customizar o tipo de autofill para casos como senhas e autenticação de dois fatores; os acessórios à esquerda e à direita de campos de texto podem ser customizados com SF Symbols, recomendando-se a accent color do app para reforçar que são tocáveis.

Exemplos citados: Stocks ensina o uso do .scenePadding para texto perto da borda; Settings ilustra large titles em nível raiz e em subviews; Timer mostra o título trazido para a área de conteúdo; World Clock detail mostra um caso em que o título permanece na status bar; Mindfulness ensina o uso de System Teal como cor-chave do app com o System Gray recuado; Mail mostra fundo azul reforçando identidade de app e o listItemTint a 30 por cento; Tips usa platters amarelo brilhante para se diferenciar de outros apps de navegação por carrossel, como Workout, e reforçar a continuidade da experiência entre plataformas; Alarms list mostra um botão scrolling primário e o estilo bordered prominent; UIPickerView mostra botões lado a lado em pill shape.

Citações: "apps for Apple Watch Series 7 should be larger, clearer, and more glanceable" e "deriving the shape of the button from the shape of the display itself".

<!-- visual:tech-talks_10884 -->
### O que as imagens mostram
Base: 10 de 10 folhas de quadros vistas, todos os códigos conferidos.
- As medidas em pontos aparecem escritas ao lado dos próprios renders de hardware, não só ditas: o par de caixas pretas traz a cota de 41 mm (folha 0001, q0004) e o render seguinte, de várias caixas coloridas sobrepostas, traz as cotas de 41 mm e de 45 mm ao mesmo tempo (q0005).
- Uma anotação aponta o defeito de layout diretamente sobre a tela: o rótulo "Too close to edge" com uma linha vertical apontando a borda esquerda, ao lado do preço da ação, entre um quadro sem rótulo antes e outro sem rótulo depois (folha 0003, q0019 a q0021).
- A correção é mostrada como relação de causa e efeito: painel de código ao lado do relógio renderizado, com a linha do modificador de margem inserida e destacada primeiro sob o bloco do preço, depois após o texto do rodapé, e uma seta laranja ligando o trecho de código ao elemento correspondente na tela (folha 0003, q0022 a q0026). O relógio troca de lado entre os quadros, e o gráfico do mesmo layout também aparece destacado no código, coerente com o tratamento diferente que a fala dá a ele.
- O par de estados de título é exibido lado a lado com o código: o comentário muda de títulos grandes para títulos inline, a linha do modificador de modo de exibição fica destacada, e a tela do relógio passa de título grande em laranja ocupando o topo para título pequeno alinhado à esquerda ao lado da seta de voltar (folha 0004, q0034 a q0036).
- Cor de identidade por app é demonstrada por acúmulo de relógios em cena, um por vez: primeiro o Mindfulness em verde-água, depois o Mail em azul ao lado, depois o Tips com cartão amarelo (folha 0005, q0038 a q0041), deixando a diferença visível por comparação direta em vez de descrição.
- A ferramenta de autoria entra em quadro: a tela de um laptop mostra o editor de cor de destaque e depois o navegador de arquivos do projeto, antes de a cena voltar para o painel de código com a linha de tingimento de item de lista destacada por uma caixa (folha 0005, q0042 a q0045).
- O sistema de botões é apresentado como diagrama de duas colunas nomeadas, separando botões de views com rolagem de botões de views fixas, com código de cor por hierarquia, verde para ação primária, cinza para secundária e dismiss, azul para toolbar; o mesmo diagrama reaparece com o título trocado de botões atuais para botões do Series 7, mantendo estrutura e cores (folha 0006, q0046 a q0050).
- Os botões fixados na base aparecem em formato de pílula lado a lado, um cinza de cancelar e um verde de iniciar, e a cena aproxima a base da tela, onde as rodas numéricas seguem parcialmente visíveis acima dos botões (folha 0006, q0051 a q0054).
- Os modificadores de estilo de botão são destacados um a um junto ao render: forma automática com estilo bordered nos botões de cancelar e iniciar, e estilo bordered prominent no botão laranja de adicionar alarme, cada caso seguido de um recorte aproximado da tela sobre o próprio botão (folha 0007, q0059 a q0063). A cor do botão segue a função, com vermelho para parar, laranja para adicionar e verde para iniciar (folha 0007).
- A diferença de espaço para texto entre tamanhos de caixa é mostrada por dois relógios com a mesma mensagem de e-mail e rótulos de tamanho anotados sob cada um, seguida de um close no maior com o corpo da mensagem aberto (folha 0008, q0065 e q0066).
- O ajuste de tamanho de tipo aparece na tela do iPhone, com controle deslizante entre um "A" pequeno e um "A" grande e botão de continuar, e no quadro seguinte o relógio surge ao lado já exibindo o texto no tamanho escolhido (folha 0008, q0068 e q0069).
- A consistência entre plataformas é composta literalmente: iPad, iPhone e relógio lado a lado exibindo a mesma tela de caixas de correio, com os mesmos ícones de pasta, estrela e bandeira nas três larguras (folha 0008, q0072).
- O teclado é desenhado sem contornos ao redor das teclas, e o ícone de apagar fica dentro do campo de texto e não entre as teclas; um ícone de chave no canto do campo sinaliza contexto de senha ou autenticação (folha 0009, q0074 a q0076).
- Uma caixa amarela de destaque circunda apenas a palavra do campo de busca, chamando atenção para um detalhe de escrita sem alterar a interface (folha 0009, q0079), e o cartão de encerramento aparece primeiro com dois recursos listados (q0081) e depois com três, mais um separador fino acima de dois links de referência (folha 0010, q0082).
- A lista de princípios de design funciona como marcador de capítulo e reaparece ao longo do vídeo: primeiro inteira, sobre dois relógios apagados (folha 0001, q0008), depois com o item da seção atual em negrito e os demais apagados (folha 0008, q0064; folha 0009, q0073), uma pista de estrutura que a fala não verbaliza a cada corte.
Proporção visual: as notas não registram nenhum quadro de apresentador em cena; os 82 quadros são telas de relógio, renders de hardware, diagramas, painéis de código e cards de texto, com o painel de código ao lado do render aparecendo em quatro folhas distintas.
Divergências ou limites registrados: dois quadros do Mindfulness aparecem idênticos, sem diferença perceptível (folha 0005, q0038 e q0039); os três quadros de close nos botões de cancelar e iniciar também são indistinguíveis nessa resolução, e as notas anotam que a diferença sutil descrita na fala entre pílula simples e forma lapidada não é visível nas imagens estáticas (folha 0006, q0052 a q0054); e dois quadros da tela de caixas de correio não apresentam diferença perceptível (folha 0008, q0070 e q0071).
<!-- /visual:tech-talks_10884 -->

## Designing for Apple Watch Series 4 (id: tech-talks_802, 9.4 min)

Base: transcrição e 7 de 7 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/tech-talks/802/.

Tese central: o Apple Watch Series 4 traz displays maiores com cantos arredondados e bordas mais finas, e a Apple orienta a atualizar layouts para usar margens e safe areas do sistema em vez de valores fixos, para que o app se beneficie do espaço extra sem cortar conteúdo.

O processo de design que a Apple descreve: comparar as novas dimensões de case e de display com as anteriores, situar os novos tamanhos (40 mm e 44 mm) dentro do espectro de tamanhos já existente, recomendar o uso dos Design Resources para criar mockups fiéis por tamanho de watch, e então explicar como o WatchKit adapta automaticamente status bar, título, margens e scroll clear areas ao novo formato de tela.

Princípios enunciados e o porquê: entregar a mesma informação e as mesmas ações independentemente do tamanho de tela, porque os quatro tamanhos de case coexistem; projetar o layout mirando as dimensões do meio do espectro (40 e 42 mm) e garantir que escale para baixo (38 mm) e para cima (44 mm); estender elementos gráficos e fundos de botão quase de ponta a ponta, mas manter o texto alinhado à margem, para acompanhar a curvatura dos novos cantos sem cortar conteúdo textual.

Técnicas concretas de construção de interface, com números exatos quando falados:
Tamanhos de case: novos 40 mm e 44 mm, contra os anteriores 38 mm e 42 mm. Dimensões de display: 38 mm anterior, 272 por 340 pixels; 42 mm anterior, 312 por 390 pixels; novo 40 mm, 324 por 394 pixels; novo 44 mm, 368 por 448 pixels. O novo display de 40 mm é 12 pixels mais largo e 4 pixels mais alto que o display do antigo 42 mm.
Layout: status bar e title area ficam indentados, criando margens esquerda e direita que se estendem verticalmente pelo conteúdo, chamadas de System Minimum Layout Margins; elementos gráficos e fundos de botão devem se estender além dessas margens, quase de ponta a ponta, até uma margem padrão de 1 pixel de cada lado; o texto deve se alinhar à margem esquerda, a partir da borda esquerda do texto na status bar. Em scroll views existem scroll clear areas no topo e na base do conteúdo, que empurram texto e botões para dentro da área visível ao fim de um scroll; para views de tela única que não devem rolar, o Xcode oferece o atributo Fixed to screen edges no attribute inspector.
Compatibilidade: um app não recompilado roda no Series 4 nas dimensões de 38 mm (em watch de 40 mm) ou 42 mm (em watch de 44 mm), centralizado na tela; recompilando para watchOS 5, o app passa a ocupar toda a largura e altura do novo display, desde que os elementos do WatchKit estejam implementados de forma relativa ao container, e não em larguras fixas.
Háptica: o Digital Crown do Series 4 introduz novos haptics, com detents (toques) produzidos por padrão a cada rotação, entregando feedback tátil em interações comuns como rolar uma lista ou selecionar um item num picker; recomenda-se avaliar se eventos de UI ligados à rotação do Digital Crown continuam alinhados a esse novo feedback tátil.
Tipografia: watchOS 5 expandiu a Dynamic Type Library com quatro tamanhos maiores, Large Title e Titles 1, 2 e 3; a categoria de conteúdo padrão varia por tamanho de case, Small para 38 mm, Large para 40 mm e 42 mm, XLarge para 44 mm.
Assets visuais: recomenda-se produzir gráficos como PDFs com fator de escala 2, colocados na caixa Universal 2x do asset catalog, com a propriedade Auto Scaling ajustada para Automatic; isso escala os gráficos 9 por cento para baixo em displays de 38 mm e 10 por cento para cima em displays de 44 mm; dois novos tamanhos de ícone de app foram introduzidos para cobrir a interface do 44 mm (short look notification e ícone de Home screen).

Exemplos citados: nenhum app de terceiros é citado; o vídeo usa apenas elementos genéricos do sistema (status bar, title area, scroll views, SpriteKit/SceneKit) como exemplo de adaptação ao novo display.

Citações: "Series 4 watches have new displays with larger dimensions" e "the border around it is thinner, bringing more attention to interactive elements".

<!-- visual:tech-talks_802 -->
### O que as imagens mostram
Base: 7 de 7 folhas de quadros vistas, todos os códigos conferidos.
- A comparação de tamanhos de tela é feita por retângulos cotados em pixels, alternando entre representação abstrata e aplicada: pares de relógio com tela verde lisa sem cota, depois retângulos com as resoluções dos dois tamanhos antigos, depois os novos, depois telas reais de app, e por fim os quatro tamanhos lado a lado sob o rótulo da geração nova (folha 0001, q0004 a q0009).
- O mockup de relógio físico, com caixa e pulseira, serve de moldura recorrente, e a área de conteúdo aparece preenchida em verde sólido como placeholder sempre que o ponto é o espaço disponível e não o conteúdo (folha 0001, q0004 e q0005; folha 0004, q0030 e q0031).
- A estrutura de tela do watchOS é montada progressivamente em zonas coloridas sobre um layout de exemplo: tela preta vazia, depois a barra de título azul com título e relógio, depois a faixa cinza de margem, depois a faixa roxa de área de liberação de rolagem na base, depois o bloco de texto de preenchimento com botão abaixo, e por fim um stepper numérico com botão azul, já sem as faixas de cor (folha 0003, q0019 a q0027). As cores por zona são recurso exclusivo da tela, a fala nomeia as zonas sem descrevê-las assim.
- A ferramenta de configuração entra em quadro no ponto exato da opção: o inspetor de atributos do Xcode com o atributo de fixar a view às bordas da tela marcado, ao lado do relógio com o mesmo stepper e botão da folha anterior (folha 0004, q0028), e depois o mesmo quadro com o card de transição sobreposto (q0029).
- Contorno tracejado interno demarca margem e recuo dentro da área de tela, e wireframes com placeholder de imagem em "X" mais texto de preenchimento representam a estrutura antes do conteúdo final (folha 0004, q0030 a q0033).
- A escala tipográfica aparece como tabela completa em grade, cruzando categoria de tamanho de conteúdo nas colunas com estilo de texto nas linhas e valor em pontos em cada célula, construída em duas etapas: primeiro os estilos menores, depois os quatro estilos maiores acrescentados acima (folha 0005, q0042 a q0044). A fala cita os estilos novos, a imagem entrega todos os valores numéricos.
- A tela de sistema de ajuste de tamanho de texto, com controle deslizante entre "Aa" pequeno e grande e uma frase de exemplo, aparece sobreposta à tabela já desfocada ao fundo, ligando a especificação ao controle que a pessoa usa (folha 0005, q0045).
- O material de apoio da própria Apple é mostrado em tela: a página das diretrizes no Mac com três colunas por faixa de tamanho de relógio (folha 0002, q0013) e um arquivo de template aberto em app de design, com painel de elementos de interface por tamanho, lista de componentes e uma paleta com um botão cinza de cancelar mais o mesmo botão de confirmação repetido em sete cores, além do painel de propriedades com posição, transformação, bordas, preenchimentos e sombras (q0014 e q0015).
- O fluxo de produção de asset é mostrado dentro do Asset Catalog do Xcode, com o ícone do projeto nas caixas universais e o painel de atributos exibindo largura de tela qualquer e escala automática, primeiro em contexto e depois em close (folha 0006, q0049 a q0052).
- A especificação de ícone traz medidas exatas em pixels e pontos para dois contextos, notificação e tela de início, ilustradas por círculos concêntricos (folha 0006, q0053), e a mesma especificação reaparece sobreposta a uma página das diretrizes na mesma folha.
- Cards de texto branco isolado marcam a estrutura da apresentação entre os blocos visuais, incluindo o título de layout (folha 0002), o de atualização do app (folha 0004), os de retorno tátil e de views roláveis (folha 0005) e o de produção gráfica, além da instrução de preparar o gráfico em escala 2x e salvar como PDF (folha 0006).
- O encerramento mostra a página de recursos do site Apple Developer, com vídeo incorporado e lista de documentação, antes do slide final preto com o logotipo e o aviso de direitos autorais de 2018 (folha 0007, q0055 a q0057).
Proporção visual: as notas não registram nenhum quadro de apresentador em cena; o vídeo inteiro é composto de mockups de relógio, retângulos cotados, capturas do Xcode e de apps do sistema, tabelas, wireframes e cards de texto.
Divergências ou limites registrados: na enumeração das resoluções da folha 0001 as notas registram a cota em pixels dos tamanhos de 38, 42 e 40 mm, mas o de 44 mm aparece rotulado sem número lido no quadro; e entre dois quadros do editor de design a única diferença registrada é a posição do cursor ou da seleção (folha 0002, q0014 e q0015).
<!-- /visual:tech-talks_802 -->

## Designing for Subscription Success (id: tech-talks_803, 9.2 min)

Base: transcrição e 6 de 6 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/tech-talks/803/.

Tese central: uma boa experiência de assinatura precisa ser sem esforço, transparente e envolvente (effortless, transparent, engaging), porque a percepção comum é de que assinar é complicado, confuso e demorado.

O processo de design que a Apple descreve: trabalhar cada um dos três princípios separadamente. Para ser effortless, tornar a oferta visível sem parecer um anúncio descartável e sempre disponibilizar a opção de assinar em Settings ou Account, além de remover fricção reduzindo o número de passos e adiando pedidos de personalização para depois do cadastro. Para ser transparent, montar uma tela única e glanceable com proposta de valor, call to action, login, restauração de compra, termos e múltiplos tiers de preço, seguindo as App Review guidelines. Para ser engaging, deixar a pessoa experimentar o app antes de decidir, por meio de free trial, liberação da maior parte do app com um recurso premium reservado, ou amostragem de conteúdo.

Princípios enunciados e o porquê: ser visível, porque as pessoas não devem precisar procurar como assinar; não apresentar a assinatura como pop-up ou notificação, porque esses formatos são feitos para serem dispensados e a assinatura não deveria ser; remover fricção, porque cada passo extra reduz a taxa de conversão, segundo dado do próprio vídeo; ser glanceable, porque a maioria das pessoas decide assinar pelo celular, em poucos segundos; oferecer múltiplos tiers, porque diferentes pessoas querem se comprometer por períodos diferentes (dia, semana, mês, dois anos); deixar experimentar antes de comprar, pela mesma lógica de provar uma roupa, visitar uma casa aberta ou fazer test drive de um carro antes de decidir.

Técnicas concretas, com números exatos quando falados: dado de um mês de uso dos três maiores apps de streaming de entretenimento dos Estados Unidos (nomes removidos na fala) mostra que um fluxo de assinatura com três cliques teve taxa de conversão de 61 por cento; com quatro cliques, a conversão caiu para 48 por cento; com nove cliques, a conversão caiu para 7 por cento.

Exemplos citados: New York Times, que mantém um botão de assinatura persistente, porém discreto, em todos os artigos, e que oferece 10 artigos grátis por mês para não assinantes, deixando a própria pessoa escolher o que ler como amostra; HER, app de namoro, que oferece a assinatura no momento em que a pessoa tenta usar o recurso de rewind (desfazer um "passar" acidental), com uma animação leve mostrando os valores da oferta justamente quando há interesse manifesto; MLB At Bat, citado como exemplo de tela glanceable que reúne proposta de valor, call to action, login, restauração de compra e termos claros numa única visão; Sleep Cycle, que libera a maior parte dos recursos de graça e reserva o recurso Trends, mostrado com um efeito de blur, como amostra do que o assinante passaria a ver.

Citações: "make your subscription effortless, transparent, and engaging" e "less clicks, less friction, will equal more conversion and more subscribers".

<!-- visual:tech-talks_803 -->
### O que as imagens mostram
Base: 6 de 6 folhas de quadros vistas, todos os códigos conferidos.
- A lista dos três princípios funciona como trilha de progresso ao longo do vídeo, com o item em foco em branco e negrito e os demais esmaecidos em cinza, reaparecendo a cada virada de seção e terminando com os três em branco, sem hierarquia, para sinalizar o fecho (folha 0001, q0005 e q0006; folha 0003, q0027; folha 0004, sem número de quadro nas notas; folha 0006, q0052). A fala não verbaliza esse marcador.
- Emoji grande e isolado ilustra conceito abstrato, sempre entre um slide de texto e a captura de app seguinte: o rosto com a mão sobre fundo roxo para a frustração de assinar, ao lado da frase de reação (folha 0001, q0004), vestido, casa e carro em duas colunas para as analogias de experimentar antes de decidir (folha 0005, q0039) e um grupo de pessoas para representar o público (folha 0006, q0051).
- O exemplo do app de notícias mostra o botão azul de assinar fixo no topo de cada tela de artigo, primeiro em uma tela e depois em três lado a lado (folha 0001, q0008 e q0009), e as mesmas três telas reaparecem com as duas negações sobrepostas, separando assinatura de anúncio e de notificação, antes de o texto ficar sozinho em quadro (folha 0002, sem número de quadro nas notas).
- A anatomia do modal de oferta aparece completa numa captura real: cartão sobreposto ao conteúdo com fundo escurecido, foto de perfil pertinente ao contexto, indicadores de página em pontos, três opções de preço com a mais longa destacada em cor sólida e selo de desconto, e o link de restaurar compra em texto discreto abaixo (folha 0002, q0014).
- O mesmo cartão reaparece com o título e a foto trocados, mantendo estrutura, hierarquia e posições idênticas, o que mostra o modal como gabarito reutilizável e não como tela única (folha 0002, q0014 para q0015).
- A alternativa permanente de assinatura é mostrada dentro da tela de configurações do app, com o item de assinar listado entre opções de conta e um item de restaurar assinatura logo próximo, em duas capturas lado a lado que fecham uma folha e abrem a seguinte (folha 0002, sem número de quadro nas notas; folha 0003, q0019 e q0020).
- O dado de conversão vira gráfico de barras duplo com rótulo numérico acima de cada barra e legenda de cor por métrica, cliques exigidos em azul claro contra taxa de conversão em amarelo, reaproveitado em três enquadramentos sem mudança de dado e depois escurecido para servir de fundo à frase de conclusão (folha 0003, q0022 a q0025).
- A tela de oferta de um app de beisebol é anotada com callouts de seta, um por quadro, apontando primeiro o restaurar compra, depois os múltiplos níveis de preço, depois os termos e condições (folha 0004, q0031 a q0033), técnica de anotação direta sobre captura real.
- Em seguida, o checklist completo de oito elementos obrigatórios de uma tela de assinatura aparece em coluna ao lado da mesma captura, transformando os callouts pontuais em lista fechada (folha 0004, q0034).
- A própria captura mostra a anatomia da tela única de oferta: título, proposta de valor em uma frase, link de recursos da assinatura, dois botões de preço, botão de login do assinante, texto legal de cancelamento com links de termos e, no rodapé, a linha de restauração de compra (folha 0004, q0029 e q0030).
- A hierarquia de botões empilhados aparece na tela de onboarding de um serviço de streaming: ação primária em azul sólido no topo, entrar e restaurar compra abaixo como ações secundárias, sobre fundo de capas de séries (folha 0005, q0042).
- O recurso premium bloqueado é mostrado como imagem, não como descrição: o gráfico de tendências de um app de sono aparece borrado atrás do aviso de conteúdo exclusivo de assinantes, com a nota no rodapé (folha 0005, q0044 e q0045).
- O mecanismo de amostra gratuita aparece como componente de aviso no topo da tela de artigo, informando quantos artigos gratuitos restam no mês, em uma matéria com foto de abertura (folha 0006, q0046).
- Esmaecimento e foco conduzem a leitura entre slide e captura: as telas de configurações ficam desfocadas atrás do texto sobre remover fricção (folha 0003, q0021), e a lista mais a captura esmaecem antes da frase de simplificação sobrepor a tela com um ícone de grade de apps (folha 0004, q0035 e q0036).
- Saudações curtas no canto marcam a mudança de destinatário de cada seção, dirigidas ao público em geral, aos assinantes e aos advogados (folhas 0001, 0003, 0004 e 0005).
Proporção visual: as notas não registram nenhum quadro de apresentador em cena; todos os quadros são slides de texto, emojis, gráficos ou capturas de apps reais, com a abertura em slide de título com crédito do apresentador e o encerramento em card preto com o logotipo da Apple e o aviso de direitos autorais.
Divergências ou limites registrados: na folha 0001 as notas identificam o app de notícias com ressalva, como estilo New York Times, e só na folha 0006 registram o nome sem ressalva; os três quadros do gráfico de barras diferem apenas por enquadramento de câmera, sem mudança de dado (folha 0003, q0022 a q0024); e os dois quadros finais do gráfico de tendências têm composição e câmera praticamente iguais (folha 0005, q0044 e q0045).
<!-- /visual:tech-talks_803 -->

## Designing for iPhone X (id: tech-talks_801, 12.8 min)

Base: transcrição e 9 de 9 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/tech-talks/801/.

Tese central: o display Super Retina do iPhone X, com cantos arredondados, sensor housing e Home indicator, exige que os apps usem o Safe Area layout guide e os layout margins do UIKit e do Auto Layout para preencher a tela toda sem cortar ou esconder controles e informação crítica.

O processo de design que a Apple descreve: primeiro revisar a escala e as dimensões do novo display; em seguida mostrar como componentes padrão do UIKit (navigation bars, table views, tab bars, toolbars) se adaptam automaticamente; depois apresentar o Safe Area layout guide como novidade do iOS 11 e explicar sua diferença em relação ao iPhone 8; por fim, orientar sobre os ajustes manuais necessários em apps com controles customizados, em orientação landscape, na status bar e no comportamento do Home indicator.

Princípios enunciados e o porquê: o app ou jogo deve sempre preencher o display em que roda, porque barras pretas no topo ou na base fazem o app parecer pequeno e inconsistente com os demais apps do iPhone X; qualquer elemento perto demais das bordas ou cantos do viewport pode ser cortado pelos cantos arredondados ou coberto pelo sensor housing, por isso controles e informação crítica precisam ser recuados; em landscape, controles e informação centralizados funcionam melhor, porque layouts assimétricos que mudam de posição conforme a rotação do aparelho prejudicam a memória muscular e geram inconsistência; o Home indicator precisa estar sempre claramente visível, e por isso o iOS ajusta dinamicamente a aparência dele (escuro sobre fundos claros, claro sobre fundos escuros) e não deve receber adornos visuais como brackets ou bezels que chamem atenção demais para ele; recursos como edge protection e auto-hide do indicador levam a uma experiência menos consistente e devem ser usados só quando absolutamente necessários.

Técnicas concretas de construção de interface, com números exatos quando falados:
Escala e assets: o display do iPhone X tem fator de escala de imagem 3x; a recomendação é usar PDFs, por serem independentes de resolução e reduzirem o tamanho do app, e quando forem necessárias imagens rasterizadas, incluir as resoluções 2x e 3x no asset catalog.
Dimensões: o display mede 375 pontos de largura por 812 pontos de altura, equivalendo a 1125 por 2436 pixels num display 3x; os 375 pontos de largura são iguais à largura dos displays de 4,7 polegadas do iPhone 6, 7 e 8, então não há diferença na quantidade de informação na dimensão mais estreita; os 812 pontos de altura são 145 pontos a mais que um display de 4,7 polegadas, dando cerca de 20 por cento a mais de espaço para conteúdo.
Safe Area e layout margins: no iPhone 8, sem barras visíveis, a Safe Area tem o mesmo tamanho do viewport; com status bar visível, a borda superior da Safe Area desce para acomodá-la, e ela é recuada ainda mais para acomodar navigation bar e toolbar ou tab bar. No iPhone X, a Safe Area já vem recuada do topo e da base mesmo sem nenhuma barra visível em portrait, para proteger conteúdo do sensor housing, dos cantos arredondados e do Home indicator; em landscape, ela é recuada das laterais e do Home indicator pela mesma razão. Layout margins, um guide separado dentro da Safe Area, mantêm margens de conteúdo consistentes entre apps e ajudam a alinhar conteúdo a controles como botões da navigation bar. UIView expõe os valores de Safe Area insets e layout margin como propriedades, mesmo para quem não usa Auto Layout. iPhone 6, 7, 8 e X pertencem todos à mesma size class de largura compacta (compact width), então o layout de um app deve ser consistente entre esses aparelhos.
Aspect ratio: fundos desenhados para o aspect ratio 16:9 do iPhone 8 aparecem cortados nas laterais no iPhone X se escalados para preencher, ou com letterbox se escalados para caber; o inverso ocorre com fundos desenhados para iPhone X exibidos em iPhone 8, cortados no topo e na base ou com pillarbox; a recomendação é compor imagens de modo que a informação visual crítica permaneça visível em qualquer aspect ratio.
Status bar e Home indicator: a status bar é mais alta no iPhone X e não muda mais de altura durante tarefas em segundo plano, como uma chamada ou rastreamento de localização, para manter uma experiência mais consistente; recomenda-se deixar espaço negativo ao redor do Home indicator, mantendo todo conteúdo não rolável dentro da Safe Area; a edge protection, quando ativada na borda inferior, exige dois swipes para sair do app, o primeiro levanta o indicador e habilita o controle, o segundo efetivamente sai; o auto-hide faz o indicador esmaecer se a tela não for tocada por alguns segundos e reaparecer ao toque, recomendado só para experiências passivas com toque pouco frequente; views roláveis verticalmente, como tabelas e collection views, devem se estender até a base do display, e não ficar restritas pela Safe Area.

Exemplos citados: nenhum app de terceiros é citado; os exemplos são os próprios componentes padrão do UIKit (navigation bars, table views, tab bars, toolbars) e cenas em tela cheia via SpriteKit ou SceneKit, usados para ilustrar adaptação automática e manual ao novo display.

Citações: "iPhone X's super retina display gives you more space to display content" e "Because edge protection leads to an inconsistent user experience".

<!-- visual:tech-talks_801 -->
### O que as imagens mostram
Base: 9 de 9 folhas de quadros vistas, todos os códigos conferidos.
- O fator de escala de imagem vira diagrama de três círculos de tamanho crescente, com rótulos abaixo e associação a cada aparelho, primeiro junto ao título e depois isolado em composição própria e maior (folha 0001, q0003 e q0004). A fala só menciona a escala verbalmente.
- As medidas aparecem como anotação gráfica sobre os contornos, com linhas, setas e números em azul claro, e o mesmo par de blocos de comparação troca a unidade entre quadros, primeiro em pixels de largura e altura, depois em pontos de largura iguais nos dois aparelhos (folha 0001, q0008 para q0009).
- A altura extra é isolada visualmente em vez de apenas somada: o bloco do aparelho novo aparece com a faixa adicional destacada em verde no topo, separada da parte azul compartilhada com o display menor, com as três cotas anotadas (folha 0002, q0010).
- O indicador de início ganha destaque por sobreposição, com uma barra amarela surgindo na base de um contorno que nos quadros anteriores estava vazio (folha 0002, q0012 para q0013).
- Blocos verdes sólidos rotulados como área segura funcionam como camada de anotação reaproveitada em contextos diferentes: preenchendo quase toda a tela num aparelho sem entalhe, recuado abaixo da barra de navegação numa captura real de app de e-mail, e recuado do topo e da base no aparelho novo mesmo sem nenhuma barra visível (folha 0003, q0024 a q0027).
- Capturas do mesmo app são empilhadas com transparência e alinhadas para comparar tamanhos: a lista de favoritos em três camadas, depois a mesma sobreposição com contornos de aparelho em zoom maior, e a barra de abas de cinco ícones comparada em quatro camadas alinhadas (folha 0002, q0017 e q0018; folha 0003, q0020).
- Duas camadas de cor separam barra e conteúdo no formulário em paisagem: a barra de navegação vermelha passa de inserida para estendida de ponta a ponta entre dois quadros, enquanto as linhas de conteúdo destacadas em verde permanecem recuadas, tornando visível que uma regra vale para a barra e outra para a célula (folha 0004, q0029 para q0030).
- Uma faixa azul clara marca o recuo lateral na borda esquerda dos dois aparelhos comparados, e o rótulo da classe de tamanho identifica que ambos pertencem à mesma largura compacta (folha 0004, q0033 a q0036).
- O par de marcas de errado e certo, círculo vermelho com "X" e círculo verde com "check", aparece pelo menos seis vezes no mesmo formato de círculo colorido com ícone branco: na rotação de retrato para paisagem e na comparação entre os dois displays (folha 0005, q0037 e q0038), nos ícones colados aos quatro cantos marcados como errado contra os mesmos ícones recuados marcados como certo (folha 0005, q0045; folha 0006, q0046 e q0047), na barra de rolagem e na tela de clima coladas às bordas marcadas como erradas (folha 0007, q0056 e q0057) e no botão centralizado dentro da área segura contra a barra fina colada à borda inferior (folha 0007, q0061 e q0062).
- O corte e a tarja de uma imagem de fundo são demonstrados com dois blocos azuis ilustrando uma árvore, com seta indicando a direção da adaptação entre os dois aparelhos e contorno branco marcando a área que seria cortada; no quadro seguinte a seta inverte e o recorte muda de bloco, mostrando os dois sentidos do mesmo problema (folha 0005, q0039 a q0043).
- Três estados rotulados com o mesmo nome de comportamento mostram o indicador de início como linha branca fina, depois com um círculo azul sobre ele sugerindo o toque, depois de volta à linha simples, ilustrando um gesto que a fala descreve apenas em texto corrido (folha 0008, q0065 a q0067).
- O caso de tela cheia aparece como par: o vídeo ocupando toda a tela com o indicador sutil na base e, no quadro seguinte, o mesmo vídeo com barra de título com data e controles de reprodução sobrepostos (folha 0008, q0070 para q0071).
- A anatomia das listas padrão é registrada e repetida entre tamanhos: favoritos com avatar circular, nome em negrito, tipo de contato em cinza, botão de informação à direita e barra de abas na base (folha 0002, q0016 a q0018); caixa de entrada com título, botão de editar, barra de busca, remetente em negrito, prévia e data alinhada à direita, mantida idêntica nos três aparelhos comparados (folha 0006, q0051, q0053 e q0054).
- O material de referência da Apple aparece em tela no começo e no fim: a página de documentação de glifos de barra, a página de recursos de design com um painel de exemplo mostrando título, campo de texto, interruptor e botões de ação (folha 0001, q0005 a q0007), e o card final com o endereço das diretrizes (folha 0009, q0073).
Proporção visual: as notas não registram nenhum quadro de apresentador em cena; os 73 quadros são cards de título, diagramas anotados, contornos de aparelho e capturas de apps do sistema, com predominância de comparações lado a lado e de camadas de anotação colorida sobre a interface.
Divergências ou limites registrados: um quadro traz um menu de contexto sobreposto com texto ilegível por causa da transparência (folha 0003, q0021); nas notas da folha 0006 fica registrado que a fala comenta a barra de status mais alta cobrindo conteúdo posicionado por valor fixo, mas as imagens desse intervalo não mostram esse caso diretamente; e vários pares de quadros se repetem sem alteração perceptível (folha 0001, q0001 e q0002, e q0006 e q0007; folha 0002, q0011 e q0012; folha 0003, q0024 e q0025; folha 0007, q0058 e q0059; folha 0008, q0068 e q0069).
<!-- /visual:tech-talks_801 -->

## O que este grupo revela sobre o jeito Apple

- A cada nova geometria de hardware (cantos arredondados do Series 4, wraparound do Series 7, sensor housing e cantos do iPhone X), a Apple parte de medidas físicas exatas em pontos e pixels e só depois deriva princípios de UI a partir delas, em vez de partir de uma ideia estética abstrata (ids: 801, 802, 10884).
- Mecanismos como Safe Area, System Minimum Layout Margins e .scenePadding cumprem o mesmo papel em plataformas diferentes: uma camada de sistema que recua automaticamente conteúdo das bordas e cantos, tirando do designer a conta manual de valores fixos (ids: 801, 802, 10884).
- Compatibilidade é tratada como requisito de design, não só de engenharia: apps não recompilados continuam funcionando, centralizados nas dimensões antigas, e só ganham o espaço extra ao recompilar com elementos relativos ao container em vez de larguras fixas (ids: 802, 801).
- Cor e tipografia aparecem explicitamente como ferramentas de identidade e hierarquia, não só de estilo: a accent color reforça a função de cada app (Mail, Tips, Mindfulness), e tamanhos de tipo extras chegam primeiro por acessibilidade (AX1 a AX3) antes de virarem recurso geral de design (id: 10884).
- Mesmo em decisões de UX de negócio, como a de assinatura, a prescrição de design é ancorada em dado quantitativo de comportamento (cliques versus conversão), na mesma lógica de "menos fricção, resultado melhor" usada nas decisões de layout (id: 803).
- As ferramentas oficiais de design (Figma, Sketch, Design Resources) são posicionadas como o elo entre designer e engenheiro, com atualização automática dos arquivos quando a Apple muda os kits, para manter o mockup fiel ao produto final (id: 111427).

## Sem transcrição

- tech-talks_111461: agora tem cartão próprio neste arquivo, com a base indicada no cartão.
- tech-talks_111466: agora tem cartão próprio neste arquivo, com a base indicada no cartão.
- tech-talks_111462: agora tem cartão próprio neste arquivo, com a base indicada no cartão.
- tech-talks_111463: agora tem cartão próprio neste arquivo, com a base indicada no cartão.

Esses quatro arquivos têm apenas título, fonte, duração e descrição; nenhum tem corpo de transcrição falada, por isso nada foi resumido deles.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111427.md, 13 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111461.md, 4 linhas lidas, até o fim: sim (arquivo só tem cabeçalho, sem transcrição).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111466.md, 4 linhas lidas, até o fim: sim (arquivo só tem cabeçalho, sem transcrição).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111462.md, 4 linhas lidas, até o fim: sim (arquivo só tem cabeçalho, sem transcrição).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_111463.md, 4 linhas lidas, até o fim: sim (arquivo só tem cabeçalho, sem transcrição).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_10884.md, 11 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_802.md, 73 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_803.md, 7 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/tech-talks_801.md, 16 linhas lidas, até o fim: sim.
