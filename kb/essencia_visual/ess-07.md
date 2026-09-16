# ess-07: padrões visuais recorrentes (lote de vídeos)

Base: 18 sínteses visuais lidas integralmente, todas do diretório visual_sintese_videos. Cada padrão abaixo aparece em pelo menos dois vídeos.

## O índice da palestra fica na tela como marcador de progresso, com hierarquia feita só por cor e opacidade, item corrente em branco pleno e os demais em cinza
- Evidência: wwdc2019_809 (slide de agenda em duas colunas com dez tópicos, folha 0006 q0047 a q0048, folha 0013 q0112 a q0113, folha 0016 q0144, folha 0020 q0177 a q0178, folha 0024 q0212 a q0213)
- Evidência: wwdc2020_10103 (menu em texto branco sobre preto, "Ideation" na folha 0003 q0019, "Principles" na folha 0005 q0038, "Editing" na folha 0006 q0051, "Creation" na folha 0007 q0055)
- Evidência: wwdc2020_10171 (sumário sempre no mesmo canto direito sobre o vídeo desfocado, folha 0003 q0026 e q0027, reaparecendo nas folhas 0004 a 0010)
- Evidência: wwdc2020_10020 (tela de índice recorrente sempre na mesma posição vertical, folhas 0002, 0003 q0019, 0010 q0090, 0011 e 0013)
- Evidência: wwdc2019_805 (slide de agenda em fundo preto, item corrente em branco bold, folha 0001 q0003 a q0009, reaproveitado no "Summary" da folha 0010)
- Evidência: wwdc2020_10162 (a lista dos três princípios reaparece sobreposta à apresentadora com só o item em foco em branco, folha 0002 q0018, folha 0004 q0029, folha 0005 q0039)
- O que isso ensina sobre construir interface: estado de progresso pode ser comunicado sem badge, marcador, numeração ou barra, só variando a opacidade do mesmo texto; e a posição fixa do bloco na tela é o que faz o leitor reconhecê-lo como bússola em vez de conteúdo novo.

## Listas crescem por acúmulo entre quadros, com o item que acaba de entrar em branco forte e os anteriores rebaixados para cinza
- Evidência: wwdc2020_10019 (acontece em "Switch Control users" folha 0002 q0012 para q0015, "Special considerations" folha 0004 q0033 para q0035, "Challenges for Switch Control" folha 0007 q0056 a q0061, "Best practices" folha 0011 q0094 para q0097)
- Evidência: wwdc2019_810 ("Utility" recebe "Moderation", depois "Focus", depois "Keep it simple", folha 0012 q0100 a q0105)
- Evidência: wwdc2019_809 (as recomendações de menu contextual são reveladas uma por vez, esmaecendo as já ditas, folha 0019 q0170 a q0171)
- Evidência: wwdc2020_10172 (listas de resumo crescem linha por linha, quatro itens na folha 0012 q0104 a q0107 e quatro na folha 0019 q0167 a q0170, nunca passando de quatro frases simultâneas)
- Evidência: wwdc2019_806 (bullets que se acumulam ao lado da captura correspondente na triagem de recursos, folha 0003 q0021 a q0026)
- O que isso ensina sobre construir interface: revelação progressiva não precisa de animação de entrada, basta a mudança de peso visual; e o teto de quatro linhas simultâneas é uma regra de densidade observável, não uma preferência.

## Julgamento de design é ensinado como par no mesmo quadro, duas versões do mesmo componente variando um detalhe, uma com check verde e outra com X vermelho
- Evidência: wwdc2020_10103 (duas variações de layout com furos de fogão folha 0010 q0088 para q0089, dois cartões de dicas folha 0012 q0100, e dois cartões de nota que diferem só por trazer ou não a palavra antes do horário, folha 0012 q0101)
- Evidência: wwdc2019_808 (grade rotulada "fillColor" com X vermelho contra a mesma grade com "systemGrey5" e check verde no mesmo quadro, folha 0007 q0056, e dois cartões modais de alturas diferentes com X e check, folha 0018 q0160 e q0161)
- Evidência: wwdc2019_809 (quatro mockups de sidebar sobre o wallpaper, cada par com cor de seleção diferente e um X vermelho ou check verde abaixo, folha 0009 q0074 a q0075)
- Evidência: wwdc2019_806 (lista de sopas com botão repetido em cada linha marcada com X vermelho, folha 0004 q0033 a q0036, contra a tela de status com um único botão no rodapé e selo verde, folha 0005 q0038 e q0041)
- Evidência: wwdc2020_10145 (lista vertical com selo verde de visto no termo aprovado e X cinza nos rejeitados, aplicada ao nome do serviço folha 0004 q0031, ao perfil folha 0006 q0054 e aos leaderboards folha 0013 q0109)
- O que isso ensina sobre construir interface: a diferença entre acerto e erro fica legível quando só uma variável muda entre os dois exemplares, e o veredito vem como selo colado ao exemplo, não como legenda separada.

## Medida entra como notação gráfica sobre o próprio componente, com números, linhas finas e marcas de canto, e não só como valor dito
- Evidência: wwdc2020_10104 (duas barras de ferramentas empilhadas com 52 e 38 de altura anotados à esquerda, folha 0008 q0065 e q0066; linha fina amarela atravessando o quadro na altura do rótulo como guia de linha de base do slider, folha 0015 q0131; escala tipográfica que ganha etiquetas amarelas com o tamanho em pontos de cada linha, de 26 até 10, folha 0017 q0145 para q0146)
- Evidência: wwdc2020_10103 (linhas finas roxas com marcas de cruz nos cantos medindo a distância dos furos até a borda do widget, comparando margem larga e margem apertada, folha 0010 q0089)
- Evidência: wwdc2020_10145 (faixas de cor horizontais atravessando a tela do jogo com os números 62, 114 e 335 e depois 280 e 91 sobrepostos, folha 0003 q0019 a q0020; marcações de 512 pixels em altura e largura desenhadas em volta do círculo sobre a própria arte do cartão, folha 0008 q0070 a q0072)
- Evidência: wwdc2019_809 (tabela tipográfica com a coluna macOS em 13, 11 e 9 pontos ao lado da coluna iOS que passa a mostrar os valores reais de 26,2 a 7,7 pontos quando o rótulo vira escala de 77 por cento, folha 0012 q0101 a q0103; diagrama do iPad Pro com 2048 e 2736 pixels marcados, folha 0011)
- Evidência: wwdc2019_808 (valores RGB e porcentagem de opacidade anotados por camada de texto, ligados por linha fina a cada elemento do cartão, folha 0004 q0033 a q0036)
- O que isso ensina sobre construir interface: a especificação vive colada ao pixel que ela governa, com uma cor de anotação que não existe na interface real (amarelo, roxo, rosa) para que a marcação nunca seja confundida com o desenho.

## A anatomia de um componente é exposta por linhas de chamada que nomeiam cada zona sobre o próprio mockup
- Evidência: wwdc2020_10172 (linha reta e rótulo em caixa branca apontando "Title", "Subtitle", "Header" sobre a foto de capa, "Action" no botão azul e "App" na linha de atribuição do rodapé, folha 0010 q0087 a q0089, folha 0011 q0092 a q0098, folha 0012 q0103)
- Evidência: wwdc2020_10145 (linhas de chamada rotuladas "Title" e "Description" apontando cada trecho do cartão de conquista, folha 0009 q0076 a q0079)
- Evidência: wwdc2019_808 (o mesmo cartão duplicado, a cópia da direita recebendo nomes de papel ligados por linha aos elementos, LabelColor, SecondaryLabelColor, SeparatorColor, SystemBackground, folha 0005 q0042 e q0043)
- Evidência: wwdc2020_10162 (linha de chamada apontando o halo branco translúcido em volta do ponto azul, folha 0001 q0008, e outra indicando que distância e tempo ao lado do resultado dependem da localização precisa, folha 0002 q0010)
- O que isso ensina sobre construir interface: nomear as zonas de um componente na imagem cria vocabulário compartilhado antes de qualquer código, e o mesmo desenho serve de contrato de conteúdo para quem for preencher cada slot.

## Código aparece emparelhado com a tela que ele produz, crescendo linha a linha enquanto a captura ao lado não muda, e com um realce que se move dentro do bloco
- Evidência: wwdc2020_10093 (blocos crescem da propriedade isolada até a assinatura completa da função, com destaque de sintaxe constante, nomes de propriedade em roxo e valores em vermelho, folha 0006 q0046 a q0051)
- Evidência: wwdc2020_10019 (nas folhas 0007 a 0009 cada trecho de Swift vem ao lado da tela que afeta, e o realce passa do bloco inteiro para o nome da classe sublinhado e depois para a linha de atribuição, folha 0009 q0076 a q0078)
- Evidência: wwdc2020_10104 (o bloco de código cresce de uma para duas e depois quatro linhas mantendo a mesma captura ao lado, folha 0003 q0019 a q0021)
- Evidência: wwdc2019_805 (o bloco cresce em camadas ao lado de um card que não muda, primeiro a criação do intent e a doação, depois as linhas de INImage, o que revela qual acréscimo produz a foto dentro do círculo de sugestão, folha 0007 q0058 a q0060)
- Evidência: wwdc2020_10020 (retângulo cinza claro cobrindo só o trecho em discussão, movendo-se do bloco de fonte padrão para o de tamanho de acessibilidade enquanto a tela do telefone muda junto, folha 0012 q0100 a q0103)
- O que isso ensina sobre construir interface: a única forma honesta de mostrar causa e efeito de uma API é fixar o resultado e variar o código, e o realce parcial é o cursor de leitura que diz onde olhar a cada instante.

## Novidade de API tem selo próprio, um círculo ou etiqueta verde colado ao elemento ou à linha que a introduz
- Evidência: wwdc2019_805 (selo circular verde de novidade sobre o mockup, tanto no modal quanto na visão detalhada da galeria, folha 0004 q0029 e folha 0005 q0038)
- Evidência: wwdc2020_10019 (etiqueta verde ao lado da linha que define a imagem da ação customizada via símbolo de sistema, folha 0009 q0078 a q0081)
- Evidência: wwdc2020_10020 (selo circular verde no canto superior direito do card de anúncio quando a API é nova do ano, folhas 0004 q0036, 0005 q0039, 0009, 0010, 0013, 0015 e 0016)
- O que isso ensina sobre construir interface: um marcador de novidade funciona melhor ancorado ao elemento específico do que ao título da seção, e a mesma cor reservada a esse papel evita competir com os selos de certo e errado.

## Ênfase entre elementos irmãos é feita apagando os outros, sem mudar tamanho, posição ou moldura de nenhum
- Evidência: wwdc2019_805 (dos três cards da StickyNote, o em foco mantém cor plena e os outros dois escurecem, folha 0008 q0066 para q0067)
- Evidência: wwdc2020_10087 (lista de onze gatilhos de contexto em duas colunas em que só três seguem em branco pleno no quadro seguinte, folha 0004 q0031 para q0032; e cartões de previsão que esmaecem enquanto os relevantes seguem em laranja pleno, folha 0014 q0121 a q0125)
- Evidência: wwdc2020_10093 (na tabela de três linhas de API, a linha ativa fica em azul saturado e as demais esmaecidas em cinza escuro, e o realce se move de linha em linha, folha 0004 q0035 para q0036, folha 0005 q0037 a q0041)
- Evidência: wwdc2020_10172 (quatro ícones de loja passam de todos brancos para apenas um em branco e os demais acinzentados, folha 0006 q0049 a q0051)
- Evidência: wwdc2019_806 (o mesmo contraste de autoria de texto feito por opacidade, trecho do sistema apagado e trecho customizado em branco cheio, folha 0013 q0117)
- O que isso ensina sobre construir interface: filtro e foco podem ser expressos sem reflow, o que preserva a memória espacial de quem olha; mudar opacidade custa menos atenção do que mudar geometria.

## O estado é explicado por dois quadros vizinhos da mesma tela, antes e depois, sem texto explicativo entre eles
- Evidência: wwdc2020_10020 (a lista de signos passa de nomes em texto colorido para a mesma lista com um ícone circular colorido à esquerda de cada nome, mantendo a cor e somando a forma, folha 0006 q0050 para q0053)
- Evidência: wwdc2020_10171 (a mesma lista do Messages sem a pílula azul e, no quadro seguinte, com a pílula de largura total no topo empurrando a lista para baixo, folha 0010 q0088 para q0089; e a linha do World Clock parcialmente deslocada com o botão vermelho emergindo por baixo, folha 0005 q0044 para q0045)
- Evidência: wwdc2020_10162 (o ponto azul nítido dá lugar à área circular desfocada no mesmo lugar do mapa, folha 0003 q0022 para q0023; e a linha de favoritos ganha tempo estimado sob cada ícone, folha 0003 q0024 para q0026)
- Evidência: wwdc2020_10103 (o cartão de calendário passa de um evento para dois e depois para a mensagem de que não há mais eventos hoje, folha 0003 q0025 a q0027; e o widget de clima troca de azul claro com sol para azul escuro de chuva com gráfico de barras, folha 0004 q0032 para q0034)
- Evidência: wwdc2020_10093 (o fundo do app muda de escuro para esverdeado quando o modo guia é ativado e os pontos de costura se acumulam ao longo da linha tracejada, folha 0014 q0119 a q0123)
- O que isso ensina sobre construir interface: desenhar o estado intermediário e o estado final lado a lado revela o que a transição precisa carregar, e mostra estados vazios e de exceção como parte do componente, não como afterthought.

## Nenhuma tela aparece como captura crua: toda interface vem dentro de moldura simulada de aparelho, com barra de status fixa
- Evidência: wwdc2020_10087 (moldura de iPhone com barra de status simulada em 9:41, isolada sobre fundo preto quando o ponto é o componente e em contexto de tela de bloqueio, dock ou tela inicial quando o ponto é a integração, observação consolidada na síntese e visível na folha 0003 q0021 a q0024)
- Evidência: wwdc2020_10088 (toda tela de app ou de sistema dentro de moldura simulada de iPhone ou de laptop, mesmo quando o conteúdo é só um menu ou uma notificação)
- Evidência: wwdc2020_10172 (mockup semitransparente de iPhone sobreposto a fotografia do contexto físico em café, estacionamento, loja, restaurante e mirante, folhas 0014 a 0016 q0119 a q0139)
- Evidência: wwdc2020_10171 (mockups de tela do Watch dominam as folhas 0002 a 0012, inclusive nas justaposições de dois relógios)
- O que isso ensina sobre construir interface: a moldura declara a escala real do alvo e impede que a composição do slide seja confundida com a tela; e manter o relógio sempre no mesmo horário elimina uma variável irrelevante de quadro para quadro.

## Comparação lado a lado no mesmo quadro é o recurso padrão para provar diferença, seja entre modos, tamanhos, aparelhos ou estados
- Evidência: wwdc2019_808 (pares de mockups de iPhone claro e escuro com os nomes das camadas ligados às áreas exatas, folha 0006 q0048 a q0052; dois iPhones rotulados "Base" e "Elevated" com o segundo mais claro, folha 0009 q0080)
- Evidência: wwdc2020_10145 (a mesma estrutura de três cartões repetida em telefone, tablet, laptop e televisão dentro da mesma folha, com o primeiro cartão ganhando realce de foco só na versão de TV, folha 0005 q0041 a q0042)
- Evidência: wwdc2020_10103 (clima compacto só com a condição atual ao lado do clima grande com previsão de seis dias, folha 0009 q0080 para q0081; e tempo de uso resumido ao lado da versão grande com barras por hora, folha 0010 q0083 para q0084)
- Evidência: wwdc2020_10104 (três janelas do Mail com o mesmo layout e escalas crescentes de texto e ícone, folha 0018 q0157 e q0158; dois sliders com e sem marcações, folha 0015 q0128)
- Evidência: wwdc2019_806 (HomePod com balão de fala ao lado do iPhone mostrando a versão visual da mesma pergunta, folha 0010 q0089 e q0090)
- Evidência: wwdc2019_809 (duas instâncias da mesma janela de fotos, a inativa com a sidebar perdendo nitidez e a ativa nítida, com os rótulos trocando de lado entre quadros, folha 0008 q0070 a q0072)
- O que isso ensina sobre construir interface: qualquer decisão de densidade, modo ou plataforma deve ser avaliada com as duas versões visíveis ao mesmo tempo, porque a diferença real só aparece na justaposição.

## O mesmo template de componente é reaproveitado entre apps e domínios diferentes, e a identidade do app entra só pelo ícone, pelo nome e pela cor
- Evidência: wwdc2019_805 (o mesmo card de ação aparece em dois apps fictícios diferentes sem variação de estrutura, folhas 0002 e 0008)
- Evidência: wwdc2020_10071 (os cartões de confirmação repetem um template único entre domínios, folha de cantos arredondados, título, corpo com o dado relevante e dois botões de texto na base, o neutro à esquerda e o de ação à direita, folha 0003 q0024, folha 0004 q0033, folha 0005 q0042, folha 0007 q0059)
- Evidência: wwdc2020_10172 (o checkout com Apple Pay reaparece com composição quase idêntica em contextos diferentes, folha 0014 q0121, folha 0015 q0134, folha 0018 q0162; e o prompt de conversão para o app completo é o mesmo cartão horizontal com ícone, nome, subtítulo e botão à direita)
- Evidência: wwdc2020_10145 (os três tipos de conquista ficam lado a lado e a diferença está inteiramente dentro do círculo central, cadeado, anel percentual e interrogação, enquanto título e descrição seguem o mesmo template, folha 0008 q0067; e o mesmo cartão traduzido para alemão mantém o layout idêntico, folha 0009)
- Evidência: wwdc2020_10088 (o menu de compartilhamento aparece com a mesma anatomia, avatares circulares acima da fileira de ícones de canal, ancorado a uma tela de fotos num iPhone e depois a uma janela de calendário num laptop, folha 0003 q0022 para q0023)
- O que isso ensina sobre construir interface: a personalidade de um app deve caber nos slots do sistema (ícone, cor, imagem, texto) e não no redesenho da estrutura, e um layout que sobrevive à tradução para outro idioma é a prova de que os slots foram dimensionados certo.

## Baixa fidelidade vem antes do conteúdo real: wireframe, forma vazia rotulada ou esboço a lápis ocupando o lugar da tela final
- Evidência: wwdc2020_10103 (forma arredondada vazia rotulada "Small" e forma vazia maior rotulada "Large", cada uma depois substituída pelo widget real preenchido, folha 0007 q0059 a q0062, folha 0008 q0064 para q0065; e grade de quadrados arredondados vazios com dois slots centrais contornados em branco mais grosso, folha 0007 q0058 para q0059)
- Evidência: wwdc2019_809 (wireframe azul de baixa fidelidade com retângulos marcados por X para conteúdo e linhas finas para texto, primeiro com uma única área vazia e depois com coluna lateral e duas áreas, folha 0011 q0094 a q0099)
- Evidência: wwdc2020_10071 (maquetes com blocos e barras cinza no lugar de conteúdo real, incluindo esqueleto de carregamento na tela de álbum e placeholders em grade na busca, folha 0006 q0047 a q0052)
- Evidência: wwdc2020_10093 (esboço a lápis sobre papel, silhueta de iPad com teclado, servindo de fundo para o título de abertura de tópico, folha 0002 q0010 para q0011)
- Evidência: wwdc2019_806 (o roteiro de conversa aparece como artefato físico, folha de papel datilografada que vira duas e depois três folhas sobrepostas conforme mais caminhos são considerados, folha 0009 q0074 a q0079)
- O que isso ensina sobre construir interface: discutir encaixe, proporção e fluxo com a forma vazia evita que a conversa vire discussão de conteúdo, e o estágio de rascunho é mostrado como parte legítima do processo, não escondido.

## A ferramenta real aparece na tela, com sua cromia e seus painéis, em vez de ilustração do que a ferramenta faz
- Evidência: wwdc2020_10093 (Xcode em tema claro com navegador de arquivos à esquerda e uma faixa rosa clara marcando a área recém editada, presente em todas as capturas do editor, folhas 0008 a 0010 e 0013 a 0015)
- Evidência: wwdc2020_10020 (Asset Catalog do Xcode com barra lateral, preview central e painel de atributos evoluindo de uma variante do símbolo para duas e depois quatro, folha 0008 q0070 a q0072 e folha 0009 q0081; e a calculadora de contraste com swatches e valores RGB, folha 0009 q0074)
- Evidência: wwdc2020_10104 (Interface Builder com hierarquia, canvas e inspetor de tamanho, folha 0003 q0022 a q0027; catálogo de objetos com itens arrastáveis, folha 0010 q0082 a q0084; catálogo de assets com o quadrado de cor de destaque, folha 0013 q0112)
- Evidência: wwdc2019_808 (app de catálogo de símbolos com nomes sob cada glifo, folha 0016 q0136 e q0137, seguido de uma ferramenta de design com painel de camadas onde o controle de cinco estrelas é editado, q0138 a q0142)
- Evidência: wwdc2019_809 (páginas reais da documentação abertas no navegador dentro da apresentação e uma janela de ferramenta de design com biblioteca de componentes em seções colapsáveis, folha 0017 q0146, folha 0024 q0209, folha 0025 q0217 a q0219)
- O que isso ensina sobre construir interface: mostrar onde exatamente no aplicativo o ajuste acontece encurta a distância entre entender e fazer, e expõe detalhes que a fala nunca menciona, como o indicador de edição recente no editor.

## Diagramas de caixa e linha traduzem relação de código ou de contexto em desenho, antes ou ao lado do exemplo concreto
- Evidência: wwdc2020_10088 (uma barra verde rotulada com uma ação do app ligada por linha vertical fina a uma barra azul escura do sistema, que no quadro seguinte se desdobra em três barras de ações distintas ligadas à mesma barra, folha 0002 q0013 para q0014)
- Evidência: wwdc2020_10087 (cartões laranja com dia, hora e local ligados por linha fina à tela de iPhone correspondente, com os dois lados mudando em conjunto entre quadros, folha 0004 q0034 a q0036; e o cartão de intent com três campos ligado por linha pontilhada à tela de calendário gerada, folha 0015 q0129 a q0132)
- Evidência: wwdc2020_10093 (cartão de composição com dois blocos azul claro unidos por sinal de mais, cada um com a linha de código correspondente à direita, folha 0006 q0053 e folha 0007 q0055 a q0060)
- Evidência: wwdc2020_10104 (hierarquia de um controlador de janela ligando a um controlador de split view e a dois controladores de view, folha 0003 q0026 e q0027; e um retângulo verde externo com outro interno mais claro e setas duplas nas quatro bordas, folha 0011 q0098)
- Evidência: wwdc2019_805 (a saída de uma ação desenhada como bloco azul sólido com quatro propriedades empilhadas, ligado ao card de origem por seta vertical simples, folha 0008 q0067 para q0068)
- O que isso ensina sobre construir interface: quando a relação entre duas coisas é o assunto, o desenho abstrato explica melhor que a tela real, e pode ser reaproveitado depois com o conteúdo trocado para provar que a regra é geral.

## Componentes e glifos são isolados sobre fundo preto, sem nada em volta, quando o assunto é a anatomia deles
- Evidência: wwdc2020_10104 (botão pop-up com preenchimento azul, slider com trilho azul antes do indicador e cinza depois, e controle segmentado com o segmento ativo em branco sobre cinza escuro, folha 0012 q0105 e q0106)
- Evidência: wwdc2020_10086 (ícone do Siri isolado sobre fundo preto, esfera com gradiente radial, folha 0001 q0007 para q0008; e o símbolo de compartilhar em contorno fino branco isolado ao lado do apresentador, folha 0002 q0017 para q0018)
- Evidência: wwdc2020_10171 (o menu que o botão abre é mostrado primeiro no contexto da tela e depois isolado sobre fundo preto, folha 0006 q0053 e q0054, folha 0007 q0057)
- Evidência: wwdc2019_808 (o grupo de controles padrão, switch, stepper, segmentado e slider, repetido em enquadramentos diferentes com o slider em posições distintas, folha 0012 q0104 a q0108)
- Evidência: wwdc2020_10071 (as três formas de acionar o assistente viram três botões cinza escuro alinhados com espaçamento igual, ícone branco centralizado e legenda abaixo, sem nenhum outro elemento sobre o fundo preto, folha 0001 q0009)
- O que isso ensina sobre construir interface: tirar o componente do contexto é o que permite julgar peso de traço, preenchimento e espaçamento interno; o fundo preto neutro evita que a cor do ambiente contamine a leitura.

## Cor carrega papel fixo na interface mostrada: azul para o que é editável ou acionável, vermelho para destrutivo, verde para confirmado
- Evidência: wwdc2019_805 (frase resumo com os parâmetros em azul sublinhado, e o campo ainda não preenchido com fundo cinza claro e borda pontilhada, folha 0002 q0013 a q0018)
- Evidência: wwdc2020_10171 (vermelho reservado ao destrutivo nas folhas 0005 e 0010, azul para a mensagem nova e roxo para a nota nova na folha 0002 q0012 e q0016, e a opção aceita em verde com marca de seleção na folha 0009 q0080 para q0081)
- Evidência: wwdc2019_808 ("Delete Draft" em vermelho no topo do action sheet, separado por linha fina, folha 0018 q0158, com o item destrutivo do menu contextual só ganhando vermelho na folha 0022 q0192)
- Evidência: wwdc2020_10087 (valor editável em azul no formulário de atalho, com botão primário azul cheio no rodapé, folha 0009 q0073 a q0076)
- Evidência: wwdc2020_10162 (os controles ligados a localização usam o azul do sistema e o halo é branco translúcido, nenhum deles usando o amarelo dos pontos de categoria nem as cores dos favoritos, folhas 0001, 0003 e 0004)
- O que isso ensina sobre construir interface: reservar cores por função, e não por seção, é o que deixa um elemento novo ser lido sem legenda; e uma tela só consegue isso se as outras cores em circulação forem mantidas fora desse papel.

## A hierarquia de botões é constante: preenchido para a ação primária, texto puro ou neutro para a secundária, e largura total quando o botão fecha a tela
- Evidência: wwdc2020_10087 (botão primário laranja cheio e botão secundário só em texto na confirmação de compra, folha 0003 q0021 a q0024)
- Evidência: wwdc2020_10071 (dois botões de texto na base do cartão, o neutro à esquerda e o de ação à direita, repetidos em quatro domínios diferentes, folhas 0003 a 0007)
- Evidência: wwdc2020_10172 (pílula azul preenchida no cartão, com o rótulo mudando conforme o tipo de experiência mas o desenho igual, folha 0011 q0098 e folha 0012 q0102; e o botão preto de pagamento ocupando a largura do rodapé, folha 0014 q0121)
- Evidência: wwdc2019_806 (formulário do sistema com campo de frase preenchido e botão azul de largura total no rodapé, folha 0006 q0054 e folha 0007 q0056)
- Evidência: wwdc2020_10020 (botão pill azul sólido como chamada primária na tela real de produto, com metadados em três colunas abaixo, folha 0004 q0028 a q0034)
- O que isso ensina sobre construir interface: a diferença entre primário e secundário é resolvida por preenchimento, não por cor diferente nem por tamanho; e a largura total funciona como sinal de que aquele botão encerra o fluxo.

## Uma frase única ganha cartão próprio, tipografia grande centralizada em fundo preto, sem nenhum outro elemento
- Evidência: wwdc2020_10019 (cartão com uma frase só para fixar a tese de que bom suporte de leitor de tela já entrega quase todo o resto, folha 0005 q0040 para q0041)
- Evidência: wwdc2020_10162 (perguntas de enquadramento em texto grande centralizado sobre preto, em dois quadros seguidos que trocam apenas a pergunta, folha 0002 q0014 para q0015)
- Evidência: wwdc2020_10171 (cartão de texto centralizado e sozinho na abertura, folha 0001 q0009, com o mesmo tipo de frase depois migrando para o lado do mockup do relógio, folha 0002 q0011 e q0012)
- Evidência: wwdc2020_10088 (cartelas de dado com número grande em negrito branco, muito maior que a legenda curta centralizada abaixo, sempre sobre a mesma fotografia desfocada, folha 0004 q0031 a q0033)
- O que isso ensina sobre construir interface: quando uma única afirmação precisa ficar, ela vira tela inteira e perde toda a companhia; a escala tipográfica sozinha faz o trabalho de ênfase.

## Texto conceitual é sobreposto direto ao vídeo do apresentador, sem cartão de fundo, mudando de alinhamento conforme o enquadramento
- Evidência: wwdc2020_10086 (frases de título em tipografia branca sem serifa sobre a filmagem ao vivo, trocando entre alinhamento à esquerda e à direita conforme a pose da pessoa em cena, folha 0001 q0006 para q0007, folha 0002 q0014 para q0015, folha 0003 q0020 a q0024)
- Evidência: wwdc2020_10088 (palavras curtas em branco sem serifa alinhadas à direita, uma de cada vez conforme a fala avança, funcionando como legenda de ênfase sem slide separado, folha 0001 q0009, folha 0002 q0010 e q0011)
- Evidência: wwdc2020_10071 (palavras de abertura de bloco, duas como cartela isolada e duas sobrepostas ao plano da apresentadora, com a cartela crescendo em dois tempos, a palavra em amarelo e o restante em branco, folha 0002 q0017 para q0018, folha 0008 q0068, folha 0009 q0076)
- Evidência: wwdc2019_810 (a palavra de conceito em corpo grande sobreposta em transparência ao apresentador e ao mockup, folha 0008 q0066 e q0067)
- O que isso ensina sobre construir interface: sobreposição translúcida mantém o contexto vivo por trás do texto, e o alinhamento do texto passa a ser função da composição da imagem, não uma constante do template.

## O apresentador convive com a interface no mesmo quadro, como miniatura no canto ou em quadro duplo, em vez de cortar entre um e outro
- Evidência: wwdc2020_10071 (a partir do meio do vídeo a edição passa a usar quadro duplo, retrato pequeno da apresentadora em um canto e a tela de iPhone ampliada ao lado, folha 0006 q0047 e q0048, folha 0008 q0064 a q0066, folha 0009 q0078 e q0079)
- Evidência: wwdc2020_10093 (slide de título com miniatura de vídeo do apresentador no canto inferior direito, folha 0001 q0001 a q0009)
- Evidência: wwdc2020_10162 (a apresentadora aparece várias vezes só como miniatura no canto sobre a tela)
- Evidência: wwdc2020_10104 (nas cartelas de abertura e fechamento o apresentador aparece em janela de vídeo no canto, não sozinho no quadro inteiro, folhas 0001 e 0021)
- Evidência: wwdc2019_805 (o apresentador aparece quase sempre em miniatura sobreposta ou ao lado da tela ampliada)
- O que isso ensina sobre construir interface: manter a fonte humana e o artefato visíveis ao mesmo tempo evita a perda de contexto do corte, e o canto ocupado pela miniatura vira espaço reservado que o layout da tela precisa respeitar.

## Troca de apresentador e de cenário sinaliza troca de bloco antes de qualquer cartela
- Evidência: wwdc2020_10087 (quatro apresentadores, cada um em locação própria, do estúdio interno ao exterior com estrada e ao corredor envidraçado, com cada troca de rosto e cenário antecipando a troca de subtópico, folhas 0006, 0012 e 0015, nas transições q0051 para q0052, q0102 para q0103 e q0134 para q0135)
- Evidência: wwdc2020_10172 (o primeiro apresentador fica num estúdio branco com poltronas e um puff laranja nas folhas 0001 a 0012, e a segunda apresentadora aparece num ambiente de vidro com luz natural, aberto por cartela preta com crédito nominal e miniatura de vídeo no canto, folha 0013 q0109 a q0110)
- Evidência: wwdc2020_10145 (o vídeo alterna trechos dos dois apresentadores em close entre as telas do jogo e os slides de especificação)
- O que isso ensina sobre construir interface: mudança de contexto pode ser anunciada por uma variável ambiental constante, e não por rótulo; quem assiste percebe a virada antes de ler qualquer coisa.

## Fotografia real de hardware, de pessoa ou de ambiente entra como argumento, não como ilustração decorativa
- Evidência: wwdc2019_810 (o motor háptico fotografado dentro do iPhone aberto com rótulo sobreposto ao componente, folha 0002 q0011 a q0016; e macros de engrenagens douradas de relojoaria levando ao close da coroa serrilhada com anel vermelho, folhas 0009 e 0010 q0080 a q0086)
- Evidência: wwdc2020_10019 (sequência documental do usuário em cadeira de rodas motorizada percorrendo a trilha até a cachoeira, close do switch bucal e visor da câmera do iPhone, folha 0003 q0019 a q0025; e uma mão pressionando dois botões rotulados ao lado do jogo rodando, folha 0010 q0082 a q0085)
- Evidência: wwdc2020_10172 (o código impresso num totem triangular branco sobre a mesa de uma cafeteria real, folha 0005 q0040 a q0045, e mockups trazidos por cima de fotos de contexto físico, folhas 0014 a 0016)
- Evidência: wwdc2020_10020 (a tela do mapa estelar aparece sendo segurada e inclinada na mão de uma pessoa para demonstrar efeito de movimento, folha 0013 q0114 a q0116)
- O que isso ensina sobre construir interface: quando a decisão depende de material, força física ou situação de uso, a imagem do mundo real prova o que nenhum diagrama prova, e mostra a restrição concreta que a interface precisa respeitar.

## Contorno tracejado é a convenção para marcar o que é área, região ou vazio, nunca um elemento sólido da interface
- Evidência: wwdc2020_10093 (moldura de borda tracejada sobreposta a capturas reais, primeiro cobrindo todo o conteúdo para explicar a região padrão e depois limitada a uma faixa horizontal para a região customizada, folha 0011 q0099 e folha 0012 q0101 e q0102, com a mesma marcação em amarelo ao redor de uma fileira contínua de amostras na folha 0017)
- Evidência: wwdc2019_805 (parâmetro ainda não preenchido com fundo cinza claro e borda pontilhada em volta do texto, marcando o campo como editável e vazio sem rótulo extra, folha 0002 q0013 para q0014)
- Evidência: wwdc2020_10172 (o ícone do App Clip é o ícone normal do app com uma borda circular tracejada acrescentada ao redor, mostrado em comparação rotulada lado a lado, folha 0002 q0017 a q0018, e repetido no ícone final do encerramento, folha 0019 q0170)
- O que isso ensina sobre construir interface: o tracejado comunica limite sem sugerir superfície, o que o torna adequado tanto para campo vazio quanto para área de captura, e é essa ausência de preenchimento que impede confundi-lo com um controle.

## Gesto e área de toque são anotados como círculo translúcido com seta, incluindo o meio do movimento e não só o resultado
- Evidência: wwdc2019_808 (o gesto de dispensar a sheet anotado quadro a quadro com um círculo azul semitransparente e seta que muda de posição sobre o texto rolável, mostrando rolagem e dispensa como duas etapas do mesmo puxão, folha 0018 q0154 a q0156)
- Evidência: wwdc2019_809 (um botão azul envolvido por círculo translúcido maior que o próprio controle representando a área de toque, com um botão pequeno e cursor de mouse logo abaixo, folha 0004 q0031 a q0032; e o remapeamento em pares, círculo azul ao lado do cursor de seta, folha 0015 q0131 a q0135)
- Evidência: wwdc2020_10171 (a lista aparece com a linha parcialmente deslocada e o botão vermelho emergindo por baixo, registrando o meio do gesto e não só o resultado, folha 0005 q0044 para q0045)
- Evidência: wwdc2019_806 (seta com rótulo apontando para o cartão inteiro para especificar que ele é um botão único, com a câmera se aproximando até a anotação ocupar a tela, folha 0014 q0122 a q0125)
- O que isso ensina sobre construir interface: a área tocável é maior que o desenho do controle e precisa ser especificada como tal, e mostrar o quadro intermediário do gesto é o que revela se o feedback durante o movimento foi projetado.

## A mesma vinheta de marca abre e fecha, e a peça de encerramento repete exatamente a de abertura
- Evidência: wwdc2020_10019 (still do laptop com adesivos e o avatar animado ao lado na abertura, repetido depois do logotipo do evento no encerramento, folha 0001 q0002 e q0003, folha 0013 q0109 a q0111)
- Evidência: wwdc2020_10071 (a mesma tampa de notebook com adesivos filmada em dois ângulos na abertura e em close no último quadro, folha 0001 q0002 e q0003, folha 0009 q0081, folha 0010 q0082)
- Evidência: wwdc2020_10103 (a moldura de marca com laptop fechado e logotipo do evento na folha 0001 q0002 a q0004 e de novo na folha 0012 q0103 a q0105)
- Evidência: wwdc2020_10162 (a mesma composição do laptop com adesivos na folha 0001 q0001 a q0003 e nas folhas 0006 e 0007)
- Evidência: wwdc2020_10086 (a mesma peça filmada de dois ângulos diferentes, com o encerramento repetindo a composição usada em outro vídeo do mesmo lote, folha 0001 q0002 e q0003, folha 0006 q0046 a q0048)
- O que isso ensina sobre construir interface: uma moldura idêntica nas duas pontas fecha a peça e cria reconhecimento entre itens de uma mesma série, com custo zero de produção porque é literalmente o mesmo material.

## Símbolos do sistema são tratados como tipografia, com peso de traço uniforme, grade por categoria e teste de escala ao lado de uma letra
- Evidência: wwdc2019_808 (parede de glifos em perspectiva e depois grade frontal organizada por categoria com peso de traço uniforme, folha 0015 q0127 e q0128; e o símbolo de compartilhar usado como corpo de prova de alinhamento com texto, com cursor piscando ao lado e repetição em tamanhos crescentes, q0130 a q0135)
- Evidência: wwdc2020_10020 (grade densa de símbolos em preto e branco organizada em linhas por tema, todos com o mesmo peso e alinhamento regular, e uma prancha de teste em fundo branco com uma letra de referência à esquerda e o mesmo símbolo repetido em três tamanhos crescentes por linha, folha 0005 q0042 e q0045)
- Evidência: wwdc2020_10104 (etiqueta amarela apontando um ícone da barra de ferramentas com tamanho em pontos, peso e escala escritos, folha 0018 q0155 e q0156; e duas caixas sobrepostas ao mesmo glifo, uma amarela cobrindo toda a área da imagem e outra azul menor dentro dela, separando retângulo total de retângulo de alinhamento, folha 0020 q0172)
- O que isso ensina sobre construir interface: símbolo tem métrica própria (peso, escala, caixa de alinhamento) que precisa ser casada com a do texto vizinho, e o teste ao lado de uma letra de referência é o método simples de verificar isso em cada tamanho.

## Achados de fonte única

- Escala tipográfica entre plataformas resolvida por um fator único: a coluna macOS com 13, 11 e 9 pontos ao lado da coluna iOS que só ganha valores quando o rótulo vira escala de 77 por cento, com 26,2 no título grande e 7,7 na legenda menor, e a mesma escala depois demonstrada dentro de uma ferramenta de design com os indicadores de largura e altura em 77 por cento (wwdc2019_809, folha 0012 q0101 a q0108). A ênfase se desloca em seguida para os estilos menores, marcando em negrito exatamente os tamanhos tratados como arriscados (folha 0013 q0110 a q0111).
- Altura de barra de ferramentas dada em número na própria comparação, 52 para o estilo unificado e 38 para o compacto, com ícones visivelmente maiores na primeira (wwdc2020_10104, folha 0008 q0065 e q0066).
- Escala de opacidade de texto em quatro níveis empilhados, título, subtítulo, placeholder e desabilitado, cada linha visivelmente mais clara que a anterior e sempre na mesma ordem em folhas diferentes (wwdc2019_808, folha 0005 q0045 e folha 0006 q0046 e q0047).
- Hierarquia de fundo com nomes por camada anotados sobre a tela, base, secundária e terciária na lista simples, e a variante agrupada com seus dois níveis próprios, tudo em par de mockups claro e escuro (wwdc2019_808, folha 0006 q0048 a q0052).
- Quatro níveis de material translúcido sobre um fundo laranja em degradê, com parte dos cartões apagada em quadros sucessivos para tornar a gradação de opacidade visível, e depois preenchidos com rótulos de vibrância em quatro níveis para texto e preenchimento (wwdc2019_808, folha 0011 q0092 a q0099).
- Tom de superfície elevada provado por comparação: o painel direito do iPad escurece em dois passos ao ganhar divisória, dois iPhones rotulados base e elevada com o segundo mais claro, e o app em slide-over mais claro que o app de fundo (wwdc2019_808, folha 0009 q0077 a q0081).
- Teste de contraste mostrado como medição com número na tela: dois painéis, claro e escuro, cada um com a razão ao lado, o valor reprovado riscado com X vermelho e o aprovado com check verde (wwdc2019_808, folha 0008 q0066 a q0069).
- Calculadora de contraste em estilo macOS com swatch de texto e de fundo, valores RGB abaixo de cada um, controle de tamanho de texto e o resultado grande de 4,5 para 1 com selo triangular amarelo informando quais tamanhos e pesos aquela razão atende (wwdc2020_10020, folha 0009 q0074 e q0075).
- Espectro de perda de visão demonstrado com quatro colunas da mesma fotografia tratada com filtros progressivos, da imagem nítida à totalmente escura, e a coluna sem visão recebendo destaque só por contorno branco porque não há conteúdo a realçar (wwdc2020_10020, folha 0001 q0009 e folha 0002 q0010).
- Notação gráfica inventada para o que não se vê: onda senoidal contínua, pico único de transiente, o mesmo transiente reduzido a retângulo azul sólido e três formas que formam o espectro de nitidez, gota arredondada, barra e triângulo, reaproveitadas como sistema fixo ao longo de todo o vídeo (wwdc2019_810, folha 0003 q0019 a q0026, folha 0013 q0111, folha 0015).
- Duas trilhas alinhadas no mesmo eixo de tempo, som acima e resposta tátil abaixo, com uma linha vertical vermelha fina marcando o ponto de referência, recurso repetido nas folhas 0006, 0013, 0014 e 0015 (wwdc2019_810).
- Eixos cartesianos com intensidade de 0,0 a 1,0 na vertical e nitidez de 0,0 a 1,0 na horizontal, com as três formas posicionadas ao longo do eixo de nitidez (wwdc2019_810, folha 0013 q0110 e q0111).
- Efeito de mascaramento mostrado como fato de tela: quatro barras verticais de alturas ligeiramente diferentes e, nos quadros seguintes, a primeira barra escurecendo e perdendo peso visual em relação às outras três (wwdc2019_810, folha 0014 q0123 a q0125).
- Protótipo reduzido ao mínimo para testar harmonia: moldura de iPhone com uma única bolinha caindo do centro para a base, ladeada por duas colunas fixas em que a coluna do mundo real já traz visual, som e tato completos e a do mundo digital ganha esses itens um a um (wwdc2019_810, folha 0007 q0057 a q0063).
- Especificações de asset sempre no mesmo formato de três linhas sobre vídeo desfocado, com a dimensão em dois vezes em peso mais forte: 1846 por 300, depois 512 por 512 em uma vez e 1024 por 1024 em dois vezes, depois 659 por 371 e 1318 por 742 (wwdc2020_10145, folhas 0006 q0048, 0009 q0075 e 0011 q0098).
- Tabela de decisão em três colunas mapeando contexto de uso para o valor de código correspondente, com os cabeçalhos de situação em cima e o valor embaixo, em formato de referência rápida, e as ressalvas aparecendo só no quadro seguinte (wwdc2020_10104, folha 0016 q0140 e q0141).
- Prática desaconselhada marcada com X vermelho circular no canto do slide sem contraparte correta ao lado, inclusive num bloco de código cujo próprio comentário na tela avisa do resultado borrado (wwdc2020_10104, folha 0008 q0066 a q0069 e folha 0020 q0173 a q0175).
- Grade de categorias diferenciada por forma e cor do ícone, círculo cinza translúcido, losango laranja, octógono preto e losango vermelho, em duas fileiras de quatro com rótulo pequeno abaixo (wwdc2019_805, folha 0006 q0052 para q0053).
- Encadeamento entre ações mostrado como transformação do próprio campo: o parâmetro passa de placeholder genérico para um chip de variável azul com nome, enquanto o editor ao lado mostra o campo correspondente com moldura verde e texto de ajuda (wwdc2019_805, folha 0009 q0079 a q0081).
- Sinônimos aceitos crescendo como segunda linha em itálico sob cada opção do cartão, mais longa a cada quadro (wwdc2019_806, folha 0011 q0093 a q0095).
- Autoria do texto marcada na imagem por etiquetas que apontam qual trecho da frase é escrito pelo desenvolvedor e qual vem da categoria do sistema (wwdc2019_806, folha 0013 q0116).
- Excesso de saudação demonstrado por repetição visual: a frase marcada com X e depois repetida em cópias esmaecidas ao redor para simular o efeito de ouvir aquilo muitas vezes (wwdc2019_806, folha 0015 q0127 e q0128).
- Barra de ícones de período do dia, nascer do sol, carro, sol e cama, em que o ícone ativo muda e o widget em destaque acompanha, de clima para música e depois notícias (wwdc2020_10103, folha 0002 q0011 a q0014).
- Encaixe espacial do widget mostrado literalmente com uma grade de quadrados arredondados vazios representando ícones da tela de início, dois slots centrais contornados em branco mais grosso, antes de a grade sumir e sobrar só a forma do tamanho pequeno (wwdc2020_10103, folha 0007 q0058 para q0059).
- Diagrama tipo mapa mental no encerramento, nascendo de ícones quase invisíveis e se resolvendo ao conectar painel, perfil, rankings, cartões de conquista, amigos, multijogador e loja a um ícone central colorido, arquitetura de informação que nenhuma tela isolada mostrou antes (wwdc2020_10145, folha 0015 q0127 e q0128).
- Localização aproximada desenhada sem símbolo novo, como grande área circular desfocada e translúcida ocupando o centro do mapa no mesmo lugar onde estaria o ponto nítido, sumindo quando o mapa é muito aproximado e sobrando só o controle pequeno no canto (wwdc2020_10162, folha 0003 q0022 para q0023 e folha 0004 q0035 para q0036).
- Exceção comunicada dentro de um item de lista padrão sem alterar os demais: só a opção de localização atual ganha uma nota curta abaixo do nome, os outros lugares sugeridos ficam sem nota (wwdc2020_10162, folha 0005 q0044 e q0045).
- Janela de validade anotada graficamente sobre uma notificação padrão, ícone de relógio com seta circular mais o texto da duração, depois isolado em tela cheia sobre fundo preto (wwdc2020_10172, folha 0018 q0154 a q0157).
- O que deve ficar de fora de uma experiência leve é mostrado como cartões de exclusão com X em círculo cinza, cada um emparelhado com a captura da tela a ser cortada, introduções, login e contas, navegação por abas (wwdc2020_10172, folha 0017 q0147 a q0151).
- Várias telas de bloqueio sobrepostas em leque, como cartas empilhadas, ganhando uma notificação nova a cada quadro, para mostrar acúmulo de casos sem precisar de telas separadas (wwdc2020_10088, folha 0003 q0025 a q0027).
- Indicador de edição recente visível em toda captura do editor, uma faixa rosa clara marcando a área recém alterada, detalhe que nenhuma fala menciona (wwdc2020_10093, folhas 0008 a 0010 e 0013 a 0015).
- Rodapé de slide com linha divisória, título da sessão à esquerda e sigla do evento à direita, presente nos slides e nunca verbalizado (wwdc2020_10093, folha 0005).
- Ponteiro mudando de forma conforme o contexto dentro do mesmo app, círculo translúcido rosa sobre a área central e mira em cruz no quadro seguinte, na mesma posição (wwdc2020_10093, folha 0011 q0092 para q0093).
- Área de clique de um controle sem borda visível sugerida por um retângulo de destaque que contorna um grupo de botões da barra de ferramentas (wwdc2020_10104, folha 0007 q0062 e q0063).
- Estado de foco de janela provado por comparação lateral, a instância inativa com a sidebar perdendo nitidez e marcada por círculo rosa com X, a ativa nítida com círculo verde, e os rótulos trocando de lado entre quadros (wwdc2019_809, folha 0008 q0070 a q0072).
- Ícone de app tratado como problema de forma e de resolução: um molde de squircle branco vazio inserido no meio de uma fileira de ícones reais e depois isolado sobre fundo quadriculado, e o mesmo ícone colorido lado a lado em 16 por 16 pixels simplificado contra a versão em resolução cheia detalhada (wwdc2019_809, folha 0017 q0148 a q0153 e folha 0018 q0155 a q0158).
- Barra de menu destrinchada como exercício de catalogação, uma tabela de duas colunas de objeto e ação, seguida da barra real com cada menu aberto em sequência, e a estabilidade do menu ilustrada por duas instâncias do mesmo menu lado a lado, uma sem seleção e outra com o item selecionado (wwdc2019_809, folhas 0021 q0183 a q0189 e 0023 q0203 a q0204).
- Menu de nível superior do sistema de acessibilidade mostrado já com ícones aplicados, submenu horizontal de quatro ícones com legenda curta ao lado do código que os define (wwdc2020_10019, folha 0009).
- Foco do cursor de varredura com convenção fixa nas capturas, retângulo de contorno azul sólido em volta do elemento, deslocando de posição entre quadros vizinhos para indicar avanço (wwdc2020_10019, folha 0007 q0056 para q0057, folha 0008 q0068 para q0069, folha 0010 q0084 para q0085).
- Variante de símbolo para alto contraste organizada no catálogo de assets, evoluindo de uma variante única para duas empilhadas e depois quatro combinando luminosidade e nível de contraste, cada uma com seu tom (wwdc2020_10020, folha 0008 q0070 a q0072 e folha 0009 q0081).
- Célula de lista que muda de arranjo quando o texto cresce, deixando de ter símbolo e nome lado a lado centralizados e passando a empilhar o símbolo acima do nome alinhado à esquerda, com bem menos itens visíveis por tela (wwdc2020_10020, folha 0012 q0100 a q0103).
- Painel de ajustes do sistema sobreposto à esquerda da mesma tela do app afetado, mostrando configuração e efeito no mesmo quadro (wwdc2020_10020, folha 0014 q0119 para q0120).
- Um cartão da série quebrando o próprio template, aparecendo primeiro só com texto e sem bloco de código, ao contrário de todos os outros, e só depois ganhando a versão com código (wwdc2020_10020, folha 0015 q0132 e folha 0016 q0137).
- Contraste de tratamento entre conteúdo informativo e acionável na mesma tela: a nota fica direto sobre o fundo preto sem contêiner, enquanto a ação destrutiva fica dentro de um contêiner retangular escuro com texto vermelho (wwdc2020_10171, folha 0010 q0084).
- Gesto que não traduz entre plataformas marcado com alerta explícito, um indicador de atualização por puxão acompanhado de círculo amarelo de exclamação, e o ganho do cursor mostrado em dois gráficos empilhados, um apontado por toque e outro por cursor no mesmo ponto de dado (wwdc2019_809, folha 0016 q0139 a q0143).
- Par de métodos complementares de animação exibido como dois blocos de código quase idênticos que trocam entre si, entrada com opacidade zero e saída com opacidade um, cada um com seu comentário (wwdc2020_10093, folha 0017 q0151 para q0152).
- Ranking embutido no jogo como painel lateral compacto com miniatura de mapa e lista numerada, com a linha do próprio jogador destacada no fim da lista mesmo estando fora do topo (wwdc2020_10145, folha 0012 q0105 a q0107).
- Transição de cena feita só por escurecimento total do quadro, sem cartela nem corte, diferente de todas as outras passagens do mesmo vídeo (wwdc2020_10071, folha 0007 q0062).
