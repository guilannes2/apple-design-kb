## Strike a pose with adaptive layouts on iPhone Duo (id: tech-talks_111463, 18.0 min)

Base: transcrição (quadros ainda não vistos). Transcrição automática local feita com Whisper, não é a oficial da Apple; nomes próprios e termos podem ter erro de audição. Fonte: https://developer.apple.com/videos/play/tech-talks/111463/.

Tese central: No iPhone Duo, a dobradiça e as câmeras criam reserved regions, e o bom design depende de saber quando adaptar: mover, redimensionar ou reorganizar o que já existe (o padrão de displacement) para manter conteúdo e controles visíveis, alcançáveis e desobstruídos em qualquer pose. Para isso a Apple apresenta a API de reserved regions, para layouts montados à mão, e os arrangements (split e overlay), contêineres de layout para duas views, sempre adaptando só quando isso melhora a experiência.

O processo de design que a Apple descreve:
1. Entender o aparelho: várias telas, cada uma com sua própria size class, o que deve soar familiar para quem já projeta para redimensionamento; recursos de hardware (a dobradiça e as duas câmeras das telas externa e interna) moldam o espaço disponível e são chamados de reserved regions, a serem tratados como qualquer outra área a que o layout já se adapta.
2. Entender cada tela: na externa, a câmera está sempre presente e toolbars e tab bars do sistema ficam na vertical dentro da nova safe area; na interna, a interface pode se adaptar à dobra ou à nova câmera FaceTime quando ativa; com o aparelho parcialmente dobrado como um livro, a dobra divide a tela interna em várias regiões usáveis.
3. Saber quando adaptar: muitas interfaces fluem naturalmente em volta das reserved regions; outras pedem uma abordagem intencional, o displacement.
4. Escolher o escopo do deslocamento: de um botão a um contêiner inteiro ou partes maiores do layout.
5. Decidir para onde o elemento vai, guiado pelo seu propósito e pela pose do aparelho (como livro ou apoiado na mesa), priorizando o que é contextual quando mais de uma região serve.
6. Considerar como o elemento se adapta ao novo entorno: posição e tamanho são as mudanças mais comuns, mas outras propriedades visuais também podem mudar.
7. Implementar com a API de reserved regions em SwiftUI ou UIKit, consultando regiões de divisão e de oclusão, ativas ou inativas.
8. Aproveitar os componentes do sistema que já se adaptam à dobra e, para layouts de duas views, usar arrangements, escolhendo entre split e overlay e reconhecendo quando um arrangement não é a ferramenta certa.
9. Roteiro final de preparação: auditar os layouts centralizados do app; considerar se dá para transformá-los em layout de duas colunas ou qual padrão de displacement faz sentido; usar contêineres e apresentações padrão do sistema, que trazem muito comportamento de graça; em layouts personalizados de split horizontal ou de overlay, considerar a arrangement view para cuidar do layout em todos os aparelhos suportados; identificar os controles de maior prioridade posicionados manualmente e adotar a Reserved Regions API para o displacement próprio onde for preciso.
10. Para usar a dobradiça além do layout, há outra API que responde ao estado de dobra, tratada na sessão Leverage Multiple Displays and Scenes on iPhone Duo.

Princípios enunciados e o porquê:
- Conteúdo e controles que atravessam a dobra se comportam como uma foto espalhada pelas duas páginas de um livro. O porquê: perto da lombada, partes da imagem ficam difíceis de ver e ela deixa de ser lida como uma imagem contínua.
- Na tela interna, se o visor da câmera FaceTime é central na experiência, manter conteúdo e controles importantes fora dessa área (a fala não dá um porquê além disso).
- Displacement ajusta o frame dos elementos existentes conforme o espaço disponível. O porquê: manter o conteúdo importante visível, alcançável e desobstruído, mesmo com o aparelho parcialmente dobrado.
- Escolher o escopo que combina com o conteúdo: um elemento que se adapta de forma independente se move sozinho; elementos que funcionam juntos se movem juntos. O porquê: preservar a relação entre eles.
- Cuidado com movimento excessivo. O porquê: afastar muito um elemento de sua origem enfraquece a relação visual entre os dois.
- Conteúdo de rolagem contínua (artigos, feeds, documentos e listas) não se desloca. O porquê: essas experiências já se adaptam pela rolagem, e movê-las entre as regiões pode interromper a continuidade.
- O propósito do conteúdo decide para onde ele vai, e esse lugar pode mudar conforme o aparelho é usado.
- Com o aparelho dobrado como livro, alertas vão para o lado trailing. O porquê: ficam mais perto de onde vão aparecer quando o aparelho fechar e a experiência continuar na tela externa.
- Com o aparelho apoiado na mesa, a região de cima serve para conteúdo que ganha com visibilidade à distância, e a de baixo para controles interativos. O porquê: o alerta continua fácil de encontrar em cima, e embaixo os elementos tocáveis têm uma superfície mais estável para o toque.
- Quando várias regiões servem, priorizar o contextual, como no iPhone a busca focada fica sobre o teclado (a fala dá o exemplo, não uma razão separada).
- Action sheets, alerts, menus e popovers são experiências contextuais leves que podem aparecer sobre uma reserved region; o objetivo principal é mantê-los totalmente visíveis, e o sistema os reposiciona automaticamente.
- O que todos os exemplos têm em comum é mover, redimensionar ou reorganizar o que já existe; manter conteúdo, funcionalidade e layouts disponíveis. O porquê: as pessoas devem ter acesso à experiência completa, seja qual for a forma como usam o iPhone Duo.
- Regiões inativas servem para decisões de alto nível sobre o app, como preferir número par de colunas em grids quando há uma division region, ativa ou não (a fala não dá o porquê).
- Ao escolher um arrangement, seguir primeiro os padrões que o app já usa. O porquê: HStack e VStack se traduzem naturalmente no split, e ZStack no overlay, com suporte embutido ao iPhone Duo.
- Sem padrão existente, usar overlay quando há relação clara de primeiro plano e fundo entre as views. O porquê, no exemplo dado: como o conteúdo de fundo pode ser rolado por cima do overlay, não há problema em ele ficar parcialmente encoberto às vezes.
- Usar split quando a relação é de principal e detalhe. O porquê: é importante que nenhuma das duas views fique encoberta.
- Não colocar contêineres de navegação, como Navigation Split View, dentro de uma arrangement view. O porquê: arrangement views não fornecem infraestrutura de navegação.
- Não colocar arrangement views dentro de List e Scroll View. O porquê dado é apenas a natureza dessas views roláveis.
- Layouts adaptativos devem mover, redimensionar e adaptar só quando isso torna a experiência melhor, para o app parecer pensado para cada pose.

Técnicas concretas de construção de interface, com números exatos quando falados:
- Números ditos: split 50/50 das colunas no Reminders; a division region da dobra, com o aparelho aberto e plano, fica inativa e com largura zero; arrangements fornecidos pelo sistema disponíveis no iOS 27.1; arrangement organiza duas views. A fala não dá valores de pontos, margens ou durações.
- Tela externa: câmera sempre presente; system toolbars e tab bars dispostas na vertical dentro da nova safe area (remete à sessão Raise the Bar with iPhone Duo).
- Deslocamento básico: um elemento centralizado com o aparelho aberto passa, ao dobrar, para a região que atende seu propósito.
- Menu de contexto: ao selecionar uma foto num álbum, em vez de centralizar o menu na região trailing, foto e menu se movem juntos e se alinham em volta da dobra.
- Busca: com o aparelho aberto, o campo aproveita o espaço extra; ao dobrar, largura e posição se adaptam para ficar sobre a view que está sendo buscada.
- Split view do sistema: mantém as duas colunas visíveis ajustando a largura e posicionando-as num split 50/50.
- Grid personalizado: preservar as margens externas e aumentar o espaçamento em volta da dobradiça, mantendo cada contêiner dentro de sua região, para que todos os itens do grid continuem interativos ao dobrar.
- Reserved regions em SwiftUI: consultar com um geometry proxy vindo de um geometry reader ou do "non-geometry change modifier" (termo incerto na transcrição automática), usando o novo método reserved region do geometry proxy para obter as regiões da view.
- Reserved regions em UIKit: método reserved region disponível em UIView.
- A propriedade frame de uma reserved region permite incorporá-la ao layout próprio.
- Estado: uma região pode estar ativa ou inativa; por padrão só as ativas são retornadas, e as inativas são obtidas com a opção de consulta include inactive do método reserved region.
- Division reserved region: representa a dobra, porque divide uma área maior em várias menores; só fica ativa quando o aparelho está dobrado.
- Occlusion region: não divide áreas, oclui; funciona como frames menores dentro dos bounds da view. A câmera FaceTime é uma occlusion region, consultada passando o tipo occlusion ao método reserved region; fica ativa quando a câmera está ativa.
- Componentes do sistema que se adaptam à dobra: contêineres de navegação como navigation stacks, navigation split views e "tap views" (termo incerto na transcrição automática); contêineres de conteúdo como List e Scroll View.
- Arrangements: contêineres de layout situados entre os de navegação e os de conteúdo, que organizam duas views segundo um conjunto de regras. As entradas consideradas são a size class horizontal e vertical, a proporção largura sobre altura e a presença de division regions ativas; as saídas são se a view aparece e, se aparece, qual o seu frame. Essa função de entradas para saídas é o arrangement.
- SwiftUI: adicionar uma arrangement view dentro do navigation stack, passando uma view primária e uma secundária.
- UIKit: usar UIArrangementViewController como root view controller do UINavigationController e configurar os view controllers primário e secundário.
- Estilo: configurado com o modificador arrangement view style; o padrão é split.
- Split arrangement: divide os bounds entre a view primária e a secundária; por padrão divide na horizontal quando a view é mais larga que alta e na vertical quando é mais alta que larga.
- Restringir eixos: método axes do split arrangement style. Se o split não pode dividir no eixo primário, a arrangement view mostra só uma view; no exemplo, com a view mais alta que larga e divisão só horizontal, aparece apenas o player.
- UIKit para o mesmo caso: método update arrangement do UIArrangementViewController com o tipo UI split arrangement configurado com eixo horizontal.
- Overlay arrangement: ao contrário do split, que prefere lado a lado, prefere posicionar o conteúdo uma view acima ou abaixo da outra; ao dobrar o aparelho, passa a preferir a primária e a secundária lado a lado.
- Z-index do overlay em SwiftUI: propriedade de ambiente overlay arrangement Z-index, que muda conforme o aparelho é dobrado e desdobrado; no exemplo, usada para alternar entre a versão recolhida e a expandida da view up next.
- Z-index do overlay em UIKit: método StateForViewPlacement do UIArrangementViewController e propriedade Z-index do estado retornado.

Exemplos citados:
- Controles de janela do iPadOS: exemplo de área a que os layouts já se adaptam, como devem ser tratadas as reserved regions.
- Livro com uma foto espalhada pelas duas páginas: mostra por que conteúdo que atravessa a dobra perde leitura.
- Álbum de fotos com menu de contexto: elementos que funcionam juntos se movem juntos e se alinham em volta da dobra.
- Alerta na pose de livro (lado trailing) e na pose apoiada na mesa (região de cima): o destino depende do uso do aparelho.
- Controles de mídia na região de baixo com o aparelho na mesa: controles tocáveis ganham superfície estável.
- Campo de busca no iPhone e no iPhone Duo: priorizar o contextual.
- Reminders: split view do sistema ajustado para 50/50.
- Design de fitness em grid: margens externas preservadas e espaçamento maior em volta da dobradiça.
- Grid com número par de colunas quando há division region: uso de regiões inativas para decisões de alto nível.
- App Podcasts no iPad e no iPhone Duo: a transcrição divide o layout ao meio; ao escondê-la no iPhone Duo dobrado, a view now playing não volta ao centro como no iPad e fica restrita à região esquerda definida pela dobra, mantendo os controles alcançáveis e desobstruídos; com o aparelho girado para retrato, não há split e a transcrição aparece inline. Também é o exemplo de relação principal e detalhe que pede split.
- App de notas de áudio do Harry, com player e up next: demonstra split com eixo restrito, overlay com estado recolhido e Z-index; a resposta final é split, porque a lista up next detalha o estado de reprodução em vez de ser fundo do player. Em um trecho a fala chama o app de "Audio Node app" (termo incerto na transcrição automática).
- Accessibility Reader: controles em primeiro plano e conteúdo legível ao fundo, caso de overlay.
- Sessões citadas: Raise the Bar with iPhone Duo e Leverage Multiple Displays and Scenes on iPhone Duo.

Citações:
"great design for iPhone Duo hinges on knowing when to adapt."
"Adaptive layouts help your app feel thoughtfully designed for every pose."
