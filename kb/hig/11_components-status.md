# Components / Status

## Activity rings (slug: activity-rings)

### O que governa
Regula o uso do elemento Activity ring, que mostra o progresso diário de uma pessoa em relação às metas de Move, Exercise e Stand.

### Por que
O elemento existe para representar um conceito muito específico do ecossistema Apple (as três métricas de atividade física) de forma consistente entre apps, para que as pessoas reconheçam instantaneamente o que estão vendo, no watchOS e no iOS, tanto quanto veem no app Activity. A Apple protege a integridade visual do símbolo (cores fixas, fundo preto, margens) porque ele funciona como uma linguagem visual padronizada: qualquer alteração de cor, opacidade ou contexto quebra esse reconhecimento e pode confundir a leitura do progresso real da pessoa. A proibição de uso decorativo ou como branding vem do mesmo princípio: Activity rings comunicam dado, não identidade visual do app.

### Faça e evite
- Exiba Activity rings quando forem relevantes ao propósito do app, especialmente em apps de saúde ou fitness, sobretudo os que contribuem dados ao HealthKit.
- Considere mostrar o elemento numa tela de métricas de treino, para acompanhar progresso durante a sessão, ou numa tela de resumo ao fim do treino.
- Use Activity rings apenas para mostrar informação de Move, Exercise e Stand. Nunca as use para outro tipo de dado.
- Nunca mostre progresso de Move, Exercise e Stand em outro elemento parecido com anel.
- Use Activity rings para mostrar o progresso de uma única pessoa. Nunca represente dados de mais de uma pessoa no mesmo elemento, e deixe claro de quem é o progresso (rótulo, foto ou avatar).
- Nunca mude as cores dos anéis, inclusive por filtro ou opacidade.
- Sempre exiba os Activity rings sobre fundo preto.
- Prefira encerrar os anéis e o fundo dentro de um círculo ajustando o corner radius da view, em vez de aplicar uma máscara circular.
- Garanta que o fundo preto continue visível ao redor do anel mais externo; se necessário, adicione um traço fino e preto na borda externa, e evite gradiente, sombra ou qualquer outro efeito visual.
- Escale os anéis de forma adequada, para que não pareçam desconectados ou deslocados.
- Quando necessário, desenhe a interface ao redor para combinar com os anéis, nunca o contrário.
- Para rótulos ou valores associados a um anel específico, use as cores correspondentes a ele.
- Mantenha a margem externa mínima do elemento igual ou maior que a distância entre os anéis; nunca deixe outros elementos cortar, obstruir ou invadir essa margem ou os próprios anéis.
- Diferencie outros elementos em forma de anel dos Activity rings, usando padding, linhas, rótulos, cor ou escala para separá-los visualmente.
- Não envie notificações que repitam informação que o app Activity já envia, e não mostre o elemento Activity ring dentro de notificações do seu app; é aceitável referenciar o progresso de forma própria, sem replicar o que o sistema já mostra.
- Não use Activity rings como decoração, em rótulos ou em gráficos de fundo.
- Não use Activity rings para branding, ícone do app ou material de marketing.

### Especificações exatas
Cores RGB especificadas para os rótulos e valores de cada anel, segundo a descrição da imagem:
- Move: R 250, G 17, B 79
- Exercise: R 166, G 255, B 0
- Stand: R 0, G 255, B 246

### Diferenças por plataforma
- watchOS: o elemento sempre contém três anéis, com cores e significados iguais aos do app Activity.
- iOS: contém um único anel Move (aproximação de atividade baseada em passos e treinos de outros apps) quando não há Apple Watch pareado, ou os três anéis quando há Apple Watch pareado. Disponível via HKActivityRingView. Como o comportamento muda conforme o pareamento, o histórico de atividade de um app pode misturar os dois estilos ao longo do tempo.
- iPadOS e watchOS: sem considerações adicionais além do exposto.
- Não suportado em macOS, tvOS ou visionOS.

### Ligações com outros artigos
Workouts (relacionado). Documentação de desenvolvedor: HKActivityRingView (HealthKit).

---

<!-- visual:activity-rings -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura é um diagrama anotado: três anéis concêntricos parcialmente preenchidos, com setas indicando o sentido do progresso em cada um e rótulos ligados por linhas guia, Move com porcentagem e calorias à esquerda, Stand com horas à direita e Exercise com minutos embaixo (img 0029).
- A ordem das cores nunca muda entre as imagens: vermelho ou rosa no anel externo, verde no do meio e ciano no interno, tanto no diagrama quanto nas capturas do relógio e do iPhone (img 0029, img 0030, img 0034).
- Na tela de treino do Apple Watch, sobre fundo preto, aparecem o ícone verde de corrida no topo, a hora e um cronômetro grande em amarelo, com a lista de valores Move, Exercise e Stand à esquerda e os três anéis à direita refletindo esses valores parciais (img 0030).
- As cores dos anéis são especificadas como amostras isoladas, cada uma um quadrado arredondado de cor sólida com o valor RGB ao lado: rosa avermelhado 250, 17, 79; verde limão 166, 255, 0; ciano 0, 255, 246 (img 0031, img 0032, img 0033).
- Nas capturas reais os anéis aparecem sempre sobre fundo preto, e no iPhone ficam dentro de um cartão "Activity Rings" com os valores listados ao lado, não sobrepostos aos anéis (img 0030, img 0034, img 0035).
- A diferença entre ter ou não um Apple Watch pareado é isolada por um par de telas Summary do app Fitness com o mesmo cabeçalho, a mesma data e o mesmo avatar memoji no canto, mudando só o cartão (img 0034, img 0035).
- Com o relógio pareado, o cartão mostra os três anéis completos e as três métricas com meta atingida (img 0034); sem ele, mostra um único anel rosa parcialmente preenchido, e as métricas de Exercise e Stand dão lugar a passos e distância (img 0035).
- A porcentagem escrita ao lado de cada anel só aparece no diagrama conceitual; nas telas de app os valores vêm como pares de valor atual e meta, com unidade no iPhone (img 0029 comparada com img 0030 e img 0034).
<!-- /visual:activity-rings -->

## Gauges (slug: gauges)

### O que governa
Regula o gauge, componente que exibe um valor numérico específico dentro de um intervalo de valores, em caminho circular ou linear.

### Por que
O gauge serve tanto para mostrar a posição atual de um valor quanto para dar contexto sobre o intervalo inteiro (extremos, gradiente de cor), de modo que a pessoa entenda não só "quanto" mas "onde isso está" dentro de uma faixa. A recomendação de rótulos sucintos existe porque o VoiceOver lê os rótulos visíveis para que quem não vê a tela também compreenda o gauge, ou seja, a acessibilidade depende diretamente da qualidade textual do componente.

### Faça e evite
- Escreva rótulos sucintos que descrevam o valor atual e os dois extremos do intervalo; ainda que nem todo estilo de gauge mostre todos os rótulos, o VoiceOver lê os que estiverem visíveis.
- Considere preencher o caminho com um gradiente para ajudar a comunicar o propósito do gauge (exemplo dado: um gauge de temperatura pode variar de vermelho a azul, do quente ao frio).

### Especificações exatas
O texto não traz números de dimensão, espaçamento, duração ou proporção para o gauge em si.

### Diferenças por plataforma
- iOS, iPadOS, visionOS, watchOS: sem considerações adicionais.
- Não suportado em tvOS.
- macOS: além dos gauges, também define o level indicator, com estilos visuais por vezes parecidos com os de gauges, configurável para capacidade, rating ou (raramente) relevância.
  - Estilo capacity, contínuo: barra horizontal translúcida que se preenche com uma barra sólida indicando o valor atual, segundo a descrição da imagem.
  - Estilo capacity, discreto: fileira horizontal de segmentos retangulares iguais e separados; o número de segmentos corresponde à capacidade total, e cada segmento preenche completamente, nunca parcialmente, para indicar o valor.
  - Considere o estilo contínuo para intervalos grandes, pois um intervalo grande pode deixar os segmentos do estilo discreto pequenos demais para serem úteis.
  - Considere mudar a cor de preenchimento para sinalizar partes significativas do intervalo (muito baixo, muito alto, ou logo após o meio). A cor padrão de preenchimento em ambos os estilos de capacity é verde. É possível mudar a cor do indicador inteiro ou usar o estado tiered para mostrar uma sequência de várias cores num único indicador (exemplo descrito na imagem: um oitavo vermelho, três oitavos amarelo, um quarto verde e o restante sem preenchimento).
  - Para orientação sobre o estilo rating (usado para ranquear algo), ver o artigo Rating indicators.
  - O estilo relevance, embora raramente usado, comunica relevância por uma barra horizontal sombreada, por exemplo numa lista de resultados de busca, ao ordenar ou comparar múltiplos itens.

### Ligações com outros artigos
Ratings and reviews (relacionado). Rating indicators (citado para o estilo rating do level indicator do macOS). Documentação de desenvolvedor: Gauge (SwiftUI), NSLevelIndicator (AppKit). Também remete ao artigo macOS para orientação geral sobre level indicators.

---

<!-- visual:gauges -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página não tem vídeo.
- A abertura funciona como diagrama de anatomia dos dois formatos, empilhados num cartão em gradiente de laranja para vermelho, sem a grade tracejada usada em outras aberturas: um gauge circular numérico em cima e um linear de porcentagem embaixo (img 0523).
- O gauge circular tem um arco incompleto em vermelho escuro ao redor do número grande "67", uma bolinha marcando a ponta do trecho preenchido e os rótulos "0" e "100" abaixo do número indicando os extremos, com setas de medida acima e abaixo cotando a altura (img 0523).
- O gauge linear tem a metade esquerda preenchida em vermelho escuro e a direita em tom mais claro, com "0%" e "100%" nas pontas e setas de medida indicando a largura e as margens laterais (img 0523).
- O indicador de capacidade contínuo do macOS é uma barra única de cantos arredondados, com trilho cinza claro e preenchimento verde sólido em cerca de dois terços, sem divisões internas (img 0524).
- O discreto usa a mesma barra dividida em 8 segmentos retangulares separados por pequenos espaços, com 6 preenchidos em verde e 2 em cinza claro, somando três quartos (img 0525).
- No estado tiered, a barra contínua recebe várias cores em sequência da esquerda para a direita: um trecho vermelho estreito, um amarelo bem mais largo, um verde e o restante em cinza não preenchido (img 0526).
- As três variações do macOS isolam uma decisão por vez: contínuo contra discreto troca a barra lisa por segmentos separados (img 0524 comparada com img 0525, com preenchimentos observados de cerca de dois terços e de três quartos), e cor única contra cores por faixa muda a codificação de cor da mesma barra contínua (img 0524 comparada com img 0526).
<!-- /visual:gauges -->

## Progress indicators (slug: progress-indicators)

### O que governa
Regula os indicadores de progresso, elementos transitórios que avisam que o app não travou enquanto carrega conteúdo ou executa operações demoradas.

### Por que
A função central do progress indicator é gerenciar a expectativa e a confiança da pessoa durante uma espera: ele existe para que ninguém confunda um processo em andamento com um app travado. Por isso a Apple distingue determinado de indeterminado conforme a duração da tarefa é conhecida ou não, e prefere o determinado sempre que possível, porque ele dá à pessoa uma base real para decidir se espera, faz outra coisa, reinicia a tarefa mais tarde ou desiste dela. A exigência de manter o indicador sempre em movimento e de ritmo de avanço uniforme (não pular de 90% em 5 segundos para os últimos 10% em 5 minutos) parte do mesmo princípio: um indicador parado ou com ritmo inconsistente é lido como falha, mesmo quando o processo continua ativo, e pode até parecer enganoso. Permitir cancelar ou pausar, e avisar quando cancelar tem consequência negativa, é uma extensão da mesma lógica de dar controle e informação honesta à pessoa durante a espera.

### Faça e evite
- Use um indicador determinado sempre que possível; o indeterminado mostra que algo está ocorrendo, mas não ajuda a estimar quanto tempo falta.
- Seja o mais preciso possível ao reportar avanço num indicador determinado. Considere nivelar o ritmo de avanço para passar confiança sobre o tempo necessário; mostrar 90% em 5 segundos e os últimos 10% em 5 minutos pode parecer que o app travou, ou até enganoso.
- Mantenha os indicadores de progresso sempre em movimento, para que as pessoas saibam que algo continua acontecendo; um indicador parado costuma ser associado a processo travado ou app congelado. Se um processo realmente travar, dê um retorno que ajude a pessoa a entender o problema e o que fazer.
- Quando possível, troque uma barra de progresso de indeterminada para determinada assim que a duração puder ser calculada; as pessoas geralmente preferem o indicador determinado, porque ajuda a entender o que está acontecendo e quanto tempo vai levar.
- Não alterne entre o estilo circular e o estilo de barra: activity indicators (spinners) e progress bars têm formatos e tamanhos diferentes, e a transição entre eles pode atrapalhar a interface e confundir as pessoas.
- Se for útil, mostre uma descrição com contexto adicional sobre a tarefa. Seja preciso e sucinto; evite termos vagos como "carregando" ou "autenticando", que raramente agregam valor.
- Exiba o indicador de progresso num local consistente, para que a pessoa encontre o status da operação de forma confiável entre plataformas, dentro do app ou entre apps.
- Quando for viável, permita interromper o processamento: se a pessoa puder interromper sem efeito colateral negativo, inclua um botão Cancel; se interromper puder causar efeito negativo (como perder a parte já baixada de um arquivo), pode ser útil oferecer um botão Pause além do Cancel.
- Avise quando interromper um processo tiver consequência negativa: quando cancelar resultar em perda de progresso, é útil mostrar um alerta com opção de confirmar o cancelamento ou retomar o processo.

### Especificações exatas
O texto não traz números de duração, tamanho ou espaçamento para os indicadores. Não há valores numéricos exatos além do exemplo qualitativo de ritmo (90% em 5 segundos, últimos 10% em 5 minutos), que é um exemplo ilustrativo de má prática, não uma especificação.

### Diferenças por plataforma
- tvOS e visionOS: sem considerações adicionais.
- iOS, iPadOS: além do padrão, existe o refresh control, um tipo especializado de activity indicator oculto por padrão, que aparece quando a pessoa arrasta para baixo a view que quer recarregar (exemplo dado: lista de mensagens do Inbox no Mail). Recomendações: realizar atualizações automáticas de conteúdo periodicamente, sem depender só da ação manual da pessoa; incluir um título curto no refresh control apenas se agregar valor, e nesse caso usá-lo para informar algo relevante sobre o conteúdo (por exemplo, quando foi a última atualização), nunca para explicar como usar o controle. Documentação de desenvolvedor: UIRefreshControl.
- macOS: o indeterminado pode ter aparência de barra ou circular, ambas com imagem animada. Prefira o activity indicator (spinner) para comunicar status de operação em segundo plano ou quando o espaço é limitado, por ser pequeno e discreto, útil para tarefas assíncronas (como buscar mensagens de um servidor) ou para comunicar progresso numa área pequena, como dentro de um campo de texto ou ao lado de um controle específico. Evite rotular um indicador giratório, já que ele costuma aparecer quando a própria pessoa inicia o processo, tornando o rótulo geralmente desnecessário.
- watchOS: por padrão o sistema exibe os indicadores em branco sobre a cor de fundo da cena; é possível mudar a cor do indicador ajustando sua tint color.

### Ligações com outros artigos
Documentação de desenvolvedor: ProgressView (SwiftUI), UIProgressView (UIKit), UIActivityIndicatorView (UIKit), UIRefreshControl (UIKit), NSProgressIndicator (AppKit).

---

<!-- visual:progress-indicators -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura reúne os dois tipos numa só composição com guias de medida em vermelho: um spinner de raios curtos centralizado no alto e, abaixo, uma barra escura preenchida em cerca de 60%, com setas marcando largura e altura (img 0906).
- No macOS, a barra determinada fica dentro de um retângulo cinza claro arredondado, com preenchimento azul sólido até pouco antes da metade e o restante em cinza claro (img 0907).
- O indicador circular determinado é um anel fino preenchido em azul no sentido horário a partir do topo, quase completo, com um trecho cinza claro restante perto da posição das 8 horas (img 0908).
- O indicador indeterminado circular do macOS é um ícone pequeno de raios curtos ao redor de um centro vazio, em cinza sobre fundo branco (img 0909).
- A barra indeterminada do macOS aparece totalmente preenchida, mas com gradiente de azul mais forte no centro para quase transparente nas pontas, o que sugere um brilho em onda percorrendo a barra em vez de um avanço de preenchimento (img 0912).
- No watchOS, barra e anel ficam dentro de um retângulo preto arredondado que imita o mostrador, com preenchimento branco sólido e o restante em cinza escuro, em vez do azul do macOS: a barra em cerca de 65% e o anel em pouco mais da metade, no sentido horário a partir do topo (img 0913, img 0914).
- O spinner associado ao watchOS usa pontos dispostos em círculo dentro de um quadrado preto arredondado, com opacidade variando de branco no topo a cinza escuro embaixo (img 0910).
- O refresh control aparece numa tela real do Mail no iPhone: o spinner cinza fica centralizado logo abaixo da barra de status, acompanhado do texto "Updated Just Now", e a lista de caixas de correio continua visível abaixo dele (img 0911).
- Nos dois indicadores circulares determinados, o preenchimento começa no topo e avança no sentido horário, azul sobre cinza claro num e branco sobre cinza escuro dentro da moldura preta do watchOS no outro (img 0908, img 0914).
Divergências registradas: a img 0910 não tem legenda visível no contexto, e sua ligação com o watchOS foi deduzida pela posição na lista de legendas.
<!-- /visual:progress-indicators -->

## Rating indicators (slug: rating-indicators)

### O que governa
Regula o rating indicator, uma série de símbolos gráficos dispostos horizontalmente (por padrão, estrelas) que comunicam um nível de ranking.

### Por que
O componente existe para comunicar uma avaliação de forma rápida e visual, e por isso a Apple mantém regras rígidas de legibilidade: símbolos sempre à mesma distância entre si, sem expandir ou encolher para caber na largura do componente, e arredondamento para símbolos completos em vez de parciais. Isso garante que o rating seja lido de forma consistente e inequívoca, independentemente do espaço disponível. A recomendação de manter a estrela, ou deixar claro o propósito de um símbolo substituto, decorre do mesmo raciocínio: a estrela já é um símbolo de ranking amplamente reconhecido, e qualquer substituição sem clareza arrisca não ser entendida como escala de avaliação.

### Faça e evite
- Facilite a mudança de ranking: ao apresentar uma lista de itens ranqueados, permita ajustar o rank de itens individuais diretamente ali, sem navegar para uma tela de edição separada.
- Se substituir a estrela por um símbolo customizado, garanta que o propósito dele fique claro, já que outros símbolos podem não ser associados a uma escala de avaliação da mesma forma que a estrela.
- O componente nunca exibe símbolos parciais; ele arredonda o valor para mostrar apenas símbolos completos.
- Dentro do rating indicator, os símbolos ficam sempre à mesma distância entre si, e não expandem nem encolhem para caber na largura do componente.

### Especificações exatas
O texto não traz números de tamanho, espaçamento ou duração para o rating indicator.

### Diferenças por plataforma
- macOS: sem considerações adicionais.
- Não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Ratings and reviews (relacionado). Documentação de desenvolvedor: NSLevelIndicator.Style.rating (AppKit). Também citado a partir do artigo Gauges, como referência do estilo rating do level indicator no macOS.

---

<!-- visual:rating-indicators -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página tem só a ilustração de abertura e não tem vídeo.
- O componente é desenhado como uma fileira horizontal de cinco estrelas, com a nota de três em cinco expressa por estrelas inteiras, três cheias e duas vazias, sem estrela fracionada (img 0918).
- Estrela cheia e estrela vazia se distinguem só pelo tom da mesma cor: vermelho escuro sólido nas preenchidas e vermelho mais claro e translúcido nas vazias, sem contorno separado (img 0918).
- As setas de medida cotam duas dimensões diferentes: a largura total da fileira e a altura de uma estrela individual (img 0918).
- É uma peça conceitual sobre degradê laranja para vermelho, no mesmo estilo de diagrama de especificação das outras ilustrações de abertura, e confirma a descrição oficial de um ranking de três em cinco estrelas (img 0918).
<!-- /visual:rating-indicators -->

## O que este grupo revela sobre o jeito Apple

1. Componentes que carregam dado do sistema (Move, Exercise, Stand em Activity rings) são tratados como vocabulário protegido: cor, forma e contexto ficam travados para preservar reconhecimento instantâneo entre apps, ao contrário de componentes genéricos como gauges ou rating indicators, que o app pode adaptar (activity-rings vs. gauges, rating-indicators).
2. A escolha entre estilo determinado e indeterminado, ou entre gauge simples e level indicator com gradiente, é sempre subordinada a dar à pessoa o máximo de informação honesta sobre "onde estou" e "quanto falta", nunca só a estética (progress-indicators, gauges).
3. Consistência de forma é tratada como regra de usabilidade, não de gosto: não alternar entre spinner e barra de progresso, não deixar os símbolos do rating indicator mudarem de espaçamento, é sempre para não confundir a leitura de um estado (progress-indicators, rating-indicators).
4. A acessibilidade aparece embutida no próprio componente, não como camada separada: o VoiceOver lê os rótulos do gauge, o que obriga o texto a ser sucinto e correto desde o desenho (gauges).
5. Há uma hierarquia clara entre feedback do sistema e feedback do app: o app pode referenciar dados como progresso de Activity de forma própria, mas nunca replicar ou duplicar o que o sistema (watchOS/app Activity) já comunica, para não gerar redundância confusa (activity-rings).
6. A Apple distingue com cuidado "dado real" de "decoração": Activity rings e rating indicators têm proibição explícita de uso decorativo ou de branding, porque comunicam informação de verdade, não identidade visual (activity-rings, rating-indicators).
7. macOS recebe tratamento à parte nesse grupo, com um componente próprio (level indicator) que sobrepõe funções de gauge, rating e relevância, mostrando que a Apple concentra em uma única plataforma variações de estilo que outras plataformas nem sequer suportam (gauges, rating-indicators, progress-indicators).
8. Dar controle à pessoa durante uma espera (cancelar, pausar, avisar sobre perda de progresso) é tratado como parte do próprio design do componente de progresso, não como funcionalidade extra opcional (progress-indicators).
9. Todos os quatro componentes deste grupo remetem a "Ratings and reviews" ou entre si (gauges cita rating-indicators, rating-indicators cita gauges), mostrando que a Apple pensa esses componentes de status como uma família inter-relacionada, não unidades isoladas (gauges, rating-indicators).

## Evidência de leitura
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/activity-rings.md: 55 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/gauges.md: 45 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/progress-indicators.md: 67 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/rating-indicators.md: 25 linhas lidas, até o fim: sim
