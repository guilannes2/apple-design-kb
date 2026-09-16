# Patterns (parte 2)

## Settings (slug: settings)

### O que governa
Quando e como oferecer opções de personalização, seja no app de Settings do sistema, numa área de configurações própria do app ou dentro da própria tela de tarefa.

### Por que
A Apple parte do princípio de que as pessoas querem que apps e jogos "simplesmente funcionem", mas valorizam poder ajustar a experiência às próprias necessidades. Toda configuração custa duas coisas: a pessoa precisa interromper o que estava fazendo para abrir a área de settings, e cada opção extra é uma decisão a mais que compete contra a abordagem de "boa configuração padrão para o maior número de pessoas". Por isso o texto trata a existência de uma configuração como algo a justificar, não como recurso neutro a mais.

### Faça e evite
- Ofereça padrões (defaults) que já entreguem a melhor experiência para a maioria das pessoas, em vez de pedir que elas decidam antes mesmo de começar a usar o app.
- Minimize o número de settings oferecidos; excesso de opções deixa a experiência menos aproximada e dificulta achar a opção certa.
- Disponibilize settings do jeito que as pessoas esperam encontrá-las (atalho de teclado convencional, por exemplo).
- Não peça em settings uma informação que o sistema já consegue detectar sozinho (controle conectado, Dark Mode ativo etc.).
- Respeite as configurações do sistema como um todo e evite duplicar, dentro do seu app, opções que já são globais (acessibilidade, scrolling, autenticação); duplicar implica, de forma confusa, que a config do sistema talvez não valha para o seu app.
- Coloque em uma área de settings própria só opções gerais e raramente alteradas (configuração de janela, comportamento de salvar jogo, mapeamento de teclado, opções de conta).
- Prefira deixar opções específicas de uma tarefa (mostrar/ocultar parte da view, reordenar uma coleção, filtrar uma lista) disponíveis na própria tela onde afetam o resultado, em vez de isolá-las numa área de settings separada, o que desconecta a opção do contexto e esconde o resultado até a pessoa voltar à tarefa.
- Em jogos, o ajuste de abordagem a uma tarefa específica tende a acontecer como parte do próprio gameplay, não como opção de settings.
- Adicione ao app de Settings do sistema apenas as opções mais raramente alteradas; se fizer sentido, ofereça um botão que abre diretamente essa tela do Settings a partir da sua interface.

### Especificações exatas
O texto não traz números, medidas ou valores exatos para este artigo.

### Diferenças por plataforma
- iOS, iPadOS, tvOS, visionOS: sem considerações adicionais.
- macOS: ao escolher o item Settings no menu App, abre a janela de settings personalizada, tipicamente com uma toolbar de botões que trocam entre "panes" (painéis) de configurações relacionadas. Inclua o item Settings no menu App (e, se houver opções em nível de documento, também no menu File). Esmaeça (dim) os botões de minimizar e maximizar da janela de settings, já que o atalho padrão Comando-Vírgula (,) torna desnecessário mantê-la na Dock, e a janela já se ajusta ao tamanho do pane atual. Use uma toolbar não customizável, sempre visível, que indique o botão ativo. Atualize o título da janela conforme o pane visível; se não houver múltiplos panes, use o título "Nome do App Settings". Restaure o último pane visualizado ao reabrir a janela.
- watchOS: apps e jogos não adicionam settings customizados ao app Settings do sistema; a alternativa é disponibilizar um pequeno número de opções essenciais na parte inferior da view principal, ou um menu "More" para reconfigurar objetos.

### Ligações com outros artigos
Onboarding (relacionado).

---

<!-- visual:settings -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 1001), código conferido; sem vídeo.
- O ícone é uma engrenagem vermelha com dezesseis dentes, três raios internos e um furo central, sobre gradiente laranja (img 1001).
- A grade de construção fica sobreposta e visível, com linhas retangulares, diagonais e um círculo guia concêntrico à engrenagem, mostrando um desenho feito sobre malha radial e retangular (img 1001).
- Os raios internos da engrenagem estão alinhados às diagonais da grade, sinal de que a geometria do símbolo segue a malha (img 1001).
- A capa repete a linguagem das aberturas de searching e right-to-left citadas nas notas: ícone simples tingido de laranja, grade retangular com círculo guia e cor ligada ao logo de seis cores da Apple (img 1001).
<!-- /visual:settings -->

## Undo and redo (slug: undo-and-redo)

### O que governa
Como oferecer undo e redo de forma que as pessoas consigam prever o resultado de cada ação de desfazer ou refazer.

### Por que
Undo e redo dão às pessoas formas fáceis de reverter ações e ajudam a explorar e experimentar uma interface ou tarefa nova com segurança. Como as pessoas costumam desfazer repetidamente até perceberem alguma mudança, elas podem perder o rastro de qual ação anterior o undo está de fato revertendo, o que gera alterações não intencionais e frustração. A prioridade do design, portanto, é ajudar a pessoa a prever o efeito do undo/redo e deixar o resultado bem visível.

### Faça e evite
- Ajude as pessoas a prever o resultado do undo e do redo tanto quanto possível: no iPhone, descreva o resultado no alerta que aparece ao balançar o aparelho, dando a opção de confirmar ou cancelar; em itens de menu de undo/redo, personalize o rótulo para identificar o resultado (ex.: "Undo Typing", "Redo Bold").
- Mostre o resultado de um undo ou redo, principalmente quando a ação mais recente afeta uma área não mais visível na tela; nesses casos, destaque o efeito (por exemplo, role o documento para mostrar o parágrafo restaurado), para que a pessoa não pense que a ação não teve efeito e a repita à toa.
- Deixe a pessoa desfazer múltiplas vezes; evite limitar sem necessidade a quantidade de undos ou redos, já que a expectativa é poder desfazer cada ação desde um passo lógico como abrir um documento ou salvar o trabalho.
- Considere permitir reverter várias mudanças de uma vez, seja um conjunto de ajustes incrementais a uma mesma propriedade, seja todas as mudanças desde a abertura do documento ou o último salvamento.
- Ofereça botões de undo e redo só quando necessário; a expectativa padrão é iniciar undo/redo pelos meios já suportados pelo sistema (menu Edit no macOS, atalhos de teclado no Mac e iPad, balançar o iPhone). Se for importante ter botões dedicados, use os símbolos padrão do sistema e coloque-os numa toolbar.

### Especificações exatas
O texto não traz números, medidas ou valores exatos para este artigo.

### Diferenças por plataforma
- visionOS: sem considerações adicionais. Não suportado em tvOS nem watchOS.
- iOS, iPadOS: evite redefinir os gestos padrão de undo e redo (deslizar com três dedos, balançar o iPhone), sob risco de confundir e tornar a experiência imprevisível. O título do alerta de undo/redo já inclui automaticamente o prefixo "Undo " ou "Redo " (com o espaço final); é preciso fornecer uma ou duas palavras adicionais que descrevam o que está sendo desfeito ou refeito, do tipo "Undo Name" ou "Redo Address Change".
- macOS: coloque os comandos de undo e redo no menu Edit e suporte os atalhos de teclado padrão; a expectativa é encontrá-los no topo do menu Edit e usar Comando-Z e Shift-Comando-Z, respectivamente.

### Ligações com outros artigos
Feedback, Pointing devices, Standard keyboard shortcuts, Edit menu (relacionados).

---

<!-- visual:undo-and-redo -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 1205), código conferido; sem vídeo.
- O símbolo é um ícone circular vermelho alaranjado com uma seta em gancho que começa embaixo à direita, sobe e curva para a esquerda até a ponta, o que confere com a leitura oficial de retorno ao início (img 1205).
- Uma grade de linhas tracejadas verticais, horizontais e diagonais, com um círculo fino concêntrico ao ícone, marca as proporções e a centralização do símbolo dentro do quadro (img 1205).
- A cor é construída em camadas: fundo laranja em gradiente, mais claro à esquerda e mais escuro à direita, com o ícone num vermelho mais saturado por cima; o tom predominante é laranja, não vermelho puro (img 1205).
- É ilustração conceitual de abertura, não captura de interface real, no mesmo padrão de símbolo sobre grade de construção tingido na cor temática que as notas apontam em typography e virtual-keyboards (img 1205).
<!-- /visual:undo-and-redo -->

## Workouts (slug: workouts)

### O que governa
Como projetar uma experiência de treino ou fitness (para Apple Watch, iPhone ou iPad) que ajude as pessoas a atingir seus objetivos, usando dados de atividade do dispositivo e componentes familiares para exibir métricas.

### Por que
As pessoas usam o Apple Watch durante muitos tipos de treino e podem carregar o iPhone ou iPad em atividades como caminhada, uso de cadeira de rodas e corrida; já dispositivos maiores ou mais estacionários (iPad Pro, Mac, Apple TV) tendem a ser usados para sessões de treino ao vivo ou gravadas, sozinho ou com outras pessoas. O raciocínio central é reduzir o atrito e a distração durante o esforço físico: mostrar só o que importa no momento, tornar a sessão ativa reconhecível à primeira vista e manter a legibilidade mesmo com o corpo em movimento.

### Faça e evite
- Em um app de fitness watchOS, use sessões de treino (workout sessions) para fornecer dados úteis e controles relevantes; como o watchOS mantém o app em tela entre os levantamentos de pulso durante uma sessão ativa, é importante mostrar os dados que mais interessam (tempo decorrido ou restante, calorias queimadas, distância percorrida) e oferecer controles relevantes como marcadores de volta ou intervalo.
- Evite distrair a pessoa com informação irrelevante durante o treino; ela não precisa, por exemplo, revisar a lista de treinos disponíveis ou acessar outras partes do app enquanto treina.
- Use uma aparência visual distinta para indicar um treino ativo; a tela de métricas costuma servir a esse propósito porque os valores se atualizam em tempo real, e um layout exclusivo reforça essa distinção.
- Forneça controles de treino fáceis de encontrar e tocar, incluindo pausar, retomar e parar, com feedback claro de início e fim de sessão.
- Ajude as pessoas a entender as informações de saúde registradas quando o sensor não está disponível durante o treino (por exemplo, água pode impedir a medição de frequência cardíaca, mas o app ainda pode registrar distância nadada e calorias); ao suportar os tipos Swimming ou Other, explique a situação com linguagem semelhante à usada no app Workout do sistema.
- Forneça um resumo ao final da sessão, confirmando que o treino terminou e exibindo as informações registradas; considere reforçar o resumo incluindo os Activity rings, para a pessoa checar seu progresso atual.
- Descarte sessões de treino extremamente breves: se uma sessão termina poucos segundos depois de começar, descarte os dados automaticamente ou pergunte se a pessoa quer registrá-los como treino mesmo assim.
- Garanta que o texto continue legível quando a pessoa está em movimento: use fontes grandes, cores de alto contraste e organize o texto para que a informação mais importante seja fácil de ler.
- Use os Activity rings corretamente: é um elemento desenhado pela Apple, com um ou mais anéis cujas cores e significados correspondem aos do app Activity; use-os apenas para o propósito documentado, não como elemento decorativo genérico.

### Especificações exatas
O texto não traz números, medidas ou valores exatos para este artigo (não há tamanhos de fonte, durações ou proporções numéricas especificados).

### Diferenças por plataforma
- iOS, iPadOS, watchOS: sem considerações adicionais além das já descritas.
- Não suportado em macOS, tvOS ou visionOS.

### Ligações com outros artigos
Activity rings (relacionado).

---

<!-- visual:workouts -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas (img 1333 a 1337), códigos conferidos; sem vídeo.
- A capa é uma figura correndo em silhueta vermelha sobre fundo laranja, com guias retangulares e circulares de construção, incluindo um círculo centrado no torso da figura (img 1333).
- A tela de controles do treino no Apple Watch é toda preta, com a hora e o estado "Paused" em verde no topo e quatro botões grandes numa grade 2x2, cada um com cor e ícone próprios da função: End vermelho com X, Resume amarelo oliva com seta circular, New verde com sinal de mais, Segment cinza com círculo e número 1 (img 1334).
- A tela de métricas empilha cinco linhas de dados na vertical, com o ícone verde de caminhada no canto superior esquerdo e a hora à direita; o tempo decorrido, em amarelo, é a maior linha da tela, acima de calorias ativas, frequência cardíaca, ritmo médio e distância (img 1335).
- A hierarquia de leitura rápida nas métricas vem só do tamanho da fonte e de um ícone colorido de contexto junto ao valor, como o coração vermelho da frequência cardíaca, sem cor de fundo para destacar (img 1335).
- Métrica sem dado aparece preenchida com traços, mantendo o rótulo do ritmo médio no lugar (img 1335).
- A tela de mídia mostra o estado sem reprodução: retângulo cinza grande com ícone de smartphone e o texto "Not Playing", três controles de voltar, tocar e avançar embaixo, e um ícone de iPhone ao lado da hora no topo (img 1336).
- As três telas do fluxo usam o mesmo fundo preto e a mesma hora no canto superior como âncora comum, variando só o conteúdo central entre grade de botões, pilha de métricas e controles de reprodução; indicadores de página em pontos sinalizam três telas, embaixo na de controles e na lateral direita na de métricas (img 1334, 1335, 1336).
- O uso correto é marcado por um selo isolado, check branco em círculo verde, sem nenhum outro elemento na folha; a imagem de exemplo que ele acompanha não está nesta folha (img 1337).
<!-- /visual:workouts -->

## O que este grupo revela sobre o jeito Apple

1. A configuração é tratada como custo, não como recurso grátis: em "settings", a diretriz central não é "como construir uma tela de opções" e sim "quando essa opção deveria nem existir", com o default certo substituindo a pergunta feita à pessoa (settings).
2. Há uma hierarquia explícita de onde uma opção deve morar, do mais contextual ao mais distante: dentro da própria tela de tarefa, depois na área de settings do app, e só por último no app Settings do sistema, sempre priorizando manter a opção perto de onde ela produz efeito (settings).
3. O sistema como autoridade única sobre preferências globais aparece duas vezes com a mesma lógica: em settings, não duplicar opções systemwide dentro do app; em undo-and-redo, preferir sempre os mecanismos de undo já suportados pelo sistema (menu Edit, atalhos, shake) a botões customizados (settings, undo-and-redo).
4. A previsibilidade do resultado de uma ação é tratada como requisito de design, não como detalhe de copy: o texto de undo-and-redo pede explicitamente que a pessoa consiga prever o efeito antes de agir, e que o resultado fique visível mesmo fora da área de tela atual (undo-and-redo).
5. A Apple assume o corpo do usuário como variável de design em contextos físicos: em workouts, fonte grande e alto contraste existem porque a pessoa está se movendo, não por preferência estética (workouts).
6. Elementos de marca com significado fixo (Activity rings) são citados como recurso a reaproveitar, mas com a ressalva de usá-los "apenas para o propósito documentado", indicando que a Apple protege a semântica de seus próprios componentes contra reuso livre (workouts).
7. Cada artigo tem uma seção "Platform considerations" que trata ausência de plataforma como informação relevante ("Not supported in..."), não como omissão; isso aparece em undo-and-redo (não suportado em tvOS e watchOS) e em workouts (não suportado em macOS, tvOS e visionOS), reforçando que o design de um recurso é sempre condicionado à plataforma, não universal por padrão.
8. Mesmo em recursos avançados (undo multibatch, sessão de treino, painel de settings no macOS), a orientação de fallback é sempre a mesma: menos interrupção do fluxo principal da pessoa, seja evitando abrir uma janela separada, seja evitando obrigar a desfazer ação por ação (settings, undo-and-redo, workouts).
9. Em nenhum dos três artigos a Apple define um valor numérico de referência (tamanho, tempo, contraste); a precisão exigida nesses casos é de comportamento e hierarquia de decisão, não de medida visual, o que contrasta com artigos de componentes visuais da HIG que costumam trazer pt/px.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/settings.md, 52 linhas lidas, até o fim: sim (arquivo termina na seção "Change log").
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/undo-and-redo.md, 37/38 linhas lidas, até o fim: sim (arquivo termina na seção "Videos").
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/workouts.md, 40/41 linhas lidas, até o fim: sim (arquivo termina na seção "Videos").
