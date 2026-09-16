# meet-with-apple

## Design with SwiftUI (id: meet-with-apple_270, 25.2 min)

Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/meet-with-apple/270/.

Tese central: Um bom app começa pela estrutura: primeiro se decide o conteúdo e as seções e a navegação, depois o layout, e só então o design visual. Os componentes nativos do SwiftUI já resolvem boa parte das decisões de design (hierarquia, alinhamento, proximidade, cor, acessibilidade), então o designer deve deixá-los fazer o trabalho pesado e colocar personalidade só nos lugares escolhidos, sem prejudicar a usabilidade.

O processo de design que a Apple descreve:
1. Navegação primeiro. A palestrante diz que desenhou o app de exemplo (uma lista de desejos de viagens) do zero e começou pensando na navegação, porque decidir conteúdo e funções dá uma estrutura para construir com clareza e mostra como usar a top bar (termo incerto na transcrição automática) e a toolbar.
2. Brainstorm: listar tudo o que a equipe queria que o app tivesse e fizesse, com todas as ideias aceitas nessa etapa.
3. Simplificar, ficando só com o essencial para esse tipo de app: criar viagens, adicionar fotos, buscar.
4. Dar um passo atrás e agrupar ideias relacionadas: viagens com atividades; progresso com a celebração das viagens concluídas.
5. Transformar os grupos nas três seções principais do app, nomeadas wish list, goals e search. O exercício serve tanto para app novo quanto para revisar um existente.
6. Levar a estrutura para os componentes de navegação: a top bar para as seções de primeiro nível e a toolbar para agir dentro de uma seção.
7. Layout: trazer o conteúdo para as telas e decidir como apresentá-lo, escolhendo entre listas e coleções conforme o conteúdo e o que as pessoas precisam fazer com ele.
8. Design visual: estilos de texto, cores semânticas e consistência, que segundo a fala são os três aspectos de maior impacto e mais cedo.
9. Toque final: voltar e conferir que todos os elementos estão alinhados e com espaçamento consistente. Em seguida, a fala passa ao uso consistente dos componentes e à coerência das imagens.
10. Só então codificar: definir ou avaliar a estrutura e a navegação, usar os componentes com intenção, e assim começar a programar sabendo exatamente o que se constrói.

Princípios enunciados e o porquê:
1. Fazer o exercício de estruturação antes de construir. Porquê: organiza o pensamento e transforma ideias soltas do brainstorm em telas conectadas, prontas para construir; nos workshops com desenvolvedores, segundo a palestrante, sempre abre os olhos.
2. Manter baixo o número de abas na top bar (termo incerto na transcrição automática). Porquê: fica simples e previsível e reduz a tomada de decisão; ao abrir o app a pessoa sabe exatamente quais opções tem. Apps que vão enfiando cada nova função na barra ficam complexos, e pouca gente gosta disso.
3. Manter a top bar nativa. Porquê: os componentes do SwiftUI trazem comportamentos embutidos, como animações e suporte de acessibilidade, que se perdem facilmente quando se customiza. Há muitos outros lugares no app para expressar personalidade; a top bar não é um deles.
4. Usar símbolos e rótulos claros que correspondam ao que há dentro de cada aba.
5. Na toolbar, minimizar o número de ações e usar símbolos familiares. Porquê: fica fácil de escanear; com itens demais, as pessoas não entendem o que se espera que façam primeiro. Solução dada: esconder as ações menos comuns ou mais avançadas no menu more.
6. Usar o estilo proeminente da toolbar em no máximo uma ação por tela. Porquê: ele acrescenta cor e cria um ponto focal imediato; se tudo for importante, nada é.
7. Manter a toolbar nativa. Porquê: acrescentar coisas como um fundo compete com o conteúdo, com a funcionalidade e com os efeitos de morphing.
8. Escolher lista ou coleção conforme o conteúdo e a tarefa. Porquê: as duas são flexíveis, mas uma serve melhor que a outra dependendo do que se mostra e do que a pessoa precisa fazer.
9. Em coleções, escolher imagens que acrescentem valor e títulos de comprimento consistente. Porquê: a maior parte do conteúdo fica fora da tela, então título e imagem definem a expectativa e convidam a rolar; imagens aleatórias, que não parecem curadas, tiram credibilidade do conteúdo; títulos de tamanhos diferentes deixam o layout desajeitado e desalinhado, prejudicando a coleção e também a rolagem vertical abaixo dela. Recomendação: definir regras para o conteúdo das coleções.
10. Usar os estilos de texto do sistema, chamados na fala de textiles (termo incerto na transcrição automática), escolhendo o estilo certo para cada finalidade e aplicando de forma consistente. Porquê: estabelecem hierarquia pronta e favorecem a leitura em diferentes tamanhos de tela e condições; o uso consistente deixa cada tela mais equilibrada e polida, e ao ver um estilo conhecido a pessoa sabe o que aquele conteúdo significa.
11. Adotar Dynamic Type. Porquê: muita gente usa estilos maiores por conforto ou necessidade, e com Dynamic Type os estilos mantêm o mesmo nome, só que consistentemente maiores.
12. Manter mínimas as escolhas de variantes tipográficas. Porquê: a interface parece intencional e o app fica mais fácil de manter e crescer; do contrário se acumulam estilos e variantes demais e surge a dúvida de quando usar cada um.
13. Usar cor semântica para estado e feedback, e não usar a cor de destaque, nem cores parecidas com ela, como decoração. Porquê: senão as pessoas não sabem se aquilo é interativo ou se tem algum significado.
14. Não exagerar na customização das cores do sistema, principalmente em botões e controles. Porquê: essas cores se adaptam sozinhas ao modo claro e escuro, ao liquid glass e a diferentes ambientes de tela.
15. Se usar uma cor fora do sistema, garantir contraste suficiente, testar contra fundos diferentes e fornecer um valor para aumento de contraste, e continuar testando. Porquê: manter o app expressivo sem afetar a usabilidade.
16. Alinhar todos os elementos e espaçar de forma consistente. Porquê: o design fica polido, equilibrado e com aspecto profissional, e isso apoia o modo como as pessoas absorvem informação e decidem o próximo passo; componentes apertados em pouco espaço geram estresse, e uma interface que respira dá espaço para processar.
17. Usar os componentes nativos do mesmo jeito em todas as telas e não oferecer várias formas de fazer a mesma coisa. Porquê: as pessoas já sabem como o componente funciona, onde o viram e o que se espera delas; e simplifica o desenvolvimento, com menos componentes para construir. A fala observa que oferecer várias formas às vezes acontece quando alguém se empolga criando uma tela nova e começa do zero.
18. Dar coerência às imagens e ilustrações. Porquê: devem parecer parte da mesma marca e da mesma coleção.
19. Deixar o SwiftUI, chamado na fala de CPI (termo incerto na transcrição automática), fazer o trabalho pesado e então acrescentar personalidade, criatividade e humanidade. Porquê: segundo a palestrante, o SwiftUI cuida de muitas das decisões de design por ela. No fechamento, ela diz esperar que as dicas da palestra reduzam um pouco a incerteza do processo e deem espaço para ser criativo no começo, decidir, fazer brainstorm e depois ir ao código.

Técnicas concretas de construção de interface, com números exatos quando falados:
1. Navegação, top bar (termo incerto na transcrição automática): mostra as seções de primeiro nível e permanece visível em todas as telas; serve para se mover pelo app. O app de exemplo tem três seções principais.
2. Navegação, toolbar: atua dentro de uma seção e tem três elementos. Primeiro, o título da vista atual, que indica onde a pessoa está e dá contexto e tom ao conteúdo. Segundo, os controles das ações mais importantes da tela; a ação primária, criar viagem, fica num controle no canto superior direito. Terceiro, controles de navegação, como o botão voltar no detalhe da viagem, que volta um nível até a wishlist.
3. Toolbar: ações menos comuns ou avançadas vão para o menu more; o estilo proeminente, que acrescenta cor, vale para no máximo 1 ação por tela; nada de fundo extra na barra.
4. Símbolos: vêm do app SF Symbols, biblioteca de iconografia da Apple com mais de 7.000 símbolos que podem ser copiados e colados no design ou no código. Na fala, a toolbar pede símbolos familiares, citados como sub-symbols (termo incerto na transcrição automática).
5. Recursos citados: as Human Interface Guidelines, que a fala abrevia como The Hague (termo incerto na transcrição automática), descritas como a casa das orientações de design para todas as plataformas da Apple e a primeira parada para dúvidas; o link fica na seção de design do site de desenvolvedores, que também tem os Apple Design Resources, cuja biblioteca de componentes nativos a palestrante diz usar em quase todo app que desenhou.
6. Layout com listas: indicadas para conteúdo baseado em texto com muitos itens, porque ajudam a escanear rápido. Estilo edge-to-edge usado nas atividades da viagem. Estilo agrupado (group style) quando é preciso categorizar: o recuo (inset) e os cantos arredondados separam as categorias. A fala menciona a dúvida comum entre S2S (termo incerto na transcrição automática; pelo contexto, o estilo edge-to-edge) e inset.
7. Listas, acessórios e controles: acessórios como imagens e subtítulos ajudam a reconhecer itens sem ler linha por linha; controles como o botão de seleção permitem agir sem ir para outra vista. Tipos de controle citados: steppers, toggles, sliders, entre outros.
8. Layout com coleções: indicadas para navegar por fotos, vídeos ou produtos. No SwiftUI, segundo a fala, coleções são basicamente stack views com uma scroll view que deixa o conteúdo ultrapassar a tela e convida a rolar. Na aba wishlist, cujo objetivo principal é navegar, o layout usa várias variações de coleções com as fotos enviadas pelas pessoas.
9. Princípios que os componentes já tratam: hierarquia, alinhamento e proximidade.
10. Tipografia: estilos de texto do sistema; Title 3 para todos os títulos de seção, como Summer Glow; suporte a Dynamic Type; fonte do sistema SF Pro no app inteiro; variante expanded para ênfase em títulos, buscando um ar esportivo; variante condensed, dita condense na fala, só com parcimônia em alguns overlays.
11. Cor: indigo como cor de destaque (accent color), aplicada nas atividades concluídas e na aba selecionada da top bar; fundo e cor dos separadores não foram definidos, vêm dos componentes nativos; a única cor escolhida foi a de destaque. Verde neon, cor não semântica e fora do kit, reservada à ênfase em indicadores de progresso e subtítulos, com contraste testado contra fundos diferentes e valor próprio para aumento de contraste.
12. Consistência: indicadores de progresso reaproveitam a mesma cor de destaque e a mesma forma, apenas um pouco menores.
13. Imagens: colocar lado a lado e comparar iluminação, nível de detalhe e clima geral; ajustar até parecerem da mesma marca; se parecerem da mesma coleção, confiar na intuição. No exemplo, a direção foi céus dinâmicos, com o assunto em geral menor ou interagindo com o espaço, e a interface mais proeminente que as fotos.

Exemplos citados:
1. O app de lista de desejos de viagens desenhado pela palestrante com a equipe e os engenheiros, com as seções wish list, goals e search; mostra o processo inteiro de brainstorm, simplificação e agrupamento virando navegação, e que o design teve tradução muito próxima no código.
2. Um exemplo de top bar abarrotada, que faz o app parecer mais complexo do que é; ensina a manter poucas abas.
3. A aba wishlist com símbolo de arco-íris: não há símbolo universal para lista de desejos, então o arco-íris foi escolhido por ser reconhecível e transmitir esperança, as viagens que se sonha fazer.
4. A ghost tab (termo incerto na transcrição automática), com símbolo mais explícito que combina com o rótulo e tem a mesma forma de muitos dos colecionáveis dentro dela.
5. A tela wishlist com o título da vista e o controle de criar viagem no canto superior direito, e o detalhe da viagem com botão voltar.
6. Uma toolbar com itens demais, corrigida escondendo ações no menu more; e criar viagem como a única ação proeminente, porque um app de lista de viagens sem viagens não faz sentido.
7. A lista de atividades da viagem em edge-to-edge, e um exemplo em estilo agrupado que, segundo a fala, não está no app e foi mostrado só para esclarecer quando usar cada estilo.
8. Um exemplo de coleção com imagens aleatórias e títulos de tamanhos diferentes, que perde credibilidade e fica desalinhado, inclusive na rolagem vertical abaixo.
9. A seção Summer Glow como título de seção em Title 3.
10. As atividades concluídas e a aba selecionada em indigo; o verde neon em indicadores de progresso e subtítulos; indicadores de progresso menores reaproveitando cor e forma.
11. As imagens de exemplo com céus dinâmicos, fornecidas no código para que se veja o padrão seguido, embora no app real as pessoas enviem as próprias fotos.
12. Nomes citados: Kurt (termo incerto na transcrição automática), que falaria depois sobre os efeitos de morphing, e Leah (termo incerto na transcrição automática), a quem a palestrante devolve a palavra no fim.

Citações:
1. "if everything is important, nothing is important."

<!-- visual:meet-with-apple_270 -->
### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.
- A palestra se organiza visualmente por uma agenda de três tópicos (Navigation, Layout, Visual design) em que o item em curso fica destacado e os outros em cinza, com submenus internos no mesmo padrão, o que dá três níveis de estrutura na tela; o app de exemplo aparece logo na abertura com o ícone Wishlist em losango arco-íris e três telas de iPhone (mapa com trilha, lista de atividades, tela Goals com emblemas hexagonais), e o fechamento é um slide de próximos passos que pede definir uma boa base antes de codar (folha 0001, q0003 a q0009; folha 0002, q0010 a q0012; folha 0017, q0146 a q0150).
- O exercício de estrutura é mostrado em post-its reais, em estágios contáveis: 14 notas soltas no brainstorm, 8 depois de simplificar, as restantes empilhadas em três aglomerados e, por fim, rotuladas como Wishlist (cinco notas), Goals (duas) e Search (uma); a fala descreve o processo sem dar essas contagens (folha 0002, q0013 a q0018).
- O slide nomeia o componente como Tab bar, termo que a transcrição registrou como incerto. A sequência de julgamento é explícita: uma barra com cinco abas rotuladas (Wishlist, Activities, Seasons, Map, Goals) recebe ícone de alerta amarelo; uma barra customizada com duas pílulas coloridas e um botão de busca separado recebe X vermelho junto do princípio de manter a aparência nativa; a barra nativa simples, com ícone e rótulo por aba, recebe check verde junto do princípio de usar símbolos e rótulos claros (folha 0003, q0024 a q0027; folha 0004, q0028 a q0034).
- As ferramentas de apoio aparecem como capturas reais: a página de tab bars das Human Interface Guidelines com barra lateral de categorias e seção de boas práticas, a página Apple Design Resources com os templates UI Kit e App Icon Template para iOS 26, e o app SF Symbols com categorias na lateral, grade de símbolos e seletor de peso (folha 0004, q0036; folha 0005, q0037 a q0041).
- A toolbar é ensinada com o nome da API sobreposto ao mockup: anotação .navigationTitle apontando para o título da tela Wishlist e, em seguida, o rótulo ToolbarItem numa linha de anotação do mesmo mockup, que tem o botão azul "+" no canto; depois uma toolbar com seis ícones (voltar, mais, lápis, marcador de mapa, compartilhar, coração) marcada com X vermelho; e por fim o "+" sozinho dentro de um círculo azul preenchido com a anotação .prominent, contra os ícones de contorno simples (folha 0005, q0045; folha 0006, q0046 a q0054; folha 0007, q0055 a q0058).
- Para listas, a tela contrasta uma lista contínua de atividades, com círculos de seleção à esquerda e sem grupos, com a mesma lista em GroupedListStyle, dividida nas seções Landmarks e Sports em cartões de cantos arredondados; o nome GroupedListStyle aparece como anotação no slide (folha 0007, q0063; folha 0008, q0064 a q0067).
- A anatomia de uma linha de lista é desenhada com linhas retas ligando rótulo e parte: Image na miniatura da foto, Subtitle no texto secundário e Selection button no círculo azul de marcação, com um item marcado e outro não; em seguida vem um catálogo de controles em linhas com Pop-up button, Stepper, Toggle e Slider (folha 0008, q0068 a q0072; folha 0009, q0073).
- Coleções aparecem na seção Winter Wild com cartões de foto de legenda sobreposta; com o mockup rolado surgem mais cartões e as anotações ScrollView e LazyVGrid sobre a estrutura; um diagrama posterior aponta Section title para o cabeçalho e Card title para as legendas (folha 0009, q0075, q0076, q0080 e q0081).
- A coleção mal curada é mostrada antes da correção: X vermelho no slide ao lado de quatro cartões com imagens genéricas e pouco relacionadas entre si (ícone de palmeira, foto circular, cartões verdes quase vazios), depois com legendas em frase longa sobre os dois primeiros; na versão corrigida da seção Fall Drift os cartões trazem fotos reais de paisagem preenchendo o quadro, sob o princípio de manter consistência para coleções escaneáveis (folha 0010, q0083 a q0087).
- A hierarquia tipográfica é anotada duas vezes sobre a mesma tela Summer Glow: primeiro por estilo do sistema (Title 3 no título de seção, Subheadline na descrição, Footnote nas legendas dos cartões), depois por variante da família (SF Pro Expanded no título, SF Pro no subtítulo, SF Pro Condensed nas legendas dos cartões), com os bullets de suportar Dynamic Type e minimizar o número de tipos; antes disso, a entrada da seção Visual design usa um slide de transição em tela cheia preta (folha 0011, q0095 a q0099; folha 0012, q0100 a q0108).
- A cor de destaque indigo é anotada em dois usos de estado na mesma tela: Completed nos checks preenchidos das atividades concluídas e Selected tab na aba Wishlist ativa, sob os bullets de descrever função e adaptar dinamicamente; outro diagrama dá os nomes label para o texto, systemIndigo para os círculos de seleção e Separator para a linha divisória (folha 0013, q0112 a q0117; folha 0014, q0118).
- A cor não semântica aparece como verde-limão restrito a barras de progresso, em cartões como Spring Explorer "2 of 3" e Explore Cambodia com 50% e o rótulo TRIP ACTIVITIES, sob o bullet de usar cor não semântica com parcimônia (folha 0014, q0120 a q0123).
- O espaçamento é mostrado com medidas: guias azuis em colchetes ao redor de um ícone hexagonal na tela Goals e, no cartão de conquista Summer Explorer, anotações de 40px, 20px e 10px nas margens em volta do título, da descrição e da seção de próximos marcos; a fala não cita valores (folha 0014, q0125 e q0126; folha 0015, q0127 e q0128).
- A reutilização de componentes é provada lado a lado: três telas de detalhe de viagem com a mesma estrutura (foto de capa, barra de progresso em 33%, lista de atividades com marcação) e fotos diferentes, sob os bullets de reaproveitar componentes e manter imagens coerentes; depois a vista se afasta para seis telas em fileira que formam o mapa do app (Wishlist, detalhe de viagem, Activities, Goals, Search com teclado) (folha 0015, q0135; folha 0016, q0136 a q0143).
- Estados de interação que a fala não detalha aparecem de passagem: a tela Wishlist em edição, com teclado do sistema, botões X e Edit Trip e confirmação em círculo azul com check (folha 0014, q0119); e um quadro de transição em que campos de formulário Date, Title e Completed se sobrepõem a fragmentos da lista, ao lado de uma tela TRIP ACTIVITIES com o botão de adicionar atividade no rodapé (folha 0016, q0144).
Proporção visual: pelas notas, 14 dos 152 quadros mostram só plateia, a apresentadora sem slide ou um quadro escuro de transição, e outros 2 são closes da apresentadora com texto de slide cortado (q0039, q0050); os demais trazem slides, mockups anotados, capturas de ferramentas ou logos.
Divergências ou limites registrados: a primeira barra de abas tem ícones pouco legíveis, só identificados no zoom de q0027 (folha 0003); alguns textos de slide aparecem cortados sobre a apresentadora (q0039, q0050, q0104, q0106) e q0042 é um quadro escuro sem texto legível.
<!-- /visual:meet-with-apple_270 -->

## AllTrails: Momentum without a rewrite (id: meet-with-apple_274, 14.2 min)

Base: transcrição e 11 de 11 folhas de quadros vistas, códigos conferidos. Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/meet-with-apple/274/.

Tese central: James Graham, CTO da AllTrails, defende que um app UIKit grande e maduro consegue velocidade moderna sem reescrever nada, deixando o SwiftUI entrar onde ele se encaixa em vez de impor a adoção de cima para baixo. O que sustenta isso é tratar a interoperabilidade como infraestrutura e medir impulso (PRs menores, revisões mais rápidas, menos regressões), não quanto do código já foi convertido.

O processo de design que a Apple descreve: A fala é de engenharia e descreve o caminho de adoção da AllTrails, nesta ordem. 1) Ponto de partida: a escala e as restrições do produto, que segundo ele são necessárias para entender as decisões técnicas. 2) Quando o SwiftUI chegou, a AllTrails já era um app UIKit grande, maduro e bem sucedido, com ciclos de lançamento semanais e experiências gratuita e paga; reescrever não era opção. 3) O SwiftUI entrou em silêncio, sem mandato e sem item de roadmap, por meio de um sandbox para experimentação de baixo risco, protótipos e serviços isolados, para aprender o framework sem apostar o release candidate nele. 4) A primeira decisão real não foi escolher entre UIKit e SwiftUI, e sim como os dois prosperam juntos: investimento cedo em interoperabilidade, com um padrão de ponte estabelecido desde o início como decisão de processo, para que as fronteiras ficassem claras. 5) Duas trilhas paralelas se formaram naturalmente: UIKit no trabalho pesado, SwiftUI em superfícies isoladas e novas. 6) O design system passou a ser construído em SwiftUI, em parceria entre design e engenharia, com todas as funcionalidades novas usando esse sistema. 7) A equipe percebeu que o SwiftUI começou a influenciar a arquitetura (view models e PRs menores); esse foi o ponto de virada em que deixou de ser experimento e começou a se tornar a escolha padrão, adotada voluntariamente pelos engenheiros. 8) O sucesso passou a ser medido por redução de linhas de código por funcionalidade, ciclos de iteração mais rápidos e menos regressões nas funcionalidades isoladas em SwiftUI. 9) Reconhecimento de que interoperabilidade é infraestrutura, com investimento em hosting wrappers, pontes de animação compartilhadas e tema unificado. 10) Estado atual: a AllTrails não está migrada para SwiftUI; é um sistema híbrido com direção. Ao final, ele propõe três perguntas para outras equipes avaliarem a adoção no próprio contexto: a interoperabilidade é tratada como infraestrutura; a ferramenta nova reduz a carga cognitiva; você mede impulso e não conversão.

Princípios enunciados e o porquê:
Não reescrever o app. O porquê: na escala em que operam, uma reescrita, seja feita por esforço de engenheiros ou por um fluxo de trabalho nativo de IA, introduz um risco enorme; num app maduro não era viável nem técnica nem organizacionalmente.
O código legado não é um problema a consertar. O porquê: o UIKit foi a base que permitiu a escala; por isso não dava para parar tudo, era preciso manter e atualizar o app com ele em uso (a metáfora usada é atualizar no meio da trilha).
Não se pode lançar código quebrado. O porquê: a diversidade de membros, do passeio casual à trilha de dia inteiro navegando offline sem sinal de celular, cria restrições rígidas de confiabilidade, duração de bateria e desempenho de interface; e cada decisão técnica afeta milhões de membros em aparelhos, regiões e níveis de conectividade diferentes.
Deixar o SwiftUI adotar a equipe, não forçar a adoção. O porquê: os engenheiros escolheram o SwiftUI para trabalho novo porque tinha menos atrito e reduzia a carga cognitiva; quando a escolha é escrever 40% menos código, a adoção se sustenta sozinha. Ele resume que o SwiftUI se espalhou por ser o caminho mais rápido, não por ordem.
Não reescrever telas estáveis e testadas só para trocar de framework. O porquê: num app maduro isso não faz sentido; o investimento novo vai para onde entrega ganhos claros para o usuário e para a velocidade.
Usar o SwiftUI onde ele se encaixa melhor. O porquê: superfícies autocontidas com estado dinâmico e atualizações de interface combinam com o modelo declarativo; superfícies experimentais podem evoluir rápido sem acoplamento forte com a arquitetura central do app.
Interoperabilidade é infraestrutura. O porquê: se ela é frágil ou improvisada, a adoção trava no momento em que a pressão real de produto aparece; quando a ponte é sólida, o SwiftUI deixa de parecer novo e passa a parecer fundacional.
Adoção não é decisão binária. O porquê: a pergunta útil não é se adotar SwiftUI, e sim em que condições a adoção cria impulso em vez de risco; o que funcionou (menos bugs, entrega mais rápida, melhor escala entre equipes) veio de um conjunto de decisões deliberadas, não de uma escolha técnica isolada.
Medir impulso, não conversão. O porquê: impulso aparece em PRs menores, revisões mais rápidas e menos regressões, não no percentual do código convertido.
UIKit e SwiftUI podem coexistir com segurança. O porquê dado é a própria experiência mostrada na fala.
Escolher SwiftUI pela velocidade, não por ser "cool". O porquê: no app do Apple Watch a escolha permitiu iterar mais rápido numa superfície complexa sem mexer na lógica de navegação legada.

Técnicas concretas de construção de interface, com números exatos quando falados:
O que o SwiftUI prometia e a equipe queria: gerenciamento de estado mais limpo; views que se atualizam sozinhas quando os dados mudam, eliminando a classe de bugs em que a interface fica fora de sincronia com o modelo; menos código, 40% a menos que os equivalentes em UIKit; e previews ao vivo, para iterar mudanças de design instantaneamente.
Ponte de interoperabilidade: pegar uma funcionalidade em SwiftUI, como o "trail coordinator" (termo incerto na transcrição automática), envolvê-la numa hosting view, colocá-la dentro de uma stack view comum de UIKit e depois adicioná-la à scroll view. Segundo a fala, algumas seções da hosting view na página contêm as subviews em SwiftUI.
Divisão de responsabilidades: UIKit cuida do ciclo de vida do app, da navegação e de superfícies complexas ou profundamente integradas; segundo a fala, continua ótimo para customização profunda de interface, como collection views complexas e barras de navegação elaboradas. SwiftUI fica com superfícies isoladas e bem delimitadas, views com renderização pesada e experimentos novos.
Design system em SwiftUI chamado "Denali" (termo incerto na transcrição automática): os componentes centrais (botões, segmentos, controles, badges) são construídos em SwiftUI e podem ser vistos dentro do app em modo debug. O que antes levava centenas de linhas de boilerplate passou a levar uma fração disso; adicionar uma variante nova ou ajustar espaçamento é uma mudança simples que se propaga para todo lugar, permitindo escalar o design system sem inchar o código.
Infraestrutura de interoperabilidade citada: hosting wrappers, pontes de animação compartilhadas e tema unificado.
Efeitos medidos na arquitetura: view models ficaram menores, muitas vezes em um terço, porque deixou de existir código de cola para manter interface e estado sincronizados; muito menos encanamento explícito (menos publishers, menos operators, bem menos gerenciamento de ciclo de vida), porque o SwiftUI propaga o estado; como interface, estado e comportamento ficam juntos, as mudanças tocam menos linhas; PRs de interface ficaram de 30 a 40% menores e as revisões de código ficaram visivelmente mais rápidas.
Métricas de sucesso usadas: redução de linhas de código por funcionalidade, ciclos de iteração mais rápidos e menos regressões nas funcionalidades isoladas em SwiftUI.
Números de contexto da AllTrails ditos na fala: mais de 90 milhões de membros na comunidade, 500.000 trilhas no mundo, mais de 1,9 bilhão de milhas registradas, 14 idiomas e ciclos de lançamento semanais.

Exemplos citados:
A página inicial da AllTrails ao longo dos anos, mostrada como exemplo de que o app evolui constantemente com superfícies novas e mais profundidade de funcionalidades.
A funcionalidade photo tour, que destaca fotos ao longo da trilha, citada ao apresentar o produto.
O perfil de membro casual (caminhada fácil e relativamente plana à tarde com vista para um lago local) contra o praticante que encara a trilha de dia inteiro do "half-dome" (termo incerto na transcrição automática) navegando offline; ensina de onde vêm as restrições de confiabilidade, bateria e desempenho.
A página de trilha e a view de atividade da comunidade, mantidas em UIKit por serem superfícies complexas e profundamente integradas.
O fluxo de avaliação de trilha, em SwiftUI por ser uma superfície autocontida com estado dinâmico, que combina com o modelo declarativo.
A experiência "ask-the-trail-anything" (termo incerto na transcrição automática), construída sobre Apple Intelligence, em SwiftUI por ser uma superfície nova e experimental que precisa iterar rápido sem acoplamento com a arquitetura central.
O design system Denali visto no app em modo debug, como caso em que o SwiftUI brilha: componentes centrais com muito menos código e ajustes que se propagam.
O app do Apple Watch, com as superfícies de bússola e mapa em SwiftUI e o mapa usando MapKit; mostra que funcionalidade crítica e sensível a desempenho pode sair com arquitetura moderna.
A funcionalidade de identificação de plantas, 100% em SwiftUI, como exemplo de que o SwiftUI define o crescimento do app.

Citações: "UIKit wasn't a problem to be fixed. It was the foundation that enabled our scale." e "you don't need a rewrite to make progress. You need direction."

<!-- visual:meet-with-apple_274 -->
### O que as imagens mostram
Base: 11 de 11 folhas de quadros vistas, todos os códigos conferidos.
- A estrutura da palestra é guiada por uma agenda em coluna única ao lado do apresentador, com hierarquia por opacidade: o item da seção atual em branco pleno e os outros em cinza apagado, trocando conforme avança (Safe introduction se acende entre q0007 e q0009, Adoption tipping point em q0010); o slide de título escuro traz título grande em branco, subtítulo menor em cinza e o logo verde da AllTrails (folha 0001, q0002 a q0009; folha 0002, q0010).
- As telas do app aparecem em quatro molduras de iPhone em linha, com barra de busca, cards de trilha com foto, badges verdes e botão verde arredondado Start; no zoom se vê um mapa topográfico com a trilha desenhada e um cartão inferior com nome, distância, elevação e os botões Download e Start (folha 0002, q0011 a q0014).
- Os números de escala são cards de fundo verde escuro translúcido, com número grande em branco no topo e legenda pequena em cinza embaixo, revelados um a um da esquerda para a direita (90M, 500,000, 1.9B, 14) (folha 0002, q0016 a q0018).
- A evolução do app é mostrada em seis iPhones com etiqueta verde de versão (iOS 12, 14 e 26), indo de uma tela de busca simples até uma interface com chips de filtro por categoria na versão mais recente; a fala só menciona a página inicial ao longo dos anos (folha 0003, q0023 e q0024).
- A lista de benefícios do SwiftUI é revelada item a item, com o item ativo em branco e os seguintes em cinza escuro quase invisível, em duas colunas com a pergunta à esquerda e o benefício à direita (folha 0003, q0026 e q0027; folha 0004, q0029).
- A tela de detalhe de trilha usada como exemplo tem métricas numa grade de dois por dois (distância, ganho de elevação, tempo estimado, tipo de percurso), aviso de acesso com link sublinhado, badge amarelo de sinal fraco esperado e dois botões na base, Download verde preenchido e Map contornado (folha 0004, q0034 e q0035).
- O padrão de ponte é mostrado em código Swift real com realce de sintaxe: declaração de hostingView com HostingView e TrailCoordinator, criação de uma UIStackView de eixo vertical e chamada addArrangedSubview; é o único trecho de código da palestra e confirma na tela o nome que a transcrição marcou como incerto (folha 0004, q0036; folha 0005, q0037).
- A divisão entre frameworks usa slides de layout repetido, título grande à esquerda, lista de três itens e dois iPhones à direita: UIKit com App lifecycle, Navigation e Legacy Flow; SwiftUI com Isolated surfaces, Rendering-heavy views e Experiments, ilustrado pelo fluxo de avaliação com estrelas (4 de 5), chips selecionáveis com check e barra de progresso fina no rodapé indicando a etapa, e por uma tela de perguntas e respostas da comunidade com avatares circulares (folha 0005, q0044 e q0045; folha 0006, q0046 e q0047).
- O design system aparece como catálogo em modo debug em quatro iPhones rotulados Denali Alert, Denali Chip View, Denali Badge, Logo, Logo Co. e Denali Button, cada um com as variações do componente empilhadas (alertas com ícone colorido, chips arredondados, emblemas, botões preenchido escuro e contornado); o mesmo layout é mostrado em modo claro e depois em modo escuro, só com fundo e superfícies invertidos. A tela confirma o nome Denali, marcado como incerto na transcrição (folha 0006, q0049 a q0054).
- Os resultados são slides de estatística com o maior tamanho de tipo da folha: número percentual em verde saturado, seta cinza para baixo à esquerda e legenda branca abaixo, alinhados à esquerda sobre preto; primeiro dois em colunas simétricas (33% Fewer ViewModel LOC e 50% Less Reactive Plumbing), depois um por slide, com 50% Less Reactive Plumbing sozinho e em seguida 35% Smaller Pull Requests. A tela dá 50% para o encanamento reativo, que a fala não quantifica, e um único 35% onde a fala dá a faixa de 30 a 40% (folha 0007, q0056 a q0060).
- Os cartões de transição seguem sempre o mesmo modelo: frase curta única, alinhada à esquerda, em branco sobre fundo preto, sem imagem de apoio, como SwiftUI enters quietly, The codebase didn't flip overnight, Invest in interoperability e Create momentum instead of risk (folha 0004; folha 0008, q0066 a q0071; folha 0009).
- O app do Apple Watch aparece em dois mostradores redondos: uma bússola digital com ponteiro triangular azul sobre verde escuro e tempo decorrido no canto, e um mapa de trilha em miniatura com rota azul sobre fundo bege e verde claro, com a coroa digital visível (folha 0008, q0072; folha 0009).
- O par título à esquerda e iPhone de exemplo à direita se repete três vezes seguidas: UIKit provides stability com uma tela de filtros de opções com toggles e botão de ação inferior; SwiftUI defines our growth com a identificação de planta (foto em close de flor roxa, nome da espécie em tipo grande sobre a imagem, cartão descritivo embaixo); e o logo AllTrails com foto e mapa de trilha. Mais adiante, depois dos slides de pergunta e de transição, What worked for us traz um iPhone com uma notificação push em card de sistema no topo de uma tela com rota de mapa (folha 0009, q0076 a q0081).
- As perguntas de avaliação usam um selo circular verde preenchido com o número em branco à esquerda do texto, e a primeira é revelada em duas fases de opacidade, de cinza fraco para branco pleno, na mesma posição (folha 0010, q0086 a q0089).
- O verde da marca se repete como acento nos elementos de destaque: os números de estatística usam o mesmo verde do logo, e os selos das perguntas repetem esse verde; o encerramento junta o ícone verde ao nome AllTrails em sans-serif branca e termina com a maçã translúcida sobre a cena clareando para cinza (folha 0007; folha 0010; folha 0011, q0092 e q0093).
Proporção visual: as 11 folhas trazem slides, telas do app, catálogo do design system ou código; quadros só de apresentador ou plateia aparecem intercalados em pelo menos sete folhas (0001, 0003, 0004, 0007, 0008, 0010 e 0011), e as notas não permitem contar a proporção por quadro.
Divergências ou limites registrados: só as duas primeiras das três perguntas aparecem completas; a folha termina num texto grande cortado que começa com "Are...", sem a terceira pergunta legível (folha 0010, q0090).
<!-- /visual:meet-with-apple_274 -->

## Showcase: Learn how apps are integrating the new design and Liquid Glass (id: meet-with-apple_208, 116.3 min)

Base: transcrição e 81 de 81 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/meet-with-apple/208/.

**Tese central.** Este é o evento guarda-chuva: a design evangelist Sarah McClanahan abre explicando o novo design e o Liquid Glass, quatro equipes (LTK, Slack, CNN, Tide Guide) apresentam seus casos (cobertos em detalhe nos cards próprios abaixo), depois há um bate-papo (fireside chat) com Sky Guide, American Airlines e Lowe's mediado por Curt Clifton, e por fim um painel com o próprio time de design da Apple (Lance Wilson, Caroline Cranfill, Bobby Martin, mediado por um colega identificado como "Mike" na fala) contando os bastidores de como o Liquid Glass foi desenhado. Este card foca no conteúdo exclusivo deste vídeo: a introdução de Sarah, o fireside chat e o painel interno da Apple.

**O processo de design que a Apple descreve.**
- Na abertura, Sarah McClanahan explica que o objetivo do redesenho foi dar mais ênfase ao conteúdo do app, criando uma separação mais nítida entre uma "camada funcional de UI" (tab bars, toolbars, controles que devem aparecer quando necessário e recuar quando não) e uma "camada de conteúdo" (onde a identidade de marca deve viver).
- No fireside chat, os três convidados relatam como chegaram às próprias decisões: Chris Laurel (Sky Guide) diz que a maior preocupação inicial era performance, porque a visão do céu do app precisa de animação suave sem quedas de quadro; resolveram prototipando rapidamente (poucos dias) uma UI em Liquid Glass dentro do Sky Guide para verificar que a performance seria aceitável antes de seguir adiante.
- Steve Lindgren (Lowe's) descreve como formaram um "pequeno time empoderado" de três pessoas (produto, UX e engenharia) dentro de uma empresa de 300 mil associados, com "direções soltas" da liderança, e que esse time depois evangelizou a mudança para o resto da organização mostrando código funcionando em vez de telas estáticas.
- Moonhee Kwak (American Airlines) descreve como recriaram fisicamente a configuração de um workshop de Liquid Glass da Apple, com desenvolvedores e designers sentados lado a lado testando em tempo real em vez de debater ideias abstratas.
- No painel interno, Lance Wilson descreve o processo como "iteração meticulosa", testando os limites de uma ideia e do que é familiar; para cada recurso lançado existem dezenas de esboços e protótipos descartados.
- Caroline Cranfill descreve o processo de colaboração entre times de frameworks e de apps através de "alignment meetings", nos quais ficava explícito o que os frameworks dariam de graça e o que cada app precisaria construir por conta própria; também descreve sessões de co-localização física entre designers e engenheiros olhando o app já compilado, porque os materiais do Liquid Glass eram difíceis de replicar nas próprias ferramentas de design.
- O time também descreve auditoria e testes extensivos das métricas fundamentais de componentes (tamanhos, densidade) em muitos contextos antes de fixar novos valores, embora nenhum valor numérico final tenha sido citado na fala (a pergunta do mediador citou "44... 48 ou 52 pontos" apenas como exemplo hipotético, não como resposta).

**Princípios enunciados e o porquê de cada um.**
- Controles nativos "pertencem à plataforma": foram construídos para suportar vários tamanhos de tela, tap targets, dynamic type, localização e animação "de graça", por isso apps que usam SwiftUI e componentes nativos desde o iOS 18 adotam o novo design automaticamente ao recompilar contra o SDK do iOS 26.
- Unificação da linguagem visual entre plataformas: motivada pela forma como usuários migram entre iPhone, iPad e Mac, e inspirada por elementos como a Dynamic Island e a experiência imersiva do Vision Pro.
- Redução do "footprint" da interface: hardware evoluiu (telas maiores, bordas mais finas), e a antiga camada de interface estava ocupando cada vez mais espaço do conteúdo; o Liquid Glass busca reverter isso.
- Trazer controles de janela do Mac OS para o iPad funcionou, mas trazer a toolbar colorida do iOS para o Mac OS não funcionou, por causa da densidade de controles em tela e do ambiente multi-janela do Mac; o time reverteu para controles mais monocromáticos no Mac, e depois percebeu que esses controles monocromáticos funcionavam melhor de volta no iOS também.
- Alertas foram testados alinhados na parte inferior da tela, mas voltaram a ficar centralizados, por serem elementos que pedem pausa e atenção do usuário.
- Busca movida do topo para a parte inferior em iPhone (em apps com e sem tabs): motivo citado é alcance/ergonomia e capacidade de a busca animar suavemente para um campo de entrada ao ser tocada; comprimir os demais itens da tab bar numa única fileira evitou precisar de uma segunda fileira de controles.
- Recolhimento da tab bar ao rolar é opcional e deve ser usado quando o objetivo é priorizar o conteúdo (ex.: leitura de artigo); em outros contextos (como navegação/descoberta) pode ser preferível manter a barra mais presente.
- Fonte do sistema San Francisco suporta mais de 150 idiomas e adapta geometria e espaçamento conforme o tamanho do texto; SF Symbols se adaptam automaticamente à direção de leitura (esquerda para direita ou o inverso), inclusive símbolos com elementos tipográficos ou numéricos, adaptados para cerca de 20 idiomas diferentes; componentes de lista crescem em altura para acomodar textos de scripts mais altos.

**Técnicas concretas de construção de interface.**
- Camada de conteúdo deve refletir a identidade de marca; controles Liquid Glass "pegam" e refletem visualmente esse conteúdo sem distrair da funcionalidade. Exemplos citados por Sarah: o app Crumble mostra conteúdo de marca edge-to-edge; a Lucid Motors usa tab bar padrão de navegação mas com identidade visual própria (ícones, cor e interações personalizadas) na área de conteúdo.
- O app Lumy (rastreador de luz do dia) usa um controle de Liquid Glass para "esfregar" (scrub) o horário do dia e descobrir nascer e pôr do sol.
- O app de treino The Outsiders usa navegação de três abas com ações padrão na toolbar superior, mas camada de conteúdo com insights densos em dados.
- Ícones de app: conversão automática de ícones legados para Liquid Glass no dia 1 do lançamento (mesmo sem o desenvolvedor ter atualizado nada), usando lógica de segmentação inteligente; Icon Composer permite especificar exatamente quais camadas recebem Liquid Glass e configurar translucência, sombras, destaques especulares e fonte de luz, além de visualizar em modos "tinted" e "clear". A American Airlines usou o Icon Composer para dissecar seu logo (águia abstrata) em quatro grupos e testar luz e sombra, chegando a uma reinterpretação sutil do logo depois de uma primeira tentativa (esticar a asa inferior para sobrepor o bico) ser reprovada pelos times de marca e jurídico.
- Lowe's manteve a barra azul característica da marca nas telas raiz de cada aba, mas removeu essa barra sólida completamente nas telas filhas de navegação (listagem e detalhe de produto), devolvendo espaço de tela ao conteúdo.
- Branding sem uma "camada" visual própria: Chris Laurel (Sky Guide) descreve que, como não há outro produto ao redor do app, "a marca é o app em si", a identidade vem da qualidade da experiência (animações suaves, controles responsivos, imagens atraentes, atenção a detalhes), não de elementos gráficos de marca.
- Sky Guide no iPad usa um layout inspirado no Apple Maps: UI de iPhone em modo retrato embutida numa sheet do lado esquerdo da tela, com a visão do céu sempre visível simultaneamente, para que ajustes de configuração se reflitam imediatamente na visualização.
- American Airlines usa um controle segmentado customizado (duplo, empilhado) na aba de viagens: um segmento nativo para a ação específica de uma tarefa, e um segmento customizado para navegação, inspirado no app Fotos da Apple (cuja API para esse padrão não estava disponível), incluindo um badge de notificação replicado a partir do comportamento nativo.
- Motion/morphing: um botão pode se transformar diretamente em um menu, evitando que o usuário precise reposicionar a mão no aparelho para completar uma ação relacionada; o time descreve o efeito com uma metáfora biológica de materialização/desmaterialização (citando mitose e meiose como referência de estudo).

**Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina.**
- Crumble e Lucid Motors: como conteúdo de marca e controles nativos podem conviver na mesma tela sem competir.
- Lumy: como um controle interativo de Liquid Glass pode virar parte central da experiência (scrub de horário).
- The Outsiders: como navegação simples (três abas, toolbar padrão) pode conviver com uma camada de conteúdo densa em dados.
- American Airlines (ícone e header): como reinterpretar um logo de marca através de Liquid Glass sem descaracterizá-lo, e como decidir deixar um logo "rolar para fora" do topo conforme o usuário rola o conteúdo.
- Lowe's (barra azul): como remover um elemento de marca muito reconhecível das telas de navegação profunda sem perder a "porta de entrada" familiar nas abas raiz.
- Sky Guide (layout inspirado no Apple Maps): como aproveitar um padrão de sheet lateral já validado pela própria Apple em vez de inventar um novo, mesmo esse padrão não sendo (ainda) um controle nativo do iPadOS.

**Até duas citações curtas, literais.**
- "Building a plane and flying it at the same time" (Caroline Cranfill, sobre o esforço de colaboração).
- "Liquid Glass is beautiful, but it's more than visual craft." (Sarah McClanahan).

<!-- visual:meet-with-apple_208 -->
### O que as imagens mostram
Base: 81 de 81 folhas de quadros abertas e vistas, todos os códigos conferidos.

- Na abertura, os controles de exemplo aparecem translúcidos sobre conteúdo colorido: player com três botões circulares, o central maior que os laterais (folha 0002, q0017); controle segmentado VIDEO/PHOTO e botão "Select" em pílula sobre foto (folha 0003, q0020 e q0021); barra inferior com cinco ícones circulares translúcidos sobre foto e chips de filtro em pílula com um item selecionado em azul e busca circular à direita (folha 0004, q0032 e q0033). Na mesma folha surge um menu escuro com ícones à esquerda dos itens e interruptores à direita (folha 0004, q0035).
- A mesma introdução cataloga os componentes nativos em quatro cartões brancos translúcidos rotulados Tab bar, Sheet, Controls e Context menu (folha 0006, q0047) e usa um único painel de controles (toggle, botão "+", slider azul, slider de gradiente, legenda One/Two/Three) primeiro isolado no telão e depois dentro de uma moldura de iPhone (folha 0001, q0004; folha 0006, q0053). O iOS 7 aparece como referência antiga: um ícone "iOS 7" seguido de quatro molduras de iPhone antigo com telas daquele sistema, de ícones planos e cores sólidas (folha 0001, q0007 e q0008), e depois de uma moldura maior com teclado de discagem (folha 0001, q0009).
- Apps de terceiros aparecem num formato fixo: ícone grande em squircle de um lado e moldura de iPhone com a tela do app do outro. No Crumbl a tela passa da capa "National Flavors" para a de um produto, mostrando navegação dentro do mesmo app (folha 0005, q0040 e q0041); o formato se repete com um ícone de urso ao lado de uma tela escura de app automotivo (folha 0005, q0042) e com um ícone de raio de sol ao lado de uma tela escura de clima (folha 0006, q0049 e q0050).
- No caso LTK, a tela mostra um mockup com o logo "RUNWAY", abas Posts, Products e Creators, indicador de porcentagem e paleta de swatches (folha 0011, q0092); um diagrama de arquitetura de informação em árvore, com caixas coloridas por categoria e amarelo no nível superior (folha 0011, q0094 a q0099); código SwiftUI ao lado do mockup com ".buttonStyle(.glass)" destacado (folha 0012, q0103 e q0104); e o par "with Runway" e "without Runway", com selo "Code complete" sobre os mockups (folha 0012, q0105 a q0107).
- No Slack, a diferença entre quadros registra o estado de um gesto: a célula da mensagem desliza e fica azul com "Keep Unread", acima dos botões fixos Keep Unread (contorno) e Mark as Read (preenchido em verde) (folha 0017, q0149 para q0150); logo depois surge uma barra de reações rápidas com ícones circulares translúcidos sobre o teclado (folha 0017, q0151 e q0152).
- Ainda no Slack, a mesma lista de canais é repetida em três iPhones para comparar três cabeçalhos prototipados (concêntrico, cápsula e gradiente), com anatomia da lista constante: ícone à esquerda, contador de não lidas à direita, seções VIP, Mentions e Project Space com triângulo de expandir, e tab bar Home, DMs, Activity e More com busca (folha 0021, q0183 a q0187). Em outro trio só o tema de cor muda (claro, escuro, laranja), mantendo grade e hierarquia (folha 0022, q0190 a q0192). O par iOS 18 e iOS 26 mostra a tab bar sólida virando tab bar e cabeçalho translúcidos sobre a mesma estrutura (folha 0020, q0176 a q0178).
- A decomposição de tela por linhas de chamada (rótulo ligado por linha reta a uma parte da interface) é o recurso de anatomia mais recorrente: no iPad do Slack, "Improved Menus" e "Windowing" (folha 0023, q0204); nos iPhones, Conversation Headers, Composer, Create Menu e Tab Bar (folha 0023, q0206); no canvas, Viewer Chrome e Canvas Controls (folha 0024, q0210); no artigo da CNN, Title, Byline, Image e Paragraph, depois Top navigation e Tab bar (folha 0027, q0235 a q0238). No Slack os rótulos entram sobre a tela já exibida limpa (folha 0023, q0203 para q0204 e q0205 para q0206; folha 0024, q0209 para q0210), e as telas vêm em slides com o nome do mês em texto grande, de September a December (folhas 0023 e 0024).
- Na CNN há um par de certo e errado sobre onde aplicar o vidro: dois iPhones rotulados "Nested glass" e "No nested glass" (folha 0028, q0252), precedidos de um slide de código Swift com um ViewModifier customizado e condicional "#available" (folha 0028, q0250 e q0251). A lista de aprendizados cresce um tópico por vez, trocando a imagem à direita: um menu de "Liquid Glass padding offset" sobre tela vermelha (folha 0029, q0254) e um player anotado com vidro na busca e nos controles do player e sem vidro na navegação inferior (folha 0029, q0256).
- No Tide Guide, a anatomia do cartão flutuante sobre o mapa aparece completa: botões + e X no canto superior direito, curva de maré com pontos de alta e baixa e horários, grade de quatro métricas com ícone e valor, e tab bar de cinco itens com o ativo preenchido em azul (folha 0034, q0300 e q0301). Na mesma folha, um cartão de maré fechado dá lugar a um painel de vento com seletor de dias em pílula azul, valor numérico grande e mini gráfico de barras, uma mudança de estado dentro do app (folha 0034, q0303 para q0304).
- Nos slides "Identity effects", o mesmo tipo de gráfico de onda aparece em contextos diferentes, dentro de um mini player e dentro de um cartão simples, e outro slide com o mesmo título traz um gráfico de vento com barras e linha (folha 0035; mini player em q0308 e q0309). Numa lista de previsão por data, cada bloco diário tem cabeçalho de data em negrito, curva preenchida em gradiente azul, ícone de clima com rótulo curto e grade de quatro horários, sob um seletor de período no topo (folha 0035, q0311).
- A evolução de um mesmo padrão aparece em três etapas de telas reais do Tide Guide: menu de contexto em lista com submenu de linha do tempo e tamanho (folha 0036, q0321 a q0323; folha 0037, q0325); popover de vidro com controles segmentados em pílula, item selecionado em cor sólida, toggle azul e item com chevron (folha 0037, q0326 e q0327, q0329 e q0330); e tela cheia "Customize Charts" com lista reordenável, botões vermelhos de remover e alças de arrastar (folha 0037, q0328).
- Layout ao longo do tempo e entre dispositivos: quatro iPhones rotulados iOS 12, 14, 16 e 26 lado a lado, das versões mais textuais à mais visual, com curva de onda e cores (folha 0032, q0283 e q0284); o mesmo gráfico de maré adaptado a notebook, iPhone e relógio (folha 0032); no iPad, barra lateral fixa e grade de cartões em duas colunas, que o iPhone ao lado reduz a uma coluna (folha 0036, q0320).
- Alinhamento e espaçamento: três telas lado a lado com borda esquerda comum, a de localização com botão vermelho "Remove" no rodapé, a de suporte com botão azul preenchido Email Support e ações com ícone à esquerda, e a de ajustes com ícone colorido à esquerda e chevron à direita em cada item (folha 0038, q0335); seguem o teclado do sistema com busca e sugestões de local (folha 0038, q0337) e o slide "Redesign not required." (folha 0038, q0342).
- Os próprios slides usam hierarquia tipográfica pura: agendas em que o item ativo fica em branco pleno e os demais em cinza translúcido, sem cor nem ícone (folha 0008, q0066 a q0072; folha 0019, q0170; folha 0033, q0296); estatísticas em serifada grande com ">>" entre valor antigo e novo e legenda pequena sem serifa (folha 0015, q0129 a q0132).
- Nas folhas 0043 a 0080, o único artefato de design projetado é o par de ícones da American Airlines rotulado iOS 18 e iOS 26, com a mesma águia passando de tratamento gráfico plano para aparência translúcida em camadas de luz (folha 0050, q0443 a q0450); fora isso, só a cenografia de dois círculos translúcidos que se aproximam e se sobrepõem (folha 0052, q0460 a q0463). Pouco antes, na abertura do fireside chat, as cartelas de identificação seguem o padrão logo, nome e iPhone com tela do app (folha 0041, q0361 a q0365).

Proporção visual: as folhas 0001 a 0038 (primeiros 52 minutos, com a abertura e os casos LTK, Slack, CNN e Tide Guide) são densas em slides, capturas de tela e mockups, enquanto das folhas 0039 a 0080 (fireside chat e painel do time de design da Apple, cerca de uma hora) quase tudo é só palco, painelistas e plateia, com exceção das cartelas das folhas 0040 e 0041 e do slide de ícones da folha 0050; a folha 0081 é o cartão final de copyright.

Divergências ou limites registrados: nas folhas 0064 a 0080 a fala descreve toolbar colorida levada ao Mac e alertas alinhados embaixo (0064), botão que se transforma em menu (0069 e 0070), métricas de tamanho de componentes (0070 e 0071), San Francisco e SF Symbols (0072 e 0073) e o Icon Composer (0079), mas nenhuma imagem correspondente aparece, e nas folhas 0043 a 0063 não há esboço, protótipo nem anotação de medida visível; o código Swift da folha 0028 é pequeno e não totalmente legível; o mockup de notebook do Slack na folha 0018 tem baixa legibilidade; os tablets nas mãos dos painelistas estão sempre apagados ou fora de vista; a folha 0081 tem só 2 dos 9 quadros preenchidos.
<!-- /visual:meet-with-apple_208 -->

## Liquid Glass showcase: Tide Guide (id: meet-with-apple_257, 10.9 min)

Base: transcrição e 9 de 9 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/meet-with-apple/257/.

**Tese central.** Tucker MacDonald, fundador da Condor Digital e desenvolvedor solo do app de marés Tide Guide desde 2018, mostra como adotou o Liquid Glass para tornar a interação mais tátil e fluida sem "pesar" a interface, defendendo que adotar componentes atualizados do sistema já traz a maior parte do ganho, e que redesenhar por completo não é pré-requisito.

**O processo de design que a Apple/o apresentador descreve.**
- Ele buscou aplicar Liquid Glass onde a interação já era central: botões, o gráfico de maré principal, os cartões de tabela de maré e o container de gráfico horário.
- Identificou "paper cuts" (pequenas fricções) em um padrão de menu de contexto com submenus que ele já usava: cada seleção reconstruía o menu inteiro rapidamente, exigindo muitos toques para configurar preferências (linha do tempo, ordem, altura dos gráficos). Testou remover a hierarquia e colocar tudo em uma lista única, mas achou isso difícil de ler à primeira vista.
- Resolveu adotando um popover de vidro, reaproveitando os mesmos componentes do menu original, que mantém as opções visíveis e permite tocar para abrir uma sheet completa de controles reordenáveis; ao terminar, tudo recolhe de volta ao menu de reticências.
- Conclusão do processo: "meu processo foi mais adotar e depois redesenhar" (paráfrase), grande parte dos ganhos veio simplesmente de usar a versão mais recente dos componentes de sistema, sem esperar por um redesenho completo.

**Princípios enunciados e o porquê de cada um.**
- Interfaces devem parecer vivas sem ficar "pesadas": efeitos expressivos e funcionais, não apenas decorativos, citação literal abaixo.
- Concentricidade (cantos suaves consistentes com a forma do hardware) torna as telas mais "acolhedoras" e "em casa", independente do dispositivo ou espaço de tela disponível.
- Alinhamento consistente à esquerda (leading) e espaçamento reduzem a carga cognitiva, porque permitem escanear rapidamente a borda inicial de cada linha e reconhecer ação/conteúdo por cor e iconografia.
- O novo posicionamento de teclado e barra de busca evita comportamento inesperado ao digitar, o que ele considera importante porque entrada de texto é um ponto sensível de frustração quando algo foge do esperado.

**Técnicas concretas de construção de interface.**
- Estilo de botão Liquid Glass: expande e "morfa" sob o dedo ao toque, dando feedback imediato antes mesmo de soltar; especialmente útil em botões pequenos, normalmente cobertos pelo próprio dedo ao tocar, onde antes não era óbvio que o toque tinha registrado até levantar o dedo.
- Botões de dia da semana na sheet do gráfico horário: expandem e "morfam" dentro do container; o efeito é descrito como "snappy" e, combinado com feedback háptico, cria um "momento" de interação.
- Variante "identity" do glass: não altera a aparência até haver interação. Aplicada à onda de maré principal (ao arrastar, surge um destaque sutil e suave sob a onda) e aos cartões do gráfico de maré (substituindo uma animação de escala que ele usava antes, deixando os cartões mais coesos com o resto do app e da plataforma).
- Mesmo efeito "identity" aplicado ao fundo dos containers do gráfico horário: ao arrastar/esfregar as condições horárias, o container "escala" de forma tátil.
- Uso do material de vidro de forma customizada como destaque de detalhes pequenos: nível de água selecionado no gráfico de maré ao arrastar o dedo pela onda, e nos anéis da animação de radar da tela vazia de estações (quando um novo usuário configura o app pela primeira vez), criando um efeito de refração.
- Popover de vidro para configurações do gráfico (linha do tempo, ordem, altura), com opção de abrir uma sheet completa e reordenar itens, e um componente customizado equivalente para os presets nas tabelas de maré.
- Mudanças de padding e hierarquia aplicadas de forma mais ampla, não restritas apenas à versão mais nova do sistema operacional.

**Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina.**
- O próprio Tide Guide em múltiplas plataformas: "super simples e glanceable" no Apple Watch, e com "layouts mais densos em informação" no iPad e no Mac, ensina que a mesma marca pode ter densidades de informação muito diferentes por plataforma, mantendo-se "purpose built" para cada uma (paráfrase).
- Menu de contexto com submenu (versão anterior) versus popover de vidro (versão nova): ensina que um padrão tecnicamente correto (context menu) pode gerar fricção de uso real (reconstrução do menu a cada seleção) que só aparece no uso continuado.

**Até duas citações curtas, literais.**
- "without being overweight, expressive and functional without being distracting"
- "my process was more adopt and then redesign"

<!-- visual:meet-with-apple_257 -->
### O que as imagens mostram
Base: 9 de 9 folhas de quadros vistas, todos os códigos conferidos.
- Comparação direta entre gerações do mesmo app: o slide "Design evolution since 2018" alinha quatro iPhones rotulados iOS 12, iOS 14, iOS 18 e iOS 26, cada um com uma captura real emoldurada em moldura de aparelho, permitindo ver lado a lado a mudança de paleta, de cartão e de estilo de gráfico (folha 0001, q0007 e q0008).
- Mesma interface reorganizada por plataforma: os slides "Meet Tide Guide" e "Designed to be Multi-platform" mostram iPhone, iPad, Mac e Apple Watch com os mesmos elementos de gráfico de onda, e o mostrador do Watch reduz tudo a um único valor numérico grande com ícone de menu no canto (folha 0001, q0005 e q0009; folha 0002, q0011).
- Par de padrões antigo e novo para o mesmo ajuste: o menu de contexto tradicional aparece como lista vertical que abre submenu com opções de período e de tamanho, e em seguida o mesmo conjunto vira popover de vidro com chips de seleção e um alternador, sem fechar o painel a cada escolha (folha 0006, q0046, q0048, q0050 e q0052).
- Terceiro passo do mesmo fluxo: tocar em "Customize Charts" abre tela cheia com lista reordenável, alça de arraste à direita de cada linha, botão circular vermelho de remoção à esquerda e marca de confirmação no canto superior direito (folha 0006, q0053).
- Diferença entre quadros que expõe o estado de interação: o mesmo cartão de gráfico de maré aparece plano e frontal em um quadro e inclinado em perspectiva em outro, tornando visível o efeito que só surge durante o toque (folha 0004, q0033 e q0035).
- Anatomia do popover de vento: cartão flutuante com botão de fechar circular no canto superior direito, chips de dia da semana com o dia ativo em fundo sólido escuro, fileira de ícones de sol e lua por período do dia e escala numérica lateral (folha 0004, q0029).
- Anatomia da tela de mapa: barra de navegação inferior com cinco itens rotulados e o item ativo marcado por pílula azul, mais um popup de local como cartão flutuante com cantos arredondados, sombra e dois botões de ação no topo (folha 0003, q0026).
- Alinhamento à esquerda repetido em três telas diferentes: detalhe de estação, "Support" e "Settings" usam a mesma linha, ícone colorido em quadrado arredondado, rótulo e ação à direita, seja chevron, botão ou alternador (folha 0007, q0060; folha 0005, q0041).
- Concentricidade mostrada em nível de componente: no slide "Increased Concentricity" os cantos dos cartões internos acompanham a curvatura dos cantos do próprio dispositivo, o que a fala só trata em abstrato (folha 0007, q0058).
- Busca e teclado ancorados na base: a lista de sugestões de local fica diretamente acima do teclado do sistema, sem folga entre os dois, com ícone de microfone no campo (folha 0007, q0062).
- Densidade diferente por tamanho de tela: no iPad, barra lateral fixa com busca, "Today", "Overview", "Charts", "Tables" e uma seção de recentes, mais grade de cartões de gráfico à direita; no iPhone, os mesmos cartões empilhados verticalmente (folha 0005, q0045).
- Sumário com hierarquia por opacidade, item ativo mais claro e os demais em cinza, com o terceiro item nomeado "Custom menus" em um momento e "Custom Components" em outro (folha 0003, q0021 e q0022; folha 0005, q0038 e q0039).
- Fechamento em duas peças: um slide só de texto, "Redesign not required.", e uma colagem que reúne as telas já mostradas em iPad, iPhones e Apple Watch como resumo do conjunto (folha 0008, q0067, q0065 e q0066).
Proporção visual: quase todas as folhas trazem slide ou mockup de app na tela, com quadros de apresentador sozinho intercalados sobretudo nas folhas 0002, 0003, 0005 e 0008, e a folha 0009 inteira é só plateia, sem interface.
<!-- /visual:meet-with-apple_257 -->

## Liquid Glass showcase: Slack (id: meet-with-apple_255, 12.5 min)

Base: transcrição e 10 de 10 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/meet-with-apple/255/.

**Tese central.** Jaime DeLanghe (líder de produto da experiência Slack na Salesforce) e Akshay Bakshi (diretor de produto mobile) descrevem por que adotar o Liquid Glass foi, segundo eles, "um no-brainer" alinhado aos princípios de produto do Slack, e como aproveitaram a oportunidade para também resolver um problema de busca limitada, movendo-a para a tab bar.

**O processo de design que a Apple/os apresentadores descrevem.**
- Jaime apresenta quatro princípios de produto do Slack que guiam toda decisão de construção (detalhados abaixo).
- Quando o iOS 26 foi anunciado na WWDC 2025, o time de mobile já estava acompanhando ao vivo em um canal dedicado, avaliando "quão longe e fundo" ir no redesenho; decidiram por um redesenho amplo porque a linguagem de design mobile do Slack já vinha evoluindo na mesma direção (animações de "morphing" em menus de criação e cabeçalhos de canal).
- Para o header do app, prototiparam e testaram no dispositivo, na mão, três versões diferentes antes de decidir (detalhado em "técnicas concretas").
- Rollout faseado por risco e frequência de uso: no lançamento de dia 1 (outubro) priorizaram os elementos mais usados diariamente (create menu, tab bar, cabeçalhos de conversa, composer) e as mudanças mais arriscadas de "reconexão de memória muscular" (header de vidro, busca na tab bar); em seguida atualizaram navegação e controles de huddle; planejaram atualizar o chrome do media player e controles de canvas em novembro, e suporte a paisagem (landscape) em dezembro. No iPad, escoparam para setembro apenas o essencial (usar o janelamento do iPadOS 26 e melhorar a menu bar), adiando controles customizados de sidebar que, em uma versão anterior do redesenho, haviam atrasado a engenharia.

**Princípios enunciados e o porquê de cada um.**
- "Take bigger, bolder bets": não se limitar a pensar pequeno, mas também buscar formas de chegar lá com segurança.
- "Seek the steepest part of the utility curve": metáfora atribuída ao fundador Stewart Butterfield, cada unidade de investimento traz retorno crescente até certo ponto, e esse é o ponto ideal para parar (comparada a um marceneiro lascando madeira com uma plaina até achar a beleza da peça).
- "Prototype the path": builds diários do próprio app testados nas mãos da equipe, com disposição para descartar o que não funciona; cultura forte de "usar o que se está construindo".
- "Be a great host": antecipar necessidades do usuário e colocar as coisas onde ele nem pensaria em procurar (metáfora das toalhas deixadas na cama para visitas, também atribuída a Stewart Butterfield).
- "Don't make me think": já que o sistema operacional inteiro está migrando para Liquid Glass, o Slack não deveria ser "extra Slack", o trabalho de ensinar o usuário a usar o software não deveria ser necessário; quanto menos o usuário precisar pensar, melhor.
- Controles nativos "future-proof" o app conforme a plataforma evolui: por exemplo, a tab bar do iOS 26 usa menos espaço, o que já melhora o modo paisagem, e novas orientações futuras serão suportadas automaticamente.

**Técnicas concretas de construção de interface.**
- Busca movida da posição anterior (limitada, exigia sair de uma thread, voltar à home, tocar em busca, encontrar DM/canal/canvas e voltar) para a tab bar, disponível globalmente em qualquer tela.
- Header prototipado em três versões: uma versão "concêntrica" que se encaixava bem na forma do aparelho mas cuja borda inferior "não resolvia bem"; uma versão "cápsula" que encolhia junto à câmera frontal e parecia boa, mas ao alternar entre conversas majoritariamente claras ou escuras às vezes parecia um botão primário; e uma versão "gradiente" parecida com apps da própria Apple, que não funcionava bem com a variabilidade de conteúdo nas scroll views do Slack. Optaram por algo mais próximo do header anterior, mas realçando os containers de Liquid Glass.
- O novo header também precisa acomodar o theming de workspaces (temas pessoais versus profissionais), que no Slack não é só estética, mas ajuda o usuário a diferenciar rapidamente entre contextos ao alternar de workspace.
- Identidade de marca do Slack mantida não pela estética do chrome, mas pela voz e tom da copy, customização e theming do usuário, e a expressividade dos emojis.

**Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina.**
- O recurso "catch up" (ketchup) do Slack, citado como exemplo de transformar uma tarefa que ninguém quer fazer (ler mensagens não lidas) em uma experiência "delightful", ensina que os princípios de produto se aplicam além da estética visual.
- Create menu e menus de cabeçalho de canal, já com animações de "morphing" antes do iOS 26, ensina que uma linguagem de interação própria pode preparar o terreno para adotar rapidamente um novo sistema de design.

**Até duas citações curtas, literais.**
- "seek the steepest part of the utility curve"
- "Our job is to help people get their job done"

<!-- visual:meet-with-apple_255 -->
### O que as imagens mostram
Base: 10 de 10 folhas de quadros vistas, todos os códigos conferidos.
- Lista de princípios construída um a um na tela: cada princípio ganha uma ilustração de boneco em desenho de linha com metáfora própria (equilibrar em uma bola, usar uma vara, subir uma escada, segurar uma xícara, apontar) e o nome em texto pequeno abaixo, a fileira crescendo de um para cinco itens conforme a fala avança (folhas 0003 e 0004, q0019 a q0032).
- Cronograma de lançamento documentado recurso por recurso: marcador de mês fixo na margem esquerda e callouts com linha conectora apontando o elemento exato, "Improved Menus" e "Windowing" no iPad de setembro, "Conversation Headers", "Create Menu" e "Composer" nos iPhones do mesmo mês, "Glass Header" e "Search in the Tab bar" em outubro (folha 0008, q0068, q0070 e q0072).
- O mesmo padrão de callout continua nos meses seguintes: "Viewer Chrome" e "Canvas Controls" sobre um player de mídia e uma tela de notas em novembro, e dezembro reduzido a um único telefone com tela de documento (folha 0009, q0074, q0077).
- Par antes e depois por versão de sistema: dois telefones na mesma composição, lista de canais à esquerda e conversa à direita, rotulados "iOS 18" e depois "iOS 26" (folha 0005, q0040 e q0042).
- Theming provado por repetição, não por afirmação: a mesma tela do workspace fictício se repete em cinco variações com estrutura idêntica, mudando só a cor de cabeçalho e de destaque, e mais adiante em três esquemas de cor com abas adicionais no topo (folha 0006, q0047 a q0051, q0053 e q0054).
- Anatomia da tela inicial do workspace: cabeçalho com nome e avatar, cartões horizontais de resumo, seção de huddles com indicador de chamada em andamento, listas agrupadas por categoria com contador numérico à direita de cada item e barra de navegação inferior de ícones (folha 0006).
- Componente de decisão com dois botões: cartão de conversa com reações e contador, botão contornado de um lado e botão preenchido em verde do outro, mais um estado intermediário de fundo azul com texto centralizado e ícone de seta que sinaliza o gesto, detalhe mecânico que a fala não descreve (folha 0002, q0013 e q0014).
- Virada de problema para solução feita em texto grande, "Search felt limited" ao lado da tela inicial sem ícone de busca dedicado na barra, depois "Search available globally" ao lado de uma lista de conversas, com zoom até o texto sangrar a tela (folha 0007, q0059 a q0064).
- Mensagens internas do próprio time viram material de slide: bolhas com avatar circular, nome em negrito, timestamp, corpo e reações, empilhadas em cascata, listando alvos como "Tab bar (tabless)", "Create menu" e "Composer" (folha 0005, q0038 e q0039).
- Slide de identidade em fileira horizontal com cinco palavras, "Voice", "Tone", "User Customization", "Theming" e "Expressivity", imediatamente antes das telas de tema (folha 0006).
- Cor de marca aplicada ao próprio evento: slide de seção em gradiente roxo e magenta com o ícone do app à direita, e o pano de fundo do palco na mesma família de cor em boa parte do vídeo, ainda que a folha 0001 registre palco escuro (folha 0001, q0006 a q0008; folha 0008).
- Créditos e encerramento padronizados: o slide de título traz nome e cargo dos dois apresentadores, o slide final reúne uma fileira de rostos circulares da equipe, e o último quadro é o ícone com a maçã usado como corte genérico entre vídeos da série (folha 0001; folha 0009, q0081; folha 0010).
Proporção visual: praticamente todas as folhas alternam slide ou captura de app com quadros do apresentador sozinho no palco, e há ainda um quadro só de plateia na folha 0004 e um quadro final sem apresentador na folha 0010.
Divergências ou limites registrados: no quadro de "Search available globally" as notas registram que a lista de conversas não mostra alteração óbvia de navegação, ou seja, a tela não prova visualmente a busca na tab bar naquele quadro (folha 0007, q0062); na folha 0009 o primeiro par de telefones aparece sem rótulo de mês visível; e na folha 0001 as notas apontam resquício do vídeo anterior no telão, com o logo de outra empresa ainda visível ao fundo.
<!-- /visual:meet-with-apple_255 -->

## Liquid Glass showcase: LTK (id: meet-with-apple_254, 9.6 min)

Base: transcrição e 8 de 8 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/meet-with-apple/254/.

**Tese central.** Jeseka Hahn, VP de product design da LTK (comunidade social de recomendações de criadores), conta como a empresa reconstruiu o app do zero em SwiftUI com um novo design system interno chamado Runway, em torno de três lições (começar pequeno; trabalhar de forma mais inteligente, não mais difícil; construir confiança), o que preparou o terreno para adotar o Liquid Glass rapidamente quando ele chegou.

**O processo de design que a Apple/a apresentadora descreve.**
- Ponto de partida da reconstrução: em 2024, mudanças constantes nas plataformas sociais, algoritmos e ruído multiplicado por IA ameaçavam a visibilidade dos criadores que dependem da LTK para sustento; anos de camadas sobre um framework envelhecido haviam deixado o app pesado, lento e caro de evoluir.
- Decidiram reconstruir com um prazo de quatro meses, com um design system verdadeiro (que não existia antes) construído com base no OS nativo da Apple para iteração e escalabilidade mais rápidas.
- Começaram literalmente por um único botão, que cresceu em padrões, telas e uma linguagem compartilhada até virar o design system Runway.
- Auditaram a arquitetura de informação, questionando cada fluxo e padrão; descobriram que resolviam o mesmo problema de múltiplas formas redundantes, mesmo em algo simples como o cartão de produto; praticaram o que chamam internamente de "brutal prioritization" para cortar redundâncias, com debates descritos como "vivos" e prioritização "brutal".
- Para convencer fundadores e liderança a pausar o trabalho corrente e apoiar a reescrita, um engenheiro principal construiu uma demonstração lado a lado mostrando quanto tempo levava para construir uma página com o design system em SwiftUI versus sem ele; a demo (sem design system, o processo "continuava e continuava") encerrou o debate.

**Princípios enunciados e o porquê de cada um.**
- "Brutal prioritization": dizer não a mais opções ajuda a focar no que realmente importa; simplificar dá velocidade e reduz a insegurança das equipes sobre decisões já tomadas.
- Confiança em cascata: primeiro confiança no sistema (design system), depois confiança entre as equipes, e por fim confiança dos próprios usuários.
- A identidade de marca não deve competir com o conteúdo do criador, deve complementá-lo, citação literal abaixo.

**Técnicas concretas de construção de interface.**
- Reescrita completa do app em SwiftUI, com componentes nativos da Apple como base do design system Runway.
- Com Liquid Glass, os controles se integraram ao conteúdo de forma que o conteúdo do criador ficasse em destaque; antes do iOS 26, a equipe gastava semanas ajustando manualmente o layout para alcançar esse mesmo objetivo.
- Após a base sólida em SwiftUI, recursos represados (dark mode, widgets) e novidades a cada nova versão do iOS puderam ser entregues com mais facilidade.
- Nova aba de busca dedicada e adoção de "visual intelligence": o usuário tira uma foto e encontra instantaneamente conteúdo relacionado de criadores dentro da LTK.

**Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina.**
- O cartão de produto (product card), citado como exemplo concreto de um mesmo problema resolvido de várias formas redundantes antes da auditoria, ensina que redundância de padrões se acumula silenciosamente em apps que evoluem por adição contínua.
- A demo lado a lado do engenheiro principal (com e sem design system), ensina que argumentos quantitativos de velocidade de desenvolvimento podem convencer liderança onde argumentos de design por si só não bastariam.

**Números exatos citados.**
- Faturamento em recomendações de criadores: US$ 6 bilhões por ano (contexto de negócio da empresa, citado na abertura).
- Prazo de reconstrução completa do app: 4 meses.
- Corte de tempo de compilação: quase 70%.
- Redução de tamanho do app: quase pela metade.
- Tempo gasto no app desde o relançamento de fevereiro: alta de 138%.
- Uso de busca desde o lançamento do iOS 26: dobrou da noite para o dia ("doubled overnight").

**Até duas citações curtas, literais.**
- "Simplifying gave us the speed to move faster."
- "Our identity should not compete with creator content."

<!-- visual:meet-with-apple_254 -->
### O que as imagens mostram
Base: 8 de 8 folhas de quadros vistas, todos os códigos conferidos.
- Prova de simplicidade em dois painéis de editor lado a lado, "with Runway" contra "without Runway", o painel sem o design system visivelmente mais longo em número de linhas, com a etiqueta "Code complete" aparecendo apenas sobre o painel esquerdo (folha 0004, q0032 a q0034).
- Uma linha de código isolada e ampliada como exemplo de API nativa adotada, mostrada sozinha na tela antes do comparativo (folha 0004).
- Ferramenta concreta da auditoria de arquitetura de informação: diagrama de árvore com nós retangulares coloridos por categoria, organizados em colunas hierárquicas, com nós amarelos destacados no topo e rótulos de fluxo como criar perfil, seguir criador e enquete de produto (folha 0003, q0021 a q0026).
- Métricas em tipografia grande com legenda curta abaixo: tempo de compilação e tamanho do app no formato antes e depois ligado por seta dupla, e uso de busca reduzido a um multiplicador único, sem par de valores (folha 0007, q0059 a q0061).
- Controles translúcidos posicionados sobre a foto, círculos pequenos com ícone central marcando pontos de interesse na imagem de produto, e barra de navegação lateral translúcida ancorada à esquerda sem tapar o conteúdo fotográfico (folha 0006, q0046, q0048 e q0049).
- Transição de estado entre quadros: da foto com marcadores de zoom para a tela de resultados de busca visual, com cabeçalho de voltar e fechar e grade de miniaturas de proporção variável, algumas ocupando duas colunas (folha 0006, q0046 para q0047).
- Barra de ações vertical na borda direita do conteúdo em tela cheia, ícones translúcidos empilhados com contador numérico abaixo de cada um, padrão que reaparece em várias telas do app (folhas 0001, 0005 e 0006, q0004 e q0041).
- Anatomia da tela de post: cabeçalho com avatar e nome, imagem dominante, coluna de ações à direita da foto, carrossel horizontal de produtos relacionados em miniaturas quadradas e bloco de legenda no rodapé (folha 0005, q0041).
- Identidade de marca expressa dentro de componentes de sistema: selo circular do design system com indicador percentual e paleta de swatches quadrados ao lado de uma tela com barra de abas de três itens (folha 0003, q0019).
- Bullets das três lições aparecendo progressivamente na abertura e voltando mais tarde com o terceiro item em destaque, marcando o ponto da fala (folha 0001, q0007 a q0009; folha 0005).
- Texto grande sem interface como recurso de ritmo: três palavras empilhadas para descrever o app antigo, o prazo de reconstrução em texto grande, dois ganhos empilhados e uma frase de fechamento sobre reconstruir do jeito certo (folhas 0002, 0003 e 0004).
- Volume mostrado por repetição de aparelho: seis telefones lado a lado no palco em um momento, cerca de dez em outro, cada um com uma tela diferente do app (folha 0006, q0051; folha 0007).
- Diferença entre quadros que sugere animação: o mesmo telefone aparece inclinado em perspectiva e depois reto de frente, indicando rotação do dispositivo em cena (folha 0006, q0052 para q0053).
- Composição incremental do slide de contexto: entre dois quadros consecutivos o conjunto de recortes de notícia cresce de três para quatro cartões, com a imagem nova inserida entre as existentes (folha 0002, q0010 para q0011).
Proporção visual: predominam slides e capturas do app, com a apresentadora em close intercalada, e a folha 0006 é quase inteira composta por telas do app em tela cheia sem palco visível.
Divergências ou limites registrados: no diagrama de arquitetura de informação as notas registram etiquetas de texto ilegíveis na distância do primeiro enquadramento (folha 0003), e na folha 0005 o texto dos cartões de notificação aparece parcialmente coberto pela apresentadora.
<!-- /visual:meet-with-apple_254 -->

## Liquid Glass showcase: CNN (id: meet-with-apple_256, 9.4 min)

Base: transcrição e 7 de 7 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/meet-with-apple/256/.

**Tese central.** Kevin Long, diretor de apps da CNN, explica como a adoção prévia do SwiftUI (motivada três anos atrás por uma troca de CMS) deixou a CNN bem posicionada para adotar o Liquid Glass rapidamente, e compartilha lições técnicas específicas de integração (aninhamento de modificadores, padding e performance).

**O processo de design que a Apple/o apresentador descreve.**
- Há três anos, a CNN iniciou uma transição para um sistema de gerenciamento de conteúdo moderno, o que exigiu reescrever o código cliente; a equipe aproveitou essa janela para modernizar a arquitetura do cliente iOS e adotar SwiftUI.
- A CNN trabalha com squads multifuncionais por plataforma (engenheiros, gerentes de produto, designers e QA), cada plataforma com competências dedicadas, compartilhando aprendizados entre times mas com soluções adaptadas a cada plataforma, mantendo os princípios de design unificados.
- Recompilaram o app no Xcode 26 para ver como ficava; componentes como tab bar e navigation bar migraram automaticamente e já "ficaram ótimos" sem trabalho extra, servindo como linha de base para desenhar o restante.
- Um designer da equipe participou de um workshop de três dias com a Apple em julho, para entender o que já vem pronto com o Liquid Glass e o que precisa ser construído sob medida; a equipe focou primeiro em acertar o básico, especialmente a navegação de nível superior.

**Princípios enunciados e o porquê de cada um.**
- Evitar modificadores de glass aninhados (aplicados tanto a uma view pai quanto a uma view filha): isso gera redundância visual, dupla translucidez, blur em camadas e renderização imprevisível; a solução foi aplicar o modificador apenas no nível mais alto necessário e criar diretrizes internas para prevenir aninhamento acidental. Citação literal abaixo.
- Cuidado com padding: o efeito de glass nem sempre respeitava o padding esperado, às vezes esticando ou cortando conteúdo; a solução foi envolver o efeito em métodos de background ou overlay e ajustar o padding para fora do escopo do modificador.
- Cuidado com performance: o efeito é intensivo em GPU, especialmente em views roláveis ou atualizadas com frequência; a equipe limitou seu uso a áreas de alta frequência (como listas e animações) e reservou o efeito para componentes estáticos ou de nível superior, como tab bar e toolbars.
- Usar um modificador de view customizado que aplica o efeito de glass condicionalmente, apenas no iOS 26, para dar controle sobre onde o efeito é aplicado (por exemplo, nos overlays de botão do player de vídeo) sem afetar o layout mais amplo do app.

**Técnicas concretas de construção de interface.**
- Antes da migração, a base de código era uma mistura de Objective-C, Swift, UIKit e React Native; o SwiftUI trouxe uma abordagem unificada e moderna para construir views, simplificou o layout e melhorou o gerenciamento de estado.
- Exemplo de renderização de artigo: cada elemento (título, byline, imagem, parágrafo) era antes representado por uma view separada, cada uma com seu próprio nib, lógica e ViewModel; com SwiftUI, consolidaram tudo em um único arquivo por elemento, reduzindo significativamente o número de arquivos e facilitando a navegação e manutenção do código.
- Ganho de velocidade de iteração: ao receber feedback interno sobre espaçamento e contraste no layout de artigo, a equipe conseguiu fazer e pré-visualizar as mudanças em minutos usando SwiftUI, em vez de horas de teste manual e ajuste de layout.
- Planos futuros: migrar o app de tvOS para compartilhar a base de código do iOS, e criar uma equipe (squad) dedicada a inovação específica de plataforma, para acelerar a adoção de novos recursos.

**Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina.**
- Renderização de artigo (título, byline, imagem, parágrafo): ensina como consolidar várias views legadas em um único arquivo por elemento reduz complexidade de manutenção.
- Overlays de botão no player de vídeo: ensina um uso seletivo e condicional do efeito de glass, aplicado apenas onde necessário, sem afetar o layout mais amplo.

**Até duas citações curtas, literais.**
- "Avoid nested glass effect modifiers."
- "The glass modifier is well designed."

<!-- visual:meet-with-apple_256 -->
### O que as imagens mostram
Base: 7 de 7 folhas de quadros vistas, todos os códigos conferidos.
- Par de certo e errado para um problema técnico: dois telefones quase idênticos rotulados "Nested glass" e "No nested glass", cada um com uma imagem dentro de um cartão sobre a tela, tornando visível a dupla translucidez que a fala só descreve em palavras (folha 0004, q0034 e q0035).
- Código real como prova de implementação: um bloco de Swift em editor escuro com sintaxe colorida, rotulado como modificador de view customizado, mostrado em dois quadros consecutivos com deslocamento de enquadramento (folha 0004, q0032).
- Lista de aprendizados construída item a item, sempre com uma imagem de exemplo diferente ao lado: primeiro o item sobre vidro sobre vidro, depois o de padding e comportamento de layout, depois o de performance (folhas 0004 e 0005, q0034 a q0038).
- Callouts que marcam onde o efeito foi e onde não foi aplicado na mesma tela: três etiquetas ligadas por linha apontam campo de busca no topo, controles do player e barra de navegação inferior, esta última nomeada como área sem o efeito (folha 0005, q0038).
- Seta de anotação indicando o deslocamento de padding provocado pelo material, sobre um telefone que mostra o logotipo dentro de um contorno de vidro translúcido (folha 0005, q0037).
- Decomposição de uma tela em componentes: uma miniatura de artigo recebe callouts com linha conectora para título, assinatura, imagem e parágrafo, materializando a consolidação de views que a fala trata em abstrato (folha 0002, q0017 e q0018).
- Callouts de navegação em dois telefones lado a lado, apontando o topo e a base da tela, com uma régua vertical pontilhada entre eles que muda de posição entre quadros consecutivos (folha 0003, q0019 e q0020).
- Mesma imagem de produto sustentando três mensagens diferentes: a composição de duas miniaturas de app permanece fixa enquanto só o texto do slide muda ao longo de três quadros, um por motivador citado (folha 0001, q0006 a q0008).
- Layout de app de mídia visto em tela real: seções horizontais roláveis com título à esquerda e capas de programa com texto sobreposto, mais barra inferior de quatro itens rotulados (folha 0003, q0021).
- Formato vertical em tela cheia para vídeo curto, com legenda sobreposta na parte superior da imagem, informação de local e data, controles e barra de progresso na base e ícone de áudio no canto (folha 0003, q0023).
- Convenção diferente para a TV: menu horizontal no topo com cinco itens, imagem de destaque ocupando a maior parte da tela e texto com botão de ação ancorados na base (folha 0006, q0047).
- Duas variações quase idênticas da mesma tela de artigo mostradas lado a lado, com a manchete e o corpo legíveis apenas no quadro em zoom (folha 0004, q0031).
- Sistema de apresentação compartilhado pela série: o slide de título e o quadro de encerramento com o logo da Apple seguem o mesmo template dos outros vídeos do grupo (folhas 0001 e 0007, q0059).
Proporção visual: todas as folhas de conteúdo trazem slide, captura de app ou código, intercalados com quadros do apresentador sozinho, e apenas a folha 0007 é majoritariamente apresentador e encerramento.
Divergências ou limites registrados: na folha 0001 as notas hesitam sobre quem está em cena, registrando "a apresentadora (o apresentador)"; na folha 0002 o quarto ícone da fileira de papéis aparece sem legenda claramente visível; e na folha 0006 as notas marcam como suposição que um texto cortado seria parte de um agradecimento.
<!-- /visual:meet-with-apple_256 -->

## O que este grupo revela sobre o jeito Apple

- O redesenho do Liquid Glass é tratado pela Apple como um evento de plataforma coordenado com acompanhamento presencial de equipes externas (workshops de vários dias, laboratórios em grupo), não apenas como uma atualização visual anunciada e deixada por conta própria dos desenvolvedores (ids: meet-with-apple_208, meet-with-apple_256).
- A separação entre "camada funcional de UI" (controles nativos) e "camada de conteúdo" (onde a marca deve viver) é o princípio mais repetido entre todos os relatos, aparecendo tanto na fala institucional da Apple quanto nas decisões concretas de cada empresa parceira: Lowe's remove sua barra azul de marca nas telas de detalhe, American Airlines deixa seu logo rolar para fora do topo, Slack mantém a marca na voz e tom da copy em vez da estética do chrome, LTK afirma explicitamente que identidade não deve competir com o conteúdo do criador, Tide Guide valoriza a concentricidade e o espaçamento que fazem a UI "recuar", e CNN descreve sua meta como "edge to edge layouts, minimal chrome" (ids: meet-with-apple_208, meet-with-apple_254, meet-with-apple_255, meet-with-apple_256, meet-with-apple_257).
- Adotar SwiftUI e componentes nativos antes da chegada do Liquid Glass é citado repetidamente como o fator que permitiu adoção rápida do novo design: a CNN já vinha migrando havia três anos por causa de uma troca de CMS, a LTK havia acabado de reescrever o app do zero, e a American Airlines já tinha migrado para componentes nativos antes do Liquid Glass chegar (ids: meet-with-apple_256, meet-with-apple_254, meet-with-apple_208).
- Prototipagem rápida "nas mãos", em dispositivo real, aparece como método recorrente de validação antes de convencer a liderança ou fechar uma decisão de design: Slack testou três versões de header no aparelho, Sky Guide prototipou em poucos dias para validar performance, LTK usou uma demo lado a lado de tempo de desenvolvimento para convencer fundadores, CNN reduziu ciclos de ajuste de layout de horas para minutos, e o próprio time de design da Apple descreve sessões de co-localização com engenheiros observando o build real, porque os materiais do Liquid Glass eram difíceis de replicar nas ferramentas de design (ids: meet-with-apple_208, meet-with-apple_255, meet-with-apple_254, meet-with-apple_256).
- Mover a busca da posição tradicional para a parte inferior da tela (tab bar) é uma mudança estrutural específica, citada de forma independente por múltiplas equipes como decisão de UX significativa, justificada tanto por ergonomia (alcance do polegar) quanto por convenção de todo o sistema operacional mudando ao mesmo tempo (ids: meet-with-apple_208, meet-with-apple_255).
- Performance em GPU do efeito de glass é uma preocupação técnica recorrente entre quem de fato construiu com o material: CNN limita seu uso a componentes estáticos e evita listas/animações de alta frequência, e Sky Guide temia especificamente competição de recursos com a animação contínua da visão do céu, resolvendo a dúvida por meio de prototipagem rápida (ids: meet-with-apple_256, meet-with-apple_208).

## Sem transcrição

- meet-with-apple_270: agora tem cartão próprio neste arquivo, com a base indicada no cartão.
- meet-with-apple_274: agora tem cartão próprio neste arquivo, com a base indicada no cartão.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_270.md, 4 linhas lidas, lido até o fim: sim (arquivo sem transcrição, só cabeçalho).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_274.md, 4 linhas lidas, lido até o fim: sim (arquivo sem transcrição, só cabeçalho).
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_208.md, 320 linhas lidas, em duas partes (1 a 226, depois 227 a 320, por limite de tamanho da primeira leitura), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_257.md, 40 linhas lidas, lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_255.md, 45 linhas lidas, lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_254.md, 39 linhas lidas, lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/meet-with-apple_256.md, 38 linhas lidas, lido até o fim: sim.
