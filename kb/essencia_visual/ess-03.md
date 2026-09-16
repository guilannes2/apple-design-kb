# Essência visual, lote ess-03

Base: 47 sínteses visuais de páginas do HIG, de pointing-devices a web-views.

## Toda capa de página é o mesmo desenho de construção: símbolo chapado numa cor do logo antigo de seis cores, sobre gradiente, com a grade tracejada e os círculos concêntricos deixados à vista
- Evidência: printing (img 0889, impressora vermelha sobre gradiente laranja com malha retangular e círculo concêntrico no corpo)
- Evidência: settings (img 1001, engrenagem com os raios internos alinhados às diagonais da grade)
- Evidência: searching (img 0994, aro da lupa concêntrico ao círculo guia, cabo coincidindo com a diagonal)
- Evidência: siri (img 1079, anel azul com circunferência guia menor marcando a proporção do traço interno)
- Evidência: undo-and-redo (img 1205), remotes (img 0921), shazamkit (img 1027), wallet (img 1229), privacy (img 0890)
- O que isso ensina sobre construir interface: a marca de qualidade da Apple não é o desenho final, é a malha por baixo dele; qualquer símbolo de sistema nasce de um círculo guia e de eixos comuns, o que faz peças desenhadas por pessoas diferentes parecerem da mesma família.

## A abertura de um componente é ficha técnica cotada, não captura de app: o componente aparece isolado, com setas de régua de largura e altura
- Evidência: pop-up-buttons (img 0883, setas cotando a largura do menu e a altura da linha selecionada)
- Evidência: steppers (img 1107, chave horizontal de largura no topo e chave vertical de altura à direita)
- Evidência: text-views (img 1143) e text-fields (img 1138, mesma construção, mudando só o conteúdo de exemplo)
- Evidência: toggles (img 1147), tab-views (img 1118, cotas nas quatro bordas do contêiner), web-views (img 1285), popovers (img 0886), sliders (img 1080)
- O que isso ensina sobre construir interface: antes de ser conteúdo, o componente é uma caixa com dimensões declaradas; documentar o retângulo e sua altura de linha vem antes de documentar o comportamento.

## Certo e errado vêm em pares que mudam uma variável só, e o selo de julgamento fica isolado num quadro próprio, nunca sobre o exemplo
- Evidência: voiceover (img 1225 a 1228, mesma tela e mesmo conteúdo, muda só onde a borda de agrupamento é desenhada; X e check em imagens separadas)
- Evidência: sign-in-with-apple (img 1059 a 1062, botão branco idêntico, varia só o fundo, cinza escuro com check e cinza claro com X)
- Evidência: toolbars (img 1166 a 1169, cápsula com a palavra "Back" recebe X, botão circular só com o símbolo recebe check, selos ao lado e nunca em cima)
- Evidência: typography (img 1201 a 1204), wallet (img 1236 a 1239), sheets (img 1032 a 1035), snippets (img 1092 a 1095)
- O que isso ensina sobre construir interface: para ensinar uma regra, congele tudo e mexa num parâmetro; e mantenha o veredito fora do artefato, para que a imagem continue servindo de referência de pixel.

## Antes e depois reaproveita a tela inteira, incluindo foto, texto e controles, trocando só o elemento em discussão
- Evidência: status-bars (img 1105 e 1106, mesma foto e mesmo enquadramento, com e sem as barras)
- Evidência: scroll-views (img 0981 e 0982, mesma palmeira e mesma barra superior, muda só o tratamento do desfoque)
- Evidência: toggles (img 1148 e 1149, mesmo cartão e mesmas linhas, muda só a cor do estado ligado)
- Evidência: pop-up-buttons (img 0884 e 0885), pull-down-buttons (img 0916 e 0917), popovers (img 0887 e 0888), tab-bars (img 1114 e 1115)
- O que isso ensina sobre construir interface: comparação convincente exige contexto idêntico; recriar a tela para o segundo caso introduz ruído e deixa o leitor sem saber o que mudou.

## Seleção se anuncia por preenchimento de fundo atrás do elemento, quase nunca por borda, sublinhado ou cor de texto sozinha
- Evidência: segmented-controls (img 0996 e 0997, segmento ativo em azul sólido com glifo branco; img 0998 e 0999, segmento ativo em branco elevado sobre cinza)
- Evidência: tab-views (img 1118 e 1119, aba ativa marcada por fundo mais opaco, e os divisores somem ao lado dela)
- Evidência: tab-bars (img 1108, fundo branco com ícone preto na aba selecionada; img 1116 e 1117, círculo de fundo mais claro no ícone destacado no visionOS)
- Evidência: toggles (img 1150 e 1151, botão de filtro comunica estado por preenchimento atrás do símbolo, sem trilho de switch), sidebars (img 1047), toolbars (img 1182)
- O que isso ensina sobre construir interface: o estado ativo precisa de área, não de contorno; um fundo preenchido sobrevive a tela pequena, a daltonismo e a fundo com imagem, coisa que um sublinhado fino não faz.

## A pílula é a unidade universal de agrupamento e de estado
- Evidência: tab-bars (img 1108, quatro abas dentro de um contêiner em pílula, com a busca fora dele)
- Evidência: toolbars (img 1163 e img 1176 a 1179, controles reunidos numa cápsula única ou repartidos em duas cápsulas conforme o parentesco das ações)
- Evidência: token-fields (img 1160 a 1162, destinatário convertido vira pílula visualmente distinta do texto solto)
- Evidência: typography (img 1194, nomes de plantas ganham cápsula translúcida para ficarem legíveis sobre o cenário), sliders (img 1086), steppers (img 1107), search-fields (img 0993)
- O que isso ensina sobre construir interface: a cápsula resolve duas coisas ao mesmo tempo, diz o que anda junto e cria o piso de contraste onde o texto flutuaria; adotá-la como forma base reduz a quantidade de decisões de borda.

## A busca nunca divide o mesmo contêiner com os destinos de navegação
- Evidência: search-fields (img 0985 e 0986, primeiro a busca é o quinto item dentro do agrupamento das abas, depois vira botão circular separado, fora do grupo, na borda final)
- Evidência: tab-bars (img 1108, a anatomia já nasce com a pílula de abas de um lado e o botão circular de busca do outro; img 1113, mesmo no estado minimizado a busca fica em botão isolado à direita)
- Evidência: search-fields (img 0988, na toolbar superior a lupa se agrupa com o botão de mais opções e não com o de adicionar)
- O que isso ensina sobre construir interface: busca é ação, não lugar; misturá-la com destinos faz o usuário ler um verbo como se fosse uma seção.

## Anatomia é ensinada por callout de linha reta que sai do elemento e termina num rótulo fora do desenho
- Evidência: status-bars (img 1104, cada ícone desce por uma linha fina até o rótulo, com a chamada do Wi-Fi cruzando por baixo da do sinal celular)
- Evidência: typography (img 1198, screenshot real do Mail com Large title, Title, Subtitle e Body text apontando para os trechos correspondentes)
- Evidência: toolbars (img 1175, rótulos de zona dividindo a barra do Freeform em três regiões; img 1180, callouts nomeando a toolbar e a moldura da janela do Finder)
- Evidência: split-views (img 1099), tab-bars (img 1110), search-fields (img 0984), snippets (img 1091), wallet (img 1268)
- O que isso ensina sobre construir interface: nomear regiões com linha e rótulo externo mantém a captura intacta e ensina vocabulário; é o mesmo hábito que faz um design system ter nomes estáveis para as zonas de uma barra.

## Menu é cartão flutuante com sombra que cobre parte do conteúdo de trás, e nunca uma tela nova
- Evidência: pop-up-buttons (img 0885, o menu emerge sobre a própria lista e cobre parcialmente as linhas vizinhas)
- Evidência: pull-down-buttons (img 0917, cartão branco com sombra sobre a nota, misturando uma fileira de ícones no topo com lista vertical abaixo)
- Evidência: the-menu-bar (img 1145, no iPad o menu de edição repete a estrutura do macOS como painel claro flutuante sobre a tela preta)
- Evidência: token-fields (img 1161 e 1162), search-fields (img 0989 e 0990, sugestões logo abaixo do campo com a primeira realçada)
- O que isso ensina sobre construir interface: escolher um valor não é mudar de lugar; manter a origem visível ancora a decisão e devolve o usuário ao contexto sem navegação.

## Divisor fino cria grupos dentro do menu, e o que é destrutivo ou fora do padrão fica isolado no fim
- Evidência: pull-down-buttons (img 0917, ação destrutiva por último, separada e em vermelho)
- Evidência: the-menu-bar (img 1144, menu de edição em três grupos, desfazer e refazer, depois recortar, copiar, colar e apagar, e buscar por último)
- Evidência: token-fields (img 1162, menu do token em quatro blocos separados por divisórias, do endereço atual até a busca pelo nome)
- Evidência: pop-up-buttons (img 0885, a opção personalizada fica isolada no fim por um separador)
- O que isso ensina sobre construir interface: hierarquia dentro de um menu se faz com espaçamento e ordem, não com negrito; a última posição é a mais cara de alcançar e por isso é onde vai o irreversível.

## Hierarquia de botões é peso de preenchimento, e o inativo é o mesmo botão desbotado, não um botão cinza diferente
- Evidência: researchkit (img 0927, decisão assimétrica com "Disagree" como texto simples e "Accept" como botão amarelo sólido; img 0929, o mesmo amarelo em versão pálida enquanto nada foi selecionado)
- Evidência: sheets (img 1037 a 1039, sequência de três quadros em que o check passa de cinza inativo a azul ativo e o X vira seta de voltar, uma máquina de estados ensinada por comparação)
- Evidência: snippets (img 1089, "Cancel" cinza claro à esquerda e "Order" azul e mais largo à direita), shazamkit (img 1028, "Not Now" cinza e "Allow" azul), sign-in-with-apple (img 1054, "Create Account" neutro acima do botão preto da Apple)
- O que isso ensina sobre construir interface: manter matiz e trocar saturação preserva a identidade do botão entre estados; trocar por cinza genérico faz o usuário procurar um controle novo em vez de reconhecer o mesmo.

## O mesmo componente atravessa plataformas mantendo a função e trocando cor, material e forma
- Evidência: progress-indicators (img 0907 e 0908, azul sobre cinza claro no macOS; img 0913 e 0914, branco sobre cinza escuro dentro de uma moldura preta que imita o mostrador no watchOS)
- Evidência: sliders (img 1082, trilha azul em cartão cinza no macOS; img 1086 e 1087, cápsula preta compacta com preenchimento verde e ícones de volume nas pontas no watchOS)
- Evidência: sheets (img 1030 metade inferior no iPhone, img 1042 cartão centralizado sobre janela escurecida no macOS, img 1043 tela cheia no watchOS, vídeo 053 crescendo a partir do centro no visionOS)
- Evidência: toolbars (img 1163, 1181, 1183), tab-bars (img 1109, 1114, 1116), search-fields (img 0983, 0990, 0993)
- O que isso ensina sobre construir interface: o que é portável é o papel do componente e sua posição no fluxo; cor, material e ponto de entrada são propriedades locais da plataforma e devem ser tratados como tokens, não como parte da definição.

## No watchOS a navegação entre páginas vira uma coluna de marcas junto à Digital Crown, sem texto nem setas
- Evidência: split-views (img 1103, coluna fina de marcas com um segmento mais alongado e claro em destaque, ao lado de uma lista sobre fundo preto)
- Evidência: tab-views (img 1120, ponto atual maior e branco numa coluna vertical, sendo o único elemento de navegação da tela)
- O que isso ensina sobre construir interface: quando a tela não comporta um controle, o indicador migra para a borda e se apoia no hardware; a posição do controle físico vira parte da gramática visual.

## Camadas se resolvem por translucidez e desfoque, com o fundo continuando atrás em vez de ser cortado
- Evidência: sidebars (img 1048 com X, imagem de flores parando na borda da sidebar sem transição; img 1050 com check, a mesma imagem seguindo borrada e espelhada atrás dos itens até a borda da janela)
- Evidência: scroll-views (img 0981, borda hard com desfoque opaco terminando em linha definida; img 0982, borda soft dissolvendo no conteúdo e deixando título e botões quase flutuando)
- Evidência: toolbars (img 1181 e 1182, barra translúcida no visionOS com o ambiente desfocado visível através do material), tab-bars (img 1116 e 1117), snippets (img 1089 e 1090, tela inicial desfocada atrás do cartão), sheets (vídeo 053, janela pai perdendo nitidez depois que a sheet aparece)
- O que isso ensina sobre construir interface: a junção entre camadas é o lugar onde uma interface parece barata ou cara; resolver por dissolução em vez de corte custa uma linha de CSS e muda a percepção da peça inteira.

## Guias horizontais vermelhas de altura de caixa alta e linha de base medem a relação entre texto e qualquer elemento vizinho
- Evidência: sf-symbols (img 1015 a 1017, o mesmo símbolo de mais ao lado da palavra "Add" em small, medium e large, com o círculo ficando abaixo, levemente acima e nitidamente acima das duas guias)
- Evidência: typography (img 1195 e 1196, SF Pro e New York comparadas com o mesmo pangrama entre duas linhas azuis de caixa alta e linha de base)
- Evidência: right-to-left (img 0953 e 0954, três botões com o mesmo rótulo em latim, árabe e hebraico; no mesmo corpo só o latim toca as duas guias, e com a fonte árabe e hebraica um pouco maior o peso visual se equilibra)
- O que isso ensina sobre construir interface: alinhamento óptico se prova com duas linhas desenhadas, não com opinião; e igualar o valor numérico de tamanho entre escritas diferentes produz desequilíbrio, não consistência.

## Zonas seguras e áreas reservadas são desenhadas como retângulos concêntricos ou blocos sólidos por cima da arte acabada
- Evidência: top-shelf (img 1188 a 1190, três retângulos concêntricos com réguas à direita para tamanho real, zona segura em foco e tamanho sem foco, o mesmo esquema repetido em 2:3, 1:1 e 16:9)
- Evidência: wallet (img 1261 a 1264, a mesma ilustração aparece acabada e depois coberta por blocos azuis que marcam o cabeçalho no topo e a área de código e rodapé embaixo, em forma de T quando o código é QR)
- Evidência: spatial-layout (img 1097, campo de visão como três circunferências de 30, 60 e 90 graus sobre o render da sala, com a janela do app quase toda dentro do círculo de 60), sf-symbols (img 1002)
- O que isso ensina sobre construir interface: quem entrega arte precisa ver o recorte, não ler sobre ele; sobrepor a máscara à peça real é a forma mais rápida de comunicar sangria e margem de segurança.

## Variação sistemática é apresentada em matriz: um eixo por parâmetro e a mesma forma repetida em todas as células
- Evidência: sf-symbols (img 1014, 27 amostras do mesmo símbolo de pasta com mais, nove colunas de Ultralight a Black por três linhas de escala; img 1018, grade de dois por cinco com outline em cima e fill embaixo; img 1019, oito linhas por onze colunas trocando só o caractere interno por escrita)
- Evidência: typography (img 1197, a palavra "Text" em nove pesos por duas linhas, romano e itálico, sem nenhuma interface em volta)
- Evidência: virtual-keyboards (img 1207 a 1218, cada tipo de teclado na mesma composição, nome em cinza no topo, campo com placeholder e teclado alinhado à base, o que permite comparar tecla a tecla)
- Evidência: wallet (img 1278 a 1283, o mesmo esqueleto de três linhas repetido por estilo de passe, mudando o uso das linhas mas nunca a quantidade), toggles (img 1153 a 1158)
- O que isso ensina sobre construir interface: a matriz revela a falha de cobertura que a amostra escolhida esconde; se um parâmetro merece existir, ele merece uma linha ou coluna própria.

## A Apple mostra o que acontece quando o espaço falta, e trata a degradação como projeto e não como acidente
- Evidência: toolbars (img 1164 e 1165, ao estreitar a janela do Notes sobram poucos ícones e surge um botão de overflow com seta dupla cujo menu recolhe inclusive o próprio More)
- Evidência: typography (img 1199 e 1200, a mesma mensagem do Mail no tamanho padrão e no maior tamanho de acessibilidade, com o nome quebrando em duas linhas, o corpo cortado no começo e os ícones do rodapé sobrepostos ao texto)
- Evidência: text-fields (img 1140 a 1142, a mesma frase cortada na borda sem reticências, quebrada em duas linhas e truncada com reticências)
- Evidência: tab-bars (img 1112 e 1113, barra com acessório expandido e depois minimizada num botão circular mais pílula), virtual-keyboards (img 1219 a 1223, o botão Sign In some atrás do teclado e depois aparece cortado ao meio pela barra de sugestões)
- O que isso ensina sobre construir interface: cada componente precisa de uma regra declarada de o que some primeiro; sem isso, a decisão cai no navegador e o que desaparece é justamente o botão de ação.

## Indeterminado se distingue de determinado pela ausência de fim visível, e o spinner cinza aparece sempre acompanhado de texto de estado
- Evidência: progress-indicators (img 0912, barra indeterminada toda preenchida com gradiente forte no centro e quase transparente nas pontas, sugerindo onda em vez de avanço; img 0911, spinner cinza abaixo da barra de status do Mail com o texto "Updated Just Now")
- Evidência: tap-to-pay-on-iphone (img 1126 barra parcial no preparo, img 1127 barra cheia tratada como indeterminado, img 1132 a barra dá lugar a um spinner cinza ao lado do rótulo "Authorizing")
- Evidência: wallet (img 1265 e 1266, barra verde parcial no pedido feito, que desaparece e vira check verde ao ser entregue)
- O que isso ensina sobre construir interface: espera sem previsão precisa de forma própria e de legenda; reaproveitar a barra determinada para o caso indeterminado promete um fim que o sistema não pode cumprir.

## Nos vídeos o efeito é isolado sobre cena neutra, os elementos animam defasados entre si e o rótulo de texto só entra depois que o efeito já foi visto
- Evidência: sf-symbols (vídeo 042, os três símbolos aparecem escalonados de um quadro vazio até os três presentes; vídeo 045, cada símbolo reduz e volta fora de fase dos outros; vídeo 046, só uma camada de cada símbolo pulsa por vez; vídeo 051, um símbolo respira por vez em rodízio ao longo de quatro folhas)
- Evidência: spatial-layout (vídeos 057 e 058, mesma cena cinza de teste com piso quadriculado, contorno amarelo vazado como referência contra a janela real preenchida, e as legendas "Dynamic Scale" e "Fixed Scale" entrando só na segunda metade)
- Evidência: tab-bars (vídeo 059, a barra sai de seis ícones sem texto para os rótulos por extenso e volta ao recolhido, sempre no mesmo enquadramento), sheets (vídeo 053, quatro quadros mostrando só o crescimento a partir do centro)
- O que isso ensina sobre construir interface: animação simultânea em todos os elementos lê como falha de renderização; a defasagem é o que transmite que o sistema está processando item por item, e a legenda depois do efeito evita que o texto substitua a observação.

## Modal sempre expõe a saída, e a única exceção deliberada é a tela que antecede um pedido de permissão
- Evidência: sheets (img 1032 com X, topo com grabber, título e só o botão azul de confirmação; img 1034 com check, X cinza de cancelar à esquerda, título ao centro e confirmação à direita; img 1036, reunir voltar, X e check ao mesmo tempo é o padrão a evitar)
- Evidência: tap-to-pay-on-iphone (img 1125, tutorial em folha modal com X circular cinza no canto superior direito), researchkit (img 0929 e 0930, "x" branco de fechar no canto superior esquerdo nas telas de pesquisa e tarefa)
- Evidência: privacy (img 0898 e 0899, a mesma tela de pré-permissão recebe reprovação exatamente por ganhar um "Cancel" empilhado sob o "Next" ou um X no canto superior esquerdo)
- O que isso ensina sobre construir interface: a saída é obrigatória no modal comum porque o custo é reversível; na antessala de um alerta do sistema a saída duplicada esconde o alerta real, então a regra se inverte de propósito e vale a pena saber qual dos dois casos você está construindo.

## Botão de sistema tem desenho congelado, e a única variável permitida é o texto
- Evidência: sign-in-with-apple (img 1055 a 1057, os três títulos no mesmo botão preto com logo e texto branco; img 1068 a 1070, o raio de canto é uma progressão controlada de cantos retos ao formato de cápsula; img 1076 a 1078, o botão só com logo aparece sob três máscaras)
- Evidência: tap-to-pay-on-iphone (img 1128 a 1131, a mesma forma azul de largura total leva check com o símbolo de ondas e X com o logo da Apple no lugar dele; img 1136 e 1137, a mesma forma com o rótulo trocado)
- Evidência: wallet (img 1272 a 1275, quatro botões de verificação de identidade com um único desenho, fundo preto arredondado e ícone à esquerda, mudando só a primeira linha de texto)
- O que isso ensina sobre construir interface: quando a forma é a marca, a customização precisa ser um eixo declarado e limitado; oferecer raio, máscara e rótulo e travar o resto é mais seguro que publicar uma recomendação em prosa.

## Ícone na borda inicial e texto depois, em toda linha de lista e item de menu
- Evidência: the-menu-bar (img 1144, cada item do menu de edição tem ícone na borda inicial e atalho de teclado à direita)
- Evidência: sidebars (img 1047, ícone de pasta à esquerda, rótulo no meio e estrela à direita, com guias tracejadas verticais alinhando as duas colunas de ícone nas três linhas)
- Evidência: pull-down-buttons (img 0917, lista vertical com ícone à esquerda e alguns itens com seta de submenu e texto secundário)
- Evidência: researchkit (img 0927 e 0932), privacy (img 0891, grade de duas colunas com ícone à esquerda do texto), wallet (img 1234)
- O que isso ensina sobre construir interface: a coluna de ícones precisa ser uma coluna de verdade, alinhada entre todas as linhas; é o alinhamento, não o desenho do ícone, que faz a lista parecer organizada.

## Avaliação por estrelas é sempre uma fileira de cinco, e a diferença entre cheia e vazia é tom da mesma cor, não contorno separado
- Evidência: rating-indicators (img 0918, três cheias em vermelho escuro sólido e duas vazias em vermelho claro translúcido, sem estrela fracionada, com cotas da largura da fileira e da altura de uma estrela)
- Evidência: ratings-and-reviews (img 0919, capa com uma única estrela partida ao meio, sólida à esquerda e em contorno à direita; img 0920, as cinco estrelas do pedido de avaliação aparecem em contorno azul e todas vazias, sem nota pré-escolhida)
- Evidência: right-to-left (img 0948 a 0950, três cheias, uma pela metade e uma vazia, com o numeral centralizado sob cada estrela e a contagem invertendo o sentido nas versões RTL)
- O que isso ensina sobre construir interface: o estado se comunica na mesma família cromática, o que mantém a fileira legível de longe; e o controle de entrada nasce vazio, porque uma nota pré-marcada vira sugestão.

## Rótulo fora da caixa à esquerda, valor à direita, e o número exato mora num campo enquanto o controle contínuo entrega só a aproximação
- Evidência: sliders (img 1081, rótulo "Opacity", slider com polegar, campo com a porcentagem e stepper colado ao campo na mesma linha, o polegar dando a posição e o campo dando o número)
- Evidência: text-fields (img 1139, campos numéricos empilhados com o rótulo fora da caixa terminado em dois pontos e o valor alinhado à direita dentro do campo)
- Evidência: pop-up-buttons (img 0884, lista agrupada com rótulos à esquerda e valores à direita), researchkit (img 0931, perfil como pares de rótulo e valor com seta de navegação)
- O que isso ensina sobre construir interface: controle contínuo e campo numérico não competem, se complementam; quem precisa de precisão digita, quem precisa de velocidade arrasta, e o rótulo fora da caixa mantém a coluna de valores alinhada.

## Alerta do sistema muda de layout conforme o número de escolhas: dois botões lado a lado, três empilhados
- Evidência: privacy (img 0894 e 0895, localização e fotos com três botões empilhados, e o de localização ainda acrescenta prévia de mapa com selo "Precise: On"; img 0896, contatos com apenas dois botões lado a lado e "Allow" em azul destacado)
- Evidência: shazamkit (img 1028, alerta de microfone com "Not Now" cinza à esquerda e "Allow" azul à direita, lado a lado)
- O que isso ensina sobre construir interface: a contagem de opções determina a forma do bloco de ação; duas escolhas cabem numa linha e leem como par, três precisam de pilha para que a ordem de preferência fique clara.

## Em quase metade das páginas a imagem carrega informação que a legenda oficial não descreve, e às vezes a contradiz
- Evidência: web-views (a legenda fala só de uma bússola tingida, e a img 1285 traz também o retângulo que a emoldura e as setas de largura e altura)
- Evidência: watch-faces (a descrição fala de uma representação estilizada de mostradores em vermelho, e a img 1284 traz três mostradores nomeados por extenso, ligados por linha conectora, sobre gradiente de laranja a rosa)
- Evidência: tab-bars (o vídeo 059 mostra o leve círculo de fundo no ícone de "Memories" também no estado recolhido, em q001, q002 e q010, o que a descrição não menciona), sheets (a img 1029 acrescenta setas de medida que o texto não detalha; no vídeo 053 o fundo é uma sala de estar reconhecível, não a janela em branco descrita), sf-symbols (no vídeo 051 só a variação de opacidade é perceptível, e não o crescer e encolher que a descrição narra)
- O que isso ensina sobre construir interface: legenda e imagem envelhecem em ritmos diferentes; quem usa o HIG como fonte precisa medir na imagem e tratar o texto como resumo, não como especificação.

## Achados de fonte única

- Margem de alvo de toque com número: um botão azul com bezel recebe 12 de folga nos quatro lados, enquanto um símbolo pequeno de informação e um botão sem moldura, só com texto azul, recebem 24, ou seja, o dobro de margem para o elemento que oferece menos superfície. Referência: pointing-devices (img 0861 a 0863).
- Proporção cotada do botão customizado de login: 44 pt de altura com fonte de 19 pt e 56 pt com fonte de 24 pt, uma razão entre altura e corpo de texto perto de 2,3 nos dois casos. Referência: sign-in-with-apple (img 1074 e 1075).
- Teto de altura da área customizável de um snippet, anotado como cota vertical no único diagrama numérico da página: 400 pt para a custom view entre o bloco de diálogo no topo e o par de botões na base. Referência: snippets (img 1091).
- Imagem de produto especificada por régua de 300 px nas duas bordas, sobre fundo sólido. Referência: wallet (img 1269).
- No banner com rolagem do Top Shelf a ordem dos rótulos se inverte em relação aos formatos de proporção fixa: a zona segura em foco passa a apontar para a borda mais externa e o tamanho real para a linha intermediária. Referência: top-shelf (img 1191).
- A postura da pessoa muda a orientação do painel, não só sua altura: para quem está sentado ereto o painel nasce vertical, e para quem está reclinado numa poltrona ele nasce elevado e inclinado em direção ao rosto. Referência: spatial-layout (vídeos 054 e 055, folha 0001, q001 a q006).
- Escala dinâmica contra escala fixa, ensinadas com o mesmo recurso: um contorno amarelo vazado marca o tamanho de referência enquanto a janela real cresce ou encolhe, e a linha amarela que liga os dois passa de diagonal a vertical no fim, sugerindo que a cena gira para se reapresentar de frente. Referência: spatial-layout (vídeos 057 e 058, folhas 0001 e 0002).
- O stepper é o único controle do lote cujo comportamento vem anotado em pseudocódigo, com "i++" ligado por linha à metade superior e "i--" à inferior. Referência: steppers (img 1107).
- Teclas de contexto ocupam parte da barra de espaço sem alterar o QWERTY de base: "@" e "." no teclado de e-mail, "@" e "#" no de rede social, e ".", "/" e ".com" antes do retorno no de URL; e o teclado de busca troca o retorno cinza por uma tecla azul com seta. Referência: virtual-keyboards (img 1211, 1216, 1217, 1218).
- O estado do Shift é comunicado pelo preenchimento do glifo, não por cor de fundo: no teclado de nome e telefone as letras aparecem em minúsculas e a tecla Shift fica com contorno vazio. Referência: virtual-keyboards (img 1212 comparada a img 1210).
- Estado misto do checkbox é o mesmo quadrado azul com um traço horizontal branco no lugar do check, e não um terceiro desenho; checkbox e radio compartilham o vocabulário de preenchimento azul com marca branca interna distinta. Referência: toggles (img 1153, 1155, 1157).
- Radio buttons na horizontal recebem blocos de mesma largura mesmo com rótulos de tamanhos muito diferentes. Referência: toggles (img 1159).
- Número mantém a ordem interna dos dígitos em latim, hebraico e árabe, no mesmo corpo e peso do texto que o cerca, inclusive na variante com algarismos arábicos orientais. Referência: right-to-left (img 0944 a 0947).
- Espelhamento em RTL é decidido por componente e não pela tela: a guia de alinhamento e o texto viram de lado enquanto o ícone de imagem central permanece no mesmo lugar, e num ícone composto o selo de mais acompanha a direção do carrinho apenas na variante RTL completa. Referência: right-to-left (img 0934 e 0935; img 0975 a 0977).
- Símbolos que contêm texto real são localizados, não apenas espelhados: assinatura, documento com letra e letra grande com cursor aparecem em latim, hebraico e árabe, com o caractere migrando para o canto oposto. Referência: right-to-left (img 0963 a 0965).
- O badge da tab bar é um círculo vermelho preso ao canto superior direito do ícone, e aparece sem número na instância mostrada. Referência: tab-bars (img 1111).
- O popover anexado perde a ponta que o ligava à origem quando é destacado, e só então ganha barra de título com X de fechar; o conteúdo interno permanece idêntico. Referência: popovers (img 0887 e 0888).
- Ao ocultar a interface em mídia de tela cheia, a status bar e a barra de navegação somem juntas, como uma camada só. Referência: status-bars (img 1105 e 1106).
- A borda de agrupamento do VoiceOver define o que é lido como uma unidade: envolver duas fotos e suas duas legendas é reprovado, envolver uma foto com a sua legenda é aprovado. Referência: voiceover (img 1225 a 1228).
- Texto de diálogo que repete nome, data e horário já visíveis no cartão interno é reprovado; o exemplo aprovado elimina o diálogo e deixa a informação só dentro da view. Referência: snippets (img 1092 a 1095).
- Na antessala de uma permissão, além da saída, também são proibidos incentivo financeiro (cifrão em círculo roxo com oferta de crédito), gráfico de benefício crescente e reprodução anotada do alerta real do sistema com o botão desejado circulado ou apontado por seta. Referência: privacy (img 0900 a 0903).
- Consentimento de pesquisa usa check verde por item ao lado do parágrafo legal e da assinatura digitada, com a decisão final assimétrica de propósito, "Disagree" como texto simples e "Accept" como botão sólido. Referência: researchkit (img 0927).
- Progresso de fluxo longo aparece escrito e desenhado ao mesmo tempo, com a contagem em texto ("Step 1 of 5") ao lado de uma barra na posição correspondente. Referência: researchkit (img 0925, 0926, 0929).
- Os três templates espaciais do SharePlay comunicam a diferença só pela posição relativa entre pessoas e conteúdo, sem texto, régua ou anotação: enfileiradas voltadas para um painel, em círculo ao redor de uma esfera, ou em meio círculo fechado com o painel empurrado para a borda. Referência: shareplay (img 1024 a 1026).
- No controle segmentado de alinhamento, uma linha divisória vertical fina separa o último ícone dos três primeiros, sugerindo subgrupo dentro do mesmo controle. Referência: segmented-controls (img 0996).
- Tick marks podem cobrir toda a trilha e não só a parte preenchida, e nem toda marca recebe rótulo: no painel Energy Saver só alguns pontos da escala são nomeados. Referência: sliders (img 1083 e 1085).
- Um menu bar extra tem menu mais compacto e sem atalhos de teclado ao lado dos itens, ao contrário dos menus da barra principal. Referência: the-menu-bar (img 1146).
- No cupom do Wallet o campo primário fica sobreposto à faixa ilustrada do topo, e não ao lado dela, coisa que só o diagrama com retângulos tracejados deixa claro. Referência: wallet (img 1243 e 1258).
- O Pass Designer no Mac organiza a edição numa árvore lateral por tipo de campo, cabeçalho, primário, rodapé e verso, com a prévia à direita e uma etiqueta de versão mínima do iOS acima dela. Referência: wallet (img 1235).
- O ponteiro no iPadOS é um círculo cinza que escurece e cresce ao se aproximar do botão e clareia e encolhe ao se afastar, enquanto o preenchimento do próprio botão não muda de cor. Referência: pointing-devices (vídeo 038, folha 0001, q001 a q007).
- A seleção de um objeto é desenhada com alças quadradas brancas nos cantos e nos pontos médios, uma alça central com setas, e uma etiqueta escura ao lado mostrando largura e altura em pontos. Referência: pointing-devices (img 0864).
