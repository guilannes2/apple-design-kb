# Essência visual do lote ess-13

Base: 17 sínteses visuais de vídeo (WWDC 2025 e 2026), lidas por inteiro.

## Um sumário lateral em texto puro marca o progresso, e só o item corrente muda de peso e de cor
- Evidência: wwdc2025_359 (folhas 0001, 0002, 0004 a 0007, 0009, 0011 e 0012; quatro palavras alinhadas à esquerda, corrente em preto espesso, demais em cinza claro fino, sem ícone nem numeração)
- Evidência: wwdc2026_250 (folhas 0004 a 0014; a lista cresce de dois para sete nomes e a fala nunca cita o recurso)
- Evidência: wwdc2026_251 (folha 0002 q0016 e q0017, folha 0006 q0046, folha 0007 q0062, folha 0009 q0079, folha 0011 q0095)
- Evidência: wwdc2026_321 (folhas 0007, 0011 e 0013, com as próprias notas registrando divergência sobre em quais folhas o slide reaparece)
- O que isso ensina sobre construir interface: hierarquia de navegação pode ser feita só com peso e cor do mesmo tamanho de tipo, sem barra, sem número e sem ícone. O estado atual fica legível porque tudo em volta recua, não porque o item ativo ganha decoração.

## Listas, tabelas, código e inventários são montados peça por peça na frente de quem assiste, no compasso da fala
- Evidência: wwdc2025_404 (folha 0007, q0057 a q0063: a tabela de vocabulário nasce só com os três cabeçalhos, depois o termo aceito, depois os evitados, depois a definição, e a linha seguinte já começa vazia)
- Evidência: wwdc2026_234 (folha 0008, q0069 a q0072: os cartões de material de referência entram um por quadro numa fileira, sempre preservando os anteriores na mesma posição)
- Evidência: wwdc2026_290 (folha 0005, q0042 a q0045: as colunas de post-its se preenchem uma por vez)
- Evidência: wwdc2026_269 (folha 0009, q0073 a q0081: a classe parte de uma casca vazia e ganha conformidade, lista de tipos, método de snapshot e writer)
- O que isso ensina sobre construir interface: mostrar a construção ensina a estrutura melhor do que mostrar o resultado pronto, porque a ordem de entrada revela o que depende do quê. Vale para onboarding, formulários longos e qualquer tela que precise justificar a própria complexidade.

## Certo e errado são julgados por ícone colorido ancorado ao elemento, não por palavra escrita
- Evidência: wwdc2025_323 (folha 0006, q0049 com círculo vermelho e X no fundo customizado, q0050 com check verde na transição de zoom; folha 0015, q0135, X vermelho sobre duas regiões de amostragem sobrepostas)
- Evidência: wwdc2025_404 (folha 0005, q0037 a q0040: os dois cartões aparecem empilhados, o antigo com X vermelho e o novo com check verde, e isso acontece uma única vez no vídeo inteiro)
- Evidência: wwdc2026_227 (folha 0004, q0031 a q0033: a lista de críticas usa X vermelho para problema de layout e ponto de exclamação laranja para risco, e a diferença de severidade por cor nunca é verbalizada)
- Evidência: wwdc2026_321 (folhas 0005, 0006, 0007, 0009, 0011, 0012, 0013 e 0014: círculo laranja com exclamação para a prática problemática e círculo verde com marca para a corrigida, reutilizados sistematicamente)
- O que isso ensina sobre construir interface: um par pequeno de ícones com cor fixa carrega julgamento sem ocupar linha de texto, e sustenta uma gradação de severidade (alerta laranja é diferente de erro vermelho) que o leitor aprende na primeira ocorrência e reconhece em todas as outras.

## Um rótulo curto ligado por linha fina ao ponto exato da tela é a forma padrão de nomear anatomia
- Evidência: wwdc2025_323 (folha 0010 q0085 com "Search Field" sobre os campos do MacBook e do iPad, folha 0009 q0076 e q0078 com efeito de borda, folha 0008 q0071 sobre o indicador numérico do ícone de sino)
- Evidência: wwdc2025_361 (folha 0009, q0074 a q0076: setas e rótulos nomeiam sidebar, painel de prévia e inspetor do Icon Composer; folha 0010, q0087 e q0088, dividem a barra inferior em duas seções)
- Evidência: wwdc2026_251 (folha 0003, q0019 a q0022, e folhas 0004, 0011 e 0013: texto cinza fino ligado por linha reta, do começo ao fim, sem a fala verbalizar a convenção)
- Evidência: wwdc2026_292 (folha 0004 q0034 e q0035, folha 0005 q0040 e q0041, folha 0014 q0119: o rótulo aponta de fora da moldura para uma linha específica do estado vazio)
- O que isso ensina sobre construir interface: vocabulário de componente se fixa quando o nome encosta no pixel. A mesma convenção serve para documentação interna, handoff e revisão, desde que o estilo do rótulo seja discreto o bastante para não competir com a interface anotada.

## O ensino acontece na diferença entre dois quadros consecutivos, com uma variável mudando de cada vez
- Evidência: wwdc2025_337 (folha 0004, q0029 para q0030: o campo de reversão só aparece quando a animação muda de desenhar para apagar, revelando uma regra de estado da interface)
- Evidência: wwdc2025_361 (folha 0013, q0109 a q0111: sombra neutra contra sombra cromática, depois a mesma sombra ganhando a linha extra de modo escuro, isolando uma propriedade por par)
- Evidência: wwdc2026_290 (folha 0002 q0018 e folha 0003 q0019 a q0024: o card do Apple Cash mantém layout idêntico e só o texto do rótulo muda entre quadros)
- Evidência: wwdc2026_250 (folha 0013, q0111 para q0112: o botão em pílula troca o texto por spinner; folha 0012, q0104 para q0105: o botão circular de pausa vira pílula com play e barra de progresso)
- O que isso ensina sobre construir interface: comparar estados só é honesto quando tudo o resto fica congelado. Manter posição, tamanho e cor do entorno é o que transforma a troca em prova, e é exatamente a disciplina que falta na maioria dos antes e depois de portfólio.

## Código e resultado dividem o quadro, com o trecho relevante realçado e o realce andando junto da fala
- Evidência: wwdc2025_323 (folhas 0004 q0031, 0005 q0039, 0011 q0093, 0014 q0125 e 0016 q0136: código à esquerda, aparelho à direita, trecho realçado a cada troca de assunto; folha 0007, q0062 para q0063, o realce migra do espaçador para o item de inspetor sem o mockup mudar)
- Evidência: wwdc2026_314 (folha 0003 q0027 e folhas 0004 a 0006: CSS monoespaçado à esquerda com a linha relevante em fundo azul claro e diagrama de blocos à direita reagindo, template idêntico para sete conceitos seguidos)
- Evidência: wwdc2026_315 (folhas 0003, 0004 e 0005: cada novo bloco de CSS aparece junto do controle já com o efeito aplicado)
- Evidência: wwdc2026_269 (folhas 0003, 0012, 0013 e 0016: o código entra sobreposto em transparência parcial sobre o app rodando, deixando o resultado visível ao fundo)
- O que isso ensina sobre construir interface: causa e efeito precisam caber no mesmo enquadramento. Quando o realce de uma linha muda sem que o resultado mude, fica provado que aquela linha não é a responsável, e isso é informação que nenhum texto entrega tão rápido.

## O conteúdo avança por acréscimo de uma propriedade por vez, sempre mantendo o que já estava
- Evidência: wwdc2026_314 (folha 0004, q0028 a q0031: primeiro o modo de exibição, depois o gabarito de colunas, depois o espaçamento, com o diagrama se redesenhando a cada acréscimo)
- Evidência: wwdc2026_315 (folha 0003, q0019 a q0023: aparência nativa, borda retangular com fonte herdada, botão arredondado com seta customizada, botão sólido no estado aberto)
- Evidência: wwdc2025_337 (folha 0015, q0128 a q0132: o realce azul claro avança de trecho em trecho conforme a API citada muda, dentro dos mesmos blocos comparando três frameworks)
- O que isso ensina sobre construir interface: sistema de estilo se aprende em camadas cumulativas, e quem apaga o passo anterior obriga o leitor a reconstruir o contexto. A regra vale para documentação de design tokens tanto quanto para tutorial.

## Um selo circular no canto marca o que é novo ou de qual versão é o comportamento
- Evidência: wwdc2026_269 (folhas 0008 a 0019: selo verde circular fixo no canto superior direito dos blocos de código, em dezenas de quadros, sem a narração citar a cada vez; folha 0017, q0145 a q0149, o mesmo trecho de código aparece idêntico com selo cinza de uma versão e depois verde da seguinte)
- Evidência: wwdc2025_323 (folha 0004, q0031 para q0032: selo verde apontando a linha exata do modificador novo dentro do bloco)
- Evidência: wwdc2026_315 (folha 0001, q0007 para q0008: marca d'água circular verde de versão sobreposta ao canto da captura do site)
- O que isso ensina sobre construir interface: disponibilidade é metadado visual, não frase. Um selo persistente e sempre na mesma posição deixa o leitor filtrar o que pode usar hoje sem interromper a leitura do conteúdo.

## Quase toda tela de resultado é enquadrada numa moldura de aparelho, e o aparelho escolhido carrega argumento
- Evidência: wwdc2025_323 (folha 0003, q0019 e q0020; folha 0007, q0059 e q0060; folha 0008, q0072: o mesmo app em MacBook, iPad e iPhone ao mesmo tempo, reforçando a ideia de família)
- Evidência: wwdc2026_269 (iPad para a loja e a biblioteca, iPhone para barra de ferramentas e ações de deslizar, MacBook para o reordenamento entre lista e grade)
- Evidência: wwdc2026_290 (folhas 0002 e 0003: todas as telas em moldura completa de iPhone com entalhe e barra de status, e a moldura só é abandonada quando a câmera aproxima um card isolado para focar no texto)
- Evidência: wwdc2025_404 (folha 0006 q0050 traz apenas a silhueta arredondada no exemplo conceitual, enquanto folha 0009 q0075 reserva a moldura realista com entalhe, barra de status e barra de progresso ao exemplo de produto real)
- O que isso ensina sobre construir interface: a moldura declara o grau de compromisso. Silhueta vazia sinaliza conceito, moldura realista sinaliza produto, e trocar de aparelho no meio de um argumento é a forma mais barata de provar adaptação entre plataformas.

## O que não tem imagem vira diagrama abstrato de blocos e formas geométricas, sem texto dentro
- Evidência: wwdc2025_356 (folha 0004, q0028 e q0029: o cálculo do raio de canto desenhado em fundo escuro com linha do canto, círculo pontilhado no vértice e guias até o centro comum)
- Evidência: wwdc2026_314 (folha 0002, q0012 a q0016: faixas horizontais desiguais, malha pontilhada e malha de linhas com células vazias comparam três modos de layout antes de qualquer código)
- Evidência: wwdc2026_321 (folha 0002, q0015 a q0018: barras cinza de larguras variadas dentro de um retângulo vertical representam a pilha, com contorno laranja na região visível e uma régua vertical para a altura estimada)
- Evidência: wwdc2026_269 (folha 0018, q0159 a q0161, e folha 0019, q0163 a q0167: a árvore de caixas cresce camada a camada, vira fileiras de pirâmides e colapsa numa cadeia única)
- O que isso ensina sobre construir interface: quando o assunto é comportamento e não aparência, desenhar a mecânica em blocos neutros evita que o leitor confunda o exemplo com a recomendação estética. O diagrama também permite exagerar escala e quantidade, coisa que uma captura real não permite.

## Cor categórica separa papéis dentro do mesmo diagrama, e a legenda fica implícita na repetição
- Evidência: wwdc2026_269 (folha 0010 q0090 e folha 0011 q0091: cartões verdes para o lado de escrita e azuis para o lado de leitura, com o mesmo código voltando no diagrama de cartões empilhados)
- Evidência: wwdc2025_337 (folha 0011, q0093 para q0094: azul para componentes que desenham e verde para os que não desenham, com o marcador passando de contorno cinza a preenchido de verde)
- Evidência: wwdc2026_314 (folha 0005, q0040 a q0045, retângulo de contorno laranja para o item sob edição entre blocos azuis; folha 0006, q0050 a q0054, contornos verdes vazios para posições possíveis e linha laranja para o limiar)
- Evidência: wwdc2026_290 (folha 0005, q0042 a q0045: post-its azuis para o que a pessoa pensa, pêssego para o que sente e verde para o que faz)
- O que isso ensina sobre construir interface: duas ou três cores com significado fixo bastam para eliminar legenda escrita, desde que o significado nunca troque dentro da mesma peça. O erro comum é reciclar a cor para outra dimensão no slide seguinte.

## Grade exaustiva de amostras é o instrumento de verificação mostrado na tela
- Evidência: wwdc2025_337 (folha 0013, q0113 a q0116: colunas de peso da mais leve à mais pesada com a coluna de referência em negrito, primeiro esmaecidas, depois nítidas com barra de escala, depois com pontos-guia sobrepostos e por fim as nove colunas preenchidas)
- Evidência: wwdc2026_251 (folha 0011 q0092 compara as fontes do sistema por marcadores distintos de altura, largura e grade por caractere; folha 0012 q0100 traz o mesmo ícone de compartilhar em três fileiras por plataforma com oito variações cada)
- Evidência: wwdc2025_361 (folha 0002 q0017 e q0018, folha 0003 q0019 e q0021: variações de cor do mesmo ícone dispostas em fileiras horizontais sob rótulos de plataforma, sempre sobre fundo preto)
- O que isso ensina sobre construir interface: consistência se prova em matriz, não em exemplo único. Fixar uma coluna ou linha como referência e variar apenas um eixo por vez é o que torna o desvio visível a olho nu.

## As medidas exatas só existem na imagem, a fala nunca as pronuncia
- Evidência: wwdc2025_323 (folha 0012, q0105: cinco alturas de botão em pontos, de 16 a 36, uma por tamanho nomeado, enquanto a fala trata só do aumento das alturas)
- Evidência: wwdc2025_359 (folha 0012, q0104: a tabela tipográfica do sistema com cada linha renderizada no próprio estilo e o tamanho em pontos declarado ao lado)
- Evidência: wwdc2025_361 (folha 0011, q0099: o painel de material traz desfoque em 50 por cento, translucidez em 60 por cento e sombra cromática em 100 por cento)
- Evidência: wwdc2026_227 (folha 0015, q0130 para q0131: os sliders de amortecimento exibem valores numéricos à direita e mudam de posição entre quadros, registrando o ajuste ao vivo)
- O que isso ensina sobre construir interface: quem só ouve a apresentação sai sem o número que permite reproduzir o resultado. Ao documentar decisão de design, o valor precisa estar escrito no artefato visual, não confiado à narração ou à memória.

## A ferramenta real aparece na tela, quase sempre com a mesma anatomia de três colunas
- Evidência: wwdc2025_337 (folha 0004, q0028 a q0030: barra lateral de categorias, canvas central com o símbolo e inspetor à direita, com o modo customizado acrescentando um painel de camadas abaixo)
- Evidência: wwdc2025_361 (folha 0009, q0074 a q0076, e folha 0011, q0091 e q0092: lista de camadas, prévia central e inspetor com os campos e valores legíveis um a um)
- Evidência: wwdc2026_252 (folha 0003, q0025, e folhas 0005, 0009 e 0012: hierarquia à esquerda, viewport ou grafo ao centro, inspetor à direita, variando só o painel central, com o item selecionado marcado por barra sólida)
- Evidência: wwdc2026_314 (folha 0007, q0061: captura do inspetor do navegador com sobreposição colorida na grade, rótulos de tamanho de coluna e painel lateral de caixas de seleção controlando o overlay)
- O que isso ensina sobre construir interface: o padrão de três colunas com a área de trabalho no meio é tão estável entre ferramentas diferentes que virou expectativa. Mudar só o painel central entre modos preserva a orientação de quem usa.

## O componente aparece isolado sobre fundo neutro antes de entrar em contexto
- Evidência: wwdc2025_323 (folha 0002, q0011 para q0012: zoom, botão simples, botão tintado, alternador, seletor em lista e controle segmentado, primeiro sobre um iPhone central e depois soltos, antes de qualquer código)
- Evidência: wwdc2026_292 (folha 0002, q0016 a q0018: a anatomia do campo de busca em três estados sucessivos sobre fundo cinza texturizado, e só depois o padrão reaparece dentro de cada app)
- Evidência: wwdc2026_290 (folha 0001, q0005 e q0006: menu de contexto, barra de abas e cartão genéricos, já com o vermelho reservado à ação destrutiva, antes de qualquer app real entrar)
- Evidência: wwdc2026_252 (folha 0015, q0129 a q0131: o balão de fala do jogo é mostrado depois isolado como componente cinza sem borda nem sombra)
- O que isso ensina sobre construir interface: separar a peça do cenário é o que permite discutir anatomia e estados sem que o conteúdo de exemplo roube a atenção. Contexto depois, nunca antes.

## Esmaecimento e opacidade dirigem o foco e marcam hierarquia, inclusive apagando o que não está em discussão
- Evidência: wwdc2025_337 (folha 0014, q0124 para q0125: todo o painel fica esmaecido menos um botão, com linha e rótulo apontando para ele, e o alvo muda de uma camada para outra entre os dois quadros)
- Evidência: wwdc2026_250 (folha 0005, q0040 e q0041, com as duas primeiras perguntas em preto e a terceira em cinza claro; folha 0009, q0079, com um laptop opaco ao lado de um celular semitransparente)
- Evidência: wwdc2026_321 (folha 0006, q0053 e q0054: a tela de um dos dois iPhones escurece sob overlay semitransparente enquanto o rótulo e a seta permanecem visíveis)
- Evidência: wwdc2025_404 (folha 0005, q0037 a q0040: o trecho a ser fundido fica em negrito enquanto o resto do corpo do cartão cai para cinza claro)
- O que isso ensina sobre construir interface: reduzir o entorno custa menos que destacar o alvo e não introduz nenhum elemento novo na tela. É o mesmo mecanismo que sustenta modal, coach mark e estado desabilitado.

## A fidelidade cresce em degraus: contorno vazio, wireframe, mock genérico, captura real
- Evidência: wwdc2026_292 (folha 0003, q0025 e q0026: três aparelhos em wireframe evoluindo de tela em branco para tela com barra de abas e depois com título grande e campo de busca; folha 0006, q0047 para q0048, o par de abas de busca aparece primeiro em wireframe e só depois em apps reais)
- Evidência: wwdc2025_356 (folha 0012, q0107 e q0108: dois contornos de aparelho totalmente vazios, um vertical estreito e um horizontal dividido ao meio, preparam a comparação de formato sem nenhum conteúdo dentro)
- Evidência: wwdc2026_250 (folha 0004, q0033 a q0036: grade de ícones sem marca vira um ícone com fatia de pizza e depois uma tela de entrega completa com foto, mapa e barra de ação)
- Evidência: wwdc2026_234 (folha 0001, q0004 e q0005: a mesma cena de montanha em foto realista e em seguida como malha wireframe branca sobre grade de referência)
- O que isso ensina sobre construir interface: escolher a fidelidade é escolher que pergunta está aberta. Wireframe convida a discutir posição e presença, mock colorido convida a discutir estilo, e misturar os dois num mesmo quadro embaralha a conversa.

## Antes e depois aparecem no mesmo quadro, rotulados ou divididos por linha, não em slides separados
- Evidência: wwdc2025_359 (folha 0006, q0050 e q0051: as duas telas lado a lado sobre a mesma grade de conteúdo, rotuladas por extenso como versão anterior e versão nova, com a barra de abas como única diferença; folha 0009, q0077, repete o recurso para grade contra lista)
- Evidência: wwdc2026_234 (folha 0010, q0087: um único quadro dividido verticalmente por linha fina, com os dois lados em tons ligeiramente diferentes, funcionando como cortina de comparação)
- Evidência: wwdc2025_323 (folha 0005, q0040: dois aparelhos lado a lado, um com a barra de abas cheia e outro com ela recolhida)
- O que isso ensina sobre construir interface: comparação em quadros sequenciais depende da memória de quem vê, comparação no mesmo quadro não. Quando a diferença é sutil, a cortina vertical é mais convincente que qualquer par de capturas.

## O placeholder é substituído por conteúdo real e pelo pior caso, e é isso que revela os problemas
- Evidência: wwdc2026_227 (folha 0007 q0055 traz a capa de livro em cor sólida roxa sem imagem, e folha 0008 q0067 a substitui por capas reais, nomes de pessoas, comentários com tempo relativo e campo de novo comentário; folha 0009 nomeia os casos de borda na própria lista de prévias, incluindo conteúdo longo, clube vazio e clube lotado)
- Evidência: wwdc2026_290 (folha 0003, q0019 para q0020: o valor do card é zerado mantendo o mesmo rótulo, num quadro dedicado a testar o tom do nome no pior caso)
- Evidência: wwdc2026_292 (folha 0014, q0119: o estado vazio é mostrado inteiro, com lupa central grande, o termo entre aspas incluindo um erro de digitação proposital e subtítulo instrutivo)
- O que isso ensina sobre construir interface: só o conteúdo verdadeiro expõe truncamento, ausência e ambiguidade de rótulo. Projetar o estado vazio e o extremo junto com o estado feliz é o que impede a correção tardia.

## Cada bloco fecha numa cartela de frase única, em tipografia grande sobre fundo liso
- Evidência: wwdc2026_250 (folha 0003 q0021 em verde alinhado à esquerda, folha 0010 q0085 em rosa alinhado à esquerda e folha 0014 em azul centralizado, o mesmo molde mudando de alinhamento entre ocorrências)
- Evidência: wwdc2026_251 (folha 0005 q0044, folha 0009 q0073, folha 0011 q0094 e folha 0013 q0112, repetida em q0113 já centralizada e com a grade de telas mais nítida ao redor)
- Evidência: wwdc2025_359 (folha 0002, q0017 e q0018: tela branca com uma única frase centralizada em negrito, uma por pergunta que guia a sessão)
- O que isso ensina sobre construir interface: uma tela com uma frase e nada mais funciona como respiro e como âncora de memória. O preço é disciplina de escrita, porque a frase precisa sobreviver sozinha sem apoio de exemplo.

## Cada vídeo inventa uma notação própria no começo e a recicla até o fim
- Evidência: wwdc2025_337 (folha 0007, q0058 a q0061: ponto vazado para início do traço, ponto preenchido para fim, pontos menores para guias e setinhas para o sentido, com um quadro de resumo reunindo seis exemplos em grade dois por três)
- Evidência: wwdc2026_227 (folha 0010 q0088 a q0090, folha 0011 q0092 a q0099 e folha 0012 q0103: ícones lineares pretos acumulados da esquerda para a direita, um por conceito de animação)
- Evidência: wwdc2026_321 (folha 0002, q0015 a q0018, com a notação da pilha reaproveitada até a folha 0013 e ganhando anotações de medida pelo caminho, incluindo um segundo contorno laranja para o alvo fora de tela em q0114)
- Evidência: wwdc2025_359 (folha 0010, q0083 a q0087: calendário para tempo, medidor circular para progresso e grade de quadrados para padrão, apresentados um por quadro e só depois reunidos em linha)
- O que isso ensina sobre construir interface: um vocabulário gráfico curto, apresentado antes de ser usado e nunca alterado depois, permite condensar explicação sem virar código secreto. O custo é apresentar cada símbolo isolado antes da primeira aplicação.

## Fotografia de objeto físico sobre mesa de madeira aterra o conceito abstrato e fecha o vídeo
- Evidência: wwdc2026_227 (folha 0011 q0094 e q0097 e folha 0012 q0100 aterram peso percebido, resposta a movimento e resposta tátil em iPhone físico na mão sobre mesa de madeira, nunca em captura isolada; a folha 0016 traz o slide final sobre fotografia de mesa)
- Evidência: wwdc2026_314 (folha 0008, q0064 a q0066: mesa de madeira com caixa verde de ferramentas, iPhone azul e caderno, com a lista de próximos passos crescendo a cada quadro)
- Evidência: wwdc2026_321 (folha 0015, q0127 e q0128: mesa de madeira com um origami de cisne verde e a lista de recomendações crescendo de dois para três itens)
- Evidência: wwdc2026_269 (folha 0020, q0176 e q0177: objetos físicos coloridos sobre mesa de madeira como fundo, com o texto revelado linha a linha em coluna à esquerda)
- O que isso ensina sobre construir interface: o último quadro é onde a marca fala, não o conteúdo. Uma fotografia calma com o texto em coluna lateral entrega o mesmo recado que um slide de lista, com temperatura completamente diferente.

## Um filtro de cor sobre a cena marca a abertura e o encerramento, e só eles
- Evidência: wwdc2025_404 (folha 0001, q0002 para q0003, com overlay roxo e rosa que se dissolve no começo; folha 0011, q0092 para q0093, com overlay azulado no último quadro)
- Evidência: wwdc2025_361 (folha 0017, q0145: o quadro final do apresentador leva tingimento rosa de encerramento)
- Evidência: wwdc2026_315 (folha 0007, q0060 para q0061: filtro laranja e sépia aplicado sobre a cena do apresentador no fim, com o selo de versão marcando a outra ponta do vídeo)
- O que isso ensina sobre construir interface: tratamento de cor reservado às pontas funciona como pontuação, sinalizando início e fim sem cartela nem texto. Usar o mesmo recurso no meio destruiria a função.

## Mosaico denso de dezenas de telas sem legenda abre ou fecha a peça
- Evidência: wwdc2025_359 (folha 0015, q0127 e q0128: a mesma tela do app em dezenas de identidades visuais distintas, em grade regular e sem legenda, com nenhuma miniatura se repetindo entre os dois quadros)
- Evidência: wwdc2026_251 (folha 0013, q0114: mosaico uniforme reunindo dezenas de telas dos apps citados, sem legendas)
- Evidência: wwdc2025_361 (folha 0001, q0004 a q0006, em recortes parciais de grades de ícones, e folha 0016, q0139 e q0141, com duas telas iniciais densas ocupando o quadro inteiro)
- O que isso ensina sobre construir interface: quantidade é argumento. Uma parede de exemplos prova alcance e variedade num só quadro, e funciona justamente porque nenhum item pede leitura individual.

## Marcação editorial visível sobre o texto mostra a decisão de escrita acontecendo
- Evidência: wwdc2025_404 (folha 0002, q0016 a q0018, com uma palavra tachada dentro da própria frase; folha 0003, q0022 para q0023, e folha 0006, q0051 para q0052, com azul marcando o que foi acrescentado ou reordenado contra o preto do restante; folha 0004, q0029 a q0035, com o negrito percorrendo um trecho por vez antes de cada corte)
- Evidência: wwdc2026_290 (folha 0006, q0050 para q0051: nove nomes em blocos laranja e, no quadro seguinte, seis riscados por linha diagonal, restando três; folha 0008 q0069 a q0072 e folha 0009 q0073 repetem a eliminação um a um ao lado do próprio controle onde o nome vai viver)
- O que isso ensina sobre construir interface: revisão de texto de interface fica mais convincente quando o descarte permanece visível. Ver o que saiu justifica o que ficou, e testar o candidato dentro do componente de destino evita nome que só funciona em lista.

## Achados de fonte única

- Tabela tipográfica do sistema com o tamanho em pontos declarado linha a linha, do título grande em 34 até as legendas em 12 e 11, e cada linha renderizada no próprio estilo que nomeia; o quadro seguinte aplica os mesmos estilos como anotação sobre uma capa em tela cheia (wwdc2025_359, folha 0012, q0104 e q0105).
- Carta de referência de cor reunindo quatro níveis de rótulo, cerca de doze pastilhas de cor do sistema e três níveis de fundo, com cada bloco duplicado em modo claro e modo escuro no mesmo quadro (wwdc2025_359, folha 0014, q0121).
- Alturas de botão declaradas em pontos, de 16 a 36, e a regra de forma separada por faixa de tamanho, com retângulo arredondado nos menores e cápsula nos maiores, tudo no mesmo diagrama com a caixa de código sobreposta (wwdc2025_323, folha 0012, q0103 a q0105).
- Duas regiões de amostragem de material de vidro se sobrepondo, marcadas com X vermelho, precedidas do diagrama da pílula cercada pela própria região de amostragem (wwdc2025_323, folha 0015, q0133 a q0135).
- Canvas do ícone anotado com etiqueta de dimensão sobre uma seleção vetorial com alças de redimensionamento, em cima de uma grade de círculos concêntricos e linhas de guia (wwdc2025_361, folha 0006, q0046).
- Convenção de exportação de camadas mostrada literalmente, miniaturas sobre fundo quadriculado de transparência numeradas em ordem de camada, do fundo ao glifo, cada uma exibindo a arte da sua camada (wwdc2025_361, folha 0008, q0066).
- O mesmo ícone posto contra sete fundos diferentes em sequência, trocando só o que está atrás dele, com o ícone passando de opaco a translúcido e assumindo o tom de cada fundo (wwdc2025_361, folha 0015, q0127 a q0133).
- Ponto que marca início e fim ao mesmo tempo ganha forma própria de cápsula alongada, distinta dos pontos redondos usados nos demais casos (wwdc2025_337, folha 0010, q0089 e q0090).
- A legenda cresce de três para quatro tipos de ponto e o item novo entra com marcador em losango, enquanto os demais mantêm o círculo (wwdc2025_337, folha 0012, q0107 para q0108).
- Barra de abas com o grupo dentro de uma cápsula e o botão de busca circular separado ao lado, composição repetida em três apps diferentes, um deles acrescentando um mini player em fileira acima (wwdc2025_356, folha 0009, q0074 a q0076).
- Margem junto à borda estudada isoladamente, com uma pequena cápsula sem rótulo mudando de distância do canto arredondado entre dois quadros, e o canto depois ampliado já sem ela (wwdc2025_356, folha 0005, q0042, q0043 e q0045).
- Aba de destaque tirada da barra e transformada em botão circular isolado no canto inferior direito, com as outras quatro agrupadas à esquerda (wwdc2026_269, folha 0004, q0033 e q0034).
- Itens saindo do menu de reticências para a barra de ferramentas entre dois quadros, chegando destacados em azul (wwdc2026_269, folha 0005, q0042 para q0043).
- Erro de compilador desenhado como faixa vermelha clara com ícone, ancorada na linha exata em que ocorre (wwdc2026_269, folha 0017 q0153 e folha 0018 q0157 e q0158).
- Sugestão preditiva dentro da mesma linha usa dois tons, a parte já digitada em preto mais escuro e a parte prevista pelo sistema em cinza mais claro (wwdc2026_292, folha 0011, q0095 e q0096).
- Token colorido distinto de texto livre dentro do campo de busca, com dois coexistindo no mesmo campo, e um avatar genérico rotulado antecedendo a aplicação para mostrar o componente base (wwdc2026_292, folha 0013, q0109 a q0114).
- Termo buscado realçado em fundo amarelo dentro da prévia dos resultados, recurso recorrente que a fala nunca descreve (wwdc2026_292, folha 0005 q0037 e folha 0012 q0103).
- Estado de exceção sinalizado só por peso tipográfico, com o rótulo passando a negrito no inspetor quando o valor foi ajustado naquele componente, enquanto os vizinhos seguem em peso normal (wwdc2026_252, folha 0008, q0065 a q0067).
- Encapsulamento mostrado como substituição visível, vários nós soltos de leitura e lógica dando lugar a um único nó com nome customizado e ícone de agrupamento (wwdc2026_252, folha 0011, q0096 a q0099).
- Painel de ajuste mostrado primeiro no estado ruim, como camada escura que ocupa metade inferior e obstrui a interface em janela estreita, e depois reorganizado lado a lado com a prévia, com rótulo apontando o botão de redimensionar que resolve (wwdc2026_227, folhas 0014 e 0015, q0124 a q0129).
- Proximidade comunicada por área de cor, com o radar de pontos dispersos virando um círculo verde sólido que preenche quase a tela inteira (wwdc2026_227, folha 0012, q0100 para q0101).
- Texto de interface em tamanho maior demonstrado no mesmo card de produto, com layout vertical preservado e nada truncado, precedido da tela de ajuste com o interruptor ativo e o slider na base (wwdc2026_251, folha 0010, q0084 a q0087).
- Cor concentrada só onde comunica, com a barra de topo colorida anotada em três pontos e depois neutra com a anotação de que a cor rola para fora da tela (wwdc2026_251, folha 0008, q0070 para q0072).
- Guia estrutural puro antes de qualquer conteúdo, com as colunas desenhadas como barras verticais laranja finas sobre fundo cinza claro que mudam de posição e espaçamento entre quadros (wwdc2026_314, folha 0003, q0019 para q0020).
- Ordem de preenchimento de uma grade provada com caixas numeradas de 1 a 15 em quatro colunas de alturas desiguais, dentro de uma janela de navegador (wwdc2026_314, folha 0003, q0022).
- Menu suspenso deixando de ser lista vertical e virando grade de cartões com linhas, colunas e espaçamento explícitos, mostrado ao lado do código que produz a mudança (wwdc2026_315, folha 0005, q0040 para q0041).
- Conteúdo rico dentro de uma opção de lista renderizado como cartão quadrado com ícone acima e rótulo abaixo (wwdc2026_315, folha 0004, q0035 para q0036).
- Custo de renderização explicado como linha do tempo horizontal com marcadores regulares de prazo de quadro, e um bloco antes cinza escuro virando vermelho ao ultrapassar o prazo (wwdc2026_321, folha 0010, q0087 a q0090).
- Espectro de literalidade de uma metáfora desenhado como controle deslizante entre dois extremos nomeados, reaparecendo com o indicador em posição diferente ao lado de dois ícones alternativos para a mesma função (wwdc2026_250, folha 0007, q0057 para q0058).
- Única captura de produto real em todo um vídeo, uma página de documentação com filtro lateral, grade de quatro cartões de princípio e índice à direita, intercalada por um só quadro (wwdc2026_250, folha 0015, q0132).
- Silhueta humana cinza usada como instrumento de referência de escala dentro da cena tridimensional, mudando de posição entre quadros enquanto a cena ganha anotações (wwdc2026_234, folha 0003 q0026 e folha 0005 q0039 e q0040).
- Elementos a remover marcados diretamente sobre o panorama com formas geométricas simples, uma oval translúcida grande e círculos de contorno branco, criando um vocabulário de circular para apontar problema (wwdc2026_234, folhas 0009 e 0010, q0080, q0081, q0084 e q0085).
- Pipeline de um asset decomposto em quatro estágios empilhados verticalmente, de dados de movimento em linhas coloridas para malha, depois textura em gradiente e por fim o elemento renderizado com fibras finas (wwdc2026_234, folha 0014, q0125).
- Balão de prompt com fundo translúcido e borda em gradiente de três cores como elemento gráfico mais recorrente de um vídeo inteiro, sempre exibindo o texto do pedido por completo (wwdc2026_227, folhas 0004, 0005, 0006, 0008 e 0014).
- Gravação de processo ao vivo denunciada por um cronômetro sobreposto de tempo decorrido nas capturas do ambiente de desenvolvimento (wwdc2026_227, folha 0002, q0014 a q0016).
