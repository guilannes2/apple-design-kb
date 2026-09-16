# ess-01, padrões visuais recorrentes

Base: 53 sínteses visuais do HIG, de `accessibility` a `game-center`.

## Toda página abre com um ícone único desenhado sobre grade de construção tracejada, com círculo guia e diagonais centrados
- Evidência: accessibility (img 0000, símbolo em silhueta com grade retangular e circular pontilhada e diagonais marcando centro e proporções)
- Evidência: carplay (img 0230, "C" com triângulo de play sobre grade tracejada e círculo guia)
- Evidência: designing-for-games (img 0433, controle com grade pontilhada, círculo e X diagonal centralizados, alças acompanhando as diagonais)
- Evidência: entering-data (img 0472, campo inscrito no círculo e só o lápis ultrapassando o limite no alto à direita)
- Evidência: file-management (img 0479, documento centrado no cruzamento das guias e inscrito no círculo tracejado)
- O que isso ensina sobre construir interface: a Apple mostra o andaime junto com a forma, e cada silhueta nasce ancorada num círculo e num par de eixos em vez de desenho livre. Para construir um sistema de ícones, definir primeiro a grade e o círculo inscrito e derivar toda forma deles dá coerência entre peças feitas em momentos diferentes.

## A cor do degradê da abertura classifica o assunto por família, e a forma interna é a única variável
- Evidência: designing-for-ios, ipados, macos, tvos, visionos, watchos, iphone-duo e designing-for-games, todos em degradê verde com a mesma composição (img 0433 a 0436, 0456 a 0459)
- Evidência: airplay, carekit, carplay, augmented-reality e game-center em degradê azul (img 0039, 0216, 0230, 0160, 0490)
- Evidência: boxes, collections, column-views, charts, collaboration-and-sharing, drag-and-drop, entering-data, feedback e file-management em degradê laranja para vermelho (img 0183, 0252, 0342, 0234, 0246, 0470, 0472, 0478, 0479)
- Evidência: action-button, always-on, apple-pencil-and-scribble, camera-control, digital-crown, eyes e focus-and-selection em degradê rosa para roxo (img 0024, 0052, 0147, 0200, 0461, 0473, 0481)
- O que isso ensina sobre construir interface: a cor faz o trabalho de taxonomia antes de qualquer texto, e o leitor sabe em que capítulo está só pela paleta. Num produto, reservar a matiz para indicar a família do conteúdo e deixar a forma indicar o item específico evita depender de rótulo.

## Aparelhos e objetos são reduzidos a três ou quatro traços reconhecíveis, sem textura nem detalhe supérfluo
- Evidência: designing-for-ios (img 0434, iPhone reduzido a moldura, entalhe do topo e barra de home)
- Evidência: designing-for-games (img 0433, controle reduzido a corpo, cruz direcional e dois botões, sem gatilhos nem empunhadura)
- Evidência: designing-for-watchos (img 0459, caixa com duas saliências laterais e duas alças)
- Evidência: app-icons (img 0083 e 0084, Podcasts em círculos concêntricos e Home em camadas aninhadas até a porta)
- O que isso ensina sobre construir interface: reconhecimento vem da silhueta e de dois ou três marcadores, não da fidelidade. Ao desenhar ícones, cortar tudo que não distingue o objeto de seus vizinhos é o que mantém leitura em tamanho pequeno.

## Medida de componente é cotada por seta dupla bidirecional sem número, enquanto asset exportável e marca de terceiro recebem cota numérica
- Evidência: boxes (img 0183, quatro setas duplas vermelhas cotando padding e margem, nenhum número impresso)
- Evidência: collections (img 0252, setas de margem externa mais duas marcas menores para o espaçamento entre células, sem valores)
- Evidência: buttons (img 0189, setas vermelhas para a largura da cápsula e o espaçamento entre dois botões, sem números)
- Evidência: apple-pay (img 0144 e 0145, contorno rosa com altura mínima de 30, largura mínima de 100 e de 140, margem de 1/10 da altura)
- Evidência: game-center (img 0496, 0497, 0500, 0501, 0505, 0511, quadrados e retângulos com valores em pt para máscara, corte e tamanhos de foco)
- O que isso ensina sobre construir interface: proporção e respiro são ensinados como relação, e o número só aparece quando alguém precisa exportar um arquivo ou proteger uma marca. Especificar um design system pela relação entre medidas, e fixar números só nos pontos de contrato, deixa o layout escalar entre tamanhos de tela.

## Certo e errado são julgados por um par fixo de selos, X cinza em círculo cinza e check verde em círculo verde, quase sempre em imagem própria isolada
- Evidência: branding (img 0186 e 0188, selos isolados e centralizados em fundo branco, sem nenhum elemento de interface junto)
- Evidência: airplay (img 0044 e 0045, selos em células próprias, sem estarem emparelhados na mesma imagem)
- Evidência: accessibility (img 0004 a 0007, botão de baixo contraste com X e botão azul royal com check)
- Evidência: eyes (img 0475 e 0477, X para a área interna quadrada e check para a circular)
- Evidência: camera-control (img 0209 a 0212, régua com "1 EV" recebe check e a mesma régua com "1" recebe X)
- O que isso ensina sobre construir interface: o veredito é um sinal padronizado e separado do exemplo, então o exemplo nunca vira ilustração deformada para parecer errada. Em documentação interna, manter os dois casos visualmente idênticos e colocar o julgamento fora deles força a diferença real a ficar evidente.

## Um exemplo por vez muda uma única variável, reaproveitando a mesma composição, o mesmo conteúdo e o mesmo enquadramento
- Evidência: branding (img 0185 e 0187, o mesmo mapa de aeroporto, mudando só se a cor de marca está nos controles ou no conteúdo)
- Evidência: focus-and-selection (img 0485 a 0489, o mesmo botão em pílula no mesmo ponto da mesma foto de praia, variando só o estado)
- Evidência: apple-pay (img 0135 a 0143, os mesmos dois botões trocando uma variável por vez: tamanho, ordem, alinhamento, raio de canto)
- Evidência: activity-rings (img 0034 e 0035, telas Summary com o mesmo cabeçalho, a mesma data e o mesmo avatar, mudando só o cartão)
- Evidência: app-clips (img 0072 a 0075, os erros vêm um por vez: proporção ovalada, depois gradiente, depois sombra)
- O que isso ensina sobre construir interface: o conteúdo fictício é mantido constante de propósito para que o olho só possa notar a variável em estudo. Ao apresentar opções de design, reusar literalmente a mesma tela e trocar um atributo evita que a decisão seja contaminada por diferenças acidentais.

## O antes e o depois usam o mesmo fundo para ensinar que é um fluxo de dois passos, não duas telas independentes
- Evidência: action-sheets (img 0026 e 0027, a mesma tela de composição do Mail, mudando só a presença da sheet sobreposta)
- Evidência: activity-views (img 0037 e 0038, a mesma nota ao fundo antes e depois de tocar em Share)
- Evidência: disclosure-controls (img 0467 e 0468, o mesmo diálogo de salvar colapsado e expandido, com o campo de nome intacto no topo)
- Evidência: controls (img 0409 e 0410, o mesmo control em pílula aberto e bloqueado)
- O que isso ensina sobre construir interface: a continuidade do fundo é o que comunica causa e efeito. Uma transição que troca a tela inteira perde a ligação entre a ação e o resultado, e o par de estados sobre a mesma base é o jeito barato de preservá-la.

## A anatomia é ensinada com linhas de chamada que nomeiam cada parte dentro da própria imagem
- Evidência: charts (img 0235, chamadas para grid line, plot area, mark, axis, tick e axis value label sobre o mesmo histograma da capa)
- Evidência: controls (img 0400, "Symbol image" à esquerda e "Value" na segunda linha do bloco de texto)
- Evidência: carekit (img 0219, header com disclosure indicator, separador horizontal e subview de conteúdo)
- Evidência: app-shortcuts (img 0092, linha de chamada nomeando "Parameter" o trecho variável azul e sublinhado da frase)
- Evidência: complications (img 0344, mostrador com linhas finas ligando rótulos às zonas Top Left, Date, Middle, Bottom Left, Bottom Middle e Bottom Right)
- O que isso ensina sobre construir interface: nomear as zonas de um componente na própria arte cria vocabulário compartilhado entre quem desenha e quem implementa. Um diagrama anotado vale mais que uma lista de slots em texto, porque amarra o nome à posição.

## O mesmo componente atravessa as plataformas com estrutura idêntica, mudando só o arranjo dos elementos e o material do fundo
- Evidência: alerts (img 0047 a 0051, título e descrição idênticos em iPhone, Mac, tvOS, Vision Pro e Watch, com botões lado a lado ou empilhados e fundo opaco, semitransparente, vidro ou degradê)
- Evidência: app-icons (img 0078, a mesma flor de Fotos trocando só a moldura: quadrado arredondado, retângulo alongado e círculo)
- Evidência: game-center (img 0492, o mesmo Game Overlay cobre a tela inteira no iPhone e vira faixa vertical na borda trailing no iPad)
- Evidência: complications (img 0367, 0380, 0387 e 0397, o mesmo dado "LON 6:09" recomposto em linha única, empilhado sobre círculo e empilhado em duas cores conforme a família)
- O que isso ensina sobre construir interface: o que viaja entre plataformas é a hierarquia de informação, não o layout. Modelar o componente pelo conteúdo e deixar arranjo e material como parâmetros da plataforma é o que permite uma só definição servir a telas muito diferentes.

## A hierarquia entre ações vem do preenchimento e do peso, com o destrutivo marcado em vermelho no texto e não no fundo
- Evidência: buttons (img 0190, primário com fundo azul sólido e texto branco, destrutivo com fundo cinza claro e texto vermelho, secundário com fundo cinza claro e texto preto)
- Evidência: alerts (img 0046, secundário em rosa claro e primário em vermelho forte com texto em negrito maior)
- Evidência: action-sheets (img 0027, "Delete Draft" em vermelho e "Save Draft" em preto, ambos na mesma forma de pílula)
- Evidência: file-management (img 0480, ação primária como único botão azul sólido logo abaixo do nome do app)
- O que isso ensina sobre construir interface: uma única ação por tela ganha preenchimento sólido, e o perigo é sinalizado por cor do texto para não competir em peso com a ação principal. Pintar o botão destrutivo inteiro de vermelho o transformaria no elemento mais pesado da tela, que é o oposto do que se quer.

## Uma só cor de destaque atravessa a tela inteira, e o item não selecionado nunca a recebe
- Evidência: carekit (img 0217 a 0229, o vermelho aparece em checks, seletor de dias, barras do gráfico, botão de registro e ações de contato, com fundos e botões secundários em branco e cinza)
- Evidência: camera-control (img 0202 a 0208, o laranja marca o ícone ativo, o traço central da régua, o ponto escolhido e todos os rótulos de valor)
- Evidência: color (img 0262, o item selecionado da tab bar leva azul no ícone e no rótulo, e o não selecionado fica preto no claro e branco no escuro, com rótulo cinza)
- Evidência: focus-and-selection (img 0484, o item destacado ganha estrela preenchida, ícone e texto vermelhos, e os demais seguem pretos sobre branco)
- O que isso ensina sobre construir interface: a cor de acento é um recurso escasso e só marca estado ou ação, nunca decora. Aplicá-la ao item inativo destrói a leitura de estado, que é a única coisa que ela deveria comunicar.

## A cor nunca carrega a informação sozinha, sempre dobrada por forma, símbolo, preenchimento ou tamanho
- Evidência: accessibility (img 0010 e 0011, dois círculos que só diferiam no tom ganham check branco no verde e octógono com X branco no vermelho)
- Evidência: charts (img 0243, sistólica em bolinhas vermelhas e diastólica em losangos pretos e brancos, com o marcador de forma repetido no cabeçalho)
- Evidência: carekit (img 0219, 0223 e 0224, círculo vermelho cheio com check para feito e círculo apenas contornado para pendente)
- Evidência: camera-control (img 0204, 0207 e 0208, a opção ativa fica laranja e também maior que as vizinhas, com o nome escrito por extenso abaixo)
- O que isso ensina sobre construir interface: qualquer estado que só existe na matiz desaparece para parte dos usuários e em fotos de baixo contraste. A regra prática é garantir um segundo canal, forma ou preenchimento ou tamanho ou texto, antes de escolher a cor.

## Amostra de cor é documentada como cartão mínimo com o valor RGB ao lado, sem nome e sem contexto de uso
- Evidência: color (img 0270 a 0341, quadrado de cantos arredondados com três valores RGB, cada cartão repetido sobre fundo branco e sobre fundo preto com valor idêntico)
- Evidência: activity-rings (img 0031 a 0033, rosa avermelhado 250, 17, 79, verde limão 166, 255, 0 e ciano 0, 255, 246)
- Evidência: color-wells (img 0253, cota de texto com o valor RGB ligada por linha ao centro do botão, tratando a cor atual como dado de especificação)
- O que isso ensina sobre construir interface: a cor é entregue como valor verificável e não como impressão. Num sistema próprio, publicar o token com o valor numérico visível sobre os dois fundos evita que alguém reamostre a cor de um screenshot.

## No modo escuro a geometria não se mexe: posição, réguas e estrutura ficam idênticas e só mudam fundo e valores internos
- Evidência: color-wells (img 0253, estrutura, réguas e posição do texto idênticas, com o popover passando a marrom vinho e a caixa branca virando contorno claro semitransparente)
- Evidência: app-icons (img 0080 a 0082, a engrenagem e a posição de cada guia não mudam, fundo e linhas trocam para preto e branco)
- Evidência: dark-mode (img 0413 e 0414, as quatro amostras mudam só um pouco de saturação enquanto o quadrado passa de cinza claro a quase preto)
- Evidência: color (img 0255 a 0258, a mesma tela do Notes em padrão claro, contraste aumentado claro, padrão escuro e contraste aumentado escuro, com o botão mantendo o fundo amarelo e trocando só o símbolo)
- O que isso ensina sobre construir interface: tema é troca de valores dentro de uma estrutura fixa, não um segundo layout. Quando a posição muda entre claro e escuro, é sinal de que a cor foi usada para resolver um problema de composição que deveria ter sido resolvido na geometria.

## O material de vidro absorve a cor do que está atrás, e o controle mantém o próprio tom sobre qualquer fundo
- Evidência: color (img 0263, botão de compartilhar sobre foto de flores e montanha aparece visivelmente tingido de rosa e azul)
- Evidência: color (img 0261, o botão circular azul com check branco não muda de tom sobre fundo branco nem sobre fundo preto, só o fundo em volta inverte)
- Evidência: controls (img 0399, 0401 e 0402, botões circulares translúcidos na Central de Controle e no rodapé da Lock Screen sobre fundo escuro desfocado)
- Evidência: buttons (vídeo 006, folha 0001, q007 e q008, menu com fundo translúcido azulado que aparenta vir do conteúdo por trás)
- O que isso ensina sobre construir interface: a translucidez cria pertencimento ao contexto sem exigir que o componente mude de definição. O preço é que legibilidade precisa ser garantida pelo próprio elemento, e não pelo fundo que muda a cada tela.

## Em visionOS a hierarquia vem de nitidez, transparência e profundidade, não de escala, e os painéis flutuam à frente da cena
- Evidência: app-icons (vídeo 004, folha 0001, fileira da frente nítida e a de trás desfocada e cortada no topo)
- Evidência: alerts (vídeo 003, folhas 0001 a 0003, o alerta se forma à frente da janela e o conjunto fica progressivamente mais transparente enquanto se desloca pela sala)
- Evidência: alerts (vídeo 002, folha 0001, o alerta nunca coincide com o contorno da janela atrás dele, aparecendo deslocado em q003 e mais perto do centro em q004)
- Evidência: eyes (vídeo 009, folhas 0001 a 0003, painéis translúcidos de cantos arredondados flutuando sobre o quarto real)
- O que isso ensina sobre construir interface: em espaço tridimensional, o que estava resolvido por tamanho e sombra passa a ser resolvido por foco e distância. Quem projeta para essas telas precisa tratar profundidade como uma dimensão de hierarquia com a mesma seriedade que trata contraste.

## Mudança de estado preserva a caixa: nada se desloca, cresce ou recompõe ao redor
- Evidência: buttons (img 0191 e 0192, "Checkout" vira "Checking out" com spinner na borda inicial, mantendo forma e cor de fundo sem mudança perceptível de tamanho)
- Evidência: eyes (vídeo 009, folha 0002, q010 a q018, o hover altera só o realce de fundo da linha mirada, sem deslocar nem redimensionar nada)
- Evidência: controls (img 0409 e 0410, o dado sensível vira duas barras cinza sem mudar forma nem tamanho do control)
- Evidência: buttons (vídeo 006, folha 0001, q006 a q008, o botão de mais opções clareia e depois fica branco sólido enquanto os vizinhos permanecem cinza)
- O que isso ensina sobre construir interface: reservar o espaço do estado final desde o estado inicial elimina o salto de layout, que é a principal fonte de erro de toque. Trocar cor, preenchimento e conteúdo dentro de uma caixa fixa resolve quase todo feedback visual.

## Menus e painéis nascem ancorados à origem, ligados por ponta, linha ou forma contínua
- Evidência: dock-menus (img 0469, balão com ponta triangular apontando de volta para o ícone de origem)
- Evidência: edit-menus (img 0471, linha fina ligando a ponta esquerda da barra à alça superior esquerda da seleção)
- Evidência: color-wells (img 0253, forma contínua em gota conectando o botão fechado ao popover aberto)
- Evidência: context-menus (img 0398, menu ancorado logo abaixo e à direita do cursor, não centralizado na tela)
- Evidência: buttons (vídeo 006, folha 0001, q007 e q008, o menu nasce ancorado logo abaixo do botão, parcialmente cortado e depois inteiro)
- O que isso ensina sobre construir interface: a ligação visual responde à pergunta "isso veio de onde" sem custo de atenção. Um painel que aparece centralizado obriga o usuário a reconstruir a causa, e o ganho de posicionar na origem é maior que o de um alinhamento perfeito.

## Os vídeos revelam a etapa intermediária que a descrição escrita omite
- Evidência: alerts (vídeo 002, folha 0001, o alerta não aparece direto, antes há um menu de contexto com "Recover" e "Delete", e a opção Delete fica destacada por cerca de meio segundo)
- Evidência: drag-and-drop (vídeo 008, folhas 0001 e 0002, o arquivo pousa primeiro como cartão plano rotulado sobre a mesa e só então o objeto 3D nasce pequeno e cresce ganhando crateras e textura)
- Evidência: buttons (vídeo 007, folha 0001, a tooltip surge com atraso, menor em q003, e só em q004 atinge tamanho e opacidade finais)
- O que isso ensina sobre construir interface: a transição é o produto, não um enfeite entre dois estados. Quando se lê só a especificação final, os passos que explicam a mudança ficam de fora e a implementação sai abrupta.

## A densidade da grade muda com a largura disponível e os mesmos elementos se redistribuem, sem sumir
- Evidência: designing-for-iphone-duo (img 0437 e 0438, a Tela de Início passa de quatro colunas por quatro linhas na tela externa para seis por quatro na interna, com a coluna de atalhos fixa na borda direita nas duas)
- Evidência: designing-for-iphone-duo (img 0452, a Calculadora passa de quatro colunas por cinco linhas para cinco colunas por quatro linhas na tela mais larga e baixa)
- Evidência: camera-control (img 0213, a fileira de ícones e o rótulo formam faixa horizontal no topo em retrato e migram para a lateral direita em paisagem)
- Evidência: apple-pencil-and-scribble (img 0159, a barra completa do iPad em paisagem vira barra superior mais paleta reduzida no iPhone em retrato)
- O que isso ensina sobre construir interface: adaptar é reorganizar a mesma matéria, não cortar funcionalidade. Definir o conjunto de elementos e depois as regras de arranjo por largura evita as versões mutiladas que aparecem quando se projeta cada tamanho do zero.

## Os controles ficam presos à borda do conteúdo ou do hardware que servem
- Evidência: camera-control (img 0201 e 0213, o overlay aparece na região logo abaixo do botão físico e acompanha a borda dele quando o aparelho gira)
- Evidência: designing-for-iphone-duo (img 0451 e 0453, em Split View cada app usa uma faixa de controles na própria borda externa, e no Mail o painel leading leva seus controles no topo e o trailing na borda vertical direita)
- Evidência: apple-pencil-and-scribble (img 0151 e 0152, os controles ficam nas duas bordas laterais do iPad justamente porque a mão que segura o Pencil cobre um dos lados)
- O que isso ensina sobre construir interface: a posição do controle é decidida pela ergonomia do gesto e pela origem física da ação, não pela simetria da tela. Duplicar o controle nas duas bordas é preferível a escolher um lado quando a mão pode vir de qualquer um.

## Rosa e vermelho são a cor da anotação: medida, espaço livre reservado e área protegida
- Evidência: app-clips (img 0069 e 0070, o espaço livre é uma faixa rosa com a mesma cota x repetida em todos os lados de cada código)
- Evidência: augmented-reality (img 0177 e 0179 a 0182, o espaço livre mínimo do glifo e de cada selo é marcado por um quadro rosa translúcido)
- Evidência: apple-pay (img 0144 e 0145, diagramas de medida com contorno rosa e cotas em pontos)
- Evidência: accessibility (img 0016, contornos vermelhos tracejados sobre as áreas de toque que se encostam sem espaço entre si)
- O que isso ensina sobre construir interface: a camada de anotação tem cor própria e nunca se confunde com a interface real. Reservar uma cor exclusiva para overlays de especificação é o que permite marcar espaços invisíveis, como área de toque e margem de proteção, sem sujar o exemplo.

## No tvOS o foco aumenta o elemento, e o asset precisa nascer em tamanhos distintos para isso
- Evidência: focus-and-selection (img 0485 e 0486, a pílula sem foco é cinza translúcida e a menor da série, e com foco vira branca opaca e maior)
- Evidência: game-center (img 0501, três retângulos concêntricos com a imagem em 659x371 pt, o tamanho em foco em 618x348 pt e o fora de foco em 548x309 pt)
- O que isso ensina sobre construir interface: em interface controlada a distância, o foco precisa de mudança de área e de opacidade, não só de borda. Isso obriga a planejar a arte com folga de escala desde a exportação.

## A ilustração estilizada simplifica e às vezes perde uma camada que a captura real tem
- Evidência: activity-views (img 0036 comparada a img 0038, a estilização tem duas fileiras e a captura real acrescenta uma fileira própria de contatos, separando contatos, apps e ações em três faixas)
- Evidência: action-sheets (img 0025 comparada a img 0027, o diagrama isola o cartão com cotas de largura e altura, sem iPhone e sem posição na tela)
- Evidência: activity-rings (img 0029 comparada a img 0030 e 0034, a porcentagem escrita ao lado de cada anel só existe no diagrama conceitual, e nas telas reais os valores vêm como par de valor atual e meta)
- O que isso ensina sobre construir interface: o diagrama serve para ensinar proporção e nomes, e a captura serve para conferir densidade real. Implementar a partir do diagrama sozinho costuma produzir uma tela com menos informação do que o componente realmente carrega.

## Itens relacionados são agrupados em blocos arredondados com separador fino, e a divisão carrega significado
- Evidência: eyes (vídeo 009, folhas 0001 a 0003, os itens do painel de detalhe se agrupam em blocos arredondados menores que juntam pares relacionados, como About com Software Update e AirDrop com Handoff)
- Evidência: dock-menus (img 0469, quatro itens divididos em dois grupos por uma linha divisória, com "Show Recents" e "Open" formando o segundo)
- Evidência: carekit (img 0219 e 0229, header com título e disclosure indicator, separador horizontal e subview de conteúdo abaixo)
- Evidência: collaboration-and-sharing (img 0251, popover em três blocos verticais: abas de canal no topo, estado no meio, toggle e itens de lista embaixo)
- O que isso ensina sobre construir interface: o agrupamento é a primeira camada de hierarquia, antes de tipografia e cor. Uma lista longa sem blocos obriga a ler tudo, enquanto três blocos permitem pular direto para a região certa.

## Texto vem antes do dado e antes da ação: título, depois descrição curta, depois o gráfico ou os botões
- Evidência: charts (img 0242, o cartão traz primeiro o título do alerta de chuva forte e um subtítulo em linguagem simples, e só depois o gráfico de barras)
- Evidência: action-sheets (img 0025, hierarquia interna de título, descrição e pilha de três ações no mesmo formato de pílula)
- Evidência: app-clips (img 0054, título em negrito, descrição em duas linhas, botão à direita e atribuição discreta abaixo)
- Evidência: column-views (img 0342, painel de detalhes empilhado por importância: miniatura grande, nome em negrito maior, linha curta de formato e tamanho, e só então os pares de rótulo e valor)
- O que isso ensina sobre construir interface: a leitura começa pela conclusão em linguagem comum e desce para a evidência. Um gráfico ou uma lista de ações posta antes da frase que explica o que está acontecendo transfere ao usuário o trabalho de interpretar.

## O estado ativo se distingue por preenchimento e por tamanho ao mesmo tempo, e a seleção pode ter dois níveis
- Evidência: column-views (img 0342, destaque fraco na coluna cuja seleção já avançou e fundo vermelho sólido no item com foco ativo, tornando visível a cascata)
- Evidência: buttons (img 0193 a 0196, o botão selecionado do visionOS inverte o contraste, com círculo interno branco sólido e ícone em contorno preto, e o indisponível aparece esmaecido)
- Evidência: camera-control (img 0204, a opção escolhida é preenchida em laranja e maior que as cinzas)
- Evidência: carekit (img 0217, dias completos com check vermelho preenchido e o dia selecionado com contorno mais grosso)
- O que isso ensina sobre construir interface: quando existem foco, seleção e conclusão ao mesmo tempo, um único recurso visual não basta. Separar preenchimento para "concluído" e contorno ou tamanho para "onde estou" mantém os dois legíveis na mesma fileira.

## Em watchOS o alerta e a action sheet compartilham a mesma construção, com botões coloridos por função em vez de neutros
- Evidência: alerts (img 0051, título e descrição centralizados em branco sobre degradê azul escuro para roxo, com primário em verde e secundário em degradê roxo e magenta)
- Evidência: action-sheets (img 0028, X de fechar no canto superior esquerdo, título e descrição centralizados e dois botões grandes em pílula empilhados, a ação em verde e o Cancel em degradê roxo e magenta)
- O que isso ensina sobre construir interface: em tela muito pequena o botão ocupa quase toda a largura, então a diferença entre as opções precisa vir da cor do próprio botão, não de posição ou peso de texto.

## Achados de fonte única

- O Icon Composer aparece como ferramenta real, com camadas nomeadas em grupos aninhados à esquerda, arte no centro e propriedades à direita: opacidade 100%, blend mode normal, preenchimento sólido, "Liquid Glass Effects" ligado, imagem em SVG, posição x e y em 0 pt e escala 100% (app-icons, img 0079).
- A grade de aparências do ícone é 3 por 2 com rótulo sob cada célula: padrão colorido, clara translúcida e tintada clara em cima, escura, escura translúcida e tintada escura embaixo (app-icons, img 0089).
- A zona segura do ícone de tvOS é um retângulo tracejado dentro da arte, e a forma cabe inteira nele com margem visível até a borda externa (app-icons, img 0090).
- Profundidade por sobreposição, sobre fundo quadriculado de transparência: o círculo externo aprovado não tem contorno e usa preenchimento semitransparente que deixa o xadrez aparecer, e o sólido parece pousado sobre ele (app-icons, img 0085 a 0088).
- Ilustração complexa no modo escuro não se resolve com borda, e sim refazendo os valores internos: roupas e cadeiras passam a branco ou cinza claro e os cabelos clareiam, enquanto um ícone simples de forma única só precisa de contorno fino (dark-mode, img 0415 a 0419).
- A hierarquia de rótulos é uma escala de quatro níveis com contraste decrescente, label, secondaryLabel, tertiaryLabel e quaternaryLabel, repetida na mesma ordem sobre preto, sobre cinza escuro elevado e sobre branco (dark-mode, img 0422 a 0424).
- A gestão de gamut é mostrada no diagrama de cromaticidade com dois triângulos, o sRGB inteiramente contido no Display P3 (color, img 0268).
- A mesma alta do Stocks é linha verde em inglês e vermelha em chinês, com valores e curva idênticos (color, img 0259 e 0260).
- A escala de cinzas do iOS vai de 28, 28, 30 a 242, 242, 247, e nos extremos o contraste com o fundo quase desaparece, o mais claro sobre branco e o mais escuro sobre preto (color, img 0318 a 0341).
- Erro de validação de pagamento é sinalizado só por texto vermelho no campo e no rótulo, sem ícone de alerta e sem mudar o layout, tanto em app quanto na web (apple-pay, img 0103 a 0105).
- A marca Apple Pay entra numa fileira com outras bandeiras de pagamento, todas no mesmo tamanho e formato, tratada como bandeira e não como botão (apple-pay, img 0146).
- O App Clip Code tem diâmetro mínimo de 3/4 de polegada, ocupa exatamente uma fatia de 60 graus quando aplicado a superfície cilíndrica, e seu espaço livre é a mesma cota x repetida nos quatro lados (app-clips, img 0061, 0067 a 0070).
- A dica do Action Button nomeia o resultado de segurar, não o estado atual: com a pílula em "Ring" a dica diz "Hold for Silent", e com a pílula em "Silent" diz "Hold for Ring" (controls, img 0407 e 0408).
- Um valor numérico reprovado é o que aparece sem unidade: a régua com "1 EV" passa e a mesma régua com apenas "1" é marcada como erro (camera-control, img 0209 a 0212).
- Duplicar no visor os valores que o overlay já mostra é o erro exemplificado, com zoom empilhado à esquerda do obturador além do rótulo do topo (camera-control, img 0214 e 0215).
- A alternativa ao gesto de swipe é um botão vermelho de menos sempre visível no modo de edição, porque com swipe o botão "Delete" cobre parte do título e do subtítulo (accessibility, img 0017 e 0018).
- A cor adaptativa importa porque o systemRed padrão fica praticamente igual sobre fundo claro e escuro, enquanto a variante acessível escurece e satura no claro e clareia puxando para rosa no escuro (accessibility, img 0008 e 0009).
- O Assistive Access reduz a Câmera a três alvos grandes em fundo preto, e a tela seguinte troca as duas opções por prévia grande, botão de disparo e voltar (accessibility, img 0021 e 0022).
- O Zoom do visionOS é uma lente circular que amplia só a região sob ela, sobre uma janela flutuante num ambiente real (accessibility, img 0023).
- No Pointer Control por cabeça o conteúdo se move sob um alvo fixo, em vez de um cursor se mover sobre conteúdo parado (accessibility, vídeo 001, folhas 0001 e 0002).
- Cada propriedade física do Apple Pencil ganha um sistema gráfico próprio de medição na mesma cor azul: arco de graus para altitude, espessura progressiva para pressão e círculo graduado para azimute (apple-pencil-and-scribble, img 0148 a 0150).
- A prévia de hover do Pencil é reprovada quando pequena demais e aprovada no tamanho médio da faixa (apple-pencil-and-scribble, img 0153 a 0157).
- Um campo estreito demais corta a escrita à mão do Scribble, e o campo largo que comporta o nome inteiro é o aprovado (apple-pencil-and-scribble, img 0158).
- A barra de armazenamento é uma única barra horizontal dividida em nove segmentos de cores distintas, separados por fino espaço em branco, com legenda de bolinha e texto abaixo (charts, img 0244).
- O eixo pode ser fixo ou dinâmico conforme o dado: nível de bateria mantém o eixo de 0% a 100%, e o gráfico de passos muda o topo do eixo de 6.000 na semana para 10.000 no mês (charts, img 0239 a 0241).
- O indicador de foco de leitor de tela aparece como retângulo de contorno cobrindo só o trecho relevante do gráfico, e não o gráfico inteiro (charts, img 0245).
- A frase de permissão da colaboração é ensinada trocando só o resumo de uma linha acima dos avatares, "Only invited people can edit." e depois "Everyone can make changes." (collaboration-and-sharing, img 0248 e 0249).
- A máscara circular do Game Center é de 512 pt tocando as quatro bordas do quadrado de 512x512 pt em iOS, iPadOS, macOS e visionOS, mas de 200 pt centralizada num quadrado de 320x320 pt no tvOS (game-center, img 0496 e 0497).
- A arte de challenge é um retângulo de 1920x1080 pt com área de corte central de 1465x1080 pt, que preserva a altura total e descarta margens estreitas nas laterais (game-center, img 0505 e 0511).
- O sistema fornece um degradê escuro na base da arte para dar legibilidade ao texto sobreposto, em vez de exigir que o desenvolvedor escureça a imagem (game-center, img 0504 e 0510).
- O cartão de conquista bloqueada é um círculo cinza uniforme com cadeado e sem título visível, enquanto a obtida traz imagem colorida, data em arco ao redor e texto legível (game-center, img 0493).
- O disclosure do diálogo de salvar do macOS faz a própria janela crescer até virar navegador de arquivos completo, com barra lateral, colunas, busca e New Folder, sem mexer no campo de nome do topo (disclosure-controls, img 0467 e 0468).
- Em paisagem na tela externa do iPhone Duo, toolbar e tab bar nunca aparecem cheias ao mesmo tempo: ou a toolbar recolhe num botão de reticências, ou a tab bar recolhe num único botão (designing-for-iphone-duo, img 0454 e 0455).
- A região de câmera interna fica dentro da região de dobra, no centro da tela aberta (designing-for-iphone-duo, img 0440 e 0445).
- No Notes com o aparelho todo aberto a coluna da lista é bem mais estreita que a de conteúdo, e parcialmente dobrado as duas passam a ter a mesma largura (designing-for-iphone-duo, img 0446 e 0447).
- Os oito princípios de design são comunicados só por pictogramas isolados, sem texto, legenda, fotografia ou tela, todos no mesmo gradiente verde e no mesmo traço (design-principles, img 0425 a 0432).
- O combo box prova a entrada livre pelo detalhe do cursor de texto logo após um valor que não está entre as opções da lista aberta (combo-boxes, img 0343).
- O document launcher separa em camadas o que é marca do app, fundo ilustrado, mascote, título grande e botão primário azul, do que é controle padrão do sistema, o navegador de arquivos neutro na parte de baixo (file-management, img 0480).
- O halo de foco do iPadOS aparece em duas variantes na mesma grade de fotos, uma colada à borda com cantos retos e outra afastada com cantos arredondados, mantendo a mesma cor (focus-and-selection, img 0482 e 0483).
- A Digital Crown é isolada de duas maneiras diferentes em fotos reais de produto: pelo dedo pousado sobre ela no Vision Pro e por um contorno vermelho desenhado sobre a foto no Apple Watch, com o botão lateral logo abaixo deixado sem destaque (digital-crown, img 0462 e 0463).
- Um shortcut de conteúdo carrega atrás do símbolo uma miniatura da própria nota, com linhas de pauta ou a lista de nomes visíveis, o que o torna reconhecível pelo conteúdo e não pelo rótulo (app-shortcuts, img 0091).
- O App Clip aberto é uma tela funcional completa, com lista de itens, preços, controles de quantidade e botão de pedido com contagem, e não uma prévia do app (app-clips, img 0055).
- No CareKit os quatro estilos de tarefa reaproveitam o mesmo cartão branco e trocam só o subview, e o header resume o que falta, como "1 remaining" (carekit, img 0219 a 0223).
- O coaching de AR e a relocalização reaproveitam o mesmo indicador de superfície translúcido e pontilhado, mudando só o texto e acrescentando um botão "Start Over" no caso de interrupção (augmented-reality, img 0162 e 0172).
- Iluminação suficiente e insuficiente são a mesma cena no mesmo ângulo, apenas em tom claro e escuro, apresentadas sem marcador de certo ou errado (augmented-reality, img 0173 e 0174).
- A dica de rotação em 3D destaca a face do cubo e a circunda com seta curva, e a alternativa 2D troca isso por um rótulo "Rotate" em cápsula escura abaixo do objeto (augmented-reality, img 0168 e 0169).
- O diagrama de código de acesso cota o respiro em volta de cada bloco, acima do título, nas laterais da fileira de caixas, entre as caixas, entre caixas e teclado e entre teclado e borda inferior (digit-entry-views, img 0460).
- A seleção de texto é construída com fundo destacado sobre a palavra, cursor vertical à direita e duas alças circulares nas pontas, uma acima à esquerda e outra abaixo à direita (edit-menus, img 0471).
