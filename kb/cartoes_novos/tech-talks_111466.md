## Design for iPhone Duo (id: tech-talks_111466, 10.8 min)

Base: transcrição (quadros ainda não vistos). Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111466/.

Tese central: Dois designers do time de design da Apple, Marcos e Vince, apresentam o iPhone Duo, o primeiro iPhone dobrável, e defendem que o app deve parecer uma experiência única que se adapta aos diferentes tamanhos de tela e posições do aparelho. Para isso, em vez de um layout sob medida para cada posição, o caminho é mirar em duas size classes, levar os controles para a lateral e manter o app livremente redimensionável.

O processo de design que a Apple descreve:
1. A fala não descreve um processo interno de design em etapas; conta apenas que o time aprendeu muito ao adaptar os próprios apps ao iPhone Duo. O que segue é a ordem do roteiro da sessão.
2. Entender primeiro os princípios do aparelho: fechado, compacto e familiar; aberto, a maior tela já feita num iPhone; e as posições de uso (parcialmente dobrado como um livro, apoiado na mesa como um laptop com a tela interna voltada para a pessoa, ou em pé apoiado nas bordas).
3. Entender como o sistema reorganiza a interface: controles na lateral nas telas externa e interna, conteúdo afastado da dobra quando o aparelho está parcialmente dobrado, nova tela dividida 50/50 e picture in picture fixado no topo.
4. Adaptar o app mirando em duas size classes, com layout margins e horizontal safe area insets, sem desenhar um layout para cada posição.
5. Avaliar se vale um layout opcional para a posição apoiada na mesa, mantendo os mesmos controles e a mesma hierarquia.
6. Mapear os controles existentes do app de iPhone para a coluna lateral e tratar as exceções.
7. Resolver a assimetria da tela externa escolhendo entre deslocar o conteúdo, centralizar na tela inteira ou combinar as duas abordagens.
8. Escolher uma estratégia para a tela interna: split view, conteúdo otimizado para a tela larga ou tab bar apresentada como sidebar.
9. Conferir o comportamento de sheets em cada posição e usar componentes do sistema para herdar o desvio da dobra.

Princípios enunciados e o porquê:
- Fechado, o aparelho é compacto e familiar e cabe confortavelmente na mão; aberto, revela a maior e mais imersiva tela já feita num iPhone. O porquê: é a melhor tela possível para apps e conteúdo num aparelho que ainda cabe no bolso.
- Várias formas de segurar e apoiar o aparelho. O porquê: dá flexibilidade e deixa a pessoa usar o aparelho do jeito que quiser, em qualquer situação.
- Na tela externa, botões e controles que normalmente ficam no topo e na base passam para o lado direito. O porquê: maximiza o espaço vertical, fica mais fácil alcançar com o polegar direito e cria à esquerda uma área contínua para o conteúdo, comparável à de um iPhone com proporção tradicional. Na tela interna os controles também vão para a lateral, pelo mesmo motivo de espaço vertical e alcance.
- Com o aparelho parcialmente dobrado como um livro, o conteúdo sai da região central. O porquê: textos e imagens ficam mais fáceis de ler longe da curva, botões e elementos interativos ficam mais fáceis de acertar nas laterais, e a curva vira um divisor natural do layout.
- Em retrato, parcialmente dobrado, os elementos interativos descem para a metade de baixo. O porquê: ficam mais fáceis de alcançar e o aparelho continua estável sobre a superfície.
- A nova tela dividida é construída sobre o gesto de home do iPhone. O porquê: parece fluida e familiar; as duas metades funcionam de forma independente, então dá para manter uma tarefa de um lado enquanto se usa o outro.
- Na tela dividida, os controles ficam na borda externa; um app do lado esquerdo leva os controles para a borda esquerda. O porquê: ficam ao alcance do polegar e longe da região central.
- Não desenhar um layout para cada posição; mirar nas size classes e evitar larguras fixas, breakpoints ou métricas atreladas a uma tela específica. O porquê: as pessoas usam o aparelho em muitas posições e o app precisa ficar bem em todas; quem já usa essas ferramentas deve ter um app que já se adapta.
- Um layout especial para a posição na mesa precisa ter os mesmos controles e a mesma hierarquia geral das outras posições. O porquê: não se deve atrelar funcionalidade a uma posição específica.
- Barras horizontais só permanecem na tela interna em retrato. O porquê: ali há espaço vertical de sobra para o conteúdo.
- Na tela externa, a maior parte do conteúdo precisa de deslocamento. O porquê: para não ficar escondida atrás dos controles.
- Algumas interfaces ainda devem centralizar na tela inteira, sem deslocamento. O porquê: isso funciona bem para interfaces imersivas, muito visuais e que não rolam, desde que haja certeza de que os controles da direita não vão bloquear elementos interativos.
- Na tela interna, não entregar apenas um app de iPhone esticado.
- A hierarquia não deve mudar entre as telas externa e interna, e a funcionalidade não deve ficar limitada a uma posição. O porquê: as pessoas podem abrir e fechar o aparelho com frequência enquanto usam o app, então ele precisa ser previsível e consistente por dentro e por fora.
- A tab bar como sidebar não serve para todo app. O porquê: funciona melhor em apps densos em informação.
- Manter elementos interativos fora da região da curva sempre que possível. O porquê: o time descobriu que botões são difíceis de tocar quando caem exatamente na dobra. Conteúdo rolável não precisa evitar essa região.

Técnicas concretas de construção de interface, com números exatos quando falados:
- A fala não dá valores de interface em pontos, pixels, tamanhos de fonte, cores ou durações. Os números ditos são contagens estruturais: a divisão 50/50 da tela dividida, as duas size classes, o layout de duas colunas e as três opções para a tela interna.
- Size classes: compact width na tela externa e regular width na tela interna. Evitar larguras fixas, breakpoints e métricas de uma tela específica. Construir com layout margins e horizontal safe area insets e pensar o app como livremente redimensionável.
- Tela externa fechada: mais larga e mais baixa que a de um iPhone tradicional. A coluna lateral direita abriga a barra superior, as toolbars do app e controles de navegação como o botão de voltar, além da barra de status redesenhada e da Dynamic Island, que se expande verticalmente quando chegam Live Activities.
- Espaço vertical compartilhado: os controles do app dividem a coluna lateral com elementos dinâmicos do sistema (Live Activities e barra de status). Sem espaço suficiente, os controles do app recolhem automaticamente num menu de overflow.
- Mapeamento dos controles do app de iPhone: botões da toolbar do topo vão para o topo do espaço vertical; botões da toolbar de baixo vão para a base; a tab bar continua alinhada embaixo. Exceção: itens largos demais para o espaço da direita, como um botão de texto ou um "segment to control" (termo incerto na transcrição automática), ficam na barra de navegação.
- Barras horizontais: mantidas apenas na tela interna em retrato.
- Dobra: conteúdo sai do centro com o aparelho parcialmente dobrado; em retrato, os elementos interativos vão para a metade de baixo.
- Tela dividida: arrastar um app para o lado cria a divisão 50/50 em duas metades independentes; controles na borda externa de cada metade.
- Picture in picture: o vídeo pode ser fixado no topo da tela e o app atual se redimensiona verticalmente para o espaço restante; ao dobrar parcialmente, o vídeo passa a ocupar metade da tela, e os apps se ajustam verticalmente aos diferentes tamanhos de vídeo em tempo real.
- Layout opcional para a posição na mesa, pensado para uso sem as mãos: mídia no topo e controles tocáveis numa base estável embaixo.
- Layouts assimétricos na tela externa, que a fala chama de "layers" (termo incerto na transcrição automática), com três abordagens: (a) deslocar o conteúdo, o que acontece sozinho quando o app se alinha às horizontal safe area insets; (b) centralizar na tela inteira sem deslocamento, para interfaces imersivas, muito visuais e sem rolagem; (c) combinar uma imagem de fundo ou cabeçalho de largura total com conteúdo rolável em primeiro plano recuado, mantendo todo elemento interativo dentro da área rolável para que nada fique coberto.
- Tela interna, três opções: split views que mostram vários níveis da hierarquia do app ao mesmo tempo; conteúdo otimizado para a tela larga, por exemplo uma pilha vertical que se reorganiza em duas colunas quando há mais espaço horizontal; e, para apps com tab bar, apresentar a tab bar como sidebar.
- Sheets na tela externa: por padrão os controles da sheet também vão para a lateral. Dá para impedir isso desativando a barra vertical na sheet, o que funciona bem para sheets com um único botão de toolbar; nesse caso a sheet para logo antes da câmera frontal e a barra de status se reposiciona.
- Sheets na tela interna, em paisagem e em retrato: usam as barras horizontais padrão. Com o aparelho parcialmente dobrado, as sheets deslizam para o lado para não repousar na dobra.
- Desvio da dobra: comportamento que empurra elementos interativos para longe da dobra quando o aparelho está parcialmente dobrado, embutido em componentes do sistema como sheets, alerts, menus, botões de toolbar e outros. Usar esses componentes sempre que possível para ganhar o mesmo comportamento no app. Conteúdo rolável não precisa evitar a região.

Exemplos citados:
- Posições de uso (livro parcialmente dobrado, laptop sobre a mesa, em pé sobre as bordas): ensinam que o app precisa funcionar em muitas configurações sem um design para cada uma.
- Tela dividida para manter uma tarefa de um lado enquanto se usa a outra metade: ensina que as metades são independentes e que os controles vão para a borda externa.
- Vídeo em picture in picture fixado no topo, que cresce até metade da tela ao dobrar: ensina que os apps precisam se ajustar verticalmente em tempo real.
- Uso sem as mãos com o aparelho sobre a mesa, com mídia em cima e controles embaixo: ensina que um layout por posição é opcional e não pode mudar controles nem hierarquia.
- Os próprios apps da Apple adaptados ao iPhone Duo: o time aprendeu que várias abordagens funcionam bem conforme o estilo do conteúdo.
- App Saúde (Health) com a tab bar apresentada como sidebar na tela interna: ensina que a sidebar funciona melhor em apps densos em informação.
- Sheet com um único botão de toolbar e a barra vertical desativada: ensina quando vale impedir que os controles da sheet migrem para a lateral.

Citações:
"Apps should feel like a single experience adapting to the different display sizes and poses."
"You don't want to tie functionality to a specific pose."
