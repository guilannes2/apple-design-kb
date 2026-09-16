# Getting started

## Design principles (slug: design-principles)

O que governa: os oito princípios fundamentais que atravessam toda a Human Interface Guidelines e servem de base para pesar decisões de design em qualquer plataforma Apple: Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft e Delight.

Por que: a Apple parte da premissa de que os designs mais bem-sucedidos e duradouros nascem de um entendimento profundo de como as pessoas pensam, sentem e interagem com o mundo. Os princípios não são regras fixas com uma única aplicação correta, e sim ferramentas para arbitrar entre prioridades concorrentes ao longo do processo de design.

Faça e evite, por princípio:

Purpose (fazer algo com significado)
- Comece pela intenção: identifique o que mais importa para quem você projeta.
- Foque no que faz o produto genuinamente útil; pergunte constantemente se o design ainda serve ao propósito.
- Priorize as funcionalidades mais importantes alinhadas ao uso real, em vez de espalhar esforço.
- Investigue soluções existentes e evite recriá-las; defina o que diferencia seu produto.

Agency (deixar as pessoas agirem do próprio jeito)
- Fique fora do caminho: leve as pessoas direto à tarefa ou ao conteúdo.
- Dê liberdade para explorar a interface sem prender a pessoa a fluxos ou modos fixos; quando um fluxo guiado for necessário, torne fácil pulá-lo ou escapar dele.
- Ajude a pessoa a se recuperar de erros: torne ações reversíveis e a recuperação de estados anteriores fácil e barata em tempo.

Responsibility (agir no melhor interesse das pessoas)
- Seja totalmente transparente sobre o que o produto faz e por quê, desde a primeira interação.
- Dê uma justificativa clara ao pedir permissão, e seja claro sobre o que é coletado e como é usado.
- Colete só o necessário para o produto funcionar, antecipe formas de uso indevido e coloque proteções contra abuso.

Familiarity (construir sobre o que as pessoas já sabem)
- Use conceitos que as pessoas já conhecem do mundo real e de outros softwares.
- Mantenha visuais e interações consistentes: uma vez estabelecido um comportamento, aplique-o em todo o design.
- Dê feedback claro: mostre quando controles estão disponíveis, quando o conteúdo muda, e use padrões do sistema para alertas e escolhas.

Flexibility (adaptar-se a contextos e necessidades diversas)
- Projete para todos, tratando acessibilidade como prioridade desde o início.
- Preserve o contexto da pessoa conforme o design se adapta entre plataformas e configurações, mantendo conteúdo e controles em posições consistentes e previsíveis, com animações naturais nas transições.
- Considere vários métodos de entrada (voz, toque, teclado etc.).
- Trate cada plataforma com a mesma intenção e nível de cuidado.

Simplicity (ser claro e direto)
- Inclua só o necessário; simplicidade não é minimalismo, é foco no que é útil.
- Seja conciso: escolha exatamente as palavras necessárias para um conceito ou rótulo de controle.
- Estabeleça hierarquia clara, com controles reconhecíveis e estrutura consistente.

Craft (cuidar de cada detalhe)
- Seja deliberado em cada decisão, buscando visuais, animações, texto e áudio de qualidade.
- Experimente e itere: prototipe cedo, descarte o que não funciona, teste em condições reais.
- Mantenha a interface atualizada com as capacidades e padrões mais recentes da plataforma; design é um compromisso contínuo, não termina no lançamento.

Delight (torná-lo humano)
- Identifique a emoção que você quer inspirar (energizar, acalmar, empolgar) e deixe-a moldar o design.
- Crie momentos definidores: cada interação, até um botão ou uma mensagem de erro, é oportunidade de expressar caráter.
- Não confunda deleite com decoração: não deixe a busca por deleite atrapalhar o propósito central do produto.
- O deleite emerge da soma de tudo: liberdade de agir, segurança para explorar, familiaridade e flexibilidade.

Especificações exatas: não há números, medidas ou valores técnicos neste artigo; é puramente conceitual.

Diferenças por plataforma: nenhuma; os princípios são declarados como transversais a todas as plataformas Apple.

Ligações com outros artigos: nenhuma citação direta a outros artigos da HIG dentro do texto (só um vídeo de recurso, "Principles of great design").

<!-- visual:design-principles -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (2 de 2), todos os códigos conferidos; nenhum vídeo listado para a página.
- As oito imagens formam um sistema de pictogramas rigorosamente uniforme: o mesmo gradiente verde, do claro ao escuro puxando para teal, o mesmo traço grosso arredondado ou preenchimento sólido, o mesmo tamanho relativo e a mesma posição centralizada à esquerda do quadro (img 0425 a 0432).
- Nenhuma ilustração traz texto, legenda, fotografia ou tela de interface; cada princípio é comunicado só por um pictograma isolado (img 0425 a 0432).
- A abertura da página usa um alvo de três círculos concêntricos sobre fundo branco, com o centro mais escuro e as bordas mais claras (img 0425).
- Os três primeiros princípios são figurados com pessoas e abrigo: figura humana de braços e pernas abertos para Purpose (img 0426), duas figuras simplificadas com as mãos unidas ao centro para Agency (img 0427) e uma casa de frente com porta ou janela quadrada vazada em branco para Responsibility (img 0428).
- Os princípios seguintes viram objetos e sinais de uso comum: setas cruzadas nas quatro direções para Familiarity (img 0429), tesoura aberta para Flexibility (img 0430), compasso de desenho técnico com ponta seca e grafite para Simplicity (img 0431) e coração sólido, sem contorno nem detalhe interno, para Craft (img 0432).
- A tesoura leva nos dedos os mesmos círculos vazados que aparecem nas outras composições (img 0430).
- As folhas trazem só a versão clara de cada ilustração; não há variante para o modo escuro no material (folhas 0001 e 0002).
- A sequência registrada vai da abertura até Craft; as folhas não trazem imagem própria para Delight, o oitavo princípio do texto (folhas 0001 e 0002).
<!-- /visual:design-principles -->

## Designing for iOS (slug: designing-for-ios)

O que governa: as características fundamentais do iPhone (tela, ergonomia, formas de entrada, padrões de uso) e as práticas recomendadas para fazer um app ou jogo se sentir "em casa" no iOS.

Por que: a Apple parte da observação de como as pessoas realmente usam o iPhone (no bolso, na mão, em movimento, em sessões curtas ou longas alternando entre apps) para justificar cada prática recomendada; a intenção é que o design reflita as circunstâncias reais de uso do dispositivo, não um ideal abstrato de interface.

Faça e evite:
- Limite o número de controles na tela para ajudar a concentração na tarefa e no conteúdo primário; torne detalhes e ações secundárias descobríveis com interação mínima.
- Adapte-se sem atrito a mudanças de aparência: orientação do dispositivo, Dark Mode e Dynamic Type, deixando a pessoa escolher a configuração que funciona melhor para ela.
- Posicione controles pensando em como o dispositivo é segurado: é mais fácil alcançar controles no meio ou na parte inferior da tela, por isso é especialmente importante permitir deslizar (swipe) para navegar de volta ou iniciar ações em uma linha de lista.
- Com a permissão da pessoa, integre informações disponíveis via capacidades da plataforma (pagamentos, autenticação biométrica, localização) de forma a melhorar a experiência sem pedir que a pessoa digite dados manualmente.

Especificações exatas: nenhum número, medida ou valor específico é dado neste artigo (as características são descritas qualitativamente, como "viewing distance de não mais que um pé ou dois").

Diferenças por plataforma: o artigo é específico do iOS; lista como recursos de sistema próprios do iOS: Widgets, Home Screen quick actions, Spotlight, Shortcuts, Activity views.

Ligações com outros artigos: cita Apple Design Resources e a iOS Pathway (documentação para desenvolvedores) como recursos relacionados.

<!-- visual:designing-for-ios -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A única imagem é um símbolo de abertura de seção, não uma tela real: retângulo de cantos bem arredondados em degradê de verde para verde limão, sem texto nem legenda (img 0434).
- Sobre o fundo há uma grade de construção pontilhada, feita de linhas retas e de um círculo central, toda alinhada ao centro da composição (img 0434).
- O iPhone é desenhado em traço verde escuro e grosso, visto de frente, reduzido a três elementos: moldura vertical arredondada, pequeno entalhe horizontal no topo para câmera e sensores e barra horizontal embaixo como indicador de home (img 0434).
- O aparelho fica exatamente sobre o cruzamento das linhas da grade e inscrito no círculo guia, o que mostra a proporção do contorno derivada de uma grade circular e retangular combinada, e não de um desenho livre (img 0434).
- O verde do fundo corresponde, segundo o texto alternativo oficial registrado nas notas, a uma das seis cores do logo da Apple; a folha traz só a versão clara (img 0434).
<!-- /visual:designing-for-ios -->

## Designing for iPadOS (slug: designing-for-ipados)

O que governa: as características fundamentais do iPad e as práticas recomendadas para que um app ou jogo aproveite a tela grande, os múltiplos modos de entrada e o multitasking do iPadOS.

Por que: a lógica é a mesma do artigo de iOS, adaptada à escala e à flexibilidade do iPad, tela grande, múltiplos modos de entrada combinados (toque, teclado, Apple Pencil, voz) e sessões de uso que vão de ações rápidas a horas de imersão, exigem um design que tire proveito do espaço sem sacrificar a facilidade de alcance dos controles.

Faça e evite:
- Aproveite a tela grande para elevar o conteúdo que importa, minimizando interfaces modais e transições em tela cheia; posicione controles onde sejam fáceis de alcançar, mas sem atrapalhar.
- Use a distância de visualização e o modo de entrada para calibrar o tamanho e a densidade do conteúdo exibido.
- Permita gestos Multi-Touch, teclado físico ou trackpad, ou Apple Pencil, e considere interações únicas que combinem múltiplos modos de entrada.
- Adapte-se sem atrito a mudanças de aparência (orientação, modos de multitasking, Dark Mode, Dynamic Type) e transicione com naturalidade para rodar em macOS.

Especificações exatas: nenhuma. O texto descreve a distância de uso como "tipicamente dentro de cerca de 3 pés (about 3 feet)" do dispositivo, mas não traz medidas de interface.

Diferenças por plataforma: recursos de sistema citados como próprios do iPadOS: Multitasking, Widgets, Drag and drop. O texto menciona explicitamente a transição do app para rodar em macOS como algo a suportar.

Ligações com outros artigos: cita Apple Design Resources e a iPadOS Pathway.

<!-- visual:designing-for-ipados -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura repete o mesmo tratamento da folha de iOS: retângulo de cantos arredondados em degradê verde, grade pontilhada e círculo guia central, sem texto sobreposto (img 0435).
- O iPad aparece em traço verde escuro vazado, como um retângulo horizontal de cantos arredondados com uma barra curta perto da borda inferior, que faz o papel do indicador de home (img 0435).
- O contorno do aparelho está inscrito no círculo guia, e o centro do iPad coincide com o cruzamento das linhas da grade, o mesmo encaixe usado para o iPhone (img 0435).
- A proporção do retângulo é mais próxima do quadrado do que a do iPhone, ou seja, a grade comum é mantida e só o formato muda para refletir a diferença real entre os dois aparelhos (img 0435).
- A folha traz apenas a versão clara da ilustração (img 0435).
<!-- /visual:designing-for-ipados -->

## Designing for macOS (slug: designing-for-macos)

O que governa: as características do Mac (tela grande, uso estacionário, múltiplos modos de entrada, múltiplos apps abertos) e as práticas recomendadas para um app se sentir em casa no macOS.

Por que: o Mac é usado de forma estacionária, com viewing distance maior e várias janelas e apps abertos ao mesmo tempo; a Apple deriva as práticas recomendadas dessa realidade de uso (mais espaço, mais precisão de entrada, mais tempo de concentração).

Faça e evite:
- Aproveite telas grandes para mostrar mais conteúdo com menos níveis aninhados e menos necessidade de modalidade, mantendo densidade de informação confortável.
- Deixe a pessoa redimensionar, ocultar, mostrar e mover janelas conforme seu estilo de trabalho; suporte modo tela cheia para um contexto livre de distrações.
- Use a barra de menu (menu bar) para dar acesso fácil a todos os comandos do app.
- Suporte modos de entrada de alta precisão para seleções e edições pixel-perfect.
- Trate atalhos de teclado (keyboard shortcuts) para acelerar ações e permitir fluxos de trabalho só de teclado.
- Suporte personalização: toolbars customizáveis, janelas configuráveis com as views mais usadas, escolha de cores e fontes na interface.

Especificações exatas: nenhum número técnico de interface; a distância de uso típica é descrita qualitativamente como "cerca de 1 a 3 pés".

Diferenças por plataforma: recursos de sistema próprios do macOS citados: menu bar, file management, going full screen, Dock menus. Menciona a possibilidade de estender o espaço de trabalho conectando telas adicionais, incluindo o iPad.

Ligações com outros artigos: cita Apple Design Resources e a macOS Pathway.

<!-- visual:designing-for-macos -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura segue a mesma composição das demais páginas de plataforma: retângulo verde, grade pontilhada e círculo guia central (img 0456).
- O Mac é a exceção de preenchimento: a forma é sólida em verde escuro, enquanto iOS e iPadOS usam contorno vazado (img 0456).
- O desenho é um monitor de mesa, com tela retangular, pescoço curto e base curva embaixo, lembrando um iMac ou display com suporte (img 0456).
- Só a tela fica inscrita no círculo guia; pescoço e base descem para fora dele, o que mostra a proporção circular aplicada à "cabeça" do ícone e não ao objeto inteiro (img 0456).
- A folha traz apenas a versão clara da ilustração (img 0456).
<!-- /visual:designing-for-macos -->

## Designing for tvOS (slug: designing-for-tvos)

O que governa: as características do Apple TV (tela grande à distância, controle remoto e outras entradas, uso imersivo) e as práticas recomendadas para experiências que "se sintam em casa" no tvOS.

Por que: as pessoas ficam tipicamente a vários pés de distância da TV (frequentemente 8 pés ou mais) e usam controle remoto, controle de jogo, voz ou apps em outros dispositivos; a Apple deriva daí a ênfase no sistema de foco (focus system), em artes de borda a borda e em animações fluidas para uma experiência cinematográfica legível à distância.

Faça e evite:
- Suporte interações poderosas e agradáveis por meio dos gestos fluidos e familiares do Siri Remote.
- Abrace o sistema de foco do tvOS, deixando-o destacar e expandir suavemente os itens na tela conforme a pessoa navega entre eles.
- Entregue artes de borda a borda, animações sutis e fluidas, e áudio envolvente, para uma experiência cinematográfica clara, legível e cativante mesmo à distância.
- Facilite o suporte a múltiplos usuários: login fácil e pouco frequente, tratamento de login compartilhado, e troca automática de perfil quando o espectador atual muda.

Especificações exatas: a distância típica de uso é descrita qualitativamente ("often 8 feet or more"), sem outros números de interface.

Diferenças por plataforma: recursos de sistema próprios do tvOS: integração com o app TV, SharePlay, Top Shelf, contas de provedor de TV. Menciona picture-in-picture como forma de acompanhar um app ou vídeo alternativo simultaneamente.

Ligações com outros artigos: cita Apple Design Resources e a tvOS Pathway. Registro de mudança (change log) de 14 de setembro de 2022: refinamento da orientação de suporte multiusuário.

<!-- visual:designing-for-tvos -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura usa a mesma composição das outras páginas de plataforma: retângulo verde, grade pontilhada e círculo guia (img 0457).
- A televisão é desenhada em traço verde escuro vazado, como um retângulo largo de cantos arredondados com uma pequena barra horizontal abaixo, que representa o pé ou suporte (img 0457).
- O retângulo da tela fica inscrito no círculo guia e a barra do suporte fica fora dele, na parte inferior, a mesma lógica do Mac, porém com contorno vazado em vez de forma sólida (img 0457).
- O contorno vazado alinha a TV ao esquema de iOS, iPadOS e iPhone Duo, e o suporte é o elemento que a separa visualmente de um tablet ou celular (img 0457).
- A folha traz apenas a versão clara da ilustração (img 0457).
<!-- /visual:designing-for-tvos -->

## Designing for visionOS (slug: designing-for-visionos)

O que governa: as características do Apple Vision Pro (espaço 3D infinito, imersão, passthrough, áudio espacial, entrada por olhos e mãos, ergonomia e acessibilidade) e as práticas recomendadas para criar experiências espaciais confortáveis e familiares.

Por que: no visionOS, o dispositivo traz o conteúdo até a pessoa em vez de forçar a pessoa a se mover até o conteúdo, e a pessoa depende inteiramente das câmeras do dispositivo para ver tudo, real e virtual; por isso a Apple trata o conforto visual e físico como prioridade máxima, e recomenda encontrar o nível mínimo de imersão que sirva a cada momento-chave do app, em vez de assumir que tudo precisa ser totalmente imersivo.

Faça e evite:
- Aproveite os recursos únicos do Apple Vision Pro (espaço, áudio espacial, imersão), integrando passthrough e entrada espacial de olhos e mãos de forma que pareçam nativas do dispositivo.
- Para cada momento-chave do app, escolha o nível mínimo de imersão adequado; nem todo momento precisa ser totalmente imersivo.
- Prefira janelas (windows) para experiências contidas e centradas em UI, com controles familiares; a pessoa pode reposicionar janelas livremente e o sistema usa escala para manter o conteúdo legível perto ou longe.
- Priorize o conforto: exiba conteúdo dentro do campo de visão da pessoa, posicionado em relação à cabeça, evitando que a pessoa precise virar a cabeça ou mudar de posição para interagir.
- Evite conteúdo visual que seja opressivo, abrupto, rápido demais, ou que não tenha um quadro de referência estacionário.
- Suporte interações com as mãos em repouso, no colo ou ao lado do corpo.
- Se suportar gestos diretos, garanta que o conteúdo interativo não esteja longe demais e que a pessoa não precise interagir com ele por períodos prolongados.
- Evite incentivar movimento excessivo durante experiências totalmente imersivas.
- Ajude as pessoas a compartilhar atividades exibindo Personas espaciais de outros participantes, dando a sensação de estarem juntos no mesmo espaço.

Especificações exatas: o texto não traz medidas numéricas (nem graus, nem metros); a única unidade citada é qualitativa (13 anos de idade como requisito mínimo de ajuste/uso do dispositivo, mencionado no aviso de segurança).

Diferenças por plataforma: específico do visionOS. Conceitos próprios descritos: Shared Space (múltiplos apps lado a lado por padrão), Full Space (um único app, podendo mostrar conteúdo 3D misturado ao ambiente, abrir um portal para outro lugar, ou entrar em outro mundo), controle de passthrough pela Digital Crown. Tecnologias de acessibilidade citadas: VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer.

> IMPORTANTE (aviso de segurança citado no texto): o Apple Vision Pro não deve ser usado ao dirigir veículo ou operar máquina pesada, nem ao se mover em ambientes potencialmente perigosos como varandas, ruas ou escadas; o dispositivo é projetado para ser ajustado e usado apenas por pessoas com 13 anos ou mais.

Ligações com outros artigos: cita Apple Design Resources, a visionOS Pathway e "Creating your first visionOS app". Change log: 2 de fevereiro de 2024 (link para o guia do usuário do Apple Vision Pro), 12 de setembro de 2023 (atualização da arte de abertura), 21 de junho de 2023 (página nova).

<!-- visual:designing-for-visionos -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura mantém a composição comum às páginas de plataforma: retângulo verde, grade pontilhada e círculo guia (img 0458).
- O Apple Vision Pro é desenhado em traço verde escuro vazado, mais espesso que o das outras folhas de abertura (img 0458).
- A forma é uma curva contínua parecida com óculos de mergulho: dois arcos superiores unidos e uma reentrância central embaixo, no lugar do encaixe do nariz (img 0458).
- A viseira inteira cabe dentro do círculo guia e ocupa praticamente todo o diâmetro dele, mais do que os ícones retangulares dos outros aparelhos (img 0458).
- Entre as aberturas registradas no lote, é o único ícone de forma orgânica, sem ângulos retos, que parte do formato físico do aparelho e não de uma tela retangular (img 0458).
- A folha traz apenas a versão clara da ilustração (img 0458).
<!-- /visual:designing-for-visionos -->

## Designing for watchOS (slug: designing-for-watchos)

O que governa: as características do Apple Watch (tela pequena no pulso, uso rápido e frequente, Digital Crown, Always On) e as práticas recomendadas para interações "glanceable" (de relance) e especializadas.

Por que: como o relógio é usado no pulso, em olhadas rápidas ao longo do dia (interações que muitas vezes duram menos de um minuto), e as pessoas frequentemente usam complications, notificações e Siri mais do que o próprio app, a Apple recomenda um design streamlined, com hierarquia rasa de navegação e conteúdo acionável antecipado às necessidades da pessoa.

Faça e evite:
- Suporte interações rápidas, glanceable, de tela única, que entreguem informação crítica de forma sucinta e permitam ações direcionadas com um gesto ou dois.
- Minimize a profundidade da hierarquia de navegação; use a Digital Crown para navegação vertical (rolagem ou troca entre telas).
- Personalize a experiência antecipando proativamente as necessidades da pessoa, usando dados do dispositivo para conteúdo acionável relevante no momento ou muito em breve.
- Use complications para entregar dados e gráficos relevantes, potencialmente dinâmicos, direto no mostrador (watch face), visíveis a cada erguer de pulso e tocáveis para ir direto ao app.
- Use notificações para entregar informação pontual e de alto valor, permitindo ações importantes sem abrir o app.
- Use plano de fundo (cor) para transmitir informação de apoio útil, e materiais para ilustrar hierarquia e senso de lugar.
- Projete o app para funcionar de forma independente, complementando notificações e complications com detalhes e funcionalidade adicionais.

Especificações exatas: nenhum número de interface; a distância de uso é descrita qualitativamente como "usualmente não mais que um pé" (no more than a foot away).

Diferenças por plataforma: específico do watchOS. Recursos de sistema citados: Complications, Notifications, Always On, Watch faces. Entradas específicas citadas: Digital Crown, Action button, GPS, sensores de oxigênio no sangue e função cardíaca, altímetro, acelerômetro, giroscópio.

Ligações com outros artigos: cita Apple Design Resources e a watchOS Pathway. Change log de 5 de junho de 2023: reforço da orientação sobre experiência glanceable e foco, e ênfase na importância da Digital Crown na navegação.

<!-- visual:designing-for-watchos -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura usa a mesma composição das outras páginas de plataforma: retângulo verde, grade pontilhada e círculo guia (img 0459).
- O Apple Watch aparece em traço verde escuro vazado, como caixa retangular de cantos bem arredondados, no mesmo esquema de contorno de iPhone, iPad, iPhone Duo e TV (img 0459).
- Na borda direita da caixa há duas pequenas saliências que representam a Digital Crown e o botão lateral (img 0459).
- Duas alças mais estreitas saem para cima e para baixo da caixa, indicando o início da pulseira (img 0459).
- Só o corpo da caixa fica inscrito no círculo guia; as alças ficam fora dele, no topo e na base da composição (img 0459).
- Saliências laterais e alças são elementos que não aparecem em nenhum outro ícone de abertura do lote (img 0459).
- A folha traz apenas a versão clara da ilustração (img 0459).
<!-- /visual:designing-for-watchos -->

## Designing for games (slug: designing-for-games)

O que governa: como criar ou adaptar um jogo para as plataformas Apple, cobrindo entrada no jogo, legibilidade em cada tela, interações intuitivas, inclusão e adoção de tecnologias Apple (Game Center, iCloud, haptics, Spatial Audio).

Por que: a Apple organiza a orientação em torno da experiência do jogador desde a instalação (quanto tempo até poder jogar) até a inclusão e a integração com o ecossistema; a lógica repetida é reduzir atrito (menos espera, bons padrões, ensino pela prática) e maximizar quem consegue jogar (acessibilidade, alternativas a controle físico, evitar estereótipos).

Faça e evite, por seção:

Jump into gameplay
- Deixe a pessoa jogar assim que a instalação terminar; inclua o máximo de conteúdo jogável possível na instalação inicial mantendo o tempo de download em 30 minutos ou menos; baixe conteúdo adicional em segundo plano.
- Forneça boas configurações padrão a partir de informações do dispositivo (resolução, reconhecimento automático de acessórios e controles, configurações de acessibilidade da pessoa); suporte os métodos de interação mais comuns da plataforma.
- Ensine através do jogo: integre configuração e onboarding em um tutorial jogável; se houver tutorial escrito, ofereça-o como referência opcional, não como pré-requisito.
- Adie pedidos (de sensores, dados pessoais como hand-tracking) até o momento certo, integrando o pedido ao cenário que o exige; peça avaliação ou review só depois que a pessoa já tiver passado tempo de qualidade com o jogo.

Look stunning on every display
- Garanta que o texto seja sempre legível, com bom contraste contra o fundo e usando pelo menos o tamanho mínimo recomendado em cada plataforma.
- Garanta que os botões sejam sempre fáceis de usar, respeitando o tamanho mínimo de botão recomendado por plataforma.
- Prefira texturas e gráficos independentes de resolução; se não for possível, combine a resolução do jogo à do dispositivo. Em visionOS, prefira arte vetorial que continue boa quando o sistema escala dinamicamente por distância e ângulo.
- Integre os recursos do dispositivo (cantos arredondados, câmera) no layout, confiando nas safe areas fornecidas pela plataforma quando possível.
- Garanta que os menus do jogo se adaptem a diferentes proporções de tela (aspect ratios) e permaneçam legíveis e fáceis de usar em todo dispositivo (e em ambas orientações no iPhone e iPad, se suportadas); prefira layouts dinâmicos com restrições relativas em vez de layouts fixos.
- Projete para a experiência em tela cheia (full screen).

Enable intuitive interactions
- Suporte o método de interação padrão de cada plataforma, prestando atenção especial ao tamanho de controles e ao comportamento de menus ao portar de um contexto baseado em ponteiro para um baseado em toque.
- Suporte controles de jogo físicos, mas ofereça também alternativas, já que nem todo jogador consegue usar um controle físico.
- Ofereça controles de jogo por toque que abracem a experiência de tela sensível ao toque no iPhone e iPad, permitindo interação direta com elementos do jogo e controles virtuais sobrepostos ao conteúdo.

Welcome everyone
- Priorize a perceptibilidade: garanta que o conteúdo do jogo possa ser percebido por visão, audição ou toque; evite depender só de cor para transmitir um detalhe importante, e ofereça legendas descritivas em cutscenes.
- Ajude jogadores a personalizar a experiência (tamanho de tipo, mapeamento de controles, intensidade de movimento, balanço de som), aproveitando as tecnologias de acessibilidade nativas da Apple.
- Dê aos jogadores ferramentas para se representarem: suporte o espectro de autoidentidade em avatares, nomes e descrições.
- Evite estereótipos em histórias e personagens; revise o jogo para identificar e remover vieses e estereótipos, e trate referências a culturas e idiomas reais com respeito.

Adopt Apple technologies
- Integre o Game Center para descoberta entre dispositivos, conexão com amigos, progresso, conquistas, leaderboards, desafios e multiplayer.
- Suporte GameSave para permitir retomar o jogo exatamente de onde parou em outro dispositivo, via iCloud.
- Suporte haptics (Core Haptics) para o jogador sentir a ação, combinando opcionalmente com áudio customizado.
- Use Spatial Audio para imergir o jogador na trilha sonora do jogo, adaptando-se automaticamente ao dispositivo atual.
- Aproveite outras tecnologias Apple (realidade aumentada, machine learning, HealthKit, localização, câmera, microfone) para mecânicas de jogo únicas.

Especificações exatas:
- Tempo de download inicial recomendado: 30 minutos ou menos.
- Tamanho de texto padrão e mínimo por plataforma: iOS/iPadOS 17 pt (padrão) / 11 pt (mínimo); macOS 13 pt / 10 pt; tvOS 29 pt / 23 pt; visionOS 17 pt / 12 pt; watchOS 16 pt / 12 pt.
- Tamanho de botão padrão e mínimo por plataforma: iOS/iPadOS 44x44 pt (padrão) / 28x28 pt (mínimo); macOS 28x28 pt / 20x20 pt; tvOS 66x66 pt / 56x56 pt; visionOS 60x60 pt / 28x28 pt; watchOS 44x44 pt / 28x28 pt.
- Proporções de tela (aspect ratios) citadas como exemplos a suportar: 16:10, 19.5:9, 4:3.

Diferenças por plataforma: tabela de métodos de interação padrão e adicionais por plataforma: iOS (padrão: Touch; adicional: Game controller), iPadOS (padrão: Touch; adicionais: Game controller, keyboard, mouse, trackpad, Apple Pencil), macOS (padrão: Keyboard, mouse, trackpad; adicional: Game controller), tvOS (padrão: Remote; adicionais: Game controller, keyboard, mouse, trackpad), visionOS (padrão: Touch; adicionais: Game controller, keyboard, mouse, trackpad, spatial game controller), watchOS (padrão: Touch; adicionais: nenhum). Suporte a controle de jogo físico existe em todas as plataformas exceto watchOS. Em macOS, iOS e iPadOS, tela cheia oculta outros apps e parte da UI do sistema; em visionOS, um jogo em Full Space pode envolver completamente a pessoa.

Ligações com outros artigos: cita explicitamente Designing for iOS, Designing for iPadOS, Designing for macOS, Designing for tvOS, Designing for visionOS, Designing for watchOS, além de Loading, Settings, Onboarding, Privacy, Ratings and reviews, Typography, Layout, Going full screen, In-game menus, Game controls, Gestures, Pointing devices, Physical controllers, Touch controls, Text sizes, Color and effects, Motion, Interactions, Buttons, Accessibility, Inclusion, Game Center, GameKit, iCloud, In-app purchase, Playing haptics, Core Haptics, Spatial Audio, Technologies, Games Pathway, "Adapting your game interface for smaller screens", "Positioning content relative to the safe area", Apple Design Resources. Change log: 9 de junho de 2025 (orientação atualizada para controles touch-based e Game Center); 10 de junho de 2024 (página nova).

<!-- visual:designing-for-games -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 de 1), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura é um ícone de controle de videogame sobre fundo em degradê verde, que vai do teal à esquerda ao verde limão à direita (img 0433).
- O corpo do controle é um contorno em traço grosso verde escuro, em forma de "A" arredondado com as duas alças curvadas para baixo (img 0433).
- O controle é reduzido a três elementos reconhecíveis: contorno do corpo, cruz direcional à esquerda e par de botões circulares à direita, um menor em cima e um maior embaixo; não há gatilhos, detalhes de empunhadura nem textura (img 0433).
- Sobre toda a imagem corre uma grade pontilhada com linhas retangulares e diagonais, mais um círculo e um X diagonal centralizados; o centro do controle coincide com o centro do quadro e as alças acompanham as diagonais do retângulo (img 0433).
- As notas registram o mesmo tipo de grade de construção na página dark-mode (img 0411), o que indica um tratamento padrão das ilustrações de abertura e não um recurso exclusivo desta página (img 0433).
- A folha traz apenas a versão clara da ilustração (img 0433).
<!-- /visual:designing-for-games -->

## Designing for iPhone Duo (slug: designing-for-iphone-duo)

O que governa: como projetar para o iPhone Duo, dispositivo de duas telas (interna e externa) com dobradiça central, cobrindo anatomia do dispositivo, poses, layouts dinâmicos, regiões reservadas, split views, arrangement views e o posicionamento vertical de toolbars, tab bars e controles de navegação.

Por que: o iPhone Duo tem uma variedade de tamanhos de tela e poses possíveis (dobrado, aberto, em pé), então a Apple prioriza um layout adaptável sobre layouts customizados para cada pose; a lógica central é usar size classes e containers que se adaptam automaticamente, em vez de reinventar o app a cada redimensionamento, preservando a familiaridade e a posição relativa dos controles conforme a pessoa move o dispositivo entre poses.

Anatomia
- O dispositivo tem tela externa (outer) e tela interna (inner). Com o dispositivo fechado, a pessoa interage com a tela externa, e o sistema posiciona toolbars e tab bars na lateral para maximizar o espaço vertical para conteúdo. Os controles permanecem na lateral também quando o dispositivo abre em paisagem, para manter a experiência consistente entre as telas.
- Uma dobradiça central suporta várias formas de segurar e posicionar o dispositivo, e também impacta o espaço disponível para o conteúdo conforme o dispositivo se dobra.
- A câmera frontal externa fica no canto, sempre visível, alinhada verticalmente com os controles laterais. A câmera interna fica atrás da tela e permanece oculta até ser ativada.

Device poses
- As pessoas seguram e apoiam o iPhone Duo de várias formas: parcialmente dobrado como um livro, apoiado sobre uma superfície, ou em pé sobre as bordas.
- Suportar as várias poses não significa desenhar um layout customizado para cada uma: em vez disso, usar size classes para que o app se adapte naturalmente ao mudar de tamanho. Um layout de largura compacta para a tela externa e um layout de largura regular para a tela interna dão a base para toda pose.

Faça e evite:
- Construa o app para redimensionar: use size classes, layout margins e safe area insets para dispor controles e conteúdo; evite larguras fixas e dependências específicas de uma tela.
- Crie uma experiência consistente entre as telas: mantenha funcionalidade e estado dos elementos iguais entre as duas telas, preservando a hierarquia de informação do app, mas mostrando um nível adicional de hierarquia na tela interna maior quando fizer sentido para o conteúdo (exemplo citado: o Mail mostra lista de e-mails OU um e-mail quando fechado, e ambos lado a lado quando aberto).
- Mantenha a mesma funcionalidade entre as poses do dispositivo: controles podem transbordar (overflow) e conteúdo pode mudar de posição ou tamanho conforme a interface se adapta, mas dê acesso aos mesmos controles e conteúdo independentemente de como a pessoa segura ou vê o dispositivo.
- Siga o layout vertical do sistema para toolbars, tab bars e controles de navegação: como a tela externa é mais larga e mais baixa que a de outros iPhones, o sistema move controles para a lateral para preservar espaço vertical e refletir a assimetria da tela; na tela interna, os controles permanecem na lateral em paisagem para preservar uma altura vertical contínua.
- Torne o jogo jogável em toda pose do dispositivo: pode travar em orientação retrato ou paisagem, mas deve preencher a tela conforme a pose muda; mantenha tamanhos de texto e controle o mais consistentes possível ao redimensionar; prefira mudar a proporção da tela (aspect ratio) em vez de usar letterbox ou pillarbox; se não puder evitar, adicione arte na área de padding para a experiência parecer tela cheia.

Dynamic layouts
- Contabilize uma variedade de configurações de hardware e software; construa layouts com layout margins e safe area insets, evitando larguras fixas ou qualquer coisa amarrada a uma tela específica.

Reserved regions (regiões reservadas), além das safe areas padrão:
- A região da câmera frontal externa: sempre presente, expande-se para a Dynamic Island em Live Activities; quando os controles estão na lateral, o sistema contabiliza automaticamente essa região.
- A região da câmera frontal interna: presente só quando a câmera está ativa; quando inativa, a câmera não é visível; quando ativa, a UI se afasta para indicar a presença da câmera.
- A região de dobra (folding region): condicional, conforme o uso do dispositivo; quando parcialmente aberto, essa região divide a tela interna em múltiplas regiões utilizáveis, excluindo a região central conforme a tela se dobra.
- Muitos componentes do sistema se adaptam automaticamente às regiões reservadas (alertas, menus de contexto, sheets se movem para contabilizar a dobra; componentes maiores como Split views adaptam largura e margens das colunas para casar com a simetria da tela interna). Para componentes customizados, existem APIs de reserved region para reposicionar conteúdo para longe dessas regiões.
- Adapte o layout quando o dispositivo se dobra: prefira um container de layout que se adapte automaticamente (exemplo citado: split view do Notes, que ajusta a largura de cada painel para permanecer claramente visível conforme o dispositivo dobra); em um layout de grade, prefira número par de colunas para o conteúdo se dividir de forma limpa.
- Evite mudanças extremas de layout conforme a pessoa dobra o dispositivo: mova só o necessário para manter elementos visíveis e fáceis de tocar; controles que desaparecem ou mudam drasticamente ficam mais difíceis de encontrar e acompanhar.

Split views
- Na tela interna, a split view expande; na tela externa, colapsa para um único painel, da mesma forma que se adapta entre ambientes regular e compacto em outros iPhones. Quando construída com componentes padrão, a split view se adapta automaticamente às regiões reservadas, ajustando largura e margens conforme a dobra.

Arrangement views
- Um arrangement view é um container de layout que guarda duas views dentro de si (uma primária e uma secundária) e as organiza dinamicamente conforme tamanho de tela, orientação e regiões reservadas.
- Dois tipos: split (divide a área horizontalmente quando o arrangement é mais largo que alto, e verticalmente quando é mais alto que largo) e overlay (posiciona a view primária sobre a secundária; quando a tela está parcialmente dobrada, as views se movem para ocupar cada lado, caso contrário a primária fica sobre a secundária).
- É possível limitar quais eixos um split arrangement usa, e colapsar a view secundária em um overlay arrangement quando não for necessário mostrá-la.
- Considere um arrangement view quando o layout já se parece com um: um layout que posiciona duas views lado a lado ou uma sobre a outra (como um HStack ou VStack) se traduz diretamente para um split arrangement; um layout que sobrepõe uma view à outra (como um ZStack) se traduz para um overlay arrangement.
- Mantenha a navegação fora dos arrangement views: eles organizam conteúdo mas não tratam navegação, então containers de navegação (navigation split views, tab views) devem ficar ao redor, não dentro, do arrangement view.

Vertical controls
- No iPhone Duo, toolbars, tab bars e controles de navegação que normalmente ficam no topo e na base da tela se movem para a lateral, preservando espaço vertical para o conteúdo e mantendo os controles ao alcance. Exceção: a tela interna em retrato, que tem espaço vertical suficiente para manter barras horizontais padrão.
- Controles na lateral incluem elementos do sistema e do app: Dynamic Island, status bar, toolbar (incluindo botões de navegação) e tab bar.
- Quando dois apps compartilham a tela interna com Split View multitasking, cada um posiciona seus controles na própria borda externa (o app à esquerda tem controles à esquerda).
- Como os controles no eixo vertical ficam alinhados ao hardware, mantêm a mesma posição relativa à câmera na tela externa, e permanecem do mesmo lado em idiomas da direita para a esquerda.
- Contabilize a assimetria nos layouts: como os controles ficam em uma borda, o espaço para conteúdo é assimétrico; use safe areas para garantir que controles não cubram o conteúdo, incluindo controles da borda oposta (como quando dois apps compartilham a tela interna).
- Mantenha os controles consistentes entre as poses do dispositivo: como nem toda pose posiciona os controles verticalmente na lateral, e o espaço disponível varia, é importante manter as posições relativas dos controles o mais parecidas possível para a pessoa não precisar reaprender onde as ações estão.
- Siga a ordem padrão de posicionamento dos itens de toolbar: reserve o topo do eixo vertical para controles de navegação primários (como Back ou Close), seguidos de ações proeminentes (como Done); mantenha os demais itens em seus agrupamentos originais, com espaço vertical entre itens vindos da barra superior e da inferior para mantê-los distintos.
- Priorize os itens de toolbar mais usados para mantê-los facilmente disponíveis: itens transbordam de baixo para cima por padrão; é possível atribuir uma prioridade de visibilidade a cada item para mudar essa ordem, começando por grupos inteiros e depois itens individuais dentro de um grupo.
- Preserve primeiro as ações mais usadas (como Compose no Mail ou New Note no Notes), e mantenha visíveis por mais tempo os controles que transmitem status importante (como itens com badges).
- Em geral, não sobrescreva o posicionamento padrão de barras: a posição dos controles no eixo vertical é um dos padrões centrais do iPhone Duo.
- Considere usar a largura total da tela para interfaces onde barras não são necessárias, especialmente layouts visuais e imersivos que não rolam, desde que nada entre em conflito com a Dynamic Island ou a status bar (exemplo citado: Calculator ocupa a largura total da tela). É possível combinar as duas abordagens, deixando uma imagem de fundo ou cabeçalho ocupar a largura total enquanto conteúdo rolável fica com inset.
- Agrupe itens de toolbar relacionados em vez de espaçá-los manualmente: grupos criados com ToolbarItemGroup (SwiftUI) ou UIBarButtonItemGroup (UIKit) fornecem espaço entre itens e outros grupos automaticamente, e se adaptam conforme o espaço disponível muda.
- Posicione controles perto do conteúdo que eles afetam: quando controles pertencem a uma área de conteúdo diferente da borda de trás (trailing edge), mantenha-os com aquela área em vez de movê-los para a lateral (exemplo citado: controles que afetam a lista de e-mails no Mail ficam acima do painel leading, não na lateral).
- Forneça título e símbolo para cada item de toolbar que não seja só texto: isso permite que o sistema escolha a representação certa para o contexto; inclua um título mesmo quando o item mostra um símbolo, porque o sistema usa o título em menus de overflow e formas expandidas.
- Mantenha botões baseados em texto ao mínimo: rótulos que incluem texto ficam em uma barra horizontal, então prefira um símbolo sempre que possível.
- Quando o espaço é limitado, preserve a toolbar ou a tab bar conforme a experiência oferecida pela view: em experiências focadas em navegação, mova itens de toolbar para o menu de overflow para manter a tab bar e os destinos primários acessíveis (comportamento padrão de compressão de barra); em experiências orientadas a tarefa, minimize a tab bar para preservar as ações de toolbar centrais à conclusão da tarefa.
- Use o menu de overflow do sistema: se o app tiver seu próprio menu de overflow, mova essas ações para o menu do sistema para que a pessoa encontre tudo em um só lugar; reserve o símbolo de reticências (ellipsis) para overflow, e dê a outros menus um símbolo distinto.

Especificações exatas: o artigo não traz nenhum número de pt, px, ms ou proporção; todas as diretrizes são qualitativas e estruturais (posições, ordens, prioridades).

Diferenças por plataforma: este artigo é inteiramente específico do dispositivo iPhone Duo, uma variação do iOS; reforça que os padrões e boas práticas de Designing for iOS continuam se aplicando.

Ligações com outros artigos: cita Designing for iOS, Dynamic layouts, Layout, Apple Design Resources, Vertical controls, Designing for games, Split views, Toolbars, além de referências de API para desenvolvedores (safeAreaInsets em SwiftUI e UIKit, NavigationSplitView, UISplitViewController, ToolbarItemVisibilityPriority, UIBarButtonItemVisibilityPriority, Label, UIBarButtonItem, ToolbarItemGroup, UIBarButtonItemGroup, ToolbarOverflowMenu, additionalOverflowItems). Change log: 9 de setembro de 2026, página nova, introduzindo os conceitos fundamentais de design para o iPhone Duo (poses do dispositivo, layouts dinâmicos entre as duas telas, toolbars e tab bars no eixo vertical).

<!-- visual:designing-for-iphone-duo -->
### O que as ilustrações mostram
Base: 5 folhas de ilustrações vistas (5 de 5), todos os códigos conferidos, com 20 imagens, todas em versão clara; nenhum vídeo listado para a página.
- O ícone de abertura mantém a composição verde com grade e círculo guia, mas troca o retângulo único dos outros aparelhos por um retângulo vertical com uma segunda aba saindo da borda superior direita, como capa aberta, e um pequeno círculo preenchido no canto superior direito (img 0436).
- A Tela de Início muda de densidade entre as telas: a externa, estreita, tem dois widgets no topo e grade de quatro colunas por quatro linhas; a interna, quase quadrada, passa a seis colunas por quatro linhas. A coluna de atalhos (telefone, Safari, Mensagens, Música) fica fixa na borda direita, fora da grade, nas duas telas (img 0437, img 0438).
- Os diagramas de anatomia usam contorno preto com rótulos: fechado, a câmera é um círculo no canto superior direito e a dobradiça uma linha vertical à esquerda (img 0439); na tela interna, a dobradiça vira faixa vertical azul clara no centro e a câmera fica no quadrante superior direito, perto da dobra (img 0440).
- As poses aparecem como seis silhuetas em traço preto fino, lado a lado e sem conteúdo desenhado: fechado na vertical, meio aberto em V como livro apoiado, aberto quase a 180 graus, livro de pé, fechado outra vez e posição de laptop com dobra na base (img 0441).
- No Mail, a tela externa mostra um único e-mail aberto com a barra de ícones empilhada na borda direita (voltar, setas, lixeira, pasta, responder, compor) (img 0442); na interna, o mesmo e-mail divide a tela com a lista Inbox à esquerda, acrescentando um nível de hierarquia (img 0443).
- As regiões reservadas são marcadas por cor e rótulo: círculo azul escuro "Outer camera region" no canto da tela externa (img 0444); na interna, faixa azul clara "Folding region" no centro com a "Inner camera region" junto dela, isto é, a câmera interna fica dentro da região de dobra (img 0445).
- No Notes, com o aparelho todo aberto a coluna da lista é visivelmente mais estreita que a do conteúdo (img 0446); parcialmente dobrado, as duas colunas passam a ter a mesma largura (img 0447).
- Os arrangement views são desenhados em duas cores: no split, metade azul clara "Secondary view" e metade roxa clara "Primary view", sem sobreposição (img 0448); no overlay, a secundária ocupa a tela toda e a primária é um retângulo menor centralizado por cima, sem tocar as bordas (img 0449).
- Na tela externa, a borda direita empilha de cima para baixo Dynamic Island, status bar, toolbar com dois botões redondos (voltar e mais opções) e tab bar com três ícones, cada um apontado por linha de chamada (img 0450).
- Os controles ficam presos ao conteúdo que servem: em Split View, cada app usa uma faixa azul clara de controles na própria borda externa, sem borda compartilhada no centro (img 0451); no Mail, o painel leading leva seus controles no topo e o trailing na borda vertical direita (img 0453).
- A Calculadora redistribui os mesmos botões: quatro colunas por cinco linhas no iPhone comum, cinco colunas por quatro linhas na tela externa, mais larga e baixa (img 0452).
- Em paisagem na tela externa, toolbar e tab bar nunca aparecem cheias ao mesmo tempo: ou os itens da toolbar recolhem num botão de reticências abaixo do voltar e a tab bar fica completa (img 0454), ou a toolbar aparece expandida e a tab bar recolhe num único botão (img 0455).
<!-- /visual:designing-for-iphone-duo -->

## O que este grupo revela sobre o jeito Apple

1. A Apple deriva prática de observação de uso real, não de estética abstrata: cada artigo de plataforma (design-principles à parte) começa descrevendo display, ergonomia, inputs e padrões de interação antes de chegar às "best practices", a regra de design é sempre justificada pela forma como o corpo e a atenção da pessoa se relacionam com o dispositivo (designing-for-ios, designing-for-ipados, designing-for-macos, designing-for-tvos, designing-for-visionos, designing-for-watchos).

2. Adaptação automática é preferida a customização manual por contexto: em vez de pedir um layout específico por pose, tamanho ou dispositivo, a orientação recorrente é usar mecanismos que se adaptam sozinhos (size classes, safe areas, dynamic layouts, arrangement views no iPhone Duo; Split View e multitasking no iPadOS; resizing de janelas no macOS) (designing-for-ipados, designing-for-iphone-duo, designing-for-macos).

3. Consistência de posição e comportamento entre contextos é tratada como requisito de usabilidade, não luxo: manter controles no mesmo lugar relativo entre telas, poses ou modos evita que a pessoa precise reaprender a interface (designing-for-iphone-duo, designing-for-watchos, designing-for-visionos).

4. Permissão e coleta de dados são tratadas como decisão de design, não só de política: o momento e a justificativa de um pedido de permissão são parte do fluxo de UX, incluindo em jogos (designing-for-games, design-principles na seção Responsibility).

5. Cada plataforma tem uma "unidade de tempo de atenção" característica que molda a orientação: iPhone (minutos a mais de uma hora, trocando entre apps), iPad (de ações rápidas a horas imersivas), Mac (minutos a horas de concentração), Apple TV (horas imersivas, mas com picture-in-picture), Apple Watch (interações de menos de um minuto, várias vezes ao dia), visionOS (imersão graduável por momento), a duração e a frequência do uso justificam diretamente a densidade de informação recomendada (designing-for-ios, designing-for-ipados, designing-for-macos, designing-for-tvos, designing-for-watchos, designing-for-visionos).

6. O conforto físico é elevado a princípio de design explícito, não implícito, especialmente onde o risco é maior: visionOS dedica uma seção inteira e um aviso formal de segurança ao conforto e à prevenção de uso em contextos perigosos (designing-for-visionos), o que não aparece com a mesma intensidade em nenhuma outra plataforma do grupo.

7. Tamanhos mínimos de texto e de alvo de toque são padronizados por plataforma, não universais: o mesmo conceito (legibilidade, alcançabilidade) resulta em números diferentes por dispositivo, refletindo a distância e o método de interação típicos de cada tela (designing-for-games, que tabula texto e botões por plataforma, em coerência direta com as ergonomias descritas em designing-for-ios, designing-for-ipados, designing-for-macos, designing-for-tvos, designing-for-visionos, designing-for-watchos).

8. Os oito princípios de design-principles funcionam como uma "gramática" que reaparece, parafraseada, em cada artigo de plataforma: Agency e a recuperação de erros aparecem como "let people resize/hide/show windows" e "recover from mistakes" no macOS; Flexibility aparece como suporte a múltiplos modos de entrada em toda plataforma; Simplicity aparece como "limitar controles na tela" no iOS e "minimizar hierarquia" no watchOS (design-principles, designing-for-ios, designing-for-macos, designing-for-watchos).

9. Onboarding e permissões são adiados até o momento de necessidade real, em vez de front-loaded: tanto designing-for-games ("defer requests until the right time") quanto o princípio de Responsibility em design-principles tratam o timing do pedido como parte do design, não um detalhe técnico.

10. Componentes de sistema padrão (system components) carregam acessibilidade, adaptação de layout e políticas de navegação "de graça": usar o padrão do sistema (toolbars, split views, size classes) é reiteradamente apresentado como o caminho que resolve automaticamente adaptação e acessibilidade, enquanto customização exige reimplementar essas garantias manualmente (designing-for-visionos, designing-for-iphone-duo, designing-for-ipados).

11. Inclusão é tratada como parte do design, não como anexo de compliance: designing-for-games dedica uma seção inteira ("Welcome everyone") a perceptibilidade, personalização, autorrepresentação e remoção de estereótipos, ecoando o princípio de Flexibility ("design for everyone") de design-principles.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/design-principles.md, 96 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-ios.md, 35 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-ipados.md, 33 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-macos.md, 36 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-tvos.md, 38 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-visionos.md, 46 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-watchos.md, 41 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-games.md, 86 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/designing-for-iphone-duo.md, 104 linhas lidas, até o fim: sim

Nenhum arquivo é só índice de coleção sem texto próprio; todos os 9 têm conteúdo substantivo.
