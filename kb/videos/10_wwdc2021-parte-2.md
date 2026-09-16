# wwdc2021 (parte 2)

## Explore the SF Symbols 3 app (id: wwdc2021_10288, 12.8 min)

- Base: transcrição e 11 de 11 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2021/10288/.
- Tese central: o app SF Symbols acompanha todo o ciclo de design e desenvolvimento, do achar e organizar símbolos até customizá-los e exportá-los para comps e código, cobrindo compatibilidade de plataforma, localização e os novos modos de renderização.

- O processo de design que a Apple descreve: na fala, o apresentador constrói, ao vivo, um app fictício de jogo de cartas para ilustrar o fluxo completo.
  - Cria uma collection (botão "+") para reunir os símbolos do projeto e encontrá-los depois.
  - Busca símbolos por categoria na sidebar (ex.: categoria "Human" para um símbolo de "adicionar jogador") e por palavra-chave na toolbar (buscas citadas: "suit", "stack", "book").
  - Arrasta e solta os símbolos encontrados para dentro da collection.
  - Antes de usar um símbolo, checa compatibilidade de plataforma no information inspector: nome do símbolo, versão do SF Symbols em que apareceu, o iOS correspondente, e se existe um nome antigo (deprecated) para dar suporte a versões de OS mais velhas.
  - Checa localização no mesmo inspector: como o símbolo muda por idioma (caractere no script nativo do usuário) e por direção de leitura (o livro abre de um lado ou de outro conforme LTR ou RTL). Recomenda não fixar um sufixo de localização (como .ar ou .zh) no Xcode e deixar o sistema escolher a representação certa.
  - Usa o rendering inspector para comparar os modos de renderização antes de decidir qual usar.
  - Para criar um símbolo customizado, duplica um símbolo existente como ponto de partida (File > Duplicate as Custom Symbol), renomeia, exporta um SVG de template, edita esse SVG num editor vetorial e arrasta o arquivo editado de volta para atualizar o símbolo no app.
  - Para anotar o símbolo custom nos novos modos de renderização, seleciona partes do desenho e arrasta cada parte para uma layer (Multicolor: define a cor de cada layer; Hierarchical: define layers como Primary e Secondary).
  - Ao final, decide como exportar o símbolo dependendo do destino: comp de design (SF fonts, colando como texto) ou desenho customizado com renderização avançada (Copy Image).

- Princípios enunciados e o porquê:
  - Deixar o sistema escolher a localização e a compatibilidade certa, em vez de fixar manualmente, porque isso tira trabalho repetido do desenvolvedor a cada novo idioma ou OS suportado.
  - Usar SF fonts (copiar como texto) sempre que o símbolo for do sistema e monochrome, porque assim ele fica automaticamente alinhado e com o peso (weight) igual ao do texto ao lado, sem ajuste manual.
  - Reservar o recurso Copy Image para comps de design, e usar o nome do símbolo (não a imagem) ao trabalhar em código, para manter cada ferramenta no papel certo dentro do fluxo de design para desenvolvimento.
  - Para colocar um símbolo custom num asset catalog do Xcode, usar Export Symbol em vez de Copy Image, para não perder recursos que só o símbolo custom completo carrega.

- Técnicas concretas de construção de interface:
  - Catálogo do sistema: mais de 3000 SF Symbols disponíveis nas plataformas Apple.
  - Exemplo de versionamento citado: o nome person.fill.badge.plus está disponível em monochrome desde a versão 2.0 do SF Symbols, correspondente ao iOS 14; o nome deprecated equivalente, person.badge.plus.fill, está disponível desde a versão 1.0, correspondente ao iOS 13.
  - Modos de renderização disponíveis no rendering inspector: Monochrome (uma cor, do sistema ou custom), Multicolor (cores intrínsecas ao significado do símbolo; no exemplo, coração e diamante ficam vermelhos, espada e paus ficam pretos, com ajuste automático para Dark Mode testável pelo Background picker), Hierarchical (novo nesse ano: uma cor com variações de opacidade para dar profundidade) e Palette (novo nesse ano: duas ou três cores especificáveis pelo usuário).
  - Cópia para design: Edit > Copy Symbol (atalho Command-C) cola o símbolo como texto usando as SF fonts. Edit > Copy Image (atalho Option-Command-C) ou Copy Image As... copia uma imagem em PNG ou SVG, com tamanho de ponto e escala de pixel configuráveis; essas configurações permanecem até serem trocadas de novo. Imagens copiadas podem ganhar padding vertical extra para que o centro vertical de vários símbolos alinhe numa linha horizontal.
  - Para código: copiar o nome do símbolo (não a imagem); para asset catalog, usar Export Symbol.

- Exemplos citados (apps, telas, componentes) e o que cada um ensina:
  - App fictício de jogo de cartas: ensina o fluxo ponta a ponta, de buscar símbolos a exportá-los para comp e código.
  - Símbolo de "adicionar jogador" (person.fill.badge.plus / person.badge.plus.fill): ensina como checar compatibilidade de versão de OS e usar nomes deprecated quando necessário.
  - Símbolo de livro para "regras do jogo": ensina localização automática de símbolos (script nativo e direção de leitura) sem esforço extra do desenvolvedor.
  - Símbolo custom "queen of hearts" (criado a partir de crown.fill, renomeado para queen.heart.fill): ensina o fluxo de duplicar, editar em vetor, reimportar e anotar um símbolo custom para os novos modos de renderização.
  - Botão com símbolo de livro + palavra "Rules": ensina o uso de Copy Symbol/colar como texto para manter símbolo e texto alinhados e com peso igual, usando as SF fonts.

- Citações:
  - "There are now over 3000 SF Symbols built into Apple platforms."
  - "Remember that Copy Image is intended to be used when you're making design comps."

<!-- visual:wwdc2021_10288 -->
### O que as imagens mostram
Base: 11 de 11 folhas de quadros vistas, todos os códigos conferidos.

- O app SF Symbols aparece sempre no mesmo layout de três colunas: sidebar com categorias fixas e, abaixo de uma linha divisória, a seção "Library" com as coleções do usuário; grade central de símbolos com legenda sob cada ícone e contador "N Symbols" no cabeçalho; inspetor à direita que alterna entre "No Selection" em cinza centralizado e o detalhe do item selecionado (folha 0001, q0009; folha 0002). A divisão espacial não é narrada na fala, só aparece na tela.
- O inspetor de disponibilidade mostra duas entradas empilhadas para o mesmo desenho: o nome atual com uma linha por modo de renderização e o número de versão alinhado à direita, e abaixo o nome obsoleto marcado com um pequeno triângulo de aviso (folha 0003, q0019). A estrutura visual de duas entradas com ícone de alerta é acréscimo da imagem sobre o que a fala explica.
- O painel "Rendering" troca de conteúdo conforme o modo: em Monochrome há um seletor de cor com amostra quadrada e valor percentual ao lado, em Hierarchical um seletor de cor único, e em Palette surge a lista "Colors" com linhas nomeadas e percentuais próprios (100, 40, 100); em todos existe uma seção "Background" ao final, e o menu suspenso lista as quatro opções empilhadas com marca de seleção na ativa (folha 0004, q0035 e q0036; folha 0005, q0038 a q0040).
- A troca de Monochrome para Multicolor é visível quadro a quadro: os naipes assumem cor própria, coração e ouros em vermelho, paus e espadas em preto, enquanto os demais símbolos da mesma coleção continuam monocromáticos (folha 0004, q0035 para q0036).
- A anotação de camadas de um símbolo customizado aparece como lista vertical "Layers", uma linha por camada com miniatura e nome de cor (folha 0006, q0054). Ao separar o desenho em Hierarchical, a lista passa de uma linha única "Primary" para duas linhas, "Primary" e "Secondary", com a linha ativa em contorno azul (folha 0007, q0059 para q0060).
- Seleção ativa é sempre um contorno quadrado azul ao redor do ícone, e a seleção múltipla troca o inspetor para o rótulo "Multiple Selected" (folha 0002, q0015).
- O fluxo de edição externa é mostrado como alternância entre dois ambientes: editor de vetores com réguas, guias azul e vermelha cruzando o ícone e painel de posição, tamanho, opacidade e sombra; janela de Finder com dois arquivos SVG; e diálogo modal de substituição de template com ícone no topo, texto em negrito, explicação em cinza e os botões "Cancel" e "Replace", este último azul como ação padrão (folha 0006, q0047 a q0051).
- A diferença entre colar como texto e colar como imagem fica registrada em dois quadros distintos: o símbolo do livro e a palavra "Rules" na mesma linha de base, mesma cor azul e peso semelhante, como se fossem caracteres (folha 0008, q0066); e a coroa customizada dentro de uma caixa de seleção com alças num app de design, com campos numéricos de posição, tamanho e opacidade (folha 0009, q0080).
- Os cartões de destaque seguem um padrão fixo: fundo preto, título curto em branco alinhado à esquerda e até duas frases de apoio em corpo menor, sem marcadores (folha 0003, q0025; folha 0008, q0072). Um cartão foge desse padrão, com selo circular verde escrito "NEW" ao lado do título e dois itens marcados por ponto (folha 0010, q0082). Ao fim de blocos temáticos aparece um rodapé de crédito com nome de outra sessão à esquerda e o ano do evento à direita, no último caso separado por linha fina (folha 0008, q0072; folha 0010, q0089).
- A passagem da demonstração para o conceito é feita por dissolução, não por corte seco: a captura do app escurece em etapas, o título do cartão aparece sobreposto e semitransparente sobre a tela ainda visível, chega ao preto total com o texto completo e depois a tela do app reaparece atrás do texto (folha 0003, q0019 a q0027).
- O cartão "When to use Copy Image" organiza quatro ícones coloridos numa fileira horizontal de espaçamento igual, com legendas curtas centralizadas abaixo, sendo que os dois últimos ícones dividem uma legenda só (folha 0010, q0086). No quadro anterior o mesmo cartão existia apenas com o título, sem os ícones.
- A apresentação sobrepõe texto de tópico ao vídeo do apresentador: no início são duas linhas brancas alinhadas à esquerda, sem caixa ou fundo sólido (folha 0001, q0006); mais adiante são três linhas empilhadas à direita do rosto, as já cobertas em cinza-claro e a atual em branco e negrito (folha 0005, q0041 e q0042).
- A localização de um símbolo é exposta no inspetor como lista de sistemas de escrita, com uma linha por item (Latin, Arabic, Hebrew, Hindi, Japanese, Korean, Thai, Chinese), estrutura que a fala não descreve item a item (folha 0002, q0018).
- O fecho é um resumo puramente icônico: uma fileira de ícones isolados em fundo preto, agrupados por tema e sem legenda, trocando de grupo entre quadros, até a tela final com a maçã e "WWDC21" centralizados (folha 0011, q0091 a q0095).

Proporção visual: pelas notas, a maior parte dos quadros é captura do app SF Symbols, cartão de texto preto ou editor externo, com o apresentador entrando em cortes curtos entre blocos, mais tomadas de contexto do laptop físico sobre a mesa (folha 0001, q0008; folha 0006, q0053; folha 0009, q0077).

Divergências ou limites registrados: as notas registram que, na folha 0009, os ícones sobre fundo preto aparecem sem texto de legenda naquele trecho (q0074 e q0075), e que a tomada do laptop visto de trás não tem detalhe legível na tela (folha 0006, q0053).
<!-- /visual:wwdc2021_10288 -->

## The process of inclusive design (id: wwdc2021_10304, 36.6 min)

- Base: transcrição e 26 de 26 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2021/10304/.
- Tese central: inclusão precisa ser considerada desde o começo e ao longo de todo o processo de design e desenvolvimento, guiada por eixos de diversidade e por escuta ativa de perspectivas diferentes das do próprio time, e não tratada como um acréscimo de última hora.

- O processo de design que a Apple descreve, fase a fase:
  - Ideação: cada pessoa do time deveria conseguir responder por que está fazendo aquele app ou jogo, que bem humano ele serve, e como as pessoas ficarão melhor. Perguntar para quem o produto é feito, pensando pelos eixos de diversidade e não só pelos usuários atuais. Desafiar as próprias suposições e ouvir ativamente experiências diferentes das do time.
  - Design: pensar nos extremos de uso, não só na pessoa média. Considerar o impacto emocional, social e físico sobre quem usa o app, perguntando se algum grupo tende a ter experiências mais negativas e se esse grupo já é vulnerável ou desfavorecido. Considerar o impacto do contexto e da localização (cultura, tipo de moradia, ambiente barulhento ou silencioso, conectividade).
  - Desenvolvimento: garantir representação e expertise inclusivas ao longo do desenvolvimento, incluindo explicitamente um grupo diverso nas discussões sobre protótipos e decisões. Planejar acessibilidade e internacionalização desde o início, entendendo as APIs de acessibilidade e localização com antecedência. Controles padrão de UIKit, AppKit ou SwiftUI já implementam os métodos de UIAccessibility e são acessíveis por padrão; controles ou views customizados exigem tempo extra de planejamento para ficarem acessíveis.
  - Teste: buscar um grupo diverso de pessoas para dar feedback real de uso. Testar com tecnologias assistivas e acomodações (VoiceOver, tamanho de texto no máximo, navegação por teclado) para identificar problemas antes que afetem clientes. Ouvir, revisar e priorizar o feedback recebido, inclusive defendendo metas de teste inclusivo como KPIs (indicadores-chave de performance) junto à empresa.
  - Lançamento: quando há prazo fixo, é preciso fazer escolhas difíceis, cortando o lançamento de uma funcionalidade para fazer menos coisas bem para todos. Quando não é possível entregar a melhor experiência para um eixo ou interseção de diversidade, é preciso entender por quê, como e quando isso será resolvido, com um plano e uma data alvo. O lançamento não é um ponto final: reavaliar e evoluir continuamente com base em feedback real após o lançamento.

- Princípios enunciados e o porquê de cada um:
  - Eixos de diversidade como referência para pensar além da própria experiência: classe, cultura, etnia, idioma, educação, crenças políticas, filosóficas e religiosas, raça, gênero, orientação sexual, idade, habilidades, deficiências, ser canhoto ou destro, medidas corporais como altura, e condições ambientais como localização, conectividade de internet e acesso a dispositivos.
  - "Inclusão é uma jornada", não um obstáculo único: mudança é um processo iterativo que exige planejamento, persistência e paciência, porque o benefício (melhorar a qualidade de vida das pessoas) compensa o esforço.
  - Design inclusivo estimula criatividade em vez de limitá-la: restrições ajudam a focar energia nas primeiras decisões dentro de um espaço de problema mais estreito, em vez de forçar todo mundo a aceitar a experiência do "denominador comum".
  - Time diverso não é o mesmo que time empoderado: ter um time diverso não garante um produto inclusivo; o que garante é um time diverso cujas perspectivas realmente entram nas decisões. Daí a recomendação de contratar pensando em "culture add" (o que falta) em vez de "culture fit" (o que já existe).
  - Inclusão não pode ser tratada no fim do processo, do mesmo jeito que segurança ou privacidade: deixar para o final é reativo e normalmente não sobra tempo para corrigir.
  - Interseccionalidade (conceito atribuído à acadêmica de direito Kimberlé Crenshaw): reconhece que pessoas com múltiplas identidades sistemicamente desfavorecidas têm necessidades e experiências únicas, que só aparecem quando se olha para a intersecção dos eixos, não para cada eixo isolado.

- Técnicas concretas de construção de interface, escrita e processo (com números exatos quando falados):
  - Dado citado: pessoas com deficiência são 15% da população mundial, número que cresce com o envelhecimento populacional e condições crônicas de saúde.
  - Exemplo de acessibilidade por reconhecimento: um recurso da Apple para reconhecer objetos e texto físico (sinalização, cartões de visita, envelopes) surgiu com o time restringindo o escopo a poucos objetos e texto, depois expandindo para botões de ação (ligar, mandar mensagem, adicionar aos contatos, copiar número reconhecido).
  - People Detection no app Magnifier: usa a tecnologia LiDAR (laser pulsado que gera um modelo 3D do ambiente ao redor) para informar a distância entre a pessoa e outras pessoas próximas; nasceu como protótipo de conveniência e virou necessidade prática durante a pandemia de COVID-19 para apoiar o distanciamento social de pessoas cegas ou com baixa visão.
  - No iOS 15, a funcionalidade Description do Markup permite escrever descrições de imagem manualmente, que são enviadas junto quando a foto é compartilhada.
  - VoiceOver Recognition image descriptions: modelo de machine learning treinado para gerar descrições de imagem automaticamente em escala. O time descobriu que modelos de ML costumam representar só dois gêneros (feminino e masculino) e decidiu tornar essas descrições automáticas de gênero neutro (exemplo de descrição gerada: pessoa com cabelo cacheado preto, camisa listrada vermelha e branca, em frente a um prédio), reservando a menção a gênero para descrições escritas manualmente por quem conhece a pessoa na foto.
  - Memories (Photos, iOS 15): o time analisou novos temas de memória pelos eixos de vida rural versus urbana, adolescentes versus avós, regional versus global, respondendo para cada tema quem está sendo incluído, quem está sendo excluído e como as pessoas vão se sentir. Passaram a representar mais hobbies (artes marciais, skate, futebol) e expandiram o catálogo internacional de feriados (Natal, Diwali, Ano-novo lunar, Eid al-Fitr, Hanukkah, entre outros).
  - Ainda em Memories, a partir de feedback sobre reencontrar fotos de um ex-parceiro, o time criou a ação "Feature Less" (destacar menos essa pessoa), disponível a partir de uma foto em destaque, dos álbuns de Pessoas, e de uma foto individual; numa segunda iteração, deixou a pessoa escolher entre "destacar menos" ou "nunca mais destacar". Também trocaram o ícone de "joinha para baixo" por um glifo mais neutro, por poder soar como "não gostar da pessoa" em situações como luto.

- Exemplos citados (apps, telas, componentes) e o que cada exemplo ensina:
  - Reconhecimento de objetos e texto para pessoas cegas ou com baixa visão: ensina como uma restrição inicial de escopo pode abrir caminho para uma solução de grande impacto.
  - People Detection (Magnifier, LiDAR): ensina colaboração entre times de acessibilidade e engenharia, e como um contexto real (pandemia) tornou um recurso de conveniência em necessidade.
  - VoiceOver Recognition image descriptions: ensina como investigar representação de machine learning por eixo de diversidade e como parcerias com organizações externas (cegas/baixa visão e LGBTQ+) ajudaram a decidir por descrições de gênero neutro.
  - Memories (fotos e vídeos): ensina técnicas concretas de pesquisa inclusiva (brainstorming multicultural em grupos pequenos e em fusos diferentes, análise por eixos de diversidade, entrevistas individuais para temas sensíveis) e iteração de design a partir de feedback real de usuários.

- Citações:
  - "Inclusive design and development stimulates new creative solutions."
  - "Diverse representation does not guarantee inclusivity will come naturally."

<!-- visual:wwdc2021_10304 -->
### O que as imagens mostram
Base: 26 de 26 folhas de quadros vistas, todos os códigos conferidos.

- A lista de eixos de diversidade é apresentada como grade de vinte ícones brancos sobre preto, quatro linhas de cinco, cada célula com símbolo de traço simples e legenda curta centralizada abaixo, mesmo espaçamento horizontal e vertical, sem bordas nem caixas separando os itens (folha 0002, q0010). A grade se forma item a item antes de ficar completa (folha 0001, q0009) e volta mais tarde no mesmo arranjo de cinco colunas por quatro linhas (folha 0019, q0167 a q0169).
- Há um recurso recorrente de tirar um ou dois ícones de dentro da grade, ampliá-los e deixá-los sozinhos com legenda maior, exatamente no momento em que a fala trata daquele eixo (folha 0002, q0011 para q0012). O mesmo recurso volta para representar interseção, e ali os dois ícones ficam próximos e passam a dividir uma legenda única de três linhas somando as duas condições com um sinal de mais no meio (folha 0013, q0109, depois q0112 e q0113).
- Os mesmos ícones da grade são reciclados como legenda contextual sobre cena filmada real: sobre a imagem de uma família à mesa aparecem, semitransparentes na faixa inferior, ícones brancos pequenos com legendas curtas de contexto (folha 0008, q0070). A fala cita cultura, ambiente, localização e conectividade; é a imagem que mostra o mesmo vocabulário de ícones da grade servindo de anotação sobre a vida real.
- O cartão de texto preto alterna alinhamento à esquerda e à direita conforme o lado em que a apresentadora entra no quadro seguinte, e as frases de apoio se acumulam uma por quadro sem apagar as anteriores (folha 0003, q0021; folha 0004, q0029; folha 0005, q0043 a q0045; folha 0006, q0048). Num bloco de perguntas de pesquisa o contraste cresce a cada quadro, as duas primeiras perguntas em cinza claro e a terceira em branco e negrito (folha 0021, q0184 a q0186).
- A partir da etapa "Ideate" o formato muda: em vez de cartão preto em tela cheia seguido de corte para a apresentadora, o mesmo quadro passa a conter as duas coisas, texto à esquerda crescendo linha a linha e a apresentadora em vídeo ocupando cerca de um terço à direita, sem moldura nem linha divisória, com o nome da etapa em negrito no topo (folha 0007, q0060 a q0063). O formato se repete idêntico em Design e Develop (folha 0008, q0065 a q0068; folha 0009, q0075 a q0077).
- O diagrama do processo muda de forma dentro da narrativa: primeiro uma linha horizontal fina com cinco palavras em fonte cursiva colorida, uma cor por etapa e um ponto colorido marcando a posição de cada uma, depois o mesmo conjunto redesenhado em círculo, seguindo a curvatura do traçado, sem linha nem pontos de marcação (folha 0007, q0055 para q0057).
- Uma pequena seta triangular branca no topo do círculo funciona como marcador de posição atual, e o anel de fato gira entre quadros: numa passagem "Test" está no topo e no quadro seguinte "Release" ocupa esse lugar, com "Test" descendo para a esquerda (folha 0008, q0064; folha 0016, q0141 para q0142).
- Os itens de lista entram por fade: o marcador novo aparece primeiro em opacidade muito baixa, quase ilegível, e só no quadro seguinte fica em branco pleno (folha 0014, q0123 para q0124; folha 0015, q0127 a q0131; folha 0025, q0222 a q0224). A ordem exata de entrada de cada item é informação que só a imagem entrega.
- Capturas de interface do sistema aparecem sempre isoladas, centralizadas em fundo preto ou dentro de uma moldura de aparelho desenhada com notch e barra de status, nunca com uma mão segurando o telefone (folhas 0003, 0010, 0011, 0014, 0018, 0019, 0022, 0023). As cenas filmadas de pessoas, ao contrário, ocupam o quadro inteiro sem fundo preto ao redor (folhas 0004, 0008, 0009).
- O reconhecimento de texto é mostrado em dois estados consecutivos: o viewfinder da Câmera com a placa fotografada e pequenos retângulos amarelos marcando cada trecho reconhecido, e no quadro seguinte um menu de contexto vertical sobre o número de telefone, com seis ações empilhadas, cada uma com ícone à direita (folha 0003, q0026 para q0027).
- A medição de distância é composta por sobreposição: sobre a cena real de uma fila de pessoas surge a moldura semitransparente de um iPhone, contorno branco fino e cantos arredondados, contendo linha pontilhada vertical que vai até a cabeça da pessoa à frente, um rótulo numérico grande junto à base dessa linha, a palavra "End" no canto superior esquerdo e uma barra de progresso fina embaixo. No quadro seguinte a cena de fundo desaparece e resta só essa tela, ampliada e centralizada (folha 0004, q0034 para q0035).
- O fluxo de descrição de imagem aparece encadeado em três telas: a foto no app Fotos com faixa de miniaturas e barra inferior de compartilhar, favoritar, informação e excluir; a mesma foto no Markup com menu vertical listando Description, Text, Signature e Magnifier sobre uma barra de desenho; e a foto anexada numa conversa do Mensagens, com a descrição escrita por humano num balão separado, fora da tela do telefone (folha 0011, q0091 a q0096).
- O cartão de Memory é o componente repetido do bloco final, sempre com a mesma anatomia: foto de fundo, ícones de coração e de reticências no canto superior, título em negrito e subtítulo menor na base (folhas 0018, 0019 e 0020). Numa passagem os quatro cartões saem de uma disposição em leque, sobrepostos e com opacidade reduzida atrás, para uma fileira alinhada e uniformemente espaçada, todos opacos (folha 0020, q0172 para q0173).
- A ação de reduzir a presença de uma pessoa aparece em pontos de entrada diferentes do app, sempre como item de lista dentro de um cartão flutuante claro de cantos arredondados, separado em blocos; no menu do cartão de Memory a ação destrutiva de excluir aparece destacada em vermelho, e num par de telas lado a lado a opção equivalente aparece com uma caixa de destaque ao redor numa delas e sem destaque na outra (folha 0022, q0195 a q0198). A iteração seguinte troca o menu por um modal de tela cheia com foto circular no topo, duas opções em formato de lista com título em negrito, texto explicativo menor, indicador circular de seleção à direita e botão azul de largura total (folha 0023, q0203 a q0205).
- Uma troca de ícone é mostrada como par lado a lado, sem rótulo de texto: o glifo de polegar para baixo ao lado de um círculo de pessoa com sinal de menos, ambos em branco sobre preto e no mesmo traço fino dos ícones de eixos (folha 0024).

Proporção visual: pelas notas, as folhas iniciais alternam cartão preto em tela cheia e corte para a apresentadora; da etapa "Ideate" em diante predomina o layout dividido, com slide à esquerda e apresentadora à direita no mesmo quadro (folhas 0007 a 0009, 0014 a 0017 e 0024 a 0026). Entram ainda blocos curtos de interface real do sistema (folhas 0003, 0010, 0011, 0012, 0014, 0018, 0019, 0022 e 0023), algumas cenas filmadas de pessoas (folhas 0004, 0008, 0009) e uma folha em que a apresentadora ocupa quase todos os quadros (folha 0026).

Divergências ou limites registrados: as notas apontam conteúdo cortado pela borda do quadro em dois pontos, a palavra "Develop" aparecendo truncada no diagrama (folha 0006, q0053 e q0054) e o início de uma terceira linha de texto cortada na base (folha 0008, q0066 a q0068). Registram também que a troca de apresentadora em cena acontece antes de a pessoa ser nomeada na fala (folha 0015) e que, na folha 0022, os menus adicionais foram anotados de forma genérica, sem transcrição item a item.
<!-- /visual:wwdc2021_10304 -->

## Practice audio haptic design (id: wwdc2021_10278, 16.0 min)

- Base: transcrição e 13 de 13 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2021/10278/.
- Tese central: para criar experiências multimodais que pareçam mágicas, a Apple usa três princípios (causality, harmony, utility) junto com a API Core Haptics, demonstrados na prática ajustando o projeto de exemplo HapticRicochet em Xcode.

- O processo de design que a Apple descreve: na fala, o apresentador trabalha diretamente no Xcode sobre o projeto HapticRicochet (derivado de um projeto anterior chamado HapticBounce), uma bola que rola e colide com as bordas do iPhone, cresce ao ser tocada, ganha um escudo (shield) ao ser tocada de novo, e cujo escudo se desgasta a cada colisão até a bola implodir; há também uma textura de fundo que pode ser ativada tocando no plano de fundo.
  - Primeiro revisa os três princípios de design de áudio e háptica usados internamente na Apple.
  - Depois apresenta os quatro elementos fundamentais do Core Haptics: engine (a ligação com o atuador físico do aparelho), player (controle de playback: iniciar, parar, pausar), pattern (uma coleção de eventos ao longo do tempo) e event (os blocos de construção da experiência; os tipos mais comuns citados são transient e continuous). Mostra um arquivo .ahap (Apple Haptic Audio Pattern, em JSON) aberto no QuickLook Visualizer do macOS 12.
  - Para o momento do shield, aplica o princípio harmony: dissecando a animação visual, o retorno háptico e o retorno sonoro separadamente antes de juntar os três.
    - Compara dois assets prontos: ShieldTransient (háptica feita de três eventos transientes, junto de um áudio contínuo e progressivo) e ShieldContinuous (háptica contínua e progressiva, junto de um áudio "wobbly" que decai). Em nenhum dos dois a háptica e o áudio combinam entre si.
    - Decide recombinar: usa a háptica contínua do ShieldContinuous com o áudio do ShieldTransient, editando o arquivo .ahap em um editor de texto e trocando a referência do arquivo de áudio de ShieldB.wav para ShieldA.wav no evento do tipo AudioCustom (cujo volume pode ser ajustado por um ParameterValue). Depois troca, no código, a inicialização do player para carregar esse arquivo ShieldContinuous revisado.
  - Para a rolling texture, resolve dois problemas:
    - Um problema técnico: a textura parava de tocar depois de alguns segundos porque o arquivo .ahap da textura só tinha 2 segundos de conteúdo háptico. A correção foi trocar o tipo do player para CHHapticAdvancedPatternPlayer (a variante avançada do pattern player, que tem funcionalidades extras como pause, resume e callbacks) e habilitar o looping, mantendo o resto do código igual.
    - Um problema de design: o padrão háptico da textura era denso (quase 100 eventos em 2 segundos), mas a textura visual de fundo era grosseira (poucos pontos). A correção foi trocar o asset visual de fundo para uma versão "Fine", com pontos mais densos, para casar com a densidade da háptica.

- Princípios enunciados e o porquê de cada um:
  - Causality: precisa ficar óbvio o que causou o feedback. Exemplo dado: a colisão da bola com a parede do telefone gera som e háptica juntos; a háptica de textura de rolamento só aparece quando o visual de fundo (a grade de pontos) está visível, para que a causa fique clara.
  - Harmony: os sentidos funcionam melhor quando são coerentes, consistentes e trabalham juntos; a experiência deve parecer com o que se vê, o que se ouve e o que se sente ao mesmo tempo. Exemplo dado: uma bola pequena deve soar e parecer pequena; uma bola grande deve soar e parecer mais pesada, como se tivesse mais massa real.
  - Utility: o feedback precisa ter valor claro para a experiência; não adicionar háptica ou som só porque é possível, porque isso rapidamente fica sobrecarregado e desagradável. Reservar háptica e áudio para momentos significativos do app, como o crescimento da bola.

- Técnicas concretas de construção de interface (com números exatos quando falados):
  - A animação visual do momento de ganhar o shield dura 500 milissegundos.
  - O formato .ahap (Apple Haptic Audio Pattern) usa sintaxe JSON.
  - O arquivo .ahap da textura de rolamento tinha apenas 2 segundos de conteúdo háptico, com quase 100 eventos (entries) nesses 2 segundos, o que motivou tanto a correção de looping quanto a densidade do visual.
  - Para sentir a háptica é necessário um iPhone físico modelo 8 ou mais novo; o simulador não reproduz háptica.

- Exemplos citados (apps, telas, componentes) e o que cada um ensina:
  - Botão Flashlight do iOS: citado como referência de experiência multimodal (animação visual, som e háptica) unificada, clara, precisa e sucinta, resultado de um processo iterativo e criativo de design e engenharia juntos.
  - HapticRicochet (bola, colisões, shield, textura de rolamento): ensina, na prática, como comparar e recombinar componentes de áudio e háptica prontos para alcançar harmonia entre os sentidos, e como resolver descompasso entre densidade háptica e densidade visual.
  - Assets ShieldTransient e ShieldContinuous: ensinam que nem todo par de áudio e háptica pronto combina, e que às vezes a solução é recombinar partes de assets diferentes (a háptica de um com o áudio do outro), não descartar nenhum dos dois.
  - CHHapticAdvancedPatternPlayer com looping: ensina a diferença entre o player básico e o avançado do Core Haptics para resolver um problema técnico específico (padrão que "acaba" antes da interação terminar).

- Citações:
  - "It should feel the way it looks, and the way it sounds."
  - "Don't add feedback just because you can."

<!-- visual:wwdc2021_10278 -->
### O que as imagens mostram
Base: 13 de 13 folhas de quadros vistas, todos os códigos conferidos.

- Os slides de princípio usam um vocabulário visual fixo: fundo preto, título em branco no canto superior esquerdo e um ícone esquemático de smartphone à direita com um ponto vermelho representando o feedback. Cada princípio recebe uma variação mínima do mesmo ícone: grade de bolinhas preenchendo a tela com um ponto de origem na borda para causalidade, ponto único com a anotação "HapticIntensity = 0.3" ao lado para harmonia, e ponto central sozinho, sem anotação, para utilidade (folha 0004, q0028, q0030 e q0032). O valor numérico anotado no slide não é dito na fala.
- A arquitetura do Core Haptics aparece como diagrama hierárquico codificado por cor e construído em três passos: primeiro o título sozinho, depois as caixas de engine em azul escuro e player em azul claro, e por fim a caixa de pattern em verde com três círculos menores de evento ligados abaixo por setas verticais (folha 0005, q0037 a q0039; o mesmo diagrama reaparece na folha 0006, q0046).
- O QuickLook do Finder é mostrado como ferramenta real de inspeção do arquivo .ahap, com dois gráficos sobrepostos, uma curva de intensidade em laranja e barras verticais finas em azul, mais o cabeçalho da janela contando os eventos do arquivo, e linhas de chamada apontando para pontos do gráfico com os rótulos "Transient" e "Continuous" (folha 0005, q0040 a q0044).
- A diferença entre os dois tipos de evento fica registrada como diferença de forma no gráfico: três marcas verticais discretas no bloco de háptica sobre uma forma de onda contínua no bloco de áudio num asset (folha 0007, q0062 e q0063) contra uma rampa ascendente de preenchimento laranja sólido, sem barras discretas, no asset alternativo (folha 0008, q0064 a q0066).
- A especificação de design é organizada por canal sensorial em três linhas paralelas, Visual, Haptic e Audio, cada uma com um badge colorido nomeando o arquivo de asset correspondente, cinza para a animação, verde para o .ahap e amarelo para o .wav, ao lado de um círculo grande representando a bola com escudo. As linhas são reveladas em etapas, primeiro a de Visual e depois as de Haptic e Audio juntas (folha 0006, q0052 a q0054); mais adiante as linhas de Haptic e Audio passam a exibir dois badges cada, para comparar os assets alternativos, com o destaque alternando entre eles (folha 0007, q0055 e q0056).
- A edição de um arquivo é mostrada como antes e depois exatos dentro do próprio código: um retângulo de destaque cinza cobre o valor do campo de caminho do arquivo de áudio, e entre um quadro e outro esse valor muda de um nome de arquivo para outro (folha 0008, q0069 a q0071). A fala descreve a troca; a imagem documenta o estado anterior e o posterior.
- O editor Swift aparece em tema escuro com realce de sintaxe por tipo, e um destaque cinza percorre o código acompanhando a fala, mudando de uma linha isolada para um bloco inteiro de linhas conforme o assunto (folha 0007, q0057 a q0060; folha 0010, q0085 e q0086; folha 0011, q0094 e q0095; folha 0012, q0102). Isso localiza com precisão qual trecho está sendo explicado a cada momento.
- A escolha entre duas classes de player é apresentada como tabela comparativa, com colunas de funcionalidade e duas linhas de player, suporte marcado por círculo verde com check e ausência indicada por célula vazia. Na tabela, a classe básica só tem marcação na primeira coluna (folha 0011, q0091 a q0093).
- A densidade háptica ganha prova visual: o gráfico do arquivo de textura mostra dezenas de barras verticais azuis finas muito próximas, com contagem de transientes no cabeçalho da janela (folha 0010, q0090), em contraste direto com os três transientes esparsos do asset visto antes (folha 0007, q0062 e q0063).
- Os estados de textura de fundo são sempre comparados lado a lado, dois ícones de smartphone com legenda de dois níveis nomeando o estado e o arquivo de asset: primeiro fundo liso contra fundo com padrão de bolinhas (folha 0010, q0082 a q0084), depois duas densidades diferentes de bolinhas rotuladas como denso e grosso (folha 0011, q0098 e q0099). A troca efetiva do asset aparece entre quadros, com o ícone da direita passando de contorno vazio para preenchido com o padrão denso (folha 0012, q0100 para q0101).
- O ambiente de trabalho é mostrado junto com o slide, não em corte separado: o navegador de arquivos do Xcode surge à direita do slide de instruções com ícones coloridos por tipo de arquivo, e o slide ganha mais duas linhas de instrução enquanto o painel de arquivos cresce, com um item de lista selecionado em azul (folha 0006, q0047 a q0049).
- As listas dos slides entram por revelação progressiva, com subitens aparecendo primeiro esmaecidos e só depois legíveis, tanto no slide de problemas a resolver (folha 0010, q0082 a q0084) quanto no encerramento (folha 0013, q0110 a q0112).
- O slide de agenda usa hierarquia tipográfica para marcar progresso, com os tópicos anteriores em cinza claro acima e o tópico atual em preto e negrito, em corpo maior (folha 0002, q0018).
- O encerramento é um painel lateral que ocupa a metade esquerda da tela, com o apresentador visível na metade direita, lista de tópicos crescendo até incluir uma seção de recursos adicionais, e um rodapé com linha divisória fina separando o nome da sessão citada, à esquerda, do código do evento à direita (folha 0013, q0110 a q0112).

Proporção visual: pelas notas, a maioria dos quadros é slide ou captura de ferramenta, Xcode, QuickLook e editor de código, com o apresentador entrando em cortes curtos entre blocos; o iPhone físico na mão aparece em sete folhas (0001, 0002, 0006, 0009, 0010, 0011 e 0012) e em nenhum quadro há tela de simulador.

Divergências ou limites registrados: na folha 0011 as notas nomeiam a mesma linha de código de duas formas diferentes, como "texturePlayer?.loopEnabled = true" na descrição da tela e como outra variável na descrição da mudança entre quadros (q0094 e q0095). Registram também um quadro inteiramente preto, sem nenhum elemento visível, diferente de todos os outros da folha (folha 0012, q0105), e trechos sem mudança perceptível entre quadros consecutivos (folha 0009, q0073 para q0074).
<!-- /visual:wwdc2021_10278 -->

## O que este grupo revela sobre o jeito Apple

- A Apple trata tanto uma ferramenta de design (SF Symbols app, id: wwdc2021_10288) quanto uma API técnica (Core Haptics, id: wwdc2021_10278) com o mesmo cuidado de processo: em vez de mostrar o resultado pronto, a fala documenta cada decisão em tempo real, incluindo comparações entre alternativas antes de escolher uma.
- Aparece com frequência o valor de poupar trabalho repetido de quem constrói o app: localização automática de símbolos sem esforço extra do desenvolvedor (id: wwdc2021_10288), acessibilidade automática dos controles padrão de UIKit, AppKit e SwiftUI (id: wwdc2021_10304), e consistência sensorial automática entre visual, som e háptica quando bem desenhada (id: wwdc2021_10278).
- Os três vídeos usam princípios curtos e nomeados como ferramenta de trabalho, não como slogans soltos: causality, harmony e utility no id wwdc2021_10278; os eixos de diversidade e a interseccionalidade no id wwdc2021_10304; nome do símbolo versus nome deprecated no id wwdc2021_10288. Em todos os casos, o princípio nomeado vira um checklist que se repete ao longo da demonstração.
- O processo descrito é sempre iterativo e comparativo, nunca "acerto de primeira": duas versões de asset de shield testadas lado a lado (id: wwdc2021_10278), duas iterações da ação "feature less" em Memories (id: wwdc2021_10304), e comparação entre nome atual e nome deprecated de um símbolo (id: wwdc2021_10288).
- Há uma ênfase recorrente em levar em conta o contexto real de quem usa o produto: idioma e direção de leitura no caso dos símbolos (id: wwdc2021_10288), os eixos de diversidade e a interseccionalidade no caso do design inclusivo (id: wwdc2021_10304), e a exigência de um iPhone físico (não simulador) para validar a experiência háptica (id: wwdc2021_10278).

## Sem transcrição

Nenhum arquivo deste grupo ficou sem transcrição; os três vídeos (wwdc2021_10288, wwdc2021_10304, wwdc2021_10278) tinham transcrição completa da fala.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2021_10288.md, 120 linhas lidas (arquivo completo, sem aviso de truncamento), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2021_10304.md, 289 linhas lidas (arquivo completo, sem aviso de truncamento), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2021_10278.md, 30 linhas lidas (arquivo completo, sem aviso de truncamento), lido até o fim: sim.
