# Essência visual, lote ess-02 (HIG, de game-controls a playing-video)

## A abertura de cada seção é sempre o mesmo chassi: cartão de cantos arredondados, degradê temático, símbolo em uma única cor sólida e grade de construção pontilhada deixada à vista
- Evidência: generative-ai (img 0527, lápis azul escuro com três estrelas sobre grade retangular e circular)
- Evidência: gyro-and-accelerometer (img 0537, anéis vazados com grade fina de horizontais, verticais e um par de diagonais mais círculos concêntricos)
- Evidência: icloud (img 0560, nuvem vazada com círculo tracejado tangente à base ditando a curvatura do lobo)
- Evidência: onboarding (img 0824, mão acenando em traço vermelho escuro com círculo guia centralizado na palma)
- Evidência: playing-audio (img 0850, alto falante em traço grosso com círculo guia centralizado no corpo)
- O que isso ensina sobre construir interface: identidade de sistema vem de repetir o contêiner, o peso de traço e o método de construção, variando um parâmetro por vez. Deixar a grade visível transforma a capa em assinatura do processo e não só em decoração.

## A cor do degradê muda por seção e funciona como código de assunto, com o desenho sempre numa tinta só
- Evidência: healthkit, homekit, icloud, nfc e photo-editing usam degradê azul (img 0538, 0544, 0560, 0807, 0840)
- Evidência: launching, managing-accounts, managing-notifications, loading e playing-audio usam degradê laranja (img 0679, 0751, 0752, 0732, 0850)
- Evidência: images, immersive-experiences, inclusion, motion e materials usam degradê amarelo (img 0630, 0638, 0667, 0800, 0770)
- Evidência: keyboards usa roxo e a própria síntese compara o mesmo esquema de construção em azul e amarelo (img 0671 contra img 0644 e img 0667)
- O que isso ensina sobre construir interface: uma paleta atribuída por área dá orientação sem exigir rótulo, desde que a forma e a estrutura fiquem constantes e só a matiz mude.

## No modo escuro a luminosidade se inverte, mas matiz, geometria e posição das marcações não saem do lugar
- Evidência: icons (img 0561, traço vira creme sobre dourado escurecido e a grade continua visível, mais discreta)
- Evidência: icons (img 0562 e 0563, a faixa fica vinho e os glifos creme, com as guias exatamente nas mesmas posições; img 0564 a 0566, discos e glifo invertem de cor e as medidas não se movem; img 0623, a margem vira vinho com a marca no mesmo lugar)
- Evidência: materials (img 0770, o fundo passa a dourado oliva e os contornos clareiam sem abandonar a matiz amarela)
- Evidência: icons (img 0567, o azul do item selecionado é idêntico nos dois modos e só as reticências trocam de preto para branco)
- O que isso ensina sobre construir interface: o modo escuro é uma troca de luminosidade, não um redesenho. A cor de destaque e as cotas devem ser as mesmas nos dois temas.

## Boa parte das capas abandona o esboço e vira diagrama de especificação, com cotas e atributos nomeados em cima do componente
- Evidência: labels (img 0676, a palavra dentro de caixa pontilhada com a anotação "System Font, Body (Emphasized)" e "Primary Text Color")
- Evidência: notifications (img 0810, guias de régua em H para largura e em I para altura sobre ícone, título, descrição e carimbo de tempo)
- Evidência: lockups (img 0733, retângulos tracejados demarcando ícone, headline e footnote, com seta medindo a largura do círculo e a altura do bloco)
- Evidência: outline-views (img 0826, guia tracejada e colchetes marcando a indentação em dois níveis e a altura de linha)
- Evidência: gauges (img 0523, anatomia dos formatos circular e linear com setas cotando altura, largura e margens)
- O que isso ensina sobre construir interface: a primeira imagem de um componente pode ensinar a anatomia dele. Nomear na arte a fonte, o papel do texto e a cor de sistema evita que a especificação viva só na documentação escrita.

## A notação de cota é sempre a mesma: seta dupla horizontal acima para largura, seta dupla vertical à direita para altura
- Evidência: image-views (img 0628, largura acima e altura à direita do glifo dentro do quadro)
- Evidência: ornaments (img 0825, seta horizontal acima da pílula e vertical à direita)
- Evidência: panels (img 0835, horizontal abaixo para largura e vertical à direita para altura)
- Evidência: lockups (img 0733) e gauges (img 0523) repetem a mesma dupla de setas
- O que isso ensina sobre construir interface: convenção de anotação é parte do design system. Quem lê a segunda prancha já sabe ler a terceira sem legenda.

## Vermelho é a cor de anotação e rosa é a cor de zona vazia (margem, padding, espaçamento reservado)
- Evidência: layout (img 0686, faixa rosa da área segura do tvOS com as medidas escritas em vermelho; img 0687, faixas rosa preenchendo o padding entre cartões focáveis)
- Evidência: icons (img 0623, quadrado externo rosa marcando a margem com o colchete de medida; img 0564, barras rosa marcando o centro geométrico)
- Evidência: lockups (img 0734, faixas verticais rosa como folga reservada entre colunas)
- Evidência: playing-video (img 0855 e 0859, o padding embutido sempre aparece como faixa rosa colada nas bordas do vídeo)
- Evidência: live-activities (img 0711 e 0722, borda vermelha fina como guia de margem e linha tracejada vermelha marcando faixa vazia)
- O que isso ensina sobre construir interface: separe a cor que mede da cor que preenche. Espaço negativo fica visível quando ganha cor própria, e é assim que se discute espaçamento sem citar número.

## Quase nada é cotado com valor numérico: as guias marcam relação e proporção, não medida absoluta
- Evidência: icons (img 0623, a margem de 10% é descrita como a única medida numérica de uma página com 29 folhas)
- Evidência: layout (img 0686, 60 no topo e na base e 80 nas laterais são os únicos números da página)
- Evidência: image-views (img 0628), lockups (img 0733), ornaments (img 0825), panels (img 0835), page-controls (img 0827) e outline-views (img 0826) trazem setas de medida sem nenhum valor escrito
- O que isso ensina sobre construir interface: o sistema é proporcional antes de ser métrico. Fixar número cedo demais engessa o layout; marcar a relação deixa o mesmo desenho escalar entre tamanhos e plataformas.

## Certo e errado são marcados por selos mínimos e sem texto: check branco em círculo verde, X branco em círculo cinza
- Evidência: homekit (img 0545 e 0546)
- Evidência: menus (img 0791 a 0794, o X no menu com ícones arbitrários e o check no menu só com texto)
- Evidência: offering-help (img 0817 a 0820, grade 2x2 com o marcador ao lado de cada variante)
- Evidência: materials (img 0774 a 0777, X no símbolo cinza sobre material e check no símbolo vibrante, nos dois modos)
- Evidência: page-controls (img 0828 a 0831) e playing-video (img 0854 e 0856)
- O que isso ensina sobre construir interface: o veredito deve ser discreto e sempre no mesmo lugar, para que a atenção fique no exemplo e não no julgamento. Verde preenchido aprova, cinza reprova, e o vermelho fica reservado para anotação.

## O par certo e errado muda uma variável só e congela todo o resto do quadro
- Evidência: menus (img 0791 a 0794, mesmo menu de dias da semana, muda só a presença de ícones)
- Evidência: materials (img 0774 a 0777, mesmo botão e mesmo fundo, muda só a cor do símbolo)
- Evidência: page-controls (img 0828 e 0830, mesma barra do app de Tempo com os mesmos botões circulares, muda só o conteúdo da pílula)
- Evidência: live-activities (img 0720 e 0721, mesmo compact, muda só a distância entre a pílula da câmera e o bloco de texto)
- Evidência: lists-and-tables (img 0698 e 0699, mesma linha, muda só o elemento da borda final)
- O que isso ensina sobre construir interface: comparação só ensina quando é controlada. Se dois exemplos diferem em três coisas, ninguém aprende qual delas causou o problema.

## Séries de variação seguem a mesma disciplina: uma dimensão de cada vez, contêiner fixo
- Evidência: layout (img 0682 a 0685, as size classes crescem em largura e altura de forma independente, sobre o mesmo fundo)
- Evidência: imessage-apps-and-stickers (img 0635 a 0637, a barra do iMessage e o painel de categorias ficam idênticos e a grade cai de quatro para três e para duas colunas conforme a figurinha cresce)
- Evidência: materials (img 0778 a 0781, mesmo ícone e mesmo fundo em progressão de opacidade de ultraThin até thick)
- Evidência: gauges (img 0524 comparada com img 0525 e com img 0526, contínuo contra discreto e cor única contra faixas de cor)
- Evidência: immersive-experiences (img 0639 a 0643, o painel de vidro fica na mesma posição e proporção e só muda quanto do ambiente real é substituído)
- O que isso ensina sobre construir interface: variação é eixo, não coleção. Definir qual parâmetro varia e travar o resto é o que transforma opções em sistema.

## Estado ativo se marca por preenchimento sólido contra contorno ou neutro, sem trocar o desenho
- Evidência: icons (img 0567, botão ativo com círculo inteiro preenchido de azul contra reticências neutras; img 0604 a 0607, a camada em foco se distingue só por preenchimento sólido, mantendo a forma)
- Evidência: menus (img 0790, item do submenu ativo com preenchimento vermelho sólido)
- Evidência: outline-views (img 0826, linha selecionada em vermelho sólido com texto branco, invertendo o contraste)
- Evidência: in-app-purchase (img 0651, plano anual com círculo vermelho preenchido e mensal com círculo vazio)
- Evidência: page-controls (img 0832 a 0834, o ponto da página atual é o único preenchido, preto sobre claro no iOS e branco sobre escuro no watchOS)
- O que isso ensina sobre construir interface: mude peso e preenchimento, nunca a silhueta. Trocar o ícone entre estados obriga o olho a reidentificar o elemento a cada mudança.

## Destaque momentâneo e escolha persistente usam marcas diferentes de propósito
- Evidência: menus (img 0790 com preenchimento sólido para hover ou seleção momentânea contra img 0796, em que um estado alternável é marcado só por checkmark discreto na margem esquerda)
- Evidência: pickers (img 0845 e 0846, contorno verde marcando o foco na roda, contra img 0849, em que o item escolhido leva check verde à direita)
- Evidência: in-app-purchase (img 0648, motivo escolhido marcado com check azul numa lista só com divisórias)
- O que isso ensina sobre construir interface: foco e seleção são coisas distintas e precisam de duas linguagens visuais. Usar a mesma marca para as duas faz o usuário achar que já escolheu quando só está navegando.

## Foco no tvOS é elevação: o item cresce, clareia para branco, ganha sombra e sobe de camada, e o layout reserva a folga
- Evidência: lockups (img 0734 a 0738, o item focado fica branco entre vizinhos cinza, com sombra e tamanho maior; o poster focado sobe de camada)
- Evidência: layout (img 0687, cartão central maior e com sombra, com faixas rosa preenchendo o padding entre ele e os vizinhos)
- Evidência: materials (img 0782, a aba ativa vira pílula branca opaca sobre o material translúcido)
- O que isso ensina sobre construir interface: se o foco aumenta o elemento, o espaçamento precisa ser dimensionado para o estado maior, não para o estado de repouso.

## Material translúcido não tem cor própria: ele assume o tom do que está atrás e o conteúdo é que precisa garantir contraste
- Evidência: materials (img 0771 e 0772, o mesmo círculo fica cinza escuro sobre céu estrelado e esbranquiçado sobre foto de praia; img 0773, a variante clear borra menos e deixa o padrão de tijolos reconhecível)
- Evidência: materials (vídeo 015, folhas 0002 e 0003, a sala escurece e a janela escurece junto, ficando mais acinzentada e opaca sem que o texto perca contraste)
- Evidência: keyboards (vídeo 014, barra estreita marrom escura e translúcida flutuando sobre a mesa de madeira, com texto branco)
- Evidência: multitasking (vídeo 016, duas janelas translúcidas do visionOS convivendo sobre cenário real que muda por trás)
- O que isso ensina sobre construir interface: material é camada de contexto, não de legibilidade. O contraste tem que vir da cor e do peso do conteúdo, porque o fundo vai mudar sem aviso.

## Legibilidade difícil se resolve tirando conteúdo e aumentando peso, não acrescentando caixa
- Evidência: live-activities (img 0707 contra img 0709, duas linhas pequenas com rótulo e código são substituídas por um único código maior e mais pesado, com os selos de erro e acerto em img 0708 e 0710)
- Evidência: materials (img 0774 a 0777, o símbolo em systemGray3 some no material e o mesmo símbolo em cor vibrante se resolve sem mudar o botão)
- Evidência: live-photos (img 0729 e 0730, crachá branco semitransparente sobre foto noturna escura, com a variante sem texto reduzida a um círculo pequeno)
- O que isso ensina sobre construir interface: quando o espaço é mínimo, corte informação antes de encolher tipografia, e resolva contraste na cor do símbolo antes de inventar um fundo novo.

## Transição entre estados é sempre gradual e local, nunca corte seco
- Evidência: gestures (vídeo 010, folha 0001, q001 a q005, o fundo do botão de coração clareia progressivamente de cinza translúcido até branco sólido sem que nada mude de posição ou tamanho)
- Evidência: immersive-experiences (vídeo 013, folha 0002, q014 a q018, a cena interna entra em transparência sobre a paisagem e cresce quadro a quadro, com linha diagonal de transição visível)
- Evidência: multitasking (vídeo 016, folha 0002, q012, q016 e q018, uma faixa vertical clara aparece só na borda entre as duas janelas, efeito localizado e sutil)
- Evidência: game-controls (img 0517 e 0518, o mesmo thumbstick passa de branco opaco com seta de direção para cinza escuro translúcido em repouso)
- O que isso ensina sobre construir interface: anime a propriedade que carrega significado (opacidade, tom, borda) e deixe posição e tamanho parados. Mudança localizada comunica sem reorganizar a tela.

## Entrada direta e entrada indireta pedem tipos diferentes de resposta
- Evidência: gestures (vídeo 010, no gesto indireto o botão realça antes do contato e depois vira branco sólido, contra vídeo 011, em que o toque direto não tem realce nem halo e a resposta é física, com blocos girando e caindo)
- Evidência: game-controls (img 0519, o mesmo botão distingue toque simples com anel completo de toque prolongado com anel parcial, como indicador de progresso)
- O que isso ensina sobre construir interface: quando o dedo toca o objeto, a física já é o feedback; quando a mira é remota, a interface precisa mostrar antes o que vai ser atingido.

## Hierarquia de ação por forma: preenchido, depois contornado, depois texto puro sem fundo
- Evidência: machine-learning (img 0748, botão preenchido em roxo, botão contornado e uma terceira ação só em texto, na mesma coluna)
- Evidência: healthkit (img 0542, botão pílula branco preenchido para sincronizar e a opção de pular logo abaixo como texto simples sem fundo)
- Evidência: in-app-purchase (img 0654, planos como botões verdes em pílula e o resgate de código como link de texto; img 0657, gerenciar, restaurar e resgatar como links azuis empilhados fora do bloco; img 0660, cancelamento como link vermelho centralizado)
- O que isso ensina sobre construir interface: a ação secundária perde o fundo antes de perder a cor, e a terciária perde o fundo e a posição de destaque. Isso mantém uma só ação óbvia por tela.

## A linha de lista é um gabarito fixo e o slot da borda final declara a intenção
- Evidência: lists-and-tables (img 0698 com ícone circular de "i" em azul para revelar informação, contra img 0699, mesma estrutura com chevron e valor secundário cinza para navegar)
- Evidência: healthkit (img 0540, cada linha de categoria com ícone colorido, nome e toggle verde à direita)
- Evidência: homekit (img 0558, linha com ícone à esquerda, título, texto secundário simulado e chevron à direita)
- Evidência: home-screen-quick-actions (img 0543, quatro linhas com símbolo geométrico na borda inicial e rótulo à direita)
- O que isso ensina sobre construir interface: mantenha o esqueleto da linha e troque só o elemento final. O usuário aprende a prever o resultado do toque pelo símbolo da direita.

## Lista agrupada é cartão dentro de cartão, com divisores finos e cabeçalho ou rodapé fora do cartão
- Evidência: lists-and-tables (img 0697, cabeçalho acima e rodapé abaixo do cartão, três linhas dentro; img 0698 e 0699, cartão cinza claro contendo cartão branco interno)
- Evidência: healthkit (img 0540, escrita e leitura em seções separadas com rótulo cinza em caixa alta fora do bloco)
- Evidência: in-app-purchase (img 0646, cinco opções numa cápsula única com divisórias finas e chevrons; img 0666, cartão único com título cinza em caixa alta e check verde na opção escolhida)
- O que isso ensina sobre construir interface: o cartão delimita o grupo e o rótulo explica o grupo de fora, o que permite empilhar seções sem criar moldura dentro de moldura.

## Placeholder deliberado: formas cegas, wireframe cinza, ícone tracejado e texto borrado quando a lição é de layout
- Evidência: live-activities (img 0701 a 0703, formas pretas nomeadas por linhas de chamada em vez de conteúdo real; img 0718 e 0719, conteúdo borrado de propósito dentro de caixa tracejada vermelha)
- Evidência: in-app-purchase (img 0658, tela de resgate como wireframe em moldura de iPhone, com área de ícone tracejada e campo vazio, sem cor de marca)
- Evidência: homekit (img 0552, três círculos cinza iguais com o HomeKit ao lado de dois quadrados tracejados genéricos; img 0559, grade de apps com três ícones tracejados)
- Evidência: machine-learning (img 0743, menu de contexto padrão sobre um iPhone cinza sem cor de app, com quatro linhas genéricas acima do divisor)
- O que isso ensina sobre construir interface: apagar o conteúdo é o jeito de provar que a estrutura funciona sozinha. Conteúdo bonito esconde problema de layout.

## Desfoque e esmaecimento dirigem o olhar dentro da própria imagem, reduzindo o entorno em vez de inflar o alvo
- Evidência: home-screen-quick-actions (img 0543, os ícones vizinhos ficam desfocados e só o ícone de origem continua nítido)
- Evidência: in-app-purchase (img 0653, a mesma tela de onboarding reaparece com o botão realçado por contorno e o resto apagado; img 0656, o link de resgate ganha cápsula preta sólida enquanto os botões verdes são esmaecidos)
- Evidência: in-app-purchase (img 0652, o artigo continua atrás com opacidade reduzida sob a mensagem de limite)
- Evidência: offering-help (img 0814, o texto de corpo por trás do popover aparece esmaecido sem ser deslocado)
- O que isso ensina sobre construir interface: sobreposição que apaga o fundo mantém contexto e ainda assim cria foco. Empurrar o conteúdo é a alternativa quando o contexto precisa continuar legível.

## Todo componente efêmero nasce ancorado no elemento que o originou, e a origem continua marcada
- Evidência: home-screen-quick-actions (img 0543, o cartão do menu fica logo acima do ícone de app de origem)
- Evidência: menus (img 0798, o menu do visionOS nasce abaixo do botão de mais opções, que aparece selecionado em branco sólido)
- Evidência: maps (img 0759, o compact place card fica ancorado logo acima do pino; img 0760, o caption reduz tudo ao rótulo sob o mesmo pino)
- Evidência: offering-help (img 0814 e 0815, seta triangular do tip apontando para a estrela azul relacionada)
- Evidência: pickers (img 0842, o toque na linha de data abre o calendário em popover logo abaixo da própria linha)
- O que isso ensina sobre construir interface: a âncora explica de onde o painel veio e para onde ele volta. Sem ela, o elemento parece ter surgido do nada e o usuário perde a referência de contexto.

## O mesmo conteúdo é reconstruído por plataforma, e o watchOS sempre vira coluna única com o mínimo
- Evidência: live-activities (img 0725 a 0727, a cadeia vai do compact do iPhone ao cartão do Smart Stack e ao layout customizado com anel de progresso)
- Evidência: maps (img 0761, full callout como folha centralizada no iPad, contra img 0762, folha que sobe da borda inferior no iPhone com fileiras de ação e métricas, contra img 0769, snapshot no Apple Watch com só dois botões circulares, sem busca nem lista)
- Evidência: in-app-purchase (img 0655, cadastro no Watch como coluna única de título, descrição, um botão de largura total e termos; img 0665 e 0666, duas soluções diferentes para exibir preço no mesmo espaço)
- Evidência: multitasking (img 0802, app switcher em cascata no iPhone, contra img 0804, grade de duas linhas no iPad)
- Evidência: menus (img 0797, as mesmas seis ações em três layouts de menu, de ícones em fileira compacta até lista vertical completa)
- O que isso ensina sobre construir interface: adaptar não é encolher. Cada plataforma redistribui as mesmas informações em outra forma, e o que não couber sai em vez de ser espremido.

## Corte na borda é a pista padrão de que existe mais conteúdo
- Evidência: notifications (img 0812, o segundo botão de ação do long look aparece cortado pela borda inferior da tela)
- Evidência: layout (img 0688 a 0694, cada grade do tvOS termina com uma coluna extra cortada na borda direita e a primeira também corta uma linha na base)
- Evidência: imessage-apps-and-stickers (img 0635 e 0637, a grade de figurinhas sempre mostra uma fileira parcial na borda inferior)
- Evidência: machine-learning (img 0749, o terceiro cartão da fileira fica cortado na borda direita do quadro)
- O que isso ensina sobre construir interface: mostrar a fatia seguinte comunica rolagem melhor do que seta ou legenda, e ainda calibra quanto conteúdo existe.

## Glifo de sistema é a mesma forma em preto sobre branco e em branco sobre preto, isolado, sem cartão nem grade
- Evidência: icons (img 0570 a 0610, ações padrão apresentadas como glifo único centralizado, com forma idêntica nos dois contrastes)
- Evidência: inclusion (img 0668 a 0670, silhuetas sólidas de pessoa, grupo e figura acenando, sem rosto, cabelo ou roupa)
- Evidência: keyboards (img 0672 a 0675, os quatro modificadores em contorno preto fino, sem preenchimento e sem cor)
- Evidência: homekit (img 0549 a 0551, a mesma casa em contorno preto sobre branco, branco sobre preto e azul customizado)
- O que isso ensina sobre construir interface: o ícone precisa funcionar como silhueta antes de funcionar como arte, porque ele vai ser recolorido pelo contexto.

## Significados opostos vêm da inversão do mesmo desenho, nunca de dois desenhos diferentes
- Evidência: icons (img 0576 e 0577, desfazer e refazer são a mesma seta curva espelhada; img 0602 e 0603, curtir e não curtir usam a mesma mão em contorno com o polegar invertido)
- Evidência: icons (img 0592 a 0595, os quatro alinhamentos são sempre quatro linhas empilhadas e só a borda de referência muda)
- Evidência: outline-views (img 0826, a mesma seta de disclosure aponta para baixo quando expandido e para a direita quando recolhido)
- Evidência: icons (img 0578 e 0580, o mesmo lápis muda de sentido pela composição, sozinho para renomear e sobreposto a um quadrado para compor)
- O que isso ensina sobre construir interface: pares de ação devem compartilhar a forma base. A relação entre os dois fica óbvia e o vocabulário do conjunto não cresce.

## Ondas concêntricas crescentes de um lado só é o motivo reservado para comunicação a distância
- Evidência: nfc (img 0807, três arcos concêntricos crescentes, o mesmo motivo de nearby-interactions sem o círculo central)
- Evidência: nearby-interactions (img 0806, duas curvas concêntricas chegando de um lado só do círculo, com a direção comunicada pela assimetria)
- Evidência: id-verifier (img 0625, ondas curvas crescentes saindo da quina do cartão de identidade)
- Evidência: playing-audio (img 0850, três ondas curvas de tamanho crescente saindo do alto falante)
- O que isso ensina sobre construir interface: uma família semântica pode compartilhar um motivo e se diferenciar pelo que o acompanha. A assimetria é o que carrega a informação de direção.

## Ao reduzir de tamanho, a arte perde elementos em vez de encolher tudo junto
- Evidência: icons (img 0618, 0620, 0621 e 0622, a grade perde linhas, o traço do eletrocardiograma engrossa, o texto fica ilegível e no tamanho mínimo resta só o coração)
- Evidência: mac-catalyst (img 0740 e 0741, o mesmo ícone pixelizado ganha margem e blocos de pixel menores no idioma Mac, com impressão de mais nitidez)
- Evidência: images (img 0631 a 0633, a mesma forma sobre grades de 10, 20 e 30 pixels por lado, com borda serrilhada e pixels cinza intermediários na menor)
- O que isso ensina sobre construir interface: defina o que sobrevive em cada tamanho antes de desenhar o maior. Detalhe que vira ruído no tamanho pequeno deve sumir, não afinar.

## O traço ensina a regra e a captura real ensina o comportamento, e as duas linguagens não se misturam na mesma imagem
- Evidência: gestures (img 0530 a 0535, o traço simples delimita a zona reservada aos overlays do sistema e as fotografias mostram o mesmo botão em Shared Space, Full Space e com a mão coberta por luva)
- Evidência: layout (img 0681 é a única composição de app completo da página e todo o resto são diagramas abstratos)
- Evidência: materials (img 0782, captura do app Destination Video no tvOS; img 0783 e 0784, a mesma sala do visionOS com janela sólida e janela translúcida)
- Evidência: panels (img 0835 traz o panel como diagrama com setas de cota e img 0836 mostra o inspector real do macOS com pares de rótulo e valor)
- O que isso ensina sobre construir interface: separe a prancha que define a regra da tela que prova o resultado. Misturar as duas faz a especificação parecer opinião sobre um app específico.

## As ferramentas de design entram na documentação como parte da lição
- Evidência: game-controls (img 0522, o app SF Symbols no Mac com a categoria Gaming selecionada, 234 símbolos e nome técnico sob cada ícone)
- Evidência: icons (img 0568 e 0569, o painel do SF Symbols com o símbolo grande, nome técnico e lista de localização com uma linha por idioma e miniatura do caractere)
- O que isso ensina sobre construir interface: mostrar a ferramenta junto da regra encurta o caminho entre ler e fazer, e ainda revela o vocabulário técnico que o time vai usar.

## As anotações técnicas existem só na imagem: o texto alternativo oficial quase nunca menciona as medidas
- Evidência: image-views (img 0628, a legenda fala em foto estilizada e não cita as setas de largura e altura)
- Evidência: labels (img 0676, a legenda fala em rótulo tingido de vermelho enquanto a imagem é um diagrama de medidas e tipografia)
- Evidência: notifications (img 0810, a descrição fala em representação estilizada e a imagem traz guias em H e em I sobre o layout)
- Evidência: outline-views (img 0826, a descrição cita só a lista em quatro colunas e as anotações de indentação por nível e de altura de linha aparecem apenas na imagem)
- Evidência: home-screen-quick-actions (img 0543, o cartão arredondado, a estrutura de linha e o desfoque dos vizinhos aparecem só na imagem)
- O que isso ensina sobre construir interface: quem só lê a documentação escrita perde a metade quantitativa da especificação. A prancha é a fonte, o texto é resumo.

## Achados de fonte única

- Área segura do tvOS anotada com os únicos números da página: 60 no topo e na base, 80 nas laterais, com a faixa em rosa e os valores em vermelho. Referência: layout (img 0686).
- Margem do ícone de documento do macOS cotada como 10% da largura, com colchete no topo e quadrado externo rosa. Referência: icons (img 0623).
- Entre as grades do tvOS de duas a nove colunas, a de nove é a única sem coluna cortada: as nove colunas cabem inteiras em três linhas completas. Referência: layout (img 0695).
- Divisão da tela em jogos feita sobre uma imagem única cortada ao meio por molduras coloridas, vermelha à esquerda para movimento e ciano à direita para câmera. Referência: game-controls (img 0520).
- Código de três cores do playing-video nomeado só na segunda folha, depois de já ter sido usado sem explicação: azul claro para a área segura do AVKit, roxo para o vídeo e rosa para o padding embutido. Referência: playing-video (img 0857 em relação a img 0853 e 0855).
- Haptics descritos por notação de linha do tempo, com barras verticais cuja altura acompanha a força e um marcador vertical que percorre o padrão, e a quantidade de pulsos isolados no início funcionando como código de identidade (dois em Notification, três em Success, um em Start). Referência: playing-haptics (vídeos 017 a 025 e 026 a 034, quadros q001 e q002).
- Centralização óptica ensinada em três etapas sobre o mesmo glifo: barras rosa marcando o centro geométrico, o glifo subindo alguns pixels com o padding já incorporando o deslocamento, e por fim os dois discos lado a lado sem marcação alguma. Referência: icons (img 0564 a 0566).
- Composição de ícone desmontada camada por camada antes do resultado: fundo, símbolo, rótulo e só então o composto. Referência: icons (img 0615 a 0618).
- Ícones de formatação que usam a própria letra como corpo e aplicam nela a variação que a ação representa, com o B em peso muito mais grosso e o U com traço da mesma espessura abaixo. Referência: icons (img 0587 a 0591).
- Uso errado de ícone de tecnologia demonstrado com acabamento pesado de propósito: degradê cromado com brilho especular no botão circular e botão retangular metálico escuro só com a palavra da marca. Referência: homekit (img 0553 e 0554).
- Posição do ícone em texto corrido testada no mesmo cartão pílula mantido constante: no início da linha, no meio da frase e no fim substituindo a palavra escrita. Referência: homekit (img 0555 a 0557).
- Gradação de tamanho dos pontos do page control: os cinco centrais em tamanho padrão, o segundo e o penúltimo menores e o primeiro e o último menores ainda. Referência: page-controls (img 0832).
- Confiança do sistema comunicada em linguagem natural e não em número ou porcentagem, com a recomendação em texto curto acima da hierarquia de botões. Referência: machine-learning (img 0748).
- Limitação do sistema sinalizada por pílula pequena "Low light" sobre o próprio quadro de captura, sem alerta modal interrompendo a tarefa. Referência: machine-learning (img 0750).
- Feedback explícito colocado dentro do menu de contexto padrão, junto das demais ações, em vez de num controle dedicado. Referência: machine-learning (img 0743).
- Overlay de digitação do visionOS fixo em relação ao teclado físico, acima e um pouco à esquerda, enquanto as mãos mudam de pose sem sair do lugar. Referência: keyboards (vídeo 014, folha 0001 q001 a folha 0002 q010).
- Clustering do mapa resolvido com troca de forma: um pino circular laranja com número vira pinos em gota com ícone e rótulo ao aproximar. Referência: maps (img 0756 e 0757).
- Mapa de interior de app próprio adotando a identidade visual do app (fundo verde, marcadores e barra de abas verdes) sem abandonar a lógica de pinos numerados e marcadores redondos do mapa padrão. Referência: maps (img 0768).
- StandBy em Night Mode reimprime o mesmo layout inteiro em tons de vermelho sobre preto, sem nenhum azul. Referência: live-activities (img 0724 em relação a img 0706).
- Modalidade representada sem escurecer o fundo: duas janelas do mesmo vermelho translúcido, com a hierarquia vindo só da sobreposição e da barra de título exclusiva da janela da frente. Referência: modality (img 0799).
- Anel de atividade usado como unidade de calendário: cada dia do mês é um conjunto de três anéis concêntricos, com anéis incompletos e dias sem dado em cinza apagado. Referência: healthkit (img 0541).
- Indicador de atividade desenhado como oito traços em cápsula a 45 graus, com opacidade decrescente para sugerir rotação numa imagem parada. Referência: loading (img 0732).
- Image well desenhado com folga generosa entre o glifo e a borda do contêiner, ao contrário da image view, em que o glifo ocupa quase todo o espaço e recebe cotas. Referência: image-wells (img 0629 comparada com image-views img 0628).
- Ícone de app do tvOS com paralaxe montada por camadas de velocidade diferente: o cartão e o anel quase parados, o rosto em primeiro plano varrendo da esquerda para a direita, mais um brilho diagonal que só aparece nas posições centrais. Referência: images (vídeo 012, folhas 0001 a 0004, q001 a q037).
- Tooltip do macOS construído de forma oposta ao tip do iPhone: caixa retangular cinza clara, sem seta, sem título em negrito, uma única linha de texto logo abaixo do ponteiro. Referência: offering-help (img 0823).
