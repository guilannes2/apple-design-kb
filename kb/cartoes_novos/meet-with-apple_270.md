## Design with SwiftUI (id: meet-with-apple_270, 25.2 min)

Base: transcrição (quadros ainda não vistos). Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/meet-with-apple/270/.

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
