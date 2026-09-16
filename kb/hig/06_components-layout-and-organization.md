# Components / Layout and organization

## Boxes (slug: boxes)

O que governa: como agrupar visualmente informações e componentes relacionados dentro de uma borda ou fundo distinto, com título opcional.

Por que: uma box comunica que seu conteúdo pertence a um mesmo grupo lógico. Isso só funciona enquanto a box permanece pequena em relação ao contêiner que a envolve; se ela se aproxima do tamanho da janela ou da tela inteira, perde a força de separar o conteúdo e passa a atravancar o resto da interface. A borda de uma box já é, por si só, um elemento visual forte, então aninhar boxes dentro de boxes para marcar subgrupos deixa a interface carregada; preferir padding e alinhamento para comunicar subdivisões internas.

Faça e evite:
Prefira manter a box pequena em relação à view que a contém.
Use padding e alinhamento para expressar subagrupamentos em vez de boxes aninhadas.
Forneça um título curto se ele ajudar a esclarecer o conteúdo da box, já que a aparência sozinha às vezes não basta, e o título também ajuda usuários de VoiceOver a prever o que vão encontrar.
Se usar título, escreva uma frase breve com capitalização estilo frase (sentence-style) e evite pontuação final, exceto em painel de configurações, onde se acrescenta dois-pontos ao título.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão.

Diferenças por plataforma: sem considerações adicionais para visionOS. Não suportado em tvOS nem watchOS. Em iOS e iPadOS, a box usa por padrão as cores de fundo secondary e tertiary. Em macOS, o título da box aparece por padrão acima dela.

Ligações com outros artigos: Layout.

<!-- visual:boxes -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0183), código conferido; sem vídeo.
- A box é desenhada como retângulo de cantos arredondados em gradiente de laranja para vermelho rosado, com um retângulo interno tracejado marcando a área do conteúdo (img 0183).
- O conteúdo interno simula uma lista de propriedades: barras horizontais cinza escuras de comprimento variável em duas colunas, a da esquerda estreita como rótulo e a da direita larga como valor (img 0183).
- Setas duplas vermelhas cotam quatro distâncias, acima e abaixo do bloco interno até as bordas superior e inferior e à esquerda e à direita até a borda externa, mostrando padding simétrico e margem constante nos quatro lados (img 0183).
- Nenhum número é impresso: a margem constante funciona como unidade de medida visual, sem grade numérica nem medida escrita (img 0183).
<!-- /visual:boxes -->

## Collections (slug: collections)

O que governa: como apresentar um conjunto ordenado de conteúdo, tipicamente baseado em imagens, em um layout customizável e altamente visual.

Por que: collections existem para exibir conteúdo visual de forma eficiente e é importante manter o layout padrão (linha horizontal ou grade) porque é isso que as pessoas já esperam; um layout customizado pode confundir ou chamar atenção indevida para si mesmo em vez do conteúdo. A facilidade de escolher um item também é central: se for difícil alcançar um item, a pessoa se frustra e perde o interesse antes de chegar ao que queria.

Faça e evite:
Use o layout padrão de linha ou grade sempre que possível; evite layout customizado que confunda.
Considere usar uma tabela em vez de uma collection para texto, já que informação textual é mais simples e eficiente de digerir em lista rolável.
Facilite a escolha de um item, com padding adequado ao redor das imagens para que efeitos de foco ou hover fiquem visíveis e o conteúdo não se sobreponha.
Adicione interações customizadas quando necessário; por padrão as pessoas tocam para selecionar, tocam e seguram para editar, e deslizam para rolar.
Considere usar animações para dar feedback ao inserir, excluir ou reordenar itens; collections suportam animações padrão para essas ações, além de permitirem animações customizadas.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão.

Diferenças por plataforma: sem considerações adicionais para macOS, tvOS ou visionOS. Não suportado em watchOS. Em iOS e iPadOS, use cautela ao fazer mudanças dinâmicas de layout: evite alterar o layout enquanto as pessoas estão vendo e interagindo com ele, a menos que seja resposta a uma ação explícita.

Ligações com outros artigos: Lists and tables, Image views, Layout.

<!-- visual:collections -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0252), código conferido; sem vídeo.
- Oito ícones idênticos de imagem, moldura arredondada com círculo de sol e montanha estilizada em rosa claro sobre vermelho, formam uma grade regular de duas fileiras por quatro colunas sobre degradê de laranja para vermelho rosado, conforme a descrição oficial (img 0252).
- Setas vermelhas de medida marcam a margem externa: acima e abaixo do bloco de ícones até a borda do contêiner, e à esquerda e à direita do bloco até a borda (img 0252).
- Duas marcas menores dentro da grade cotam o espaçamento entre células, uma horizontal entre a terceira e a quarta imagem da fileira de cima e uma vertical entre a terceira imagem de cima e a de baixo (img 0252).
- O vocabulário de medida é o mesmo que as notas apontam em boxes e buttons, setas bidirecionais sem números, aqui aplicado para mostrar a coleção como grade com espaçamento consistente entre itens (img 0252).
<!-- /visual:collections -->

## Column views (slug: column-views)

O que governa: um column view (também chamado de browser) permite navegar uma hierarquia de dados usando uma série de colunas verticais, onde cada coluna representa um nível da hierarquia.

Por que: esse formato serve bem quando a hierarquia é profunda e as pessoas tendem a navegar para frente e para trás com frequência entre níveis, sem precisar dos recursos de ordenação que uma tabela oferece. Mostrar a raiz da hierarquia sempre na primeira coluna dá às pessoas um ponto de partida consistente para recomeçar a navegação.

Faça e evite:
Considere usar column view quando a hierarquia é profunda, a navegação entre níveis é frequente, e não há necessidade de ordenação (sorting) como em uma tabela.
Mostre o nível raiz da hierarquia de dados na primeira coluna.
Considere mostrar informações sobre o item selecionado quando não há itens aninhados a exibir, como o Finder faz com uma prévia e dados como data de criação, modificação, tipo e tamanho.
Deixe as pessoas redimensionarem as colunas, especialmente importante quando nomes de itens longos não cabem na largura padrão.

Dentro de uma coluna, um item pai que contém filhos é marcado com um ícone de triângulo; ao selecionar o pai, a próxima coluna mostra seus filhos, e a navegação continua até um item sem filhos.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão.

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS, visionOS ou watchOS (column view é exclusivo de macOS). Uma nota no artigo recomenda que, para apresentar conteúdo hierárquico em iPadOS ou visionOS, considere-se usar Split views em vez de column view.

Ligações com outros artigos: Lists and tables, Outline views, Split views.

<!-- visual:column-views -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0342), código conferido; sem vídeo e sem versão escura registrada.
- A column view é desenhada como três colunas lado a lado separadas por linhas verticais finas, tingidas em vermelho e rosa sobre fundo em degradê laranja avermelhado (img 0342).
- A primeira coluna lista três pastas, cada uma com ícone de pasta à esquerda e chevron à direita indicando que abre a coluna seguinte; a pasta A aparece selecionada com fundo apenas levemente mais claro (img 0342).
- A segunda coluna lista cinco imagens com miniatura à esquerda; a imagem B aparece com fundo vermelho sólido, contraste bem mais forte que o destaque da primeira coluna (img 0342).
- A seleção usa dois níveis de destaque ao mesmo tempo: fraco para a coluna cuja seleção já avançou para a próxima e sólido para o item com o foco ativo, o que torna visível a navegação em cascata de coluna em coluna (img 0342).
- A largura das colunas cresce da esquerda para a direita, e a última, a mais larga, não é lista, e sim painel de detalhes do item selecionado (img 0342).
- O painel de detalhes empilha a informação por importância: miniatura grande, nome do arquivo em negrito e maior que os nomes de item em peso regular, linha curta de formato e tamanho, e depois uma seção Information com pares de rótulo e valor alinhados em colunas, criação e modificação, separados por divisória fina (img 0342).
Divergências registradas: a descrição oficial fala só genericamente de três colunas com pastas, imagens e informação de arquivo, sem os dois níveis de destaque nem a cascata que a imagem mostra.
<!-- /visual:column-views -->

## Disclosure controls (slug: disclosure-controls)

O que governa: controles que revelam e escondem informação e funcionalidade associadas a controles ou views específicas, nas variantes disclosure triangle e disclosure button.

Por que: esconder detalhes até que sejam relevantes evita sobrecarregar as pessoas com muitas opções detalhadas de uma vez. A recomendação de posicionar os controles mais usados no topo da hierarquia de disclosure, com a funcionalidade mais avançada escondida por padrão, existe para que a informação essencial seja encontrada rapidamente sem exigir que a pessoa abra tudo primeiro.

Faça e evite (disclosure triangles):
Use um disclosure triangle para mostrar e esconder informação e funcionalidade associada a uma view ou lista de itens.
O triângulo aponta para dentro, a partir da borda inicial (leading), quando o conteúdo está escondido, e para baixo quando está visível; clicar ou tocar alterna entre os dois estados e a view expande ou colapsa de acordo.
Forneça um rótulo descritivo ao usar um disclosure triangle, indicando o que está sendo revelado ou escondido, como "Advanced Options".

Faça e evite (disclosure buttons):
Use um disclosure button para mostrar e esconder funcionalidade associada a um controle específico, como no Save sheet do macOS, que expande o diálogo para opções avançadas de navegação.
O botão aponta para baixo quando o conteúdo está escondido e para cima quando está visível; clicar ou tocar alterna o estado e a view expande ou colapsa.
Posicione um disclosure button perto do conteúdo que ele mostra e esconde, estabelecendo uma relação clara entre o controle e as opções expandidas.
Use no máximo um disclosure button em uma única view; múltiplos disclosure buttons adicionam complexidade e podem confundir.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão.

Diferenças por plataforma: sem considerações adicionais para macOS. Não suportado em tvOS nem watchOS. Em iOS, iPadOS e visionOS, disclosure controls estão disponíveis via a view SwiftUI DisclosureGroup.

Ligações com outros artigos: Outline views, Lists and tables, Buttons. Há também um vídeo relacionado citado ("Stacks, Grids, and Outlines in SwiftUI").

<!-- visual:disclosure-controls -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas (img 0464 a 0468), códigos conferidos; sem vídeo.
- Par de estados do disclosure button: dois botões quadrados brancos lado a lado, rotulados Collapsed e Expanded, com chevron para baixo no primeiro e para cima no segundo; só sob o expandido aparece um retângulo vermelho vazio maior, representando o painel de conteúdo revelado (img 0464).
- Lista em estilo Finder, toda colapsada: três linhas de pasta com ícone azul e, à esquerda do ícone, um triângulo apontando para a direita, sobre fundos alternados claro, cinza claro e claro (img 0465).
- A mesma lista com a pasta do meio expandida: o triângulo dela passa a apontar para baixo e abaixo surgem três linhas indentadas, com ícones de pasta menores e triângulos próprios para a direita, enquanto as pastas vizinhas continuam colapsadas (img 0466, em sequência a 0465).
- O diálogo de salvar do macOS no estado colapsado é compacto: campo de nome, campo de tags vazio, linha Where com seletor de pasta e o disclosure button de chevron para baixo logo à direita desse seletor, mais Cancel e Save, sem navegador de arquivos (img 0467).
- Depois do clique, a mesma janela cresce na vertical e ganha barra lateral com Shared, Favorites e Locations, navegador de colunas com a pasta selecionada, setas de voltar e avançar, seletores de visualização, campo de busca e botão New Folder no rodapé, sem mudar o campo de nome no topo (img 0468, em sequência a 0467).
- Os dois controles são demonstrados por pares de estado, lado a lado ou em sequência: o triângulo muda de direção e o conteúdo revelado entra indentado na própria lista, enquanto o botão inverte o chevron e, no diálogo de salvar, faz a mesma janela crescer até mostrar um navegador de arquivos completo (img 0464 a 0468).
<!-- /visual:disclosure-controls -->

## Labels (slug: labels)

O que governa: um label é um texto estático que as pessoas podem ler e frequentemente copiar, mas não editar; aparece em botões, itens de menu e views para ajudar a entender o contexto atual e o que se pode fazer a seguir.

Por que: a escolha entre label, text field e text view depende do volume de texto e da necessidade de edição, o que orienta a pessoa a usar o componente certo para a quantidade e a editabilidade do conteúdo. As quatro cores de label do sistema existem para comunicar níveis relativos de importância visual do texto de forma consistente em toda a plataforma.

Faça e evite:
Use um label para exibir uma pequena quantidade de texto que não precisa ser editado; use um text field se precisar editar pouco texto, e um text view se precisar exibir (e opcionalmente editar) uma grande quantidade de texto.
Prefira fontes do sistema; um label pode exibir texto plano ou estilizado e suporta Dynamic Type por padrão (onde disponível); ao ajustar o estilo ou usar fontes customizadas, garanta que o texto permaneça legível.
Use as cores de label fornecidas pelo sistema para comunicar importância relativa.
Torne selecionável o texto de um label que contenha informação útil, como uma mensagem de erro, uma localização ou um endereço IP, para que a pessoa possa copiar e colar em outro lugar.

Especificações exatas: o artigo define quatro cores de label do sistema e seus nomes de API por plataforma.
| Cor do sistema | Uso de exemplo | iOS, iPadOS, tvOS, visionOS | macOS |
| Label | Informação primária | label | labelColor |
| Secondary label | Um subtítulo ou texto suplementar | secondaryLabel | secondaryLabelColor |
| Tertiary label | Texto que descreve um item ou comportamento indisponível | tertiaryLabel | tertiaryLabelColor |
| Quaternary label | Texto de marca d'água (watermark) | quaternaryLabel | quaternaryLabelColor |

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, tvOS ou visionOS. Em macOS, para exibir texto não editável em um label, usa-se a propriedade isEditable de NSTextField. Em watchOS, componentes de texto de data e hora exibem a data atual, a hora atual, ou uma combinação das duas, com vários formatos, calendários e fusos horários configuráveis; um componente de timer de contagem regressiva exibe uma contagem precisa (regressiva ou progressiva) em vários formatos; quando se usam os componentes de data e timer fornecidos pelo sistema, o watchOS ajusta automaticamente a apresentação do label ao espaço disponível e atualiza o conteúdo sem input adicional do app. O artigo também sugere considerar componentes de data e timer em complications.

Diferenças por plataforma, registro histórico: o log de mudanças do artigo registra uma atualização em 5 de junho de 2023 para refletir mudanças do watchOS 10.

Ligações com outros artigos: Text fields, Text views, e, dentro do próprio texto, Color e Complications.

<!-- visual:labels -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0676 a 0678), código conferido; sem vídeo.
- A capa troca o esboço com grade de guias por um diagrama de especificação: a palavra "Label" centralizada, grande e em negrito, dentro de uma caixa pontilhada que marca sua área, sobre degradê de laranja para rosa (img 0676).
- Setas vermelhas cotam a caixa delimitadora do texto: uma vertical acima e abaixo, uma horizontal atravessando toda a largura do cartão e uma marca vertical à direita da palavra (img 0676).
- Abaixo da palavra, a anotação nomeia os atributos tipográficos e de cor, "System Font, Body (Emphasized)" e "Primary Text Color" (img 0676).
- No watchOS, o label de data e hora é um retângulo preto de cantos arredondados, sem moldura de relógio, com texto branco: a data encostada na borda inicial à esquerda e a hora na borda final à direita, na mesma linha (img 0677).
- O label de cronômetro usa a mesma forma preta arredondada, menor e mais estreita, com um único valor numérico grande centralizado (img 0678).
- Os dois exemplos de watchOS mantêm o mesmo contêiner e variam só conteúdo e alinhamento: dois valores em bordas opostas contra um valor único ao centro (img 0677 e 0678).
Divergências registradas: a legenda oficial fala de um rótulo de texto estilizado tingido de vermelho, mas a imagem é, na prática, um diagrama de medidas e tipografia (img 0676).
<!-- /visual:labels -->

## Lists and tables (slug: lists-and-tables)

O que governa: listas e tabelas apresentam dados em uma ou mais colunas de linhas (rows), podendo representar dados organizados em grupos ou hierarquias, e suportando seleção, adição, remoção e reordenação.

Por que: o formato baseado em linhas é especialmente adequado para tornar texto fácil de escanear e ler; por isso o texto recomenda preferir listas e tabelas para conteúdo textual e usar uma collection quando os itens variam muito de tamanho ou há muitas imagens. A escolha de estilo de tabela ou linha deve coordenar com o tipo de dado e a plataforma, porque diferentes estilos comunicam agrupamento, hierarquia ou experiências específicas de cada plataforma.

Faça e evite (geral):
Prefira exibir texto em uma lista ou tabela; para itens que variam muito de tamanho ou muitas imagens, considere uma collection.
Deixe as pessoas editarem uma tabela quando fizer sentido; elas apreciam poder reordenar uma lista mesmo sem poder adicionar ou remover itens. Em iOS e iPadOS, é preciso entrar em um modo de edição antes de selecionar itens da tabela.
Forneça feedback apropriado ao selecionar um item de lista: uma tabela que ajuda a navegar por uma hierarquia costuma destacar persistentemente a linha selecionada, enquanto uma tabela de opções costuma destacar a linha brevemente antes de adicionar uma imagem, como um checkmark, indicando seleção.

Faça e evite (conteúdo):
Mantenha o texto do item sucinto para que o conteúdo da linha seja confortável de ler, minimizando truncamento e quebra de linha.
Considere formas de preservar a legibilidade de texto que poderia ser cortado ou truncado; às vezes uma reticência (ellipsis) no meio do texto ajuda a distinguir o item porque preserva início e fim do conteúdo.
Use cabeçalhos de coluna descritivos em tabelas multicoluna, com substantivos ou frases nominais curtas em capitalização estilo título (title-style), sem pontuação final; se não houver cabeçalho de coluna em uma tabela de coluna única, use um label ou header para dar contexto.

Faça e evite (estilo):
Escolha um estilo de tabela ou lista que coordene com os dados e a plataforma.
Escolha um estilo de linha adequado à informação a exibir, por exemplo uma pequena imagem na borda inicial seguida de um label explicativo breve.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão; menciona nomes de estilos (grouped, elliptical, bordered) sem valores numéricos associados.

Diferenças por plataforma:
iOS, iPadOS, visionOS: use um info button (chamado detail disclosure button quando aparece em uma linha de lista) apenas para revelar mais informação sobre o conteúdo de uma linha; ele não suporta navegação por uma tabela ou lista hierárquica. Para permitir navegar para as subviews de uma linha, use um disclosure indicator accessory control. Evite adicionar um índice (index) a uma tabela que exibe controles, como disclosure indicators, na borda final das linhas, porque tanto o índice quanto esses elementos ficam do lado final e pode ser difícil usar um sem ativar o outro.
macOS: quando agregar valor, deixe que as pessoas cliquem em um cabeçalho de coluna para ordenar a tabela por essa coluna; se clicarem no cabeçalho de uma coluna já ordenada, reordene na direção oposta. Deixe redimensionar colunas. Considere usar cores de linha alternadas em tabela multicoluna para ajudar a rastrear valores entre colunas, especialmente em tabelas largas. Use um outline view em vez de um table view para apresentar dados hierárquicos, já que o outline view se parece com um table view mas inclui disclosure triangles para expor níveis aninhados.
tvOS: confirme que imagens próximas a uma tabela continuam com boa aparência já que cada linha em foco aumenta ligeiramente de tamanho e destaca; os cantos de uma linha focada também podem ficar arredondados, o que pode afetar imagens nas laterais; não adicione máscaras próprias para arredondar cantos.
watchOS: quando possível, limite o número de linhas, já que listas curtas são mais fáceis de escanear, mas às vezes as pessoas esperam ver uma lista longa (o exemplo dado é inscrição em muitos podcasts); ajude listando os itens mais relevantes e provendo uma forma de ver mais. Restrinja a extensão das detail views se quiser suportar navegação vertical paginada, já que essa navegação só funciona quando as detail views são curtas; se elas rolam, a navegação paginada vertical entre elas deixa de funcionar.

Registro histórico do artigo: log de mudanças em 21 de junho de 2023 (atualizado para incluir orientação para visionOS) e 5 de junho de 2023 (atualizado para refletir mudanças do watchOS 10).

Ligações com outros artigos: Collections, Outline views, Layout, e dentro do texto, Search fields.

<!-- visual:lists-and-tables -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_lists-and-tables, folha 0001), códigos conferidos; sem vídeo.
- A abertura não usa esboço geométrico anotado: mostra direto uma tabela agrupada de exemplo, tingida de vermelho e laranja, com texto de cabeçalho acima do cartão, três linhas dentro dele e texto de rodapé abaixo (img 0697).
- Cada linha da tabela de abertura leva um chevron na borda final e é separada da seguinte por um divisor fino; cabeçalho e rodapé ficam fora do cartão, não dentro dele (img 0697).
- A lista agrupada é construída como um cartão cinza claro de cantos arredondados que contém um cartão branco interno, com as linhas separadas por divisores finos (img 0698, img 0699).
- Para revelar informação sem navegar, cada linha traz o título à esquerda e um ícone circular de "i" em azul na borda final (img 0698).
- Para navegar ao próximo nível, a linha troca o "i" por um chevron que aponta para a direita, precedido de um texto secundário cinza de valor ("Detail"), com o título em negrito à esquerda (img 0699).
- O par img 0698 e img 0699 mantém a mesma estrutura de linha e muda só o elemento da borda final, o que isola visualmente a diferença entre botão de informação e indicador de navegação.
- A hierarquia tipográfica da linha de navegação é título em negrito à esquerda e valor secundário em cinza à direita, junto do chevron (img 0699).
Divergências registradas: em img 0699 aparece o texto secundário cinza "Detail" antes do chevron, que a descrição oficial não menciona (ela cita só o chevron na borda final).
<!-- /visual:lists-and-tables -->

## Lockups (slug: lockups)

O que governa: lockups combinam múltiplas views separadas (um content view, um header e um footer) em uma única unidade interativa, usada em tvOS nas variantes cards, caption buttons, monograms e posters.

Por que: header, footer e content view expandem e contraem juntos quando o lockup ganha foco, então o espaçamento entre lockups precisa considerar esse crescimento para não sobrepor ou deslocar outros lockups. Manter tamanhos consistentes dentro de uma linha ou grupo torna o conjunto de botões ou imagens de conteúdo mais visualmente agradável.

Faça e evite:
Deixe espaço adequado entre lockups, já que um lockup em foco expande de tamanho.
Use tamanhos de lockup consistentes dentro de uma linha ou grupo.
Nos caption buttons, garanta que ao ganhar foco eles se inclinem (tilt) acompanhando o movimento do swipe: quando alinhados verticalmente, inclinam para cima e para baixo; quando alinhados horizontalmente, inclinam para os lados; quando dispostos em grade, inclinam nas duas direções.
Nos monograms, prefira imagens a iniciais, já que uma imagem de pessoa cria uma conexão mais íntima do que texto; se a imagem não estiver disponível, aparecem as iniciais da pessoa em seu lugar.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão.

Diferenças por plataforma: lockups não são suportados em iOS, iPadOS, macOS, visionOS ou watchOS; são um componente exclusivo de tvOS.

Ligações com outros artigos: Designing for tvOS, Layout, e dentro do texto, Image views.

<!-- visual:lockups -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (hig-img_lockups, folhas 0001 e 0002), códigos conferidos; sem vídeo.
- A abertura define o lockup como um bloco empilhado de ícone circular, linha de título grande em negrito e linha de nota menor, com retângulos tracejados demarcando cada elemento, uma seta dupla medindo a largura do círculo e uma seta vertical medindo a altura do bloco inteiro (img 0733).
- A hierarquia tipográfica anotada no lockup é de duas linhas com papéis distintos, headline acima e footnote abaixo, em tamanhos claramente diferentes (img 0733).
- O foco em tvOS é sinalizado pelo mesmo contraste: o item focado fica branco e se destaca dos vizinhos cinza claro (img 0734, img 0735, img 0736, img 0737, img 0738); ele também ganha sombra em img 0734, img 0735, img 0737 e img 0738, e aparece maior que os vizinhos em img 0734, img 0737 e img 0738.
- O espaçamento entre lockups aparece como faixas verticais vazias, destacadas em rosa, entre colunas de conteúdo, reservando a folga para o item crescer sem encostar nos vizinhos (img 0734).
- O card em foco mostra a divisão em header, corpo e footer com um exemplo de avaliação (nota e cinco estrelas, quatro preenchidas em amarelo) sobre linhas de texto placeholder, destacado em branco numa fileira de cards cinza (img 0735).
- O caption button em foco ganha uma leve rotação para o lado, coerente com a fileira horizontal, enquanto os outros três botões ficam retos e cinza (img 0736).
- No monograma em foco, o círculo cresce, recebe sombra e um ícone de pessoa mais nítido, e só ele exibe as duas linhas de legenda, título e subtítulo; os monogramas vizinhos ficam menores e sem texto legível (img 0737).
- O poster é uma imagem vertical com rótulo abaixo, organizado em fileira sob uma faixa de cabeçalho perto da borda inferior da tela; o poster focado sobe de camada e aumenta de tamanho (img 0738).
Divergências registradas: a inclinação de foco só aparece na variante horizontal (img 0736); a variante vertical descrita no texto não é mostrada.
<!-- /visual:lockups -->

## Outline views (slug: outline-views)

O que governa: um outline view apresenta dados hierárquicos em uma lista rolável de células organizadas em colunas e linhas, com pelo menos uma coluna contendo os dados hierárquicos primários; contêineres pai têm disclosure triangles que expandem para revelar seus filhos.

Por que: o outline view serve para exibir bem conteúdo baseado em texto e costuma aparecer no lado inicial (leading) de um split view, com conteúdo relacionado do lado oposto; manter a hierarquia exposta em apenas uma coluna, com outras colunas mostrando atributos suplementares, evita confundir a estrutura dos dados. Reter as escolhas de expansão da pessoa evita que ela precise renavegar até o mesmo ponto na próxima vez.

Faça e evite:
Use tabela em vez de outline view para dados não hierárquicos.
Exponha a hierarquia de dados apenas na primeira coluna; outras colunas mostram atributos que se aplicam aos dados hierárquicos.
Use cabeçalhos de coluna descritivos, com substantivos ou frases nominais curtas em capitalização estilo título e sem pontuação, evitando especialmente dois-pontos no final. Sempre forneça cabeçalhos de coluna em outline view multicoluna; em outline view de coluna única sem cabeçalho, use um label ou outro meio de dar contexto.
Considere deixar clicar em cabeçalhos de coluna para ordenar; em outline view ordenável, clicar em um cabeçalho ordena de forma ascendente ou descendente por essa coluna, podendo haver ordenação secundária adicional nos bastidores; clicar no cabeçalho da coluna primária ordena em cada nível da hierarquia (no Finder, por exemplo, todas as pastas de nível superior são ordenadas, depois os itens dentro de cada pasta); clicar de novo no cabeçalho já ordenado inverte a direção.
Deixe redimensionar colunas.
Facilite expandir ou colapsar contêineres aninhados; por exemplo, clicar no disclosure triangle de uma pasta no Finder expande só aquela pasta, mas Option-clique no disclosure triangle expande todas as subpastas.
Retenha as escolhas de expansão da pessoa, armazenando o estado para exibi-lo novamente na próxima vez.
Considere cores de linha alternadas em outline views multicoluna para ajudar a rastrear valores entre colunas.
Deixe editar dados se fizer sentido no app; em uma célula editável, espera-se poder clicar uma vez para editar o conteúdo, podendo responder de forma diferente a um duplo clique (por exemplo, clique único edita o nome de um arquivo, duplo clique abre o arquivo). Considere também permitir reordenar, adicionar e remover linhas.
Considere usar uma reticência centralizada para truncar texto de célula em vez de cortá-lo, já que a reticência no meio preserva início e fim do conteúdo.
Considere oferecer um campo de busca para ajudar a encontrar valores rapidamente em um outline view extenso; janelas com outline view como recurso principal costumam incluir um campo de busca na toolbar.

Especificações exatas: o texto não traz nenhum número, medida ou valor padrão.

Diferenças por plataforma: outline views não são suportados em iOS, iPadOS, tvOS, visionOS ou watchOS (exclusivo de macOS).

Ligações com outros artigos: Column views, Lists and tables, Split views, e dentro do texto, Search fields. Há também um vídeo relacionado citado ("Stacks, Grids, and Outlines in SwiftUI").

<!-- visual:outline-views -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_outline-views, folha 0001), códigos conferidos; sem vídeo.
- O outline view aparece como tabela de quatro colunas com cabeçalhos curtos em substantivo (nome, data de modificação, tamanho, tipo), separados por linhas verticais finas (img 0826).
- Os contêineres pai trazem seta de disclosure: apontando para baixo quando a pasta está expandida e para a direita quando está recolhida, com um ícone de pasta ou de imagem antes de cada nome (img 0826).
- Guias de medida anotadas em vermelho mais escuro marcam o recuo dos filhos em relação à pasta pai: uma guia tracejada vertical e marcadores em forma de colchete na margem esquerda indicando a indentação em dois níveis diferentes (img 0826).
- Uma guia vertical com marcador de altura ao lado das linhas filhas anota a altura de linha (img 0826).
- A linha selecionada recebe preenchimento vermelho sólido com texto branco, invertendo o contraste em relação às linhas não selecionadas (img 0826).
Divergências registradas: a descrição oficial fala só da lista de pastas e imagens em quatro colunas; as anotações de indentação por nível e de altura de linha aparecem apenas na imagem.
<!-- /visual:outline-views -->

## Split views (slug: split-views)

O que governa: um split view gerencia a apresentação de múltiplos painéis (panes) adjacentes de conteúdo, cada um podendo conter tabelas, collections, imagens ou views customizadas, tipicamente para mostrar múltiplos níveis da hierarquia do app ao mesmo tempo e suportar navegação entre eles.

Por que: ao selecionar um item no painel primário, o painel secundário exibe o conteúdo desse item (e um painel terciário pode existir se o secundário também tiver conteúdo adicional). É comum usar split view para exibir uma sidebar de navegação, onde o painel inicial lista os itens ou coleções de nível superior e os painéis secundário e terciário apresentam coleções filhas e detalhes de item. Destacar persistentemente a seleção atual em cada painel que leva à detail view esclarece a relação entre o conteúdo dos vários painéis e ajuda a pessoa a se orientar.

Faça e evite:
Para suportar navegação, destaque persistentemente a seleção atual em cada painel que leva à detail view.
Considere permitir arrastar e soltar (drag and drop) conteúdo entre painéis, já que o split view dá acesso a múltiplos níveis de hierarquia e isso facilita mover conteúdo de uma parte do app para outra.

Especificações exatas: em tvOS, por padrão um split view dedica um terço da largura da tela ao painel primário e dois terços ao painel secundário, podendo também usar layout meio a meio (half-and-half). Em macOS, o divisor no estilo fino (thin divider style) mede um ponto de largura.

Diferenças por plataforma:
iOS: prefira usar split view em ambiente regular, não compacto, já que ele precisa de espaço horizontal para exibir múltiplos painéis; em ambiente compacto, como iPhone em retrato, fica difícil exibir múltiplos painéis sem quebra ou truncamento de texto.
iPadOS: pode incluir dois painéis verticais, como o Mail, ou três painéis verticais, como o Keynote. É preciso considerar larguras de janela estreitas, compactas e intermediárias, já que janelas do iPad são redimensionáveis fluidamente, garantindo que seja possível navegar entre os painéis de forma lógica em cada largura.
macOS: os painéis podem ser arranjados verticalmente, horizontalmente ou ambos, com divisores entre painéis que suportam arrastar para redimensionar. Defina padrões razoáveis para tamanhos mínimo e máximo de painel, mantendo o divisor visível (se um painel fica pequeno demais, o divisor pode parecer sumir e ficar difícil de usar). Considere deixar esconder um painel quando fizer sentido, como no Keynote, que permite esconder o navigator e as presenter notes para reduzir distrações ou ganhar espaço de edição. Forneça múltiplas formas de revelar painéis escondidos, como um botão de toolbar ou um comando de menu com atalho de teclado. Prefira o estilo de divisor fino (thin divider), evitando estilos mais grossos a menos que haja necessidade específica, como quando ambos os lados do divisor usam elementos lineares fortes que dificultam distinguir um divisor fino.
tvOS: um split view pode funcionar bem para filtrar conteúdo, exibindo no painel secundário os resultados da categoria de filtro escolhida no painel primário. Escolha um layout de split view que mantenha os painéis equilibrados (um terço/dois terços por padrão, ou meio a meio). Exiba um único título acima do split view para o conteúdo como um todo, sem títulos separados por painel. Escolha o alinhamento do título conforme o tipo de conteúdo do painel secundário: se ele contém uma coleção de conteúdo, considere centralizar o título na janela; se contém uma única view principal de conteúdo importante, considere posicionar o título acima do painel primário para dar mais espaço ao conteúdo.
visionOS: para exibir informação suplementar, prefira um split view a uma nova janela, já que ele dá acesso conveniente a mais informação sem sair do contexto atual, enquanto abrir uma nova janela pode confundir quem está navegando ou reposicionando conteúdo e exige gerenciar a relação entre views de várias janelas. Se precisar solicitar uma pequena quantidade de informação ou apresentar uma tarefa simples antes de a pessoa voltar à tarefa principal, use um Sheet.
watchOS: o split view exibe a list view ou uma detail view como view de tela cheia. Exiba automaticamente a detail view mais relevante quando o app inicia, mostrando informação pertinente ao local, horário ou ações recentes. Se o app exibe múltiplas páginas de detalhe, coloque as detail views em um Tab view vertical, permitindo usar a Digital Crown para rolar entre as abas; o watchOS também exibe um indicador de página ao lado da Digital Crown, mostrando o número de abas e a selecionada no momento.

Registro histórico do artigo: log de mudanças em 9 de junho de 2025 (adicionadas considerações de plataforma para iOS e iPadOS), 5 de dezembro de 2023 (adicionada orientação para split views em visionOS) e 5 de junho de 2023 (adicionada orientação para split views em watchOS).

Ligações com outros artigos: Sidebars, Tab bars, Layout, e dentro do texto, Drag and drop, Sheets, Tab views.

<!-- visual:split-views -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (hig-img_split-views, folhas 0001 e 0002), códigos conferidos; sem vídeo.
- A abertura nomeia os três papéis de um split view de três colunas, barra lateral, canvas e inspetor, dentro de uma janela com os três círculos de controle no canto superior esquerdo (img 1099).
- As setas de medida da abertura cobrem a largura total da janela e, na base, só as colunas laterais; o canvas central não tem seta própria e preenche o espaço que sobra (img 1099).
- No macOS, a anatomia é diagramada como a tela inteira de um laptop dividida por linhas retas em blocos azul claro, sem sobreposição nem transparência, mudando só a posição dos divisores entre um exemplo e outro (img 1100, img 1101, img 1102).
- Painéis empilhados: uma única linha horizontal separa um painel superior grande de um painel menor na base (img 1100).
- Painéis lado a lado: uma única linha vertical separa um painel esquerdo nitidamente mais estreito de um painel direito mais largo, ou seja, proporção assimétrica (img 1101).
- Arranjo misto: uma coluna estreita à esquerda ocupa toda a altura, e a área da direita é subdividida por uma linha horizontal em painel maior em cima e menor embaixo (img 1102).
- No watchOS, a tela mostra uma lista vertical com título em azul, cabeçalho de seção em branco e três itens separados por traços finos, sobre fundo preto, sem painéis lado a lado (img 1103).
- A navegação entre páginas no relógio é indicada por uma coluna fina de marcas junto à Digital Crown, com um segmento mais alongado e mais claro em destaque, o que sugere um indicador de posição, sem texto nem setas (img 1103).
Divergências registradas: na resolução vista não foi possível confirmar que o segmento destacado da img 1103 corresponde à quinta aba, como afirma a descrição oficial; só se vê um indicador de várias posições com uma em destaque.
<!-- /visual:split-views -->

## Tab views (slug: tab-views)

O que governa: um tab view apresenta múltiplos painéis de conteúdo mutuamente exclusivos na mesma área, entre os quais as pessoas alternam usando um controle em abas (tabbed control).

Por que: a aparência de um tab view sugere fortemente enclausuramento (enclosure), então as pessoas esperam que cada aba mostre conteúdo de alguma forma semelhante ou relacionado ao das outras abas. A preferência por um controle em abas sobre um pop-up button se justifica porque o primeiro exige um único clique ou toque para selecionar (contra dois do pop-up) e apresenta todas as opções na tela ao mesmo tempo, enquanto o pop-up exige clicar para ver as opções.

Faça e evite:
Use um tab view para apresentar áreas de conteúdo estreitamente relacionadas.
Garanta que os controles dentro de um painel afetem apenas o conteúdo desse mesmo painel, já que os painéis são mutuamente exclusivos e devem ser totalmente autocontidos.
Forneça um rótulo para cada aba que descreva o conteúdo do seu painel, em geral com substantivos ou frases nominais curtas (um verbo ou frase verbal curta pode fazer sentido em alguns contextos), usando capitalização estilo título.
Evite usar um pop-up button para alternar entre abas, exceto quando há painéis demais para exibir razoavelmente como abas, caso em que o pop-up pode ser uma alternativa razoável.
Evite fornecer mais de seis abas em um tab view, pois isso pode sobrecarregar e criar problemas de layout; para seis ou mais painéis, considere outra forma de implementar a interface, como apresentar cada aba como opção de view em um menu de pop-up button.

Anatomia: o controle em abas aparece na borda superior da área de conteúdo, podendo ser escondido quando o app alterna entre painéis programaticamente. Quando o controle em abas está escondido, a área de conteúdo pode ser borderless, bezeled ou bordered com uma linha; uma view borderless pode ser sólida ou transparente. Em geral, recua-se (inset) o tab view deixando uma margem de área window-body em todos os lados; é possível estender o tab view até as bordas da janela, mas esse layout é incomum.

Especificações exatas: no máximo seis abas recomendadas em um tab view (acima disso, considerar outra abordagem).

Diferenças por plataforma: não suportado em iOS, iPadOS, tvOS ou visionOS. Em iOS e iPadOS, para funcionalidade similar, considere usar um segmented control. Em watchOS, tab views são exibidos usando page controls.

Registro histórico do artigo: log de mudanças em 5 de junho de 2023 (adicionada orientação para uso de tab views em watchOS).

Ligações com outros artigos: Tab bars, Segmented controls.

<!-- visual:tab-views -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_tab-views, folha 0001), códigos conferidos; sem vídeo.
- A abertura mostra o tab view como um contêiner retangular com cotas de medida nas quatro bordas e um controle segmentado em pílula sobreposto à borda superior, com três abas de rótulo genérico (img 1118).
- A aba ativa é marcada por um fundo mais opaco, não por sublinhado nem por cor de texto (img 1118, img 1119).
- Os divisores entre abas somem ao lado da aba selecionada: há um traço vertical fino entre a segunda e a terceira aba, mas nenhum entre a primeira, que está destacada, e a segunda (img 1118).
- Na janela real de macOS, o controle de três abas fica na borda superior, com a primeira selecionada sobre fundo cinza claro arredondado e o corpo da janela abaixo vazio (img 1119).
- As cotas da abertura são setas verticais no topo e na base e setas horizontais nas duas laterais, tratando o contêiner inteiro como área medida, e não só o controle de abas (img 1118).
- No watchOS não há controle segmentado visível: a página atual é marcada numa coluna vertical de pontos junto à Digital Crown, onde o ponto atual é maior e branco e os demais são menores (img 1120).
- A tela do relógio usa fundo preto com hora e título em azul no alto e corpo vazio, isolando o indicador de páginas como único elemento de navegação (img 1120).
<!-- /visual:tab-views -->

## O que este grupo revela sobre o jeito Apple

A Apple trata layout hierárquico como problema central de macOS e resolve o mesmo problema de três formas distintas conforme o padrão de navegação esperado: column views para ida e volta frequente entre níveis sem precisar ordenar, outline views para dados hierárquicos com múltiplas colunas de atributos e ordenação, e split views para mostrar vários níveis simultaneamente lado a lado (column-views, outline-views, split-views).

Vários componentes de organização (column views, outline views, tab views) são explicitamente exclusivos de macOS ou têm suporte muito restrito fora dele, o que mostra que macOS mantém um vocabulário de densidade de informação que as demais plataformas, otimizadas para toque, não herdam (column-views, outline-views, tab-views).

Repetidamente a documentação recomenda esconder complexidade por padrão e revelar só sob demanda: boxes evitam aninhamento visual, disclosure controls escondem opções avançadas, outline views escondem níveis via disclosure triangles (boxes, disclosure-controls, outline-views).

A reticência centralizada (ellipsis no meio do texto) aparece como solução recorrente para truncamento em pelo menos dois componentes distintos, sinalizando um padrão de interface consolidado e não uma escolha pontual (lists-and-tables, outline-views).

Cores de linha alternadas para facilitar rastrear valores em tabelas largas aparecem como recomendação repetida em três componentes de dados tabulares diferentes, mostrando que é convenção de plataforma, não capricho de app (lists-and-tables, outline-views, split-views, este último quanto à observação equivalente sobre elementos lineares fortes ao lado de divisores).

Estado de navegação (seleção destacada, expansão de containers) deve ser persistido e retomado, não apenas exibido no momento: outline views armazenam escolhas de expansão e split views mantêm a seleção destacada de forma persistente para orientar a pessoa (outline-views, split-views).

Componentes de tvOS (lockups, o comportamento de foco em lists-and-tables, split views em tvOS) compartilham um vocabulário próprio de foco, inclinação (tilt) e expansão ao ganhar destaque, distinto do restante das plataformas, porque a navegação por controle remoto exige indicação visual constante de onde está o foco (lockups, lists-and-tables, split-views).

Vários artigos remetem uns aos outros formando pares de decisão explícitos que a documentação usa para orientar a escolha do componente certo: tabela versus outline view para dados hierárquicos, column view versus split view para navegação hierárquica no iPadOS/visionOS, tab view versus pop-up button quando há muitas opções (lists-and-tables, outline-views, column-views, split-views, tab-views).

A Apple é consistente em pedir capitalização estilo título sem pontuação final para cabeçalhos de coluna e rótulos de aba, e capitalização estilo frase para títulos descritivos como o de uma box, uma distinção de estilo de texto aplicada de forma sistemática entre componentes (boxes, lists-and-tables, outline-views, tab-views).

Regras de limite concreto (número máximo de abas, número mínimo de disclosure buttons por view) aparecem apenas onde a Apple já testou o ponto em que a interface deixa de funcionar bem, e não aparecem em componentes sem esse tipo de risco de excesso, como boxes ou lockups.

## Evidência de leitura

/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/boxes.md, 32 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/collections.md, 30 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/column-views.md, 26 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/disclosure-controls.md, 46 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/labels.md, 52 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/lists-and-tables.md, 63 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/lockups.md, 48 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/outline-views.md, 38 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/split-views.md, 66 linhas lidas, até o fim: sim
/Users/guilhermelannes/Downloads/apple-design-kb/text/hig/tab-views.md, 43 linhas lidas, até o fim: sim
