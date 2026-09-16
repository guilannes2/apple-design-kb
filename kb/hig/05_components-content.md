# Components / Content

## Charts (slug: charts)

### O que governa
Como organizar dados em um gráfico (chart) para comunicar informação com clareza e apelo visual, cobrindo anatomia, tipos de mark, eixos, conteúdo descritivo, cor e acessibilidade.

### Por que
A Apple parte da ideia de que um chart eficaz destaca poucas informações chave de um conjunto de dados para ajudar as pessoas a ganhar insights e tomar decisões, não a exibir todos os dados possíveis. O raciocínio central é hierarquia de atenção: os dados em si devem ser o elemento mais proeminente, enquanto descrições e eixos dão contexto sem competir com eles. Outro fio condutor é que a acessibilidade não é um extra: como todo infográfico, um chart precisa ser totalmente acessível independentemente de como a pessoa percebe o conteúdo, e por isso VoiceOver, Audio Graphs e navegação por teclado/Switch Control recebem tratamento extenso. Por fim, há uma preocupação com honestidade perceptiva dos dados (por exemplo, escolha do limite inferior do eixo Y) para não distorcer a leitura das diferenças entre valores.

### Faça e evite
- Escolha o tipo de mark (bar, line, point) de acordo com a informação que quer comunicar.
- Use bar marks para comparar categorias ou ver proporções de um todo, especialmente quando cada valor representa uma soma.
- Use line marks para mostrar mudança ao longo do tempo e revelar tendências pela inclinação da linha.
- Use point marks para mostrar a relação entre duas propriedades e identificar outliers e clusters.
- Considere combinar tipos de mark quando isso trouxer clareza, como pontos sobre uma linha para destacar valores individuais.
- Use um intervalo (range) fixo no eixo quando limites mínimo e máximo específicos forem significativos para todos os valores possíveis (por exemplo, carga de bateria de 0 a 100%).
- Use um intervalo dinâmico quando os valores possíveis variarem muito e você quiser que as marks preencham a área de plotagem.
- Defina o valor do limite inferior do eixo de acordo com o tipo de mark e o uso do chart; zero funciona bem em bar charts para permitir comparação visual de alturas, mas pode ofuscar diferenças relevantes em outros tipos, como frequência cardíaca.
- Prefira sequências de valores familiares nos rótulos de tick e grid-line (por exemplo, 0, 5, 10) em vez de sequências incomuns (1, 6, 11).
- Ajuste a densidade e o peso visual de grid lines e rótulos ao contexto de uso do chart: excesso de grid lines sobrecarrega visualmente, poucas dificultam estimar valores.
- Escreva descrições (títulos, subtítulos) que expliquem o propósito do chart antes que a pessoa examine os detalhes, especialmente para usuários de VoiceOver e pessoas com certas deficiências cognitivas.
- Resuma a mensagem principal do chart com linguagem simples e direta.
- Em ambientes compactos, maximize a largura da área de plotagem; mantenha rótulos do eixo vertical o mais curtos possível sem perder clareza, e considere descrever unidades em outro lugar (como no título).
- Torne todo chart acessível: forneça accessibility labels para os componentes e considere usar Audio Graphs.
- Permita interação com os dados quando fizer sentido, mas nunca exija interação para revelar informação crítica.
- Amplie a área de toque (hit target) quando as marks forem pequenas demais para alcançar com dedo ou ponteiro, permitindo "esfregar" (scrub) pela área de plotagem inteira.
- Torne um chart interativo navegável por teclado (incluindo full keyboard access) e Switch Control, seja seguindo a sequência linear padrão, seja definindo um caminho lógico customizado via accessibility APIs, seja permitindo mover o foco entre subconjuntos de valores em datasets muito grandes.
- Ajude as pessoas a perceberem mudanças importantes no chart, inclusive por animação, mas complemente com outros sinais para usuários de VoiceOver ou que desativaram animações.
- Alinhe o chart com os elementos vizinhos da interface, por exemplo alinhando a borda inicial (leading) do chart com a de outras views; considere colocar o rótulo de cada grid line vertical no lado final (trailing) e deslocar o eixo Y para o lado final para não ultrapassar a borda inicial.
- Não confie apenas na cor para diferenciar dados ou comunicar informação essencial; complemente com formas ou padrões diferentes.
- Adicione separação visual entre áreas de cor contíguas, como em bar charts empilhados com segmentos coloridos.
- Ao escrever accessibility labels: priorize clareza e abrangência, incluindo contexto (data, localização) e não apenas o valor bruto.
- Evite termos subjetivos como "rapidamente", "gradualmente", "quase" nas descrições; use valores reais.
- Evite formatos ambíguos e abreviações nas descrições de dados (prefira "June 6" a "6/6", "60 minutes" a "60m").
- Descreva o que os detalhes do chart representam, não a aparência deles (por exemplo, não descrever cores usadas para diferenciar séries).
- Seja consistente ao longo do app ao se referir a um eixo específico (por exemplo, sempre mencionar o eixo X primeiro).
- Oculte rótulos visíveis de texto de eixos e ticks das tecnologias assistivas, já que usuários de VoiceOver obtêm essa informação por accessibility labels e Audio Graphs.

### Especificações exatas
O texto não traz números de pt, px, ms, proporções ou tamanhos padrão específicos para charts; as referências numéricas presentes são exemplos de valores de dados (0%, 50%, 100% de carga de bateria; sequência 0, 5, 10; sequência alternativa 1, 6, 11), não especificações de design.

### Diferenças por plataforma
- iOS, iPadOS, macOS, tvOS, visionOS: sem considerações adicionais além das gerais.
- watchOS: em geral, evitar exigir interações complexas com o chart; priorizar informação visível de relance e interações simples quando agregarem valor. Se o app também existir em outra plataforma, considerar usar essa versão para exibir mais detalhes (exemplo citado: o app Heart Rate no watchOS mostra o chart do dia atual, enquanto o Health no iPhone mostra dados de frequência cardíaca em vários períodos e permite examinar marks individuais).

### Ligações com outros artigos
Charting data, Creating a chart using Swift Charts, Marks, Inclusive color, Enhancing the accessibility of a chart, Vision (para VoiceOver), Accessibility, UIAccessibility.Notification (UIKit), NSAccessibility.Notification (AppKit), Swift Charts.

---

<!-- visual:charts -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações abertas (img 0234 a 0245), códigos conferidos; sem vídeo.
- A capa já é um gráfico com dados rotulados: histograma em curva de sino com barras vermelho escuras sobre degradê laranja avermelhado, eixo Y marcado 0, 50 e 100 à direita, horários no eixo X, setas vermelhas de medida para a altura total e a largura do eixo X, e grade tracejada por cima (img 0234).
- O diagrama de anatomia reaproveita o mesmo histograma, agora em azul sobre branco, com chamadas nomeando cada parte: grid line numa linha pontilhada vertical de fundo, plot area na área interna das barras, mark na barra central mais alta, axis na régua vertical de 0 a 100 do lado direito, tick numa marca do eixo X e axis value label num rótulo de horário (img 0235, em sequência a 0234).
- Os três tipos de mark aparecem em dados distintos: barras azuis de passos por dia num mês, eixo Y de 0 a 15.000 e um pico isolado acima de 10.000 perto do dia 26 (img 0236); linha azul com área em degradê abaixo, cotação de 2018 a 2022 com eixo Y de 71 a 182 e tendência de alta (img 0237); linha com um pequeno círculo em cada ponto de dado, de abril a setembro, eixo Y de 50 a 80 e pico em julho (img 0238).
- Eixo fixo no nível de bateria: cartão arredondado com eixo Y sempre de 0% a 100%, barras verdes perto do topo, barras intermediárias em cinza claro decrescendo, duas barras verdes menores no fim e ícones de raio e pausa sobre a faixa superior de algumas barras (img 0239).
- Eixo dinâmico no gráfico de passos: o mesmo cartão com seletor de período D, W, M, 6M e Y e o resumo de média e datas em texto acima; em W, barras laranja por dia da semana e eixo Y terminando em 6.000; em M, barras mais estreitas por dia e eixo Y terminando em 10.000 (img 0240 e 0241).
- No conteúdo descritivo, um cartão escuro traz primeiro o título do alerta de chuva forte e um subtítulo em linguagem simples, e só depois o gráfico de barras azul claras muito finas e numerosas, com eixo X em minutos de agora até 50 minutos (img 0242).
- A cor nunca trabalha sozinha na pressão arterial: sistólica em bolinhas vermelhas na parte de cima e diastólica em losangos pretos e brancos na parte de baixo, na mesma área de plotagem com eixo Y de 50 a 150, e o cabeçalho repete o marcador de forma ao lado de cada faixa de valores (img 0243).
- A barra de armazenamento é uma única barra horizontal dividida em nove segmentos de cores distintas, do vermelho ao cinza claro, cada um separado do vizinho por um fino espaço em branco, com legenda de bolinha colorida e texto abaixo (img 0244).
- Na acessibilidade, um gráfico de linha preta de elevação, com subida e descida totais no cabeçalho, eixo X em milhas e eixo Y em pés, recebe um retângulo de contorno preto cobrindo só cerca do quinto final da rota, o trecho de maior subida, além de um pequeno ponto circular no início do trajeto; as notas leem o retângulo como indicador de foco, provavelmente do VoiceOver (img 0245).
<!-- /visual:charts -->

## Image views (slug: image-views)

### O que governa
Como usar uma image view, que exibe uma única imagem (ou, em alguns casos, uma sequência animada de imagens) sobre um fundo transparente ou opaco, incluindo quando usá-la em vez de símbolos, ícones ou botões de imagem.

### Por que
A intenção central é usar cada componente para seu propósito específico: uma image view serve para exibir imagem, não para receber interação, e a Apple prefere que interatividade fique a cargo de componentes já preparados para isso, como um botão de sistema configurado para exibir imagem. Da mesma forma, para ícones a orientação é preferir SF Symbols ou interface icons em vez de image views, porque símbolos e ícones são vetoriais, coloríveis e podem adotar as cores de destaque (accent colors) escolhidas pela pessoa, o que uma imagem bitmap comum não oferece prontamente. Há também uma preocupação de legibilidade quando texto é sobreposto a imagens, e de performance/consistência quando a image view exibe sequências animadas.

### Faça e evite
- Use uma image view quando o propósito principal da view for simplesmente exibir uma imagem.
- Em casos raros em que a imagem precise ser interativa, configure um botão fornecido pelo sistema para exibi-la, em vez de adicionar comportamento de botão à image view.
- Para exibir um ícone, prefira um symbol (SF Symbols) ou interface icon a uma image view.
- Tome cuidado ao sobrepor texto a imagens: isso pode reduzir tanto a clareza da imagem quanto a legibilidade do texto; garanta contraste entre texto e imagem e considere recursos como sombra de texto ou camada de fundo.
- Em sequências animadas, use um tamanho consistente para todas as imagens; pré-escalar as imagens para caber na view evita que o sistema precise escalar, e quando o sistema precisa escalar, a performance costuma ser melhor se todas as imagens tiverem o mesmo tamanho e formato.

### Especificações exatas
Não há números, medidas, durações ou proporções específicas no texto.

### Diferenças por plataforma
- iOS, iPadOS: sem considerações adicionais.
- macOS: para uma image view editável, usar um image well (suporta copiar, colar, arrastar e usar Delete para limpar o conteúdo); para tornar uma imagem clicável, usar um image button em vez de image view.
- tvOS: muitas imagens no tvOS combinam múltiplas camadas com transparência para criar sensação de profundidade (ver Layered images).
- visionOS: janelas de apps e jogos em visionOS podem usar image views para exibir imagens 2D, estereoscópicas e fotos espaciais; apps que usam RealityKit também podem exibir imagens de qualquer tipo fora de image views, ao lado de conteúdo 3D, ou gerar uma cena espacial a partir de uma imagem 2D existente.
- watchOS: usar SwiftUI para criar animações quando possível; alternativamente, WatchKit pode animar uma sequência de imagens dentro de um elemento de imagem, se necessário (API citada: WKImageAnimatable).

### Ligações com outros artigos
Images, Image wells, Image buttons, SF Symbols, Layered images, visionOS.

---

<!-- visual:image-views -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, com uma única imagem (img 0628) e os outros três quadrantes da grade vazios, código conferido; sem vídeo.
- O quadro é um retângulo de cantos bem arredondados com gradiente de laranja à esquerda para rosa avermelhado à direita, tendo ao centro o glifo clássico de imagem: moldura arredondada branca translúcida com um círculo e uma silhueta de montanhas (img 0628).
- Setas de medida transformam a capa em diagrama de dimensionamento: uma seta dupla horizontal acima marca a largura e uma seta dupla vertical à direita marca a altura do glifo dentro do quadro (img 0628).
- A combinação de placeholder com cotas de largura e altura trata a image view como um contêiner com dimensões próprias, que podem diferir das da imagem que ele carrega (img 0628).
Divergências registradas: a legenda oficial fala só de uma foto estilizada tingida de vermelho e não menciona as setas de medida que a imagem mostra (img 0628).
<!-- /visual:image-views -->

## Text views (slug: text-views)

### O que governa
Como usar uma text view, que exibe conteúdo de texto multilinha e estilizado, opcionalmente editável, em contraste com labels e text fields.

### Por que
A lógica de escolha do componente é a quantidade e a natureza do texto: text views existem para texto longo, editável ou em formato especial, oferecendo mais opções de exibição e entrada de texto do que labels ou text fields. Para pouco texto, a Apple prefere a simplicidade de um label (ou de um text field, se editável). Por trás das recomendações de legibilidade está o princípio de que liberdade de estilização (múltiplas fontes, cores, alinhamentos) não pode comprometer a leitura do conteúdo, daí a recomendação de adotar Dynamic Type e testar com opções de acessibilidade ativadas. A recomendação de tornar texto útil selecionável reflete a ideia de que informação como mensagens de erro ou números de série tem valor prático quando pode ser copiada.

### Faça e evite
- Use uma text view para texto longo, editável ou em formato especial; para pouco texto, use um label ou, se editável, um text field.
- Mantenha o texto legível mesmo usando múltiplas fontes, cores e alinhamentos.
- Adote Dynamic Type para que o texto continue bom quando a pessoa muda o tamanho do texto no dispositivo.
- Teste o conteúdo com opções de acessibilidade ativadas, como texto em negrito (bold text).
- Torne selecionável o texto útil, como uma mensagem de erro, número de série ou endereço IP, para permitir copiar e colar em outro lugar.

### Especificações exatas
Não há números, medidas ou durações específicas no texto.

### Diferenças por plataforma
- macOS, visionOS, watchOS: sem considerações adicionais.
- iOS, iPadOS: exibir o tipo de teclado apropriado; há vários tipos de teclado disponíveis, cada um pensado para facilitar um tipo diferente de entrada, e o teclado exibido ao editar uma text view precisa ser adequado ao tipo de conteúdo.
- tvOS: é possível exibir texto usando uma text view; como a entrada de texto no tvOS é mínima por design, o tvOS usa text fields para texto editável em vez de text views.
- Nota geral de comportamento: em iOS, iPadOS e visionOS, se uma text view for editável, um teclado aparece quando a pessoa seleciona a view. Por padrão, o conteúdo é alinhado à borda inicial (leading) e usa a cor de label do sistema.

### Ligações com outros artigos
Labels, Text fields, Combo boxes, Accessibility, Typography, Virtual keyboards.

---

<!-- visual:text-views -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 1143), código conferido; sem vídeo.
- Sobre gradiente laranja e vermelho, um retângulo rosa claro contém um parágrafo de texto com várias linhas, representando a área de texto multilinha (img 1143).
- Setas de régua cotam o bloco: uma horizontal no topo para a largura e uma vertical à direita para a altura (img 1143).
- A construção é a mesma da abertura de text-fields citada nas notas, e o que muda é o conteúdo de exemplo, um parágrafo inteiro em vez de uma palavra única, o que separa visualmente text view de text field antes de qualquer leitura (img 1143).
<!-- /visual:text-views -->

## Web views (slug: web-views)

### O que governa
Como usar uma web view, que carrega e exibe conteúdo web rico, como HTML incorporado e sites, diretamente dentro do app.

### Por que
O princípio orientador é escopo de uso: uma web view serve para mostrar conteúdo web pontual sem tirar a pessoa do contexto do app (o exemplo dado é o Mail exibindo conteúdo HTML de mensagens), mas não deve virar um substituto de navegador. A razão declarada é que Safari é a forma primária como as pessoas navegam na web, então replicar a funcionalidade de um navegador dentro de outro app é considerado desnecessário e desencorajado. A recomendação de suportar navegação para frente e para trás reflete a expectativa de que, se a pessoa provavelmente vai visitar múltiplas páginas dentro da web view, ela precisa dos mesmos controles básicos de navegação que teria em um navegador.

### Faça e evite
- Suporte navegação para frente e para trás quando apropriado; esse comportamento existe na web view mas não vem ativado por padrão, então é preciso fornecer os controles correspondentes se as pessoas forem visitar múltiplas páginas.
- Evite usar uma web view para construir um navegador. Usar uma web view para permitir acesso breve a um site sem sair do contexto do app é adequado, mas tentar replicar a funcionalidade do Safari é desnecessário e desencorajado.

### Especificações exatas
Não há números, medidas ou durações específicas no texto.

### Diferenças por plataforma
- iOS, iPadOS, macOS, visionOS: sem considerações adicionais.
- tvOS e watchOS: web views não são suportadas.

### Ligações com outros artigos
Webkit.org (link externo citado como relacionado).

---

<!-- visual:web-views -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 1285), código conferido; sem vídeo.
- Sobre gradiente de laranja para vermelho rosado, um retângulo horizontal rosa muito claro fica centralizado e emoldura um ícone de bússola em contorno simples, círculo com ponteiro triangular apontando para dentro (img 1285).
- Setas de dupla ponta cotam o retângulo, uma horizontal acima para a largura e uma vertical à direita para a altura, como no dimensionamento de uma janela ou viewport de conteúdo web (img 1285).
- O ícone temático deixa de ser só símbolo e vira diagrama de dimensionamento; pelas notas, a capa de watch-faces não usa esse recurso e a de wallet só o usa nos diagramas técnicos internos, não na abertura (img 1285).
Divergências registradas: a legenda oficial descreve apenas um ícone de bússola estilizado tingido de vermelho, sem mencionar o retângulo que o emoldura nem as setas de largura e altura que a imagem mostra.
<!-- /visual:web-views -->

## O que este grupo revela sobre o jeito Apple

1. Componente certo para o propósito certo, sem sobrecarregar um componente com função que já existe em outro: image view não deve virar botão (usar botão de sistema em vez disso), ícone não deve ser image view (usar SF Symbols), texto curto não deve ser text view (usar label ou text field), e web view não deve virar navegador (usar Safari). Sustentado por: image-views, text-views, web-views.
2. Recusa explícita a replicar funcionalidade de apps de sistema dentro de apps de terceiros, mesmo quando tecnicamente possível: a orientação de não construir um navegador dentro de uma web view é o exemplo mais direto disso. Sustentado por: web-views.
3. Acessibilidade tratada como requisito estrutural, não acabamento: o artigo de charts dedica uma seção inteira e regras detalhadas de accessibility label, Audio Graphs, VoiceOver e navegação por teclado/Switch Control, tratando isso como parte da definição de "chart bem feito", não como adendo. Sustentado por: charts.
4. Preferência sistemática por dados e conteúdo reais em vez de representações subjetivas ou decorativas: em charts, a orientação de evitar termos subjetivos ("rapidamente", "quase") e de usar valores reais nas descrições, e de não descrever aparência (cor) mas sim o que os dados representam. Sustentado por: charts.
5. Hierarquia visual como princípio recorrente: em charts, os dados devem ser o elemento mais proeminente e descrições/eixos não devem competir com eles; em image-views, a mesma lógica aparece ao alertar que texto sobre imagem pode prejudicar tanto a imagem quanto o texto se não houver cuidado com contraste. Sustentado por: charts, image-views.
6. Adaptação de complexidade por plataforma, reduzindo interação em contextos de tela pequena ou de entrada limitada: watchOS deve evitar interações complexas em charts e preferir informação de relance; tvOS usa text field em vez de text view porque a entrada de texto ali é mínima por design; web views nem existem em tvOS e watchOS. Sustentado por: charts, text-views, web-views.
7. Consistência entre plataformas como valor: os quatro artigos organizam explicitamente uma seção "Platform considerations" que declara, plataforma a plataforma, onde o comportamento padrão muda e onde não muda ("no additional considerations for..."), deixando claro que a regra-base vale a menos que dito o contrário. Sustentado por: charts, image-views, text-views, web-views.
8. Symbols e ícones vetoriais (SF Symbols) são tratados como a via preferida para elementos gráficos pequenos e coloríveis, alinhados às cores de destaque escolhidas pela pessoa, em vez de bitmaps estáticos. Sustentado por: image-views.
9. Precaução ativa contra fazer a pessoa depender só de percepção visual de cor: tanto em charts (não confiar só na cor para diferenciar dados, usar formas ou padrões complementares) quanto na lógica geral de VoiceOver e Audio Graphs, a Apple constrói redundância de canais de informação. Sustentado por: charts.
10. Peso editorial forte em "não exigir interação para informação crítica": charts deixa explícito que interação pode enriquecer a experiência mas nunca pode ser o único caminho para revelar informação essencial, o que ecoa a preocupação de acessibilidade e de robustez para diferentes formas de uso (teclado, Switch Control, VoiceOver). Sustentado por: charts.

## Evidência de leitura
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/charts.md, 99 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/image-views.md, 53 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/text-views.md, 37 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/web-views.md, 25 linhas lidas, até o fim: sim.
