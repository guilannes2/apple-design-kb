# Foundations (parte 2)

## Materials (slug: materials)

O que governa: os efeitos visuais de translucidez e profundidade (Liquid Glass e materiais padrão) que separam elementos de primeiro plano, como texto e controles, dos elementos de fundo, como conteúdo e cores sólidas.

Por que: ao deixar a cor do fundo atravessar para o primeiro plano, um material estabelece hierarquia visual e ajuda as pessoas a manterem a noção de lugar dentro da interface. A Apple distingue duas funções: Liquid Glass unifica a linguagem de design entre plataformas e permite apresentar controles e navegação sem obscurecer o conteúdo abaixo; os materiais padrão ajudam na diferenciação visual dentro da própria camada de conteúdo.

Faça e evite:
- Use Liquid Glass para formar uma camada funcional distinta de controles e navegação (tab bars, sidebars) que flutua acima da camada de conteúdo.
- Não use Liquid Glass na camada de conteúdo; use Standard materials para elementos como fundos de app.
- Exceção: controles transitórios na camada de conteúdo, como sliders e toggles, podem assumir aparência de Liquid Glass quando a pessoa os ativa.
- Use efeitos de Liquid Glass com moderação; aplicar o efeito a muitos controles customizados distrai do conteúdo.
- Use a variante clear de Liquid Glass só para componentes sobre fundos visualmente ricos (fotos, vídeos); a variante regular é a indicada quando o fundo pode prejudicar a legibilidade, como em alertas, sidebars ou popovers com bastante texto.
- Ao usar a variante clear sobre conteúdo brilhante, considere uma camada de escurecimento escura com 35% de opacidade; não é necessária se o fundo já for suficientemente escuro ou se os controles padrão de reprodução de mídia do AVKit já fornecerem seu próprio dimming.
- Escolha materiais e efeitos padrão (UIBlurEffect, UIVibrancyEffect, NSVisualEffectView.BlendingMode) pelo significado semântico e uso recomendado, nunca pela cor aparente que produzem, já que as configurações do sistema podem mudar essa aparência.
- Use cores vibrantes definidas pelo sistema sobre materiais para garantir legibilidade em qualquer contexto.
- Materiais mais espessos (mais opacos) dão melhor contraste para texto e elementos finos; materiais mais finos (mais translúcidos) ajudam a pessoa a reter o contexto do que está atrás.

Especificações exatas: nenhum número, medida ou valor padrão exato foi fornecido neste artigo, exceto a opacidade de 35% recomendada para a camada de escurecimento atrás de componentes com Liquid Glass clear sobre fundo brilhante.

Diferenças por plataforma:
- iOS, iPadOS: além do Liquid Glass, continuam a oferecer quatro materiais padrão na camada de conteúdo: ultra-thin, thin, regular (padrão) e thick. Definem cores vibrantes para labels, fills e separators específicas para cada material; labels e fills têm vários níveis de vibrância (label, secondaryLabel, tertiaryLabel, quaternaryLabel para labels; fill, secondaryFill, tertiaryFill para fills), separators têm um nível único. Evite quaternary sobre os materiais thin e ultraThin, pois o contraste fica baixo demais.
- macOS: fornece vários materiais padrão com propósitos designados e versões vibrantes de todas as especificações (NSVisualEffectView.Material). Define dois modos de blending de fundo: behind window e within window.
- tvOS: Liquid Glass aparece em elementos de navegação e experiências de sistema como Top Shelf e Control Center; elementos como image views e botões adotam Liquid Glass ao ganhar foco. Também continua oferecendo materiais padrão: ultraThin (para telas cheias que exigem esquema de cor claro), thin (overlays que obscurecem parcialmente o conteúdo e exigem esquema claro), regular (overlays gerais) e thick (overlays que exigem esquema escuro).
- visionOS: janelas usam por padrão um material do sistema chamado glass, que deixa luz, o Environment atual, conteúdo virtual e objetos físicos do entorno passarem através. Não existe modo escuro distinto; o glass se adapta automaticamente à luminância do que está atrás. Prefira translucidez a cores opacas nas janelas. Para separação visual ou indicar interatividade: thin chama atenção para elementos interativos como botões e itens selecionados; regular separa seções do app, como sidebar ou tabela agrupada; thick cria um elemento escuro que permanece distinto sobre um fundo regular. Define três valores de vibrância: label (texto padrão), secondaryLabel (texto descritivo como notas de rodapé e subtítulos) e tertiaryLabel (elementos inativos, só quando o texto não precisa de alta legibilidade).
- watchOS: use materiais para dar contexto em views modais de tela cheia, comuns nessa plataforma; evite remover ou substituir os fundos de material fornecidos por padrão em folhas modais.

Ligações com outros artigos: Color, Accessibility, Dark Mode.

<!-- visual:materials -->
### O que as ilustrações mostram
Base: 7 de 7 folhas de ilustrações vistas (img 0770 a 0789, várias em versão clara e escura) e 4 de 4 folhas do vídeo hig-vid_materials__015 vistas (quadros q001 a q037), códigos conferidos.
- A abertura desenha uma cápsula sobre um quadrado arredondado a partir de uma grade pontilhada explícita, com linhas verticais, horizontais, diagonais radiais e um círculo de guia; a borda do quadrado sob a cápsula aparece levemente curvada, sugerindo a deformação óptica do vidro sobre o que está atrás. No modo escuro o fundo vira dourado oliva e os contornos ficam claros, invertendo a luminosidade sem mudar a matiz amarela (img 0770, clara e escura).
- O Liquid Glass regular muda de tom conforme o fundo, sem mudar de forma: sobre céu estrelado o círculo fica cinza escuro semitransparente, sobre foto de praia fica esbranquiçado, e nos dois casos borra o conteúdo atrás (img 0771, img 0772).
- A variante clear borra menos que a regular: dentro do círculo o padrão da parede de tijolos continua reconhecível, ao contrário do borrão mais forte das duas imagens anteriores (img 0773 comparada a img 0771 e img 0772).
- Contraste sobre material é ensinado com par de errado e certo, nos dois modos: o símbolo de compartilhar em systemGray3 sobre o botão de material quase se confunde com o fundo, seguido de um selo com X (img 0774, img 0775); o mesmo botão com o símbolo em cor vibrante se destaca claramente, no claro e no escuro, seguido de um selo com check verde (img 0776, img 0777).
- Os quatro materiais padrão do iOS e iPadOS são o mesmo ícone sobre o mesmo fundo colorido em progressão de opacidade: ultraThin quase transparente e com pouco embaçamento, thin mais opaco e esbranquiçado, regular quase branco leitoso e thick quase branco puro, restando só um halo de cor nas bordas (img 0778 a img 0781, claras).
- No modo escuro a mesma série vai de um azul translúcido que ainda mostra as formas atrás até um tom escuro quase uniforme no thick, com o gradiente de fundo desaparecendo a cada nível (img 0778 a img 0781, escuras).
- No tvOS a página usa captura real do app Destination Video: barra de abas com a aba ativa em pílula branca opaca e, abaixo, um cartão translúcido com título, descrição, duração e dois botões, em Liquid Glass, deixando ver borrada a cena colorida de fundo (img 0782).
- No visionOS a mesma sala de estar serve de par comparativo: uma janela azul sólida bloqueia totalmente o ambiente, e a janela translúcida deixa ver, borrados, os móveis e a luz atrás dela (img 0783, img 0784).
- Uma única janela do visionOS combina três espessuras anotadas com linhas de chamada: "Thick" numa barra horizontal opaca perto do topo, "Regular" no painel grande translúcido e "Thin" num botão em pílula no canto inferior direito. No escuro o contraste entre as três cai, mas a barra thick continua a mais sólida (img 0785, clara e escura).
- No watchOS o material cobre a tela inteira de um modal com botão X translúcido no canto superior esquerdo, hora, ícone de fone, título em negrito e descrição; o botão "Action" em pílula com gradiente roxo para magenta se destaca como camada própria sobre esse material, com texto branco de alto contraste (img 0789).
- No vídeo, a janela do app Music no visionOS gira no eixo vertical e volta a ficar frontal; o vidro continua translúcido o tempo todo, a distorção e o borrão do fundo ficam mais visíveis quando a janela está mais inclinada, e o conteúdo interno não muda de posição relativa (vídeo, folha 0001, q001 a q009, com maior inclinação em q002 a q004).
- Depois o fundo troca para uma escrivaninha em luz mais amena (folha 0002, q010 a q018), a sala escurece e a janela escurece junto, ficando mais acinzentada e opaca sem que o texto da lista perca contraste (folha 0003, q020 a q028), e por fim a cena se estabiliza sem oscilação do material (folha 0004, q029 a q037).
Divergências registradas: a descrição oficial de img 0785 fala em barra lateral à esquerda em regular e área de conteúdo à direita, com thin no botão e thick no campo de texto, mas a imagem mostra os três materiais na mesma janela ampla, sem coluna lateral claramente separada; nas imagens de vibrância do visionOS (img 0786 label, img 0787 secondaryLabel, img 0788 tertiaryLabel) o símbolo branco parece igualmente nítido nos três níveis, e a diferença de contraste não pôde ser distinguida com segurança; a descrição oficial do vídeo não menciona que o enquadramento de fundo muda da sala com sofá para a escrivaninha no meio da gravação.
<!-- /visual:materials -->

## Motion (slug: motion)

O que governa: como usar movimento e animação de forma intencional para transmitir status, dar feedback e enriquecer a experiência visual do app ou jogo, incluindo considerações específicas de conforto em visionOS.

Por que: muitos componentes do sistema já incluem movimento automaticamente e o ajustam conforme configurações de acessibilidade ou método de entrada, mantendo experiências familiares e consistentes. Movimento adicionado sem propósito distrai as pessoas e pode fazer com que se sintam desconectadas ou fisicamente desconfortáveis; nem todos podem ou querem experimentar movimento, então ele nunca deve ser o único canal de comunicação de informação importante.

Faça e evite:
- Adicione movimento com propósito; não adicione movimento pela própria animação.
- Torne o movimento opcional; complemente feedback visual com alternativas como hápticos e áudio.
- Busque feedback realista que siga os gestos e expectativas das pessoas; movimento que não faz sentido desorienta.
- Prefira animações de feedback breves e precisas, que tendem a parecer leves e discretas e comunicam informação com mais eficácia do que animação proeminente.
- Em apps, evite em geral adicionar movimento a interações de UI que ocorrem com frequência, já que o sistema já fornece animações sutis para elementos padrão.
- Deixe as pessoas cancelarem o movimento; não as force a esperar uma animação terminar antes de agir, especialmente se a experimentam repetidamente.
- Considere usar símbolos animados quando fizer sentido (SF Symbols 5 ou posterior).
- Em jogos, garanta que o movimento funcione bem por padrão em cada plataforma suportada; manter uma taxa de quadros consistente de 30 a 60 fps costuma resultar em experiência suave e visualmente agradável.
- Deixe as pessoas personalizarem a experiência visual do jogo para otimizar desempenho ou bateria, por exemplo alternando modos de energia quando o sistema detecta fonte de energia externa.

Especificações exatas: taxa de quadros recomendada em jogos de 30 a 60 fps. Em visionOS, evitar oscilação sustentada de objetos com frequência próxima de 0,2 Hz, à qual as pessoas são muito sensíveis.

Diferenças por plataforma:
- iOS, iPadOS, macOS, tvOS: nenhuma consideração adicional.
- visionOS: o movimento pode combinar com Depth para dar feedback essencial quando as pessoas olham para elementos interativos. Evite mostrar movimento nas bordas do campo de visão da pessoa, pois isso é especialmente perceptível na visão periférica e pode causar desconforto; se precisar mostrar um objeto se movendo na periferia, mantenha o brilho semelhante ao restante do conteúdo visível. Ao mover objetos virtuais grandes, aumente a translucidez ou reduza o contraste para tornar o movimento menos perceptível e ajudar as pessoas a não sentirem que elas ou seu entorno estão se movendo; considere manter o tamanho de uma janela relativamente pequeno. Considere usar fades ao reposicionar um objeto, se o movimento em si não comunicar nada útil. Em geral, evite deixar as pessoas girarem um mundo virtual inteiro, pois isso costuma atrapalhar a sensação de estabilidade mesmo quando a pessoa controla a rotação; prefira mudanças direcionais instantâneas durante um fade rápido. Considere dar às pessoas um referencial estacionário, já que é mais fácil lidar com movimento visual contido em uma área que não se move. Evite oscilação sustentada de objetos, principalmente perto de 0,2 Hz; se precisar mostrar oscilação, mantenha amplitude baixa e considere tornar o conteúdo translúcido.
- watchOS: SwiftUI oferece um jeito eficiente de adicionar movimento; para animar layout e aparência via WatchKit, ou criar sequências de imagem animada, usar WKInterfaceImage. Todas as animações baseadas em layout e aparência incluem automaticamente um easing embutido no início e no fim da animação, que não pode ser desligado ou customizado.

Ligações com outros artigos: Feedback, Accessibility, Spatial layout, Immersive experiences.

<!-- visual:motion -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista (img 0800, versão clara), código conferido; a página não tem vídeo.
- A abertura da página segue o mesmo método de construção dos outros esboços de seção do HIG: forma tingida de amarelo desenhada sobre uma grade pontilhada com linhas verticais, horizontais, diagonais radiais e um círculo de guia (img 0800).
- O movimento é sugerido pela sobreposição de formas de diamante repetidas e deslocadas na horizontal: a da esquerda em contorno de chevron duplo, mais clara e vazada, e a da direita mais sólida e escura, parcialmente atrás da primeira (img 0800).
- À esquerda das formas, uma fileira curva de pequenos círculos de tamanho decrescente funciona como rastro; junto com a sobreposição das formas, sugere uma trajetória em arco e não um deslocamento puramente linear (img 0800).
Divergências registradas: a descrição oficial fala em três diamantes sobrepostos, mas na imagem só duas formas se distinguem com segurança, e o rastro de pontos não é mencionado na descrição (img 0800).
<!-- /visual:motion -->

## Privacy (slug: privacy)

O que governa: como solicitar, explicar e proteger o acesso a dados e recursos sensíveis das pessoas, incluindo os textos de permissão, o botão de localização e as práticas de proteção de dados armazenados.

Por que: as pessoas usam seus dispositivos de forma muito pessoal e esperam que os apps preservem sua privacidade; é natural desconfiar de um pedido de informação pessoal ou acesso a um recurso do dispositivo, especialmente sem necessidade óbvia. Transparência sobre como os dados são usados aumenta a confiança, e pedir acesso só quando a funcionalidade de fato precisa evita gerar desconfiança.

Faça e evite:
- Solicite acesso somente aos dados que a funcionalidade realmente precisa; peça permissões o mais específicas possível.
- Seja transparente sobre como o app coleta e usa dados das pessoas; respeite escolhas de recursos do sistema como Hide My Email e Mail Privacy Protection.
- Processe dados no dispositivo sempre que possível, por exemplo usando o Apple Neural Engine e modelos CreateML customizados no iOS, evitando idas e vindas a um servidor remoto.
- Adote proteções de privacidade definidas pelo sistema e siga boas práticas de segurança, como usar CloudKit para criptografia e gestão de chaves em iOS 15 e posterior.
- Solicite permissão apenas quando o app claramente precisa do acesso; idealmente, espere até a pessoa de fato usar a funcionalidade que exige o acesso, por exemplo por meio do location button.
- Evite solicitar permissão no lançamento do app, a menos que o dado ou recurso seja necessário para o app funcionar.
- Escreva o purpose string (texto de justificativa) como frase breve, completa, direta, específica e fácil de entender, em sentence case, sem voz passiva, terminando com ponto.
- Exemplo correto de purpose string: frase ativa que descreve claramente como e por que o app coleta o dado. Exemplos incorretos: frase passiva com justificativa vaga, ou frase imperativa sem justificativa.
- Em telas ou janelas customizadas que precedem o alerta padrão do sistema (pre-alert screens), inclua só um botão, deixando claro que ele abre o alerta do sistema; use termos como "Continue" ou "Next" no botão, nunca um termo como "Allow" que possa se confundir com o botão do alerta.
- Não inclua ações adicionais na tela customizada, como opção de fechar ou cancelar sem ver o alerta do sistema.
- Nunca preceda o alerta padrão de rastreamento (app tracking) com uma tela customizada que confunda ou induza a pessoa; ofertar incentivos, exibir uma tela parecida com um pedido, mostrar imagem do alerta ou anotar a tela atrás do alerta são exemplos de designs proibidos que levam à rejeição na App Store review (referência: App Review Guidelines 5.1.1 (iv)).
- Considere usar o location button (iOS, iPadOS, watchOS) para dar autorização temporária de localização no momento em que a tarefa precisa dela; a primeira vez que a pessoa toca no botão, o sistema mostra um alerta padrão explicando o comportamento do botão; depois disso, tocar no botão concede permissão única sem precisar reconfirmar entendimento.
- É possível customizar o location button: título do sistema (por exemplo "Current Location" ou "Share My Current Location"), glifo preenchido ou contornado, cor de fundo, cor do título e do glifo, e raio de canto; não é possível customizar outros atributos visuais. É responsabilidade do desenvolvedor garantir que o texto caiba sem truncar em todos os tamanhos de acessibilidade e traduções.
- Evite depender só de senhas para autenticação; prefira passkeys, e se ainda usar senha, use autenticação de dois fatores; use identificação biométrica (Face ID, Optic ID, Touch ID) para proteger acesso a apps que a pessoa mantém logado.
- Armazene informação sensível em um keychain; nunca armazene senhas ou conteúdo seguro em arquivos de texto simples, mesmo com permissões de arquivo restritas.
- Evite inventar esquemas de autenticação customizados; prefira recursos do sistema como passkeys, Sign in with Apple ou Password AutoFill.

Especificações exatas: nenhum número específico (pt, px, ms, etc.) foi fornecido neste artigo, além da referência à cláusula 5.1.1 (iv) das App Review Guidelines.

Diferenças por plataforma:
- iOS, iPadOS, tvOS, watchOS: nenhuma consideração adicional além das gerais.
- macOS: assine o app com um Developer ID válido se distribuído fora da loja; proteja dados das pessoas com app sandboxing, exigido para todos os apps enviados à Mac App Store; evite presumir quem está logado, já que o fast user switching pode ter várias pessoas ativas no mesmo sistema.
- visionOS: por padrão, algoritmos do ARKit lidam com persistência, mapeamento do mundo, segmentação, matting e iluminação do ambiente, sempre rodando e beneficiando apps no Shared Space sem enviar dados a eles; para acessar APIs do ARKit, o app precisa abrir um Full Space, e recursos como Plane Estimation, Scene Reconstruction, Image Anchoring e Hand Tracking exigem permissão explícita. A entrada do usuário (input) é privada por design: o sistema mostra automaticamente hover effects quando a pessoa olha para componentes interativos, sem expor para onde ela está olhando antes de tocar. O acesso à câmera funciona diferente: a câmera traseira fornece entrada em branco (é só conveniência de compatibilidade), e a câmera frontal só fornece entrada após permissão explícita da pessoa.

Ligações com outros artigos: Entering data, Onboarding.

<!-- visual:privacy -->
### O que as ilustrações mostram
Base: 4 de 4 folhas de ilustrações vistas (img 0890 a 0905, todas em versão clara), códigos conferidos; a página não tem vídeo.
- A abertura desenha uma mão erguida em gesto de pare, em marrom dourado sobre degradê amarelo, com grade de guias retangulares e círculo concêntrico atrás, no mesmo método de construção geométrica das outras ilustrações de abertura do HIG (img 0890).
- A página de produto da App Store organiza a privacidade em texto introdutório com o nome do desenvolvedor e link para a política, seguido de dois cartões brancos empilhados, "Data Used to Track You" e "Data Linked to You", cada um com título, subtítulo explicativo e itens numa grade de duas colunas com ícone à esquerda do texto (img 0891).
- Os selos de certo e errado têm a mesma composição e o mesmo tamanho, isolados num quadro branco, e variam só na cor e no símbolo: círculo verde com check branco para o correto, círculo cinza claro com X cinza escuro para o incorreto (img 0892, img 0893).
- Os alertas de permissão de localização e de fotos, sobre a tela "New Post", seguem a mesma estrutura de título, texto explicativo e três botões empilhados; o de localização, com título em negrito e botões de fundo cinza claro, acrescenta uma prévia de mapa com selo "Precise: On" e pino azul central e ordena os botões como permitir uma vez, permitir durante o uso e não permitir, e o de fotos oferece selecionar fotos, permitir acesso a todas e não permitir (img 0894, img 0895).
- O alerta de acesso a contatos, sobre a aba "Friends" com avatares, usa só dois botões lado a lado, com "Allow" em azul destacado, diferente dos botões empilhados dos dois alertas anteriores (img 0896).
- A tela customizada que antecede o alerta, no formato aceito, é uma tela cheia com fundo lilás claro de padrão hexagonal, título, três benefícios com ícone e texto, uma nota de que a opção pode ser mudada nos Ajustes e um único botão "Next" na base (img 0897).
- As versões proibidas partem da mesma tela e acrescentam uma saída: um segundo botão "Cancel" empilhado sob o "Next" (img 0898) ou um X de fechar no canto superior esquerdo, ao lado do relógio (img 0899).
- As telas proibidas de rastreamento usam persuasão visual: um cifrão grande em círculo roxo com botão "Get $100 Credit" (img 0900) e um gráfico de barras roxas crescentes da esquerda para a direita com botão "Allow Tracking" (img 0901).
- Outras telas proibidas reproduzem o alerta real do sistema dentro da tela customizada e o anotam: o botão de permitir durante o uso circulado à mão em roxo, com botão "Continue" na base (img 0902), ou uma seta roxa subindo de uma instrução para escolher permitir (img 0903).
- O botão de localização aparece como pílula azul sólida com ícone branco de seta de localização seguido do rótulo "Current Location", sem mais nenhum elemento (img 0904).
- Em contexto, sobre um mapa real com ruas nomeadas, o alerta padrão de localização mantém a prévia de mapa com "Precise: On" e os três botões empilhados vistos antes (img 0905).
<!-- /visual:privacy -->

## Right to left (slug: right-to-left)

O que governa: como adaptar a interface para idiomas de leitura da direita para a esquerda (RTL), como árabe e hebraico, incluindo alinhamento de texto, números, controles, imagens e ícones.

Por que: quando alguém escolhe um idioma para o dispositivo (ou só para o app), espera que a interface se adapte de várias formas. Frameworks de UI do sistema já suportam RTL por padrão e invertem componentes automaticamente; a orientação existe para quando é preciso ajustar layout ou aprimorar localizações específicas envolvendo moedas, numerais ou símbolos matemáticos.

Faça e evite:
- Ajuste o alinhamento de texto para bater com a direção da interface quando o sistema não fizer isso automaticamente (por exemplo, texto alinhado à esquerda em LTR deve virar alinhado à direita em RTL).
- Alinhe um parágrafo (três ou mais linhas) de acordo com o idioma dele, não com o contexto atual; blocos de uma ou duas linhas continuam seguindo a direção de leitura do contexto atual.
- Use um alinhamento consistente para todos os itens de uma lista, inclusive itens exibidos em um script diferente.
- Diferentes idiomas RTL usam sistemas numéricos distintos: hebraico usa numerais arábicos ocidentais; árabe pode usar numerais arábicos ocidentais ou orientais, variando por país, região e até por área dentro da mesma região. Identifique a forma apropriada de exibir números em cada localidade que o app cobre para tópicos numéricos; apps sem foco em número podem confiar nas representações padrão do sistema.
- Não inverta a ordem dos dígitos dentro de um número específico (como "541", telefone ou número de cartão): a ordem interna permanece sempre a mesma, independentemente do idioma.
- Inverta a ordem de numerais que mostram progresso ou direção de contagem (como em barras de progresso, sliders, ratings), mas nunca inverta os próprios numerais; também inverta uma sequência de numerais se ela comunica uma ordem específica.
- Inverta controles que mostram progresso de um valor a outro, como sliders e indicadores de progresso, e inverta também as posições de glifos ou imagens que representam início e fim; inverta controles de navegação de ordem fixa, como o botão voltar, que precisa apontar para a direita em RTL, e botões de próximo/anterior.
- Preserve a direção de um controle que se refere a uma direção real ou aponta para uma área da tela; esse controle mantém sua direção original independentemente do contexto.
- Equilibre visualmente scripts latinos e RTL adjacentes quando necessário: aumentar em cerca de 2 pontos o tamanho da fonte RTL ajuda a equilibrar texto árabe ou hebraico ao lado de texto latino todo em maiúsculas, já que árabe e hebraico não têm maiúsculas.
- Evite inverter imagens como fotografias, ilustrações e artes gerais, pois inverter uma imagem pode mudar seu significado, e inverter imagem protegida por direitos autorais pode ser violação; considere criar uma nova versão da imagem quando o conteúdo estiver fortemente ligado à direção de leitura.
- Inverta as posições de imagens quando a ordem delas for significativa (cronológica, alfabética, favoritos etc.), para preservar o significado da ordem no contexto RTL.
- Ao usar SF Symbols para ícones de interface, você ganha variantes para o contexto RTL e símbolos localizados para árabe e hebraico, entre outros idiomas; se criar símbolos customizados, é possível especificar a direcionalidade deles.
- Inverta ícones de interface que representam texto ou direção de leitura, por exemplo barras alinhadas à esquerda que representam texto devem virar alinhadas à direita em RTL.
- Considere criar uma versão localizada de um ícone de interface que exibe texto real, como as diferentes versões dos símbolos de assinatura, rich-text e cursor I-beam que o SF Symbols oferece para latim, hebraico e árabe.
- Inverta um ícone de interface que mostra movimento para frente ou para trás, já que a direção percebida como "para frente" depende do sentido de leitura; por exemplo, o ícone de um alto-falante com ondas sonoras precisa inverter a direção das ondas.
- Não inverta logotipos ou sinais e marcas universais (como o checkmark); exibir um logotipo invertido confunde as pessoas e pode ter repercussões legais.
- Em geral, evite inverter ícones de interface que representam objetos do mundo real, a menos que o objeto seja usado para indicar direcionalidade; a maioria das pessoas é destra, então inverter um ícone que mostra uma ferramenta usada com a mão direita normalmente não é necessário.
- Antes de simplesmente inverter um ícone customizado complexo, considere seus componentes individuais e o equilíbrio visual geral: alguns componentes (como badge, barra diagonal ou lupa) precisam manter a linguagem visual independentemente da localização (por exemplo, a mesma barra diagonal de proibição em versões LTR e RTL do SF Symbols); em outros casos, é preciso inverter um componente ou sua posição para preservar o sentido e o equilíbrio visual do ícone.
- Se o ícone customizado inclui um componente que pode implicar destreza manual (como uma ferramenta), considere preservar a orientação da ferramenta ao mesmo tempo em que inverte a imagem base, se necessário.

Especificações exatas: aumentar em cerca de 2 pontos o tamanho de fonte RTL para equilibrar visualmente com texto latino em maiúsculas.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Layout, Inclusion, SF Symbols.

<!-- visual:right-to-left -->
### O que as ilustrações mostram
Base: 12 de 12 folhas de ilustrações vistas (img 0933 a 0979, todas em versão clara), códigos conferidos; a página não tem vídeo.
- O alinhamento de texto é demonstrado com o mesmo cartão em duas versões: em LTR uma barra azul vertical marca a guia à esquerda e o texto e a barra interna alinham por ela; em RTL a guia e o alinhamento passam para a direita, mas o ícone de imagem central continua no mesmo lugar, sem inversão (img 0934, img 0935).
- Parágrafos em árabe e em latim aparecem com uma linha vertical vermelha marcando a margem de leitura de cada um: árabe à direita e latim à esquerda numa composição (img 0936) e os dois alinhados à direita na outra (img 0938), com um selo isolado de certo (img 0937) e um de errado (img 0939) intercalados na sequência.
- Uma lista RTL é desenhada como cinco barras cinza de comprimentos variados alinhadas a uma única guia azul à direita (img 0940); na versão de alinhamento misto, a segunda barra se desloca para a esquerda com uma guia azul própria (img 0941).
- Os numerais aparecem em tipografia grande e simples: "123" em algarismos ocidentais e depois em algarismos arábicos orientais, de traço mais caligráfico (img 0942, img 0943); em frases, o número aparece com a mesma ordem interna de dígitos no latim, no hebraico e no árabe, no mesmo tamanho e peso do texto, e no árabe também na variante com algarismos orientais (img 0944 a img 0947).
- A avaliação por estrelas mostra três estrelas cheias, uma pela metade e uma vazia, com cada numeral centralizado sob sua estrela e contagem crescente da esquerda para a direita (img 0948); nas versões RTL a ordem da contagem se inverte, uma com algarismos orientais (img 0949) e outra com algarismos ocidentais dispostos de 5 a 1 (img 0950).
- O slider de volume espelha por inteiro: em LTR o alto-falante sem ondas fica à esquerda, o com ondas à direita e a trilha azul se preenche da esquerda até o controle central; em RTL os ícones trocam de lado e o preenchimento parte da direita (img 0951, img 0952).
- O equilíbrio entre escritas é medido com duas linhas horizontais vermelhas, de ascendente e de base, sobre três botões azuis com o rótulo de download em latim maiúsculo, árabe e hebraico no mesmo tamanho: só o latim toca as duas linhas (img 0953); com a fonte árabe e hebraica ligeiramente maior, os rótulos alcançam melhor as guias e o peso visual se equilibra (img 0954).
- Na seção de imagens, um globo simplificado reaparece com as massas de terra deslocadas em relação à primeira versão, o que é compatível com a inversão horizontal citada na descrição oficial (img 0955, img 0956); e um cartão com título, grade de quatro áreas com a maior selecionada em contorno azul e fileira de cinco formas espelha título, área maior e ordem das formas (img 0957, img 0958).
- Ícones que representam texto ou direção são espelhados por completo: lista com marcadores, livro com lombada, campo de texto com lápis, janela com pontos no canto e toggle com círculo preenchido trocam de lado (img 0959, img 0960); o documento com linhas alinhadas à esquerda passa a ter as linhas à direita (img 0961, img 0962); o alto-falante com ondas passa a emitir para a esquerda (img 0966, img 0967); o alto-falante mudo espelha com a barra diagonal em direção oposta (img 0973, img 0974).
- Os símbolos com texto real são localizados em vez de só espelhados: assinatura, documento com letra e letra grande com cursor I-beam aparecem em latim, hebraico e árabe; na versão hebraica a assinatura termina à esquerda com o X à direita, e nas versões hebraica e árabe a letra do documento vai para o canto superior direito e a letra grande fica à direita do cursor (img 0963 a img 0965).
- Aparecem em versão única, sem par espelhado, o logotipo da Apple TV, o checkmark, um relógio analógico sem elemento assimétrico, um lápis com a ponta no canto inferior esquerdo e um controle de videogame (img 0968 a img 0972).
- Ícones compostos mostram o tratamento por componente: o carrinho de compras espelhado mantém o selo de mais no canto superior direito (img 0976), e a variante RTL completa reposiciona o selo para o canto superior esquerdo, acompanhando a direção do carrinho (img 0975, img 0977); o cartão com lupa espelha, levando a lupa para a esquerda e o ponto do cartão para o canto oposto (img 0978, img 0979).
<!-- /visual:right-to-left -->

## SF Symbols (slug: sf-symbols)

O que governa: o uso da biblioteca SF Symbols, milhares de símbolos configuráveis que se integram ao San Francisco, incluindo modos de renderização, gradientes, cor variável, pesos, escalas, variantes de design, animações e criação de símbolos customizados.

Por que: os símbolos se alinham automaticamente ao texto em todos os pesos e tamanhos porque compartilham a fundação tipográfica do San Francisco, permitindo emparelhamento preciso de peso entre símbolo e texto adjacente e consistência visual em toda a interface. A disponibilidade de símbolos e recursos varia conforme a versão do sistema visada; recursos introduzidos em um determinado ano não estão disponíveis em sistemas operacionais anteriores.

Faça e evite:
- É proibido usar símbolos do SF Symbols, ou imagens confusamente semelhantes a eles, em ícones de app, logotipos ou qualquer outro uso de marca registrada.
- Escolha o modo de renderização conforme a necessidade: monochrome aplica uma cor a todas as camadas; hierarchical aplica uma cor variando a opacidade por nível hierárquico da camada; palette aplica duas ou mais cores, uma por camada (se especificar só duas cores para um símbolo com três níveis, a camada secundária e a terciária compartilham a mesma cor); multicolor aplica cores intrínsecas para reforçar significado (por exemplo, leaf usa verde, trash.slash usa vermelho para sinalizar perda de dados).
- Confirme que o modo de renderização escolhido funciona bem em todo contexto; é possível usar o modo automático para obter o modo preferido de um símbolo, mas vale checar os resultados onde um modo diferente possa melhorar a legibilidade.
- Use cores fornecidas pelo sistema para que os símbolos se adaptem automaticamente a acomodações de acessibilidade e modos de aparência como vibrância e Dark Mode.
- Em SF Symbols 7 e posterior, use gradient rendering para gerar um gradiente linear suave a partir de uma única cor de origem; funciona em qualquer tamanho, mas fica melhor em tamanhos maiores.
- Use variable color para representar uma característica que muda ao longo do tempo, como capacidade ou intensidade, aplicando cor a diferentes camadas conforme o valor atinge diferentes limiares entre 0% e 100%; algumas camadas de um símbolo podem optar por não participar da variable color. Use variable color para comunicar mudança, não para comunicar profundidade; para profundidade, use hierarchical rendering.
- SF Symbols oferece nove pesos de símbolo (de ultralight a black), cada um correspondendo a um peso da fonte San Francisco, e três escalas: small, medium (padrão) e large, definidas em relação à altura da caixa alta (cap height) do San Francisco.
- Especificar uma escala permite ajustar a ênfase do símbolo em relação ao texto adjacente sem alterar o emparelhamento de peso com texto que usa o mesmo tamanho de ponto.
- SF Symbols define variantes de design como fill, slash e enclosed para comunicar estados e ações com precisão mantendo consistência visual; outline é a variante mais comum, sem áreas sólidas, parecida com texto; a maioria dos símbolos também tem variante fill, com áreas sólidas. Outline funciona bem em toolbars, listas e junto de texto; símbolos com forma envolvente (círculo, quadrado) melhoram legibilidade em tamanhos pequenos; a variante fill dá mais ênfase visual e funciona bem em tab bars do iOS e ações de swipe, e em lugares onde se usa a accent color para comunicar seleção.
- SF Symbols oferece variantes específicas para diversos idiomas e sistemas de escrita (latim, árabe, hebraico, hindi, tailandês, chinês, japonês, coreano, cirílico, devanágari e vários sistemas de numerais índicos), que se adaptam automaticamente quando o idioma do dispositivo muda.
- Aplique animações de símbolos com critério; não há limite de quantas animações uma view pode receber, mas animações demais sobrecarregam a interface e distraem.
- Use animações de símbolos para comunicar informação de forma mais eficiente e considere o tom do app ao adicioná-las, alinhando com a identidade de marca.
- Ao criar um símbolo customizado, exporte o template de um símbolo parecido e modifique com uma ferramenta de edição vetorial; siga o template como guia, mantendo consistência de nível de detalhe, peso óptico, alinhamento, posição e perspectiva com os símbolos do sistema; o símbolo customizado deve ser simples, reconhecível, inclusivo e diretamente relacionado à ação ou conteúdo que representa.
- Símbolos que representam produtos ou recursos da Apple são protegidos por direitos autorais: podem ser exibidos, mas não customizados (a SF Symbols app sinaliza esses símbolos com um ícone de informação); não crie réplicas de produtos Apple.
- Atribua margens laterais negativas ao símbolo customizado se necessário, para auxiliar o alinhamento horizontal óptico quando o símbolo contém um badge ou elemento que aumenta sua largura; use o padrão de nomenclatura que inclui a configuração relevante, como "left-margin-Regular-M".
- Otimize camadas para permitir animação por camada em símbolos customizados, anotando-as no app SF Symbols; teste as animações com todos os presets, já que formas e caminhos podem não aparecer como esperado em movimento.
- Evite criar símbolos customizados que incluam variantes comuns, como enclosures ou badges; use a biblioteca de componentes do app SF Symbols para manter consistência de design.
- Forneça textos alternativos (descrições de acessibilidade) para símbolos customizados, para que o VoiceOver descreva a UI visível.

Especificações exatas: nove pesos de símbolo (ultralight a black); três escalas (small, medium padrão, large), definidas em relação à cap height da fonte San Francisco.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: SF Symbols, Typography, Icons, Images, Branding, VoiceOver.

<!-- visual:sf-symbols -->
### O que as ilustrações mostram
Base: 5 de 5 folhas de ilustrações vistas (img 1002 a 1019, todas em versão clara) e 11 vídeos vistos por inteiro (hig-vid_sf-symbols__042 a __052, 24 folhas no total), códigos conferidos.
- O ícone do app SF Symbols aparece com a grade de construção sobreposta: linhas pontilhadas verticais e horizontais e dois círculos concêntricos tracejados centralizados, servindo de guia e de área segura para o glifo dentro do quadrado (img 1002).
- As camadas de um símbolo são isoladas por contraste sobre a mesma silhueta de cloud.sun.rain.fill: primária com a nuvem em preto e o resto em cinza claro, secundária com o sol em preto, terciária com as gotas em preto (img 1003 a img 1005); no modo hierárquico o símbolo inteiro fica azul em três opacidades, nuvem opaca, sol médio e gotas bem claras (img 1006).
- Os modos de renderização são comparados com a mesma fileira de oito símbolos utilitários: monocromático todo em azul sólido e traço fino (img 1007); hierárquico com azul forte só no elemento de destaque, como o sinal de mais, o traço da lixeira e o "abc", e azul claro no restante (img 1008); paleta com parte da fileira toda azul e o resto com azul no destaque e cinza claro nas demais partes (img 1009); multicolor com a lixeira em vermelho e sublinhado vermelho pontilhado sob o "abc", mantendo azul ou cinza nos outros elementos (img 1010).
- O gradiente é ensinado por par mínimo: o mesmo sol em amarelo chapado e com gradiente sutil, mais vivo à esquerda e um pouco mais escuro à direita (img 1011, img 1012); a cor variável aparece como quatro estados do alto-falante lado a lado, com nenhuma, uma, duas e três ondas preenchidas de azul, enquanto o corpo fica azul fixo (img 1013).
- Pesos e escalas são tabulados numa matriz de 27 amostras do mesmo símbolo de pasta com mais: nove colunas de Ultralight a Black e três linhas Small, Medium e Large, com rótulos acima e à esquerda e variação sutil de espessura de traço e tamanho (img 1014).
- A escala em relação ao texto é medida com duas linhas vermelhas, na altura das maiúsculas e na linha de base, sobre o símbolo de mais em círculo ao lado da palavra "Add": em small o círculo fica menor que o vão entre as guias (img 1015), em medium ultrapassa levemente as duas guias (img 1016) e em large fica nitidamente maior, com o traço vertical do mais quase tocando as guias e o símbolo encostado na palavra, sem o espaço visto nas duas anteriores (img 1017).
- As variantes de design aparecem em grade de duas linhas por cinco colunas: o coração simples, com barra diagonal, em círculo, em quadrado e em retângulo, em outline na linha de cima e em fill na de baixo (img 1018); a localização aparece em grade de oito linhas por onze colunas de símbolos de texto, em que cada linha repete os mesmos onze símbolos trocando só o caractere interno: latim, árabe, hebraico, devanágari, um segundo caractere devanágari ou numeral indiano, ideograma CJK, hiragana e hangul (img 1019).
- Todos os vídeos mostram três símbolos diferentes lado a lado recebendo o mesmo efeito; nos de breathe e rotate eles aparecem em preto sobre fundo branco, sem cor, texto ou interface ao redor (vídeos __051 e __052). No appear os símbolos entram escalonados, primeiro a antena, depois a pilha de fotos e por fim a forma de onda, de um quadro vazio em q001 até os três em q005 (vídeo __042, folha 0001); no disappear somem em ordem, pasta, lâmpadas e balões, até o quadro vazio em q004, e voltam completos em q005 (vídeo __043, folha 0001).
- No scale cada símbolo reduz e volta ao tamanho de forma defasada dos outros, com o picture in picture menor de q002 a q006 e o HomePod menor em q006, q008 e q009, e os três cheios de novo no quadro final q019 (vídeo __045, folhas 0001 a 0003). No pulse só uma camada de cada símbolo alterna entre cinza claro e escuro, a tela do AirPlay, o círculo de pausa e o retângulo atrás da pessoa, fora de fase entre si, como em q013 (vídeo __046, folhas 0001 a 0003).
- Na cor variável animada só uma parte de cada símbolo aparece escura por vez e o destaque percorre os caminhos: no Wi-Fi o arco maior em q001 e q004, o menor em q002 e q005 e o ponto da base em q003, q006 e q009, com o mesmo rodízio nas ondas do alto-falante e nas gotas do aspersor (vídeo __047, folhas 0001 a 0003). No breathe a opacidade vai de preto a cinza claro e volta em ciclos de cerca de 2 segundos, um símbolo por vez em rodízio: onda sonora na folha 0001, balão de tradução de q014 a q024 e alvo de anéis de q025 a q036 (vídeo __051, folhas 0001 a 0004).
- O replace troca o símbolo inteiro em cada posição, de forma escalonada: a grade encolhe em q002 e vira lista em q003, a nuvem de chuva clareia em q004 e vira nuvem com sol em q005, o círculo com X surge claro em q006 no lugar do microfone, e tudo volta ao original em q010 (vídeo __048, folhas 0001 e 0002). O Magic Replace acrescenta e remove elementos sobre a mesma forma: cartão com triângulo de alerta desde q001, barra diagonal no microfone a partir de q003, selo trocado de check para X em q006, triângulo removido em q007, barra e X revertidos em q012 e estado original em q013 (vídeo __049, folhas 0001 e 0002).
- No rotate só uma parte de cada símbolo gira enquanto o resto fica fixo: os raios internos da engrenagem dentro do contorno dentado, as pás do ventilador sobre base e moldura, e os dois pontos da órbita ao redor do centro e dos anéis, aparentemente em velocidades diferentes; ao contrário do breathe, os três giram ao mesmo tempo até o último quadro q015 (vídeo __052, folhas 0001 e 0002).
Divergências registradas: a imagem de multicolor reaproveita a fileira de oito símbolos em vez dos exemplos de folha verde e lixeira com barra da descrição oficial, e o oitavo símbolo sai cortado na borda, sem cor confirmável (img 1010); no bounce (vídeo __044, q001 a q015) e no wiggle (vídeo __050, q001 a q009) os quadros não mostram diferença de escala, posição ou rotação, então o movimento descrito não é confirmado nem contradito; no breathe a descrição oficial fala em crescer e encolher junto com a opacidade, mas só a variação de opacidade é perceptível nos quadros (vídeo __051); na cor variável animada não foi possível identificar o quadro em que o ciclo reverte (vídeo __047).
<!-- /visual:sf-symbols -->

## Spatial layout (slug: spatial-layout)

O que governa: técnicas de layout espacial para aproveitar a tela infinita do Apple Vision Pro, cobrindo campo de visão, profundidade e escala de conteúdo.

Por que: as pessoas percebem profundidade e se orientam no espaço através de pistas visuais como distância, oclusão e sombra; o objetivo do layout espacial é apresentar conteúdo de forma envolvente e confortável, evitando desconforto visual, sensação de confinamento ou desorientação.

Faça e evite:
- O sistema não fornece informação sobre o campo de visão real da pessoa (varia conforme a configuração do Light Seal e a acuidade periférica de cada um).
- Centralize conteúdo importante dentro do campo de visão; por padrão o visionOS já lança o app diretamente à frente da pessoa. Em experiências imersivas, mantenha o conteúdo importante centralizado e evite mostrar movimento distrativo ou objetos brilhantes e de alto contraste na periferia.
- Evite ancorar conteúdo à cabeça da pessoa (head-anchored); embora o app deva em geral ficar dentro do campo de visão, ancorar conteúdo de forma estática à frente da pessoa pode causar sensação de confinamento e desconforto, principalmente se obscurece muito passthrough. Prefira ancorar o conteúdo no espaço da pessoa, permitindo que ela olhe livremente ao redor.
- Incorpore pequenas quantidades de profundidade em toda a interface, mesmo em janelas padrão, para parecer mais natural, já que as pessoas podem ver o conteúdo de qualquer ângulo; o SwiftUI já adiciona efeitos visuais que dão essa sensação de profundidade em janelas 2D.
- Para profundidade adicional, use RealityKit para criar objetos 3D, exibidos livremente ou dentro de um volume (componente que mostra conteúdo 3D, similar a uma janela mas sem moldura visível).
- Forneça pistas visuais que comuniquem a profundidade do conteúdo com precisão; pistas ausentes ou conflitantes com a experiência real do mundo causam desconforto visual.
- Use profundidade para comunicar hierarquia, já que um objeto que se destaca em profundidade fica mais perceptível; as pessoas notam mudanças de profundidade, como quando um sheet aparece sobre uma janela e a janela recua no eixo z.
- Em geral, evite adicionar profundidade ao texto, pois texto que parece flutuar sobre o fundo é difícil de ler, o que atrasa a leitura e pode causar desconforto visual.
- Garanta que a profundidade agregue valor: use-a para separar visualmente elementos grandes e importantes (como tab bar ou toolbar se destacando de uma janela), mas evite em objetos pequenos, como o símbolo de um botão, pois isso pode reduzir legibilidade e usabilidade; reveja também a frequência de mudanças de profundidade no app, já que as pessoas precisam refocar os olhos a cada diferença de profundidade, o que cansa se ocorrer com muita frequência.
- visionOS define dois tipos de escala: dynamic scale (o sistema aumenta a escala de uma janela conforme ela se afasta da pessoa e diminui conforme se aproxima, mantendo o tamanho aparente constante em qualquer distância) e fixed scale (o objeto mantém a mesma escala independentemente da proximidade, parecendo menor quando distante, como um objeto físico).
- Para suportar escala dinâmica e a aparência de profundidade, visionOS define um ponto como um ângulo, diferente de outras plataformas, que definem um ponto como número de pixels variável conforme a resolução de uma tela 2D.
- Considere usar fixed scale quando quiser que um objeto virtual pareça exatamente como um objeto físico (por exemplo, manter a escala real de um produto); prefira aplicar fixed scale com moderação, reservando-a para objetos não interativos, já que conteúdo interativo precisa escalar para manter usabilidade conforme se aproxima ou se afasta.
- Evite exibir muitas janelas; isso pode obscurecer o entorno da pessoa, causando sensação de sobrecarga, confinamento e desconforto, além de dificultar mover o app.
- Priorize gestos indiretos padrão, que não exigem que a pessoa mova a mão para dentro do campo de visão; gestos diretos, que exigem tocar o objeto virtual com o dedo, podem cansar, especialmente se o objeto está na linha de visão ou acima dela; reserve gestos diretos para objetos próximos que convidam a inspeção ou manipulação de perto por curtos períodos.
- A Digital Crown recentraliza janelas no campo de visão da pessoa sem que o app precise fazer nada.
- Inclua espaço suficiente ao redor de componentes interativos para facilitar o olhar sobre eles, já que o visionOS mostra um efeito de hover visual quando a pessoa olha para um elemento; posicione múltiplos componentes visionOS de tamanho regular com centros a pelo menos 60 pontos de distância entre si, deixando 16 pontos ou mais de espaço entre eles; não deixe controles se sobreporem a outros elementos ou views interativos.
- Permita que as pessoas usem o app com movimento físico mínimo ou nenhum, a menos que algum movimento seja essencial à experiência.
- Use o chão para posicionar uma experiência imersiva grande, alinhando o plano horizontal com o chão físico, ajudando o conteúdo a se misturar de forma intuitiva com o entorno.

Especificações exatas: espaçamento mínimo de 60 pontos entre os centros de componentes visionOS de tamanho regular, com 16 pontos ou mais de espaço entre eles.

Diferenças por plataforma: não suportado em iOS, iPadOS, macOS, tvOS ou watchOS; toda a orientação deste artigo é exclusiva de visionOS.

Ligações com outros artigos: Eyes, Layout, Immersive experiences.

<!-- visual:spatial-layout -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações (img 1096 a 1098) e 8 folhas de vídeo de 5 vídeos (054, 055, 056, 057, 058), todas abertas e com códigos conferidos.
- A abertura da página usa fundo amarelo sólido com grade de linhas tracejadas e duas circunferências concêntricas sob um pictograma laranja de três setas saindo de um ponto central, sugerindo os eixos de um espaço tridimensional sem nenhum rótulo (img 1096).
- O campo de visão é desenhado como três circunferências concêntricas laranja, rotuladas 30°, 60° e 90°, partindo de um ponto fora do quadro à esquerda, implicitamente a posição da pessoa, sobre o render de uma sala de estar; a janela translúcida do app fica quase toda dentro do círculo de 60°, com as bordas laterais chegando perto do de 90° (img 1097).
- Em uma janela 2D padrão (Notes no visionOS), de cantos arredondados, a profundidade é sugerida só por uma leve elevação com sombra que separa a janela do fundo desfocado, sem deslocar camadas dentro dela; lista de pastas e notas à esquerda e a nota aberta à direita no mesmo painel (img 1098).
- No vídeo 054 (folha 0001, q001 a q006), em desenho de linha sobre fundo escuro, a pessoa sentada ereta com headset aparece sozinha em q001, um painel azul vertical surge em q002 em posições que variam de quadro a quadro, e a linha pontilhada azul que sai da altura dos olhos só aparece em q004, cresce em q005 e toca a borda do painel em q006.
- No vídeo 055 (folha 0001, q001 a q006), com a pessoa reclinada numa poltrona com apoio de pés, o painel já nasce elevado acima e à frente dela e inclinado em sua direção; a linha pontilhada surge em q004 e em q006 quase alcança a borda inferior. Comparado ao 054, o que muda com a postura é a orientação do painel: vertical para quem está ereto, inclinado para quem está reclinado.
- No vídeo 056 (folhas 0001 e 0002), um satélite 3D flutua num volume dentro de uma sala fotorrealista; em q001 ele é pequeno e tem abaixo um indicador "Scene" com barra de progresso pontilhada, que some em q002; o objeto cresce rapidamente até quase tocar as bordas laterais com os painéis solares (q004), o ângulo de visão ainda muda em q005 e q006, e de q007 a q013 ele mantém o tamanho grande, com variações sobretudo de rotação e de reflexo de luz nos painéis solares.
- Escala dinâmica, no vídeo 057 (folhas 0001 e 0002): numa cena de teste cinza claro com piso quadriculado, uma janela branca arredondada (ícone circular no canto superior direito, barrinha sob a base) ganha em q004 um contorno amarelo vazado que marca a posição e o tamanho originais, ligado ao chão por uma linha diagonal amarela; de q005 a q012 a janela real se afasta desse contorno e fica maior, em q013 surge o rótulo "Dynamic Scale", e em q016 as duas formas se fundem numa só, com borda amarela e linha agora vertical.
- Escala fixa, no vídeo 058 (folhas 0001 e 0002): mesma cena e mesma janela; o contorno amarelo de referência aparece em q003 maior que a janela, que encolhe a cada quadro enquanto o contorno mantém o tamanho até q009; em q010 surge o rótulo "Fixed Scale", na folha 0002 o conjunto inteiro parece recuar no quadro, em q013 a linha fica totalmente vertical e em q014 a janela está minúscula e centralizada dentro do contorno.
- Os vídeos 057 e 058 seguem a mesma construção didática: referência vazada fixa contra objeto real preenchido, linha amarela que passa de diagonal a vertical ao final (sugerindo que o ambiente gira para reapresentar a cena de frente) e legenda de texto que só entra na segunda metade, depois de o efeito já ter sido mostrado.
Divergências registradas: na img 1098 a nota aberta não aparece como janela separada posicionada ao lado, como a descrição oficial sugere, e sim no lado direito do mesmo painel. No vídeo 054 os quadros parados a cada 0,5 s não mostram a janela centralizada de forma estável, e só q006 traz a linha completa; no 055 a linha não toca visivelmente o painel em nenhum dos seis quadros. No vídeo 056 a manipulação da orientação do satélite não se distingue como gesto de arrastar nos quadros estáticos, parecendo rotação automática ou de câmera, e o indicador "Scene" não consta da descrição oficial. Os rótulos "Dynamic Scale" (057) e "Fixed Scale" (058) também não são mencionados nas descrições oficiais.
<!-- /visual:spatial-layout -->

## Writing (slug: writing)

O que governa: as escolhas de palavras, voz, tom e padrões de linguagem dentro do app, cobrindo desde onboarding até mensagens de erro e labels de configuração.

Por que: as palavras usadas no app são parte essencial da experiência do usuário; a voz consistente e um tom adequado a cada contexto ajudam o app a parecer coeso, confiável e bem projetado, além de guiar a pessoa com clareza através das tarefas.

Faça e evite:
- Determine a voz do app pensando em com quem está falando e no tipo de vocabulário familiar às pessoas que o usam; crie uma lista de termos comuns e use-a como referência para manter a linguagem consistente.
- Ajuste o tom conforme o contexto situacional, considerando o que a pessoa está fazendo tanto no mundo físico quanto dentro do app (por exemplo, tom direto e sério para uma queda detectada versus tom leve e parabenizante para uma conquista de atividade).
- Seja claro: escolha palavras facilmente compreensíveis, revise cada palavra para confirmar que é necessária, use menos palavras quando possível, e leia o texto em voz alta na dúvida.
- Escreva para todos: use linguagem simples e direta, escreva pensando em acessibilidade e localização, evitando jargão e terminologia de gênero.
- Considere o propósito de cada tela, priorizando a informação mais importante primeiro; se houver mais de uma ideia, considere dividir o texto em várias telas e pense no fluxo de informação entre elas.
- Seja orientado à ação: use voz ativa e labels claros nos botões, quase sempre com um verbo (por exemplo "Send" costuma funcionar melhor que "Let's do it!"); evite "Click here" em links, preferindo frases descritivas como "Learn more about UX Writing", especialmente importante para pessoas que usam leitores de tela.
- Construa padrões de linguagem consistentes ao longo do app, o que facilita a familiaridade e também facilita escrever para o app no futuro.
- Adote regras de capitalização alinhadas ao estilo do app e aplique-as de forma consistente; title case tende a soar mais formal, sentence case mais casual; escolha um estilo por tipo de elemento de UI e mantenha (por exemplo, title case para todos os alertas ou sentence case para todos os headlines).
- Dê orientação clara e use linguagem consistente em fluxos com múltiplas etapas: comece com algo como "Get Started" para indicar o início do fluxo, use "Continue" ou "Next" (de forma consistente) para avançar, e deixe claro quando o fluxo termina com algo como "Done".
- Use pronomes possessivos com moderação (my, your); por exemplo "Favorites" comunica o mesmo que "Your Favorites" de forma mais concisa; se usar, use de forma consistente e sem trocar de perspectiva; evite usar "we" por completo, pois pode ficar ambíguo quem é o "nós", especialmente em mensagens de erro (prefira "Unable to load content" a "We're having trouble loading this content").
- Escreva pensando em como as pessoas usam cada dispositivo: mantenha a linguagem consistente entre dispositivos, mas ajuste o texto conforme apropriado; descreva gestos corretamente em cada dispositivo (não dizer "click" em um dispositivo touch como iPhone ou iPad, onde o correto é "tap").
- iPhone e Apple Watch, por terem telas pequenas, oferecem oportunidades de personalização mas exigem brevidade; TVs costumam ficar em espaços comuns, vistas por várias pessoas ao mesmo tempo, e telas maiores também exigem brevidade porque o texto precisa ser grande o suficiente para ser lido à distância.
- Forneça próximos passos claros em telas vazias (empty states), que também podem mostrar a voz do app, mas o conteúdo precisa ser útil e adequado ao contexto; guie a pessoa com ações possíveis, com um botão ou link quando possível; lembre que empty states costumam ser temporários, então não mostre ali informação crucial que depois vai desaparecer.
- Escreva mensagens de erro claras: o ideal é ajudar a evitar o erro; quando a mensagem for necessária, exiba-a o mais perto possível do problema, evite culpar a pessoa, e seja claro sobre o que ela pode fazer para corrigir (por exemplo, "Choose a password with at least 8 characters" é mais útil que "That password is too short"); interjeições como "oops!" ou "uh-oh" costumam ser desnecessárias e podem soar insinceras; se a linguagem sozinha não resolver um erro que afeta muitas pessoas, use isso como oportunidade para repensar a interação.
- Escolha o método de entrega certo (alerta, notificação, action sheet etc.) considerando urgência, importância, contexto e quanta informação de apoio a pessoa precisa, com tom apropriado à situação.
- Mantenha labels de configurações claros e simples, o mais práticos possível; se o label não bastar, adicione uma explicação descrevendo o que acontece quando ligado (a pessoa infere o oposto); se precisar direcionar alguém a uma configuração, forneça um link ou botão direto em vez de tentar descrever a localização.
- Mostre dicas em campos de texto: rotule os campos com clareza e use texto de dica ou placeholder (como um exemplo "name@example.com" ou uma descrição "Your name"); mostre erros bem ao lado do campo e instrua como preencher corretamente, em vez de repreender por não seguir as regras ("Use only letters for your name" é melhor que "Don't use numbers or symbols"); evite mensagens de erro robóticas sem informação útil, como "Invalid name".

Especificações exatas: nenhum número, medida ou valor exato foi fornecido neste artigo.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Apple Style Guide, Writing inclusively, Inclusion, Accessibility, Color, Notifications, Alerts, Action sheets, Settings, Text fields, VoiceOver, Localization.

<!-- visual:writing -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações (img 1338 a 1341) vista, código conferido; a página não tem vídeo.
- A abertura é monocromática amarela: uma prancheta de cantos arredondados atravessada na diagonal por um lápis, sobreposta a linhas de grade retangulares e a um círculo guia central, na mesma lógica de grade das aberturas de outras páginas (img 1338).
- A mensagem séria de queda no Apple Watch é montada com fundo em degradê azul e roxo escuro, hora no topo com um X para fechar, uma frase curta e declarativa centralizada, sem emoji, e dois botões empilhados: "EMERGENCY SOS", com círculo vermelho à esquerda, acima de "I'm OK", em degradê roxo e rosa; a ação de emergência fica antes da ação de dispensar (img 1339).
- A mensagem leve de conquista usa anel de atividade colorido no canto superior esquerdo, hora e "now" no topo, um título curto seguido de frase com número concreto (35 dias) e ponto de exclamação, sobre fundo colorido desfocado em rosa, roxo e verde (img 1340).
- Comparadas, as duas telas mostram que o tom não vem só das palavras: cor de fundo, temperatura e composição mudam junto, escuro e frio com botão de emergência na situação grave, vibrante com anel de conquista na comemoração (img 1339 e img 1340).
- O rótulo de configuração aparece como cartão em fundo preto, título curto à esquerda e interruptor verde ligado à direita, com uma frase de apoio em cinza claro abaixo que descreve só o que acontece com a função ligada, sem explicar o estado desligado (img 1341).
<!-- /visual:writing -->

## Typography (slug: typography)

O que governa: as escolhas tipográficas do sistema (tamanhos, hierarquia, famílias de fontes San Francisco e New York, text styles, Dynamic Type) que garantem legibilidade e expressam a marca do app, incluindo as tabelas completas de especificação de tamanho, leading e tracking por plataforma.

Por que: escolhas tipográficas ajudam a exibir texto legível, transmitir hierarquia de informação, comunicar conteúdo importante e expressar marca ou estilo. As pessoas precisam ler o conteúdo em diferentes distâncias de visualização e condições variadas; por isso o sistema define tamanhos padrão e mínimos recomendados por plataforma, tanto para fontes customizadas quanto de sistema. Text styles formam uma hierarquia tipográfica que permite escalar texto proporcionalmente quando as pessoas mudam o tamanho de texto do sistema ou ativam ajustes de acessibilidade.

Faça e evite:
- Use tamanhos de fonte que a maioria das pessoas consegue ler facilmente, seguindo os tamanhos padrão e mínimos recomendados por plataforma; se usar fonte customizada de peso fino, mire tamanhos maiores que os recomendados para aumentar a legibilidade.
- Teste a legibilidade em diferentes contextos, inclusive em jogos, em cada plataforma suportada; se o texto estiver difícil de ler, considere tamanho maior, mais contraste entre texto e fundo, ou tipografias projetadas para legibilidade otimizada, como as fontes do sistema.
- Em geral, evite pesos de fonte leves: ao usar fontes do sistema, prefira os pesos Regular, Medium, Semibold ou Bold, e evite Ultralight, Thin e Light, que podem ser difíceis de ver, especialmente em texto pequeno.
- Ajuste peso, tamanho e cor da fonte para enfatizar informação importante e ajudar a visualizar hierarquia, mantendo a hierarquia relativa e a distinção visual dos elementos de texto mesmo quando as pessoas ajustam o tamanho do texto.
- Minimize o número de tipografias usadas, mesmo em uma interface bastante customizada; misturar tipografias demais obscurece a hierarquia de informação e prejudica a legibilidade, além de deixar a interface com aparência inconsistente.
- Priorize o conteúdo importante ao responder a mudanças de tamanho de texto; nem todo conteúdo é igualmente importante (por exemplo, ao aumentar o tamanho de texto em uma janela com abas, não se espera que os títulos das abas aumentem também).
- A Apple fornece duas famílias tipográficas: San Francisco (SF), sem serifa, com variantes SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew e SF Mono, além de variantes arredondadas de várias delas; e New York (NY), com serifa, projetada para funcionar bem sozinha ou junto com as fontes SF. Ambas estão disponíveis em formato de fonte variável, que combina diferentes estilos em um único arquivo e permite interpolação entre estilos.
- As fontes do sistema suportam tamanhos ópticos dinâmicos, mesclando tamanhos ópticos discretos (como Text e Display) e pesos em um design contínuo único, o que dispensa a escolha de tamanho óptico discreto, exceto ao usar uma ferramenta de design que não suporte todos os recursos do formato de fonte variável.
- Os text styles definem uma combinação de peso de fonte, tamanho de ponto e valores de leading para cada tamanho de texto (por exemplo, body prioriza leitura confortável em várias linhas; headline usa tamanho e peso que distinguem um título do conteúdo ao redor); considere usar os text styles nativos para consistência e para suporte automático a Dynamic Type.
- É possível modificar os text styles nativos usando symbolic traits definidos pelas APIs do sistema, como o trait bold, que adiciona peso ao texto criando outro nível de hierarquia, ou ajustes de leading (loose leading, mais espaço entre linhas, ajuda em colunas largas ou passagens longas; tight leading, menos espaço, ajuda a caber texto em áreas de altura restrita, como uma linha de lista); evite tight leading quando o texto tiver três ou mais linhas, mesmo em áreas de altura limitada.
- Use as constantes definidas em Font.Design para acessar as fontes do sistema; não incorpore (embed) fontes do sistema no app ou jogo.
- Ao produzir um mockup fiel de interface que usa as fontes variáveis do sistema, pode ser necessário ajustar o tracking, já que em um app rodando o sistema ajusta o tracking dinamicamente em cada tamanho de ponto.
- Ao usar fonte customizada, garanta legibilidade seguindo os tamanhos mínimos recomendados por estilo e peso; implemente os mesmos comportamentos de acessibilidade que as fontes do sistema já suportam automaticamente (Dynamic Type onde disponível, resposta a recursos como Bold Text); em jogos baseados em Unity, é possível usar os plug-ins da Apple para Unity para suportar Dynamic Type, ou, se o plug-in não for apropriado, permitir ajuste de tamanho de texto por outros meios.
- Dynamic Type é um recurso em nível de sistema (iOS, iPadOS, tvOS, visionOS, watchOS) que permite às pessoas ajustar o tamanho do texto visível no dispositivo para legibilidade e conforto.
- Garanta que o layout do app se adapte a todos os tamanhos de fonte; verifique se o design escala e se texto e glifos permanecem legíveis em todos os tamanhos, inclusive nos tamanhos de acessibilidade maiores (testável em Settings > Accessibility > Display & Text Size > Larger Text).
- Aumente o tamanho de ícones de interface significativos conforme o tamanho de fonte aumenta; ao usar SF Symbols, os ícones já escalam automaticamente com as mudanças de tamanho do Dynamic Type.
- Mantenha o truncamento de texto ao mínimo conforme o tamanho de fonte aumenta; em geral, procure exibir tanto texto útil no maior tamanho de acessibilidade quanto no maior tamanho padrão; evite truncar texto em regiões roláveis, a menos que a pessoa possa abrir uma view separada para ler o resto.
- Considere ajustar o layout em tamanhos de fonte grandes: em contextos com restrição horizontal, itens inline (como glifos e timestamps) e limites de contêiner podem apertar o texto e causar truncamento ou sobreposição; considere um layout empilhado, com texto acima de itens secundários; texto em múltiplas colunas também pode ficar menos legível em tamanhos grandes por restrição de espaço horizontal, então reduza o número de colunas conforme o tamanho de fonte aumenta.
- Mantenha uma hierarquia de informação consistente independentemente do tamanho de fonte atual, mantendo elementos primários no topo da view mesmo com fonte muito grande.

Especificações exatas:

Tamanhos padrão e mínimo de fonte por plataforma: iOS/iPadOS padrão 17 pt, mínimo 11 pt; macOS padrão 13 pt, mínimo 10 pt; tvOS padrão 29 pt, mínimo 23 pt; visionOS padrão 17 pt, mínimo 12 pt; watchOS padrão 16 pt, mínimo 12 pt.

Pesos emphasized (symbolic traits) podem ser medium, semibold, bold ou heavy conforme o text style.

Tabelas de Dynamic Type iOS/iPadOS (estilo, peso, tamanho em pontos, leading em pontos, peso emphasized), por tamanho de categoria:
- xSmall: Large Title 31/38 Bold; Title 1 25/31 Bold; Title 2 19/24 Bold; Title 3 17/22 Semibold; Headline (Semibold) 14/19 Semibold; Body 14/19 Semibold; Callout 13/18 Semibold; Subhead 12/16 Semibold; Footnote 12/16 Semibold; Caption 1 11/13 Semibold; Caption 2 11/13 Semibold.
- Small: Large Title 32/39 Bold; Title 1 26/32 Bold; Title 2 20/25 Bold; Title 3 18/23 Semibold; Headline 15/20 Semibold; Body 15/20 Semibold; Callout 14/19 Semibold; Subhead 13/18 Semibold; Footnote 12/16 Semibold; Caption 1 11/13 Semibold; Caption 2 11/13 Semibold.
- Medium: Large Title 33/40 Bold; Title 1 27/33 Bold; Title 2 21/26 Bold; Title 3 19/24 Semibold; Headline 16/21 Semibold; Body 16/21 Semibold; Callout 15/20 Semibold; Subhead 14/19 Semibold; Footnote 12/16 Semibold; Caption 1 11/13 Semibold; Caption 2 11/13 Semibold.
- Large (padrão): Large Title 34/41 Bold; Title 1 28/34 Bold; Title 2 22/28 Bold; Title 3 20/25 Semibold; Headline 17/22 Semibold; Body 17/22 Semibold; Callout 16/21 Semibold; Subhead 15/20 Semibold; Footnote 13/18 Semibold; Caption 1 12/16 Semibold; Caption 2 11/13 Semibold.
- xLarge: Large Title 36/43 Bold; Title 1 30/37 Bold; Title 2 24/30 Bold; Title 3 22/28 Semibold; Headline 19/24 Semibold; Body 19/24 Semibold; Callout 18/23 Semibold; Subhead 17/22 Semibold; Footnote 15/20 Semibold; Caption 1 14/19 Semibold; Caption 2 13/18 Semibold.
- xxLarge: Large Title 38/46 Bold; Title 1 32/39 Bold; Title 2 26/32 Bold; Title 3 24/30 Semibold; Headline 21/26 Semibold; Body 21/26 Semibold; Callout 20/25 Semibold; Subhead 19/24 Semibold; Footnote 17/22 Semibold; Caption 1 16/21 Semibold; Caption 2 15/20 Semibold.
- xxxLarge: Large Title 40/48 Bold; Title 1 34/41 Bold; Title 2 28/34 Bold; Title 3 26/32 Semibold; Headline 23/29 Semibold; Body 23/29 Semibold; Callout 22/28 Semibold; Subhead 21/28 Semibold; Footnote 19/24 Semibold; Caption 1 18/23 Semibold; Caption 2 17/22 Semibold.
Base de tamanho de ponto: resolução de imagem de 144 ppi para @2x e 216 ppi para @3x.

Tamanhos de acessibilidade maiores iOS/iPadOS (AX1 a AX5), mesmo formato:
- AX1: Large Title 44/52 Bold; Title 1 38/46 Bold; Title 2 34/41 Bold; Title 3 31/38 Semibold; Headline 28/34 Semibold; Body 28/34 Semibold; Callout 26/32 Semibold; Subhead 25/31 Semibold; Footnote 23/29 Semibold; Caption 1 22/28 Semibold; Caption 2 20/25 Semibold.
- AX2: Large Title 48/57 Bold; Title 1 43/51 Bold; Title 2 39/47 Bold; Title 3 37/44 Semibold; Headline 33/40 Semibold; Body 33/40 Semibold; Callout 32/39 Semibold; Subhead 30/37 Semibold; Footnote 27/33 Semibold; Caption 1 26/32 Semibold; Caption 2 24/30 Semibold.
- AX3: Large Title 52/61 Bold; Title 1 48/57 Bold; Title 2 44/52 Bold; Title 3 43/51 Semibold; Headline 40/48 Semibold; Body 40/48 Semibold; Callout 38/46 Semibold; Subhead 36/43 Semibold; Footnote 33/40 Semibold; Caption 1 32/39 Semibold; Caption 2 29/35 Semibold.
- AX4: Large Title 56/66 Bold; Title 1 53/62 Bold; Title 2 50/59 Bold; Title 3 49/58 Semibold; Headline 47/56 Semibold; Body 47/56 Semibold; Callout 44/52 Semibold; Subhead 42/50 Semibold; Footnote 38/46 Semibold; Caption 1 37/44 Semibold; Caption 2 34/41 Semibold.
- AX5: Large Title 60/70 Bold; Title 1 58/68 Bold; Title 2 56/66 Bold; Title 3 55/65 Semibold; Headline 53/62 Semibold; Body 53/62 Semibold; Callout 51/60 Semibold; Subhead 49/58 Semibold; Footnote 44/52 Semibold; Caption 1 43/51 Semibold; Caption 2 40/48 Semibold.

Text styles macOS (peso, tamanho em pontos, altura de linha em pontos, peso emphasized), base 144 ppi @2x: Large Title Regular 26/32 Bold; Title 1 Regular 22/26 Bold; Title 2 Regular 17/22 Bold; Title 3 Regular 15/20 Semibold; Headline Bold 13/16 Heavy; Body Regular 13/16 Semibold; Callout Regular 12/15 Semibold; Subheadline Regular 11/14 Semibold; Footnote Regular 10/13 Semibold; Caption 1 Regular 10/13 Medium; Caption 2 Medium 10/13 Semibold.

Text styles tvOS (peso, tamanho, leading, emphasized), base 72 ppi @1x e 144 ppi @2x: Title 1 Medium 76/96 Bold; Title 2 Medium 57/66 Bold; Title 3 Medium 48/56 Bold; Headline Medium 38/46 Bold; Subtitle 1 Regular 38/46 Medium; Callout Medium 31/38 Bold; Body Medium 29/36 Bold; Caption 1 Medium 25/32 Bold; Caption 2 Medium 23/30 Bold.

Dynamic Type watchOS (peso, tamanho, leading, emphasized), por tamanho de mostrador:
- xSmall: Large Title 30/32,5 Bold; Title 1 28/30,5 Semibold; Title 2 24/26,5 Semibold; Title 3 17/19,5 Semibold; Headline 14/16,5 Semibold; Body 14/16,5 Semibold; Caption 1 13/15,5 Semibold; Caption 2 12/14,5 Semibold; Footnote 1 11/13,5 Semibold; Footnote 2 10/12,5 Semibold.
- Small (padrão 38mm): Large Title 32/34,5 Bold; Title 1 30/32,5 Semibold; Title 2 26/28,5 Semibold; Title 3 18/20,5 Semibold; Headline 15/17,5 Semibold; Body 15/17,5 Semibold; Caption 1 14/16,5 Semibold; Caption 2 13/15,5 Semibold; Footnote 1 12/14,5 Semibold; Footnote 2 11/13,5 Semibold.
- Large (padrão 40mm/41mm/42mm): Large Title 36/38,5 Bold; Title 1 34/36,5 Semibold; Title 2 28/30,5 Semibold; Title 3 19/21,5 Semibold; Headline 16/18,5 Semibold; Body 16/18,5 Semibold; Caption 1 15/17,5 Semibold; Caption 2 14/16,5 Semibold; Footnote 1 13/15,5 Semibold; Footnote 2 12/14,5 Semibold.
- xLarge (padrão 44mm/45mm/49mm): Large Title 40/42,5 Bold; Title 1 38/40,5 Semibold; Title 2 30/32,5 Semibold; Title 3 20/22,5 Semibold; Headline 17/19,5 Semibold; Body 17/19,5 Semibold; Caption 1 16/18,5 Semibold; Caption 2 15/17,5 Semibold; Footnote 1 14/16,5 Semibold; Footnote 2 13/15,5 Semibold.
- xxLarge: Large Title 41/43,5 Bold; Title 1 39/41,5 Semibold; Title 2 31/33,5 Semibold; Title 3 21/23,5 Semibold; Headline 18/20,5 Semibold; Body 18/20,5 Semibold; Caption 1 17/19,5 Semibold; Caption 2 16/18,5 Semibold; Footnote 1 15/17,5 Semibold; Footnote 2 14/16,5 Semibold.
- xxxLarge: Large Title 42/44,5 Bold; Title 1 40/42,5 Semibold; Title 2 32/34,5 Semibold; Title 3 22/24,5 Semibold; Headline 19/21,5 Semibold; Body 19/21,5 Semibold; Caption 1 18/20,5 Semibold; Caption 2 17/19,5 Semibold; Footnote 1 16/18,5 Semibold; Footnote 2 15/17,5 Semibold.

Tamanhos de acessibilidade maiores watchOS (AX1 a AX3):
- AX1: Large Title 44/46,5 Bold; Title 1 42/44,5 Semibold; Title 2 34/41 Semibold; Title 3 24/26,5 Semibold; Headline 21/23,5 Semibold; Body 21/23,5 Semibold; Caption 1 18/20,5 Semibold; Caption 2 17/19,5 Semibold; Footnote 1 16/18,5 Semibold; Footnote 2 15/17,5 Semibold.
- AX2: Large Title 45/47,5 Bold; Title 1 43/46 Semibold; Title 2 35/37,5 Semibold; Title 3 25/27,5 Semibold; Headline 22/24,5 Semibold; Body 22/24,5 Semibold; Caption 1 19/21,5 Semibold; Caption 2 18/20,5 Semibold; Footnote 1 17/19,5 Semibold; Footnote 2 16/17,5 Semibold.
- AX3: Large Title 46/48,5 Bold; Title 1 44/47 Semibold; Title 2 36/38,5 Semibold; Title 3 26/28,5 Semibold; Headline 23/25,5 Semibold; Body 23/25,5 Semibold; Caption 1 20/22,5 Semibold; Caption 2 19/21,5 Semibold; Footnote 1 18/20,5 Semibold; Footnote 2 17/19,5 Semibold.

Tabelas de tracking (valores em 1/1000 em e em pontos, por tamanho de ponto de 6 a 96 ou mais) foram fornecidas integralmente no texto original para: SF Pro (iOS, iPadOS, visionOS), SF Pro Rounded, New York (variando de 6 a 260 pt), macOS (idêntica à tabela SF Pro), tvOS (idêntica à tabela SF Pro), SF Compact (watchOS) e SF Compact Rounded (watchOS). Como exemplo de amplitude: em SF Pro, o tracking varia de +41 (1/1000 em, +0,24 pt) em 6 pt até 0 em tamanhos de 80 pt ou mais; em New York, o tracking chega a -18 (1/1000 em, -4,57 pt) em 260 pt. Os valores completos, tamanho a tamanho, estão na fonte original e não foram reproduzidos linha a linha aqui por serem tabelas extensas de referência técnica; qualquer implementação que precise do valor exato de tracking para um tamanho de ponto específico deve consultar a fonte original ou o arquivo de texto já baixado.

Diferenças por plataforma:
- iOS, iPadOS: SF Pro é a fonte do sistema; apps também podem usar NY.
- macOS: SF Pro é a fonte do sistema; NY está disponível para apps Mac construídos com Mac Catalyst; macOS não suporta Dynamic Type. Quando necessário, use as variantes dinâmicas de fonte do sistema para igualar o texto de controles padrão: Control content (controlContentFont(ofSize:)), Label (labelFont(ofSize:)), Menu (menuFont(ofSize:)), Menu bar (menuBarFont(ofSize:)), Message (messageFont(ofSize:)), Palette (paletteFont(ofSize:)), Title (titleBarFont(ofSize:)), Tool tips (toolTipsFont(ofSize:)), Document text/user (userFont(ofSize:)), Monospaced document text/user fixed pitch (userFixedPitchFont(ofSize:)), Bold system font (boldSystemFont(ofSize:)), System font (systemFont(ofSize:)).
- tvOS: SF Pro é a fonte do sistema; apps também podem usar NY.
- visionOS: SF Pro é a fonte do sistema; ao usar NY, é preciso especificar os type styles desejados. visionOS usa versões mais bold dos estilos Dynamic Type body e title, e introduz Extra Large Title 1 e Extra Large Title 2 para layouts editoriais largos. Em geral, prefira texto 2D: quanto mais profundidade visual os caracteres têm, mais difícil fica a leitura; um pouco de texto 3D pode ser divertido, mas para conteúdo que as pessoas precisam ler e entender, prefira texto com pouca ou nenhuma profundidade visual. Teste a legibilidade do texto em diferentes escalas. Maximize o contraste entre texto e fundo do contêiner; por padrão o sistema exibe texto em branco, pois costuma contrastar bem com o material de fundo padrão. Se exibir texto sem fundo, considere deixá-lo em negrito para melhorar legibilidade, evitando sombras para aumentar contraste, já que o espaço atual pode não ter uma superfície visual para projetar sombra de forma precisa. Mantenha o texto voltado para a pessoa sempre que possível (billboarding), fazendo com que a linha de base do texto permaneça perpendicular à linha de visão da pessoa conforme ela se move.
- watchOS: SF Compact é a fonte do sistema; apps também podem usar NY; em complicações, watchOS usa SF Compact Rounded.

Ligações com outros artigos: SF Symbols, Accessibility, Supporting Dynamic Type (seção interna referenciada como artigo relacionado), visionOS, Text input and output.

<!-- visual:typography -->
### O que as ilustrações mostram
Base: 4 folhas de ilustrações (img 1192 a 1204) vistas, códigos conferidos; a página não tem vídeo.
- A abertura expressa hierarquia pela tipografia: um "a" minúsculo pequeno ao lado de um "A" maiúsculo grande, em marrom escuro sobre amarelo mostarda que cobre a imagem inteira, com grade retangular, um círculo grande centrado na letra maior e linhas tracejadas marcando alinhamentos e proporções entre as duas (img 1192).
- Legibilidade em jogo é ensinada por um par de antes e depois com a mesma cena, ângulo e paleta no iPhone em paisagem: primeiro os nomes das plantas aparecem pequenos e sem fundo sobre um gradiente lilás e rosa; depois ficam maiores, dentro de cápsulas com fundo cinza translúcido, e o cartão "Plants Recorded 0/3" também ganha texto maior (img 1193 e img 1194).
- As duas famílias do sistema são comparadas com o mesmo pangrama e com duas linhas guia horizontais azuis marcando a altura da caixa alta e a linha de base: SF Pro em preto sobre branco (img 1195) e New York, serifada (img 1196).
- A escala de pesos é uma grade tipográfica pura, sem interface: a palavra "Text" repetida em duas linhas (Upright e Italics) por nove colunas de peso, de Ultralight a Black, com o itálico logo abaixo de cada peso (img 1197).
- A hierarquia de text styles numa tela real é mostrada com uma screenshot do Mail no iPhone anotada por rótulos externos e linhas retas: Large title aponta para "Inbox", Title para o nome do remetente, Subtitle para o assunto e Body text para o trecho do corpo do e-mail (img 1198).
- Dynamic Type aparece como a mesma mensagem de Mail em dois extremos. No tamanho padrão, avatar à esquerda, nome e data numa linha, destinatário e clipe na linha de baixo, assunto em negrito e corpo com quatro linhas (img 1199). No maior tamanho de acessibilidade, o nome quebra em duas linhas, destinatário e data ficam em linhas separadas, o assunto ocupa duas linhas grandes, o corpo é cortado logo no começo e os ícones do rodapé ficam sobrepostos ao texto (img 1200).
- No visionOS, o par certo e errado usa a mesma sala 3D e a mesma janela translúcida arredondada, variando só a profundidade da palavra "hello": em serifa branca plana, lida de frente e nítida (img 1201), contra letras com espessura e volume que ficam confusas e sobrepostas entre si (img 1203).
- As marcas de julgamento vêm isoladas em quadros próprios sobre fundo branco, sem sobrepor os exemplos: check branco em círculo verde para o uso correto (img 1202) e X branco em círculo cinza para o incorreto (img 1204).
<!-- /visual:typography -->

## O que este grupo revela sobre o jeito Apple

1. A Apple constrói hierarquia visual e de informação em camadas sobrepostas, nunca por acaso: Liquid Glass separa controles de conteúdo (materials), profundidade e escala comunicam importância em visionOS (spatial-layout), e os text styles formam uma escada tipográfica explícita de tamanho e peso (typography). A ideia de "camada funcional" versus "camada de conteúdo" se repete como princípio organizador central.

2. Toda decisão visual tem que sobreviver ao pior caso de acessibilidade antes de ser aprovada: cor vibrante sobre material para não depender de configurações do sistema (materials), Dynamic Type e AX1 a AX5 cobrindo até 70 pt de leading (typography), e movimento tratado como opcional, nunca único canal de informação (motion).

3. A Apple trata "realismo perceptivo" como critério de design, não estética: motion pede feedback que corresponda ao gesto físico da pessoa; spatial-layout usa pistas de profundidade (distância, oclusão, sombra) para evitar desconforto visual; right-to-left inverte ícones de movimento (como ondas sonoras) para preservar o sentido de "para frente".

4. Conforto físico e psicológico do usuário é tratado como requisito de engenharia, não nota de rodapé: em visionOS, oscilação de 0,2 Hz é citada com precisão de frequência (motion), gestos diretos são desencorajados por cansarem o braço (spatial-layout), e texto com profundidade é desaconselhado por atrasar a leitura (spatial-layout, typography).

5. A confiança da pessoa é protegida contra manipulação de interface por regras bem específicas e não apenas princípios vagos: privacy lista taxativamente designs proibidos em telas de pré-alerta de tracking (incentivos, imagem do próprio alerta, anotações apontando o botão), citando a cláusula exata da App Review Guidelines.

6. Onde a Apple permite customização, ela desenha o espaço de liberdade com precisão cirúrgica: o location button pode mudar título, glifo, cor de fundo e raio de canto, mas nada além disso (privacy); símbolos customizados devem seguir o template do sistema em nível de detalhe, peso óptico e alinhamento (sf-symbols).

7. A internacionalização (RTL, numerais, tipografia multi-idioma) é tratada como sistema de regras semânticas, não espelhamento mecânico: números nunca invertem a ordem interna dos dígitos mesmo em contexto RTL, mas invertem quando comunicam progresso; logotipos e marcas universais nunca são espelhados; fonte árabe ou hebraica ganha até 2 pontos a mais para equilibrar visualmente com maiúsculas latinas (right-to-left).

8. A tipografia do sistema (San Francisco e New York) e os símbolos (SF Symbols) são desenhados como uma única fundação técnica compartilhada: os nove pesos de símbolo correspondem exatamente aos pesos da fonte SF, permitindo "emparelhamento preciso de peso" entre ícone e texto adjacente (sf-symbols, typography).

9. A escrita (writing) é tratada com o mesmo rigor sistemático dado ao código visual: capitalização, pronomes possessivos e mensagens de erro seguem padrões explícitos e comparáveis (certo/errado) em vez de recomendações soltas, o que reforça que "voz do produto" é parte do sistema de design, não just copy solta.

10. Nas plataformas mais nichadas (visionOS, watchOS), a Apple assume responsabilidades extras de conforto físico do corpo humano que não existem nas plataformas de tela plana: watchOS embute easing obrigatório e não customizável em toda animação (motion); visionOS define distância mínima entre elementos interativos em pontos angulares, não em pixels (spatial-layout, typography).

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/materials.md, 123 linhas lidas de 123, sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/motion.md, 61 linhas lidas de 61, sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/privacy.md, 117 linhas lidas de 117, sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/right-to-left.md, 113 linhas lidas de 113, sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sf-symbols.md, 131 linhas lidas de 131, sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/spatial-layout.md, 61 linhas lidas de 61, sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/typography.md, 933 linhas lidas de 933, em três blocos (1-350, 351-700, 701-933), sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/writing.md, 53 linhas lidas de 53, sim

Nota sobre as tabelas de tracking de typography.md: as tabelas de tracking por tamanho de ponto (SF Pro, SF Pro Rounded, New York, macOS, tvOS, SF Compact, SF Compact Rounded) foram lidas por completo, linha a linha, mas na seção de especificações exatas acima foram resumidas em vez de transcritas número por número, por serem tabelas de referência técnica muito extensas (mais de 300 linhas de dados numéricos); todos os valores permanecem disponíveis no arquivo fonte já lido, sem nenhuma omissão de leitura.
