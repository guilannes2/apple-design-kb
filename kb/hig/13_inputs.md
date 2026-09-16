# Inputs

## Action button (slug: action-button)

### O que governa
Rege o comportamento do Action button do iPhone e do Apple Watch: como um app oferece uma ação rápida a esse botão físico configurável, e como reage a pressões simples ou combinadas.

### Por que
A ideia central é dar acesso instantâneo a uma função que a pessoa já usa com frequência, no mesmo espírito de falar com a Siri ou tocar no Spotlight. A Apple evita que o app "reensine" o que o sistema já ensina: como o sistema mostra sozinho como configurar o botão, o app não deve repetir essa orientação nem competir com ela.

### Faça e evite
- Ofereça um conjunto das funções essenciais do app para o Action button.
- Não crie um App Shortcut só para abrir o app: ícone, widgets e complicações do Apple Watch já cobrem isso.
- Escreva um rótulo curto para cada ação, com capitalização de título, começando com verbo, no presente, sem artigos nem preposições.
- Mantenha o rótulo no máximo com três palavras (exemplo dado: "Start Race" em vez de "Started Race" ou "Start the Race").
- Deixe o sistema explicar como usar o Action button com o app; não repita essa orientação por conta própria.
- No iOS, mantenha a pessoa no contexto atual: use Live Activities e snippets em vez de abrir o app inteiro.
- No watchOS, prefira que a segunda pressão continue ou avance a ação, em vez de interrompê-la.
- Pense bem antes de oferecer mais de uma função secundária no watchOS, porque isso aumenta a carga cognitiva.
- Para parar uma tarefa (não só pausar), ofereça essa opção dentro da própria interface, não via botão.
- Pause a função atual quando a pessoa pressiona o Action button junto com o botão lateral, exceto em apps de mergulho, onde pausar pode ser perigoso.

### Especificações exatas
Nenhum número, medida ou duração é dado no texto para este artigo.

### Diferenças por plataforma
Suportado apenas em iOS (iPhone) e watchOS (Apple Watch); não suportado em iPadOS, macOS, tvOS ou visionOS. No Apple Watch Ultra, o botão também cobre ações relacionadas a atividade, incluindo treinos e mergulhos.

### Ligações com outros artigos
Workouts, Digital Crown, App Shortcuts, Live Activities.

<!-- visual:action-button -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 imagem, em aparência clara), código conferido; sem vídeos.
- A única ilustração é um sketch em roxo sobre degradê de rosa para lilás: uma seta horizontal curta aponta para a direita, na direção de uma forma em L invertido (segmento vertical curto que curva e termina num traço horizontal), leitura que sugere a lateral do relógio com o botão na borda (img 0024).
- Sobre o desenho há uma grade de construção pontilhada com círculo e retângulos, mais eixos diagonais, verticais e horizontais centrados no ponto em que a seta encontra a forma em L (img 0024).
- A peça segue o mesmo padrão de sketch com grade geométrica visto no ícone da página de acessibilidade, mudando a paleta para tons de roxo em degradê (img 0024).
<!-- /visual:action-button -->

## Apple Pencil and Scribble (slug: apple-pencil-and-scribble)

### O que governa
Rege como um app de iPad deve responder ao Apple Pencil como instrumento de marcação e ponteiro, e como o Scribble converte escrita à mão em texto em qualquer campo de texto.

### Por que
A Apple ancora o design no comportamento de instrumentos de marcação do mundo real: a pessoa já tem expectativas de como lápis e canetas físicos funcionam, e o app deve honrar essas expectativas em vez de exigir um modo especial. A prioridade central é a sensação de conexão direta e imediata entre a ponta do Pencil e o conteúdo na tela, sem gestos acidentais que causem perda de dados.

### Faça e evite
- Deixe a pessoa alternar livremente entre Apple Pencil e o dedo; controles que não respondem ao Pencil parecem quebrados.
- Permita fazer uma marca no instante em que o Apple Pencil toca a tela, sem exigir toque em botão ou troca de modo antes.
- Use inclinação (altitude), força (pressão), orientação (azimute) e barrel roll para variar a espessura e a intensidade do traço.
- Ao responder à pressão, prefira afetar propriedades contínuas, como opacidade da tinta ou tamanho do pincel.
- Garanta que o Pencil pareça manipular diretamente só o conteúdo que toca; evite ações desconectadas em outras partes da tela.
- Projete para uso com a mão esquerda e com a direita; evite posicionar controles em locais que qualquer uma das mãos possa cobrir, e considere permitir reposicioná-los.
- No hover, mostre uma prévia das dimensões e cor da marca que a ferramenta atual fará; evite modificar a prévia continuamente conforme a distância muda.
- Não use hover para iniciar uma ação, especialmente uma ação destrutiva.
- Prefira mostrar um valor de prévia próximo do meio da faixa dinâmica, não nos extremos.
- Considere usar hover para revelar interações próximas de onde a pessoa está marcando, como um menu de tamanhos ao usar Squeeze ou uma tecla modificadora.
- Prefira restringir a prévia de hover ao Apple Pencil, não a um dispositivo apontador, para evitar confusão.
- Respeite a configuração da pessoa para o gesto de toque duplo (alternar ferramenta/borracha, ferramenta atual/anterior, mostrar/ocultar seletor de cor, ou nada); se o comportamento padrão do sistema não fizer sentido no app, ainda é possível usar o gesto para trocar de modo de interação.
- Se oferecer comportamento customizado de toque duplo, dê um controle para a pessoa escolher esse modo, mas não o ative por padrão.
- Evite usar toque duplo para uma ação que modifique conteúdo, especialmente uma ação destrutiva difícil de desfazer.
- Trate o squeeze (Apple Pencil Pro) como um gesto único e rápido, com ação discreta, não contínua; exiba o resultado prontamente e perto da ponta do Pencil.
- Defina ações de squeeze não destrutivas e fáceis de desfazer.
- Use barrel roll só para modificar o tipo de marca (por exemplo, girar o ângulo de um marcador), não para navegação ou para exibir outros controles.
- Com Scribble, deixe a pessoa escrever em qualquer lugar em que o texto seja aceito, sem precisar tocar ou selecionar o campo antes.
- Torne o Scribble disponível em todo lugar onde faça sentido escrever, mesmo fora de um campo de texto formal (exemplo: criar um lembrete escrevendo abaixo do último item).
- Evite exibir texto de autocompletar enquanto a pessoa escreve, pois pode interferir visualmente; oculte o texto de placeholder assim que a escrita começa.
- Mantenha o campo de texto parado enquanto a pessoa escreve; se não for possível evitar mover ou redimensionar, adie a mudança até a pausa da escrita.
- Evite rolagem automática de texto enquanto a pessoa escreve ou edita, para não atrapalhar a seleção de texto.
- Dê espaço suficiente para escrever; aumente o campo de texto antes ou quando a pessoa pausar a escrita, nunca durante a escrita.
- No PencilKit, evite o ajuste dinâmico de cores do Dark Mode quando a pessoa desenha sobre conteúdo existente (como PDF ou foto), para manter a marcação nítida.
- Considere botões de desfazer e refazer customizados em ambiente compacto, já que o seletor de ferramentas padrão só os inclui em ambiente regular; considere também suportar o gesto padrão de três dedos para desfazer/refazer em qualquer ambiente.

### Especificações exatas
Nenhum valor numérico é dado no corpo do texto do artigo. As imagens descrevem um Apple Pencil inclinado a 45 graus a partir de uma linha horizontal (segundo a descrição da imagem), mas isso não é apresentado como uma especificação de interface no texto.

### Diferenças por plataforma
Recurso exclusivo do iPadOS; não suportado em iOS, macOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Entering data (Undo and redo é citado dentro do texto para o gesto de três dedos).

<!-- visual:apple-pencil-and-scribble -->
### O que as ilustrações mostram
Base: 4 folhas de ilustrações vistas (13 imagens, todas em aparência clara), códigos conferidos; sem vídeos.
- A abertura é um rabisco em ziguezague com espessura variável, em roxo escuro sobre degradê de rosa para roxo, com grade retangular e círculo de construção sobrepostos (img 0147).
- Altitude: o Pencil inclinado apoia a ponta num plano indicado por sombra azul em gradiente, mais escura junto à ponta, e um arco de traços azuis pontilhados à direita marca o ângulo de inclinação a partir da horizontal (img 0148).
- Pressão: a linha traçada começa fina e cinza clara e vai engrossando e escurecendo até ficar preta e grossa perto da ponta; um triângulo azul em gradiente abaixo repete a ideia de intensidade crescente da esquerda para a direita (img 0149).
- Azimute: o Pencil fica equilibrado na ponta sobre um círculo azul pontilhado com marcações de grau em toda a volta, e uma marca mais escura num ponto indica a orientação (img 0150).
- Cada propriedade física ganha seu próprio sistema gráfico de medição (arco, espessura progressiva, círculo de graus), todos na mesma cor azul de destaque (img 0148, img 0149 e img 0150).
- Para uso com as duas mãos, o iPad em paisagem tem três controles circulares azuis empilhados em cada borda lateral (conta-gotas, pincel, comentário); a mão esquerda com o Pencil no canto inferior esquerdo cobre parte dos controles desse lado, e a mão direita, na outra imagem, cobre os do lado direito (img 0151 e img 0152).
- A prévia de hover é uma elipse azul sob a ponta do Pencil pairando sobre um retângulo cinza, em três tamanhos: pequena, no extremo baixo, marcada com X cinza; média, perto do meio da faixa, marcada com check verde; grande, no extremo alto, mostrada sem selo (img 0153 a img 0157).
- No Scribble, dois campos "Name" empilhados comparam largura: o estreito corta a escrita à mão e leva X cinza à esquerda; o largo comporta o nome inteiro e leva check verde à esquerda, com os selos junto do próprio campo (img 0158).
- O conjunto de comandos de desenho muda de arranjo entre ambientes: no iPad em paisagem, uma barra inferior completa com desfazer e refazer à esquerda, canetas e pincéis ilustrados, seletor de cor com círculo preto maior ativo entre amostras menores, e adicionar e mais opções à direita; no iPhone em retrato, a barra superior traz voltar, desfazer, mais opções e um círculo laranja de confirmação, e embaixo fica só uma paleta reduzida com pincéis e cor, sem desfazer na borda inferior (img 0159).
Divergências registradas: a descrição oficial de img 0151 e img 0152 fala em controles obscurecidos em cinza e controles do outro lado destacados, mas nas imagens vistas os seis controles têm o mesmo azul sólido, sem diferença de opacidade entre os lados.
<!-- /visual:apple-pencil-and-scribble -->

## Camera Control (slug: camera-control)

### O que governa
Rege como um app de câmera usa o botão físico Camera Control do iPhone 16 e iPhone 16 Pro para abrir a experiência de câmera e ajustar valores por meio de um overlay com sliders e pickers.

### Por que
O overlay existe para dar acesso rápido a ajustes sem sobrecarregar o visor com controles duplicados; a Apple prioriza um visor grande e livre de distrações, já que as pessoas apreciam uma prévia de captura o mais limpa possível.

### Faça e evite
- Use SF Symbols para representar a função de cada controle; o sistema não suporta símbolos customizados. Os símbolos não representam o estado atual do controle.
- Mantenha os nomes de controles curtos, porque os rótulos seguem os tamanhos de Dynamic Type e nomes longos podem obscurecer o visor.
- Inclua unidades ou símbolos junto ao valor de um slider (por exemplo, EV, %, ou uma string customizada) para dar contexto.
- Defina valores proeminentes para um slider, ou seja, os valores mais escolhidos ou espaçados uniformemente, como os incrementos principais do fator de zoom; o sistema facilita parar nesses valores.
- Deixe espaço para o overlay no visor; posicione a UI do app fora das áreas que o overlay ocupa, tanto em retrato quanto em paisagem.
- Minimize distrações no visor: evite duplicar controles (sliders, toggles) na UI do app quando o overlay do sistema os exibe.
- Habilite ou desabilite controles conforme o modo da câmera (por exemplo, desabilite controles de vídeo ao fotografar); não é possível remover ou adicionar controles em tempo de execução.
- Posicione controles usados com frequência mais ao centro, para acesso rápido, e os menos usados nas extremidades; o sistema lembra o último controle usado no app ao reabrir o overlay.
- Permita lançar a experiência do app a partir de qualquer lugar, incluindo o dispositivo bloqueado, criando uma extensão de captura de câmera bloqueada.

### Especificações exatas
Nenhum número, medida, duração ou proporção é dado no texto.

### Diferenças por plataforma
Suportado apenas em iOS (iPhone 16 e iPhone 16 Pro); não suportado em iPadOS, macOS, watchOS, tvOS ou visionOS.

### Ligações com outros artigos
SF Symbols, Controls.

<!-- visual:camera-control -->
### O que as ilustrações mostram
Base: 4 folhas de ilustrações vistas (16 imagens, todas em aparência clara), códigos conferidos; sem vídeos.
- A abertura desenha a silhueta do iPhone em contorno roxo escuro grosso sobre degradê de rosa para roxo, com uma seta larga apontando para a borda inferior direita do aparelho, onde fica o botão, sob grade tracejada e círculo guia (img 0200).
- Um diagrama anotado sobre o desenho do iPhone usa duas linhas de chamada: uma aponta o botão físico como pequena faixa horizontal na borda, a outra aponta a área cinza logo abaixo como a região em que o overlay aparece, explicitando a relação espacial entre os dois (img 0201).
- O overlay vive numa faixa preta no topo da tela: uma fileira de cinco ícones de controle, com o ativo destacado em laranja e o nome dele, "ZOOM", em laranja centralizado abaixo da fileira (img 0202).
- O slider tem desenho próprio: régua de traços verticais finos brancos com um traço laranja mais grosso no centro e o valor em laranja abaixo; zoom ("1x") e exposição ("0 EV") usam exatamente a mesma régua, mudando só o rótulo do valor (img 0203, img 0205 e img 0206).
- O picker é uma fileira de quatro pontos curtos, com a opção escolhida preenchida em laranja e maior que as cinzas, e o nome da opção escrito por extenso em laranja abaixo (img 0204).
- Na fileira de ícones, o controle ativo se destaca por cor e por tamanho: o raio preenchido do flash e os três círculos sobrepostos dos filtros aparecem em laranja e maiores que os vizinhos, com "FLASH" e "FILTERS" como rótulos (img 0207 e img 0208).
- Par de valor com contexto: a régua com "1 EV" recebe check verde, e a mesma régua com apenas "1", sem unidade, recebe X cinza; o desenho é idêntico e só o texto do rótulo varia (img 0209 a img 0212).
- Na mesma cena noturna de lago lado a lado, a fileira de ícones e o rótulo "ZOOM" formam uma faixa horizontal no topo em retrato e migram para a lateral direita em paisagem, com o obturador branco trocando de posição, mantendo o overlay junto da borda do botão físico (img 0213).
- Visor limpo contra visor duplicado, no mesmo enquadramento: no primeiro só há o rótulo "1x" em laranja no canto superior esquerdo e o obturador branco central; no segundo o app repete valores de zoom empilhados verticalmente à esquerda do obturador ("2", "1x" em laranja, ".5"), além do rótulo do topo (img 0214 e img 0215).
- A linguagem se repete nos controles do overlay: item ativo em laranja, acompanhado de rótulo em laranja logo abaixo, seja ícone, régua ou pontos (img 0202 a img 0209).
<!-- /visual:camera-control -->

## Digital Crown (slug: digital-crown)

### O que governa
Rege o uso da Digital Crown como entrada física no Apple Vision Pro (volume, imersão, recentralização, acessibilidade, sair do app) e no Apple Watch (navegação principal a partir do watchOS 10, rolagem, inspeção de dados).

### Por que
No Apple Watch, a Digital Crown assume o papel de navegação primária porque listas, abas e páginas são organizadas verticalmente, e girar a coroa é o meio mais natural de percorrê-las sem obstruir a tela com o dedo. O feedback tátil por detentes existe para dar uma sensação física à rolagem, reforçando a percepção de progresso.

### Faça e evite
- Ancore a navegação do app na Digital Crown a partir do watchOS 10; reforce sempre essas interações com equivalentes de toque na tela.
- Considere usar a Digital Crown para inspecionar dados quando a navegação não for necessária (exemplo dado: no World Clock, girar a coroa avança o horário de um local selecionado).
- Forneça feedback visual em resposta às interações com a Digital Crown; sem esse feedback, as pessoas presumem que girar a coroa não tem efeito.
- Atualize a interface na mesma velocidade em que a pessoa gira a Digital Crown, para dar controle preciso; evite atualizar em um ritmo que dificulte selecionar valores.
- Use o feedback háptico padrão quando fizer sentido no app; desative os detentes se eles não combinarem com a animação do app, e considere trocar detentes por linha para detentes lineares em tabelas com linhas de alturas muito diferentes.
- Não responda a pressões na Digital Crown: o watchOS reserva essa interação para funcionalidade do sistema, como revelar a Home Screen.

### Especificações exatas
Nenhum número, medida ou duração é dado no texto.

### Diferenças por plataforma
Suportado em visionOS (Apple Vision Pro) e watchOS (Apple Watch); não suportado em iOS, iPadOS, macOS ou tvOS. No Apple Vision Pro, os apps de visionOS não recebem informação direta da Digital Crown; ela serve a funções do sistema (volume, imersão, recentralizar, Acessibilidade, sair do app).

### Ligações com outros artigos
Feedback, Action button, Immersive experiences.

<!-- visual:digital-crown -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (3 imagens, todas em aparência clara), código conferido; sem vídeos.
- A abertura, em degradê roxo e magenta com grade pontilhada e círculo guia, desenha a coroa vista de lado como forma ovalada com sulcos horizontais para a serrilha e, à esquerda, uma seta curva grossa apontando para cima e para a esquerda que sugere o giro; coroa e seta ficam contidas no círculo guia central (img 0461).
- No Apple Vision Pro, uma fotografia real em close de perfil mostra o dedo indicador sobre o botão circular pequeno e serrilhado na lateral, entre a faixa de tecido da têmpora e a viseira, sem nenhuma tela ou interface visível (img 0462).
- No Apple Watch, a fotografia real do relógio com o app de sono ativo (gráfico de barras azuis de estágios) recebe um contorno vermelho em volta da coroa, e o botão lateral logo abaixo fica sem destaque, isolando exatamente qual controle é a Digital Crown (img 0463).
- A página combina ícone esquemático de abertura com fotos reais de produto em dois aparelhos: no Vision Pro a coroa é indicada pelo dedo pousado sobre ela, e no Apple Watch por um contorno vermelho desenhado sobre a foto (img 0461, img 0462 e img 0463).
<!-- /visual:digital-crown -->

## Eyes (slug: eyes)

### O que governa
Rege como o olhar funciona como mira de interação em visionOS: como o sistema realça um elemento quando a pessoa olha para ele (hover effect) e como projetar componentes fáceis de mirar com os olhos.

### Por que
A privacidade é um princípio explícito: o visionOS não informa ao app onde a pessoa está olhando antes de um toque, para preservar a privacidade; o app só sabe quando o componente é de fato acionado. O design para conforto visual busca evitar ajustes oculares rápidos e repetidos, porque isso cansa e distrai; formas arredondadas ajudam porque o olho tende a ser atraído para cantos, dificultando manter o foco no centro de uma forma.

### Faça e evite
- Sempre dê às pessoas mais de uma forma de interagir com o app, suportando recursos de acessibilidade.
- Projete para conforto visual: mantenha os objetos necessários dentro do campo de visão; evite exigir múltiplos ajustes oculares rápidos, seja por uma área grande, seja por múltiplos níveis de profundidade.
- Posicione conteúdo a uma distância confortável de visualização; para leitura ou engajamento prolongado, mire pelo menos um metro de distância.
- Prefira usar componentes de UI padrão do sistema, que respondem de forma consistente ao olhar.
- Minimize distrações visuais; movimento (especialmente na visão periférica) atrai o olhar involuntariamente, então revelar conteúdo perto do que a pessoa está olhando pode desviar a atenção dela.
- Dê espaço suficiente ao redor de cada item para facilitar mirar nele: use uma margem de pelo menos 16 pontos ao redor dos limites de cada item, ou posicione os itens de modo que seus centros fiquem sempre pelo menos 60 pontos separados.
- Evite padrões ou texturas repetitivas que preencham o campo de visão, pois os olhos podem travar em elementos diferentes, dando a impressão de profundidades distintas.
- Considere pistas visuais sutis para encorajar a pessoa a olhar para o item mais provável (posição próxima ao centro do campo de visão, movimento suave, contraste aumentado, variações de cor ou escala); prefira pistas perceptíveis sem serem exageradas.
- Prefira formas arredondadas para itens interativos, porque o olho é atraído para cantos.
- Em componentes formados por mais de um elemento, defina uma forma contentora geral que o visionOS possa realçar por inteiro.
- Ao criar efeitos de hover customizados, defina dois estados (com e sem o efeito); o sistema decide quando aplicar o efeito fora do processo do app, então o app não sabe o momento exato nem pode rodar código que dependa de saber quando a pessoa está olhando.
- Prefira um efeito de hover customizado para enfatizar um momento especial da experiência; excesso de efeitos customizados dilui o impacto, distrai e pode causar desconforto visual.
- Escolha o atraso certo: sem atraso (padrão) para efeitos sutis ou que convidam à interação; atraso curto quando a pessoa precisa olhar e interagir rapidamente (como a expansão de abas em uma tab bar); atraso mais longo quando o efeito mostra informação adicional, como um tooltip.
- Mantenha uma ou mais views primárias do elemento inalteradas entre os dois estados do efeito de hover, para dar estabilidade visual.
- Teste minuciosamente efeitos de hover customizados, de preferência usando o Apple Vision Pro.

### Especificações exatas
- Margem mínima ao redor de cada item interativo: 16 pontos.
- Alternativa: centros dos itens sempre a pelo menos 60 pontos de distância entre si.
- Distância confortável de visualização para leitura ou uso prolongado: pelo menos 1 metro.

### Diferenças por plataforma
Exclusivo do visionOS; não suportado em iOS, iPadOS, macOS, tvOS ou watchOS.

### Ligações com outros artigos
Immersive experiences, Gestures, Spatial layout, Accessibility, Depth, Focus and selection.

<!-- visual:eyes -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações (5 imagens, em aparência clara) e 3 folhas de vídeo (24 quadros de um vídeo) vistas, códigos conferidos.
- A abertura desenha um olho de frente em traço roxo escuro, com contorno em amêndoa, íris circular preenchida e pupila menor vazada em branco, centralizado e inscrito no círculo guia da grade pontilhada sobre degradê rosa e roxo (img 0473).
- A comparação de forma usa o mesmo quadrado cinza médio externo, com mesma cor e tamanho, e varia só a área interna mais clara: quadrado de cantos retos numa versão, círculo na outra (img 0474 e img 0476).
- Os selos ficam em imagens separadas: X branco em círculo cinza claro para a versão quadrada e check branco em círculo verde para a versão circular (img 0475 e img 0477).
- No vídeo, o app Ajustes do visionOS aparece em passthrough sobre um quarto real com violão, janela com persiana e poltrona; a tela tem duas colunas, lista lateral à esquerda com General selecionado e painel de detalhe à direita (vídeo eyes 009, folha 0001, q001).
- Os dois painéis são cartões translúcidos de cantos arredondados flutuando sobre o ambiente; dentro do detalhe, os itens se agrupam em blocos arredondados menores que juntam pares relacionados, como About com Software Update e AirDrop com Handoff, com separador fino entre itens do mesmo bloco (vídeo eyes 009, folhas 0001 a 0003).
- A hierarquia tipográfica traz o título "General" em destaque no topo do painel e os itens em texto branco menor abaixo, e ela não muda ao longo do clipe (vídeo eyes 009, folha 0002, q010 a q018).
- Entre q001 e q024 a câmera, a lista lateral e os grupos nunca mudam de lugar; a única variação é uma diferença sutil de luminosidade em uma linha por vez do painel de detalhe, compatível com o hover passando de linha em linha (vídeo eyes 009, folhas 0001 a 0003).
- O hover não desloca nem redimensiona nada: altera só o realce de fundo da linha mirada, sem recompor o resto da tela (vídeo eyes 009, folha 0002, q010 a q018).
Divergências registradas: a descrição oficial fala em vários ajustes recebendo o hover em sequência conforme o olhar se move; na resolução da grade de quadros não foi possível identificar com segurança qual linha está realçada em cada quadro.
<!-- /visual:eyes -->

## Focus and selection (slug: focus-and-selection)

### O que governa
Rege como o foco (indicador visual de qual componente uma interação vai afetar) funciona em navegação baseada em componentes, usando entradas como remoto, controle de jogo ou teclado, e como o foco se diferencia da seleção.

### Por que
O foco existe para que a pessoa sempre saiba onde está dentro do app; mudar o foco sem a interação da pessoa a obriga a gastar tempo procurando o item recém-focado, atrasando a tarefa. Por isso, confiar nos efeitos de foco do sistema garante consistência e previsibilidade, já que esses efeitos foram ajustados com precisão para as interações com dispositivos Apple.

### Faça e evite
- Confie nos efeitos de foco fornecidos pelo sistema; considere criar efeitos customizados só se for absolutamente necessário.
- Evite mudar o foco sem a interação da pessoa. A exceção é quando a pessoa está movendo o foco com um dispositivo de movimentos discretos e direcionais (teclado, remoto, controle) e o item previamente focado desaparece: nesse caso, mover o foco para um item próximo é aceitável; fora desse cenário, é melhor simplesmente ocultar o indicador de foco.
- Seja consistente com a plataforma ao trazer foco para itens: em iPadOS e macOS, o Full Keyboard Access cobre botões, sliders e toggles, então o app só precisa suportar foco para elementos de conteúdo (itens de lista, campos de texto, campos de busca); em tvOS, o app precisa garantir que todo elemento onscreen seja alcançável por foco.
- Indique o foco com aparências visuais consistentes com a plataforma (exemplo: em iPadOS/macOS, texto branco e destaque de fundo na cor de destaque do app para itens focados de uma lista, e cor de texto padrão com destaque cinza para itens não focados).
- Em geral, use um anel de foco (focus ring) para campo de texto ou busca, mas use um destaque (highlight) em lista ou coleção.
- Em iPadOS 15 e posterior, o sistema de foco suporta interações de teclado para navegar em campos de texto, text views e sidebars, além de collection views e outras views customizadas.
- Evite suportar navegação por teclado para controles como botões, controles segmentados e switches no iPadOS; deixe o Full Keyboard Access cuidar disso.
- No iPadOS, pressionar Tab move o foco entre grupos de foco (áreas como sidebar, grade, lista); pressionar uma seta suporta foco direcional, limitado à navegação entre itens do mesmo grupo de foco.
- Componentes onscreen podem indicar foco pelo efeito halo (anel de foco customizável, aplicável a views customizadas e a conteúdo totalmente opaco dentro de uma célula) ou pela aparência destacada (o texto do componente usa a cor de destaque do app; ocorre automaticamente ao selecionar uma célula de collection view com content configurations definidas).
- Customize o efeito halo quando necessário; por padrão o sistema infere a forma do halo a partir da forma do item, mas é possível ajustar cantos arredondados, caminhos Bézier, ou a posição do halo se outro componente o ocluir.
- Garanta que o foco se mova pelas views customizadas de forma sensata; por padrão, o foco percorre grupos de foco em ordem de leitura (de início a fim, de cima para baixo); ajuste identificando um contêiner como um único grupo de foco quando necessário.
- Ajuste a prioridade de um item dentro de um grupo de foco para refletir sua importância; quando um grupo recebe foco, seu item primário também recebe foco automaticamente.
- Em tvOS, em uma experiência de tela cheia, deixe as pessoas usar gestos para interagir com o conteúdo, não para mover o foco, porque o item em tela cheia não mostra foco.
- Em tvOS, evite exibir um ponteiro; as pessoas esperam navegar por um número fixo de itens mudando o foco, não arrastando um pequeno ponteiro por uma tela grande. Se o app exigir um ponteiro, garanta que seja bem visível e integrado.
- Em tvOS, projete a interface para acomodar componentes em vários estados de foco (até cinco estados visualmente distintos: não focado, focado, escolhido, selecionado, indisponível); forneça assets para o tamanho maior de foco, já que focar geralmente aumenta a escala do item.

### Especificações exatas
Nenhum número, medida ou duração é dado no texto.

### Diferenças por plataforma
- Não suportado em iOS ou watchOS.
- iPadOS 15+: sistema de foco com Tab (entre grupos de foco) e setas (foco direcional dentro do grupo); efeitos halo e destaque.
- tvOS: foco direcional universal por swipe no remote ou setas do teclado; até cinco estados visuais distintos por item focável.
- visionOS: usa o mesmo sistema de foco de iPadOS e tvOS para entrada por teclado ou controle de jogo conectado; o efeito de hover (olhar) é diferente do sistema de foco e não está relacionado a ele.

### Ligações com outros artigos
Eyes, Keyboards.

<!-- visual:focus-and-selection -->
### O que as ilustrações mostram
Base: 3 folhas de ilustrações vistas (9 imagens, todas em aparência clara), códigos conferidos; sem vídeos.
- A abertura, em degradê de rosa para roxo com grade retangular e circular, mostra em roxo escuro sólido um anel grosso com quatro pequenas setas triangulares apontando para fora (cima, baixo, esquerda, direita) e um disco cheio no centro, forma que remete a travar o foco (img 0481).
- No iPadOS, numa grade de seis fotos em duas linhas e três colunas, a foto focada recebe um halo azul grosso e contínuo que segue o retângulo da célula, com cantos retos e colado à borda da foto (img 0482).
- Na mesma grade, a variante do halo tem cantos arredondados e fica levemente afastada da borda da foto, com respiro visível; a forma muda entre as duas versões, a cor azul permanece (img 0482 e img 0483).
- Na aparência destacada de lista, entre sete itens com estrela vazia e "Title", o segundo ganha fundo cinza claro arredondado, a estrela passa de contorno a preenchida e ícone e texto ficam em vermelho, a cor de destaque do app, tudo sem halo nem elevação; os demais seguem pretos sobre branco, sem realce (img 0484).
- No tvOS, os estados são mostrados com o mesmo botão em pílula, no mesmo ponto da mesma foto de praia, variando uma coisa por vez: sem foco, a pílula é cinza translúcida, deixa a textura da areia aparecer atenuada, tem texto preto e é a menor da série (img 0485).
- Com foco, a pílula vira branca opaca, sem transparência, e fica maior, com texto preto grande (img 0486).
- Destacado e selecionado também usam pílula branca opaca com texto preto, em porte visualmente semelhante ao do botão com foco (img 0487 e img 0488).
- Indisponível volta ao fundo cinza translúcido e usa texto acinzentado de contraste bem mais baixo, o botão mais apagado da sequência (img 0489).
Divergências registradas: a descrição oficial diz que o botão destacado tem o mesmo tamanho do botão sem foco, mas na imagem ele parece do porte do botão com foco, com a ressalva da margem de erro de leitura em miniatura (img 0487); a diferença de sombra entre estados citada na descrição não é distinguível na resolução vista (img 0488).
<!-- /visual:focus-and-selection -->

## Game controls (slug: game-controls)

### O que governa
Rege como um jogo suporta entrada por controles físicos de jogo e pelos métodos de interação padrão de cada plataforma (toque, remoto, mouse e teclado), incluindo controles virtuais em tela, mapeamento de botões físicos e atalhos de teclado específicos de jogo.

### Por que
A Apple recomenda apoiar tanto controles físicos quanto os métodos padrão da plataforma porque nem todo jogador tem acesso a um controle físico, e porque jogadores valorizam poder usar o método de interação com o qual já estão familiarizados; o objetivo é alcançar o público mais amplo possível.

### Faça e evite
- Decida se faz sentido mostrar controles virtuais sobre o conteúdo do jogo; procure reduzir a sobreposição associando ações a gestos diretos no jogo quando possível (exemplo: tocar em objetos para selecioná-los em vez de um botão de seleção virtual).
- Posicione botões virtuais onde sejam fáceis de alcançar, respeitando limites do dispositivo, guias e áreas seguras; não sobreponha o Home indicator nem o Dynamic Island no iPhone; posicione botões frequentes perto do polegar do jogador, evitando as regiões circulares de movimento e câmera; posicione controles secundários (como menus) no topo da tela.
- Garanta tamanho mínimo dos controles: 44x44 pt para controles usados com frequência, 28x28 pt para controles menos importantes, como menus.
- Sempre inclua estados de pressão visíveis e táteis; combine o estado de pressão com som e hápticos.
- Use símbolos que comuniquem a ação que o botão executa (por exemplo, uma arma para ataque); evite formas abstratas ou nomenclatura baseada no controle físico, como A, X ou R1.
- Mostre e oculte controles virtuais conforme a jogabilidade, reduzindo a poluição visual e ajudando o jogador a se concentrar (exemplo: ocultar controles de movimento até o jogador tocar a tela).
- Combine funcionalidade em um único controle; considere redesenhar mecânicas que exigem pressionar múltiplos botões simultaneamente ou em sequência; aproveite gestos como toque duplo e toque e segure para variações da mesma ação.
- Mapeie movimento para o lado esquerdo da tela e câmera para o lado direito, como o esperado; use a maior área de entrada possível; para movimento, prefira mostrar um thumbstick virtual onde o polegar pousar, em vez de posição fixa; para câmera, prefira toque direto em vez de thumbstick virtual.
- Suporte o método de interação padrão da plataforma como alternativa a controles físicos, já que um controle de jogo é uma compra opcional.
- Em tvOS e visionOS, é possível exigir um controle de jogo físico; o App Store exibe um selo "Game Controller Required" nesse caso; ainda assim, verifique a presença do controle e solicite a conexão de forma elegante, já que a pessoa pode abrir o jogo sem um conectado.
- Detecte automaticamente se um controle está pareado e obtenha seu perfil, em vez de exigir configuração manual.
- Customize o conteúdo onscreen para corresponder ao controle conectado, já que cores e símbolos reais podem diferir dos nomes padrão do framework Game Controller.
- Mapeie botões do controle ao comportamento de UI esperado fora da jogabilidade: A ativa um controle; B cancela uma ação ou volta à tela anterior; ombro esquerdo navega para a esquerda entre telas ou seções; ombro direito navega para a direita; thumbstick esquerdo/direito e direcional movem a seleção; Home/logo é reservado para controles do sistema; Menu abre configurações do jogo ou pausa a jogabilidade. Os botões X, Y, gatilho esquerdo e gatilho direito não têm comportamento de UI padronizado definido.
- Suporte múltiplos controles conectados, usando rótulos e glifos que correspondem ao controle ativamente em uso; em multiplayer, use rótulos e símbolos do controlador específico de cada jogador.
- Prefira símbolos, não texto, para se referir a elementos do controle de jogo, já que o Game Controller framework disponibiliza SF Symbols para a maioria dos elementos.
- No teclado, priorize comandos de tecla única, mais rápidos e fáceis, especialmente durante o uso simultâneo de mouse ou trackpad; teste o conforto do key binding em um teclado Apple, considerando remapear Control (^) para Command (⌘) quando vier de um teclado não Apple; leve em conta a proximidade física das teclas ao definir comandos relacionados (exemplo: teclas numéricas para categorias de inventário); deixe os jogadores customizar os key bindings.
- Em visionOS, faça o controle de jogo espacial (como o PlayStation VR2 Sense) se comportar de modo similar à entrada por mãos: suporte olhar para um objeto e pressionar o gatilho esquerdo ou direito para interação indireta, ou alcançar e pressionar o gatilho para interação direta.

### Especificações exatas
- Tamanho mínimo de controles virtuais usados com frequência: 44x44 pt.
- Tamanho mínimo de controles virtuais menos importantes (menus): 28x28 pt.

### Diferenças por plataforma
Sem considerações adicionais específicas para iOS, iPadOS, macOS ou tvOS além do já descrito; não suportado em watchOS. Em visionOS, há orientação específica para controles de jogo espaciais e correspondência com entrada por mãos.

### Ligações com outros artigos
Designing for games, Gestures, Keyboards, Playing haptics, Touch Controller, Game Controller.

<!-- visual:game-controls -->
### O que as ilustrações mostram
Base: 3 folhas de ilustrações vistas (10 imagens, todas em aparência clara), códigos conferidos; sem vídeos.
- A abertura desenha uma cruzeta direcional em contorno roxo escuro sólido, inscrita no círculo guia da grade de construção, sobre degradê de rosa para roxo (img 0513).
- O estado pressionado de um botão virtual aparece em traço: a mão direita segura o iPhone em paisagem e o polegar pressiona o botão com X, que fica mais escuro, preenchido e de contorno mais grosso que os botões de triângulo e quadrado ao lado, com um traço extra ao redor sugerindo brilho; um botão circular maior ocupa o canto inferior esquerdo (img 0515).
- Os botões virtuais dessa ilustração reaproveitam a linguagem de controle físico, com símbolos de triângulo, quadrado e X em coluna (img 0515).
- O mapeamento de entrada para ação é desenhado como dois círculos cinza ligados por seta: o botão do controle com símbolo de quadrado leva à ação no jogo representada por uma mão fazendo o gesto de pegar, cada lado com seu rótulo de texto (img 0516).
- O mesmo thumbstick virtual, na mesma cena e enquadramento, muda com o uso: em movimento fica branco opaco e bem visível, com pequena seta curva indicando direção; em repouso vira cinza escuro translúcido, sem contorno de destaque nem seta (img 0517 e img 0518).
- Toque simples e toque prolongado são diferenciados no mesmo botão cinza com ícone de chama: o primeiro tem anel completo ao redor, o segundo um anel parcial, como indicador de progresso circular incompleto (img 0519).
- A divisão da tela é feita sobre uma única imagem de jogo cortada ao meio por molduras coloridas: metade esquerda com borda vermelha para controles de movimento, metade direita com borda ciano para controles de câmera (img 0520).
- O diagrama do controle físico, em contorno cinza claro visto de frente, rotula em pares esquerda e direita os botões de ombro, gatilhos e thumbsticks (o esquerdo mais alto, o direito mais baixo), além do botão de menu pequeno no centro superior e da cruzeta; os quatro botões de ação à direita, em losango, ficam sem rótulo (img 0521).
- O app SF Symbols no Mac aparece com a categoria Gaming selecionada na barra lateral, 234 símbolos, numa grade de ícones com o nome técnico sob cada um (img 0522).
Divergências registradas: a descrição oficial de img 0514 fala num gráfico com o posicionamento ideal dos controles de toque, mas a imagem vista está toda desfocada e nenhuma marcação, seta ou zona de posicionamento é legível.
<!-- /visual:game-controls -->

## Gestures (slug: gestures)

### O que governa
Rege o vocabulário de gestos físicos (tap, swipe, drag e outros) que as pessoas usam para manipular diretamente objetos em um app ou jogo, em telas sensíveis ao toque, no ar, ou em dispositivos de entrada como trackpad, mouse, remoto ou controle de jogo com superfície de toque.

### Por que
A consistência é o princípio central: como as pessoas esperam que a maioria dos gestos funcione da mesma forma independentemente do contexto, usar um gesto familiar para uma ação exclusiva do app (ou inventar um gesto único para uma ação padrão) quebra essa expectativa. Gestos customizados só se justificam para tarefas especializadas e frequentes que os gestos padrão não cobrem.

### Faça e evite
- Dê à pessoa mais de uma forma de interagir com o app, já que muitas preferem ou precisam usar voz, teclado ou Switch Control; não presuma que um gesto específico está sempre disponível.
- Responda a gestos de forma consistente com as expectativas das pessoas; evite usar um gesto familiar como tap ou swipe para uma ação exclusiva do app, e evite criar um gesto único para uma ação padrão, como ativar um botão ou rolar uma view.
- Trate os gestos com a maior responsividade possível, fornecendo feedback que ajude a prever o resultado e, se necessário, comunique a extensão e o tipo de movimento necessário.
- Indique claramente quando um gesto não está disponível; sem essa comunicação, a pessoa pode achar que o app travou ou que está executando o gesto errado.
- Adicione gestos customizados só quando necessário, para tarefas especializadas e frequentes não cobertas por gestos existentes (exemplo: um jogo ou app de desenho); o gesto customizado precisa ser descobrível, simples de executar, distinto de outros gestos, e nunca a única forma de realizar uma ação importante.
- Torne os gestos customizados fáceis de aprender, oferecendo momentos no app para ensiná-los e testando em cenários reais de uso.
- Use gestos de atalho para complementar gestos padrão, não substituí-los; mesmo com um atalho, mantenha a forma familiar (exemplo: um botão Voltar na toolbar, além de um gesto de deslizar da borda).
- Evite conflitar com gestos que acessam a UI do sistema, como o deslizar de borda no watchOS ou o rolar a mão para acessar overlays do sistema no visionOS.
- Em iOS e iPadOS, considere permitir reconhecimento simultâneo de múltiplos gestos quando isso melhora a experiência, como em um jogo com joystick e botões de disparo operados ao mesmo tempo.
- No visionOS, ofereça tanto gestos indiretos (olhar para focar e manipular à distância, como juntar rapidamente dedo e polegar) quanto diretos (tocar fisicamente o objeto, funcionando melhor dentro do alcance e para uso pouco frequente, já que manter os braços erguidos cansa).
- No visionOS, suporte gestos padrão em todo lugar possível, mesmo oferecendo gestos customizados.
- No visionOS, prefira gestos indiretos para UI e componentes comuns como botões; reserve gestos diretos e customizados para objetos que convidam interação de proximidade ou movimentos específicos de jogo.
- No visionOS, evite exigir movimentos ou posições corporais específicas como única forma de entrada; considere entradas alternativas.
- No visionOS, ao projetar gestos customizados, priorize o conforto, testando continuamente a ergonomia; evite exigir braços erguidos por muito tempo; tenha cautela com gestos complexos que envolvam múltiplos dedos ou ambas as mãos, considerando alternativa com menos movimento; evite gestos customizados que exijam uma mão específica.
- No visionOS 2+, reserve a área ao redor da mão da pessoa para os overlays do sistema (Home e Control Center) e seus gestos; evite ancorar conteúdo às mãos ou pulsos, ou posicione-o fora da área imediata da mão; considere adiar o comportamento do overlay do sistema em apps imersivos, exigindo um toque para revelar o Home indicator, quando fizer sentido para manter a pessoa na narrativa.
- Use cautela com gestos customizados que envolvam rolar a mão, o pulso e o antebraço, movimento reservado para revelar overlays do sistema.
- No watchOS 11+, use o toque duplo com cuidado: evite defini-lo como ação primária em views com listas, scroll views ou abas verticais, pois conflita com a navegação padrão; escolha para ação primária o botão mais usado em uma view sem rolagem (exemplo: o botão de play/pause em uma view de controles de mídia).

### Especificações exatas
Nenhuma medida numérica (pt, px, ms) é dada no texto; a tabela de especificações lista apenas os gestos padrão e as plataformas em que cada um é suportado, sem valores.

### Diferenças por plataforma
- iOS, iPadOS: suportam também swipe de três dedos (desfazer à esquerda, refazer à direita), pinch de três dedos (copiar ao juntar, colar ao afastar), swipe de quatro dedos exclusivo do iPadOS (trocar entre apps), e shake (desfazer/refazer).
- macOS: interação primária via teclado e mouse; gestos padrão também disponíveis em Magic Trackpad, Magic Mouse ou controle de jogo com superfície de toque.
- tvOS: gestos padrão via remoto compatível, Siri Remote, ou controle de jogo com superfície de toque.
- visionOS: suporta gestos indiretos e diretos; gestos diretos padrão incluem touch, touch and hold, touch and drag, double touch, swipe, pinch com duas mãos (zoom) e pinch com movimento circular de duas mãos (rotacionar); há também gestos de sistema para overlays (Home, Control Center) via olhar para a palma da mão.
- watchOS: suporte a double tap a partir do watchOS 11 para rolar listas e scroll views, avançar entre abas verticais, e acionar uma ação primária definida pelo app; também funciona em ações customizadas de notificações, agindo na primeira ação não destrutiva.

### Ligações com outros artigos
Feedback, Eyes, Playing haptics, Accessibility, Apple Pencil and Scribble, Standard gestures (Pointing devices, Remotes, Game controls).

<!-- visual:gestures -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações (8 imagens, em aparência clara) e 3 folhas de vídeo de dois vídeos (6 e 11 quadros, vistos por inteiro), códigos conferidos.
- A abertura desenha uma mão em contorno roxo escuro grosso, com indicador esticado e demais dedos dobrados, e um traço curvo que sai da base do indicador, contorna a mão por trás e termina acima dela, sugerindo um deslizar em arco para a direita (img 0528).
- O gesto customizado aparece dentro do contexto real de um jogo em visionOS: sala de estar com placar "14 score" flutuando à esquerda e barra de controle de mídia, as duas mãos formando um coração com polegares e indicadores, e um efeito luminoso rosa e roxo em forma de gota saindo de cima do gesto como resposta visual (img 0529).
- Em traço simples, a mão aberta de palma para cima tem acima e ao redor um círculo azul tracejado, maior que a própria mão, que delimita a área reservada aos overlays do sistema (img 0530).
- A sequência em traço separa as revelações: sem o círculo, um pequeno botão circular cinza com ícone de círculo surge acima da palma (img 0531); com a mão girada, dorso voltado para quem olha, surge acima dela uma pílula de status com hora, bateria com porcentagem, Wi-Fi e um botão redondo de volume à direita (img 0532). As duas revelações nunca aparecem na mesma imagem.
- O traço simples fica para ensinar zonas e estados do sistema, e a fotografia fica para o comportamento em contexto (img 0530 a img 0535).
- Padrão em Shared Space e em Full Space: a mesma mão real, palma para cima e com o mesmo botão cinza acima, é mostrada sobre uma sala real e depois sobre uma floresta imersiva; só o fundo muda (img 0533 e img 0534).
- Comportamento adiado: a mão coberta por luva volumosa de traje espacial branco, palma para cima sobre céu estrelado, sem nenhum botão acima dela (img 0535).
- Gesto indireto, primeira fase: numa barra de três botões circulares (compartilhar, coração, mais) no topo de uma janela translúcida, o fundo do botão de coração clareia progressivamente de cinza translúcido até quase branco, enquanto os outros dois não mudam e o ícone continua acinzentado, sem contorno definido (vídeo gestures 010, folha 0001, q001 a q004).
- Gesto indireto, segunda fase: de q004 para q005 o botão passa a fundo branco sólido opaco com o coração em contorno preto nítido, e fica assim em q006; em nenhum momento mudam posição, tamanho ou os demais botões. Um recorte no canto inferior direito mostra, vistas de cima, duas mãos sobre superfície cinza (vídeo gestures 010, folha 0001, q004 a q006).
- Gesto direto: numa sala em passthrough, uma coluna vermelha com divisórias horizontais, que sugere blocos empilhados, está sobre um tampo claro; a mão surge na borda inferior direita em q003, aproxima-se da base em q004 e, em q005, com os dedos estendidos tocando a base, dois blocos giram no ar, um deles mostrando face branca; em q006 a mão já saiu e restam três cubos vermelhos espalhados lado a lado (vídeo gestures 011, folha 0001, q001 a q006).
- No gesto direto não há realce nem halo antes do contato, e a resposta é física, com queda e rotação, em vez de mudança de aparência como no botão do gesto indireto (vídeo gestures 011, folha 0001, q004 a q006, comparado ao vídeo gestures 010).
- De q006 ao fim os cubos ficam imóveis, com leves reenquadramentos de câmera, e o clipe termina sem nenhum elemento de interface 2D em cena (vídeo gestures 011, folhas 0001 e 0002, q006 a q011).
Divergências registradas: a descrição oficial do vídeo 010 diz que o recorte mostra a mão fazendo o toque indireto de polegar e indicador, mas na resolução vista só se distinguem duas mãos com uma área clara perto dos dedos, sem confirmar o gesto exato; no vídeo 011 a descrição fala em três blocos empilhados, e a contagem inicial não é legível nos quadros por causa das sombras e da cor uniforme, embora o resultado final de três cubos seja consistente.
<!-- /visual:gestures -->

## Gyroscope and accelerometer (slug: gyro-and-accelerometer)

### O que governa
Rege o uso de dados de giroscópio e acelerômetro do dispositivo para experiências baseadas em movimento em tempo real.

### Por que
O princípio é usar dados de movimento apenas quando trazem um benefício tangível para a pessoa; a Apple desestimula coletar dados só por coletar, e reconhece que gestos baseados em movimento podem ser fisicamente difíceis para algumas pessoas replicarem com precisão, além de afetarem a bateria.

### Faça e evite
- Use dados de movimento só para oferecer um benefício tangível (exemplo: um app de fitness usando os dados para dar feedback sobre atividade e saúde geral, ou um jogo usando-os para melhorar a jogabilidade).
- Forneça um texto explicando por que o app precisa acessar dados de movimento; esse texto aparece na solicitação de permissão do sistema na primeira tentativa de acesso.
- Fora da jogabilidade ativa, evite usar acelerômetros ou giroscópios para manipulação direta da interface, já que alguns gestos baseados em movimento podem ser difíceis de replicar com precisão, fisicamente desafiadores para algumas pessoas, e afetar o uso da bateria.

### Especificações exatas
Nenhum número, medida ou duração é dado no texto.

### Diferenças por plataforma
Disponível em iOS, iPadOS e watchOS; apps de tvOS podem usar dados de giroscópio do Siri Remote. Sem considerações adicionais específicas por plataforma além disso; não há menção de suporte em macOS ou visionOS.

### Ligações com outros artigos
Feedback, Core Motion.

<!-- visual:gyro-and-accelerometer -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 imagem, em aparência clara, sem versão escura no lote), código conferido; sem vídeos.
- O ícone de abertura desenha o giroscópio como anéis vazados entrelaçados, e não como formas sólidas: um círculo externo e dois elos ovais cruzados em X, em roxo escuro sobre gradiente de rosa para roxo (img 0537).
- Um traço diagonal reto atravessa o conjunto de canto a canto e sugere o eixo de rotação do giroscópio (img 0537).
- Sobre o desenho há uma grade fina de linhas horizontais, verticais e um par de diagonais, mais círculos concêntricos tracejados; é guia de construção discreta, sem cotas nem números (img 0537).
- O cartão tem cantos arredondados e proporção larga, e a peça usa uma única cor de tinta sobre o gradiente, o que liga o ícone a uma das cores do logo de seis cores dentro de um sistema cromático por seção (img 0537).
<!-- /visual:gyro-and-accelerometer -->

## Keyboards (slug: keyboards)

### O que governa
Rege o uso de teclado físico como entrada essencial (texto, jogos, controle de apps) e os atalhos de teclado padrão e customizados, incluindo o Full Keyboard Access.

### Por que
Atalhos de teclado padrão existem para funcionar de forma consistente em todo o sistema e na maioria dos apps, permitindo que a pessoa transfira o conhecimento que já tem para experiências novas; por isso a regra geral é não reapropriar um atalho padrão, a menos que a ação original simplesmente não faça sentido na experiência.

### Faça e evite
- Suporte o Full Keyboard Access quando possível (disponível em iOS, iPadOS, macOS e visionOS), permitindo navegar e ativar janelas, menus, controles e recursos do sistema só com o teclado.
- No iPadOS, evite suportar navegação por teclado para controles como botões, controles segmentados e switches; deixe que o Full Keyboard Access cuide da ativação de controles, navegação para todos os componentes onscreen, e interações baseadas em gesto como arrastar e soltar.
- Respeite os atalhos de teclado padrão que funcionam em outros apps e no sistema; para uma ação exclusiva usada com frequência, prefira criar um atalho customizado em vez de reaproveitar um atalho padrão associado a outra ação.
- Em jogos, as pessoas esperam certos atalhos padrão (como Command-Q para sair), mas também esperam poder modificar os key bindings de cada jogo conforme o estilo de jogo pessoal.
- Em geral, não reaproprie atalhos de teclado padrão para ações customizadas; só considere redefinir um atalho padrão se sua ação original não fizer sentido na experiência (exemplo dado: um app sem edição de texto pode reaproveitar Command-I, normalmente Itálico, para "Get Info").
- Defina atalhos de teclado customizados só para os comandos específicos do app mais usados; definir atalhos demais pode fazer o app parecer difícil de aprender.
- Use teclas modificadoras da forma esperada (exemplo: Command ao arrastar move itens como grupo; Shift ao arrastar-redimensionar restringe à proporção original; segurar uma seta move o item selecionado pela menor unidade definida pelo app até soltar a tecla).
- Prefira Command como modificador principal em um atalho customizado; use Shift como modificador secundário complementar; use Option com moderação, para comandos menos comuns ou recursos avançados; evite usar Control como modificador, já que o sistema o usa amplamente em recursos e atalhos em todo o sistema.
- Evite usar um modificador adicional com caracteres que não estão disponíveis em todos os teclados; se precisar de um modificador diferente de Command, prefira usá-lo só com caracteres alfabéticos.
- Liste teclas modificadoras na ordem correta quando houver mais de uma: Control, Option, Shift, Command.
- Evite adicionar Shift a um atalho que já usa o caractere superior de uma tecla de dois caracteres (exemplo: o atalho de Ocultar Barra de Status é Command-Barra, e o de Ajuda é Command-Interrogação, não Shift-Command-Barra).
- Deixe o sistema localizar e espelhar os atalhos conforme necessário, automaticamente, inclusive em layouts da direita para a esquerda.
- Evite criar um atalho novo adicionando um modificador a um atalho existente para um comando não relacionado (exemplo: evite Shift-Command-Z para algo sem relação com desfazer/refazer, já que as pessoas associam Command-Z a desfazer).
- Em visionOS, escreva títulos de atalho descritivos, já que a interface de atalhos mostra uma lista plana por categoria, sem títulos de submenu para dar contexto.

### Especificações exatas
A tabela completa de atalhos padrão do macOS está reproduzida no texto (por exemplo, Command-Space para Spotlight, Command-C para copiar, Command-Q para sair, etc.), sem valores numéricos de medida associados, são combinações de teclas, não medidas físicas. A ordem correta de modificadores em um atalho customizado é: Control, Option, Shift, Command.

### Diferenças por plataforma
Sem considerações adicionais específicas para iOS, iPadOS, macOS ou tvOS além do descrito; não suportado em watchOS. Em visionOS, os atalhos de teclado aparecem em uma interface de atalho exibida ao segurar a tecla Command em um teclado conectado, organizada como a menu bar do iPad ou Mac, mas mostrando todas as categorias relevantes em uma única view; ao conectar um teclado físico em visionOS, o sistema exibe um overlay de teclado virtual com autocompletar e outros controles.

### Ligações com outros artigos
Virtual keyboards, Entering data, Pointing devices, Game controls, Focus and selection, Right to left.

<!-- visual:keyboards -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações (5 imagens, em aparência clara) e 2 folhas de vídeo (10 quadros, seção visionOS) vistas, códigos conferidos.
- A abertura desenha um teclado visto de cima: retângulo de cantos arredondados com fileiras de teclas quadradas e uma tecla longa embaixo como barra de espaço, num cartão roxo em degradê, com grade pontilhada retangular e um círculo grande centralizado, o mesmo esquema de construção das aberturas vistas em azul e amarelo (img 0671, comparada a img 0644 e img 0667).
- Os quatro glifos de modificador formam um conjunto único: contorno preto fino, sem preenchimento e sem cor, isolados sobre fundo branco, em proporção semelhante entre si e bem menores que a ilustração de abertura (img 0672 a 0675).
- Command é um trevo de quatro laços ligados por retas, e Shift é uma seta para cima em contorno, com corpo retangular estreito e ponta triangular (img 0672, img 0673).
- Option é feito de segmentos em Z deitado com um traço horizontal curto alinhado ao topo, e Control é um V invertido raso e largo, como um circunflexo achatado (img 0674, img 0675).
- O material estático se limita ao ícone e aos glifos: nenhuma imagem mostra tela de app, teclado físico completo ou tabela de atalhos (img 0671 a 0675).
- No vídeo, a cena é real e doméstica: mesa redonda de madeira clara vista de cima, teclado físico branco e trackpad branco, mãos digitando; o único elemento de interface visionOS é uma barra estreita, marrom escura e translúcida, flutuando acima do teclado, com texto branco pequeno no centro e controles nas pontas (vídeo 014, folha 0001, q001 a q009).
- O texto dentro da barra muda a cada quadro enquanto os dedos trocam de posição, o que aparenta ser digitação em tempo real, embora o texto seja pequeno demais para ler com segurança (vídeo 014, folha 0001, q001 a q003).
- A barra varia levemente de largura entre quadros, mais estreita em q004 e q005 e um pouco mais larga em q006, mantendo o texto centralizado (vídeo 014, folha 0001).
- A posição da barra fica fixa em relação ao teclado, acima e um pouco à esquerda, do primeiro ao último quadro, enquanto as mãos mudam de pose sem sair do lugar; as notas leem isso como o overlay tomando o teclado físico, e não as mãos, como referência espacial (vídeo 014, folha 0001 q001 a folha 0002 q010).
Divergências registradas: a descrição oficial fala de uma janela virtual com o texto digitado e sugestões, mas os 10 quadros mostram apenas uma faixa estreita, sem janela grande nem lista de sugestões separada; o texto da barra é pequeno demais para ler, então as sugestões só se confirmam pela presença da barra, não pelo conteúdo.
<!-- /visual:keyboards -->

## Nearby interactions (slug: nearby-interactions)

### O que governa
Rege experiências que integram a presença de pessoas e objetos próximos usando o hardware Ultra Wideband e o framework Nearby Interaction, como transferir áudio ao aproximar dispositivos.

### Por que
O princípio central é enraizar a interação na percepção física natural das pessoas do mundo ao redor: a Apple busca inspiração observando como a tarefa funcionaria no mundo físico, e prioriza informação próxima e contextualmente relevante para criar experiências que pareçam orgânicas. A privacidade é preservada por identificadores de dispositivo gerados aleatoriamente que duram só o tempo da sessão de interação.

### Faça e evite
- Considere a tarefa a partir da perspectiva do mundo físico para encontrar inspiração (exemplo: aproximar fisicamente os dispositivos para transferir uma música, em vez de usar só a UI do app).
- Use distância, direção e contexto para informar a interação, priorizando informação próxima e contextualmente relevante (exemplo: o share sheet do iOS sugerindo o contato mais próximo e de frente usando informação de dispositivos com o chip U1).
- Considere como mudanças de distância física podem guiar a interação, espelhando a expectativa de que a percepção de um objeto se aguça ao se aproximar dele (exemplo: ao procurar um AirTag, o display transita de uma seta direcional para um círculo pulsante conforme a pessoa se aproxima).
- Forneça feedback contínuo, que reflita o dinamismo do mundo físico e reforce a conexão entre a interação e a tarefa (exemplo: atualizações contínuas de direção e proximidade ao procurar um item perdido no Find My).
- Considere usar múltiplos tipos de feedback (visual, sonoro, háptico) para uma experiência mais holística, coordenando o tipo de feedback com a tarefa e o contexto atual (visual quando a pessoa interage com a tela; sonoro e háptico quando interage com o ambiente).
- Evite usar uma interação de proximidade como a única forma de realizar uma tarefa, já que nem todo mundo pode experimentá-la.
- Encoraje a pessoa a segurar o dispositivo em orientação retrato, já que segurar em paisagem pode reduzir a precisão e a disponibilidade da informação de distância e direção; se o recurso só suportar retrato, prefira dar feedback visual implícito em vez de instruir explicitamente.
- Projete para o campo de visão direcional do dispositivo, já que o sensor tem um campo de visão específico, semelhante ao da câmera Ultra Wide do iPhone 11 e posteriores; fora desse campo, o app pode receber distância mas não direção relativa.
- Ajude a pessoa a entender como objetos interpostos (pessoas, animais, objetos grandes) podem reduzir a precisão ou disponibilidade da informação; considere adicionar orientação sobre isso no onboarding ou tutorial.

### Especificações exatas
Nenhum número, medida ou duração é dado no texto.

### Diferenças por plataforma
Sem considerações adicionais para iPadOS; não suportado em macOS, tvOS ou visionOS. No iOS (iPhone), as APIs de Nearby Interaction fornecem distância e direção de um dispositivo par. No watchOS, fornecem apenas a distância, e todos os apps de watchOS participando de uma interação de proximidade precisam estar em primeiro plano.

### Ligações com outros artigos
Feedback, Ultra Wideband availability, Nearby Interaction (framework).

<!-- visual:nearby-interactions -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 imagem, em aparência clara), código conferido; sem vídeos.
- O sketch de abertura é tingido num tom entre roxo e magenta e assenta sobre a mesma grade de linhas e o mesmo círculo guia das outras páginas de abertura do HIG (img 0806).
- A forma central é um círculo grande de contorno grosso com um ponto sólido menor dentro, lido como uma pessoa ou sensor visto de cima (img 0806).
- À direita do círculo há duas curvas concêntricas em forma de ondas, dobradas sobre um eixo vertical, e elas aparecem só desse lado (img 0806).
- A direção é comunicada por assimetria: as ondas não envolvem o círculo, chegam de um único lado, o que reforça a ideia de uma fonte vindo de uma direção específica, em linha com a descrição oficial (img 0806).
<!-- /visual:nearby-interactions -->

## Pointing devices (slug: pointing-devices)

### O que governa
Rege o uso de dispositivos apontadores (trackpad, mouse) para navegar a interface e iniciar ações, incluindo o sistema de ponteiro do iPadOS (formas, efeitos de conteúdo, magnetismo, acessórios) e os ponteiros e gestos padrão do macOS.

### Por que
No Mac, o dispositivo apontador é tipicamente combinado com o teclado; no iPad e no Vision Pro, ele é uma forma adicional de interagir, sem substituir toque, olhos ou gestos. A consistência sistêmica é central: as pessoas esperam que os mesmos gestos funcionem da mesma forma em todo app ou jogo, e que possam se mover fluidamente entre modos de entrada sem aprender interações diferentes para cada um.

### Faça e evite
- Seja consistente ao responder a gestos de mouse e trackpad, já que as pessoas esperam que a maioria dos gestos funcione da mesma forma em todo o sistema.
- Evite redefinir gestos de trackpad em nível de sistema, mesmo em um jogo com gestos customizados específicos do app; lembre-se de que as pessoas podem customizar esses gestos.
- Ofereça uma experiência consistente no app, seja a pessoa usando gestos, olhos, um dispositivo apontador ou teclado.
- Deixe a pessoa usar o ponteiro para revelar e ocultar controles que minimizam ou desaparecem automaticamente (exemplo: revelar a barra de ferramentas minimizada do Safari segurando o ponteiro sobre ela no iPadOS).
- Ofereça uma experiência consistente ao segurar uma tecla modificadora enquanto interage com objetos, garantindo o mesmo resultado ao arrastar com toque ou com o ponteiro.
- No iPadOS, permita seleção múltipla em views customizadas quando necessário; em iPadOS 15+, clicar e arrastar o ponteiro sobre múltiplos itens os seleciona, expandindo-se em um retângulo visível; collection views padrão não-lista suportam isso por padrão.
- No iPadOS, distinga entre entrada por ponteiro e por dedo só se isso agregar valor (exemplo: um scrubber que permite clicar um ponto exato de busca com o ponteiro).
- No iPadOS, suporte os efeitos de conteúdo do sistema quando possível: highlight (retângulo translúcido arredondado com leve parallax, aplicado por padrão a bar buttons, tab bars, controles segmentados e menus de edição), lift (parallax sutil com aparência de elevação, aplicado por padrão a ícones de app e botões da Control Center) e hover (efeito genérico com escala, tinta ou sombra customizáveis, sem transformar a forma padrão do ponteiro).
- Use highlight para um elemento pequeno com fundo transparente; use lift para um elemento pequeno com fundo opaco; use hover para elementos grandes.
- Prefira as aparências de ponteiro fornecidas pelo sistema para botões padrão e áreas de entrada de texto.
- Adicione padding ao redor de elementos interativos para criar regiões de toque confortáveis; em geral funciona bem cerca de 12 pontos de padding ao redor de elementos com bezel, e cerca de 24 pontos ao redor de elementos sem bezel.
- Crie regiões de toque contíguas para bar buttons customizados, evitando que o ponteiro volte brevemente à forma padrão entre botões adjacentes.
- Especifique o raio de canto de um elemento não padrão que recebe o efeito lift, se sua forma não for um retângulo arredondado padrão (por exemplo, um círculo).
- Prefira efeitos de ponteiro fornecidos pelo sistema para elementos customizados que se comportam como elementos padrão.
- Use efeitos de ponteiro de forma consistente em todo o app.
- Evite criar efeitos de ponteiro e de conteúdo gratuitos, puramente decorativos.
- Mantenha formas de ponteiro customizadas simples, para que o significado seja instantaneamente compreensível.
- Considere anotações customizadas com informação útil ao segurar o ponteiro sobre um elemento (exemplo: valores X e Y em uma área de gráfico; largura e altura de uma imagem redimensionável no Keynote).
- Evite exibir texto instrucional junto ao ponteiro, o que pode fazer o app parecer complicado.
- Considere a interação entre sombra, escala e espaçamento ao definir efeitos de hover customizados; reserve escala para elementos que podem crescer sem apertar elementos vizinhos (não funciona bem, por exemplo, para uma linha de tabela); para elementos com pouco espaço ao redor, considere um efeito de hover com tinta, mas sem escala nem sombra; não use sombra sem escala, porque um elemento sem escala não parece se aproximar do observador mesmo com sombra implicando elevação.

### Especificações exatas
- Padding recomendado ao redor de elementos interativos com bezel: cerca de 12 pontos.
- Padding recomendado ao redor de elementos interativos sem bezel (incluindo símbolos): cerca de 24 pontos.

### Diferenças por plataforma
- Sem considerações adicionais para iOS; não suportado em tvOS ou watchOS.
- iPadOS: sistema de ponteiro completo com formas, efeitos de conteúdo (highlight, lift, hover), acessórios de ponteiro e magnetismo (aplicado por padrão a elementos com lift e highlight, mas não a hover; também aplicado a áreas de entrada de texto).
- macOS: ampla gama de gestos de mouse e trackpad customizáveis (clique primário, clique secundário, rolagem, smart zoom, swipe entre páginas, swipe entre apps em tela cheia, Mission Control, Lookup, tap to click, force click, zoom com pinça, rotação, Notification Center, App Exposé, Launchpad, Show Desktop); conjunto padrão de estilos de ponteiro (arrow, closed hand, contextual menu, crosshair, disappearing item, drag copy, drag link, horizontal I beam, open hand, operation not allowed, pointing hand, resize down/left/left-right/right/up/up-down, vertical I beam).
- visionOS: é possível conectar um dispositivo apontador externo ou teclado e usá-los junto com olhos e mãos; olhar para um elemento e mover o ponteiro traz o foco para o elemento sob o ponteiro automaticamente; a área para a qual a pessoa olha determina o contexto do ponteiro; com um dispositivo que suporta gestos (trackpad, mouse), o ponteiro se oculta durante o gesto, reaparecendo onde a pessoa está olhando quando movido.

### Ligações com outros artigos
Entering data, Keyboards.

<!-- visual:pointing-devices -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações (23 imagens, em aparência clara) e 9 folhas de vídeo de 6 vídeos (035 a 039 com uma folha cada, 040 com quatro) vistas, códigos conferidos.
- A abertura é uma seta de ponteiro estilo mouse em roxo escuro sobre degradê rosa e roxo, com grade tracejada e círculo concêntrico sobrepostos (img 0860).
- A área de acerto é desenhada sempre do mesmo jeito: o elemento centralizado dentro de um retângulo rosa translúcido maior, com cotas vermelhas nos quatro lados; um botão azul sólido com bezel e texto branco recebe 12 de cada lado (img 0861).
- Um símbolo pequeno de informação num círculo azul e um botão sem bezel, só com texto azul, recebem 24 nos quatro lados, o que mostra que elemento pequeno ou sem moldura ganha o dobro de margem de toque (img 0862, img 0863, comparadas a img 0861).
- A anotação customizada aparece junto a um retângulo cinza selecionado, com alças quadradas brancas nos cantos e nos pontos médios e uma alça central com setas; ao lado, uma etiqueta escura mostra largura e altura em pontos (img 0864).
- A galeria de ponteiros usa ícones pretos isolados sobre branco, sem grade nem cotas; o significado vem da forma do traço e de selos pequenos sob a seta, como círculo verde com mais, círculo cinza com X e círculo cinza translúcido com sinal de proibido (img 0865 a 0882; selos em img 0869, img 0870, img 0874).
- As formas incluem mãos em contorno preto, o punho fechado com preenchimento branco e a mão aberta e o indicador esticado em estilo luva, cursor de texto vertical feito de dois traços opostos ligados por linha fina e sua versão horizontal de chaves opostas unidas ao centro, e mira em cruz fina; os ponteiros de redimensionar formam um sistema de barra reta com uma ou duas setas saindo do centro, cobrindo as quatro direções e os dois eixos (img 0866, img 0873, img 0875, img 0872, img 0882, img 0868, img 0876 a 0881).
- Num formulário de evento do Calendar, o ponteiro vira barra vertical de texto junto aos campos URL e Notes e volta a ser um círculo cinza no espaço entre eles; o ciclo se repete duas vezes nos sete quadros (vídeo 035, folha 0001, q001 a q007).
- O destaque da aba ativa é um fundo atrás do ícone e do título: pílula clara arredondada com ícone e texto azuis no Photos, com a aba inativa esmaecida e sem fundo; caixa retangular escura atrás de "World Clock" em laranja no Clock, com "Alarm" em cinza (vídeo 036 e vídeo 039, folha 0001, q001 a q007).
- No Dock do iPadOS, o único sinal do ponteiro sob um ícone é uma mancha oval escura e translúcida junto ao ícone de Mensagens no primeiro quadro; nos demais, todos os ícones têm o mesmo tamanho, sem sombra nem elevação visível (vídeo 037, folha 0001, q001 a q007).
- Num alerta com o botão vermelho "Discard Changes", o círculo do ponteiro escurece e cresce ao se aproximar do botão e clareia e encolhe ao se afastar, em ciclo repetido, enquanto o preenchimento do botão não muda de cor (vídeo 038, folha 0001, q001 a q007).
- No visionOS, a janela do Safari flutua com moldura escura translúcida, cantos arredondados e barra de endereço central; os controles de topo (fechar, ícone do app) aparecem só quando ela ganha foco e somem quando o perde, e uma miniatura da mão no trackpad fica ancorada no canto inferior esquerdo durante toda a gravação (vídeo 040, folha 0001 q006, folha 0004 q033).
- A rolagem é contínua e granular, revelando blocos novos de cima para baixo a cada quadro, enquanto o ângulo e a posição da janela no espaço variam levemente mesmo quando o conteúdo está parado; o scroll segue funcionando com ou sem foco na moldura (vídeo 040, folha 0002 q015 a q018, folha 0003 q019 a q027, folha 0004 q034 a q036).
Divergências registradas: nos vídeos 036 e 039 o destaque fica parado na aba ativa em todos os quadros, sem o deslize entre abas que a descrição oficial narra; no vídeo 037 só o ícone de Mensagens mostra algum indício do efeito, sem Safari e Música se elevarem como diz a descrição; no vídeo 038 o que muda é o círculo do ponteiro, enquanto a descrição diz que o fundo do botão escurece; no vídeo 035 o ciclo aparece duas vezes, e a descrição fala de uma transição só. As notas atribuem parte disso à amostragem de poucos quadros, que pode não capturar transições rápidas.
<!-- /visual:pointing-devices -->

## Remotes (slug: remotes)

### O que governa
Rege o uso do Siri Remote como o principal método de entrada do Apple TV: combinação de clickpad e superfície de toque para gestos como swipe e press, navegação por foco, e botões específicos (Back, Play/Pause).

### Por que
O remote existe para que as pessoas se sintam conectadas ao conteúdo na tela mesmo à distância, do outro lado da sala. A consistência com o sistema de foco do tvOS é central: mover o foco sempre na mesma direção do gesto reforça a conexão entre a pessoa e o conteúdo que está vendo.

### Faça e evite
- Prefira usar gestos padrão para ações padrão; redefinir ou reaproveitar comportamentos padrão do remote causa confusão e complexidade, a menos que a pessoa esteja jogando ativamente.
- Seja consistente com a experiência de foco do tvOS, combinando gestos com o sistema de foco de formas familiares, como sempre mover o foco na mesma direção do gesto.
- Forneça feedback claro do que acontece quando a pessoa faz gestos no app (exemplo: apoiar levemente o polegar no remote mostra onde deslizar para baixo e revelar uma área de informações).
- Defina novos gestos só quando fizer sentido no app; dentro da jogabilidade, gestos customizados podem ser divertidos, mas fora dela as pessoas esperam gestos padrão.
- Diferencie entre press e tap, e evite responder a um tap inadvertido; press é intencional e funciona bem para escolher um botão, confirmar uma seleção ou iniciar uma ação durante o jogo; tap serve para navegação ou mostrar informação adicional, mas um tap inadvertido pode ocorrer ao apoiar o polegar, pegar, mover ou entregar o remote a outra pessoa, então evite responder a taps durante reprodução de vídeo ao vivo.
- Considere usar a posição de um tap (cima, baixo, esquerda, direita na superfície de toque) para ajudar na navegação ou jogabilidade, só quando fizer sentido e for intuitivo e descobrível.
- Em quase todos os casos, ao pressionar o botão Back, abra o pai da tela atual (no nível superior do app, a Apple TV Home Screen; dentro do app, definido pela hierarquia do app, não necessariamente a tela anterior). A exceção é durante jogabilidade ativa: responda ao Back abrindo um menu de pausa in-game, para evitar pressões acidentais repetidas que interrompam o jogo; com o menu de pausa aberto, um novo Back fecha o menu e retoma o jogo. Segurar o Back sempre vai para a Home Screen de qualquer lugar.
- Responda corretamente ao botão Play/Pause durante reprodução de mídia: ele deve reproduzir, pausar ou retomar.
- Em apps com EPG (guia eletrônico de programação), responda aos botões de navegação de EPG do remote conforme o esperado: um botão "guide" ou "browse" abre o EPG; "page up"/"page down" navegam dentro do guia; evite responder a esses botões de outra forma enquanto a pessoa navega o EPG. Durante a reprodução de conteúdo (fora do EPG), "page up"/"page down" trocam de canal. Sem suporte a EPG no app, o sistema roteia essas pressões para o app de guia padrão do dispositivo.

### Especificações exatas
Nenhum número, medida ou duração é dado no texto.

### Diferenças por plataforma
Exclusivo do tvOS (Apple TV); não suportado em iOS, iPadOS, macOS, visionOS ou watchOS.

### Ligações com outros artigos
Gestures, Focus and selection, Buttons, EPG experience, Providing Channel Navigation.

<!-- visual:remotes -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 imagem, em aparência clara), código conferido; sem vídeos.
- O esboço de abertura é um Siri Remote em roxo escuro sobre degradê de rosa para roxo, com corpo retangular vertical de cantos arredondados (img 0921).
- O desenho segue a disposição física do controle real: círculo grande no topo como superfície de toque, dois círculos pequenos lado a lado logo abaixo e, à direita desse par, uma forma alongada vertical para os botões de mídia e volume (img 0921).
- Uma grade de guias retangulares cobre toda a composição, e o círculo guia concêntrico fica centralizado no topo do controle, coincidindo com a superfície de toque circular, de modo que o elemento circular do objeto real serve de âncora para a geometria do ícone (img 0921).
- A peça repete a disciplina de grade de outras ilustrações de abertura da mesma família, como a impressora e a mão de privacidade, e a cor roxa corresponde a uma das seis cores do logo original, conforme a descrição oficial (img 0921).
<!-- /visual:remotes -->

## O que este grupo revela sobre o jeito Apple

- A privacidade é um limite estrutural, não só uma política declarada: visionOS deliberadamente não informa ao app onde a pessoa está olhando até o toque efetivo (eyes), e a Nearby Interaction usa identificadores aleatórios de duração limitada à sessão (nearby-interactions).
- Toda entrada nova é ancorada em uma expectativa física ou sistêmica preexistente antes de merecer um comportamento customizado: Apple Pencil se comporta como um instrumento de marcação real (apple-pencil-and-scribble), nearby interactions se inspiram em como a tarefa funcionaria no mundo físico (nearby-interactions), e gestos customizados só se justificam quando "não cobertos por gestos existentes" (gestures, game-controls).
- Ações potencialmente destrutivas ou irreversíveis recebem uma barreira extra de design contra o acidente: toque duplo e squeeze do Apple Pencil evitam ações destrutivas (apple-pencil-and-scribble), hover nunca deve iniciar uma ação (apple-pencil-and-scribble), e o remote do Apple TV evita responder a taps inadvertidos, sobretudo durante vídeo ao vivo (remotes).
- O sistema sempre é a fonte de verdade do comportamento padrão, e o app deve evitar competir com a orientação que o próprio sistema já oferece: Action button (action-button), atalhos de teclado padrão (keyboards), Full Keyboard Access (keyboards) e gestos padrão de trackpad no macOS (pointing-devices) seguem essa mesma régua.
- Feedback contínuo e imediato é tratado como requisito, não luxo, em qualquer entrada que dependa de proximidade, pressão ou movimento: Digital Crown (digital-crown), Camera Control (camera-control), nearby interactions (nearby-interactions) e gestos em geral (gestures) exigem resposta visível ao que a pessoa está fazendo.
- Cada plataforma tem seu próprio sistema de foco/mira coerente com seu hardware de entrada primário, e a Apple evita misturar paradigmas: foco direcional no tvOS, grupos de foco no iPadOS, hover ocular no visionOS (focus-and-selection, eyes), cada um mapeado ao dispositivo físico dominante daquela plataforma.
- Existe uma hierarquia clara de prioridade de entrada por dispositivo: no Mac, teclado e apontador são o par padrão; no iPad e no Vision Pro, o dispositivo apontador é "adicional", nunca substituindo toque, olhos ou gestos (pointing-devices); no Apple Watch, a Digital Crown é a navegação primária desde o watchOS 10, mas sempre reforçada com o toque na tela (digital-crown).
- Os alvos de toque e as regiões de interação têm valores mínimos consistentes ao redor de "dedo e conforto", não de precisão de pixel: 44x44 pt para controles virtuais de jogo frequentes e 28x28 pt para os menos importantes (game-controls), 16 pt de margem ou 60 pt entre centros para itens no visionOS (eyes), 12 pt e 24 pt de padding em torno de elementos com e sem bezel no iPadOS (pointing-devices).
- A customização é sempre balizada por moderação: atalhos de teclado customizados só para os comandos mais usados (keyboards), efeitos de hover customizados só para "momentos especiais" (eyes), key bindings de jogo com boa combinação de teclas próximas, mas sempre remapeáveis pelo jogador (game-controls).
- Text e escrita física (Scribble) recebem tratamento à parte da entrada por teclado, priorizando naturalidade sobre recursos como autocompletar, que passam a ser tratados como distrações durante a escrita à mão (apple-pencil-and-scribble).
- Symbols em vez de texto ou rótulos abstratos é um padrão recorrente para comunicar função de controle de forma universal: SF Symbols na Camera Control (camera-control) e nos controles de jogo (game-controls), símbolos de teclas modificadoras no teclado (keyboards).

## Evidência de leitura

| Arquivo | Linhas lidas | Lido até o fim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/action-button.md | 39 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/apple-pencil-and-scribble.md | 87 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/camera-control.md | 60 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/digital-crown.md | 48 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/eyes.md | 65 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/focus-and-selection.md | 69 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/game-controls.md | 86 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/gestures.md | 121 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/gyro-and-accelerometer.md | 26 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/keyboards.md | 184 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/nearby-interactions.md | 45 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/pointing-devices.md | 131 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/remotes.md | 42 | sim |

Todos os 13 artigos do grupo "Inputs" (índice 13 da lista hig) foram lidos por inteiro com a ferramenta Read, em uma única chamada por arquivo, sem truncamento reportado pela ferramenta. Nenhum artigo é apenas índice de coleção; todos têm texto próprio completo.
