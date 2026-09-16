# wwdc2022 (parte 2)

## Design for Arabic · صمّم بالعربي (id: wwdc2022_110441, 19.5 min)

Base: transcrição e 14 de 14 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2022/110441/.

Apresentador: Mohamed Samir, designer do Apple Design team.

### Tese central

Projetar bem para o público árabe exige tratar o árabe não como uma simples tradução de texto, mas como uma mudança estrutural completa: direção da interface (right to left), tipografia própria do script árabe, iconografia localizada e sistemas numéricos, sendo que grande parte disso já é resolvida automaticamente pelos frameworks nativos da Apple (como SwiftUI) quando o app usa as APIs do sistema.

### O processo de design que a Apple descreve

Na fala, o apresentador descreve o raciocínio de design em etapas:

1. Justificar o investimento: cerca de 660 milhões de pessoas usam o script árabe hoje, tornando-o a terceira escrita mais usada no mundo depois do latim e do chinês, com falantes em mais de 22 países.
2. Entender a direção de leitura: o árabe é escrito da direita para a esquerda, e essa direcionalidade não afeta só o texto, mas o layout inteiro (títulos, parágrafos, colunas, imagens) de cima para baixo e da direita para a esquerda.
3. Pensar em wireframes: a melhor forma de raciocinar sobre a direcionalidade do layout, segundo o apresentador, é transformar as telas em wireframes e decidir quais elementos trocam de lado (da esquerda para a direita) e quais mantêm posição.
4. Mapear o fluxo mental do usuário: ao inverter a direção, a navegação entre páginas também se inverte, como se o usuário folheasse um livro árabe da direita para a esquerda.
5. Revisar componente por componente onde a direcionalidade impacta ou não: conteúdo (imagens, vídeos, fundos) normalmente não deve ser espelhado, mas interação, animação, escalas, paginação, calendários e gráficos com componente de tempo geralmente devem seguir a direção direita para esquerda.
6. Checar relevância cultural, não só linguística: o exemplo do calendário islâmico lunar no app Calendar é citado como algo além da tradução, ligado à cultura do público.
7. Verificar iconografia símbolo a símbolo: perguntar se o símbolo representa uma direção fisicamente motivada (como o ângulo do uso da mão direita na lupa, mantido) ou uma direção ligada à leitura de texto (como as linhas do ícone do Today, invertidas).
8. Checar o sistema numérico correto por país-alvo: como há dois sistemas de numerais árabes em uso hoje, o apresentador recomenda verificar qual predomina no país que o app está mirando, ou suportar ambos.

### Princípios enunciados e o porquê de cada um

- Não inverter conteúdo fotográfico ou de vídeo ao espelhar a UI: o exemplo dado é o sol nascendo a leste no app Weather, que deve permanecer correto independentemente da localização ou do idioma; inverter a imagem quebraria a realidade física representada.
- Alinhar sempre os parágrafos à direita no árabe, porque é a direção natural de leitura do script.
- Manter os ponteiros do relógio na direção física normal mesmo em UI árabe, para corresponder à representação física de um relógio real, enquanto os pontos de progresso do calendário mudam de direção porque representam avanço de tempo lido como texto.
- Usar tracking (espaçamento entre letras) igual a zero em tipografia árabe quando a fonte não for totalmente otimizada, porque a natureza conectada das letras árabes pode quebrar ligações (Kashida) ou criar espaçamentos indevidos se for manipulada como se fosse latim.
- Preferir a fonte de sistema (SF Arabic) sempre que possível, porque ela já resolve automaticamente ligações entre letras, escala óptica e problemas de transparência em palavras.
- Aumentar o tamanho da fonte árabe em relação ao latim quando caixa alta for usada no texto latino, porque o árabe não tem distinção de maiúsculas/minúsculas e visualmente parece menor ao lado de latim em caixa alta.
- Prever espaçamento vertical extra quando houver uso intenso de marcas de vocalização (diacríticos), porque essas marcas tornam o texto árabe ligeiramente mais alto e podem ser cortadas (clipping) se o espaço vertical for insuficiente.
- Checar transparência em texto árabe com cuidado: opacidade aplicada a caracteres individuais pode revelar juntas visíveis entre letras; a fonte de sistema aplica opacidade à palavra ou frase inteira para evitar essa distorção.
- Priorizar símbolos culturalmente e linguisticamente relevantes, não apenas espelhados automaticamente, porque alguns ícones (como a lupa) carregam significado universal ligado ao uso físico (mão direita), enquanto outros (como as linhas de texto do ícone Today) carregam significado ligado à direção de leitura e devem ser adaptados.

### Técnicas concretas de construção de interface

Layout e direção:
- Títulos, botões e a navigation bar devem trocar de ordem e posição em árabe.
- Parágrafos sempre alinhados à direita.
- Carrosséis e elementos deslizáveis fluem da direita para a esquerda, incluindo a interação e a animação (exemplo: carrossel "the weather across the day" no app Weather).
- Escala de temperatura no app Weather: em árabe, a temperatura mais baixa fica à direita e a mais alta à esquerda; o gradiente da escala e o indicador são invertidos para refletir isso.
- Pontos de paginação (pagination dots) fluem da direita para a esquerda, porque a página primária fica mais à direita e a navegação avança para a esquerda.
- No app Calendar, o progresso de datas, meses e anos corre da direita para a esquerda, correspondendo ao funcionamento de calendários físicos no mundo árabe; linhas vermelhas sob certas datas marcam o início de cada mês do calendário lunar islâmico.
- Em Settings, toggles e segmented controls têm design e interação espelhados no layout árabe.
- Em gráficos (charts) com componente de tempo, como o gráfico de uso de bateria, os dias da semana progridem da direita para a esquerda em árabe (o horário mais cedo fica à direita, o mais tarde à esquerda), espelhando o comportamento do calendário; outros gráficos dependem do país e devem ser checados individualmente antes de decidir a direção.

Tipografia:
- SF Arabic é a fonte exclusiva da Apple para árabe, desenhada para ter consistência estilística com a família SF latina em contextos bilíngues, e oferece todos os pesos, de Ultralight a Black.
- Exemplos de uso de pesos citados: o app Clock usa Bold no título, Regular nas cidades e Light nos numerais do relógio; o app Health usa bold, medium e regular em títulos e corpo de texto; o app Weather usa múltiplos pesos em numerais e corpo de texto.
- SF Arabic tem tamanho óptico (optical size): a forma da letra muda de acordo com o ponto usado. Tamanhos grandes (títulos, headings) têm um estilo grotesco contemporâneo alinhado ao restante da família SF; tamanhos pequenos (parágrafos, corpo de texto) priorizam legibilidade e funcionalidade, adicionando angularidade aos terminais e ajustando largura e contraste da estrutura da fonte. O sistema escolhe automaticamente a forma correta conforme o tamanho do ponto.
- Exemplo citado: no App Store Editorial sheet, o estilo "display" é usado no título e "text" nos parágrafos, com árabe e inglês funcionando de forma coesa lado a lado.
- Este ano (2022) a Apple introduziu SF Arabic Rounded, com todos os pesos de Ultralight a Black; exemplo citado: o app Reminders usa SF Arabic Rounded em títulos e corpo de texto, dando um visual mais "prático, ativo ou suave" dependendo do contexto.
- Ajuste de tamanho: ao usar caixa alta em latim, recomenda-se aumentar o tamanho da fonte árabe em 10% para compensar a diferença de volume óptico entre os dois scripts.
- Tracking (espaçamento entre letras): usar 0 de tracking quando a fonte árabe não for totalmente otimizada para espaçamento, ou usar a fonte de sistema, que adiciona a ligação correta entre letras (chamada "Kashida", com comprimentos variáveis para um espaçamento mais orgânico).
- Transparência: a fonte de sistema aplica opacidade à palavra ou frase inteira, e não a cada letra isolada, para evitar juntas visíveis entre caracteres conectados.

Iconografia:
- Mais de 300 símbolos árabes e right-to-left estão disponíveis na biblioteca SF Symbols, incluindo um símbolo de assinatura árabe desenhado exclusivamente e outros de formatação de texto.
- No app SF Symbols é possível checar a seção de localização no painel de informações de cada símbolo para ver a variante local em árabe e em outros scripts não latinos.
- Exemplos de decisões símbolo a símbolo: o ícone do Today tab (linhas alinhadas à direita, seguindo a direção de leitura) foi alterado; a lupa foi mantida igual porque sua direção reflete o ângulo de uso pela mão direita, comportamento da maioria dos usuários no mundo, independentemente da localização; o ícone de escrita mantém a angularidade da caneta mas espelha a direção da escrita; o ícone de alto-falante muda de direção mas mantém a direção do traço (slash), consistente em todo o ecossistema Apple; os pontos de progresso do calendário mudam de direção, mas os ponteiros do relógio permanecem como estão, para corresponder à representação física de um relógio real.
- Todos os símbolos right-to-left e locais aparecem automaticamente no app se as APIs de sistema forem usadas.

Numerais:
- Existem dois sistemas de numerais árabes em uso hoje: o Western Arabic (usado em países árabes do norte da África ocidental, como Marrocos, Argélia e Tunísia) e o Eastern Arabic (usado em alguns países do Levante e do Golfo). Egito e Arábia Saudita usam ambas as versões.
- A escolha entre os dois sistemas acontece automaticamente conforme o país do usuário, e também pode ser definida manualmente pelo usuário.
- Exemplos de apps que refletem essa escolha: Calculator, Calendar e o watch face Typograph, citado como desenhado nas duas formas de numerais.
- Recomendação: se o app inclui numerais, prever suporte às duas formas, ou verificar o país alvo para decidir qual forma é mais adequada.

### Exemplos citados

- App Store: fluxo do story card na aba Today até a página de produto de um app, usado para explicar como transformar telas em wireframes ao adaptar a direção do layout.
- Weather app: ensina que conteúdo de imagem (o sol nascendo a leste) não deve ser espelhado, e que carrossel, escala de temperatura e paginação seguem a direção do idioma.
- Calendar app: ensina o padrão de progressão de datas da direita para a esquerda e a relevância cultural de marcar o calendário lunar islâmico com linhas vermelhas.
- Settings (bateria): ensina que toggles e segmented controls devem ser espelhados em interação e design.
- Gráfico de uso de bateria: ensina como gráficos com componente de tempo seguem a direção do calendário em árabe.
- Pages app: ensina que a navigation bar e os ícones seguem a direção right to left completa.
- Clock, Health e Weather apps: ensinam o uso de diferentes pesos da SF Arabic em hierarquia tipográfica.
- App Store Editorial sheet: ensina o uso combinado de tamanhos ópticos display e text em contexto bilíngue.
- Reminders app: ensina o uso de SF Arabic Rounded para dar um tom mais prático e suave.
- SF Symbols app: ensina onde checar variantes localizadas de ícones.
- App Store tab bar: ensina a lógica de quando espelhar um ícone (Today) e quando não espelhar (lupa).
- Calculator, Calendar e o watch face Typograph: ensinam a coexistência dos dois sistemas de numerais árabes.

### Citações

"Regardless the location or the language" (sobre manter o sol nascendo a leste no app Weather, sem inverter o conteúdo).

"As if they are navigating through an Arabic book from right to left" (sobre o modelo mental de navegação em árabe).

<!-- visual:wwdc2022_110441 -->
### O que as imagens mostram
Base: 14 de 14 folhas de quadros vistas, todos os códigos conferidos.
- Artigo em iPad como primeira demonstração de layout invertido: o título aparece primeiro sozinho num slide de fundo claro (folha 0002, q0012) e depois dentro do layout completo do app, com título grande e parágrafos alinhados à direita, imagem de apoio à esquerda do bloco de texto e barra de ferramentas do topo espelhada, com os controles de navegação do lado direito (q0013 a q0016). Sobre essa tela abre um menu suspenso de opções de exibição alinhado à direita, com itens de lista e um toggle ativado em verde (q0014).
- Wireframe mostrado em três estágios na mesma sequência: as três telas de iPhone com conteúdo real, depois as mesmas telas reduzidas a blocos cinza sem conteúdo, depois o wireframe já espelhado com o conteúdo árabe recolocado, com a barra inferior e os cards trocando de lado (folha 0003, q0022 a q0025). As notas registram que, nesse trecho, a fala descreve títulos, botões e barra de navegação trocando de posição em árabe.
- Par de telas lado a lado em duas molduras de iPhone idênticas, inglês à esquerda e árabe à direita, é o recurso central da sessão, com um rótulo em árabe ao lado de cada par nomeando o assunto em teste (imagem, escala de temperatura, ordem dos dias, calendário islâmico, gráfico ao longo do tempo) (folha 0004, q0028 a q0036). No par do app de clima o nome da cidade e os textos trocam de lado enquanto a ilustração do sol e o ícone de clima ficam exatamente no mesmo canto físico nas duas versões (folha 0003, q0026 e q0027); na folha 0004 o mesmo princípio aparece como um céu azul idêntico dos dois lados, rotulado imagem (q0028).
- Anatomia do cartão de escala de temperatura no par de comparação: barra de gradiente com um número em cada ponta, "18°" à esquerda e "32°" à direita na versão inglesa, e a mesma barra com a ordem trocada na versão árabe (folha 0004, q0030).
- Componentes com eixo de tempo comparados no mesmo formato: calendário anual em grade de 12 meses em 4 linhas de 3, com a ordem dos meses espelhada na versão árabe; uma caixa de aviso sobreposta ao calendário aparece só no quadro seguinte, com o texto "1444 AH, First Day of Islamic Month" na versão inglesa e alguns números de dia em vermelho na árabe; e o gráfico de barras de uso de bateria com as barras e os rótulos de hora invertidos entre as duas versões (folha 0004, q0032 a q0036).
- Slides de tipografia em fundo preto absoluto com um único elemento em branco e uma legenda pequena embaixo, padrão que se repete por várias folhas: a palavra de exemplo ganha uma linha de chamada e a legenda de escrita conectada num quadro que o anterior não tinha; a letra aparece nas quatro formas posicionais rotuladas isolada, inicial, medial e final; e uma grade densa de glifos pequenos ocupa a tela inteira (folha 0005, q0039 a q0043).
- Comparação de volume entre os dois scripts feita com dois retângulos de cor sólida, um por palavra, cada um sublinhado por uma linha fina, com a legenda de pouco espaço entrando só no segundo quadro (folha 0005, q0044 e q0045). Em seguida a mesma palavra árabe recebe as marcas de vocalização e fica visivelmente mais alta que a versão anterior, no mesmo enquadramento (folha 0006, q0046 e q0047).
- Tabela de pesos em coluna dupla: o nome da família latina repetido do mais fino ao mais espesso à esquerda e a família árabe nos mesmos pesos à direita, com rótulos de peso nas extremidades; o par isolado de nomes de fonte no quadro anterior se expande nessa tabela completa (folha 0006, q0052 e q0053). O mesmo formato de tabela reaparece para a variante arredondada, com as terminações de letra mais suaves (folha 0008, q0068), seguido da tela real que a usa (q0069 e q0070).
- Tamanho óptico demonstrado como duas colunas rotuladas "Display" e "Text" com a mesma palavra em escalas diferentes, cada bloco com um marcador circular acima e um rótulo lateral em árabe, e depois a variante de texto ampliada sozinha para expor a angularidade das terminações (folha 0007, q0058 a q0061).
- Medida anotada dentro do slide: o valor de espaçamento entre letras aparece em porcentagem embaixo da frase de exemplo, permanece igual nos três primeiros quadros e cresce a partir do quarto, enquanto as ligações entre as letras se alongam e se rompem e as letras se separam de forma artificial (folha 0009, q0076 a q0080). No quadro seguinte a frase perde opacidade e a palavra do próximo tópico entra como marca d'água por cima, anunciando o assunto antes da fala, que continua com o slide de transparência a 50 por cento (q0081; folha 0010, q0082).
- Ajuste de tamanho entre scripts mostrado com setas: uma seta para baixo ao lado da frase latina em minúsculas e uma para cima ao lado da mesma frase em caixa alta, com a frase árabe ao lado nas duas linhas (folha 0010, q0084 e q0085). Logo depois vem o cartão editorial real da loja nas duas versões, e o quadro seguinte aproxima o rodapé mostrando a aba ativa destacada em azul no lado oposto ao da versão inglesa (q0086 e q0087).
- Comparação ícone a ícone em slides de duas linhas rotuladas inglês e árabe, percorrendo um símbolo diferente por quadro: alguns invertem a orientação, como o documento com linhas de texto, e o ícone de busca aparece com o cabo apontando exatamente para o mesmo lado nas duas linhas, sem inversão (folha 0011, q0094 a q0099). Antes deles, um recorte aproximado da barra de abas do App Store mostra os mesmos ícones espelhados na versão árabe (q0093). O mesmo formato de duas linhas volta num slide único que compara assinatura, lista numerada, letra, numeral e um ícone de formatação de texto; as notas apontam formas totalmente diferentes entre os dois scripts na assinatura, na letra e no numeral, e mesma estrutura no ícone de formatação (folha 0012, q0100).
- Ferramentas e documentação mostradas na própria tela: o app de símbolos aberto num MacBook com barra lateral de categorias à esquerda, grade central de ícones e painel de detalhes à direita com a informação de localização do símbolo selecionado (folha 0012, q0103); e a página de orientações de layout da direita para a esquerda do site de diretrizes da Apple em tela cheia de MacBook, com menu lateral, título grande e mockups de iPhone (folha 0013, q0117; folha 0014, q0118).
- Numerais tratados primeiro como forma e depois como decisão de produto: blocos escuros arredondados tipo tecla, com "123" inteiro que se divide em três blocos e depois vira uma grade de teclado numérico (folha 0012, q0106 a q0108); em seguida os dois sistemas lado a lado com rótulo de cada um, e os lugares onde a escolha aparece, a lista de ajustes com marca de seleção azul, o calendário anual com a mesma grade de meses mudando só o sistema numérico dos dias e dois mostradores de Apple Watch, um laranja e um verde, com os ponteiros sobrepostos aos números grandes (folha 0013, q0109 a q0114).
- Lista de tópicos em árabe do lado direito do apresentador que se acumula item a item e destaca o atual por opacidade e tamanho, reaparecendo antes de cada virada de assunto e sinalizando a seção antes de a fala anunciar (folha 0003, q0019 a q0021; folha 0010, q0090; folha 0012, q0105).
- Encerramento por mosaico: uma grade densa de miniaturas de telas de apps nativos em árabe já aparece ao final do bloco de tipografia (folha 0008, q0072) e a recapitulação final reúne em grade irregular miniaturas de quase todos os exemplos da sessão, de relógios a wireframes, slides de espaçamento, ícones e telas de app (folha 0014, q0119 a q0122); a cartela final é coberta por uma faixa escura que avança da direita para a esquerda sobre o texto "WWDC22" (q0125 e q0126).
Proporção visual: só a folha 0001 é dominada pelo apresentador; nas demais ele aparece em trechos curtos de ligação (por exemplo q0037, q0048 a q0050, q0064 a q0067, q0083, q0115 e q0116) e a maioria dos quadros é slide de tipografia em fundo preto ou captura de interface em moldura de aparelho, com as folhas 0004 e 0011 inteiramente sem apresentador. As molduras variam conforme o tipo de conteúdo: iPad no artigo longo, iPhone na maior parte dos apps, Apple Watch nos mostradores e MacBook nas ferramentas e na documentação.
Divergências ou limites registrados: na folha 0010 as notas anotam que, no slide de caixa alta, o texto árabe aparece do mesmo tamanho visual nas duas linhas, e que a diferença de tratamento está indicada pelas setas e pela legenda, não pelo tamanho efetivamente mostrado. As notas também registram quadros sem mudança visível entre si, q0059 e q0060 na folha 0007, q0084 e q0085 na folha 0010 e q0091 e q0092 na folha 0011, o que limita o que se pode afirmar sobre a animação nesses trechos, e descrevem a mudança do ícone de teclado com relógio (folha 0011) em termos vagos, sem detalhar o que muda. Na folha 0002 as próprias notas divergem sobre o menu de opções de exibição: a descrição da tela o coloca em q0014 e q0015, e a linha de mudança entre quadros diz que ele some de q0014 para q0015.
<!-- /visual:wwdc2022_110441 -->

## O que este grupo revela sobre o jeito Apple

- Localização, para a Apple, não é tradução de texto: é redesenho estrutural do layout, da direção de navegação, da tipografia, dos ícones e dos sistemas numéricos, com decisões caso a caso sobre o que espelhar e o que não espelhar (id: wwdc2022_110441).
- A Apple distingue direção motivada pela física do mundo real (sol, ponteiros de relógio, ângulo da mão) de direção motivada pela leitura de texto, e usa esse critério para decidir o que inverter em right-to-left (id: wwdc2022_110441).
- A companhia investe em tipografia própria e otimizada por script (SF Arabic, SF Arabic Rounded, escala óptica automática) para tirar do desenvolvedor a responsabilidade manual de acertar ligação de letras, espaçamento e transparência (id: wwdc2022_110441).
- Grande parte do trabalho de adaptação para right-to-left é resolvida automaticamente pelos frameworks nativos (SwiftUI e APIs de sistema), o que a Apple usa como argumento para incentivar o uso desses frameworks em vez de soluções customizadas (id: wwdc2022_110441).

## Sem transcrição

Nenhum arquivo deste grupo ficou sem transcrição.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2022_110441.md, 24 linhas lidas, até o fim: sim.
