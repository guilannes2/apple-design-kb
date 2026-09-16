# wwdc2020 (parte 2)

## Design for intelligence: Make friends with "The System" (id: wwdc2020_10087, 19.6 min)

Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2020/10087/.

Tese central: para que a inteligência do sistema (Siri Suggestions, widgets, Shortcuts) acelere as tarefas das pessoas, o app precisa falar a mesma língua que o sistema através de três conceitos do Intents framework: define, learn e execute.

O processo de design que a Apple descreve:
- Define: o desenvolvedor pergunta quais são as ações importantes e repetíveis que as pessoas realizam no app, e as representa como "intents", com os atributos relevantes definidos como parâmetros do intent. Exemplo dado na fala: um intent "order coffee" com parâmetros de tipo de bebida e tamanho, configurado para representar um "large iced latte".
- Learn: cada vez que alguém usa o app e realiza uma tarefa, o app faz uma "donation", um registro (snapshot) do intent executado. Essas doações alimentam a inteligência on-device, que detecta padrões de tempo e contexto (por exemplo, quando e onde a pessoa costuma pedir café) e gera previsões, como as Siri Suggestions na tela de bloqueio.
- Execute: quando uma previsão acerta e a pessoa interage com ela, o intent reconstruído volta para o app executar a ação. Há duas formas de execução: em segundo plano (sem trocar de app, podendo mostrar uma UI de confirmação dentro do próprio fluxo) ou abrindo o app diretamente na parte relevante, como a tela de confirmação do pedido.

Princípios enunciados e o porquê de cada um:
- Privacidade on-device: as doações nunca saem do dispositivo; o sistema aprende localmente. Isso permite personalização profunda sem expor dados da pessoa.
- Reduzir fricção: o objetivo da experiência inteligente é devolver tempo à pessoa, então o app deve estar pronto para executar uma ação mesmo quando não está em primeiro plano ou nem sequer está aberto.
- Meta real que a fala explicita: "surprise and delight" sem que a pessoa perceba o cálculo por trás.

Técnicas concretas de construção de interface citadas na fala:
- Shortcuts (explicado por Mert): intents de sistema já prontos para categorias gerais de ação (por exemplo, enviar mensagem) e intents customizados definidos no Xcode para ações exclusivas do app (por exemplo, "order soup"). O fluxo "Add to Siri" expõe os parâmetros do intent para a pessoa editar no momento do cadastro (trocar tomato soup por clam chowder, ou deixar o campo vazio para a Siri perguntar toda vez). Recomendação de posicionamento: oferecer o "Add to Siri" nos fluxos que as pessoas já usam (por exemplo, na tela de confirmação de pedido), nunca como interrupção tipo pop-up de newsletter. No app Shortcuts, intents de apps diferentes podem ser conectados por arrastar e soltar, passando a saída de um intent como entrada de outro.
- Widgets (explicado por Chad): os novos widgets do iOS 14 são alimentados por intents, o que permite personalização (por exemplo, o intent "show weather" tem a localização como parâmetro). Stacks (pilhas de widgets) usam a combinação de intents e donations para girar automaticamente e colocar o widget mais relevante no topo no momento certo.
- Siri Event Suggestions: o app deve doar os detalhes de uma reserva ao sistema quando a pessoa a visualiza; no iOS 14 e macOS Big Sur, essa integração também passa a acontecer via web markup em Mail e Safari.

Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina:
- Soup Chef: app de exemplo usado para ilustrar intents "order soup", "check delivery time" e "order history"; mostra como transformar uma ação de app em comando de voz via Siri.
- Charty: app de gráficos citado como consumidor do intent "order history" do Soup Chef dentro de um shortcut multi-etapas, mostrando a flexibilidade de encadear intents entre apps diferentes no app Shortcuts.
- Weather widget: exemplo de widget que sobe ao topo de um Smart Stack no momento certo, guiado por intents e donations.

Citações curtas e literais:
- "What happens on your device stays on your device."
- "It's classic 'surprise and delight.'"

<!-- visual:wwdc2020_10087 -->
# wwdc2020_10087: Design for intelligence: Make friends with "The System"

### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.

- Os três conceitos da sessão viram um sistema gráfico fixo de ícones circulares, cada um com cor e símbolo próprios (Define em magenta com lápis, Learn em verde com livro, Execute em laranja com engrenagens), e o conceito em foco aparece maior e mais saturado enquanto os outros dois encolhem e desbotam (folha 0002, q0014 e q0015, depois de a maleta de ferramentas rotulada com o framework aparecer sozinha em q0013). O trio reaparece igual em vários pontos como âncora de navegação (folha 0003, q0026; folha 0005, q0044).
- O parâmetro de um intent é desenhado como par de círculo mais rótulo, e a tela mostra a passagem do estado vazio para o preenchido: primeiro um círculo cinza só com o nome, depois dois círculos rotulados "Item" e "Size" sob o título do intent, depois os mesmos círculos em verde e dourado já com os valores escolhidos sobrepostos (folha 0003, q0022 a q0024).
- A tela de pedido usada como exemplo mostra a anatomia completa de uma confirmação de compra: moldura de iPhone com barra de status simulada em 9:41, fundo bege claro, foto do produto, linha de item, linha de gorjeta, total, botão primário laranja cheio e botão secundário só em texto (folha 0003, q0021 a q0024). A hierarquia de botões, preenchido para ação principal e texto puro para a secundária, é convenção visual que a fala não verbaliza.
- Os gatilhos de contexto aparecem como lista de onze frases curtas em duas colunas, e a filtragem é feita por opacidade: no quadro seguinte só três frases seguem em branco pleno e todas as demais ficam acinzentadas (folha 0004, q0031 para q0032). A mesma lista depois se dissolve em transição cruzada com a tela do app surgindo à direita (q0033).
- O vocabulário de diagrama mais repetido é o cartão de contexto ligado por linha fina a uma tela de iPhone: cartões laranja com dia, hora e local conectados ao pedido correspondente, e o conteúdo dos dois lados muda em conjunto entre quadros, de um pedido de café numa segunda para uma limonada numa terça (folha 0004, q0034 a q0036).
- A previsão do sistema é mostrada como notificação na tela de bloqueio, em cartão translúcido claro com ícone do app, título em negrito e linha secundária descrevendo a sugestão, sobre papel de parede em gradiente (folha 0005, q0044 e q0045).
- As duas formas de executar a ação são mostradas como duas telas comparadas lado a lado: um iPhone com o cartão de confirmação "Ready to order?" sobreposto à tela de bloqueio, com foto, resumo do pedido e par de botões cancelar e confirmar, e outro iPhone com a tela completa do app aberta (folha 0006, q0047 a q0049). A diferença entre execução em segundo plano e abertura do app fica registrada na imagem como diferença de tela, não só como explicação falada.
- A configuração de um atalho aparece como formulário de dois campos rotulados, "When I say" e "Do", com valor editável em azul e botão primário azul cheio no rodapé; entre quadros o valor do campo muda e surge um menu secundário de opções com botão de cancelar, mostrando o momento exato da edição do parâmetro (folha 0009, q0073 a q0076).
- O app Atalhos aparece em dois níveis: grade de duas colunas de cartões coloridos, quatro na grade e um quinto logo abaixo, cada um com ícone e nome; e o editor com blocos de ação empilhados verticalmente, cada bloco marcado pelo ícone do app de origem e com os parâmetros destacados em azul dentro da frase de descrição, mais um botão circular azul de adicionar ao fim da pilha (folha 0010, q0086 a q0090).
- A passagem do apresentador para a interface é feita por um recurso de montagem recorrente: uma silhueta translúcida de iPhone se sobrepõe ao corpo da pessoa em cena antes do corte para a tela (folha 0010, q0085 e q0089; folha 0012, q0104).
- A configuração de widget é mostrada como formulário seguido de lista de seleção padrão do iOS: um cartão com o campo de localização e o valor atual dá lugar à lista completa de cidades disponíveis (folha 0013, q0115 para q0116). Na mesma folha aparecem tamanhos diferentes de widget na tela inicial, do compacto ao maior que combina dois conteúdos na mesma linha (q0110, q0117).
- A rotação da pilha de widgets é explicada com o mesmo diagrama de cartões usado para o café, agora com previsões por cidade e horário: alguns cartões esmaecem enquanto os relevantes para o momento seguem em laranja pleno, e o resultado aparece como widget de clima trocando de cidade entre quadros (folha 0014, q0121 a q0125).
- A doação de uma reserva é desenhada como cartão de intent com três campos empilhados de tempo, local e número de pessoas, ligado por linha pontilhada à tela de calendário gerada, e em seguida duas telas comparadas sob os rótulos de app nativo e navegador mostrando o mesmo evento produzido pelos dois caminhos (folha 0015, q0129 a q0132).
- Nenhuma tela aparece como captura crua: toda interface é mockup em moldura de iPhone com barra de status simulada, isolada sobre fundo preto quando o ponto é explicar o componente, e mostrada em contexto de tela de bloqueio, dock ou tela inicial só quando o ponto é justamente a integração com o sistema (observação consolidada na síntese das notas).
- A produção alterna quatro apresentadores, cada um em locação própria, do estúdio interno com sofá escuro ao exterior com estrada, à área junto a um prédio curvo de vidro e a um corredor envidraçado, e cada troca de rosto e cenário antecipa visualmente a troca de subtópico (folhas 0006, 0012 e 0015, nas transições q0051 para q0052, q0102 para q0103 e q0134 para q0135).

Proporção visual: das dezessete folhas, quinze alternam apresentador e material de tela, contando a folha 0001, que soma a cartela de abertura ao apresentador; a folha 0016 é inteiramente apresentador falando, sem nenhum elemento de interface, e a folha 0017 é só a cartela de encerramento.

Divergências ou limites registrados: as notas marcam leituras parciais em dois pontos, os círculos de parâmetro registrados como cinza e sem nome completo visível (folha 0003, q0022) e o texto do campo "Do" registrado de forma aproximada (folha 0009, q0073). A identificação do prédio de vidro como arquitetura tipo Apple Park é inferência assinalada como tal nas notas (folha 0012, q0103).
<!-- /visual:wwdc2020_10087 -->

## Design for intelligence: Meet people where they are (id: wwdc2020_10200, 5.9 min)

Base: transcrição e 6 de 6 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2020/10200/.

Tese central: a inteligência do sistema pode ajudar uma pessoa mesmo antes de ela instalar um app, e continua acelerando-a em cada etapa seguinte, da descoberta ao uso avançado.

O processo de design que a Apple descreve: a fala usa uma narrativa de jornada (uma pessoa fictícia que começa a treinar em uma academia) para encadear, em sequência, os pontos de contato de inteligência do sistema:
1. Sem nenhum app de academia instalado, o Maps sugere direções de carro para o endereço da academia porque reconheceu o local mencionado em uma mensagem no Messages.
2. Na recepção da academia, uma tag NFC oferece um App Clip que mostra a grade de horários das aulas sem precisar baixar o app completo; o App Clip também oferece um caminho para baixar o app completo ali mesmo.
3. Depois de instalar o app, ao puxar a tela para baixo para abrir a Search, o app já aparece como sugestão em Siri Suggestions, porque a Siri aprendeu e previu qual app a pessoa quer abrir a partir do padrão de uso do telefone.
4. Já familiarizada com o app, a pessoa passa a usar sugestões de shortcut na Search para pular direto para a grade de horários de yoga, economizando passos.
5. Depois de perder uma aula por não notar uma mudança de horário, ela cria uma Smart Stack de widgets na Home Screen; a pilha gira automaticamente para mostrar o widget mais relevante e a tempo (por exemplo, o widget da academia quando o horário da aula muda).
6. Por fim, ela configura uma automação de Shortcuts que dispara ao chegar na academia, mostrando o horário do ônibus e iniciando o registro do treino.

Princípios enunciados e o porquê de cada um:
- A inteligência do sistema deve acompanhar a pessoa em todos os estágios de maturidade de uso, do "nunca instalei o app" ao "automatizei minha rotina com ele", entregando o touchpoint certo para cada estágio.
- O valor da inteligência não é só velocidade: é resolver um problema que a pessoa "nem sabia que tinha", como descobrir o app certo a partir de um contexto do dia a dia.

Técnicas concretas de construção de interface: App Clip acionado por tag NFC; Smart Stack de widgets com rotação automática por relevância e horário; Shortcuts automation disparada por chegada em um local (geofencing implícito na fala, sem detalhar a API).

Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina: o app fictício de academia ("Mission Gym", citado depois no vídeo id wwdc2020_10087 pelo mesmo grupo de sessões) ilustra a jornada completa; Maps, Messages, App Clip, Search/Siri Suggestions e Smart Stack de widgets aparecem como pontos de entrada sucessivos, mostrando que cada um resolve uma etapa diferente da jornada, não etapas redundantes.

Citações curtas e literais:
- "Discovering this app helped her solve a problem she didn't even know she had."

<!-- visual:wwdc2020_10200 -->
# wwdc2020_10200: Design for intelligence: Meet people where they are

### O que as imagens mostram
Base: 6 de 6 folhas de quadros vistas, todos os códigos conferidos.

- A estrutura inteira da apresentação é fixada por um gráfico próprio: uma linha do tempo horizontal com quatro círculos ligados por uma reta e um rótulo centralizado sob cada círculo, do estágio anterior ao download até o de usuário experiente, em branco sobre fundo preto (folha 0001, q0006). É recurso visual que organiza a narrativa e que a fala não descreve em detalhe.
- O ponto de entrada mais cedo da jornada é mostrado como par de telas em sequência: a conversa no Messages com o endereço e, logo depois, o mapa já com o mesmo endereço preenchido como sugestão (folha 0001, q0009 e q0010).
- A anatomia da sugestão no Maps fica visível no cartão ancorado na parte inferior da tela, com ícone do app de origem à esquerda do endereço e um rótulo secundário em cinza identificando que aquilo é sugestão da Siri (folha 0002, q0010). A imagem mostra a atribuição da origem, detalhe de composição que a fala resume apenas como sugestão.
- A tela de busca aparece com hierarquia completa: barra de pesquisa no topo, grade de ícones de apps sugeridos em três colunas e teclado ocupando a metade inferior (folha 0003, q0022). O app de academia aparece entre os ícones sugeridos dessa grade.
- A sugestão de atalho é mostrada exatamente onde se encaixa na tela: um bloco verde retangular com texto branco e ícone de seta inserido entre a grade de ícones e o teclado, em quadros que de resto mantêm a mesma composição (folha 0003, q0022 para q0026). A comparação entre os dois quadros mostra o antes e o depois da inserção, e a data exibida na grade também muda entre eles.
- A notificação aparece como cartão verde sobreposto à tela inicial com hierarquia de três níveis, título da aula e horário, parágrafo de descrição e botão de ação em verde mais escuro (folha 0004, q0032). A cor, a divisão do texto e a presença do botão embutido são detalhes que só a imagem registra.
- A troca de conteúdo genérico por conteúdo do app é mostrada como substituição na mesma posição da tela inicial: primeiro uma pilha de widgets com clima, calendário e notas, paginada por pontos, depois um widget dedicado do app de academia listando as duas próximas aulas, ocupando a largura de dois ícones (folha 0004, q0033 para q0034).
- O cartão de automação no app Atalhos mostra a composição de mais de um app numa única linha: dois ícones de app lado a lado, transporte e exercício, antes do texto do gatilho e da ação, tudo dentro de um cartão claro agrupado sob uma seção pessoal (folha 0005, q0041).
- Um pequeno retrato da apresentadora fica ancorado no canto ao lado de praticamente todo mockup de tela ao longo do vídeo (folhas 0001 a 0004), amarrando visualmente cada demonstração à jornada de uma pessoa específica em vez de apresentá-la como exemplo abstrato.
- Abertura e encerramento usam a mesma composição de adesivos na tampa do laptop, criando moldura visual idêntica no começo e no fim (folhas 0001, 0005 e 0006).

Proporção visual: o material de tela se concentra nas folhas 0001, 0003, 0004 e 0005, enquanto a folha 0002 é quase inteira a apresentadora falando, com um único elemento de interface, e a folha 0006 é só a cartela de encerramento.
<!-- /visual:wwdc2020_10200 -->

## Make your app visually accessible (id: wwdc2020_10020, 16.1 min)

Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2020/10020/.

Tese central: acessibilidade visual vai muito além do VoiceOver; como a perda de visão é um espectro amplo (visão total, parcial, baixa visão, ausência de visão, daltonismo, sensibilidade à luz, sensibilidade a movimento), o app precisa combinar cor com forma, cuidar da legibilidade do texto e respeitar as preferências de exibição que a pessoa já configurou no sistema.

O processo de design que a Apple descreve: o apresentador (Drew Haas, engenheiro do time de acessibilidade) usa como estudo de caso ao vivo um app próprio em construção, Starstruck (app de constelações), junto com um exemplo do App Store (Sneaky Sasquatch), mostrando o app antes e depois de ativar cada configuração de acessibilidade no dispositivo. A recomendação de processo explícita é pensar em acessibilidade visual desde o início do design, mas frisando que nunca é tarde para revisar.

Princípios enunciados e o porquê de cada um:
- Nunca usar só cor para indicar significado, porque para pessoas daltônicas ou com baixa visão a distinção se perde; a solução recomendada é somar forma à cor.
- Cuidar do contraste de cor porque ele pode ser a diferença entre um elemento visível e um elemento que se mistura ao fundo; regra geral dada na fala: as cores devem ficar mais escuras no Light Mode e mais claras no Dark Mode quando o contraste é aumentado.
- Não truncar texto quando o tamanho da fonte aumenta; em vez disso, quebrar a linha e usar toda a largura disponível, para que ninguém perca conteúdo.
- Respeitar, e não sobrepor, as preferências de exibição que a pessoa já ativou (Reduce Motion, Reduced Transparency, Smart Invert Colors, Bold Text, Increase Contrast), mesmo quando esses efeitos fazem parte da identidade visual do app.

Técnicas concretas de construção de interface, com números exatos quando falados:
- SF Symbols: mais de 1.500 símbolos consistentes e configuráveis, que escalam com o tamanho e o peso do texto.
- Button Shapes: nova API do iOS 14 para dar forma alternativa a botões quando essa configuração de acessibilidade está ativa; verificação via buttonShapesEnabled em UIAccessibility, com notificação para mudanças em tempo real.
- Differentiate Without Color (API do iOS 13): aplicar a ícones de status, texto com cores distintivas e qualquer elemento que hoje dependa só de cor para transmitir significado.
- Increase Contrast: usar cores de sistema, que já se adaptam automaticamente; para cores customizadas, é preciso fornecer uma aparência alternativa de alto contraste. No Accessibility Inspector do Xcode, a Color Contrast Calculator foi usada para medir o contraste entre o símbolo branco e o fundo roxo customizado do Starstruck: 4,5 para 1 (citado como a proporção mínima geralmente aceitável para a maioria dos casos) na aparência padrão, subindo para 7,5 para 1 na aparência de alto contraste, escurecendo o fundo.
- Smart Invert Colors: configurar accessibilityIgnoresInvertColors em views que não devem ser invertidas, como fotos, vídeos e ícones do app.
- Bold Text: checagem via isBoldTextEnabled em UIAccessibility; funciona automaticamente para apps que usam os estilos de fonte do sistema.
- Reduce Motion: checagem via isReduceMotionEnabled e observação da notificação de mudança; a nova API do iOS 14 para Prefer Cross-Fade Transitions (prefersCrossFadeTransitions) troca transições de slide por um crossfade mais sutil; funciona automaticamente para apps que usam UINavigationController padrão do UIKit.
- Reduced Transparency: efeitos de blur e vibrancy viram uma única cor sólida; checagem disponível via UIAccessibility para quem não usa os efeitos visuais do sistema.
- Ajuste de layout para tamanhos de fonte de acessibilidade: no exemplo do Starstruck, a stack view do símbolo e do rótulo muda do eixo horizontal com alinhamento centralizado (tamanho padrão) para o eixo vertical com alinhamento à esquerda (tamanho de acessibilidade), e o número de linhas do rótulo é sempre configurado como zero para permitir quebra ilimitada.

Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina:
- Sneaky Sasquatch (App Store): o botão "start playing" usa cor do sistema mais uma forma ao redor, mostrando como reforçar com forma o que hoje é sinalizado só por cor.
- Starstruck (app pessoal do apresentador, em construção): ícones de zodíaco com cor e símbolo distintos para daltônicos, texto em negrito opcional, blur de fundo decorativo e um efeito de parallax entre as estrelas em primeiro plano e a arte de fundo; serve de exemplo completo de como aplicar cor com forma, contraste, tipografia e respeito a Reduce Motion e Reduced Transparency no mesmo app.
- Home Screen do iOS: citada como exemplo já familiar de efeito de parallax, para ilustrar por que esse tipo de efeito pode causar enjoo em pessoas sensíveis a movimento.

Citações curtas e literais:
- "Vision loss is best described as a broad continuum."

<!-- visual:wwdc2020_10020 -->
# wwdc2020_10020: Make your app visually accessible

### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.

- A tese do espectro de perda de visão é demonstrada, não afirmada: quatro colunas lado a lado com a mesma fotografia de praia e penhasco tratada com filtros progressivos, da imagem nítida à totalmente escura, cada coluna com seu rótulo (folha 0001, q0009). No quadro seguinte a coluna sem visão ganha uma borda branca fina que enquadra um retângulo vazio, destaque feito só com contorno porque não há conteúdo a realçar (folha 0002, q0010).
- Os cards de anúncio de API seguem um template fixo repetido a cada recurso novo: título grande em negrito, selo circular verde de novidade no canto superior direito quando a API é nova do ano, até três frases curtas de recomendação e um bloco de código monoespaçado com destaque de sintaxe por cor logo abaixo (folhas 0004 q0036, 0005 q0039, 0009, 0010, 0013, 0015 e 0016). A imagem carrega a assinatura exata de cada API, que a fala só descreve por comportamento.
- O exemplo de botão bem resolvido aparece como tela real de produto da App Store, com botão pill azul sólido como chamada primária e metadados dispostos em três colunas com ícone pequeno acima de cada rótulo (folha 0004, q0028 a q0030 e q0034).
- A recomendação de reforçar significado com símbolo é sustentada por dois materiais distintos: uma grade densa de símbolos em preto e branco organizada em linhas por tema, todos com o mesmo peso de traço e alinhamento regular, e uma prancha de teste tipográfico em fundo branco com uma letra de referência à esquerda e o mesmo símbolo repetido em três tamanhos crescentes por linha (folha 0005, q0042 e q0045). A prancha é método de verificação de escala que a fala não descreve com esse detalhe.
- O par antes e depois central do vídeo é a lista de signos do app de exemplo: primeiro apenas nomes em texto colorido sobre fundo preto, com chevron de navegação à direita, depois a mesma lista com um ícone circular colorido acrescentado à esquerda de cada nome, mantendo a cor e somando a forma (folha 0006, q0050 para q0053).
- As ferramentas de desenvolvedor aparecem como capturas reais, nunca como ilustração: o Asset Catalog do Xcode com barra lateral, preview central e painel de atributos à direita evolui de uma variante única do símbolo para duas variantes empilhadas de contraste normal e alto no mesmo slot (folha 0008, q0070 a q0072), e depois para quatro variantes combinando luminosidade e nível de contraste, cada uma com seu tom de roxo (folha 0009, q0081).
- A medição de contraste aparece com números na tela: uma janela de calculadora em estilo macOS com swatch de texto e de fundo, valores RGB abaixo de cada swatch, controle de tamanho de texto e um resultado grande de 4,5 para 1 acompanhado de selo triangular amarelo de aviso informando quais tamanhos e pesos aquela razão atende (folha 0009, q0074 e q0075).
- As preferências do sistema são mostradas nas telas reais de ajuste do iOS, com alternador verde padrão ligado e controle deslizante de tamanho de texto com a letra pequena em uma extremidade e a grande na outra (folha 0011, q0091 para q0092), e depois a lista raiz de Ajustes com os ícones quadrados coloridos de cada seção (folha 0014 e, já na mão de uma pessoa, folha 0016, q0142).
- A frase de destaque sobre legibilidade usa hierarquia por peso dentro da própria sentença: as palavras que importam em branco e negrito, o restante da frase em cinza regular (folha 0011, q0093).
- O código recebe realce parcial como recurso didático, com um retângulo cinza claro cobrindo só o trecho em discussão, e o realce se move entre quadros do bloco de fonte padrão para o bloco de tamanho de acessibilidade (folha 0012, q0100 a q0103). A tela do telefone muda junto: a célula deixa de ter símbolo e nome lado a lado, centralizados, e passa a empilhar o símbolo acima do nome, alinhado à esquerda, com bem menos itens visíveis por tela.
- A tela de detalhe do app mostra outro padrão de leitura: pares rótulo e valor em coluna, rótulo pequeno em cinza acima do valor maior em branco, com espaçamento generoso entre grupos e cabeçalho de seção em caixa alta (folha 0012, q0108).
- O efeito de movimento é demonstrado fisicamente: a tela do mapa estelar aparece sendo segurada e inclinada na mão de uma pessoa (folha 0013, q0114 a q0116). Em seguida um painel de ajustes com alternadores verdes é sobreposto à esquerda da mesma tela, mostrando a configuração e o app afetado no mesmo quadro (folha 0014, q0119 para q0120).
- O progresso da palestra é rastreável por uma tela de índice recorrente sempre na mesma posição vertical, com o tópico ativo em branco e os demais em cinza (folhas 0002, 0003 q0019, 0010 q0090, 0011 e 0013); ao fim da seção de cor e formas aparece ainda um card de resumo com selo circular verde de verificação (folha 0010, q0086).
- Um card da série quebra o próprio template: a tela de transparência reduzida aparece primeiro só com texto, sem bloco de código, ao contrário dos outros cards da série, e só depois surge a versão com código (folha 0015, q0132; folha 0016, q0137).

Proporção visual: a maior parte das folhas alterna o apresentador com material de tela, e há três tipos distintos de material (cards de API com código, capturas de ferramentas do Xcode e telas de iPhone do app de exemplo); as folhas 0003 e 0007 são quase só o apresentador falando, com variação apenas de enquadramento, e a folha 0017 é a vinheta final.

Divergências ou limites registrados: as notas assinalam quadros repetidos sem alteração perceptível entre si (folha 0009, q0074 e q0075; folha 0015, q0128 e q0129) e um passo do realce de código em que o destaque permanece na mesma condição em vez de avançar (folha 0012, q0100 para q0101). A identificação da fachada curva como Apple Park é registrada como provável, não confirmada (folha 0002). O app de exemplo aparece na tela com o nome "Constellations", enquanto as notas o tratam como o mesmo app fictício citado na fala por outro nome.
<!-- /visual:wwdc2020_10020 -->

## Design for intelligence: Discover new opportunities (id: wwdc2020_10088, 5.2 min)

Base: transcrição e 5 de 5 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2020/10088/.

Tese central: a inteligência do sistema é uma colaboração entre o sistema operacional e os apps, viabilizada em grande parte pela extensibilidade, e participar dela abre para o app pontos de entrada muito além da tela inicial.

O processo de design que a Apple descreve: JP Lacerda define intelligence como fazer os produtos Apple parecerem que "conhecem" a pessoa (seus objetivos, hábitos, preferências, interesses e relacionamentos) para dois efeitos: "achieve more" (acelerar a pessoa a um objetivo que ela já tem em mente) e "discover more" (enriquecer a vida da pessoa com conteúdo, pessoas, lugares e apps relevantes entregues no momento certo). A partir dessa definição, a fala percorre os principais entry points do sistema onde um app pode aparecer: Shortcuts (voz, Siri Suggestions widget, Search, tela de bloqueio, Smart Stack), Sharing Suggestions, Siri Event Suggestions (reservas levadas automaticamente ao Calendar), Siri Suggestions no Maps, sugestão proativa de Do Not Disturb e sugestão de check-in de voo na tela de bloqueio. Ao final, orienta o desenvolvedor a escolher quais entry points fazem sentido para as ações do próprio app e a pensar em como medir esse impacto.

Princípios enunciados e o porquê de cada um:
- Privacidade como direito humano fundamental: analytics de uso só são coletados com opt-in explícito e não identificam a pessoa, o que permite medir impacto sem comprometer a confiança.
- Menos tédio (menos toques e cliques) e menos distração (foco no que importa) são os dois efeitos que a inteligência deve produzir para justificar cada novo entry point.

Técnicas concretas de construção de interface, com números exatos quando falados:
- Quando alguém interage pela primeira vez com uma Sharing Suggestion do app, em média passa a compartilhar o dobro do que compartilhava antes por aquele app; esse padrão foi observado em vários apps que adotaram Sharing Suggestions.
- Algumas companhias aéreas relataram que 82% dos check-ins feitos a partir de notificação vieram da ação de Siri Event Suggestion.
- Apps de terceiros são vistos, em média, cinco vezes por dia entre tela de bloqueio, Sharing, Search e outros entry points do sistema.

Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina:
- Weather widget subindo ao topo de um Smart Stack no momento certo, mostrando a mecânica de priorização automática por relevância.
- Siri Event Suggestions levando uma reserva de restaurante automaticamente para o Calendar, e depois avisando na tela de bloqueio a hora de sair com base no trânsito, ilustrando como uma única doação de dado gera múltiplos momentos de valor.
- Sugestão de Do Not Disturb antes de assistir a um filme e sugestão de check-in de voo na tela de bloqueio, mostrando entry points que antecipam a necessidade da pessoa sem que ela precise abrir nenhum app.

Citações curtas e literais:
- "The goal of intelligence is to make your Apple products feel like they know you."

<!-- visual:wwdc2020_10088 -->
# wwdc2020_10088: Design for intelligence: Discover new opportunities

### O que as imagens mostram
Base: 5 de 5 folhas de quadros vistas, todos os códigos conferidos.

- Os conceitos-chave aparecem como palavras curtas sobrepostas ao vídeo do apresentador, em branco sem serifa e alinhadas à direita, uma de cada vez conforme a fala avança (folha 0001, q0009; folha 0002, q0010 e q0011). A tela funciona como legenda de ênfase, sem slide separado.
- O conceito de múltiplos pontos de entrada ganha um diagrama abstrato antes de qualquer exemplo concreto: uma barra verde rotulada com uma ação do app, junto ao rótulo do app, ligada por linha vertical fina a uma barra azul-escura rotulada com o sistema; no quadro seguinte a barra verde única se desdobra em três barras de ações distintas, todas ligadas à mesma barra do sistema (folha 0002, q0013 para q0014). É camada de explicação mais abstrata do que a fala oferece.
- A tela do app Atalhos aparece com a mesma grade de quatro cartões coloridos usada em outro vídeo da mesma trilha (folha 0002, q0017 e q0018), evidência visual de material e exemplos reaproveitados entre sessões, não apenas de discurso semelhante.
- A relação entre configurar e colher o resultado é mostrada como comparação de duas telas lado a lado: um iPhone com a tela de configuração do atalho, com os campos de frase e de ação, e outro com as sugestões já aparecendo no sistema (folha 0003, q0019 para q0020).
- O menu de compartilhamento aparece com sua anatomia padrão, avatares circulares de contatos sugeridos numa fileira acima da fileira de ícones de canal, e o mesmo componente é mostrado duas vezes em contextos diferentes, ancorado a uma tela de fotos num iPhone e depois a uma janela de calendário num laptop (folha 0003, q0022 para q0023). A repetição do mesmo componente em dois aparelhos é ponto que só a imagem estabelece.
- As notificações de sugestão na tela de bloqueio aparecem em cartão translúcido claro com ícone, título em negrito e texto secundário, incluindo o horário exibido na tela junto ao aviso (folha 0003, q0024).
- A variedade de contextos de sugestão é resolvida por um recurso visual próprio deste vídeo: várias telas de bloqueio sobrepostas em leque, como cartas empilhadas, ganhando uma nova notificação a cada quadro, de trânsito a supressão de interrupções e check-in de voo (folha 0003, q0025 a q0027). Mostra o acúmulo de casos sem precisar de telas separadas.
- Os dados de impacto viram cartelas com padrão fixo: número grande em negrito branco, muito maior que o texto de apoio, com uma legenda curta centralizada abaixo, sempre sobre a mesma fotografia desfocada de lago e árvores; entre quadros troca só o número e a legenda (folha 0004, q0031 a q0033).
- O fechamento é uma lista de três recomendações em texto alinhado à direita sobreposto ao vídeo do apresentador, cada linha como item independente e sem marcadores (folha 0004, q0036), mantendo o mesmo tratamento tipográfico das palavras-chave do início.
- Toda tela de app ou de sistema aparece dentro de moldura simulada de iPhone ou de laptop, nunca como captura solta, mesmo quando o conteúdo mostrado é apenas um menu ou uma notificação (observação consolidada na síntese das notas).
- Abertura e encerramento repetem a mesma cartela padrão da trilha, com o wordmark do evento, o laptop fechado e os adesivos em close (folhas 0001 e 0005).

Proporção visual: a folha 0003 é inteiramente material de tela, sem o apresentador em quadro; as folhas 0001, 0002 e 0004 alternam o apresentador com textos sobrepostos, diagrama e cartelas de dado; a folha 0005 mostra o apresentador em dois quadros e depois a cartela de encerramento.

Divergências ou limites registrados: as notas listam o quadro q0013 nas duas descrições da folha 0002, entre os quadros do apresentador e entre os do diagrama, registrando-o como parcial.
<!-- /visual:wwdc2020_10088 -->

## Adopt the new look of macOS (id: wwdc2020_10104, 28.7 min)

Base: transcrição e 21 de 21 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2020/10104/. Observação: a duração de 2,8 min consta no cabeçalho do arquivo, mas o texto da transcrição é extenso; reporto a duração exatamente como está registrada na fonte, sem corrigi-la por inferência.

Tese central: o novo visual do macOS Big Sur, sidebars full-height, toolbars redesenhadas e SF Symbols no Mac, chega automaticamente para a maioria dos apps que compilam contra o novo SDK, mas uma camada extra de adoção intencional permite ir além do que vem de graça.

O processo de design que a Apple descreve: a sessão é dividida por dois engenheiros de AppKit em três blocos sequenciais. John Tegtmeyer cobre a estrutura da janela (sidebar e toolbar); Jeff Nadeau cobre os controles e, por fim, a iconografia com symbol images. Em cada bloco, o padrão de explicação é o mesmo: primeiro o que o framework já entrega sem nenhuma mudança de código, depois o que exige adoção manual para ganhos extras.

Princípios enunciados e o porquê de cada um:
- Deixar o framework fazer o trabalho pesado sempre que possível, porque isso garante consistência visual com o resto do sistema sem custo de engenharia.
- Oferecer pontos de adoção incremental (sidebar full-height, tracking separators, accent color customizado) para quem quer expressar mais personalidade ou dar mais contexto visual sem reescrever a estrutura do app.

Técnicas concretas de construção de interface, com números exatos quando falados:
- Sidebar full-height: obtida usando NSSplitViewController com o SplitViewItem configurado com sidebar behavior, mais a fullSizeContentView window mask; NSView passou a expor safe areas para isso, inclusive no Interface Builder.
- Cor dos ícones da sidebar: NSTintConfiguration com quatro modos, default (usa a accent color), monochrome (aparência sem cor, como no Catalina), preferredColor (uma cor específica que volta a seguir a accent color se ela for customizada, exemplo dado: as pastas do Mail em teal) e fixedColor (uma cor que nunca muda, exemplo dado: a pasta VIP do Mail, sempre uma estrela amarela).
- Estilos de toolbar via NSWindow.toolbarStyle: unified (novo padrão, controles maiores, ícones em negrito, inline title junto à sidebar), unified compact (layout mais comprimido, controles de tamanho regular, com inline title opcional), preference (voltado à janela de preferências, aplicado automaticamente ao usar NSTabViewController com toolbar TabStyle), expanded (título acima da toolbar, indicado para títulos longos ou toolbar muito povoada) e automatic (valor padrão, mantém o layout de apps já existentes).
- Large control size: nova opção de tamanho grande disponível para botões (inclusive pop-up e pull-down), segmented controls, text fields e search fields; é o tamanho usado por padrão em todos os itens do novo estilo de toolbar unified e nos botões de alertas do sistema.
- Subtitle property em NSWindow: texto secundário sob o título no estilo unified (exemplo dado: contagem de mensagens não lidas no Mail) ou ao lado do título no estilo expanded.
- NSSearchToolbarItem: campo de busca colapsa em botão quando a janela é comprimida e se expande de volta ao clicar; adoção descrita em dois passos, trocar a classe do item para NSSearchToolbarItem e usar a propriedade searchField em vez de view; mantém compatibilidade retroativa em sistemas mais antigos sem checagem de versão manual.
- NSTrackingSeparatorToolbarItem: alinha itens da toolbar aos divisores de um split view, criando seções full-height que acompanham o redimensionamento; a criação de cada item leva uma linha de código, associando o item a um split view e ao divisor que ele deve acompanhar.
- Sombra automática entre a toolbar e conteúdo com scroll (scroll shadow), substituível por um separador explícito ou por nenhum separador via titlebarSeparatorStyle, configurável por seção do split view ou pela janela como um todo.
- Sliders: novo estilo com as marcações (tick marks) posicionadas dentro da track; recomendação de alinhar o rótulo adjacente pelo baseline do slider, técnica que também funciona no Catalina.
- NSTableView.style: quatro opções, automatic (padrão, escolhe com base no contexto da tabela), fullWidth (seleção de borda a borda, como no Catalina), inset (novo estilo, com padding horizontal extra nas células, padding vertical extra no topo e na base, altura de linha maior e espaçamento maior em tabelas multicoluna) e sourceList (voltado à aparência de sidebars).
- Tipografia: text styles chegam ao macOS, com tamanhos e pesos centrados no tamanho de corpo padrão de 13 pontos; acessados via preferredFont(forTextStyle:) ou preferredFontDescriptor(forTextStyle:); a fala frisa que isso não é o mesmo que dynamic type, não existe um slider que ajuste esses tamanhos em todo o sistema.
- SF Symbols no Mac: mais de 2.500 símbolos embutidos, mais a opção de desenhar símbolos próprios. Exemplo com números exatos: os ícones grandes da toolbar unified são symbol images configurados em tamanho de 13 pontos, peso medium, usando a large symbol scale. Uso recomendado via NSImageView (resolve baseline, display scale e outras propriedades de alinhamento automaticamente); a fala recomenda evitar usar NSImage direto em layer contents, porque a imagem perde a sensibilidade ao contexto e o resultado tende a sair borrado.
- Accent color customizado: qualquer cor pode virar a accent color do app, definida como named color no asset catalog e aplicada quando a preferência do sistema está em "multicolor"; a recomendação é continuar desenhando com as named system colors (não a cor customizada em código direto) para respeitar a preferência da pessoa quando ela escolhe outra accent color do sistema.

Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina:
- Mail: usado como referência recorrente, mostra a sidebar full-height com ícones coloridos, as pastas em teal com preferredColor, a pasta VIP em amarelo fixo com fixedColor, a contagem de não lidos como subtitle sob o título, e as seções full-height da toolbar alinhadas aos divisores do split view via NSTrackingSeparatorToolbarItem.

Citações curtas e literais:
- "Your native Mac app will look great on macOS Big Sur out of the box."
- "The idea behind large controls is that sometimes you just need a bigger button."

<!-- visual:wwdc2020_10104 -->
### O que as imagens mostram
Base: 21 de 21 folhas de quadros vistas, todos os códigos conferidos.

- Medida anotada diretamente sobre o componente: duas barras de ferramentas são exibidas empilhadas e comparadas, cada uma com um número à esquerda indicando sua altura, 52 para o estilo unified e 38 para o compacto, com ícones e o botão de mover visivelmente maiores na primeira (folha 0008, q0065 e q0066). A tela dá o valor exato que a fala trata só como "controles maiores".
- Etiqueta amarela com seta apontando um único ícone da barra de ferramentas do Mail, com a especificação completa daquele símbolo em texto, tamanho em pontos, peso e escala (folha 0018, q0155 e q0156). A anotação surge entre q0154 e q0155, ou seja, o slide primeiro mostra o ícone e só depois o rotula.
- Anatomia geométrica de um símbolo exposta por duas caixas sobrepostas ao mesmo ícone de balão de diálogo, uma amarela cobrindo toda a área da imagem e outra azul menor dentro dela, separando o retângulo total do retângulo de alinhamento (folha 0020, q0172). O par de anotações chega em dois tempos, a primeira sozinha em q0171.
- Linha fina amarela atravessando toda a largura do quadro na altura do rótulo ao lado do slider, funcionando como guia de alinhamento de linha de base entre texto e controle (folha 0015, q0131). Nos quadros anteriores o mesmo slider aparece sem a guia, com o indicador mudando de formato de gota para círculo e ganhando marcações no trilho (q0129 a q0130).
- Escala tipográfica apresentada em duas colunas, com cada nome de estilo renderizado no próprio tamanho e peso que representa, e um segundo passo em que etiquetas amarelas acrescentam o tamanho em pontos de cada linha, da maior de 26 pontos até as legendas de 10 pontos (folha 0017, q0145 para q0146). A hierarquia é demonstrada pelo próprio desenho do slide antes de ser dita em número.
- Gabarito de slide técnico repetido em quase todo o vídeo: título grande fixo no topo, lista curta de condições de uso, bloco de código monoespaçado com sintaxe colorida de um lado e captura ou mockup do outro (folhas 0003, 0004, 0006 a 0009 e 0013 a 0020). A tela fixa a ordem de leitura e mostra o código literal que a fala apenas resume.
- Construção incremental dentro do mesmo slide, em vez de troca de composição a cada frase: o bloco de código cresce de uma para duas e depois quatro linhas mantendo a mesma captura ao lado (folha 0003, q0019 a q0021), e o tópico anterior é esmaecido e deslocado quando o seguinte entra (folha 0013, q0109 a q0111).
- Marcação de prática desaconselhada com um X vermelho circular no canto do slide, sem contraparte de exemplo correto ao lado: no slide das propriedades de tamanho mínimo e máximo do item de barra de ferramentas (folha 0008, q0066 a q0069) e no bloco de código que atribui a imagem direto ao conteúdo da camada, cujo comentário na própria tela avisa que o símbolo tende a sair borrado ou distorcido (folha 0020, q0173 a q0175).
- Comparações lado a lado como recurso didático recorrente: três janelas do Mail com o mesmo layout e escalas crescentes de texto e ícone nos tamanhos de sidebar (folha 0018, q0157 e q0158), dois sliders com e sem marcações (folha 0015, q0128) e as duas alturas de barra de ferramentas já citadas.
- Diagramas de caixa traduzindo relação de código em desenho: a hierarquia de um controlador de janela ligando a um controlador de split view e a dois controladores de view (folha 0003, q0026 e q0027), e um retângulo verde externo com outro interno mais claro e setas duplas nas quatro bordas, mostrando que o scroll view precisa preencher o item inteiro (folha 0011, q0098).
- Tabela de decisão de três colunas mapeando contexto para valor de estilo de tabela, com os cabeçalhos de situação em cima e o valor de código embaixo de cada um, em formato de referência rápida (folha 0016, q0140 e q0141). Duas linhas de ressalva aparecem só no quadro seguinte (q0141).
- Ferramentas reais na tela, não apenas mockup: o Interface Builder com painel de hierarquia, canvas e o inspetor de tamanho com o checkbox de safe area marcado (folha 0003, q0022 a q0027), o catálogo de objetos com os itens de busca arrastáveis (folha 0010, q0082 a q0084) e o catálogo de assets do Xcode com o quadrado de cor de destaque e a janela de opções do compilador (folha 0013, q0112 e q0113).
- Cor e materiais: fileira horizontal de círculos de cor de destaque com espaçamento uniforme (folha 0012, q0107 e q0108), à qual se acrescenta um círculo multicolorido na frente dos tons sólidos para representar a opção de cor livre (folha 0013, q0109). Nas capturas da sidebar do Mail, uma folha registra ícones coloridos por seção, com estrela amarela nos favoritos e pastas em teal (folha 0002, q0017), e outra registra os itens sobre fundo escuro rosado com o selecionado em azul (folha 0004, q0033 e q0036).
- Componentes isolados sobre fundo preto, sem texto em volta, para leitura de anatomia: botão pop-up com preenchimento azul, slider com trilho azul antes do indicador e cinza depois, e controle segmentado com o segmento ativo em branco sobre cinza escuro (folha 0012, q0105 e q0106). No bloco de controles grandes as composições são sucessivas, não simultâneas: primeiro um mockup de onboarding com botão vermelho de ação centralizado (folha 0014, q0120 a q0122) e depois o painel com os seis tipos de controle empilhados com espaçamento generoso (q0123 e q0124).
- Diferença entre quadros mostrando estado de um mesmo componente: o campo de busca aparece colapsado como ícone de lupa e depois expandido em caixa de texto com borda azul de foco (folha 0009, q0075 a q0077); um retângulo de destaque contorna um grupo de botões da barra de ferramentas, leitura que as notas registram como sugestão da área de clique de um controle sem borda visível (folha 0007, q0062 e q0063), e outro contorna a divisória entre sidebar e lista, subindo até o topo da janela (folha 0010, q0087 e q0088).

Proporção visual: das 21 folhas, quase todas são slides com código, mockup ou captura de tela, com o apresentador entrando em cortes curtos entre blocos; a abertura e o fechamento são cartões de marca da WWDC, com adesivos, logotipo e MacBook, e neles o apresentador aparece em janela de vídeo no canto ou em corte curto, não sozinho no quadro inteiro (folhas 0001 e 0021). As notas não registram nenhuma demonstração ao vivo, todo app aparece como captura estática, quase sempre o mesmo Mail usado como estudo de caso único.

Divergências ou limites registrados: as notas marcam leituras incertas em três pontos, a comparação de duas versões do campo de busca é descrita como "provavelmente antes e depois" (folha 0009, q0075 para q0076), o painel do catálogo que escurece é lido como provável transição de saída (folha 0010, q0083 para q0084), e o ícone de balão que abre a seção de símbolos é interpretado como exemplo genérico de contexto de app de mensagens (folha 0019, q0164 para q0165). Vários pares de quadros são registrados como sem mudança perceptível de conteúdo (folhas 0002, 0004, 0005, 0010, 0011, 0012 e 0017).
<!-- /visual:wwdc2020_10104 -->

## The winners of the 2020 Apple Design Awards (id: wwdc2020_20022, 2.8 min)

Base: transcrição e 8 de 8 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/wwdc2020/20022/.

Tese central: A Apple homenageia desenvolvedores todo ano com o Apple Design Award e, em 2020, sem poder fazer isso presencialmente, anunciou os vencedores de forma pessoal, em chamadas surpresa. Desenvolvedores descrevem seus apps, e as falas finais tratam de fazer as coisas com muito amor, de seguir aprendendo e de convencer outras pessoas do valor do que se faz quando ainda não está bonito.

O processo de design que a Apple descreve: A fala não descreve um processo de design estruturado; a transcrição traz trechos curtos e soltos das chamadas de anúncio. O que aparece sobre o fazer, na ordem em que é falado:
1. Ajuste fino: um trecho solto diz algo como um pouco menos aqui e um pouco mais aqui, sem indicar a que se refere nem quem fala.
2. Aprendizado contínuo: uma fala diz que todos ainda estão aprendendo e perseguem um ideal que nunca pode ser alcançado.
3. Esforço: todos trabalham muito só para fazer coisas bonitas passarem a existir.
4. Fase inicial: a coisa precisa chegar ao mundo, mas é preciso convencer muitas outras pessoas de que terá valor, sobretudo no começo, quando ainda não está bonita, mas vai ficar.

Princípios enunciados e o porquê:
1. Contar uma história ancorada e pessoal. Porquê: é a resposta dada à pergunta sobre o que torna Where Cards Fall único.
2. Evocar o lado luminoso da humanidade, com um jogo abstrato que fica mais compreensível com o tempo. É o objetivo declarado do Sky; a fala não dá razão além do próprio objetivo.
3. Ter um elenco inclusivo. Porquê: para que parecesse convidativo a mais pessoas. A frase vem logo depois da fala sobre o Sky, e a transcrição não indica quem a diz nem de qual app se trata.
4. Manter o objetivo simples: tornar extremamente fácil escrever notação musical. O nome desse app não é dito na fala.
5. Fazer o fotógrafo esquecer a ferramenta. Porquê: no Darkroom, a intenção é que a pessoa esqueça que está num app editando fotos e pense só nas histórias que quer contar.
6. Mirar uma ferramenta icônica. O Shaper 3D quer criar uma ferramenta de design que defina o futuro do design 3D; a frase sai truncada e repetida na transcrição ("for the next", depois "for the next two years"), e o trecho sobre dois anos pode pertencer à frase seguinte, então o prazo não é certo.
7. Os premiados como base para os outros. Porquê: segundo a fala após o anúncio, passam a ser aqueles em cujos ombros outros desenvolvedores podem se apoiar para construir a próxima geração de apps.
8. Fazer com muito amor. Porquê: a conexão entre quem faz e a coisa feita volta a acender quando as pessoas a experimentam.
9. Pôr o coração no que se faz, transcrito como "boil your heart and sow into something" (termo incerto na transcrição automática). Porquê: assim a coisa será excepcional, transcrito como "exception" (termo incerto na transcrição automática).
10. Seguir aprendendo. A mesma fala acrescenta, sem ligar como causa, que todos perseguem um ideal que nunca pode ser alcançado.
11. Convencer outras pessoas do valor do que se faz, sobretudo no começo. Porquê: a coisa precisa chegar ao mundo, e no começo ainda não está bonita, mas vai ficar.

Técnicas concretas de construção de interface, com números exatos quando falados: A fala não traz técnica de construção de interface nem valores de layout, tipografia, cor, materiais, componentes ou interação. O único trecho próximo de ajuste é o fragmento sobre um pouco menos aqui e um pouco mais aqui, sem objeto nem contexto.

Exemplos citados:
1. O prêmio em si: entregue todo ano na conferência, transcrita como "wwc" (termo incerto na transcrição automática); em 2020, sem poder ser presencial, foi feito de forma pessoal por chamadas.
2. O formato do anúncio: a chamada começa como conversa sobre o app com "lauren grim" (termo incerto na transcrição automática), apresentada como design evangelist da Apple; no meio, alguém diz ter recebido mensagem e pede para mesclar outra pessoa na chamada; entra "john galenzi" (termo incerto na transcrição automática), que diz já ter encontrado o desenvolvedor algumas vezes, e é anunciado o prêmio. Também são cumprimentados "match", "simon" e "sam" (termos incertos na transcrição automática).
3. Where Cards Fall: história muito ancorada e pessoal.
4. Sky: jogo abstrato sobre o lado luminoso da humanidade, que vai ficando mais compreensível com o tempo.
5. "loom" (termo incerto na transcrição automática): descrito como uma abordagem lúdica de um instrumento para criar "drone animation" (termo incerto na transcrição automática).
6. Um app de notação musical, sem nome na fala, cujo objetivo era tornar a escrita de partitura extremamente fácil.
7. Darkroom: edição de fotos em que o fotógrafo deveria esquecer o app e pensar nas histórias.
8. Shaper 3D: ferramenta de design 3D com ambição de ser icônica e definir o futuro da área.
9. A reação de um vencedor: perguntado como se sente, diz que aquilo o inspirou a fazer ainda mais.

Citações:
1. "we're all in pursuit of an ideal that can never be achieved"

<!-- visual:wwdc2020_20022 -->
### O que as imagens mostram
Base: 8 de 8 folhas de quadros vistas, todos os códigos conferidos.

- Abertura tratada como cartão de identidade visual, com adesivos, logotipo da Apple, o texto do ano e um cubo com o nome do prêmio dispostos livremente sobre fundo em degradê, seguida da paisagem do campus exibida na tela de um MacBook e de cortes internos do prédio, vidro curvo, corredores envidraçados e ambientes de trabalho (folha 0001, q0001 a q0006). Entre q0001 e q0002 os próprios elementos gráficos se reposicionam na tela.
- A interface que estrutura o vídeo inteiro é a grade de chamada de vídeo, com legenda em texto branco no canto inferior esquerdo de cada participante indicando cidade e país (folhas 0001 e 0002, q0007 em diante). As localizações aparecem só na tela, Los Angeles, Santa Monica, Tel Aviv, Budapeste e Londres.
- Corte direto entre pessoa e produto, sem transição gradual, amarrando cada app ao momento em que é citado: da chamada para a cena isométrica de jogo (folha 0002, q0015 para q0016), dela para o logotipo do jogo em tela preta (q0016 para q0017) e desse para uma arte conceitual pintada (q0017 para q0018).
- Processo de criação de personagem documentado em duas etapas na mesma folha, esboços a lápis com anotações técnicas de figurino escritas ao lado dos bonecos, e depois a ilustração acabada e colorida com trajes estilizados (folha 0003, q0024 para q0025). É a única sequência de processo de design visível no vídeo.
- Identidade tipográfica de cada produto mostrada isoladamente: logotipo em letra desenhada à mão, branca sobre preto, para um dos jogos (folha 0002, q0017), wordmark cursivo translúcido sobre cenário tridimensional para outro (folha 0003, q0020) e uma tela de abertura minimalista com um único elemento gráfico central e a palavra de início em letras espaçadas (folha 0003, q0021).
- Paleta e material como argumento de cena: interior iluminado por luz dourada vinda de uma porta contra ambiente escuro, com a silhueta centralizada no vão (folha 0002, q0016), contrastando com a arte conceitual pintada em aquarela digital de paleta fria, azul e turquesa, de uma formação rochosa em forma de mãos (q0018).
- Anatomia de painel de ajuste no app de edição de fotos, lista vertical de rótulos com sliders horizontais, dez parâmetros nomeados na tela; o quadro anterior traz o mesmo app na tela de galeria, com grade de miniaturas de filtro ao lado da foto (folha 0008, q0064 para q0065). São duas telas em sequência, não uma composição única, e os nomes exatos dos controles existem só na imagem.
- Anatomia do app de partituras em três telas distintas: biblioteca em grade escura de miniaturas com menu de contexto lateral de cinco ações (folha 0004, q0030), tela de notação com nomes de instrumento alinhados à esquerda da pauta (q0031) e tela inicial em formato de painel, com saudação personalizada pelo nome, grade de documentos recentes e cinco abas de navegação no topo (folha 0008, q0070).
- Anatomia de modelagem tridimensional em duas telas separadas: menu lateral de ferramentas com ícone mais texto em cinco itens e informação técnica no rodapé, contagem de corpos selecionados e volume (folha 0008, q0069); e, num tablet, painel vertical de ícones pequenos à esquerda e menu inferior com abas, com o objeto renderizado sobre fundo branco (folha 0005, q0038). As notas não amarram as duas telas ao mesmo app pela imagem, o nome vem da fala.
- O oposto disso no app de desenho, interface quase ausente, tela cheia na cor verde água com poucos ícones nos cantos e nenhum controle visível, deixando o quadro inteiro para o gesto com a caneta (folha 0007, q0058 a q0060). Nesses três quadros a figura desenhada evolui de dois ovais conectados para uma forma maior acrescentada acima e depois para uma figura definida com cabeça e corpo.
- Ponte entre projeto digital e peça física mostrada em três quadros seguidos, manipulação do modelo no tablet, máquina de corte a laser em operação com faíscas, e mãos segurando as peças brancas resultantes (folha 0005, q0038 a q0040). A fala trata da ambição da ferramenta, a imagem mostra a peça saindo dela.
- Enquadramento recorrente com mãos e dispositivo físico dentro do quadro, em vez de captura pura de tela, usado nos três apps de criação (folhas 0004, 0005 e 0007).
- Reação emocional filmada na própria grade de chamada, alguém apontando o celular para a tela como quem fotografa, outro com a mão no rosto rindo, e a moldura mudando de dois participantes para um em destaque e de volta (folha 0006, q0047 a q0054). Que esse seja o momento do anúncio do prêmio é o que as notas registram a partir da fala, não algo escrito na tela.
- Encerramento montado como apanhado visual rápido dos premiados, passando por edição de fotos, jogo de ritmo com pista em neon e pontuação na tela, modelagem tridimensional, partituras e cena isométrica de jogo, terminando no ícone de um dos apps isolado sobre fundo preto, forma orgânica rosa sobre turquesa em estilo plano com cantos arredondados (folha 0008, q0064 a q0072).

Proporção visual: as oito folhas alternam grade de chamada de vídeo com apresentadores e desenvolvedores e capturas dos apps e jogos premiados, mais a abertura e as imagens do campus; nenhuma folha registra slide técnico, bloco de código, medida anotada ou diagrama de layout.

Divergências ou limites registrados: as notas assinalam atribuição incerta em duas folhas, os esboços de personagem são ligados a um jogo citado como não nomeado naquela folha (folha 0003), e a transição de tópico da folha 0004 é descrita como provável, sem certeza de qual app está em tela. O nome do app de desenho aparece grafado de duas formas nas notas, com dois o nas folhas 0004 e 0007 e com três o no ícone lido na folha 0008. A folha 0003 ainda descreve a pessoa em chamada como apresentadora e, na mesma frase, como um homem de óculos, inconsistência registrada no próprio texto das notas.
<!-- /visual:wwdc2020_20022 -->

## O que este grupo revela sobre o jeito Apple

- As três sessões de "Design for intelligence" (ids wwdc2020_10087, wwdc2020_10200, wwdc2020_10088) tratam do mesmo arcabouço, o vocabulário compartilhado define/learn/execute do Intents framework, de três ângulos complementares e deliberadamente sequenciados: a visão de oportunidade do desenvolvedor (10088), a jornada de uma pessoa usuária (10200) e a mecânica técnica por trás (10087). Nenhuma das três repete o conteúdo da outra a fundo, cada uma acrescenta uma camada.
- Privacidade on-device aparece como princípio repetido em contextos diferentes, não só como nota de rodapé de compliance: em 10087, como garantia de que as doações nunca saem do dispositivo; em 10088, como opt-in explícito e anonimização para qualquer analytics.
- Tanto na inteligência proativa (10087, 10200, 10088) quanto no redesign visual do macOS (10104) e na acessibilidade (10020), o padrão de argumentação é o mesmo: primeiro mostrar o que o sistema já entrega de graça (previsões automáticas, sidebar automática, cores de sistema que já respeitam Increase Contrast), depois explicar o ponto extra de adoção manual que leva o app além do básico.
- As sessões preferem exemplos concretos e nomeados a explicações abstratas: Soup Chef e Charty (10087), a academia fictícia da jornada narrada (10200), Sneaky Sasquatch e Starstruck (10020) e Mail (10104) aparecem repetidamente como estudo de caso vivo, incluindo demonstrações de "antes e depois" ao ligar uma configuração.

## Sem transcrição

- wwdc2020_20022: agora tem cartão próprio neste arquivo, com a base indicada no cartão.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10087.md: 88 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10200.md: 30 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10020.md: 76 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10088.md: 27 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_10104.md: 110 linhas lidas, até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2020_20022.md: 4 linhas lidas, até o fim: sim (arquivo só tem cabeçalho, sem transcrição falada).
