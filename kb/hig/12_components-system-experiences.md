# Components / System experiences

## App Shortcuts (slug: app-shortcuts)

### O que governa
Rege como um app expõe suas funções ou conteúdos principais para serem acionados de fora dele, via Siri, Spotlight, Shortcuts, Action Button ou aperto do Apple Pencil, usando App Intents.

### Por que
A Apple parte do princípio de que a interação mais valiosa é a que dispensa abrir o app. Um App Shortcut fica disponível desde a instalação, antes mesmo do primeiro uso, porque representa uma ação que o app já sabe fazer, não uma personalização aprendida. Ao mesmo tempo, depois que a pessoa usa o app, os shortcuts podem refletir escolhas dela (como contatos recentes no FaceTime), o que mostra a intenção de aproximar automação do contexto real de uso. A limitação a frases de ativação curtas e a poucos parâmetros opcionais vem da lógica de interação por voz: algo que soa complicado ao ser dito em voz alta tende a ser difícil de lembrar ou pronunciar corretamente.

### Faça e evite
- Prefira adotar app schemas para tipos comuns de funcionalidade, deixando App Shortcuts para recursos ou conteúdos exclusivos não cobertos por schemas.
- Ofereça App Shortcuts para as tarefas mais comuns e importantes do app, priorizando as que a pessoa completa sem sair do contexto atual.
- Permita um único parâmetro opcional por shortcut quando fizer sentido, com valores previsíveis e familiares, já que a pessoa não terá a lista de opções à vista.
- Peça esclarecimento quando faltar uma informação opcional, sugerindo um padrão (por exemplo, o tipo mais usado recentemente) e apresentando alternativas curtas.
- Mantenha as interações de voz simples; se a frase soa complicada ao ser dita, provavelmente é difícil de lembrar ou pronunciar.
- Evite embutir informação demais em um único parâmetro (o exemplo dado, "Start sleep meditation with nature sounds", é citado como parâmetro duplo problemático); peça informação adicional em uma etapa seguinte se for realmente necessária.
- Torne os App Shortcuts descobríveis dentro do próprio app, com dicas ocasionais quando a pessoa realiza ações comuns.
- Responda ao engajamento com o shortcut usando diálogo falado pela Siri e visuais como snippets e Live Activities.
- Use snippets para exibir informação estática ou opções de diálogo; use Live Activities para acesso contínuo a informação que muda ao longo de um período, como timers e contagens regressivas.
- Forneça detalhe suficiente para interação em dispositivos somente de áudio (AirPods, HomePod), incluindo toda informação crítica no texto de diálogo completo.
- Forneça frases de ativação breves e memoráveis, e variantes naturais; o nome do app é obrigatório na frase, mas o restante pode ser criativo.
- Use title case ao se referir a App Shortcuts ou ao app Shortcuts (e mantenha "Shortcuts" no plural); use minúsculas ao se referir a shortcuts individuais (não App Shortcuts nem o app Shortcuts).

### Especificações exatas
- Cada app pode incluir até 10 App Shortcuts.

### Diferenças por plataforma
- iOS, iPadOS: App Shortcuts podem aparecer na área Top Hit do Spotlight ao buscar o app, ou na área Shortcuts abaixo. Cada shortcut usa um símbolo do SF Symbols ou uma imagem de prévia do item ao qual liga diretamente. A ordem inicial em Spotlight e no app Shortcuts segue a ordem definida pelo desenvolvedor (mais importantes primeiro); depois que a pessoa passa a usar os shortcuts, o sistema reordena priorizando os mais usados.
- macOS: App Shortcuts não são suportados; porém ações criadas com App Intents são suportadas, e a pessoa pode montar shortcuts personalizados com elas no app Shortcuts do Mac.
- visionOS, watchOS: sem considerações adicionais.
- tvOS: não suportado.

### Ligações com outros artigos
Siri, Snippets, Live Activities.

---

<!-- visual:app-shortcuts -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página não tem vídeo.
- O resultado de busca com App Shortcuts é montado como uma única barra horizontal arredondada, branca e translúcida, sobre um cartão em gradiente laranja para rosa, com quatro itens lado a lado, cada um com seu rótulo (img 0091).
- A forma separa os tipos de item: o app Notes aparece primeiro, com ícone quadrado e rótulo "Notes", e os três shortcuts seguintes usam ícones circulares vermelhos com símbolo de lápis (img 0091).
- A mesma fileira combina um shortcut de ação, "New Note", com shortcuts de conteúdo que abrem notas existentes pelo nome, "Meeting Agenda" e "Dog Names" (img 0091).
- Cada shortcut de conteúdo leva atrás do símbolo uma miniatura da própria nota, com linhas de pauta ou a lista de nomes visíveis, o que torna o item reconhecível pelo conteúdo (img 0091).
- O card de um shortcut isolado sobre fundo branco tem ícone pequeno de xícara à esquerda e a frase "Order a Vanilla Latte" em preto, com o trecho variável destacado em azul e sublinhado (img 0092).
- Uma linha de chamada vinda de baixo nomeia esse trecho como "Parameter", anotando dentro do próprio card a diferença entre texto fixo da frase e valor variável (img 0092).
<!-- /visual:app-shortcuts -->

## Complications (slug: complications)

### O que governa
Rege o desenho de complications, os elementos que exibem informação relevante e atualizada no mostrador do Apple Watch.

### Por que
A premissa é que as pessoas preferem apps com complications poderosas porque isso dá acesso rápido a dados que importam sem precisar abrir o app. O texto é explícito: o comportamento que as pessoas mais apreciam numa complication não é o atalho para abrir o app, é a exibição de informação relevante que sempre parece atual. Por isso uma complication estática, sem dado significativo, tende a perder espaço de destaque no mostrador escolhido pela pessoa. A limitação de atualizações diárias por app reflete uma arbitragem de recursos do sistema: como o número de atualizações e de entradas de timeline é limitado, o app precisa escolher os horários que mais valorizam o dado exibido.

### Faça e evite
- Identifique conteúdo essencial e dinâmico que a pessoa queira ver rapidamente; evite complications estáticas sem dado significativo.
- Suporte o máximo possível de famílias de complication para estar disponível em mais mostradores; se não houver dado útil para uma família, forneça ao menos uma imagem que represente o app (como o ícone) para permitir abrir o app a partir do mostrador.
- Considere criar múltiplas complications por família para aproveitar mostradores compartilháveis centrados no app.
- Defina um deep link diferente para cada complication suportada, levando ao trecho mais relevante do app; complications que abrem sempre a mesma área parecem menos úteis.
- Tenha cuidado com privacidade: com o display Always-On, a informação pode ficar visível a outras pessoas além de quem usa o relógio.
- Escolha cuidadosamente quando atualizar os dados, considerando que o número de atualizações diárias e de entradas de timeline armazenadas é limitado.
- Escolha o estilo de anel ou gauge conforme o dado: fechado (closed) para percentual de um total, como um indicador de bateria; aberto (open) quando os valores mínimo e máximo são arbitrários ou não representam percentual, como um indicador de velocidade; segmentado (segmented), semelhante ao aberto, para valores dentro de um intervalo definido pelo app, útil para mudanças rápidas de valor.
- Garanta que as imagens fiquem boas em modo tinted (tintado): evite usar cor como único meio de comunicar informação importante, e forneça, quando necessário, uma versão alternativa tintada de uma imagem colorida que não fique boa dessaturada.
- Use, em geral, larguras de linha de dois pontos ou mais nos conteúdos da complication, porque linhas mais finas são difíceis de ver rapidamente, especialmente com a pessoa em movimento.
- Forneça um conjunto de imagens de placeholder estáticas para cada complication suportada, usadas enquanto o sistema verifica se pode gerar um placeholder localizado.
- Prefira usar o WidgetKit para desenvolver complications a partir do watchOS 9; para versões anteriores, use o protocolo CLKComplicationDataSource do ClockKit.

### Especificações exatas
A partir do watchOS 9, o sistema organiza complications em famílias (circular, corner, inline, rectangular) com layouts recomendados; complications de versões anteriores usam templates legados (nongraphic) que não assumem a cor selecionada pela pessoa.

Circular, imagem regular (por tamanho de caixa 40mm / 41mm / 44mm / 45mm-49mm):
- Image: 42x42 pt / 44.5x44.5 pt / 47x47 pt / 50x50 pt (84x84, 89x89, 94x94, 100x100 px @2x)
- Closed gauge: 27x27 pt / 28.5x28.5 pt / 31x31 pt / 32x32 pt
- Open gauge: 11x11 pt / 11.5x11.5 pt / 12x12 pt / 13x13 pt
- Stack (não texto): 28x14 pt / 29.5x15 pt / 31x16 pt / 33.5x16.5 pt
- Texto padrão (SwiftUI): estilo Rounded, peso Medium, tamanho 12 pt (40mm), 12.5 pt (41mm), 13 pt (44mm), 14.5 pt (45mm/49mm)

Circular extra-large (para o mostrador X-Large):
- Image: 120x120 pt / 127x127 pt / 132x132 pt / 143x143 pt
- Open gauge: 31x31 pt / 33x33 pt / 33x33 pt / 37x37 pt
- Closed gauge: 77x77 pt / 81.5x81.5 pt / 87x87 pt / 91.5x91.5 pt
- Stack: 80x40 pt / 85x42 pt / 87x44 pt / 95x48 pt
- Texto padrão: Rounded, Medium, tamanho 34.5 pt (40mm), 36.5 pt (41mm), 36.5 pt (44mm), 41 pt (45mm/49mm)

Placeholders da família circular (38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm):
- Circular:, / 42x42 pt / 44.5x44.5 pt / 47x47 pt / 50x50 pt
- Bezel:, / 42x42 pt / 44.5x44.5 pt / 47x47 pt / 50x50 pt
- Extra Large:, / 120x120 pt / 127x127 pt / 132x132 pt / 143x143 pt

Corner (40mm / 41mm / 44mm / 45mm-49mm):
- Circular: 32x32 pt / 34x34 pt / 36x36 pt / 38x38 pt
- Gauge: 20x20 pt / 21x21 pt / 22x22 pt / 24x24 pt
- Texto: 20x20 pt / 21x21 pt / 22x22 pt / 24x24 pt
- Placeholder (38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm):, / 20x20 pt / 21x21 pt / 22x22 pt / 24x24 pt
- Texto padrão: Rounded, Semibold, tamanho 10 pt (40mm), 10.5 pt (41mm), 11 pt (44mm), 12 pt (45mm/49mm)

Inline, utilitarian small (38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm):
- Flat: 9-21x9 pt / 10-22x10 pt / 10.5-23.5x21 pt / N/A / 12-26x12 pt
- Ring: 14x14 pt / 14x14 pt / 15x15 pt / 16x16 pt / 16.5x16.5 pt
- Square: 20x20 pt / 22x22 pt / 23.5x23.5 pt / 25x25 pt / 26x26 pt

Inline, utilitarian large (Flat, 38mm / 40mm-42mm / 41mm / 44mm / 45mm-49mm): 9-21x9 pt / 10-22x10 pt / 10.5-23.5x10.5 pt / N/A / 12-26x12 pt.

Rectangular (40mm / 41mm / 44mm / 45mm-49mm):
- Large image with title: 150x47 pt / 159x50 pt / 171x54 pt / 178.5x56 pt (com corner radius automático de 4 pt)
- Large image without title: 162x69 pt / 171.5x73 pt / 184x78 pt / 193x82 pt
- Standard body: 12x12 pt / 12.5x12.5 pt / 13.5x13.5 pt / 14.5x14.5 pt
- Text gauge: 12x12 pt / 12.5x12.5 pt / 13.5x13.5 pt / 14.5x14.5 pt
- Texto padrão: Rounded, Medium, tamanho 16.5 pt (40mm), 17.5 pt (41mm), 18 pt (44mm), 19.5 pt (45mm/49mm)

Templates legados: circular small, modular small, modular large, extra large, cada um com tabelas próprias de tamanho de imagem por caixa (38mm, 40mm/42mm, 41mm, 44mm, 45mm/49mm), incluindo formatos Ring, Simple, Stack e Placeholder.

### Diferenças por plataforma
Não suportado em iOS, iPadOS, macOS, tvOS ou visionOS; exclusivo do watchOS.

### Ligações com outros artigos
Watch faces (o texto remete a ele para o conceito de mostrador compartilhável centrado em complications).

---

<!-- visual:complications -->
### O que as ilustrações mostram
Base: 14 de 14 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo e só traz versões claras das folhas.
- A abertura é um diagrama de vocabulário de posição: um mostrador estilizado com linhas finas ligando rótulos às zonas Top Left (Earth), Date, Middle (cartão retangular de agenda), Bottom Left (anéis de atividade), Bottom Middle (bússola com "315° NW") e Bottom Right (temperatura com faixa de mínima e máxima) (img 0344).
- Todo exemplo é um slot sobre fundo preto: quadrado na maioria das famílias (Circular, Corner, Circular small, Modular small, Extra large) e retângulo largo em Inline, Rectangular, Modular large e num caso de Circular com texto curvo (img 0345 a img 0397, img 0353).
- O anel fechado envolve um símbolo ou número: vermelho vivo em cerca de 90% ao redor de uma nota musical, com o restante em vermelho apagado (img 0345), verde quase fechado com leve sobreposição no ponto de início ao redor de "100" (img 0346) e azul em cerca de 85% ao redor de "85" (img 0355).
- Os arcos abertos usam gradiente e deixam a base para um ícone ou sigla: verde a violeta com um pequeno sol perto das 6 horas (img 0347), arco multicolor com "AQI" abaixo de "42" (img 0348) e, nos de temperatura, mínima e máxima como números menores coloridos abaixo do valor, verde para o extremo baixo e laranja ou vermelho para o alto (img 0349, img 0358).
- Na família Circular também há slots sem medidor: pilha de texto com "AAPL" em branco e a cotação em verde (img 0352), ícone vermelho de pôr do sol sobre o horário em branco (img 0351) e só o ícone do app Respirar, sem texto (img 0350).
- Texto curvo acompanhando a borda aparece só em Corner e num caso Circular, sempre em letras maiúsculas ou compactas: a agenda curvada no topo com "FRI" em vermelho e "23" grande em branco (img 0353), "CUP" em branco com o fuso em laranja (img 0365) e o cronômetro em laranja com ícone pequeno (img 0366).
- Os medidores de Corner seguem a curva do canto: uma barra curva grossa laranja acima de "14:59" com ícone de cronômetro (img 0363) e um arco curto verde a laranja ao lado de "72°", com os extremos nas pontas e um ponto laranja marcando a posição atual (img 0364); há ainda ícone de sol atrás de nuvem sobre fundo azul escuro arredondado (img 0362).
- Inline ocupa um retângulo preto largo em faixa horizontal: texto cinza claro em uma linha, como "LON 6:09" e "11:00AM PHOTO SHOOT" (img 0367, img 0371), dois medidores brancos lado a lado (img 0368, img 0369) ou a imagem realista da lua à esquerda com o resto vazio (img 0370).
- Rectangular organiza três linhas alinhadas à esquerda com hierarquia de cor, título em azul, valor em branco e linha secundária em cinza (img 0372); a variação troca a terceira linha por ícone no título e barra de progresso azul em cerca de 70% na base (img 0373), e a de frequência cardíaca põe "2 MINS AGO" em vermelho acima de um gráfico de linha com eixo vertical 102 e 52 e eixo horizontal de 12AM a 6PM (img 0374).
- Em Modular large, a primeira linha colorida funciona como título e o restante vem em branco, como "Cupertino, CA" em vermelho (img 0389), "Final Score" em azul claro (img 0390) e "Wednesday" em vermelho sobre "Mar 9" bem maior (img 0391); em colunas, rótulos amarelos CAL, MIN e HOUR ficam à esquerda dos valores em branco (img 0388), padrão que Modular small repete com CP e MH em roxo (img 0381).
- O mesmo dado é recomposto conforme a família: "LON 6:09" fica numa linha só em Inline (img 0367), empilhado em salmão sobre círculo marrom avermelhado em Circular small (img 0380) e empilhado em laranja e branco em Modular small e Extra large (img 0387, img 0397); o pôr do sol com horário se repete em cinco famílias (img 0351, img 0360, img 0379, img 0386, img 0396) e "68°" cresce até ocupar quase toda a largura em Extra large (img 0385 comparada com img 0395).
- Em Circular small predominam cores menos saturadas e círculos de fundo escurecidos: anel bege ao redor de uma gota (img 0375), cronômetro em salmão sem anel (img 0377), "68°" em amarelo pálido sobre círculo escurecido (img 0378) e pôr do sol em branco sobre círculo cinza escuro (img 0379).
Divergências registradas: na abertura o tom é mais um degradê laranja e rosa do que o vermelho uniforme descrito (img 0344); na img 0367 "LON" e "6:09" aparecem lado a lado numa linha, e não empilhados como diz a descrição oficial; na img 0390 não há linhas de grade separando colunas, ao contrário da tabela com grade descrita; o ícone do Respirar é verde azulado na img 0350 e predominantemente azul na img 0359; o texto curvo da img 0353 só foi lido de forma aproximada.
<!-- /visual:complications -->

## Controls (slug: controls)

### O que governa
Rege o desenho de controls, botões ou alternadores (toggles) que dão acesso rápido a uma funcionalidade do app a partir da Control Center, da Lock Screen ou do Action Button.

### Por que
A lógica central é que um control existe para representar, de forma compacta e sem abrir o app, o estado e a ação de uma funcionalidade específica. Como o control aparece em contextos com pouco ou nenhum texto (por exemplo, apenas o símbolo na Lock Screen), o símbolo sozinho precisa carregar o significado da ação, daí a exigência de escolher um símbolo descritivo e de fornecer versões para os dois estados de um toggle. A exigência de redigir informação sensível quando o dispositivo está bloqueado, e de autenticação para ações que afetam segurança, reflete a mesma preocupação presente em Live Activities e widgets: esses elementos ficam visíveis a terceiros e não devem vazar dados privados nem permitir ações críticas sem confirmação de identidade.

### Faça e evite
- Ofereça controls para ações que trazem o maior benefício sem precisar abrir o app; por exemplo, iniciar uma Live Activity direto de um control.
- Atualize os controls quando a pessoa interage com eles, quando uma ação é concluída, ou remotamente via push notification, refletindo com precisão o estado e se a ação ainda está em progresso.
- Escolha um símbolo descritivo que sugira o comportamento do control; para toggles, forneça símbolo para os dois estados (o exemplo dado é `door.garage.open` e `door.garage.closed`).
- Use animações de símbolo para destacar mudanças de estado: anime a transição entre estados em toggles; para botões com ação de duração, anime indefinidamente enquanto a ação ocorre e pare ao concluir.
- Selecione uma cor de tint alinhada à marca do app; o sistema a aplica ao símbolo do toggle no estado ativo, e também no valor e símbolo exibidos na Dynamic Island quando a ação é disparada pelo Action Button.
- Ajude a pessoa a fornecer informação adicional necessária para a ação (por exemplo, escolher qual luz específica controlar), solicitando configuração já na primeira adição do control; a reconfiguração pode ocorrer a qualquer momento.
- Forneça texto de dica (hint text) para o Action Button, usando verbos, para explicar o que acontece ao pressionar e segurar.
- Inclua um placeholder se o título ou valor do control puder variar, exibido na galeria de controls da Control Center, da Lock Screen, ou antes de atribuí-lo ao Action Button.
- Oculte informação sensível quando o dispositivo está bloqueado, podendo especificar se o próprio estado do símbolo também deve ser redigido (nesse caso, o sistema mostra o símbolo em seu estado desligado).
- Exija autenticação para ações que afetam segurança, como travar/destravar uma porta ou dar partida em um carro.
- Se o app suportar captura de câmera, é possível criar um control que leva direto à experiência de câmera do app mesmo com o dispositivo bloqueado; qualquer tarefa além da captura exige desbloqueio.
- Use a mesma UI de câmera no app e na experiência de câmera do control, para que a transição pareça contínua.
- Forneça instruções para ajudar a pessoa a entender como adicionar o control que abre essa experiência de câmera.

### Especificações exatas
Nenhum valor numérico (medida, duração, tamanho) é fornecido neste artigo.

### Diferenças por plataforma
- iOS, iPadOS, macOS: sem considerações adicionais.
- watchOS, tvOS, visionOS: não suportado.

### Ligações com outros artigos
Live Activities, Widgets, Action button, Branding, SF Symbols.

---

<!-- visual:controls -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo e só traz versões claras das folhas.
- A abertura é um recorte estilizado da Central de Controle em rosa monocromático e sem texto, com botões circulares translúcidos (avião, AirPlay, Wi-Fi, sinal, Bluetooth, elo, globo) agrupados e um botão maior de Wi-Fi ocupando mais espaço no canto inferior esquerdo (img 0399).
- A anatomia é ensinada com linhas de chamada sobre um control de cantos arredondados em fundo de textura clara: símbolo de lua à esquerda, marcado como "Symbol image", e à direita duas linhas empilhadas, o título em cima e o detalhe embaixo, este marcado como "Value" (img 0400).
- Na Central de Controle real do iPhone, sobre fundo escuro desfocado, a grade mostra Wi-Fi ativo em azul, Bluetooth em azul e sinal celular em verde, e o control de silêncio aparece ativo como círculo branco com sino cortado, com brilho e volume abaixo, além de um cartão de mídia e de Focus no rodapé (img 0401).
- O mesmo control de silêncio aparece em três superfícies: na grade da Central (img 0401), como botão circular translúcido no rodapé da Lock Screen ao lado da lanterna (img 0402) e na Dynamic Island expandida, com sino cortado e a palavra "Silent" em vermelho sobre a grade de apps (img 0403).
- A cor de tint é ensinada por um par com o mesmo control circular grande: lâmpada branca sem cor no estado desligado (img 0404) e lâmpada preenchida em amarelo vivo no estado ligado (img 0405).
- O control configurável é um retângulo longo com lua em círculo cinza à esquerda e a palavra "Option" acompanhada de setas para cima e para baixo, indicando que um valor pode ser escolhido (img 0406).
- O texto de dica do Action Button é mostrado em par: com a pílula em "Ring" e sino branco, a dica sobre os ícones diz "Hold for Silent" (img 0407); com a pílula em "Silent" e sino cortado em vermelho, diz "Hold for Ring" (img 0408), ou seja, a dica começa com verbo e nomeia o resultado de segurar, não o estado atual.
- A ocultação de dados sensíveis é um antes e depois do mesmo control em pílula: aberto, em fundo branco com lâmpada amarela, título em preto e detalhe em cinza (img 0409); bloqueado, em fundo escuro com lâmpada branca e o texto trocado por duas barras cinza claras, uma curta e uma longa, sem mudar forma nem tamanho (img 0410).
Divergências registradas: as notas indicam que a descrição oficial nem sempre esclarece quando a imagem é captura de tela real, como nas img 0401, img 0402, img 0403, img 0407 e img 0408, e quando é ilustração.
<!-- /visual:controls -->

## Live Activities (slug: live-activities)

### O que governa
Rege como um app comunica o progresso de uma atividade, evento ou tarefa em locais visíveis do sistema (Dynamic Island, Lock Screen, StandBy, menu bar do Mac, Smart Stack do Apple Watch, CarPlay Dashboard) sem exigir que a pessoa abra o app.

### Por que
A ideia central é que uma Live Activity vai além de uma notificação pontual: ela entrega atualizações frequentes de status por um período e permite interação com a informação exibida, servindo como "casa unificada" para alertas e indicadores de atividade em curso. A limitação a atividades de curta a média duração (até oito horas) e o foco em informação essencial decorrem do princípio de que a Live Activity precisa continuar relevante e glanceable, não uma réplica da tela do app. As regras de margem concêntrica e de alinhamento ao redor da câmera TrueDepth (Dynamic Island) existem porque o formato físico do recorte da tela impõe uma geometria que, se ignorada, produz tensão visual, elementos "furando" o contorno arredondado ou parecendo deslocados.

### Faça e evite
- Ofereça Live Activities para tarefas e eventos com início e fim definidos, priorizando durações curtas a médias que não excedam oito horas.
- Foque na informação mais importante para visualização rápida; a Live Activity não precisa mostrar tudo, e a pessoa pode tocar para abrir o app e ver mais detalhes.
- Não use Live Activity para anúncios ou promoções.
- Evite exibir informação sensível, já que a Live Activity fica visível em locais públicos como a Lock Screen ou o display Always-On; prefira mostrar um resumo inócuo e deixar que o toque leve ao app para ver o conteúdo sensível, ou redija (redact) as views sensíveis e permita que a pessoa configure se quer exibi-las.
- Crie uma Live Activity que combine com a estética e a personalidade visual do app, tanto no modo claro quanto no escuro, para reforçar reconhecimento.
- Se incluir uma marca (logo mark), exiba-a sem container e não use o ícone completo do app.
- Não adicione elementos ao app que chamem atenção para a Dynamic Island.
- Garanta que o texto seja fácil de ler: use texto grande, com peso mais forte (medium ou superior), e use texto pequeno com moderação.
- Adapte a diferentes tamanhos de tela e apresentações, usando os valores da seção de especificações como referência.
- Ajuste tamanho e posição dos elementos para uso eficiente do espaço, exibindo só o necessário para o conteúdo.
- Use layouts familiares e templates com margens padrão do sistema e tamanhos de texto recomendados, disponíveis nos Apple Design Resources.
- Use margens consistentes e posicionamento concêntrico: alinhe o raio de canto do conteúdo ao raio de canto externo da Live Activity subtraindo a margem, via container do SwiftUI (ContainerRelativeShape).
- Ao separar um bloco de conteúdo, use um container com shape recuado (inset) ou uma linha grossa; não desenhe o conteúdo até a borda da Dynamic Island.
- Altere dinamicamente a altura da Live Activity na Lock Screen ou na apresentação expandida conforme a quantidade de informação disponível.
- Não personalize a cor de fundo das apresentações compact, minimal e expanded (fundo preto opaco fixo); é possível personalizar a cor de fundo da apresentação Lock Screen, garantindo contraste suficiente, especialmente em Always-On com luminância reduzida.
- Use cor para expressar a identidade do app; cores fortes ajudam a Live Activity a se destacar entre outras.
- Tinja a cor da key line (linha de contorno visível em fundo escuro/Dark Mode) para combinar com o conteúdo.
- Use transições e animações do sistema ou customizadas com duração máxima de dois segundos; o sistema não anima em displays Always-On com luminância reduzida.
- Anime mudanças de layout preservando o máximo possível do layout existente, movendo elementos para as novas posições em vez de removê-los e reanimá-los.
- Evite sobrepor elementos; prefira animar elementos para fora e reanimá-los em nova posição, usando fade-in/fade-out para itens de lista que não se movem.
- Garanta que tocar a Live Activity abra o app na localização certa, diretamente relacionada ao conteúdo.
- Foque em ações simples e diretas; limite a interatividade, de preferência a um único elemento, reservada a funcionalidade essencial que a pessoa ativa uma vez ou pausa/retoma temporariamente (playback de música, treinos, gravação de áudio).
- Considere permitir que a pessoa responda a atualizações de evento ou progresso com um botão ou toggle.
- Inicie a Live Activity em momentos apropriados e facilite desativá-la no app; ofereça controles no próprio app (por exemplo, um botão para deixar de seguir um jogo).
- Ofereça um App Shortcut que inicie a Live Activity, por exemplo via Action Button.
- Atualize a Live Activity só quando houver conteúdo novo; mantenha a mesma exibição se o status não mudar.
- Alerte apenas para atualizações essenciais que exijam atenção; alertas acendem a tela e tocam som por padrão. Evite alertar com frequência excessiva ou com atualizações não cruciais, e não use push notifications junto de Live Activities para as mesmas atualizações.
- Deixe a pessoa acompanhar múltiplos eventos com uma única Live Activity que usa layout dinâmico e alterna entre eventos, em vez de criar Live Activities separadas.
- Encerre a Live Activity imediatamente quando a tarefa ou evento terminar; considere definir um tempo de dismissal personalizado, proporcional à duração da atividade (na maioria dos casos, 15 a 30 minutos é adequado).
- Comece o design pelo iPhone e depois refine para outros contextos (StandBy, CarPlay, Apple Watch).

### Compact presentation
- Foque na informação mais importante, dinâmica e atualizada.
- Garanta unidade visual entre os elementos leading e trailing (separados pela câmera TrueDepth), usando cor e tipografia consistentes.
- Mantenha o conteúdo o mais estreito possível e justo (snug) contra a câmera TrueDepth, sem obscurecer informação chave na status bar e sem padding extra; mantenha layout equilibrado entre os dois lados.
- Ao tocar, leve ao app diretamente aos detalhes relacionados; garanta que os elementos leading e trailing levem à mesma tela.

### Minimal presentation
- Garanta que a Live Activity seja reconhecível: exiba informação atualizada em vez de apenas um logo estático, se possível (o exemplo dado é o Timer mostrando o tempo restante em vez de um ícone fixo).

### Expanded presentation
- Mantenha o posicionamento relativo dos elementos para criar um layout coerente entre apresentações, com expansão previsível.
- Envolva o conteúdo de forma justa (tightly) ao redor da câmera TrueDepth, evitando espaço vazio.

### Lock Screen presentation
- Não replique o layout de notificações; crie um layout específico ao conteúdo da Live Activity.
- Escolha cores que funcionem bem em uma Lock Screen personalizada, usando cor de fundo e tint personalizados e opacidade com moderação.
- Garanta contraste suficiente no Dark Mode e no display Always-On; por padrão a Live Activity usa fundo claro no modo claro e escuro no modo escuro.
- Verifique a cor gerada automaticamente para o botão de dismiss, que combina com as cores de fundo e primeiro plano da Live Activity, ajustando via `activitySystemActionForegroundColor(_:)` se necessário.
- Use margens padrão para alinhar o design às notificações.

### StandBy presentation
- Atualize o layout para o StandBy, considerando um layout customizado que aproveite o espaço extra.
- Considere usar a cor de fundo padrão no StandBy, que mescla a Live Activity com a moldura do dispositivo e permite escala ligeiramente maior por não precisar acomodar as margens ao redor da câmera TrueDepth.
- Use margens padrão e evite estender elementos gráficos até a borda da tela.
- Verifique o design em Night Mode, no qual o sistema aplica tint vermelho.

### CarPlay
- No CarPlay, o sistema combina automaticamente os elementos leading e trailing da apresentação compact em um único layout no CarPlay Dashboard.
- O mesmo design de Live Activity se aplica a CarPlay e Apple Watch; embora Live Activities no Apple Watch possam ser interativas, o sistema desativa elementos interativos no CarPlay.
- Considere criar um layout customizado se a Live Activity se beneficiar de texto maior ou informação adicional, declarando suporte à família suplementar `ActivityFamily.small`.
- Tenha cautela ao incluir botões ou toggles no layout customizado, já que o CarPlay os desativa; prefira exibir conteúdo temporal em vez de controles se a pessoa provavelmente observar a Live Activity dirigindo.

### Especificações exatas

Duração máxima de animação: 2 segundos (não há animação em Always-On com luminância reduzida).

Margem padrão de layout na Lock Screen: 14 pontos.

Tempo de dismissal após o fim da atividade: recomendado 15 a 30 minutos (a Live Activity é removida imediatamente da Dynamic Island e do CarPlay ao terminar; na Lock Screen, no menu bar do Mac e no Smart Stack do watchOS permanece por até quatro horas, salvo tempo customizado).

Dimensões CarPlay: Live Activity em 240x78 pt, 240x100 pt, 170x78 pt. Configurações de Smart Display Zoom: Widescreen 1920x720 pt, Portrait 900x1200 pt, Standard 800x480 pt.

Dimensões iOS (todas em pontos):
- Tela 430x932: compact leading e trailing 62.33x36.67; minimal (largura em intervalo) 36.67 a 45x36.67; expanded (altura em intervalo) 408x84 a 160; Lock Screen (altura em intervalo) 408x84 a 160.
- Tela 393x852: compact leading e trailing 52.33x36.67; minimal 36.67 a 45x36.67; expanded 371x84 a 160; Lock Screen 371x84 a 160.

Raio de canto da Dynamic Island: 44 pontos, com o formato arredondado igual à câmera TrueDepth.

Largura da Dynamic Island por dispositivo (compact/minimal e expanded, em pontos): iPhone 17 Pro Max 250/408; iPhone 17 Pro 230/371; iPhone Air 250/408; iPhone 17 230/371; iPhone 16 Pro Max 250/408; iPhone 16 Pro 230/371; iPhone 16 Plus 250/408; iPhone 16 230/371; iPhone 15 Pro Max 250/408; iPhone 15 Pro 230/371; iPhone 15 Plus 250/408; iPhone 15 230/371; iPhone 14 Pro Max 250/408; iPhone 14 Pro 230/371.

Dimensões iPadOS (Lock Screen, altura em intervalo, em pontos): tela 1366x1024 → 500x84 a 160; 1194x834 → 425x84 a 160; 1012x834 → 425x84 a 160; 1080x810 → 425x84 a 160; 1024x768 → 425x84 a 160.

Dimensões macOS: usam os mesmos valores de iOS.

Dimensões watchOS (Smart Stack, em pontos, por tamanho de caixa): 40mm → 152x69.5; 41mm → 165x72.5; 44mm → 173x76.5; 45mm → 184x80.5; 49mm → 191x81.5.

### Diferenças por plataforma
- iOS, iPadOS: sem considerações adicionais além das já descritas nas apresentações.
- macOS: Live Activities ativas aparecem automaticamente no menu bar de um Mac pareado, usando as apresentações compact, minimal e expanded; clicar nela abre o iPhone Mirroring para exibir o app.
- watchOS: ao iniciar no iPhone, a Live Activity aparece no topo do Smart Stack do Apple Watch pareado; por padrão combina os elementos leading e trailing da apresentação compact. Sem app watchOS, tocar abre uma view em tela cheia com botão para abrir o app no iPhone pareado; com app watchOS, tocar abre o app watchOS. É possível criar layout customizado watchOS com mais informação e funcionalidade interativa, mas as mesmas cautelas do CarPlay quanto a botões/toggles se aplicam, pois o layout customizado watchOS também é usado no CarPlay.
- tvOS, visionOS: não suportado.

### Ligações com outros artigos
App Shortcuts, Widgets, Dark Mode, Always On, CarPlay, StandBy.

---

<!-- visual:live-activities -->
### O que as ilustrações mostram
Base: 7 de 7 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura empilha duas Dynamic Islands: em cima, uma pílula vermelha tracejada e vazia sobre o placar resumido, e embaixo o placar completo com times, ícones, arremessadores e a situação do jogo, sugerindo a passagem da forma simples para o conteúdo completo (img 0700).
- As apresentações são nomeadas com linhas de chamada sobre a moldura do iPhone e sem conteúdo real: compact são duas formas pretas nos dois lados de uma pílula vermelha, "Leading side" e "Trailing side" (img 0701); minimal é uma pílula presa à ilha, "Minimal (attached)", e um círculo preto separado, "Minimal (detached)" (img 0702); expanded é uma forma preta única quase da largura do aparelho, com a pílula vermelha centralizada no topo (img 0703).
- Na Lock Screen, a Live Activity é um banner preto arredondado no terço inferior, com ícones azuis à esquerda e duas linhas de texto à direita, e o dado dinâmico "8 minutes" em azul (img 0704); o mesmo cartão também aparece sobreposto no topo da Home Screen, cobrindo parte da grade de ícones (img 0705).
- A legibilidade é mostrada em par: "GATE" e "C15" pequenos em duas linhas ao lado da pílula (img 0707) contra só "C15", maior e mais pesado (img 0709), com marcadores isolados de X cinza e check verde (img 0708, img 0710); a versão aprovada troca conteúdo por tamanho e peso.
- Uma borda vermelha fina contorna toda a cápsula expandida como guia de margem, e o botão "Contact Juan C." com balão de fala fica numa barra escura arredondada separada, abaixo do conteúdo da entrega (img 0711).
- A margem concêntrica é ajustada com a cápsula contornada em vermelho: um círculo azul claro encostado na borda, sem respiro (img 0712), o ícone de sacola e copo com pequena folga (img 0713) e o mesmo ícone numa posição quase idêntica, que a legenda oficial marca como perto da borda sem invadir a curva (img 0714).
- Para separar um bloco, a barra "Text" colada no fundo e nas duas laterais, sem cantos próprios, é o erro (img 0715); as alternativas são um retângulo de cantos arredondados, recuado e com margem visível dos lados e embaixo (img 0716), ou uma linha horizontal azul clara com "Text" abaixo, sem caixa (img 0717).
- O alinhamento ao perímetro arredondado é conferido com o conteúdo borrado de propósito dentro de uma caixa tracejada em vermelho: longe demais da borda direita (img 0718) e deslocado para perto do canto arredondado sem ultrapassá-lo (img 0719).
- No compact, o erro é o espaço vazio entre a pílula que representa a câmera e o bloco com "8min", que deixa a forma larga e desequilibrada (img 0720); a correção aproxima os dois e reduz a largura total (img 0721).
- No expanded, uma linha tracejada vermelha marca a faixa vazia entre a câmera e o início do conteúdo (img 0722); na versão corrigida, o bloco começa mais perto do nível da câmera, sem essa faixa (img 0723).
- O cartão de voo do StandBy é azul sólido e largo, com o conteúdo dentro de um retângulo tracejado: companhia, rota SFO para NRT com avião e trajetória pontilhada, tempo para pouso, partida e terminal (img 0706); no Night Mode o mesmo layout aparece inteiro em tons de vermelho sobre preto, sem azul (img 0724).
- A adaptação para o watchOS vem em cadeia: o compact do iPhone com ícone à esquerda e "8min" à direita (img 0725); o Smart Stack padrão, cartão branco com "From Delivery App" em cinza no topo e ícone e "8 min" empurrados para cantos opostos da base (img 0726); e o layout customizado, com título em negrito, "Arriving in" e "8 min" empilhados à esquerda e um anel de progresso azul claro com o ícone no centro à direita (img 0727).
Divergências registradas: na img 0706 o tracejado demarca a área de conteúdo dentro do cartão azul, e não a borda externa que a descrição oficial associa à escala 2x; a diferença de padding entre as img 0713 e img 0714 é sutil demais para medir a olho e foi lida pela legenda oficial; na img 0717 a linha parece fina, embora o texto fale em linha grossa; a folha da img 0708 mostra só o marcador de erro, sem a imagem de contexto.
<!-- /visual:live-activities -->

## Notifications (slug: notifications)

### O que governa
Rege conteúdo, ações e badges de notificações, o mecanismo pelo qual um app entrega informação pontual e de alto valor que a pessoa entende rapidamente.

### Por que
O princípio central é que a pessoa ativa notificações para receber atualizações rápidas de forma sucinta, e que ela responde às notificações quando lhe convém, não imediatamente. Isso explica a regra contra notificações repetidas para o mesmo assunto (lota a Notification Center e pode levar a pessoa a desligar todas as notificações do app) e contra instruções de tarefa que dependem de a pessoa se lembrar delas depois de dispensar a notificação. A recusa em usar badges para qualquer coisa que não seja contagem de notificações não lidas decorre do mesmo raciocínio de honestidade de interface presente em outros artigos do grupo: um componente do sistema deve significar sempre a mesma coisa, senão a pessoa perde a capacidade de confiar nele.

### Faça e evite
- Forneça notificações concisas e informativas.
- Evite enviar múltiplas notificações para o mesmo assunto, mesmo que a pessoa não tenha respondido.
- Evite notificações que instruam a pessoa a realizar tarefas específicas dentro do app; se fizer sentido, ofereça ações simples direto na notificação em vez disso.
- Use um alerta, não uma notificação, para exibir mensagens de erro.
- Trate notificações com elegância quando o app está em primeiro plano: as notificações não aparecem, mas o app ainda recebe a informação; apresente-a de forma perceptível mas não invasiva, como incrementar um badge ou inserir o dado discretamente na view atual (o exemplo dado é o Mail simplesmente adicionando a mensagem à lista de não lidas).
- Evite incluir informação sensível, pessoal ou confidencial em uma notificação, já que não se pode prever o contexto em que a pessoa a receberá.
- Quando a notificação tiver título, o sistema o exibe no topo; em notificação de comunicação direta, o sistema mostra automaticamente o nome do remetente; em notificação não relacionada a comunicação, mostra o nome do app se nenhum título for fornecido.
- Crie um título curto quando ele der contexto ao conteúdo; use title-style capitalization e sem pontuação final.
- Escreva conteúdo sucinto e fácil de ler, usando frases completas, sentence case e pontuação correta, sem truncar manualmente (o sistema trunca quando necessário).
- Forneça texto genericamente descritivo para quando as prévias de notificação estiverem desativadas nas Configurações, dando contexto suficiente sem revelar detalhes demais (exemplos citados: "Friend request", "New comment", "Reminder", "Shipment"), com sentence-style capitalization.
- Evite incluir o nome ou ícone do app no texto, já que o sistema já exibe automaticamente uma versão grande do ícone (ou a imagem de contato badgeada com o ícone, em notificações de comunicação).
- Considere fornecer um som para complementar as notificações; se usar som customizado, garanta que seja curto, distintivo e bem produzido, mas não dependa dele para comunicar informação importante, pois a pessoa pode não ouvi-lo. Não é possível programar uma vibração para acompanhar o som.
- A notificação pode apresentar até quatro botões de ação para realizar tarefas sem abrir o app; ofereça ações que façam sentido no contexto, com rótulo curto em title case descrevendo o resultado, sem nome do app nem informação extra.
- Evite fornecer uma ação que só abra o app, pois isso polui a view de detalhe.
- Prefira ações não destrutivas; se uma ação destrutiva for necessária, garanta contexto suficiente para evitar consequências não intencionais (o sistema dá aparência distinta a ações identificadas como destrutivas).
- Forneça um ícone de interface simples e reconhecível para cada ação de notificação, exibido do lado trailing do título da ação.
- Use um badge apenas para mostrar quantas notificações não lidas existem; não use badge para informação numérica não relacionada a notificações (dados de clima, datas, preços de ações, placares).
- Garanta que badging não seja o único método de comunicar informação essencial, já que a pessoa pode desativá-lo.
- Mantenha os badges atualizados, atualizando assim que a pessoa abre as notificações correspondentes (reduzir a contagem a zero remove todas as notificações relacionadas da Notification Center).
- Evite criar uma imagem ou componente customizado que imite a aparência ou o comportamento de um badge.

### Especificações exatas
Até quatro botões de ação por notificação (limite comum a iOS/iPadOS e aos long looks do watchOS).

### Diferenças por plataforma
- iOS, iPadOS, macOS, tvOS, visionOS: sem considerações adicionais.
- watchOS: as notificações ocorrem em duas etapas, short look e long look; é possível também visualizá-las na Notification Center; em dispositivos suportados, a pessoa pode dar duplo toque para responder.
  - Short look: aparece quando o pulso é levantado e desaparece quando é abaixado. Evite usá-lo como único meio de comunicar informação importante, já que aparece brevemente; mantenha privacidade, evitando informação potencialmente sensível no título.
  - Long look: fornece mais detalhe; a pessoa pode rolar verticalmente ou usar a Digital Crown; pode ser dispensado tocando ou abaixando o pulso. Pode ser estático ou dinâmico; a interface estática exibe a mensagem e texto/imagens estáticos adicionais; a interface dinâmica dá acesso ao conteúdo completo e mais opções de configuração visual. O sistema usa a interface estática como padrão quando a dinâmica está indisponível (sem rede, ou app companheiro do iPhone inacessível). Forneça, no mínimo, a interface estática; de preferência forneça também a dinâmica. A estrutura geral (sash no topo com ícone e nome do app, botão Dismiss no rodapé abaixo de todos os botões customizados) não pode ser alterada, mas a área de sash e o fundo da área de conteúdo podem ser customizados (cor sólida ou aparência borrada/translúcida no sash). Por padrão, o fundo da área de conteúdo é transparente; para igualar o fundo de outras notificações do sistema, usar branco com 18% de opacidade, ou uma cor customizada da marca. É possível oferecer até quatro ações customizadas abaixo da área de conteúdo, além do botão Dismiss sempre presente no rodapé.
  - Double tap: ao responder por duplo toque, o sistema seleciona a primeira ação não destrutiva como resposta; portanto a ordem das ações customizadas importa, e convém colocar a ação mais usada no topo da lista.

### Especificações exatas (watchOS)
Opacidade de fundo padrão para igualar outras notificações do sistema: branco com 18% de opacidade.

### Ligações com outros artigos
Managing notifications, Alerts.

---

<!-- visual:notifications -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (3 imagens, todas em aparência clara), código conferido; sem vídeos.
- A imagem de abertura é um diagrama de especificação, não só um desenho conceitual: sobre o mockup de uma notificação aparecem guias de régua em forma de H (largura) e de I (altura) marcando margens e alinhamentos internos (img 0810).
- A anatomia padrão fica legível nesse diagrama: ícone do app à esquerda com guias de largura dos dois lados, título ao centro com linha pontilhada indicando a extensão do texto e guias de altura acima e abaixo, descrição logo abaixo com a mesma marcação, e o carimbo de tempo "now" no canto superior direito com guia de largura própria (img 0810).
- O conjunto é apoiado num cartão retangular de cantos arredondados e semitransparente, com a notificação tingida de vermelho e laranja (img 0810).
- O short look do watchOS é um cartão vertical em que o ícone circular grande, sobre fundo em gradiente escuro azul arroxeado, ocupa a maior parte da área superior, com título em negrito e uma prévia curta do conteúdo abaixo (img 0811).
- O long look aparece dentro da tela do relógio, com a hora no topo, ícone circular pequeno no canto superior esquerdo do cartão, "now" à direita, título em negrito, corpo de texto e dois botões de ação em largura total (img 0812).
- No long look o segundo botão de ação está cortado pela borda inferior da tela, recurso visual que indica que o conteúdo continua e pode ser rolado (img 0812).
- A diferença entre as duas etapas é construída pela proporção entre imagem e texto: no short look o ícone domina e o texto é mínimo; no long look o ícone encolhe para um selo no canto e o espaço passa a ser do texto e dos botões (img 0811 e img 0812).
Divergências registradas: a descrição oficial da img 0810 fala apenas em representação estilizada de uma notificação, mas a imagem vista é um diagrama com marcações de medida (guias H e I) sobre o layout.
<!-- /visual:notifications -->

## Snippets (slug: snippets)

### O que governa
Rege snippets, views compactas exibidas em resposta a uma ação realizada via Siri, Spotlight ou o app Shortcuts, mostrando resultado ou pedindo confirmação.

### Por que
A distinção entre snippet de confirmação e de resultado reflete duas necessidades distintas de interação por voz/intent: confirmar antes de agir (com possibilidade de opções que afetam o resultado) versus apenas informar o desfecho, que não exige mais ação. A regra de omitir o texto do diálogo falado da representação visual do snippet e usar a custom view para comunicar a informação visualmente evita redundância entre o que a Siri fala e o que a pessoa vê, reconhecendo que fala e leitura são canais complementares, não idênticos.

### Faça e evite
- Garanta legibilidade: verifique contraste suficiente entre o conteúdo customizado do snippet e o fundo fornecido pelo sistema, em ambas as aparências (clara e escura), e mantenha margens consistentes.
- Mantenha o conteúdo conciso, já que os snippets existem para interações rápidas e leves; crie custom views com altura máxima de 400 pontos para garantir que todo o conteúdo fique visível.
- Leve em conta que fontes desenham em tamanhos variados conforme a preferência de tamanho de texto da pessoa.
- Para um snippet de resultado, se precisar dar mais detalhe, faça deep link para o conteúdo no app em vez de incluí-lo na custom view.
- Escolha um rótulo descritivo para o botão primário de um snippet de confirmação (por exemplo, "Order" em vez de "OK" ou "Proceed" para pedir café); se nenhum rótulo for especificado, o padrão do sistema é "Continue".
- Comunique o propósito do snippet visualmente; não dependa de mostrar o texto do diálogo para transmitir o propósito. Prefira omitir o diálogo da representação visual e usar a custom view para transmitir a informação (o texto traz um exemplo explícito de uso incorreto, em que o diálogo repete a informação já mostrada na custom view, e um exemplo correto, em que o diálogo é omitido da parte visual).

### Especificações exatas
Altura máxima da custom view de um snippet: 400 pontos.

Componentes: um snippet de confirmação inclui dois botões fornecidos pelo sistema (Cancel secundário e um botão primário com rótulo customizável); um snippet de resultado inclui um único botão Done que dispensa a view.

### Diferenças por plataforma
- iOS, iPadOS, macOS: sem considerações adicionais.
- tvOS, visionOS, watchOS: não suportado.

### Ligações com outros artigos
Siri, App Shortcuts, Live Activities.

---

<!-- visual:snippets -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (8 imagens, todas em aparência clara), códigos conferidos; sem vídeos.
- A ilustração de abertura traz setas de medição no topo (horizontal) e na lateral direita (vertical) do cartão de calendário, tratando largura e altura como dimensões deliberadas do componente, e um contorno tracejado ao redor do bloco do evento que sugere a região customizável; sobre o gradiente laranja e vermelho, o botão "Done" aparece em vermelho (img 1088).
- O snippet é um cartão flutuante sobre a tela anterior, com a tela inicial desfocada ao fundo e a barra de status visível; ele não ocupa a tela inteira (img 1089 e img 1090).
- O snippet de confirmação separa conteúdo e ações: o cartão do app, em vermelho escuro com imagem do café e uma linha com stepper redondo de menos e mais, fica acima; os dois botões ficam na base, fora do cartão colorido, com "Cancel" cinza claro à esquerda e "Order" azul, mais largo, à direita (img 1089).
- O snippet de resultado tem um único botão azul "Done" ocupando a largura do cartão, sem opção de cancelar; o conteúdo usa barra de progresso verde quase cheia e uma fileira de quatro ícones circulares (img 1090).
- O diagrama de anatomia divide o cartão em três regiões rotuladas por uma chave lateral: diálogo no topo, custom view lilás ao centro com a cota vertical de altura máxima de 400 pt, e na base o par de botões secundário cinza à esquerda e primário azul à direita; é a única imagem que traz o valor numérico (img 1091).
- Par de errado: o texto de diálogo no topo repete nomes, data e horário que o cartão interno já mostra com ícone de calendário, título e participantes, e a imagem recebe o selo de X cinza em círculo (img 1092 e img 1093).
- Par de certo: o snippet de calendário da abertura (img 1088), agora sem nenhum texto de diálogo, com título e participantes só dentro do bloco tracejado da view e botão azul "Done", marcado com check branco em círculo verde (img 1094 e img 1095).
- Cores de destaque como rosa magenta e vermelho escuro identificam o conteúdo do app, contrastando com o restante do cartão em cinza e branco neutros (img 1089, img 1092 e img 1094).
<!-- /visual:snippets -->

## Status bars (slug: status-bars)

### O que governa
Rege a status bar, a faixa na borda superior da tela que exibe hora, operadora, sinal Wi-Fi e nível de bateria.

### Por que
A recomendação central, obscurecer o conteúdo sob a status bar, parte do fato de que seu fundo é transparente por padrão, o que pode confundir a pessoa ao tentar interagir com controles visíveis por trás dela sem conseguir. A permissão de ocultá-la temporariamente durante mídia em tela cheia reconhece que a status bar pode distrair quando a atenção da pessoa está no conteúdo, mas a proibição de escondê-la permanentemente preserva o acesso básico a hora e conectividade sem obrigar a pessoa a sair do app.

### Faça e evite
- Obscureça o conteúdo sob a status bar; como o fundo é transparente por padrão, prefira usar um scroll edge effect para posicionar uma view borrada atrás da status bar, mantendo-a legível e não sugerindo que o conteúdo atrás dela é interativo.
- Considere ocultar temporariamente a status bar ao exibir mídia em tela cheia, para uma experiência mais imersiva (o exemplo dado é o app Fotos ocultando a status bar ao navegar fotos em tela cheia).
- Evite ocultar a status bar permanentemente, pois sem ela a pessoa precisa sair do app para ver a hora ou a conexão Wi-Fi; permita reexibi-la com um gesto simples e descobrível (no exemplo do Fotos, um único toque a reexibe).

### Especificações exatas
Nenhum valor numérico é fornecido neste artigo.

### Diferenças por plataforma
- iOS, iPadOS: sem considerações adicionais.
- macOS, tvOS, visionOS, watchOS: não suportado.

### Ligações com outros artigos
Nenhum artigo relacionado é citado no corpo do texto.

---

<!-- visual:status-bars -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (3 imagens, todas em aparência clara), código conferido; sem vídeos.
- A abertura amplia os elementos da status bar do iPhone, com a hora à esquerda e, à direita, sinal celular, Wi-Fi e bateria cheia; cada elemento desce por uma linha vertical fina até um rótulo que nomeia o que ele representa (hora com local, barras de sinal, força do Wi-Fi, bateria em 100%). É peça didática, não captura real (img 1104).
- A linha de chamada do Wi-Fi é a mais longa e cruza por baixo do rótulo do sinal celular (img 1104).
- Com a status bar visível, ela fica diretamente sobre a foto no topo da tela, e logo abaixo vem uma barra de navegação translúcida com seta de voltar à esquerda, data e hora da foto ao centro e botão de mais opções com três pontos à direita (img 1105).
- Na versão oculta, a mesma foto com o mesmo enquadramento ocupa o quadro inteiro, sem status bar e também sem a barra de navegação; as duas camadas de interface somem juntas (img 1106).
- A recomendação de ocultar a status bar em mídia em tela cheia é demonstrada por um par quase idêntico em que só varia a presença das barras, sem os selos de X e check usados em outras páginas (img 1105 e img 1106).
<!-- /visual:status-bars -->

## Top Shelf (slug: top-shelf)

### O que governa
Rege a área Top Shelf da Home Screen da Apple TV, que exibe conteúdo em destaque de forma rica acima das linhas de apps no Dock.

### Por que
A ideia é que Top Shelf é a oportunidade de conduzir a pessoa diretamente ao conteúdo mais relevante assim que ela seleciona o app no Dock, sem etapas intermediárias. Por isso os templates de carrossel priorizam botões que levam direto à reprodução ou a mais informação. A recomendação de evitar anúncios e preços parte da lógica de que a pessoa já colocou o app em destaque porque confia nele; mostrar publicidade ali quebraria essa relação de confiança já estabelecida.

### Faça e evite
- Ajude a pessoa a entrar direto no conteúdo; os templates Carousel actions e Carousel details incluem, por padrão, um botão primário para iniciar a reprodução e um botão More Info para abrir o app em uma view de detalhes.
- Destaque conteúdo novo (lançamentos, episódios recentes, próximos filmes e séries) e evite promover conteúdo que a pessoa já comprou, alugou ou assistiu.
- Personalize o conteúdo favorito da pessoa, mostrando recomendações direcionadas e permitindo retomar reprodução ou jogo ativo.
- Evite mostrar anúncios ou preços; exibir conteúdo comprável é aceitável, mas prefira focar em conteúdo novo e empolgante, mostrando preços só quando houver interesse demonstrado.
- Mostre conteúdo dinâmico e envolvente que ajude a atrair a pessoa e incentive ver mais; se necessário, forneça imagens estáticas, mas prefira criar layered images para uma experiência dinâmica.
- Se não fornecer o conteúdo dinâmico em tela cheia recomendado, forneça ao menos uma imagem estática como fallback, exibida quando o app está em foco no Dock e não há conteúdo em tela cheia disponível; o tvOS espelha e borra a imagem para caber em 1920 pixels de largura na proporção 16:9.
- Evite sugerir interatividade em uma imagem estática, já que ela não é focável.

### Dynamic layouts

Carousel actions: foca em vídeo e imagens em tela cheia com controles discretos; funciona bem para conteúdo que a pessoa já conhece, como conteúdo gerado por usuário ou continuações de uma franquia. Forneça um título sucinto e, se necessário, um subtítulo breve.

Carousel details: estende o carousel actions, permitindo incluir informação sobre o conteúdo (sinopse, elenco, metadados). Forneça um título que identifique o conteúdo atual, exibido perto do topo da tela; acima do título é possível incluir uma frase sucinta ou atribuição ao app.

Sectioned content row: mostra uma única linha rotulada de conteúdo seccionado, útil para destacar conteúdo visto recentemente, novo ou favoritos; o conteúdo é focável, permitindo rolagem rápida, e um rótulo aparece quando um item entra em foco. Forneça conteúdo suficiente para preencher a largura completa da tela e inclua pelo menos um rótulo.

Scrolling inset banner: mostra uma série de imagens grandes que ocupam quase toda a largura da tela, com rolagem automática por temporizador até a pessoa focar em uma; a sequência retorna ao início após a última imagem. Forneça de três a oito imagens (mínimo de três é recomendado para o efeito funcionar; mais de oito dificulta a navegação a uma imagem específica). Se precisar de texto, adicione-o à própria imagem (esse layout não mostra rótulos abaixo do conteúdo), incluindo o texto também no accessibility label da imagem para que o VoiceOver o leia.

### Especificações exatas
- Imagem estática de fallback: 2320x720 pt (2320x720 px @1x, 4640x1440 px @2x).
- Poster (2:3): tamanho real 404x608 pt (808x1216 px @2x); zona segura/focada 380x570 pt (760x1140 px @2x); tamanho sem foco 333x570 pt (666x1140 px @2x).
- Square (1:1): tamanho real 608x608 pt (1216x1216 px @2x); zona segura/focada 570x570 pt (1140x1140 px @2x); tamanho sem foco 500x500 pt (1000x1000 px @2x).
- 16:9: tamanho real 908x512 pt (1816x1024 px @2x); zona segura/focada 852x479 pt (1704x958 px @2x); tamanho sem foco 782x440 pt (1564x880 px @2x). Ao misturar tamanhos de imagem numa mesma linha, imagens 16:9 escalam para 500 pixels de altura se combinadas com poster ou square.
- Scrolling inset banner: tamanho real 1940x692 pt (3880x1384 px @2x); zona segura/focada 1740x620 pt (3480x1240 px @2x); tamanho sem foco 1740x560 pt (3480x1120 px @2x).
- Número de imagens recomendado para scrolling inset banner: de três a oito.

### Diferenças por plataforma
Não suportado em iOS, iPadOS, macOS, visionOS ou watchOS; exclusivo do tvOS.

### Ligações com outros artigos
Apple Design Resources (para os templates de layout e layered images).

---

<!-- visual:top-shelf -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (5 imagens, todas em aparência clara), códigos conferidos; sem vídeos.
- A abertura organiza a tela em duas faixas: um título "Featured Content" sobre uma fileira de quatro cartões de imagem grandes, que representa o Top Shelf, e abaixo uma fileira de cinco ícones circulares de app, que representa a grade de apps (img 1187).
- É a única imagem com conteúdo de app simulado; as demais são diagramas técnicos abstratos, um por proporção de imagem (img 1187 a img 1191).
- O diagrama do pôster 2:3 empilha três retângulos concêntricos com réguas de anotação à direita: contorno cinza externo para o tamanho real, linha azul clara intermediária para a zona segura em foco e área azul sólida interna, a menor, para o tamanho sem foco (img 1188).
- Quadrado 1:1 e 16:9 repetem exatamente o mesmo esquema, com os mesmos três rótulos, a mesma ordem de fora para dentro e o mesmo código azul; muda só a proporção do retângulo (img 1189 e img 1190).
- Em todos os formatos o tamanho sem foco é a camada sólida mais interna e menor (img 1188 a img 1191); nos três diagramas de proporção fixa isso indica que a arte real precisa de margem além da área visível sem foco (img 1188 a img 1190).
- No banner com rolagem, uma faixa larga e baixa, a ordem das réguas muda: o rótulo da zona segura em foco aponta para a borda fina mais externa e o do tamanho real para a linha intermediária, invertendo a posição desses dois rótulos em relação aos três diagramas anteriores (img 1191).
<!-- /visual:top-shelf -->

## Watch faces (slug: watch-faces)

### O que governa
Rege o desenho e o compartilhamento de watch faces (mostradores), a view que a pessoa escolhe como principal no watchOS, e como um app pode configurar mostradores compartilháveis que destacam suas complications.

### Por que
O mostrador é descrito como o centro da experiência watchOS, e a possibilidade de compartilhar mostradores configurados (desde watchOS 7) reflete a lógica de que um mostrador bem curado, com as complications do app já configuradas, oferece uma experiência pronta sem exigir que a pessoa configure nada sozinha. Isso serve tanto para engajamento (uma professora de fitness compartilhando um mostrador com seus alunos) quanto para descoberta do app, já que quem adiciona o mostrador sem ter o app instalado é levado a instalá-lo.

### Faça e evite
- Ajude a pessoa a descobrir o app compartilhando mostradores que destacam suas complications; idealmente suporte múltiplas complications para compor uma experiência curada.
- Para alguns mostradores, é possível especificar cor de destaque do sistema, imagens ou estilos.
- Se a pessoa adicionar o mostrador sem ter o app instalado, o sistema solicita a instalação.
- Exiba uma prévia de cada mostrador compartilhado, destacando suas vantagens; é possível obter uma prévia enviando o mostrador para si mesmo por e-mail pelo app Watch no iOS, que inclui uma moldura ilustrada de dispositivo adequada para exibição em sites e apps. Alternativamente, é possível substituir a moldura ilustrada por uma moldura de hardware de alta fidelidade, disponível nos Apple Design Resources, e compor sobre a prévia.
- Procure oferecer mostradores compartilháveis para todos os dispositivos Apple Watch. Alguns mostradores estão disponíveis a partir do Series 4 (California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, Solar Dial), e o Explorer está disponível a partir do Series 3 com celular. Se usar um desses mostradores na configuração, considere oferecer uma configuração semelhante usando um mostrador disponível no Series 3 ou anterior, rotulando claramente os dispositivos suportados por cada mostrador compartilhável.
- Responda com elegância se a pessoa escolher um mostrador incompatível: o sistema envia um erro ao app quando isso ocorre em Series 3 ou anterior; considere oferecer imediatamente uma configuração alternativa com um mostrador compatível, em vez de exibir um erro, e ajude a pessoa a entender, junto das prévias, que ela pode receber um mostrador alternativo se escolher um incompatível com seu dispositivo.

### Especificações exatas
Nenhum valor numérico específico (medida, duração etc.) é dado; o artigo cita apenas nomes de mostradores e as gerações de hardware mínimas exigidas (Series 4 para a lista nomeada; Series 3 com celular para o Explorer).

### Diferenças por plataforma
Não suportado em iOS, iPadOS, macOS, tvOS ou visionOS; exclusivo do watchOS.

### Ligações com outros artigos
Apple Design Resources.

---

<!-- visual:watch-faces -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 imagem, em aparência clara), código conferido; sem vídeos.
- A abertura funciona como vitrine comparativa: três mostradores lado a lado, cada um recortado dentro de um retângulo arredondado de contorno tracejado e ligado por uma linha vertical ao seu nome escrito abaixo (img 1284).
- Os três exemplos mostram arranjos distintos de informação: Solar Graph com hora digital grande, dia da semana, curva solar e temperatura; GMT analógico redondo com ponteiros, marcação de 24 horas na borda, indicador de atividade no canto superior e dados numéricos na base; Unity Lights com ponteiros brancos finos e escalas curvas nos cantos para decibéis, data e temperatura (img 1284).
- O conjunto usa gradiente diagonal de laranja para rosa avermelhado no fundo, e não um tingimento vermelho uniforme (img 1284).
Divergências registradas: a descrição oficial fala só numa representação estilizada de uma série de mostradores tingida de vermelho; a imagem traz os três nomes por extenso (Solar Graph, GMT, Unity Lights) com linha conectora entre cada mostrador e seu nome, o que a descrição não menciona.
<!-- /visual:watch-faces -->

## Widgets (slug: widgets)

### O que governa
Rege o desenho de widgets, que dão acesso rápido a informação essencial e interações focadas do app em contextos além do app em si (Home Screen, Lock Screen, desktop do Mac, superfícies do Apple Vision Pro, Smart Stack do Apple Watch, CarPlay).

### Por que
O princípio recorrente do artigo é o de balanço entre densidade de informação e capacidade de leitura rápida (glanceability): um widget disperso demais parece desnecessário, um widget denso demais deixa de ser glanceable. A insistência em conteúdo dinâmico ("prefira informação que muda ao longo do dia") decorre da constatação de que, se o conteúdo nunca muda, a pessoa tende a não manter o widget em posição de destaque. As múltiplas regras sobre modos de renderização (full-color, accented, vibrant) e sobre como cada plataforma aplica esses modos existem porque o mesmo widget precisa se adaptar à personalização de aparência que a pessoa escolhe (clara, escura, tintada, clara translúcida), sem perder legibilidade nem significado transmitido só por cor.

### Faça e evite
- Escolha ideias simples relacionadas ao propósito principal do app; inclua conteúdo pontual e funcionalidade relevante.
- Crie um widget que dê acesso rápido ao conteúdo que a pessoa quer; replicar o ícone do app agrega pouco valor adicional.
- Prefira informação dinâmica que muda ao longo do dia; se o conteúdo nunca parecer mudar, a pessoa pode não manter o widget em posição de destaque.
- Procure oportunidades de surpreender e encantar, como um tratamento visual único em ocasiões especiais.
- Ofereça widgets em múltiplos tamanhos quando isso agregar valor; widgets pequenos tendem a mostrar uma única informação, tamanhos maiores suportam camadas adicionais. Evite simplesmente expandir o conteúdo de um widget pequeno para preencher uma área maior; é mais importante criar um widget no tamanho que melhor representa o conteúdo do que oferecer todos os tamanhos.
- Equilibre densidade de informação: layouts esparsos parecem desnecessários, layouts densos demais são menos glanceable; se o layout estiver denso demais, considere um tamanho maior ou substituir texto por gráficos.
- Exiba apenas informação diretamente relacionada ao propósito principal do widget, mesmo em tamanhos maiores com mais dados.
- Use elementos de marca com cuidado (cores, tipografia, glifos estilizados) para tornar o widget reconhecível sem sobrepor a informação útil; um pequeno logo no canto superior direito é suficiente quando o widget mostra conteúdo de múltiplas fontes.
- Escolha entre exibir conteúdo automaticamente ou permitir personalização, dependendo se a informação exige configuração (o exemplo dado é o widget Stocks, que exige escolher os símbolos, versus o widget Podcasts, que exibe conteúdo recente automaticamente).
- Evite espelhar a aparência do widget dentro do próprio app, para não confundir a pessoa sobre seu comportamento.
- Deixe claro quando a autenticação agrega valor, por exemplo com uma mensagem do tipo "Sign in to view reservations" quando a pessoa está deslogada.

### Atualização de conteúdo
- Mantenha o widget atualizado, encontrando a frequência apropriada conforme a frequência de mudança do dado e quando a pessoa precisa ver o dado novo; se a pessoa checar o widget com mais frequência do que ele pode atualizar, considere exibir texto informando quando o dado foi atualizado pela última vez.
- Use a funcionalidade do sistema para atualizar datas e horas, já que a frequência de atualização do widget é limitada.
- Use transições animadas para chamar atenção a atualizações de dado, com duração de até dois segundos.

### Interatividade
- A pessoa toca ou clica no widget para abrir o app correspondente; ele também pode incluir botões e toggles para funcionalidade adicional sem abrir o app (o exemplo dado é o widget Reminders com toggles para marcar tarefas concluídas).
- Ofereça funcionalidade simples e relevante, reservando complexidade para o app.
- Garanta que a interação abra o app na localização correta, com deep link direto a detalhes e ações relacionadas ao conteúdo do widget.
- Ofereça interatividade mantendo o widget glanceable e organizado; evite criar layouts semelhantes a apps dentro do widget, e preste atenção ao tamanho dos alvos de toque. Widgets acessórios inline oferecem apenas um alvo de toque.

### Margens e padding
- Use margens padrão para garantir legibilidade: a largura de margem padrão para a maioria dos widgets é de 16 pontos; margens mais justas de 11 pontos podem funcionar para agrupamentos de conteúdo como gráficos, botões ou formas de fundo. Widgets usam margens menores no desktop do Mac e na Lock Screen, incluindo no StandBy.
- Coordene o raio de canto do conteúdo com o raio de canto do widget, usando um container do SwiftUI (ContainerRelativeShape).

### Texto em widgets
- Prefira a fonte do sistema, os estilos de texto e o SF Symbols; se usar fonte customizada, use com moderação, garantindo legibilidade rápida (funciona bem usar fonte customizada só no texto grande e SF Pro no texto menor).
- Evite tamanhos de fonte muito pequenos; em geral, use fontes de 11 pontos ou maiores, já que texto menor que 11 pontos pode ser difícil de ler.
- Evite rasterizar texto; use sempre elementos e estilos de texto para garantir boa escala e permitir que o VoiceOR leia o conteúdo. Em iOS, iPadOS e visionOS, widgets suportam tamanhos de Dynamic Type de Large até AX5 ao usar Font ou custom(_:size:).

### Uso de cor
- Use cor para realçar a aparência do widget sem competir com o conteúdo.
- Transmita significado sem depender exclusivamente de cores específicas, já que widgets podem aparecer monocromáticos (com ou sem tint customizado) e, no watchOS, o sistema pode inverter cores dependendo do mostrador escolhido; use texto e iconografia além de cor para expressar significado.
- Use imagens em cor plena com critério: quando a pessoa escolhe aparência tintada ou clara translúcida, o sistema dessatura imagens coloridas por padrão; é possível optar por renderizar imagens em cor plena mesmo nesses casos, mas isso chama atenção especial para o widget, podendo parecer fora de lugar. Considere reservar imagens em cor plena para representar conteúdo de mídia (como a capa de um álbum), em dimensões menores que o tamanho do widget.

### Modos de renderização
- Full-color: suporte às aparências clara e escura, preferindo fundos claros na aparência clara e fundos escuros na escura; considere usar as cores semânticas do sistema para texto e fundo, ou variantes de cor no catálogo de assets.
- Accented: agrupa os componentes do widget em um grupo accented e um grupo primary. No iPhone, iPad e Mac, o sistema tinge o conteúdo primary e accented de branco; no Apple Watch, tinge o conteúdo primary de branco e o accented na cor do mostrador escolhido.
- Vibrant: garanta contraste suficiente para legibilidade. Nesse modo, a opacidade dos pixels de uma imagem determina a força do efeito de material borrado de fundo (pixels totalmente transparentes deixam o material de fundo passar como está); o brilho dos pixels determina a vibração na Lock Screen (valores de cinza mais claros dão mais contraste, valores mais escuros dão menos). Renderize conteúdo como imagens, números e texto em opacidade plena; use branco ou cinza claro para o conteúdo mais proeminente e valores de cinza mais escuros para elementos secundários, usando valores opacos de escala de cinza em vez de opacidades de branco para o melhor efeito.

### Prévias e placeholders
- Desenhe uma prévia realista para a galeria de widgets, destacando as capacidades do widget; pode exibir dado real, mas se ele demorar para carregar, exiba dado simulado realista.
- Desenhe conteúdo de placeholder que ajude a reconhecer o widget, combinando componentes estáticos de interface com formas semiopacas representando conteúdo dinâmico (retângulos de larguras diferentes sugerindo linhas de texto, círculos ou quadrados no lugar de glifos e imagens).
- Escreva uma descrição sucinta do widget, começando com um verbo de ação (exemplos dados: "See the current weather conditions and forecast for a location", "Keep track of your upcoming events and meetings"); evite frases desnecessárias que referenciem o próprio widget, como "This widget shows...", "Use this widget to...", "Add this widget". Use linguagem acessível e sentence-style capitalization.
- Agrupe os tamanhos do widget e forneça uma única descrição, para não parecer que cada tamanho é um widget diferente.
- Considere colorir o botão Add, após a pessoa escolher o app na galeria, para reforçar a marca.

### Especificações exatas

Margem padrão: 16 pontos (a maioria dos widgets); margens mais justas de 11 pontos para agrupamentos internos.

Tamanho mínimo de fonte recomendado: 11 pontos.

Duração máxima de animação em atualização de dado: 2 segundos.

Escala permitida a widgets no visionOS (ajuste de tamanho pela pessoa): de 75% a 125%.

Dimensões iOS por tamanho de tela (portrait, pt): tabela relaciona Small, Medium, Large, Circular, Rectangular e Inline para dez tamanhos de tela, de 320x568 a 430x932. Exemplos: tela 430x932 → Small 170x170, Medium 364x170, Large 364x382, Circular 76x76, Rectangular 172x76, Inline 257x26; tela 320x568 → Small 141x141, Medium 292x141, Large 292x311 (Circular, Rectangular e Inline não disponíveis, N/A).

Dimensões iPadOS: tabela relaciona, para nove tamanhos de tela (de 768x1024 a 1192x1590, este último com Display Zoom em "More Space"), os valores de Canvas e Device para Small, Medium, Large e Extra large. Exemplo: tela 1024x1366, Canvas → Small 170x170, Medium 378.5x170, Large 378.5x378.5, Extra large 795x378.5; Device → Small 160x160, Medium 356x160, Large 356x356, Extra large 748x356.

Dimensões visionOS (em pontos e em milímetros a 100% de escala): Small 158x158 pt (268x268 mm); Medium 338x158 pt (574x268 mm); Large 338x354 pt (574x600 mm); Extra large 450x338 pt (763x574 mm); Extra large portrait 338x450 pt (574x763 mm).

Dimensões watchOS (Smart Stack, pt): 40mm 152x69.5; 41mm 165x72.5; 44mm 173x76.5; 45mm 184x80.5; 49mm 191x81.5.

### Diferenças por plataforma
- macOS: sem considerações adicionais.
- tvOS: não suportado.
- iOS, iPadOS: widgets na Lock Screen são funcionalmente semelhantes a watch complications e seguem também os princípios de design de Complications, além dos princípios de widgets; em muitos casos um design para complications também funciona bem para widgets na Lock Screen e vice-versa. O app pode oferecer widgets na Lock Screen em três formatos: texto inline acima do relógio, e formas circular e retangular abaixo do relógio. Deve suportar o display Always-On no iPhone, usando níveis de cinza com contraste suficiente sob luminância reduzida. Deve considerar oferecer Live Activities para atualizações em tempo real, já que widgets não mostram informação em tempo real; widgets e Live Activities compartilham frameworks e semelhanças de design, sendo boa prática desenvolvê-los em conjunto.
  - StandBy e CarPlay: no iPhone em StandBy, o sistema exibe dois widgets pequenos da família de sistema lado a lado, ampliados para preencher a Lock Screen. Suportar StandBy também garante bom funcionamento em CarPlay, que usa o mesmo widget pequeno com o fundo removido, ampliado para caber na grade da tela de Widgets. Limite o uso de imagens ricas ou cor para transmitir significado no StandBy; em vez disso, aproveite o espaço extra ampliando e reorganizando texto, e não use cores de fundo para mesclar com o fundo preto. Em condições de pouca luz no StandBy, o sistema renderiza os widgets em aparência monocromática com tint vermelho.
- visionOS: widgets são objetos 3D que a pessoa posiciona em uma superfície horizontal ou vertical; o widget persiste na posição mesmo quando o Apple Vision Pro é desligado e religado, com escala consistente ao mundo real. Aparecem em cor plena por padrão, mas passam ao modo accented quando a pessoa personaliza com cores de tint de paletas fornecidas pelo sistema; é possível customizar a largura da moldura de widgets no estilo elevated. Não há aparências claras/escuras em nível de sistema no visionOS (exceção citada: o widget de poster do Music oferece sua própria opção de tema claro/escuro gerado a partir da arte do álbum). Deve-se adaptar o design ao contexto espacial (living rooms, cozinhas, escritórios), testando em toda a gama de paletas de cor do sistema e condições de iluminação.
  - Thresholds e tamanhos: dois limiares de distância, simplified (visualização à distância) e default (visualização de perto). No threshold à distância, mostre uma versão simplificada com menos detalhes, tipografia maior e sem elementos interativos; de perto, mostre mais detalhes com tipografia menor, mantendo elementos compartilhados entre os dois limiares para continuidade. Escolha o tamanho de família de widget adequado ao contexto real onde a pessoa o posicionará (mesa, parede, aparador).
  - Mounting styles: elevated (padrão, funciona em superfícies horizontais e verticais, inclina-se levemente para trás em superfícies horizontais e projeta sombra suave; em superfícies verticais pode ficar rente, como um quadro) e recessed (só em superfícies verticais, o conteúdo parece recuado na superfície, criando efeito de profundidade tipo recorte). Escolha o estilo conforme o conteúdo: elevated para conteúdo que deve se destacar (lembretes, mídia, dados glanceable); recessed para conteúdo imersivo ou ambiente (clima, conteúdo editorial). É possível restringir o widget a um único estilo suportado.
  - Treatment styles: paper (aparência impressa, mais sólida, responde à luz ambiente escurecendo ou clareando; exemplo dado é o widget de poster do Music) e glass (aparência em camadas, separa visualmente primeiro plano e fundo, mantendo elementos de primeiro plano sempre brilhantes e legíveis independentemente da luz ambiente; exemplo dado é um widget de notícias com imagens editoriais de fundo e manchetes nítidas em primeiro plano).
- watchOS: por padrão os widgets no Smart Stack usam fundo preto; considere uma cor de fundo customizada que transmita significado adicional (o exemplo dado é o app Stocks usando fundo vermelho para queda e verde para alta). É possível incentivar o sistema a exibir ou elevar a posição do widget no Smart Stack fornecendo informação de relevância (baseada em localização ou em ações do sistema em curso, como um treino).

### Ligações com outros artigos
Layout, Dark Mode, Complications, Live Activities, StandBy, CarPlay.

---

<!-- visual:widgets -->
### O que as ilustrações mostram
Base: 10 folhas de ilustrações vistas (38 imagens, todas registradas como aparência clara), códigos conferidos; sem vídeos.
- A progressão de tamanho do widget de Calendário é feita por acréscimo de colunas, não por aumento de fonte: o pequeno mostra só o dia e dois eventos; o médio tem a mesma altura e o dobro da largura, com hoje e amanhã em duas colunas; o grande acrescenta régua vertical de horas com linha vermelha na hora atual e eventos posicionados sobre ela; o extra grande estende a régua a quatro dias, com a coluna de hoje visivelmente mais larga. Os eventos seguem sempre o mesmo padrão de barra lilás com traço vertical colorido à esquerda (img 1287, img 1288, img 1289 e img 1290). Já o extra grande retrato de Música empilha blocos, capa na metade superior e metadados na inferior sobre fundo claro (img 1291).
- Os formatos acessórios trocam o cartão por formas próprias com tipografia adaptada: circular com ícone pequeno sobre círculo translúcido e só a hora do próximo evento; de canto com texto curvo acompanhando o arco do mostrador, hora em branco e título em vermelho sobre preto; inline como uma única linha numa faixa translúcida, sem cartão; retangular com duas linhas de evento empilhadas (img 1292, img 1293, img 1294 e img 1295). Na Lock Screen do iPhone, o texto inline fica acima do relógio grande e os widgets circulares abaixo dele (img 1316).
- O mesmo widget pequeno de Stocks, com o mesmo layout, muda só cor e opacidade entre aparências: em cor plena mantém fundo preto e verde semântico de alta; em clara fica dessaturado e translúcido, deixando o fundo aparecer; tintado aplica um único roxo a fundo, texto e gráfico, apagando o verde; na Lock Screen do iPad vira monocromático castanho sobre fundo castanho (img 1296, img 1297, img 1298 e img 1300).
- No Apple Vision Pro o widget vira objeto com moldura branca espessa, sombra e profundidade, preservando as cores plenas; em StandBy aparece maior, em vermelho monocromático sobre preto total (img 1299, img 1301 e img 1302).
- No Apple Watch o mesmo cartão de evento assume três tratamentos: faixa com fundo texturizado bege e traço rosa claro separando hora e título; complicação retangular com fundo preto sólido, traço vermelho e texto branco e cinza; no Smart Stack, cartão claro com traço vermelho flutuando destacado sobre o preto ao redor (img 1303, img 1304 e img 1305).
- O widget pequeno de Weather mostra a hierarquia tipográfica: local pequeno com ícone no topo, temperatura enorme ao centro, condição e máxima e mínima menores embaixo, sobre degradê azul (img 1306).
- O estado de toggle é mostrado pelo mesmo widget de Reminders lado a lado: sete tarefas com círculos vazios e, na outra versão, o primeiro e o terceiro círculos preenchidos em vermelho sólido, sem nenhuma outra mudança de layout (img 1307 e img 1308). O widget médio de watchlist alinha cada linha em três colunas, nome, minigráfico verde e valor com variação (img 1309).
- Em cor plena, a versão clara e a escura do widget de Notes trocam só o fundo do corpo e a cor do texto (branco com texto preto, preto com texto branco); a barra amarela de marca no topo permanece idêntica (img 1310 e img 1311).
- O placeholder usa a mesma geometria do conteúdo final: três barras amarelas mais claras de larguras decrescentes no cartão amarelo viram as três linhas de texto real na versão carregada (img 1312 e img 1313).
- Na galeria, um cartão modal sobe da base com título, descrição, miniatura do widget, indicador de páginas e botão "Add Widget" na cor de marca do app, amarelo no Notes e azul no Weather (img 1314 e img 1315).
- Par de StandBy: certo é o relógio analógico e o Weather em branco sobre preto, sem cartão nem moldura, com selo de check verde; errado é o Weather mantendo o cartão azul arredondado com sombra da Tela de Início, destacado do preto, com selo de X cinza. Em pouca luz tudo passa a vermelho monocromático, inclusive os números do mostrador (img 1317 a img 1321).
- No visionOS, a mesma cena em moldura branca em perspectiva adapta densidade à distância: vista de longe tem capa e texto pequeno sem lista de faixas; vista de perto o cartão fica maior e ganha um bloco extra com quatro linhas de nomes de faixa (img 1322 e img 1323).
Divergências registradas: as legendas distinguem StandBy padrão e StandBy em pouca luz para img 1301 e img 1302, mas as notas registram que a diferença não é distinguível a olho; as duas usam o mesmo vermelho sobre preto.
<!-- /visual:widgets -->

## O que este grupo revela sobre o jeito Apple

1. Honestidade estrita de estado: em quase todo artigo do grupo (controls, complications, notifications, widgets, live-activities) há a mesma regra subjacente, o componente precisa refletir o estado real e atual, nunca um estado congelado ou enganoso; badges só contam notificações não lidas, complications não devem ser estáticas, controls precisam se atualizar após cada interação. Sustentado por: controls, complications, notifications, widgets.

2. Privacidade como restrição de design, não só de política: vários componentes ficam expostos a olhares alheios (Always-On display, Lock Screen, curtos looks no pulso) e a resposta de design é sempre a mesma, redigir/ocultar informação sensível e exibir só um resumo inócuo, deixando o detalhe para dentro do app autenticado. Sustentado por: complications, live-activities, notifications, controls.

3. O texto falado (Siri) e o texto visual não são intercambiáveis: tanto em App Shortcuts quanto em Snippets, a Apple separa explicitamente o que a Siri fala do que aparece na tela, chegando a recomendar omitir o diálogo da representação visual para não duplicar informação. Sustentado por: app-shortcuts, snippets.

4. Geometria física dita regra de layout: o formato arredondado da Dynamic Island (ao redor da câmera TrueDepth) e o raio de canto dos widgets geram regras extremamente específicas de margem concêntrica, blur para alinhar bordas, e uso de ContainerRelativeShape, mostrando que o hardware físico do dispositivo molda diretamente as regras de HIG, não apenas convenções abstratas de UI. Sustentado por: live-activities, widgets.

5. Especificação numérica muda de granularidade conforme o risco de erro: componentes altamente geométricos e replicados em muitos tamanhos de tela (complications, widgets, top-shelf, live-activities) vêm com tabelas extensas de pontos e pixels por tamanho de dispositivo; componentes mais conceituais e sem geometria fixa (notifications, status-bars, watch-faces, controls) não trazem nenhum valor numérico. Sustentado por: complications, widgets, top-shelf, live-activities, notifications, status-bars, watch-faces, controls.

6. Recorrência do princípio "menos é mais útil": todos os componentes glanceable do grupo (widgets, complications, live-activities, notifications) compartilham a mesma advertência, mostrar só a informação essencial, com deep link para o app quando for preciso mais detalhe; excesso de densidade é tratado como falha de design, não como recurso. Sustentado por: widgets, complications, live-activities, notifications.

7. A marca deve aparecer sem competir com a função: em controls, live-activities, widgets e top-shelf, a Apple permite uso de cor e identidade visual da marca, mas sempre com a ressalva de que a marca não pode ofuscar a informação funcional nem imitar componentes do sistema (por exemplo, não replicar a aparência de um badge, não usar o ícone completo do app como logo mark). Sustentado por: controls, live-activities, widgets, top-shelf.

8. Modularidade cross-device como requisito de design, não add-on: Live Activities e widgets precisam ser desenhados desde o início para múltiplas apresentações (compact, minimal, expanded, Lock Screen, StandBy, CarPlay, watchOS, visionOS), e o texto recomenda explicitamente começar pelo iPhone e depois adaptar, em vez de desenhar cada plataforma isoladamente. Sustentado por: live-activities, widgets, complications.

9. Onde a ação é possível, ela deve ser mínima e única: controls, notifications e live-activities recomendam limitar a interatividade a poucos elementos (idealmente um), com preferência por ações não destrutivas e por evitar layouts "parecidos com app" dentro de um componente que deveria ser glanceable. Sustentado por: controls, notifications, live-activities, widgets.

10. Legado técnico é tratado com pragmatismo, não ocultado: tanto em complications quanto em App Shortcuts há reconhecimento explícito de frameworks anteriores (ClockKit, legacy templates) e orientação clara de migração (preferir WidgetKit, preferir app schemas a App Shortcuts individuais quando aplicável), mostrando que a HIG documenta a transição tecnológica, não só o estado ideal final. Sustentado por: complications, app-shortcuts.

## Evidência de leitura

| Arquivo | Linhas lidas | Lido até o fim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/app-shortcuts.md | 64 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/complications.md | 224 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/controls.md | 60 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/live-activities.md | 270 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/notifications.md | 90 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/snippets.md | 49 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/status-bars.md | 22 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/top-shelf.md | 84 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/watch-faces.md | 26 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/widgets.md | 285 | sim |

Todos os 10 arquivos do grupo foram lidos por inteiro em uma única chamada de Read cada, sem sinal de truncamento (nenhum arquivo se aproximou do limite padrão de leitura). Nenhum artigo deste grupo é apenas índice de coleção sem texto próprio.
