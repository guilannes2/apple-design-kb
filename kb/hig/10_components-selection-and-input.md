# Components / Selection and input

Base: Human Interface Guidelines da Apple, textos em /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/. Grupo de índice 10 da lista "hig" em groups.json, kb 54.

## Color wells (slug: color-wells)

O que governa: o color well, o controle que abre um seletor de cor para ajustar a cor de texto, formas, guias e outros elementos na tela.

Por que: a Apple recomenda o seletor de cor do sistema porque ele garante consistência entre apps e permite que as pessoas salvem um conjunto de cores acessível em qualquer app, além de ajudar a manter uma experiência familiar entre iOS, iPadOS e macOS.

Faça e evite:
- Considere o seletor de cor do sistema para uma experiência familiar em vez de construir um customizado.
- Em macOS, ao clicar num color well ele recebe destaque visual de confirmação de que está ativo, depois abre o seletor de cor.
- Em macOS, o color well suporta arrastar e soltar: cores podem ser arrastadas entre color wells e do seletor de cor para um color well.

Especificações exatas: nenhum número, medida ou duração é dado no texto.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS e visionOS. Não suportado em tvOS nem watchOS. Comportamento de destaque, abertura do picker e drag and drop descrito é específico de macOS.

Ligações com outros artigos: Color (relacionado). Documentação: UIColorWell e UIColorPickerViewController (UIKit), NSColorWell (AppKit), Color Programming Topics.

<!-- visual:color-wells -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido, com a mesma imagem em versão clara e escura; a página não tem vídeo.
- O color well é desenhado como botão quadrado de cantos arredondados com um chevron circular apontando para baixo, com seta de medida horizontal acima e vertical à direita cotando largura e altura (img 0253, clara).
- Uma cota de texto com o valor RGB aponta por uma linha para o centro do botão, tratando a cor atual como dado de especificação do controle (img 0253, clara).
- Abaixo do botão abre um popover com dez amostras em duas fileiras de cinco quadrados, em tons crescentes de vermelho e rosa, organizados em grade regular (img 0253, clara).
- O popover se liga ao botão por uma forma contínua em gota, que conecta visualmente o controle fechado ao painel aberto e sugere uma só origem, em vez de dois elementos soltos (img 0253, clara).
- As réguas e a cota são anotações de documentação, e não elementos reais da interface, o que faz da imagem um diagrama de geometria do componente e não uma captura do sistema (img 0253).
- No modo escuro, estrutura, réguas e posição do texto ficam idênticas; o fundo escurece, o contêiner do popover passa a marrom vinho, a caixa branca do botão vira contorno claro semitransparente e as amostras mantêm os mesmos tons (img 0253, clara e escura).
<!-- /visual:color-wells -->

## Combo boxes (slug: combo-boxes)

O que governa: o combo box, que combina um campo de texto com um botão pull-down num único controle, permitindo digitar um valor customizado ou escolher de uma lista de valores predefinidos.

Por que: o controle existe para equilibrar duas necessidades, a conveniência de escolher entre as opções mais prováveis e a liberdade de entrar um valor customizado quando nenhuma opção pré-definida serve. Quando a pessoa digita um valor customizado, ele não é adicionado à lista de opções.

Faça e evite:
- Preencha o campo com um valor padrão significativo tirado da lista; o campo pode ficar vazio por padrão, mas é melhor quando o valor padrão remete às opções ocultas; o valor padrão não precisa ser o primeiro item da lista.
- Use um rótulo introdutório para indicar que tipos de itens esperar, geralmente em title-style capitalization e terminando em dois pontos.
- Ofereça opções relevantes: as pessoas valorizam tanto poder digitar um valor customizado quanto a conveniência de escolher da lista das opções mais prováveis.
- Garanta que os itens da lista não sejam mais largos que o campo de texto, para não serem truncados e ficarem difíceis de ler.

Especificações exatas: nenhum número é dado no texto.

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS. É um controle exclusivo de macOS (NSComboBox, AppKit).

Ligações com outros artigos: Text fields, Pull-down buttons.

<!-- visual:combo-boxes -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido; só a versão clara está registrada e a página não tem vídeo.
- O combo box une num único controle o campo de texto editável e, à direita dele, o botão de seta para baixo, que fica dentro de um pequeno retângulo vermelho arredondado (img 0343).
- A régua horizontal acima cobre a largura do controle inteiro, incluindo o botão de seta, e a régua vertical à direita marca a altura, tratando campo e botão como uma unidade dimensional (img 0343).
- O campo mostra "Cupertino" com o cursor de texto logo depois da palavra, e a lista aberta abaixo traz quatro outras cidades, o que deixa visível que o valor digitado não precisa estar entre as opções predefinidas (img 0343).
- A lista suspensa usa a mesma hierarquia tipográfica para os quatro itens, em texto vermelho sobre fundo em degradê mais claro, sem nenhum item marcado como selecionado; o valor corrente fica só no campo (img 0343).
Divergências registradas: a descrição oficial fala genericamente de um combo box exibindo uma lista de cidades, e a imagem acrescenta o detalhe da entrada livre, pelo cursor após um nome que não está na lista.
<!-- /visual:combo-boxes -->

## Digit entry views (slug: digit-entry-views)

O que governa: a digit entry view, uma tela que ocupa a tela inteira e pede para a pessoa digitar uma série de dígitos, como um PIN, usando um teclado específico para dígitos.

Por que: como é usada tipicamente para dados sensíveis (como PIN), a Apple recomenda esconder o valor digitado e deixar clara a finalidade da tela, para que a pessoa entenda por que está sendo pedida a entrada.

Faça e evite:
- Use campos de dígito seguros (secure digit fields), que exibem asteriscos em vez do dígito digitado; use sempre um campo seguro quando o app pedir dados sensíveis.
- Declare claramente o propósito da digit entry view, com um título e um prompt que expliquem por que alguém precisa digitar dígitos.
- É possível adicionar um título opcional e um prompt acima da linha de dígitos.

Especificações exatas: nenhum número é dado no texto.

Diferenças por plataforma: não suportado em iOS, iPadOS, macOS, visionOS ou watchOS. Exclusivo de tvOS (a imagem do artigo descreve uma tela de PIN de cinco dígitos do Apple TV, segundo a descrição da imagem), com API TVDigitEntryViewController (TVUIKit).

Ligações com outros artigos: Virtual keyboards.

<!-- visual:digit-entry-views -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido; a página não tem vídeo.
- A imagem é um diagrama de especificação, e não captura de tela: título grande "Enter Passcode" e prompt de uma linha centralizados acima de cinco caixas retangulares enfileiradas na horizontal, que representam os campos de dígito (img 0460).
- A ordem vertical da tela é título, prompt, fileira de dígitos e, embaixo, uma fileira de números de 1 a 0 com botão de apagar, com o "1" destacado num quadrado branco como item em foco (img 0460).
- As cotas marcam o respiro em volta de cada bloco: seta vertical dupla acima do título até a borda superior, setas horizontais de cada lado da fileira de caixas para as margens laterais, pequenas marcas verticais entre as caixas para o espaçamento entre elas, e setas verticais entre as caixas e o teclado e entre o teclado e a borda inferior (img 0460).
- O diagrama comunica proporção e espaçamento por cotas, sem apresentar valores numéricos na leitura registrada, e usa tipografia grande centralizada (img 0460).
Divergências registradas: a descrição oficial identifica a imagem como tela de código de cinco dígitos da Apple TV, mas a imagem não mostra nenhum elemento que identifique o aparelho ou o tvOS; a compatibilidade com uma tela vista a distância é inferência das notas, não algo visível.
<!-- /visual:digit-entry-views -->

## Image wells (slug: image-wells)

O que governa: o image well, uma versão editável de uma image view, onde a pessoa pode copiar e colar a imagem, apagá-la, ou arrastar uma nova imagem para dentro sem precisar selecioná-lo primeiro.

Por que: o controle serve para tornar a manipulação de imagem direta e consistente com os padrões de edição do sistema (copiar, colar, arrastar), de modo que as pessoas usem os mesmos gestos e atalhos que já esperam de outros contextos de edição.

Faça e evite:
- Reverta para uma imagem padrão quando necessário: se o image well exige uma imagem, volte a mostrar a imagem padrão caso a pessoa limpe o conteúdo.
- Se o image well suportar copiar e colar, garanta que os itens padrão de menu de copiar e colar estejam disponíveis, já que as pessoas esperam usar esses itens de menu ou os atalhos de teclado padrão.

Especificações exatas: nenhum número é dado no texto.

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS. Exclusivo de macOS (NSImageView, AppKit).

Ligações com outros artigos: Image views, Edit menu.

<!-- visual:image-wells -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido, com uma única imagem na grade; a página não tem vídeo.
- O image well é desenhado como retângulo de cantos bem arredondados em degradê, com o glifo de imagem contido num quadrado menor de borda arredondada clara, centralizado (img 0629).
- Há bastante espaço vazio entre o quadrado interno e o retângulo maior, e essa moldura interna funciona como o poço onde uma imagem seria solta (img 0629).
- Diferente da ilustração de image views, que mostra o glifo ocupando quase todo o espaço com setas de dimensionamento, o image well não traz setas de medida e apresenta o glifo menor e com folga, o que sugere uma área de soltar distinta de uma área só de exibição (img 0629, comparada à img 0628 da página de image views).
Divergências registradas: a imagem concorda com a descrição oficial de poço de imagem estilizado, mas acrescenta a moldura de borda arredondada visível ao redor do glifo, ausente na descrição textual.
<!-- /visual:image-wells -->

## Pickers (slug: pickers)

O que governa: o picker, que exibe uma ou mais listas roláveis de valores distintos para escolha. Existem vários estilos fornecidos pelo sistema, cada um com valores selecionáveis e aparência diferentes; os valores exatos mostrados e sua ordem dependem do idioma do dispositivo (e, para date pickers, da localização do dispositivo).

Por que: o picker existe para facilitar a entrada de valores únicos ou de múltiplas partes sem exigir digitação livre. A Apple orienta a escolher o componente pelo tamanho da lista: um picker equilibra bem listas de tamanho médio a longo, pois rolar rapidamente por muitos itens funciona bem, mas adiciona peso visual demais a uma lista curta (para isso, pull-down buttons são melhores) e não é ideal para conjuntos muito grandes (para isso, listas e tabelas se ajustam em altura e podem ter índice, o que agiliza localizar uma seção).

Faça e evite:
- Considere um picker para listas de tamanho médio a longo; para listas curtas, considere um pull-down button; para conjuntos muito grandes, considere listas e tabelas.
- Use valores previsíveis e logicamente ordenados, como uma lista alfabetizada de países, para que as pessoas consigam se mover rapidamente pelos itens mesmo com valores ocultos antes da interação.
- Evite trocar de tela para mostrar um picker; ele funciona bem exibido em contexto, abaixo ou perto do campo que está sendo editado, tipicamente na parte inferior de uma janela ou num popover.
- Considere oferecer menos granularidade ao especificar minutos num date picker, aumentando o intervalo de minutos desde que ele divida 60 igualmente (por exemplo, intervalos de quinze minutos).

Especificações exatas:
- Por padrão, uma lista de minutos inclui 60 valores (0 a 59).
- Exemplo de intervalo alternativo: 0, 15, 30 e 45 minutos.
- O modo countdown timer (iOS, iPadOS) exibe horas e minutos até um máximo de 23 horas e 59 minutos, e esse modo não está disponível nos estilos inline ou compact.

Diferenças por plataforma:
- Sem considerações adicionais para visionOS.
- iOS, iPadOS: date picker com quatro estilos (compact, inline, wheels, automatic) e quatro modos (date, time, date and time, countdown timer). Compact é recomendado quando o espaço é restrito: mostra um botão no accent color do app que, ao ser tocado, abre uma modal com editor de calendário e time picker familiares, permitindo múltiplas edições antes de confirmar ao tocar fora.
- macOS: dois estilos de date picker, textual (para espaço limitado e seleções específicas de data e hora) e graphical (para navegar por dias num calendário, selecionar um intervalo de datas, ou quando um mostrador tipo relógio é apropriado). Ver NSDatePicker.
- tvOS: pickers disponíveis via SwiftUI (Picker).
- watchOS: pickers exibem listas navegadas pela Digital Crown, no estilo wheels, incluindo date e time pickers nesse estilo; é possível configurar contorno (outline), legenda (caption) e indicador de rolagem; para listas mais longas, um navigation link exibe o picker como botão, e a pessoa também pode percorrer as opções girando a Digital Crown sem tocar no botão.

Ligações com outros artigos: Pull-down buttons, Lists and tables.

Change log do artigo: 5 de junho de 2023, atualização da orientação para uso de pickers em watchOS.

<!-- visual:pickers -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações vistas, todos os códigos conferidos; a página não tem vídeo.
- A abertura estiliza um Apple Watch com três faixas empilhadas como lista rolável: a central é maior, tem contorno branco destacado e o texto "Item", marcando a seleção, e as faixas de cima e de baixo aparecem reduzidas e parcialmente cobertas, como itens fora de foco; uma seta aparece à direita da faixa central (img 0841).
- No layout compacto do iOS, a linha "Date" mostra o valor em azul à direita dentro de um cartão cinza claro, e o toque abre abaixo um popover sobre o conteúdo com calendário mensal completo, setas de navegação de mês, cabeçalho dos dias da semana e grade de dias, com o dia escolhido em círculo azul e outro dia em azul, lido nas notas como a data atual (img 0842).
- No layout inline, o cartão traz o título e um toggle verde ativo na mesma linha, e o mesmo calendário fica incorporado dentro do próprio cartão, sem popover (img 0843).
- Na variação com rodas, o cartão "Time" mostra o valor em azul na linha do título e, abaixo, três rodas verticais para hora, minutos e AM ou PM, com o valor central em texto maior e preto e os adjacentes em cinza claro, sugerindo profundidade de rolagem tipo carretel (img 0844).
- No watchOS, a tela preta tem título em azul no topo e botão de voltar; abaixo, um rótulo verde nomeia o campo e uma roda de três posições destaca o valor central com contorno verde, com os vizinhos cortados e esmaecidos, e um botão verde de confirmação fica na base (img 0845).
- Para data, três rodas lado a lado com contorno cada uma, a central destacada em verde, e o botão da base diz "Next", indicando seleção em etapas (img 0846); para hora, três rodas separadas por dois pontos, com a central em verde e botão de confirmação na base (img 0847).
- Para listas maiores no watchOS, o picker fechado é um botão retangular cinza escuro com duas linhas de texto, uma maior em branco e outra menor em cinza abaixo, que representa a opção selecionada (img 0848); tocado, abre uma lista vertical com linhas separadas por divisórias finas e check verde à direita do item selecionado (img 0849).
- Nas telas de watchOS o verde é reservado para foco e seleção: contorno da roda, rótulo do campo, botão de ação e check (img 0845, img 0846, img 0847, img 0849); o azul aparece no título do topo (img 0845, img 0849).
- No iOS o azul marca o valor na linha do cartão (img 0842, img 0844) e o dia escolhido no calendário compacto (img 0842), e o mesmo componente muda de forma de apresentação entre popover, inline e rodas (img 0842, img 0843, img 0844).
<!-- /visual:pickers -->

## Segmented controls (slug: segmented-controls)

O que governa: o segmented control, um conjunto linear de dois ou mais segmentos, cada um funcionando como um botão; em geral todos os segmentos têm largura igual. Oferece uma escolha única entre um conjunto de opções ou, em macOS, uma escolha única ou múltipla.

Por que: o valor do segmented control está em agrupar funções relacionadas de forma que a agrupação se preserve independentemente do tamanho da view ou de onde o controle aparece, o que ajuda as pessoas a entenderem de relance quais controles estão selecionados no momento. Também pode funcionar sem estado de seleção, como um conjunto de botões que executam ações (por exemplo, Reply, Reply all e Forward no macOS Mail).

Faça e evite:
- Use um segmented control para oferecer escolhas intimamente relacionadas que afetam um objeto, estado ou view.
- Considere um segmented control quando é importante agrupar funções ou mostrar claramente seu estado de seleção.
- Mantenha os tipos de controle consistentes dentro de um único segmented control: não misture segmentos que representam ações com segmentos que representam estado de seleção.
- Limite o número de segmentos: muitos segmentos são difíceis de interpretar e demorados de navegar.
- Mantenha o tamanho dos segmentos consistente; quando todos têm largura igual, o controle parece equilibrado; procure manter também larguras de ícone e título consistentes.
- Prefira usar texto ou imagens, não uma mistura dos dois, num mesmo segmented control, pois misturar pode gerar uma interface confusa e desconectada.
- Use conteúdo de tamanho similar em cada segmento, já que os segmentos costumam ter largura igual.
- Use substantivos ou frases nominais para rótulos de segmento, com title-style capitalization; um segmented control com rótulos de texto não precisa de texto introdutório.

Especificações exatas: procure não mais que cerca de cinco a sete segmentos numa interface larga, e não mais que cerca de cinco segmentos no iPhone.

Diferenças por plataforma:
- Não suportado em watchOS.
- iOS, iPadOS: considere um segmented control para alternar entre subviews intimamente relacionadas (exemplo: o sheet de novo evento do Calendar alterna entre criar um evento e um lembrete); para alternar entre seções totalmente separadas do app, use tab bars.
- macOS: considere texto introdutório para esclarecer o propósito do controle; se usar símbolos ou ícones, pode adicionar um rótulo abaixo de cada segmento e um tooltip por segmento; use uma tab view na área principal da janela, em vez de segmented control, para alternância de views; considere suportar spring loading (em Mac com Magic Trackpad, permite ativar um segmento arrastando itens selecionados sobre ele e fazendo force click, sem soltar os itens, e continuar arrastando depois).
- tvOS: considere uma split view em vez de segmented control em telas que filtram conteúdo; evite colocar outros elementos focalizáveis perto de segmented controls, porque os segmentos ficam selecionados quando o foco chega até eles, não quando são clicados, o que pode causar foco acidental em elementos próximos.
- visionOS: quando a pessoa olha para um segmented control que usa ícones, o sistema mostra um tooltip com o texto descritivo fornecido.

Ligações com outros artigos: Split views, Buttons, Tab bars, Boxes, Tab views.

Change log do artigo: 21 de junho de 2023, atualizado para incluir orientação para visionOS.

<!-- visual:segmented-controls -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A ilustração de abertura funciona como diagrama de proporções: três segmentos rotulados "Label", o primeiro selecionado em fundo claro, setas horizontais acima marcando a largura total, marca vertical à direita indicando a altura e uma seta pequena sob o primeiro segmento sugerindo o ponto de toque (img 0995).
- Escolha única e escolha múltipla aparecem em pares com o mesmo desenho de controle, mudando só a quantidade de segmentos preenchidos: nos ícones de alinhamento, apenas um segmento fica em azul sólido com glifo branco (img 0996); nos estilos B, I, U e S, três ficam azuis ao mesmo tempo e o quarto permanece branco (img 0997).
- Nesses dois controles, os segmentos inativos ficam sobre fundo branco, com glifo cinza no de alinhamento, e a seleção é indicada por preenchimento, não por borda ou sublinhado (img 0996, img 0997).
- No controle de alinhamento, uma linha divisória vertical fina separa o terceiro segmento do quarto, o que sugere um agrupamento ligeiramente diferente para o último ícone dentro do mesmo controle (img 0996).
- Nas telas de iOS, a seleção tem outro tratamento: o segmento ativo aparece em branco elevado, sobre fundo cinza no seletor de período do app Saúde (img 0998), e também em branco elevado no par Event e Reminder do Calendário (img 0999).
- No app Saúde, o controle com cinco segmentos de rótulos curtos (D, W, M, 6M, Y) fica logo abaixo do cabeçalho e governa o período dos gráficos de Move e Exercise que vêm abaixo (img 0998).
- No sheet New Event do Calendário no iPhone, o controle de dois segmentos fica logo abaixo do cabeçalho com os botões de fechar e confirmar, e os campos abaixo (all-day, Starts, Ends, Travel Time) são os específicos do modo Event selecionado (img 0999).
- No Calendário do Mac, chamadas de texto separam os dois componentes parecidos: o segmented control fica na barra lateral filtrando convites, com "New" selecionado em vermelho, enquanto a tab view com Day, Week, Month e Year fica no canto superior direito da janela principal, com Month selecionado (img 1000).
- Todos os exemplos usam um único tipo de conteúdo por controle: só ícones (img 0996), só letras de estilo (img 0997) ou só rótulos de texto (img 0998, img 0999, img 1000), e os exemplos reais sempre mostram o controle dentro de uma tela completa de app, não isolado.
<!-- /visual:segmented-controls -->

## Sliders (slug: sliders)

O que governa: o slider, uma trilha horizontal com um controle chamado thumb que a pessoa ajusta entre um valor mínimo e máximo; conforme o valor muda, a porção da trilha entre o mínimo e o thumb se preenche de cor. Pode exibir opcionalmente ícones à esquerda e à direita que ilustram o significado dos valores mínimo e máximo.

Por que: a consistência direcional existe porque as pessoas desenvolvem uma expectativa fixa de onde ficam os extremos mínimo e máximo, e quebrar essa expectativa atrapalha o uso intuitivo. O feedback ao vivo e as marcações de escala (tick marks) existem para ajudar a localizar valores específicos com mais precisão, principalmente quando a faixa de valores é ampla ou não linear.

Faça e evite:
- Personalize a aparência do slider (cor da trilha, imagem e cor do thumb, ícones laterais) se isso agregar valor e comunicar intenção.
- Use direções familiares: valor mínimo do lado inicial (leading) e máximo do lado final (trailing) em sliders horizontais; mínimo embaixo e máximo em cima em sliders verticais.
- Considere complementar um slider com um campo de texto e um stepper correspondentes, especialmente quando o slider representa uma faixa ampla de valores; o stepper oferece uma forma conveniente de incrementar em valores inteiros.
- Em macOS, considere dar feedback ao vivo conforme o valor muda.
- Em macOS, escolha o estilo de slider que corresponde à expectativa das pessoas: horizontal é ideal para mover-se entre um ponto inicial e final fixos; circular é indicado para valores que se repetem ou continuam indefinidamente.
- Em macOS, considere usar um rótulo para introduzir um slider, em sentence-style capitalization terminando em dois pontos.
- Em macOS, use tick marks para aumentar clareza e precisão, e considere rotulá-las para ainda mais clareza; não é necessário rotular cada marca, a menos que seja preciso reduzir confusão; em muitos casos, rotular apenas os valores mínimo e máximo já basta; quando os valores do slider são não lineares, rótulos periódicos dão contexto; também é boa prática mostrar um tooltip com o valor do thumb quando a pessoa mantém o ponteiro sobre ele.

Especificações exatas:
- Exemplo de faixa: slider horizontal de opacidade entre 0 e 100 por cento.
- Exemplo de slider circular: rotação de um objeto entre 0 e 360 graus.
- Exemplo de slider circular para animação: quatro rotações completas equivalem a quatro giros, ou 1440 graus de rotação.

Diferenças por plataforma:
- Não suportado em tvOS.
- iOS, iPadOS: não use um slider para ajustar volume de áudio; para controle de volume, use uma volume view, que é personalizável e inclui um slider de nível de volume e um controle para trocar o dispositivo de saída de áudio ativo.
- macOS: sliders podem incluir tick marks; num slider linear, o thumb tem formato de losango estreito; num slider circular, o thumb aparece como um pequeno círculo, e as tick marks, quando presentes, aparecem como pontos igualmente espaçados ao redor da circunferência.
- visionOS: prefira sliders horizontais, pois em geral é mais fácil gesticular de um lado para o outro do que de cima para baixo.
- watchOS: o slider é uma trilha horizontal exibida como um conjunto de passos discretos ou como uma barra contínua, representando uma faixa finita de valores; a pessoa toca botões nas laterais do slider para aumentar ou diminuir o valor por um montante predefinido; o sistema exibe sinais de mais e menos por padrão, mas é possível criar glifos customizados se necessário.

Ligações com outros artigos: Steppers, Pickers, Text fields, Playing audio.

Change log do artigo: 21 de junho de 2023, atualizado para incluir orientação para visionOS.

<!-- visual:sliders -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A ilustração de abertura nomeia as três posições de referência do slider com marcações verticais finas rotuladas "Min", "Mid" e "Max" acima da trilha, alinhadas ao início, ao meio e ao fim, com o polegar em forma de pílula no centro exato (img 1080).
- Na abertura, as pontas da trilha levam um ícone de brilho e uma seta dupla apontando para fora, que indicam o sentido de diminuir e aumentar, e a trilha à esquerda do polegar fica mais escura que a da direita, sugerindo a parte preenchida; é uma peça conceitual, não captura de app (img 1080).
- Slider, campo de texto e stepper formam um grupo numa única linha: rótulo "Opacity", slider azul com polegar branco circular, campo retangular com o valor em porcentagem e o stepper de setas empilhadas colado à direita do campo; o polegar dá a posição aproximada e o campo dá o número exato (img 1081).
- No macOS, o slider linear sem marcas é só a trilha preenchida em azul da esquerda até o polegar branco, dentro de um cartão cinza claro (img 1082).
- A versão com tick marks mantém o mesmo cartão e acrescenta traços verticais cinza curtos, igualmente espaçados, cerca de nove, cobrindo toda a trilha e não só a parte preenchida (img 1083).
- O slider circular do macOS é um aro claro pequeno com um ponto cinza escuro na posição das 12 horas, sem numeração e, nesta instância, sem marcas de escala (img 1084).
- No painel Energy Saver, as tick marks ficam sob a trilha e só alguns pontos da escala recebem rótulo ("1 min", "15 min", "1hr", "3 hrs", "Never"), não cada marca; o polegar aparece logo depois de "15 min" (img 1085).
- No watchOS, o slider é uma cápsula preta compacta com ícone de volume baixo à esquerda e de volume alto à direita, e o preenchimento é verde (img 1086, img 1087).
- A diferença entre discreto e contínuo no watchOS está só na textura da barra central, mostrada lado a lado na mesma folha: blocos curtos separados por espaços, com pouco menos da metade preenchida, contra uma barra lisa preenchida até cerca da metade (img 1086, img 1087).
<!-- /visual:sliders -->

## Steppers (slug: steppers)

O que governa: o stepper, um controle de dois segmentos usado para aumentar ou diminuir um valor incremental; ele fica ao lado de um campo que exibe seu valor atual, porque o próprio stepper não exibe um valor.

Por que: como o stepper não mostra nenhum valor por si só, a Apple enfatiza deixar claro qual valor está sendo alterado; a combinação com um campo de texto existe para atender tanto a pequenas mudanças (bem servidas por toques ou cliques no stepper) quanto a mudanças grandes ou muito variáveis (melhor servidas por digitação direta).

Faça e evite:
- Deixe óbvio qual valor o stepper afeta.
- Considere parear um stepper com um campo de texto quando mudanças grandes de valor forem prováveis; steppers funcionam bem sozinhos para pequenas mudanças com poucos toques ou cliques, mas as pessoas apreciam poder digitar valores específicos quando os valores variam muito (exemplo dado: uma tela de impressão com stepper e campo de texto para definir o número de cópias).
- Em macOS, para faixas de valores grandes, considere suportar Shift-click para mudar o valor rapidamente, por um múltiplo maior que o incremento padrão.

Especificações exatas: exemplo dado de Shift-click alterando o valor por 10 vezes o incremento padrão.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS ou visionOS. Não suportado em watchOS nem tvOS. Shift-click com múltiplo maior é específico de macOS.

Ligações com outros artigos: Pickers, Text fields.

<!-- visual:steppers -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página tem só a ilustração de abertura e não tem vídeo.
- O stepper é desenhado como uma pílula vertical dividida ao meio por uma linha horizontal fina, com seta para cima na metade superior e seta para baixo na metade inferior, deixando cada segmento com uma única função (img 1107).
- A ilustração traz cotas de construção: uma chave horizontal no topo indicando a largura do controle e uma chave vertical à direita indicando a altura total (img 1107).
- O comportamento vem anotado em pseudocódigo, com "i++" ligado por linha à metade superior e "i--" ligado à metade inferior, mapeando cada segmento ao incremento e ao decremento; é o único ponto do material que expressa a lógica do controle como notação de código (img 1107).
- O controle aparece isolado, sem campo ou número ao lado, em gradiente laranja para vermelho, como peça conceitual e não captura de app; a imagem não mostra o pareamento com campo de texto (img 1107).
<!-- /visual:steppers -->

## Text fields (slug: text-fields)

O que governa: o text field, uma área retangular onde a pessoa entra ou edita pequenos trechos específicos de texto, como um nome ou endereço de e-mail; para volumes maiores de texto, usa-se text views em vez disso.

Por que: as orientações giram em torno de reduzir esforço e ambiguidade na entrada de texto: mostrar o propósito do campo antes de digitar (placeholder e rótulo), proteger dados sensíveis, ajustar tamanho e espaçamento ao conteúdo esperado, manter uma sequência de tabulação lógica entre campos, e validar no momento certo para não interromper o fluxo de digitação desnecessariamente.

Faça e evite:
- Use um text field para pedir uma pequena quantidade de informação; para textos maiores, use text views.
- Mostre uma dica (placeholder text) no campo, como "Email" ou "Password", para comunicar seu propósito; como o placeholder desaparece ao digitar, também pode ser útil incluir um rótulo separado.
- Use campos de texto seguros para esconder dados privados, sempre que o app pedir dados sensíveis como senha.
- Combine o tamanho do campo com a quantidade de texto esperada, para ajudar a pessoa a avaliar visualmente quanto texto fornecer.
- Espace uniformemente múltiplos campos de texto, empilhando-os verticalmente quando possível e usando larguras consistentes para criar um layout organizado.
- Garanta que a tabulação entre múltiplos campos siga uma sequência lógica; o sistema tenta fazer isso automaticamente.
- Valide campos quando fizer sentido, escolhendo o momento certo conforme o contexto (por exemplo, validar e-mail ao trocar de campo; validar nome de usuário ou senha antes de trocar de campo).
- Use um number formatter para dados numéricos, que configura o campo para aceitar só valores numéricos e pode exibir o valor de forma específica (certo número de casas decimais, porcentagem, moeda); não presuma a apresentação exata, pois a formatação varia por localidade.
- Ajuste as quebras de linha conforme a necessidade do campo: por padrão o sistema corta texto que ultrapassa os limites do campo; alternativamente é possível quebrar linha por caractere ou palavra, ou truncar com reticências no início, meio ou fim.
- Considere um expansion tooltip para mostrar a versão completa de texto cortado ou truncado, aparecendo quando a pessoa posiciona o ponteiro sobre o campo.
- Em iOS, iPadOS, tvOS e visionOS, mostre o tipo de teclado apropriado ao tipo de conteúdo esperado.
- Minimize a entrada de texto em apps de tvOS e watchOS, preferindo formas mais eficientes de coletar informação, como botões.

Especificações exatas: nenhum número fixo de especificação é dado no texto (os exemplos de imagem mencionam um número com quatro casas decimais e um valor de moeda, mas são descrições de imagem, não uma regra numérica).

Diferenças por plataforma:
- Sem considerações adicionais para tvOS ou visionOS.
- iOS, iPadOS: exiba um botão Clear na extremidade final (trailing) do campo para apagar a entrada com um toque, sem precisar manter a tecla Delete pressionada; use imagens e botões nas duas extremidades do campo, em geral a extremidade inicial (leading) para indicar o propósito do campo e a final (trailing) para recursos adicionais, como um botão de marcadores (Bookmarks).
- macOS: considere um combo box se precisar combinar entrada de texto com uma lista de opções.
- watchOS: apresente um campo de texto só quando necessário, preferindo sempre que possível exibir uma lista de opções em vez de exigir digitação.

Ligações com outros artigos: Text views, Combo boxes, Entering data, Virtual keyboards.

Change log do artigo: 5 de junho de 2023, atualização refletindo mudanças no watchOS 10.

<!-- visual:text-fields -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A ilustração de abertura define as partes do campo: placeholder "Value" com cursor, botão circular de limpar com X na extremidade direita e setas de régua sobrepostas marcando a largura acima e a altura à direita (img 1138).
- A abertura é a única peça conceitual, em gradiente laranja e vermelho; todas as demais imagens da página são capturas limpas do campo sobre fundo neutro, sem moldura de aparelho (img 1138 a img 1142).
- Para dados numéricos, os campos aparecem empilhados verticalmente num cartão cinza claro, com o rótulo fora da caixa, à esquerda e terminado em dois pontos, e o valor alinhado à direita dentro do campo (img 1139).
- O mesmo número aparece em duas apresentações: "100000.00" como número simples e "$100,000.00" com separador de milhar e símbolo de moeda (img 1139).
- Os três comportamentos de texto longo usam a mesma frase de teste para comparação direta: num campo de uma linha, o texto é cortado exatamente na borda direita, sem reticências (img 1140).
- Na quebra por palavra, o campo fica mais alto, com duas linhas, e a frase aparece completa, dividida entre "jumps" e "over" (img 1141).
- No truncamento, o campo volta a ter uma linha e o restante do texto é substituído por reticências no final (img 1142).
<!-- /visual:text-fields -->

## Toggles (slug: toggles)

O que governa: o toggle, que deixa a pessoa escolher entre um par de estados opostos, como ligado e desligado, usando uma aparência diferente para indicar cada estado; pode ter estilos como switch e checkbox, que variam por plataforma. Além dos toggles, todas as plataformas também suportam botões que se comportam como toggle, mudando de aparência conforme o estado.

Por que: o toggle sempre gerencia o estado de algo (não uma lista de opções, para o que se usa outro componente como pop-up button); a Apple insiste em tornar óbvias as diferenças visuais entre os estados e em não depender só de cor para comunicar o estado, porque nem todo mundo percebe diferenças de cor.

Faça e evite:
- Use um toggle para escolher entre dois valores opostos que afetam o estado de um conteúdo ou view.
- Identifique claramente a configuração, view ou conteúdo que o toggle afeta; em geral o contexto ao redor já basta, mas é possível fornecer um rótulo, comum em apps macOS; se usar um botão que se comporta como toggle, use um ícone de interface que comunique seu propósito e atualize sua aparência (tipicamente mudando o fundo) conforme o estado atual.
- Torne óbvias as diferenças visuais de estado (adicionar/remover preenchimento de cor, mostrar/esconder a forma de fundo, mudar detalhes internos como uma marca de seleção ou ponto); evite depender só de cores diferentes.

Especificações exatas:
- Radio buttons são tipicamente exibidos em grupos de dois a cinco.
- Se for preciso apresentar mais de cerca de cinco opções, considere um componente como pop-up buttons em vez de uma lista longa de radio buttons.

Diferenças por plataforma:
- Sem considerações adicionais para tvOS, visionOS ou watchOS.
- iOS, iPadOS: use o estilo switch só dentro de uma linha de lista, sem precisar de rótulo porque o conteúdo da linha já dá o contexto; mude a cor padrão do switch (verde) só se necessário, preferindo o accent color do app quando fizer sentido, garantindo contraste suficiente com a aparência sem cor; fora de uma lista, use um botão que se comporte como toggle, não um switch (exemplo dado: o botão de filtro no app Phone usa um destaque azul quando ativo e remove o destaque quando inativo); evite fornecer um rótulo que explique o propósito do botão, já que o ícone de interface combinado com a aparência de fundo alternativa já comunicam isso.
- macOS: além do estilo switch, suporta o estilo checkbox e também define radio buttons; use switches, checkboxes e radio buttons no corpo da janela, não no frame da janela (evite em toolbar ou status bar).
  - Switches: prefira um switch para configurações que se quer enfatizar, já que tem mais peso visual que um checkbox, sendo adequado quando controla mais funcionalidade que um checkbox tipicamente controla (por exemplo, ligar ou desligar um grupo de configurações); dentro de um formulário agrupado, considere um mini switch para controlar a configuração numa única linha, cuja altura é semelhante à de botões e outros controles, resultando em linhas de altura consistente; ao apresentar uma hierarquia de configurações num formulário agrupado, é possível usar um switch regular para a configuração primária e mini switches para as subordinadas; em geral, não substitua um checkbox já em uso por um switch.
  - Checkboxes: um checkbox é um pequeno botão quadrado, vazio quando desligado, com marca de seleção quando ligado, e pode conter um traço quando o estado é misto; tipicamente inclui um título na extremidade final (trailing); num checklist editável, pode aparecer sem título ou conteúdo adicional; use checkbox em vez de switch se precisar apresentar uma hierarquia de configurações, usando alinhamento (geralmente pela borda inicial/leading) e indentação para mostrar dependências; considere radio buttons se precisar apresentar um conjunto de mais de duas opções mutuamente exclusivas; considere um rótulo para introduzir um grupo de checkboxes se a relação entre eles não for clara, alinhando a linha de base do rótulo com o primeiro checkbox do grupo; reflita com precisão o estado do checkbox (ligado, desligado ou misto) na aparência, mostrando o estado misto quando os checkboxes subordinados têm estados diferentes.
  - Radio buttons: um radio button é um pequeno botão circular seguido de um rótulo, tipicamente exibido em grupos de dois a cinco, apresentando um conjunto de escolhas mutuamente exclusivas; o estado é selecionado (círculo preenchido) ou desselecionado (círculo vazio); embora um radio button também possa exibir um estado misto (indicado por um traço), esse estado é raramente útil porque múltiplos estados podem ser comunicados com radio buttons adicionais, e para estado misto é melhor usar um checkbox; prefira um conjunto de radio buttons para opções mutuamente exclusivas, e checkboxes se a pessoa puder escolher múltiplas opções; evite listar radio buttons demais (mais de cerca de cinco opções sugere considerar um componente como pop-up buttons); para uma única configuração liga/desliga, prefira um checkbox, já que a presença ou ausência da marca de seleção torna o estado mais fácil de entender rapidamente (em casos raros de um checkbox não comunicar claramente estados opostos, é possível usar um par de radio buttons, cada um rotulado com o estado que controla); use espaçamento consistente ao exibir radio buttons horizontalmente, medindo o espaço necessário para o rótulo mais longo e usando essa medida de forma consistente.

Ligações com outros artigos: Pop-up buttons, Layout.

Change log do artigo: 29 de março de 2024, orientação aprimorada para uso de switches em apps macOS, esclarecimento sobre quando um checkbox tem título, e nova arte para radio buttons; 12 de setembro de 2023, arte atualizada.

<!-- visual:toggles -->
### O que as ilustrações mostram
Base: 4 de 4 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A ilustração de abertura mostra o par de estados do switch com rótulo pontilhado "Label": ligado em vermelho escuro com a bolinha branca à direita e setas de régua medindo largura e altura, e desligado em branco com contorno vermelho fino e um pequeno círculo vazio à direita (img 1147).
- No iOS, o switch aparece dentro de linhas de lista num cartão, com rótulo "Title" à esquerda e linha divisória fina entre as linhas; desligado é trilho cinza claro com a bolinha à esquerda, ligado é verde padrão com a bolinha branca à direita (img 1148).
- A troca da cor padrão é mostrada repetindo exatamente a mesma estrutura de cartão e mudando só a cor do estado ligado para um roxo customizado, em imagem separada (img 1149 comparada com img 1148).
- O botão que se comporta como toggle é mostrado em dois quadros do app Phone: com o controle segmentado em "Missed", o botão circular de filtro à direita da barra fica em azul sólido e a lista mostra só chamadas perdidas em vermelho (img 1150); com "All" selecionado, o botão perde o preenchimento, fica só com contorno cinza claro, e a lista mostra todas as chamadas (img 1151).
- Nesses quadros do Phone, o estado do botão de filtro é comunicado por preenchimento de fundo atrás do símbolo, sem trilho de switch (img 1150, img 1151).
- Os três estados do checkbox aparecem isolados, cada um em sua imagem com legenda: ligado é quadrado de cantos arredondados em azul com marca de check branca (img 1153), desligado é só um contorno cinza claro muito sutil (img 1154) e misto é o quadrado azul com um traço horizontal branco no lugar do check (img 1155).
- Numa lista de sete checkboxes num cartão cinza claro, o primeiro item está em estado misto e os seguintes variam entre vazio e marcado, mostrando os estados lado a lado numa lista plana (img 1152).
- O grupo de radio buttons tem cinco linhas num cartão, e só o terceiro círculo está preenchido em azul com ponto branco central, enquanto os demais são círculos vazios cinza claro (img 1156).
- Os estados do radio button repetem o padrão isolado com legenda: selecionado é círculo azul com ponto branco central e desselecionado é círculo vazio com contorno cinza muito sutil (img 1157, img 1158).
- Checkbox e radio button compartilham o mesmo vocabulário: preenchimento azul com uma marca branca interna distinta (check, traço ou ponto) para indicar estado, em vez de apenas mudar de cor (img 1153, img 1155, img 1157).
- Em radio buttons dispostos na horizontal, os três blocos ocupam a mesma largura mesmo com rótulos de tamanhos diferentes ("A long text label", "Short label"), com a opção central selecionada (img 1159).
Divergências registradas: na lista de checkboxes (img 1152) não há indentação hierárquica visível, embora o texto do artigo trate de hierarquia expressa por alinhamento e indentação.
<!-- /visual:toggles -->

## Virtual keyboards (slug: virtual-keyboards)

O que governa: em dispositivos sem teclado físico, o sistema oferece vários tipos de teclado virtual para entrada de dados; um teclado virtual pode fornecer um conjunto específico de teclas otimizado para a tarefa atual (por exemplo, um teclado para digitar e-mail pode incluir "@", um ponto ou até ".com") e não suporta atalhos de teclado. Quando fizer sentido, o app pode substituir o teclado do sistema por uma view customizada de entrada de dados específica do app; em iOS, iPadOS e tvOS também é possível criar uma app extension que oferece um teclado customizado instalável em substituição ao teclado padrão.

Por que: escolher o teclado certo para o tipo de conteúdo reduz esforço de digitação e erros, e ao especificar o significado semântico de uma área de entrada de texto o sistema consegue oferecer automaticamente um teclado compatível, inclusive refinando as correções que propõe. Teclados e input views customizados existem para tarefas de entrada de dados específicas do app que o teclado padrão não atende bem, mas a Apple pede que essa substituição faça sentido no contexto, senão a pessoa pode estranhar não conseguir voltar ao teclado do sistema.

Faça e evite:
- Escolha um teclado que corresponda ao tipo de conteúdo sendo editado (por exemplo, o teclado de números e pontuação para dados numéricos).
- Considere personalizar o tipo da tecla Return se isso esclarecer a experiência de entrada de texto (por exemplo, um Return do tipo busca quando o app inicia uma pesquisa).
- Ao criar um input view customizado, garanta que ele faça sentido no contexto do app, já que além de tornar a entrada de dados simples e intuitiva é preciso que as pessoas entendam por que não conseguem usar o teclado do sistema ali.
- Toque o som padrão de teclado enquanto a pessoa digita num input view customizado, para manter o feedback familiar que as pessoas esperam do teclado do sistema (esse som pode ser desligado globalmente em Ajustes > Sons).
- Teclados customizados (via app extension) fazem sentido quando se quer expor uma funcionalidade de teclado única em todo o sistema, como uma forma nova de digitar texto ou suporte a um idioma que o sistema não suporta; se o objetivo é um teclado só dentro do próprio app, prefira um input view customizado.
- Depois de escolhido em Ajustes, um teclado customizado pode ser usado para entrada de texto em qualquer app, exceto ao editar campos de texto seguros e campos de número de telefone; a pessoa pode escolher múltiplos teclados customizados e alternar entre eles a qualquer momento.
- Forneça uma forma óbvia e fácil de trocar de teclado: a tecla Globe do teclado padrão (que substitui a tecla Emoji dedicada quando há múltiplos teclados disponíveis) alterna rapidamente entre teclados, e as pessoas esperam uma experiência igualmente intuitiva no teclado customizado.
- Evite duplicar recursos do teclado do sistema: em alguns dispositivos, as teclas Emoji/Globe e Dictation aparecem automaticamente abaixo do teclado mesmo com teclados customizados em uso, e o app não pode afetar essas teclas.
- Considere fornecer um tutorial de teclado dentro do app, em vez de exibir conteúdo de ajuda dentro do próprio teclado.

Especificações exatas: nenhum número, medida ou duração é dado no texto.

Diferenças por plataforma:
- Não suportado em macOS.
- iOS, iPadOS: use o keyboard layout guide para que o teclado pareça parte integrada da interface e para manter partes importantes da interface visíveis enquanto o teclado virtual está na tela; posicione controles customizados acima do teclado (input accessory view) com cuidado, garantindo que sejam relevantes à tarefa atual; se outras views do app usam Liquid Glass, ou se a view customizada parece deslocada acima do teclado, aplique Liquid Glass à view que contém os controles para manter consistência (uma toolbar padrão adota Liquid Glass automaticamente); use o keyboard layout guide e o padding padrão para garantir o posicionamento esperado dos controles.
- tvOS: exibe um teclado virtual linear quando a pessoa seleciona um campo de texto usando o Siri Remote; uma tela de teclado em grade aparece quando outros dispositivos são usados, com o layout de conteúdo se adaptando automaticamente ao teclado; ao ativar uma digit entry view, o tvOS mostra um teclado específico para dígitos.
- visionOS: o teclado virtual do sistema suporta gestos diretos e indiretos e aparece numa janela separada que a pessoa pode mover para onde quiser; não é preciso considerar a localização do teclado nos layouts.
- watchOS: num Apple Watch, um campo de texto pode mostrar um teclado se a tela do dispositivo for grande o bastante; caso contrário, o sistema permite ditado ou Scribble para entrada de informação; não é possível mudar o tipo de teclado no watchOS, mas é possível definir o content type do campo de texto, que o sistema usa para facilitar a entrada (como oferecer sugestões); a pessoa também pode usar um iPhone pareado próximo para digitar texto no Apple Watch.

Ligações com outros artigos: Entering data, Keyboards, Layout, Digit entry views, App extensions.

Change log do artigo: 9 de junho de 2025, orientação adicionada sobre controles customizados acima do teclado e atualização sobre disponibilidade do teclado virtual em watchOS; 2 de fevereiro de 2024, esclarecimento sobre suporte a gestos diretos e indiretos em visionOS; 5 de dezembro de 2023, arte adicionada para visionOS; 21 de junho de 2023, título do artigo mudado de "Onscreen keyboards" e atualizado para incluir orientação para visionOS.

<!-- visual:virtual-keyboards -->
### O que as ilustrações mostram
Base: 5 de 5 folhas de ilustrações e 2 de 2 folhas do vídeo de visionOS abertas, todos os códigos conferidos.
- A abertura é um teclado numérico estilizado, com letras mnemônicas sob cada número, em gradiente diagonal de vermelho para rosa e sem grade de construção sobreposta (img 1206).
- Cada tipo de teclado é mostrado na mesma composição padronizada, com o nome do tipo em cinza no topo, um campo com placeholder logo abaixo e o teclado completo alinhado à base, sem moldura de aparelho, o que permite comparar as variações tecla a tecla (img 1207 a img 1218).
- Os teclados numéricos mudam por detalhes mínimos: asciiCapableNumberPad e numberPad têm grade 3 por 3 com 0 e apagar na última linha, sem letras mnemônicas, sugestões, emoji ou microfone (img 1208, img 1213); decimalPad acrescenta o ponto decimal à esquerda do 0 (img 1209); phonePad traz as letras sob os números e a tecla "+*#" no canto inferior esquerdo, com o 0 centralizado (img 1215).
- O teclado de letras padrão tem sugestões acima das teclas, Shift, apagar, "123", espaço e retorno, com emoji no canto inferior esquerdo e microfone à direita (img 1210); o asciiCapable mantém o layout mas mostra só o microfone, sem emoji (img 1207).
- Teclas de contexto ocupam parte da barra de espaço sem alterar o QWERTY base: "@" e "." no emailAddress (img 1211), "@" e "#" no twitter (img 1216) e ".", "/" e ".com" antes do retorno no URL (img 1217).
- O webSearch troca o retorno cinza por uma tecla azul com seta, sinalizando a ação de busca pela cor e pelo ícone da tecla (img 1218).
- O namePhonePad difere do padrão só pela caixa das letras: aparecem em minúsculas e a tecla Shift fica com contorno vazio em vez de preenchida, o que mostra o estado do Shift pelo preenchimento do glifo (img 1212 comparada com img 1210 e img 1207).
- O numbersAndPunctuation reorganiza as linhas em números de 0 a 9, depois pontuação e moeda, depois mais pontuação com apagar, e oferece a tecla "ABC" para voltar às letras, com microfone e sem emoji (img 1214).
- O uso correto da guia de layout do teclado é mostrado numa tela Account de iPhone: campos Email e Password empilhados e botão preto Sign In, todos visíveis acima do teclado que ocupa a metade inferior, com a marca de check branca em círculo verde numa imagem à parte (img 1219, img 1220).
- Os erros usam a mesma tela em outras posições de rolagem: no primeiro, o Password fica reduzido a uma barra cinza fina e o Sign In some atrás do teclado, marcado com X branco em círculo cinza (img 1221, img 1222); no segundo, os campos ficam livres, mas o Sign In aparece cortado ao meio pela barra de sugestões (img 1223).
- No vídeo de visionOS, o teclado escuro é um painel único e sem moldura, com barra "Text preview", linha de três sugestões e teclas, flutuando sobre uma sala real; posição e tamanho do painel ficam fixos enquanto só o texto e a tecla sob o dedo mudam, e o toque aparece como realce branco na tecla (vídeo, folha 0001, q001 a q009, realce em q005, q006 e q008).
- A sequência vai do painel vazio e sem mãos (q001), às mãos entrando e digitando com vários dedos no ar (q002 a q009), até "Hello" completo com cursor e três variações da palavra em pequenas cápsulas, já sem mãos; entre q010 e q011 a janela fica um pouco mais perto e mais à direita, o que sugere que ela pode ser reposicionada (vídeo, folhas 0001 e 0002).
Divergências registradas: a descrição oficial do vídeo diz apenas que uma pessoa digita num teclado virtual no visionOS, e os quadros mostram também a cena real ao fundo, o texto e as sugestões surgindo progressivamente e o deslocamento da janela; as palavras das sugestões e os fragmentos intermediários de texto só foram lidos de forma aproximada; na img 1217 o microfone não está visível na captura; a img 1219 é uma tela de login concreta, mais específica que a descrição oficial genérica de dois campos e um botão.
<!-- /visual:virtual-keyboards -->

## O que este grupo revela sobre o jeito Apple

1. A escolha de componente é sempre guiada pelo volume e formato do dado, não por preferência estética: pickers versus pull-down buttons versus listas e tabelas (pickers), o limite de cinco a sete segmentos num segmented control (segmented-controls), o limite de cerca de cinco opções antes de trocar radio buttons por pop-up buttons (toggles).
2. Componentes de estado sempre exigem clareza visual redundante, nunca dependente só de cor: toggles pedem diferença visual óbvia além de cor (toggles), checkboxes usam preenchimento e marca de seleção além da cor azul (toggles), sliders preenchem a trilha de cor mas também têm thumb e, no watchOS, glifos de mais/menos (sliders).
3. macOS recebe sistematicamente mais estilos e mais controle manual do que as demais plataformas: combo boxes e image wells só existem em macOS (combo-boxes, image-wells), sliders ganham tick marks e estilo circular só em macOS (sliders), toggles ganham checkbox, radio button e mini switch só em macOS (toggles).
4. Vários controles deste grupo são deliberadamente "mudos" sozinhos e dependem de um parceiro para mostrar o valor: o stepper não exibe valor e precisa de um campo ao lado (steppers), o slider é frequentemente complementado por um campo de texto e um stepper (sliders), o combo box junta texto livre com lista (combo-boxes).
5. Segurança de dado sensível aparece como padrão recorrente, não como exceção: campos de texto seguros para senha (text-fields), campos de dígito seguros para PIN (digit-entry-views), e teclados customizados são bloqueados justamente em campos de texto seguros e de número de telefone (virtual-keyboards).
6. A Apple prefere manter as pessoas no lugar em vez de trocar de tela: pickers devem aparecer em contexto, embaixo ou perto do campo, evitando troca de view (pickers); teclados devem respeitar o keyboard layout guide para não cobrir conteúdo importante (virtual-keyboards).
7. Plataformas sem teclado físico e de interação mais limitada (tvOS, watchOS) recebem instrução explícita para minimizar entrada de texto e preferir listas, botões, ditado ou Scribble em vez de digitação (text-fields, virtual-keyboards, pickers).
8. Onde o sistema pode inferir o tipo de conteúdo, a Apple pede para usar essa inferência em vez de reinventar: number formatter para campos numéricos (text-fields) e keyboardType/textContentType para escolher automaticamente o teclado certo (virtual-keyboards).
9. Liquid Glass aparece como camada de consistência visual mais recente aplicada mesmo a controles auxiliares, como os controles customizados acima do teclado em iOS e iPadOS (virtual-keyboards), mostrando que atualizações de linguagem visual do sistema se propagam para componentes de apoio, não só para telas principais.
10. Grupos de opções mutuamente exclusivas têm um teto informal recorrente ao redor de cinco itens antes de a Apple recomendar um componente mais compacto: radio buttons (toggles), segmentos num iPhone (segmented-controls).

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/color-wells.md, 28 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/combo-boxes.md, 26 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/digit-entry-views.md, 22 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/image-wells.md, 23 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pickers.md, 69 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/segmented-controls.md, 58 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sliders.md, 57 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/steppers.md, 27 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/text-fields.md, 54 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/toggles.md, 74 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/virtual-keyboards.md, 81 linhas lidas, sim, até o fim.

Todos os 11 artigos do grupo foram lidos até o fim num único Read por arquivo, sem truncamento reportado pela ferramenta. Nenhum artigo do grupo é apenas índice de coleção sem texto próprio.
