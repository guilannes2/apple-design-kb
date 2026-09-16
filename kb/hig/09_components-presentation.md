# Components / Presentation

## Action sheets (slug: action-sheets)

O que governa: um action sheet é uma view modal que apresenta escolhas relacionadas a uma ação que a pessoa iniciou deliberadamente.

Por que: a Apple distingue action sheet de alerta pela intenção. Um action sheet aparece porque a pessoa fez algo que exige esclarecimento (por exemplo, cancelar uma mensagem em edição), enquanto um alerta é geralmente inesperado, avisando sobre um problema ou mudança de situação que a pessoa não provocou diretamente. Interromper a tarefa atual tem custo, por isso o uso deve ser raro e o texto deve ser rápido de entender.

Faça e evite:
- Use action sheet, não alerta, para oferecer escolhas ligadas a uma ação intencional.
- Use action sheets com moderação, porque interrompem a tarefa atual.
- Mantenha títulos curtos o bastante para caber em uma linha; título longo é difícil de ler rápido e pode truncar ou exigir rolagem.
- Forneça uma mensagem só se necessário; o título mais o contexto da ação geralmente bastam.
- Se necessário, forneça um botão Cancel que permita rejeitar uma ação que destruiria dados; posicione-o na parte inferior do action sheet (ou no canto superior esquerdo no watchOS). Um confirmation dialog em SwiftUI já inclui Cancel por padrão.
- Torne escolhas destrutivas visualmente proeminentes: use o estilo destrutivo e posicione esses botões no topo, onde chamam mais atenção.
- Em iOS e iPadOS, use action sheet, não menu, para escolhas ligadas a uma ação; pessoas esperam um menu quando escolhem revelá-lo, não como resposta a uma ação.
- Evite deixar um action sheet rolar em iOS/iPadOS; quanto mais botões, mais esforço para escolher, e rolar pode causar toque acidental.
- No watchOS, evite mostrar mais de quatro botões, incluindo Cancel; como Cancel é obrigatório, o alvo é no máximo três escolhas adicionais.

Especificações exatas: nenhum número de medida (pt, px, ms) é dado no texto. O único limite numérico é o de botões no watchOS: até quatro botões no total (Cancel incluído), ou seja, no máximo três escolhas além do Cancel.

Diferenças por plataforma:
- iOS, iPadOS: action sheet em vez de menu para ações; evitar rolagem.
- watchOS: estilo definido pelo sistema com título, mensagem opcional, botão Cancel e um ou mais botões adicionais; três estilos de botão definidos pelo sistema (Default, Destructive, Cancel); aparência varia por dispositivo.
- macOS, tvOS: sem considerações adicionais.
- visionOS: não suportado.

Ligações com outros artigos: Modality, Sheets, Alerts.

<!-- visual:action-sheets -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido; a página não tem vídeo.
- O diagrama de abertura isola um cartão claro com título em negrito, descrição curta abaixo e três botões em pílula empilhados, com contorno tracejado; uma seta dupla horizontal acima mede a largura total e uma marcação vertical à direita mede a altura do cartão, então a imagem trata o componente como bloco de proporções, e não como tela de app (img 0025).
- A hierarquia interna do cartão é título, depois descrição, depois a pilha de três ações, todas com o mesmo formato de pílula (img 0025).
- No Mail do iPhone, a primeira captura mostra o estado de composição, com botão X de fechar, botão de envio azul circular com seta para cima e os campos da mensagem (img 0026).
- A segunda captura repete exatamente a mesma tela e muda só a sobreposição: um cartão branco flutuante logo abaixo da barra de status, cobrindo parte do topo e deixando o e-mail visível atrás, com dois botões em pílula empilhados (img 0027).
- Nessa action sheet os dois botões empilhados são "Delete Draft" em vermelho e "Save Draft" em preto (img 0027).
- O par antes e depois com o mesmo fundo deixa claro, por comparação direta, que se trata de um fluxo de dois passos disparado pela ação da pessoa, e não de duas telas independentes (img 0026, img 0027).
- No watchOS, a action sheet ocupa a tela sobre degradê azul escuro para roxo, com X de fechar no canto superior esquerdo, título e descrição centralizados em branco e dois botões grandes em pílula empilhados, a ação em verde e o Cancel em degradê roxo e magenta, ou seja, botões coloridos por função em vez de neutros (img 0028).
Divergências registradas: a img 0025 diverge da descrição oficial, que fala de botões na parte inferior de um iPhone, enquanto a imagem mostra um cartão isolado com anotações de largura e altura, sem iPhone e sem posição na tela; a img 0028 mostra texto e rótulos reais e cores distintas por botão, onde a descrição oficial fala genericamente em conteúdo que representa texto e dois botões empilhados.
<!-- /visual:action-sheets -->

## Alerts (slug: alerts)

O que governa: um alerta dá à pessoa informação crítica que ela precisa receber imediatamente, como um problema, um aviso de que a ação pode destruir dados, ou a chance de confirmar uma compra ou outra ação importante que ela mesma iniciou.

Por que: alertas interrompem a tarefa atual, então a Apple trata essa interrupção como um custo que só se justifica quando a informação é essencial e acionável. O texto do documento insiste em tom direto e neutro porque alertas costumam descrever problemas sérios, e ser vago ou acusatório piora a experiência justamente no momento em que a pessoa mais precisa de clareza. A escolha entre título de frase completa e fragmento de frase segue a mesma lógica de precisão de linguagem usada em outros componentes de texto da Apple.

Faça e evite:
- Use alertas com moderação; cada um deve oferecer só informação essencial e ações úteis.
- Evite usar um alerta apenas para informar, sem ação associada; prefira comunicar isso de outra forma dentro do contexto relevante.
- Evite alertas para ações comuns e desfazíveis, mesmo destrutivas, porque a pessoa já tem a intenção de descartar o dado e pode desfazer.
- Evite mostrar alerta ao iniciar o app; se precisar informar algo importante logo de início, torne a informação descobrível de outra forma, como dados em cache ou um rótulo discreto.
- Em todo o texto do alerta, seja direto e use tom neutro e acessível; evite ser oblíquo, acusatório ou mascarar a gravidade.
- Escreva um título que descreva a situação com clareza e concisão, descrevendo o que aconteceu, o contexto e por quê, sem ser verboso; evite títulos vazios como "Error" ou "Error 329347 occurred" e evite títulos longos que quebrem em mais de duas linhas.
- Se o título for frase completa, use capitalização de frase e pontuação final apropriada; se for fragmento, use capitalização de título e não use pontuação final.
- Inclua texto informativo só se agregar valor; se precisar, mantenha curto, com frases completas e pontuação adequada.
- Evite explicar os botões do alerta se o texto e os títulos dos botões já forem claros.
- Se suportado, inclua campo de texto só quando a entrada da pessoa for necessária para resolver a situação.
- Crie títulos de botão sucintos e lógicos, com uma ou duas palavras que descrevam o resultado de selecionar o botão; prefira verbos e frases verbais relacionadas ao texto do alerta ("View All", "Reply", "Ignore"). Em alertas puramente informativos, pode usar "OK" para aceitação, evitando "Yes" e "No". Sempre use "Cancel" para o botão que cancela a ação do alerta.
- Evite usar "OK" como título do botão padrão a não ser que o alerta seja puramente informativo, porque o significado de "OK" pode ficar ambíguo.
- Posicione os botões onde a pessoa espera: em geral, o botão mais provável de ser escolhido fica no lado à direita (trailing) numa linha de botões ou no topo numa pilha; o botão padrão sempre fica no lado à direita ou no topo. Botões Cancel ficam tipicamente à esquerda (leading) numa linha ou embaixo numa pilha.
- Use o estilo destrutivo para identificar um botão que executa uma ação destrutiva que a pessoa não escolheu deliberadamente. Quando a pessoa já escolheu deliberadamente uma ação destrutiva (como Empty Trash), o alerta resultante não aplica o estilo destrutivo ao botão, porque o botão cumpre a intenção original da pessoa.
- Se houver uma ação destrutiva, inclua um botão Cancel para dar uma forma clara e segura de evitar a ação; nunca torne o Cancel o botão padrão. Se quiser encorajar a pessoa a ler o alerta em vez de simplesmente apertar Return, evite tornar qualquer botão padrão. Se precisar exibir um alerta com um único botão que também é o padrão, use um botão Done, não um Cancel.
- Ofereça formas alternativas de cancelar um alerta quando fizer sentido, além do botão Cancel.
- Em iOS e iPadOS, use action sheet, não alerta, para oferecer escolhas ligadas a uma ação intencional (exemplo: cancelar mensagem no Mail oferece três escolhas: apagar as edições, salvar o rascunho ou voltar a editar).
- Evite, quando possível, exibir um alerta que role; mantenha títulos curtos e mensagem breve só quando necessária.
- Em macOS, use o símbolo de aviso (`exclamationmark.triangle`) com moderação, só quando a atenção extra for realmente necessária, como confirmar uma ação que pode causar perda inesperada de dados; não use o símbolo para tarefas cujo único propósito é sobrescrever ou remover dados, como salvar ou esvaziar a lixeira.

Especificações exatas:
- visionOS: se precisar exibir uma accessory view em um alerta, crie uma view com altura máxima de 154 pt e raio de canto de 16 pt.
- Em todos os alertas, até três botões no total.

Diferenças por plataforma:
- iOS, iPadOS: preferir action sheet para escolhas ligadas a ações intencionais; minimizar rolagem do alerta.
- macOS: exibe automaticamente o ícone do app no alerta, mas permite ícone ou símbolo alternativo; permite alertas repetíveis com supressão de ocorrências subsequentes; permite accessory view customizada; permite botão Help; uso comedido do símbolo de aviso.
- visionOS: no Shared Space, o alerta aparece na frente da janela do app, ligeiramente à frente no eixo z; se a pessoa mover a janela sem dispensar o alerta, ele permanece ancorado à janela; no Full Space, o alerta aparece centralizado no campo de visão.
- tvOS, watchOS: sem considerações adicionais. Formas alternativas de cancelar variam: sair para a Tela de Início (iOS, iPadOS); Escape ou Command-Período com teclado conectado (iOS, iPadOS, macOS, visionOS); pressionar Menu no controle remoto (tvOS).

Ligações com outros artigos: Modality, Action sheets, Sheets.

<!-- visual:alerts -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações vistas, mais 1 de 1 folha do vídeo hig-vid_alerts__002 e 3 de 3 folhas do vídeo hig-vid_alerts__003, todos os códigos conferidos.
- O diagrama de abertura é o único com cotas: setas duplas no topo, à esquerda e à direita do cartão e um pequeno chevron embaixo, que as notas leem como anotações de dimensão e possivelmente de margens; dentro, título em negrito, descrição e dois botões em pílula lado a lado, o secundário em rosa claro e o primário em vermelho forte com texto em negrito maior, o que marca a hierarquia entre as duas ações pela cor e pelo peso (img 0046).
- No iPhone, o alerta é pequeno e centralizado sobre fundo cinza sólido, com os dois botões lado a lado, o secundário em cinza claro e o primário em azul preenchido (img 0047).
- No Mac, o alerta é mais compacto, centralizado sobre a janela, e os botões ficam empilhados, com o primário azul preenchido em cima e o secundário cinza claro embaixo (img 0048).
- No tvOS, o alerta é semitransparente sobre uma foto de paisagem, deslocado à direita do centro, com os botões lado a lado e o primário em azul preenchido (img 0049).
- No Vision Pro, o alerta é um painel de vidro fosco translúcido sobre um ambiente doméstico desfocado, com ícone circular azul de exclamação no topo e botões empilhados sem preenchimento sólido, no mesmo material do painel (img 0050).
- No Apple Watch, título e descrição ficam centralizados em branco sobre degradê azul escuro para roxo, com dois botões grandes em pílula empilhados, o primário em verde e o secundário em degradê roxo e magenta, a mesma paleta e estrutura da action sheet de watchOS (img 0051).
- Comparando as plataformas, a estrutura de título e descrição é idêntica em todas, e o que muda é o arranjo dos botões (lado a lado em iPhone e tvOS, empilhados em Mac, Vision Pro e Watch) e o material do fundo (opaco, semitransparente, vidro ou degradê) (img 0047 a img 0051).
- No vídeo do Freeform, o alerta não aparece direto: primeiro há um menu de contexto no item com "Recover" e "Delete" em vermelho (q001), a opção Delete fica destacada (q002, 1,5 s) e só então o menu some e surge o alerta com ícone do app, título de pergunta, texto, botão vermelho "Delete" e "Cancel" (q003, 2,0 s) (hig-vid_alerts__002, folha 0001).
- Nesse vídeo o alerta nunca coincide com o contorno da janela atrás dele: aparece deslocado para a direita e para cima em q003 e fica mais perto do centro da janela em q004 (2,5 s), com conteúdo idêntico, o que sugere que ele flutua à frente da janela em profundidade (hig-vid_alerts__002, folha 0001).
- No segundo vídeo, numa sala de estar, o alerta nasce como um painel pequeno e semitransparente no lugar do menu (q003) e se forma à frente da janela em q004 e q005; a partir de q005 a janela e o alerta ficam progressivamente mais transparentes e começam a se deslocar juntos para a esquerda, quadro a quadro, até q009 (hig-vid_alerts__003, folha 0001).
- De q010 a q015 o conjunto segue para a esquerda da sala e de q016 a q018 volta para a direita, sempre com a mesma transparência elevada e a mesma distância relativa entre alerta e janela; em q019 (12,0 s) o conjunto está de volta perto da posição inicial, com o alerta ainda preso à janela (hig-vid_alerts__003, folhas 0002 e 0003).
Divergências registradas: no hig-vid_alerts__002, os quadros acrescentam à descrição oficial a etapa do menu de contexto antes do alerta e a variação de posição do alerta entre q003 e q004; no hig-vid_alerts__003, acrescentam que o movimento da janela vai para a esquerda e depois retorna para a direita, e não segue uma única direção.
<!-- /visual:alerts -->

## Page controls (slug: page-controls)

O que governa: um page control exibe uma fileira de imagens indicadoras, cada uma representando uma página numa lista plana, ajudando a navegar até a página desejada.

Por que: o raciocínio da Apple é que o page control serve para relações sequenciais e ordenadas, não hierárquicas, e que sua legibilidade depende de manter os indicadores simples e em pequeno número, porque pontos são contados de relance, não lidos como texto. A customização de imagem só se justifica quando reforça o significado geral do controle; caso contrário, vira ruído visual que exige memorização.

Faça e evite:
- Use page controls para representar movimento entre uma lista ordenada de páginas; não representam relações hierárquicas ou não sequenciais. Para navegação mais complexa, considere sidebar ou split view.
- Centralize um page control na parte inferior da view ou janela.
- Embora o page control possa lidar com qualquer número de páginas, evite exibir muitas: mais de cerca de 10 pontos são difíceis de contar de relance; acima disso, considere outro arranjo, como grade.
- Por padrão, o page control usa a imagem de ponto do sistema para todos os indicadores, mas pode exibir imagem única para identificar uma página específica.
- Garanta que imagens customizadas de indicador sejam simples e claras; evite formas complexas, espaço negativo, texto ou linhas internas, que tornam o ícone confuso em tamanhos muito pequenos.
- Customize a imagem padrão do indicador só quando isso reforçar o significado geral do controle.
- Evite usar mais de dois tipos diferentes de imagens de indicador num mesmo page control; usar várias imagens únicas exige que a pessoa memorize o significado de cada uma e deixa o controle com aparência bagunçada.
- Evite colorir imagens de indicador; cores customizadas reduzem o contraste que diferencia o indicador da página atual; deixe o sistema colorir automaticamente.
- Em iOS/iPadOS, o controle pode encolher indicadores em ambos os lados para sugerir que há mais páginas disponíveis quando não cabem todos no espaço.
- Evite animar transições de página durante o "scrubbing" (arrastar); use a transição animada de rolagem só para o toque (tap), porque o scrubbing pode ser muito rápido e a animação constante causa lag e flashes visuais.
- O page control pode incluir um fundo translúcido em retângulo arredondado com três estilos: Automatic (mostra o fundo só durante interação, use quando o page control não é o elemento navegacional primário), Prominent (sempre mostra o fundo, use só quando o controle é o principal elemento navegacional da tela), Minimal (nunca mostra o fundo, use quando só quer indicar a posição da página atual sem feedback visual de scrubbing).
- Evite suportar o scrubber ao usar o estilo de fundo minimal, pois ele não dá feedback visual durante o scrubbing.
- Em tvOS, use page controls em coleções de páginas em tela cheia; controles adicionais dificultam manter o foco ao mover entre páginas.
- Em visionOS, os page controls representam páginas disponíveis e indicam a atual, mas a pessoa não interage diretamente com eles.
- Em watchOS, use paginação vertical para separar múltiplas views em páginas distintas e com propósito claro, permitindo rolar pela Digital Crown; essa abordagem é mais eficaz que paginação horizontal ou muitos níveis de navegação hierárquica. Considere limitar o conteúdo de uma página individual à altura de uma única tela.

Especificações exatas: o único número explícito é o limite prático de cerca de 10 pontos antes de a contagem visual ficar difícil.

Diferenças por plataforma:
- Não suportado em macOS.
- iOS, iPadOS: indicadores adaptativos (encolhem, destacam a página atual), interação por toque e scrubbing, três estilos de fundo (Automatic, Prominent, Minimal).
- tvOS: uso em coleções de páginas em tela cheia.
- visionOS: indicadores não interativos.
- watchOS: paginação horizontal (embaixo da tela) ou vertical (ao lado da Digital Crown); indicador transita entre navegação de páginas e rolagem de conteúdo de uma página longa.

Ligações com outros artigos: Scroll views.

<!-- visual:page-controls -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações vistas, todos os códigos conferidos; a página não tem vídeo.
- O diagrama de abertura põe o page control na base de uma janela de cantos arredondados, com a página ativa em ponto preto sólido e as demais em vermelho mais claro; uma seta vertical dupla cobre quase toda a altura da janela e outra, curta, fica junto ao controle, sugerindo a cotagem da posição e da altura do componente em relação à janela (img 0827).
- Uso incorreto, marcado com X cinza: na barra do app de Tempo, a pílula central troca os pontos por uma sequência de ícones cinzas de condição climática diferentes entre si, entre um botão circular de mapa à esquerda e um de lista à direita (img 0828 com img 0829).
- Uso correto, marcado com check verde: a mesma barra, mas a pílula mostra só o ícone de localização no início seguido de pontos simples, com a página atual em preto e as demais em cinza claro, limitando o controle a dois tipos de indicador (img 0830 com img 0831).
- Nos dois exemplos do Tempo o page control vive dentro de uma pílula ladeada por botões circulares, e a diferença entre certo e errado está só no conteúdo da pílula (img 0828, img 0830).
- Em iOS e iPadOS, uma pílula cinza clara com nove pontos mostra a gradação de tamanho: os cinco centrais em tamanho padrão, o segundo e o penúltimo menores e o primeiro e o último menores ainda, com o ponto central preenchido em preto como página atual (img 0832).
- No watchOS vertical, uma coluna de pontos pequenos fica à direita da tela, na posição da Digital Crown, com o ponto atual em branco e os demais em cinza escuro (img 0833).
- No watchOS horizontal, cinco pontos ficam em fileira na parte inferior da tela, com o atual em branco e os demais em cinza escuro, mostrando que o mesmo padrão muda de eixo conforme a direção da paginação (img 0834).
- Em todas as variações o indicador atual se distingue por preenchimento sólido em contraste com os demais, preto sobre claro nas versões claras e branco sobre preto no watchOS (img 0827, img 0830, img 0832, img 0833, img 0834).
<!-- /visual:page-controls -->

## Panels (slug: panels)

O que governa: num app macOS, um panel tipicamente flutua acima de outras janelas abertas, fornecendo controles, opções ou informações suplementares relacionadas à janela ativa ou à seleção atual.

Por que: o panel existe para dar acesso rápido a controles importantes sem competir com a janela principal pela atenção; por isso tem aparência menos proeminente que os estados de janela do macOS. A distinção entre painel-inspector (atualiza conforme a seleção muda) e janela Info (mantém sempre o mesmo conteúdo) reflete o princípio de que o tipo de container deve corresponder ao comportamento esperado do conteúdo.

Faça e evite:
- Use um panel para dar acesso rápido a controles ou informações importantes relacionados ao conteúdo em que a pessoa está trabalhando.
- Considere usar panel para funcionalidade de inspector, que exibe detalhes do item selecionado e atualiza automaticamente quando o item muda; para conteúdo que não muda com a seleção (janela Info), use uma janela regular, não um panel. Dependendo do layout, considere também um pane de split view para inspector.
- Prefira controles de ajuste simples num panel; evite controles que exijam digitar texto ou selecionar itens, porque exigem múltiplas etapas; prefira sliders e steppers, que dão controle mais direto.
- Escreva um título breve que descreva o propósito do panel, usando um substantivo ou frase nominal com capitalização de título (exemplos: "Fonts", "Colors", "Inspector").
- Mostre e oculte panels apropriadamente: quando o app fica ativo, traga todos os panels abertos para frente, independentemente de qual janela estava ativa quando o panel abriu; quando o app fica inativo, oculte todos os seus panels.
- Evite incluir panels na lista de documentos do menu Window; é aceitável incluir comandos para mostrar/ocultar panels no menu Window, mas panels não são documentos nem janelas padrão.
- Em geral, evite deixar disponível o botão de minimizar de um panel, já que a pessoa normalmente não precisa minimizá-lo.
- Refira-se aos panels pelo título na interface e na documentação de ajuda, sem incluir o termo "panel" nos menus (por exemplo, "Show Fonts", "Show Colors", "Show Inspector"); na documentação, pode ser útil acrescentar "window" ao título quando isso ajudar na clareza.
- Um panel estilo HUD serve à mesma função de um panel padrão, mas tem aparência mais escura e translúcida; funciona bem em apps de conteúdo altamente visual ou imersivo, como edição de mídia.
- Prefira panels padrão em vez de HUD; a pessoa pode ficar distraída ou confusa com um HUD sem razão lógica para sua presença, e o HUD pode não combinar com a aparência atual configurada. Use HUD só em app orientado a mídia (filmes, fotos, slides), quando um panel padrão obscureceria conteúdo essencial, ou quando não precisar incluir controles (a maioria dos controles do sistema não combina com a aparência do HUD, exceto o disclosure triangle).
- Mantenha um único estilo de panel quando o app muda de modo; por exemplo, se usar HUD em modo tela cheia, prefira manter o estilo HUD ao sair do modo tela cheia.
- Use cor com moderação em HUDs; excesso de cor na aparência escura de um HUD distrai. Geralmente pequenas quantidades de cor de alto contraste bastam para destacar informação importante.
- Mantenha HUDs pequenos; não deixe um HUD obscurecer o conteúdo que ele ajusta nem competir com o conteúdo pela atenção.

Especificações exatas: nenhum número (pt, px, ms) é dado no texto.

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS. Todo o artigo é específico do macOS.

Ligações com outros artigos: Windows, Modality.

<!-- visual:panels -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido; a página não tem vídeo.
- O diagrama de abertura mostra o panel padrão como janela secundária compacta e escura, com barra de título e botão circular de fechar, flutuando sobre uma janela principal maior em degradê (img 0835).
- O panel aparece deslocado para a esquerda e para baixo em relação ao centro da janela de fundo, cobrindo só parte do conteúdo principal e não o todo (img 0835).
- Setas de medida cotam o panel como especificação: uma horizontal dupla abaixo para a largura e uma vertical dupla à direita para a altura (img 0835).
- O estilo HUD é mostrado com captura real do macOS: um panel "Inspector" escuro e translúcido, com botão de fechar vermelho no canto superior esquerdo, pelo qual se vê o papel de parede colorido atrás (img 0836).
- O conteúdo do HUD se organiza em pares de rótulo e valor alinhados um contra o outro, com nome do arquivo e data no topo e depois seções com disclosure triangle: "General" aberta, com origem, resolução, tamanho e taxa de dados, formato e demais campos, e "Video Details" ainda recolhida, o que forma um inspector denso e hierárquico (img 0836).
Divergências registradas: as notas registram que a img 0836 acrescenta à descrição oficial detalhes como o caminho completo do arquivo, a resolução em pixels e a existência da segunda seção recolhível "Video Details", que a descrição não menciona.
<!-- /visual:panels -->

## Popovers (slug: popovers)

O que governa: um popover é uma view transitória que aparece acima de outro conteúdo quando a pessoa clica ou toca um controle ou área interativa.

Por que: o popover existe para expor uma pequena quantidade de informação ou funcionalidade sem consumir o espaço permanente de uma sidebar ou panel; por ser efêmero, a Apple limita seu escopo a poucas tarefas relacionadas e trata seu fechamento automático como comportamento esperado, reservando confirmação explícita (Cancel/Done) só para quando há risco real de perda de trabalho.

Faça e evite:
- Use um popover para expor uma pequena quantidade de informação ou funcionalidade, limitando-o a poucas tarefas relacionadas, já que ele desaparece após a interação.
- Considere usar popovers quando quiser mais espaço para conteúdo, evitando o custo de espaço de sidebars e panels, para conteúdo temporário.
- Posicione popovers apropriadamente: a seta deve apontar o mais diretamente possível para o elemento que o revelou; idealmente o popover não cobre esse elemento nem conteúdo essencial.
- Use um botão Close (incluindo Cancel ou Done) só para confirmação e orientação, quando trouxer clareza (como sair salvando ou não); caso contrário, o popover fecha normalmente ao clicar/tocar fora dele ou selecionar um item nele. Se houver múltiplas seleções possíveis, mantenha o popover aberto até que a pessoa o dispense explicitamente ou clique/toque fora dele.
- Sempre salve o trabalho ao fechar automaticamente um popover não modal, já que a pessoa pode dispensá-lo sem querer clicando fora; descarte o trabalho só quando a pessoa clicar um botão Cancel explícito.
- Mostre apenas um popover por vez; múltiplos popovers poluem a interface e causam confusão. Nunca mostre uma cascata ou hierarquia de popovers, um emergindo do outro; se precisar mostrar um novo, feche o aberto primeiro.
- Não mostre outra view sobre um popover; nada deve aparecer sobre ele, exceto um alerta.
- Quando possível, permita fechar um popover e abrir outro com um único clique ou toque, especialmente quando vários botões de barra abrem popovers diferentes.
- Evite deixar um popover grande demais; faça-o apenas grande o suficiente para exibir seu conteúdo e apontar para o local de origem; o sistema pode ajustar o tamanho para garantir bom encaixe.
- Ofereça transição suave ao mudar o tamanho de um popover, animando a mudança para não dar a impressão de que um novo popover substituiu o antigo.
- Evite usar a palavra "popover" na documentação de ajuda; refira-se à tarefa ou seleção específica.
- Evite usar um popover para mostrar um aviso, já que a pessoa pode perdê-lo ou fechá-lo sem querer; use um Alert.
- Em iOS/iPadOS, evite exibir popovers em views compactas; reserve popovers para views largas, e para views compactas use todo o espaço disponível com uma view modal em tela cheia como um sheet.
- Em macOS, é possível tornar um popover destacável (detachable), o que o transforma num panel separado ao ser arrastado, permanecendo visível enquanto a pessoa interage com outro conteúdo. Considere permitir que a pessoa destaque um popover; faça mudanças mínimas de aparência no popover destacado para manter o contexto.

Especificações exatas: nenhum número (pt, px, ms) é dado no texto.

Diferenças por plataforma:
- Sem considerações adicionais para visionOS.
- Não suportado em tvOS ou watchOS.
- iOS, iPadOS: evitar popovers em views compactas, reservar para views largas.
- macOS: suporte a popover destacável, virando panel.

Ligações com outros artigos: Sheets, Action sheets, Alerts, Modality.

<!-- visual:popovers -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações vista, código conferido; a página não tem vídeo.
- O diagrama de abertura define a forma canônica do popover sem conteúdo interno: um retângulo branco translúcido de cantos bem arredondados com um pequeno triângulo no topo apontando para a origem, e setas de medida marcando largura total na base e altura total à direita (img 0886).
- No Calendar do macOS, o popover anexado sai do bloco compacto do evento por uma pequena ponta e fica ao lado dele, sem cobri-lo, maior que o bloco de origem (img 0887).
- O popover anexado não tem barra de título nem botão de fechar; o conteúdo segue uma hierarquia de nome do evento em destaque, data e horário completos, recorrência com ícone, um botão de ação e a lista de convidados com checks verdes (img 0887).
- O popover destacado vira painel independente: perde a ponta que o ligava ao evento, ganha barra de título com X de fechar à esquerda e o título "Info" centralizado, e fica mais afastado do bloco de origem (img 0888).
- Entre os dois estados o conteúdo interno permanece idêntico; a única adição no destacado é um botão "Show" na base do painel (img 0887, img 0888).
<!-- /visual:popovers -->

## Scroll views (slug: scroll-views)

O que governa: um scroll view permite visualizar conteúdo maior que os limites da view, movendo o conteúdo vertical ou horizontalmente.

Por que: a Apple trata a rolagem como comportamento sistêmico esperado em todas as plataformas, por isso a orientação central é suportar os gestos e atalhos padrão em vez de recriar comportamentos customizados. O scroll edge effect existe para separar visualmente elementos flutuantes (como toolbars) do conteúdo que rola por trás, e não é decorativo: ele existe para manter controles distinguíveis, não para escurecer ou bloquear. O Look to Scroll reflete o mesmo princípio de dar escolha à pessoa (gesto ou olhar) sem substituir o comportamento padrão.

Faça e evite:
- Suporte os gestos de rolagem padrão e atalhos de teclado; se construir rolagem customizada, garanta que os indicadores usem o comportamento elástico esperado.
- Torne aparente quando o conteúdo é rolável, por exemplo exibindo conteúdo parcial na borda da view para indicar que há mais naquela direção.
- Evite colocar um scroll view dentro de outro com a mesma orientação, pois isso cria interface imprevisível e difícil de controlar; é aceitável colocar um scroll view horizontal dentro de um vertical (ou vice-versa).
- Considere suportar rolagem página a página quando fizer sentido para o conteúdo, definindo o tamanho da página (tipicamente a altura ou largura atual da view) e, se quiser, uma unidade de sobreposição para manter contexto.
- Em certos casos, role automaticamente para ajudar a pessoa a encontrar seu lugar: quando uma operação seleciona conteúdo ou posiciona o cursor numa área oculta; quando a pessoa começa a digitar num local não visível; quando o ponteiro passa da borda da view durante uma seleção; quando a pessoa seleciona algo e rola para um novo local antes de agir sobre a seleção. Em todos os casos, role automaticamente só o necessário para manter o contexto.
- Se suportar zoom, defina valores máximo e mínimo de escala apropriados.
- Scroll edge effect: use o estilo automático por padrão, que fornece separação visual mais opaca para toolbars superiores com muitos controles, texto fora de controles Liquid Glass e cabeçalhos de tabela fixados; se usar o estilo soft, teste bem a legibilidade em vários contextos.
- Use scroll edge effect só quando um scroll view estiver atrás de elementos de interface flutuantes; não é decorativo, não bloqueia nem escurece como um overlay, existe para manter controles visualmente distintos.
- Aplique um scroll edge effect por view; em layouts de split view no iPad e Mac, cada painel pode ter seu próprio efeito, mantendo altura consistente entre eles para alinhamento.
- Em iOS/iPadOS, considere mostrar um page control quando o scroll view estiver em modo página a página; se mostrar page control junto com scroll view, não mostre o indicador de rolagem no mesmo eixo, para evitar controles redundantes.
- Em macOS, um indicador de rolagem é comumente chamado de scroll bar; se necessário, use scroll bars pequenas ou mini num panel, mantendo o mesmo tamanho para todos os controles daquele panel.
- Em tvOS, views podem rolar mas não são tratadas como objetos distintos com indicadores de rolagem; quando o conteúdo excede a tela, o sistema rola automaticamente a interface para manter os itens focados visíveis.
- Em visionOS, o indicador de rolagem tem tamanho pequeno e fixo, aparecendo em local previsível (centralizado verticalmente na borda trailing durante rolagem vertical; centralizado horizontalmente na borda inferior da janela durante rolagem horizontal). Ao olhar para o indicador e iniciar um gesto de arrastar, ele habilita uma experiência de jog bar que permite manipular a velocidade da rolagem, revelando marcas que aceleram ou desaceleram conforme pequenos ajustes no gesto. Considere aumentar margens se o conteúdo usar margens apertadas, para não sobrepor o indicador.
- Look to Scroll (visionOS): permite rolar só com os olhos, começando quando a pessoa olha perto da borda do scroll view (topo/base para vertical, laterais para horizontal); funciona junto com o comportamento existente, então a pessoa escolhe gesto ou olhar. Suporte Look to Scroll para views de leitura ou navegação; evite usá-lo para conteúdo secundário com controles ou informação densa que exija rolagem precisa e rápida. Mantenha consistência entre views semelhantes. Defina áreas de rolagem claras, preferindo que a view ocupe toda a largura ou altura da janela; se a view for recuada da janela, forneça limites claros. Remova efeitos ou animações customizadas de rolagem (como parallax) antes de suportar Look to Scroll, pois podem causar comportamento inesperado.
- Em watchOS, prefira conteúdo com rolagem vertical, já que a pessoa está acostumada a usar a Digital Crown para navegar; se o app tiver uma única lista ou view de conteúdo, girar a Digital Crown rola verticalmente quando o conteúdo é mais alto que a tela. Use tab views para rolagem página a página; se colocadas em pilha vertical, a pessoa pode girar a Digital Crown para se mover verticalmente por páginas em tela cheia, com indicador de página ao lado da Digital Crown. Ao exibir conteúdo paginado, considere limitar o conteúdo de uma página individual à altura de uma tela; para páginas longas, a Digital Crown pode tanto navegar entre páginas curtas quanto rolar conteúdo de uma página mais longa, porque o indicador de página se expande em indicador de rolagem quando necessário.

Especificações exatas: nenhum número (pt, px, ms) é dado explicitamente no texto para dimensões ou durações.

Diferenças por plataforma:
- iOS, iPadOS: page control combinado com scroll view, evitando indicador redundante no mesmo eixo; scroll edge effects.
- macOS: scroll bar como termo; scroll bars pequenas/mini em panels; scroll edge effects.
- tvOS: rolagem automática do sistema para manter itens focados visíveis, sem indicadores distintos.
- visionOS: indicador de rolagem pequeno e de posição fixa; jog bar ao olhar e arrastar; Look to Scroll.
- watchOS: rolagem vertical via Digital Crown; tab views para paginação; indicador de página que se expande em indicador de rolagem.

Ligações com outros artigos: Page controls, Gestures, Pointing devices.

<!-- visual:scroll-views -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações e 2 de 2 folhas do vídeo hig-vid_scroll-views__041 vistas, todos os códigos conferidos.
- A abertura é decorativa: uma moldura arredondada de imagem com sol e montanhas, tingida de vermelho alaranjado, com uma barra de rolagem vertical fina e escura no canto superior direito (img 0980).
- O efeito de borda hard aparece num app de iPhone com barra superior translúcida (voltar, "Title" e adicionar) sobre foto de palmeira: o desfoque atrás da barra é mais opaco, com o topo escuro e nítido, e termina numa borda bem definida logo abaixo da barra (img 0981).
- O efeito soft usa exatamente a mesma tela e muda só o tratamento atrás da barra: a área fica bem mais clara, sem fundo opaco definido, e o desfoque se dissolve aos poucos no conteúdo sem linha de corte, deixando título e botões quase flutuando sobre a foto (img 0982).
- O par reaproveita a mesma tela, foto e controles e muda só o tratamento do desfoque, permitindo comparar lado a lado os dois estilos de borda no mesmo layout (img 0981, img 0982).
- No vídeo, uma nota do Notes flutua numa sala 3D no visionOS; de q001 a q003 fica parada no topo do documento e a partir de q004 o conteúdo sobe, com título, parágrafo e desenhos saindo pelo topo em sequência (q005, q006) e um novo desenho entrando pela base em q007 (folha 0001).
- A rolagem passa do fim do conteúdo: em q008 e q009, e ainda em q010 e q011, a prancheta mostra só área em branco; em q012 um bloco de texto entra cortado pela borda superior, em q013 e q014 aparecem desenhos de folha, e em q015 o topo do documento volta, até q016 e q017 ficarem praticamente idênticos a q001 a q003 (folhas 0001 e 0002).
- Uma marca vertical fina e translúcida junto à borda direita da prancheta, compatível com indicador de rolagem, aparece em quase todos os quadros com conteúdo da primeira folha, em todos os quadros com conteúdo da segunda e também nos quadros em branco q008 e q009; nos quadros parados não dá para confirmar marcas distintas dentro dela nem medir mudança de comprimento ou de posição do traço (folha 0001 q001 a q009, folha 0002 q012 a q017).
Divergências registradas: o trecho em que a rolagem passa por uma área em branco e retorna ao topo (q008 a q011) não é mencionado na descrição oficial, que fala só do indicador reagindo à velocidade da rolagem.
<!-- /visual:scroll-views -->

## Sheets (slug: sheets)

O que governa: um sheet ajuda a pessoa a realizar uma tarefa delimitada e fortemente relacionada ao contexto atual, como fornecer informação específica ou completar uma tarefa simples antes de voltar à view pai.

Por que: a distinção central do artigo é entre sheet modal e não modal: em macOS, tvOS, visionOS e watchOS o sheet é sempre modal, prevenindo interação com a view pai até ser dispensado; em iOS e iPadOS pode ser não modal, afetando a view pai sem se fechar. Essa flexibilidade em iOS/iPadOS existe porque, nessas plataformas, o sheet pode funcionar como ferramenta de edição contínua (como o sheet de formatação de texto no Notes) em vez de apenas coletar uma entrada pontual. A regra sobre nunca empilhar sheets reflete o princípio geral da Apple de que a pessoa deve sempre saber voltar de onde veio.

Faça e evite:
- Para fluxos complexos ou prolongados, considere alternativas ao sheet: em iOS/iPadOS, uma view modal em tela cheia (para vídeos, fotos, câmera ou tarefas multietapas); em macOS, considere abrir uma nova janela ou modo tela cheia; em visionOS, considere transicionar para um Full Space.
- Exiba apenas um sheet por vez a partir da interface principal; se fechar um sheet deveria voltar a outro sheet, a pessoa pode se perder; se algo dentro de um sheet resultar em outro sheet, feche o primeiro antes de mostrar o novo, reabrindo-o depois se necessário.
- Use uma view não modal quando quiser apresentar itens suplementares que afetam a tarefa principal na view pai; considere split view (visionOS) ou panel (macOS); em iOS/iPadOS, use um sheet não modal para esse fluxo.
- Ofereça uma alternativa ao botão Done: se fornecer Done, sempre combine com Cancel (para dispensar sem confirmar/salvar) ou Back (para voltar a uma etapa anterior); depender só do Done implica que completar a tarefa é a única saída, o que pode parecer restritivo ou enganoso.
- Evite mostrar os três botões juntos, Cancel, Done e Back.
- Botões comuns: Cancel (ou Close) dispensa o sheet sem salvar alterações; Done dispensa após completar a tarefa ou salvar explicitamente; Back navega a uma etapa anterior num fluxo multietapas ou a uma view pai numa hierarquia, sem dispensar o sheet.
- Em iOS/iPadOS, para sheets de view única, o Cancel fica na borda leading da toolbar superior; quando presente, o Done fica na borda trailing. Em fluxos multietapas, a posição dos botões pode variar entre as etapas.
- Sheets redimensionáveis expandem quando a pessoa rola o conteúdo ou arrasta o grabber (indicador horizontal pequeno no topo do sheet); redimensionam conforme detents, alturas nas quais o sheet naturalmente repousa. Detents definidos pelo sistema: large (altura totalmente expandida) e medium (cerca de metade da altura totalmente expandida). Sheets podem ter um ou mais valores de detent customizados.
- Sheets suportam automaticamente o detent large; adicionar o detent medium permite repousar em ambas as alturas, enquanto especificar só medium impede a expansão até altura total.
- Em app para iPhone, considere suportar o detent medium para permitir divulgação progressiva do conteúdo; considere não suportá-lo quando o conteúdo só faz sentido em altura total.
- Inclua um grabber num sheet redimensionável: mostra que dá para arrastar para redimensionar, e a pessoa também pode tocar para percorrer os detents; funciona com VoiceOver para redimensionar sem ver a tela.
- Suporte deslizar (swipe) para dispensar um sheet; a pessoa espera esse gesto em vez de tocar um botão de dispensa; se houver alterações não salvas, use um action sheet para confirmar.
- Em app iPadOS, prefira os estilos de apresentação page ou form sheet, que usam um tamanho padrão, centralizando o conteúdo sobre um fundo escurecido.
- Em macOS, o sheet é uma view em formato de cartão com cantos arredondados que flutua sobre a janela pai; a janela pai fica escurecida enquanto o sheet está na tela, sinalizando que não pode ser usada até ele ser dispensado; porém a pessoa espera poder interagir com outras janelas do app antes de dispensar o sheet.
- Apresente o sheet em um tamanho padrão razoável em macOS, já que a pessoa geralmente não espera redimensioná-lo, embora em alguns casos seja bom suportar redimensionamento.
- Permita interagir com outras janelas do app sem antes dispensar o sheet em macOS: ao abrir o sheet, a janela pai (e seus panels de documento modeless, se aplicável) vêm para frente; garanta que outras janelas do app também possam vir para frente mesmo com o sheet aberto.
- Use um panel em vez de sheet em macOS quando a pessoa precisar fornecer entrada repetidamente e observar resultados, como um panel de localizar e substituir.
- Em visionOS, o sheet flutua na frente da janela pai, escurecendo-a e se tornando o alvo da interação. Evite exibir um sheet que emerge da borda inferior da janela; prefira centralizá-lo no campo de visão. Apresente-o num tamanho padrão que ajude a manter o contexto, evitando cobrir a maior parte ou toda a janela, mas considere permitir redimensionamento.
- Em watchOS, o sheet é uma view em tela cheia que desliza sobre o conteúdo atual do app, semitransparente para ajudar a manter o contexto, com material que borra e dessatura o conteúdo coberto. Use um sheet só quando a tarefa modal exigir título customizado ou apresentação de conteúdo customizada; se precisar dar informação importante ou apresentar escolhas, considere Alert ou Action sheet. Mantenha as interações de sheet breves e ocasionais, usando-o só como interrupção temporária para uma tarefa importante; evite usá-lo para navegar pelo conteúdo do app. Se mudar o rótulo padrão, prefira SF Symbols para representar a ação, evitando rótulo que sugira navegação hierárquica ou que pareça título de página/app, pois a pessoa não saberia como dispensar o sheet.

Especificações exatas: os únicos valores dados são qualitativos (large = altura totalmente expandida; medium = cerca de metade da altura totalmente expandida); nenhum número em pt, px ou ms é fornecido no texto.

Diferenças por plataforma:
- Sem considerações adicionais para tvOS.
- iOS, iPadOS: modal ou não modal; botões Cancel/Done/Back posicionados na toolbar; detents (large, medium); grabber; swipe para dispensar; estilos page/form sheet no iPadOS.
- macOS: sempre modal; formato de cartão com cantos arredondados; janela pai escurecida mas outras janelas do app continuam acessíveis; tamanho padrão razoável, redimensionável quando fizer sentido; preferir panel para entrada repetida com observação de resultado.
- visionOS: sempre modal; flutua na frente da janela, escurecendo-a; evitar emergir da borda inferior, preferir centralizar; tamanho padrão que preserva contexto.
- watchOS: sempre modal; view em tela cheia semitransparente com material de blur/dessaturação; uso restrito a tarefas que exigem título ou apresentação customizados; rótulo preferencialmente em SF Symbols.

Ligações com outros artigos: Modality, Action sheets, Popovers, Panels.

<!-- visual:sheets -->
### O que as ilustrações mostram
Base: 5 de 5 folhas de ilustrações e 1 de 1 folha do vídeo hig-vid_sheets__053 (quadros q001 a q004) vistas, todos os códigos conferidos.
- O esboço de abertura mostra uma janela de desktop com três círculos no topo esquerdo e uma sheet mais clara descendo a partir do topo da janela, com setas de duas pontas nas quatro direções ao redor dela, que as notas leem como medida ou possibilidade de redimensionamento (img 1029).
- No Notes do iPhone, a sheet não modal "Format" ocupa a metade inferior sobre a nota, que continua visível acima; a sheet traz uma fileira de abas de estilo de texto, com a ativa em laranja, e duas fileiras de ícones de formatação, lista, recuo e alinhamento (img 1030).
- Com outro trecho selecionado, a mesma sheet aberta passa a destacar o botão de itálico em laranja, ou seja, o estado dos controles acompanha a seleção na view pai sem que a sheet se feche (img 1031).
- Uso incorreto, marcado com X cinza: topo de sheet com grabber, título centralizado e só um botão azul de confirmação à direita, sem saída alternativa (img 1032 com img 1033).
- Uso correto, marcado com check verde: X cinza de cancelar à esquerda, título ao centro e botão azul de confirmação à direita (img 1034 com img 1035).
- Padrão a evitar: seta de voltar à esquerda e, agrupados à direita, o X de cancelar e o check de confirmar, reunindo os três botões ao mesmo tempo (img 1036).
- O fluxo em várias etapas repete a mesma composição e muda só dois elementos: primeiro X à esquerda com check cinza inativo, depois seta de voltar no lugar do X com check ainda inativo, e por fim voltar com o check em azul ativo, uma máquina de estados de botões ensinada por comparação e não por anotação (img 1037, img 1038, img 1039).
- No detent grande, o recorte mostra grabber e X cinza logo abaixo da barra de status e o restante da tela em branco, com a sheet ocupando quase toda a área visível (img 1040); no detent médio, a metade superior mostra a view de trás em cinza e a metade inferior é um retângulo branco de cantos arredondados com X circular no canto superior esquerdo (img 1041).
- No macOS, a sheet é um cartão de cantos arredondados centralizado sobre a janela do Notes escurecida, com título, lista de três novidades cada uma com ícone e botão "Continue" em amarelo no canto inferior direito do cartão (img 1042).
- No watchOS, a sheet é tela cheia sobre degradê azul para magenta, com X circular translúcido no canto superior esquerdo, hora no direito e um botão grande em pílula para a ação primária na base (img 1043); a variação troca o X por seta de voltar (img 1044), e o contraste entre um rótulo de texto "Title" em pílula no canto superior esquerdo e o X padrão ilustra o rótulo que pode parecer navegação hierárquica (img 1045, img 1046).
- No vídeo do visionOS, q001 mostra só a janela translúcida e desfocada sobre uma sala 3D; em q002 surge no centro um retângulo cinza de cantos arredondados, mais opaco e definido que o fundo, que cresce em q003 e mais ainda em q004, sempre centralizado e sem conteúdo interno, com a janela pai desfocada durante toda a abertura (0,0 s a 2,0 s).
- A abertura no visionOS aparece como crescimento de escala a partir do centro, e não como subida a partir da borda inferior, e a sala atrás fica menos nítida depois que a sheet aparece do que em q001 (hig-vid_sheets__053).
Divergências registradas: a img 1029 acrescenta setas de medida ou redimensionamento que a descrição oficial não detalha; no vídeo, a descrição oficial fala de uma janela em branco, mas o fundo é uma sala de estar desfocada com móveis reconhecíveis.
<!-- /visual:sheets -->

## Windows (slug: windows)

O que governa: uma janela apresenta as views e componentes de UI de um app ou jogo; em iPadOS, macOS e visionOS, janelas definem os limites visuais do conteúdo do app, separam-no de outras áreas do sistema e habilitam fluxos de multitarefa dentro e entre apps.

Por que: a Apple distingue janela primária (navegação e conteúdo principal, com ações associadas) de janela auxiliar (tarefa ou área específica, dedicada a uma experiência, sem navegação para outras áreas do app, tipicamente com botão de fechar). Essa distinção orienta quando abrir uma nova janela: fazer isso ajuda a multitarefa e a preservar contexto, mas abrir novas janelas em excesso cria confusão e dificulta a navegação. A rejeição a UI de janela customizada segue o mesmo princípio de outros componentes: janelas fornecidas pelo sistema já são reconhecidas pela pessoa, e replicar a aparência sem perfeição faz o app parecer quebrado.

Faça e evite:
- Garanta que as janelas se adaptem fluidamente a diferentes tamanhos para suportar fluxos de multitarefa e múltiplas janelas.
- Escolha o momento certo para abrir uma nova janela: abrir conteúdo numa janela separada ajuda a multitarefa ou a preservar contexto (exemplo: Mail abre nova janela ao compor, mantendo a nova mensagem e o e-mail existente visíveis ao mesmo tempo); evite abrir novas janelas como comportamento padrão, a menos que faça sentido para o app.
- Considere oferecer a opção de ver conteúdo numa nova janela, por exemplo via comando em menu de contexto ou no menu File.
- Evite criar UI de janela customizada; janelas do sistema têm aparência e comportamento reconhecíveis; não crie frames ou controles customizados, e não tente replicar a aparência do sistema, pois isso sem correspondência perfeita faz o app parecer quebrado.
- Use o termo "window" em conteúdo voltado à pessoa; o sistema se refere a janelas de app como "windows" independentemente do tipo; usar outros termos, incluindo "scene" (que se refere à implementação), tende a confundir.
- Em iPadOS, janelas se apresentam de duas formas, dependendo da escolha em Multitasking & Gestures: tela cheia (o app preenche toda a tela, e a pessoa alterna entre apps ou janelas do mesmo app pelo app switcher) ou em janela (redimensionável livremente, múltiplas janelas simultâneas, reposicionáveis e trazíveis para frente; o sistema lembra tamanho e posição mesmo com o app fechado).
- Em iPadOS, garanta que os controles de janela não sobreponham itens da toolbar; quando em modo janela, os controles de janela aparecem na borda leading da toolbar; se o app tiver botões nessa borda, mova-os para dentro quando os controles de janela aparecerem.
- Em iPadOS, considere permitir gesto para abrir conteúdo em nova janela, como o gesto de pinça no Notes para expandir um item em nova janela.
- Em macOS, a pessoa geralmente roda vários apps ao mesmo tempo, vendo janelas de múltiplos apps numa mesma área de trabalho e alternando frequentemente entre elas.
- Anatomia de janela no macOS: consiste em um frame e uma área de corpo (body); a pessoa move a janela arrastando o frame e frequentemente redimensiona arrastando as bordas. O frame aparece acima da área de corpo e pode incluir controles de janela e uma toolbar; em casos raros, a janela pode exibir uma bottom bar, parte do frame que aparece abaixo do conteúdo do corpo.
- Estados de janela no macOS: Main (a janela frontal que a pessoa vê é a janela principal do app; só pode haver uma main window por app), Key (também chamada janela ativa, aceita a entrada da pessoa; só pode haver uma key window na tela por vez; embora a main window do app em primeiro plano costume ser a key window, outra janela, como um panel flutuante, pode ser a key), Inactive (uma janela que não está em primeiro plano).
- O sistema dá aparências diferentes para janelas main, key e inactive para ajudar a identificá-las visualmente: a key window usa cor nas opções da barra de título para fechar, minimizar e ampliar; janelas inactive e main que não são key usam cinza nessas opções. Janelas inactive também não usam Materials (efeito que puxa cor do conteúdo por trás da janela), o que as torna com aparência mais discreta e visualmente mais distantes.
- Algumas janelas, tipicamente panels como Colors ou Fonts, só se tornam key window quando a pessoa clica na barra de título ou num componente que requer entrada de teclado, como um campo de texto.
- Garanta que janelas customizadas usem as aparências definidas pelo sistema, já que a pessoa depende das diferenças visuais para identificar a janela em primeiro plano e saber qual receberá sua entrada; com componentes fornecidos pelo sistema, o fundo e a aparência dos botões da janela atualizam automaticamente ao mudar de estado; com implementações customizadas, esse trabalho precisa ser feito manualmente.
- Evite colocar informação ou ações críticas numa bottom bar, porque a pessoa costuma reposicionar a janela de forma que oculte sua borda inferior; se precisar usar uma, use-a só para pequena quantidade de informação diretamente relacionada ao conteúdo da janela ou a um item selecionado nela (exemplo: o Finder usa a status bar para mostrar número total de itens, itens selecionados e espaço disponível em disco); para mais informação, considere um inspector, tipicamente apresentado no lado trailing de uma split view.
- Em visionOS, o sistema define dois estilos principais de janela: default (chamado window) e volumétrico (chamado volume); ambos podem exibir conteúdo 2D e 3D, e a pessoa pode ver múltiplas janelas e volumes simultaneamente no Shared Space e em um Full Space.
- Existe também o estilo plain window em visionOS, similar ao default, exceto que o plano vertical não usa o fundo em glass.
- O sistema define a posição inicial da primeira janela ou volume que a pessoa abre no app ou jogo; tanto no Shared Space quanto num Full Space, a pessoa pode mover janelas e volumes para novos locais.
- Janela default em visionOS: consiste num plano vertical que usa um fundo Materials não modificável chamado glass e inclui botão de fechar, barra de janela e controles de redimensionamento; pode incluir também botão Share, tab bars, toolbars e um ou mais ornaments. Por padrão, visionOS usa escala dinâmica para ajudar o tamanho aparente da janela a permanecer consistente independentemente da proximidade de quem vê.
- Prefira usar uma janela para apresentar interface familiar e suportar tarefas familiares, reservando experiências mais imersivas para conteúdo e atividades significativas; se quiser mostrar conteúdo 3D delimitado como um tabuleiro de jogo, considere usar um volume.
- Mantenha o fundo em glass da janela: ajuda o conteúdo a parecer parte do ambiente, adaptando-se dinamicamente à iluminação, usando reflexos especulares e sombras para comunicar escala e posição; removê-lo tende a deixar elementos de UI e texto menos legíveis e a parecer menos relacionados entre si; um fundo opaco obscurece o ambiente e pode deixar a janela com aparência constritora e pesada.
- Escolha um tamanho inicial de janela que minimize áreas vazias; por padrão, uma janela mede 1280x720 pt. Quando uma janela abre pela primeira vez, o sistema a posiciona a cerca de dois metros na frente de quem veste o dispositivo, dando-lhe uma largura aparente de cerca de três metros. Espaço vazio demais dentro da janela pode fazê-la parecer desnecessariamente grande e obscurecer outro conteúdo no espaço da pessoa.
- Busque uma forma inicial que combine com o conteúdo da janela (exemplo: uma janela padrão do Keynote é larga porque slides são largos, enquanto uma janela padrão do Safari é alta porque páginas web costumam ser bem mais compridas que largas).
- Escolha um tamanho mínimo e máximo para cada janela, para manter o conteúdo com boa aparência em todos os tamanhos que a pessoa possa escolher ao redimensionar.
- Minimize a profundidade do conteúdo 3D exibido numa janela; o sistema adiciona realces e sombras às views e controles dentro da janela para dar aparência de profundidade; embora seja possível exibir conteúdo 3D numa janela, o sistema o recorta (clip) se ele se estender demais para fora da superfície da janela; para conteúdo com maior profundidade, use um volume.
- Volumes em visionOS: exibem conteúdo 2D ou 3D visualizável de qualquer ângulo; incluem controles de gerenciamento de janela como uma janela normal, mas o botão de fechar e a barra de janela de um volume mudam de posição para encarar quem vê conforme a pessoa se move ao redor.
- Prefira usar um volume para exibir conteúdo 3D rico; para apresentar interface familiar centrada em UI, geralmente é melhor usar uma janela.
- Posicione conteúdo 2D de forma que pareça bem de múltiplos ângulos dentro de um volume, já que a perspectiva da pessoa muda conforme ela se move; para fixar conteúdo 2D a áreas específicas de conteúdo 3D dentro de um volume, é possível usar um attachment.
- Em geral, use escala dinâmica em volumes, para ajudar o conteúdo a permanecer legível e fácil de interagir mesmo à distância; se quiser que o conteúdo represente um objeto real (como um produto num app de varejo), pode usar escala fixa (padrão).
- A aparência padrão de baseplate (o "piso" horizontal do volume) ajuda a pessoa a perceber as bordas do volume; a partir do visionOS 2, o sistema torna a baseplate visível automaticamente com um brilho suave ao redor da borda quando a pessoa olha para ela; se o conteúdo não preencher o volume, esse brilho ajuda a indicar as bordas, especialmente útil para manter o controle de redimensionamento fácil de encontrar; se o conteúdo for full bleed ou preencher os limites do volume, ou se um baseplate customizado for exibido, o brilho padrão pode não ser desejado.
- Considere oferecer conteúdo de alto valor num ornament; a partir do visionOS 2, um volume pode incluir um ornament além de toolbar e tab bar, útil para reduzir a poluição visual e elevar views ou controles importantes; ao usar uma âncora de anexação para especificar a posição do ornament (como `topBack` ou `bottomFront`), ele permanece na mesma posição relativa à perspectiva de quem vê conforme a pessoa se move ao redor do volume; evite posicionar um ornament na mesma borda de uma toolbar ou tab bar, e prefira criar apenas um ornament adicional para não ofuscar o conteúdo importante do volume.
- Escolha um alinhamento que suporte a forma como a pessoa interage com o volume; conforme ela o move, a baseplate pode permanecer paralela ao chão do ambiente, ou pode inclinar-se para corresponder ao ângulo em que a pessoa está olhando; em geral, um volume paralelo ao chão funciona bem para conteúdo com pouca interação, enquanto um volume que se inclina conforme o olhar mantém o conteúdo confortavelmente utilizável mesmo com a pessoa reclinada.

Especificações exatas:
- visionOS: tamanho padrão inicial de janela de 1280x720 pt; posicionada a cerca de dois metros na frente de quem vê; largura aparente de cerca de três metros.

Diferenças por plataforma: não suportado em iOS, tvOS ou watchOS.
- iPadOS: modo tela cheia (com app switcher) ou modo janela (redimensionável livremente, posição e tamanho lembrados pelo sistema); controles de janela na borda leading da toolbar; gesto de pinça para abrir em nova janela.
- macOS: anatomia de frame e body; frame com controles de janela, toolbar e, raramente, bottom bar; três estados de janela (Main, Key, Inactive), cada um com aparência distinta; uso de Materials para diferenciar estados; recomendação contra informação crítica em bottom bar.
- visionOS: dois estilos principais (window default com fundo glass, e volume) mais o estilo plain window; janela padrão de 1280x720 pt a dois metros de distância; escala dinâmica; volumes com baseplate, alinhamento ajustável, ornaments e escala dinâmica ou fixa.

Ligações com outros artigos: Layout, Split views, Multitasking (e, dentro do texto, referências a Spatial layout, Materials, Depth, Immersive experiences).

<!-- visual:windows -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações vistas, todos os códigos conferidos; a página não tem vídeo.
- A abertura reduz a janela a uma silhueta sem conteúdo: três botões redondos no canto superior esquerdo, bolhas translúcidas no lado direito da barra de título e setas de medida de duas pontas nas bordas direita e inferior para altura e largura, a única imagem da página que comunica redimensionamento por cota (img 1324).
- No iPadOS, o mesmo documento do Notes aparece em tela cheia sem moldura, sem Dock e sem Tela de Início (img 1325), e em modo janela como retângulo de cantos arredondados com sombra, centralizado sobre o papel de parede e com o Dock na base; os três elementos aparecem juntos ou somem juntos, e isso é o que distingue os dois modos (img 1326).
- No macOS, três janelas empilhadas em diagonal recebem rótulos que apontam cada estado: a inativa ao fundo, uma janela do Finder com os botões de janela sem cor; a janela chave, o painel Colors com roda de cores e os botões de janela coloridos; e a janela principal, a do Notes (img 1327).
- Nessa ilustração a janela chave é o painel de cores, e não a janela principal do app, e a diferenciação de estados se apoia em profundidade do empilhamento e rótulos de texto, não só em cor (img 1327).
- No visionOS, a ilustração abstrata distingue os dois estilos pela forma: a janela é um plano fino duplo e inclinado, em azul monocromático com contornos tracejados, e o volume é um cubo translúcido de faces tracejadas com a face inferior mais sólida, ambos sobre uma barra fina (img 1328, img 1329).
- Uma janela real do visionOS flutua sobre uma sala, com fundo de vidro que deixa o ambiente transparecer levemente; o conteúdo segue imagem no topo, título, subtítulo e três colunas de texto, cada uma com título e parágrafo curto (img 1330).
- Na janela com conteúdo 3D, outra tela do mesmo app traz título, texto explicativo à esquerda, um botão e opções na base, e um satélite 3D renderizado aparece fora do retângulo da janela, sobreposto à cena real (img 1331).
- O volume mostra um globo 3D sobre a mesa de centro, lado a lado com uma janela translúcida de texto e botão, e uma pequena barra de controles com quatro ícones logo abaixo do globo, o que põe janela e volume coexistindo no mesmo espaço (img 1332).
<!-- /visual:windows -->

## O que este grupo revela sobre o jeito Apple

1. A escolha entre alerta, action sheet, sheet e popover depende sistematicamente de quem iniciou o evento e de quanta atenção ele merece: alerta para o inesperado ou crítico (alerts), action sheet para uma escolha decorrente de ação intencional (action-sheets), sheet para uma tarefa delimitada dentro do contexto atual (sheets), popover para informação pequena e transitória (popovers). A mesma lógica de "não interromper sem necessidade" aparece nos quatro.
2. A Apple trata interrupção como um custo explícito e recorrente em toda a documentação de apresentação: "use com moderação" aparece quase literalmente em alerts, action-sheets e sheets, sempre justificado pelo mesmo argumento de que o componente tira a pessoa da tarefa atual.
3. Empilhamento é tratado como falha de orientação em vários componentes: nunca uma cascata de popovers (popovers), nunca mostrar mais de um sheet ao mesmo tempo a partir da interface principal (sheets), nunca mostrar outra view sobre um popover exceto um alerta (popovers). O padrão sistemático é manter a pessoa sempre com um caminho de volta óbvio.
4. Vários componentes reaproveitam a mesma lógica de botão: Cancel sempre no lado ou posição menos proeminente e nunca como botão padrão quando há ação destrutiva (alerts), sempre pareado com Done ou Back para não parecer a única saída (sheets), presente por padrão em confirmation dialogs (action-sheets).
5. O estilo destrutivo de botão segue uma regra consistente e sutil entre alerts e action-sheets: ele marca uma ação que a pessoa não escolheu deliberadamente, mas é retirado quando a pessoa já demonstrou intenção explícita (como escolher "Empty Trash"), porque nesse caso o botão só cumpre a intenção original.
6. A Apple valoriza terminologia estável voltada à pessoa: usar sempre "window" em vez de "scene" (windows), evitar a palavra "popover" na documentação de ajuda (popovers), referir-se a panels pelo título sem a palavra "panel" nos menus (panels). Em todos os casos, o termo técnico de implementação é escondido do vocabulário voltado ao usuário final.
7. Há uma hierarquia implícita de "peso" de apresentação: popover e page control para pequenas doses de informação temporária; sheet para tarefa delimitada; panel para controles persistentes específicos de macOS; janela para o container mais completo e estruturado. Cada nível seguinte assume mais espaço de tela e mais permanência.
8. A adaptação por plataforma segue um padrão de "convergência com particularidade": quase todos os componentes existem em iOS/iPadOS/macOS com pequenas variações, mas cada plataforma introduz uma mecânica de interação própria e coerente com seu paradigma dominante: watchOS usa a Digital Crown e limita conteúdo à altura da tela (page-controls, scroll-views, sheets); visionOS introduz profundidade, glass, ornaments e volumes (windows); tvOS elimina indicadores distintos em favor de foco automático (scroll-views).
9. Elementos puramente decorativos são explicitamente rejeitados em favor de elementos funcionais: o scroll edge effect "não é decorativo" (scroll-views); cor em HUDs deve ser usada "com moderação" e só para destacar informação (panels); indicadores de page control não devem ser coloridos, para não reduzir contraste funcional (page-controls).
10. A Apple é consistente ao proibir a recriação de UI do sistema: não crie UI de janela customizada (windows), garanta que janelas customizadas usem aparências definidas pelo sistema (windows), deixe o sistema colorir automaticamente os indicadores do page control (page-controls). A justificativa repetida é que replicar sem perfeição faz o app parecer quebrado ou confunde a leitura visual do sistema.
11. Vários artigos remetem a "Modality" como conceito guarda-chuva (action-sheets, alerts, panels, popovers, sheets), confirmando que a Apple organiza toda essa família de componentes de apresentação em torno de um princípio central único de modalidade, do qual cada componente é uma variação de escopo e peso.
12. Mudanças de guidance ao longo do tempo (registradas nos change logs de alerts, scroll-views, sheets e windows) mostram evolução recente e ativa: guidance de scroll edge effect (2025/2026), Look to Scroll em visionOS (2026), guidance de botões em sheets (2026) e janelas redimensionáveis em iPadOS (2025), indicando que a Apple continua ajustando esses componentes de apresentação junto com mudanças mais amplas de design do sistema, como Liquid Glass.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/action-sheets.md, 45 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/alerts.md, 81 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/page-controls.md, 68 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/panels.md, 43 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/popovers.md, 46 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/scroll-views.md, 82 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sheets.md, 96 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/windows.md, 100 linhas lidas, sim, até o fim.

Nenhum arquivo do grupo é apenas índice de coleção; todos os oito têm texto próprio completo.
