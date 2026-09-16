# ess-09: padrões visuais recorrentes (18 vídeos WWDC 2021 e 2022)

## O sumário da sessão vira barra de progresso, e a hierarquia é feita só com peso e opacidade, sem caixa, ícone ou numeração
- Evidência: wwdc2022_10139 (folha 0006, q0046 a q0048; folha 0008, q0069 para q0070; folha 0010, q0086)
- Evidência: wwdc2022_10037 (folha 0003, q0021 e q0022; folha 0006, q0053; folha 0009, q0078; folha 0013, q0115)
- Evidência: wwdc2022_10169 (folha 0002, q0016; folha 0004, q0034; folha 0009, q0074; folha 0013, q0110 e q0111)
- Evidência: wwdc2022_10015 (folhas 0005 a 0010, q0054, q0058, q0064, q0078, q0087 a q0089)
- Evidência: wwdc2022_10001 (folhas 0002, 0009, 0013 e 0018, q0010 a q0014, q0077 e q0078, q0113 a q0117, q0154)
- Evidência: wwdc2022_10157 (folha 0002, q0014 e q0015; folha 0006, q0048; folha 0008, q0069 e q0072)
- Evidência: wwdc2022_10131 (folha 0002, q0010; folha 0005, q0045; folha 0006, q0046)
- O que isso ensina sobre construir interface: um indicador de onde a pessoa está no percurso não precisa de componente próprio, basta manter a lista inteira visível e trocar peso e opacidade do item corrente. Mesmo texto, mesma posição, nenhuma caixa nova.

## Nada aparece inteiro de uma vez: listas, grades e tabelas crescem item por item, e o item novo entra por fade a partir de opacidade quase ilegível
- Evidência: wwdc2022_10131 (folha 0004, q0034 a q0036; folha 0010, q0083, de um item até sete)
- Evidência: wwdc2021_10304 (folha 0014, q0123 para q0124; folha 0015, q0127 a q0131; folha 0025, q0222 a q0224)
- Evidência: wwdc2022_10139 (folha 0018, q0159 a q0161; folha 0019, q0163 a q0165)
- Evidência: wwdc2022_10158 (folha 0011, q0097 a q0099; folha 0012, q0100 a q0106)
- Evidência: wwdc2022_10009 (folha 0012, q0100 a q0103, com os círculos de check surgindo um a um; folha 0016, q0140 a q0142)
- Evidência: wwdc2022_10037 (folha 0016, q0137 a q0139, subitens em cinza claro antes de virar branco pleno)
- Evidência: wwdc2021_10283 (folha 0009, q0079 a q0081; folha 0010, q0082 e q0083)
- O que isso ensina sobre construir interface: revelação progressiva é uma ferramenta de foco, não um efeito. O que já entrou permanece na tela para dar contexto, e o item novo se distingue pela opacidade em transição, não por cor ou marcador diferente.

## Certo e errado são marcados por selo gráfico colado à tela julgada, check verde contra X ou triângulo de alerta, sem nenhuma legenda explicando a convenção
- Evidência: wwdc2021_10283 (folha 0004, q0033 a q0035; folha 0007, q0056 a q0060; folha 0011, q0091 a q0093)
- Evidência: wwdc2022_10037 (folha 0004, q0034 a q0036; folha 0011, q0094 a q0099; folha 0012, q0103 a q0106)
- Evidência: wwdc2022_10001 (folha 0006, q0049 a q0051, barra de abas com X vermelho contra versão reorganizada com check verde)
- Evidência: wwdc2022_10157 (folha 0006, q0046 e q0047, dois sliders lado a lado, um com alerta amarelo e outro com check verde)
- Evidência: wwdc2022_10169 (folha 0010, q0088, duas versões do mesmo snippet com X vermelho e check verde no canto superior)
- O que isso ensina sobre construir interface: o par comparativo funciona porque os dois lados dividem o mesmo gabarito e só o ponto em discussão muda. O veredito fica num selo pequeno no canto, nunca numa frase explicativa dentro do exemplo.

## A prova é feita por diferença entre dois quadros quase idênticos: tudo congela e um único elemento muda
- Evidência: wwdc2022_10157 (folha 0008, q0066 a q0068, três silhuetas iguais e só a terceira passando de branca para cinza)
- Evidência: wwdc2022_10131 (folha 0007, q0056 a q0058, o cartão fica exatamente na mesma posição da tela enquanto o fundo 3D gira)
- Evidência: wwdc2022_10158 (folha 0003, q0022 e q0023, a onda do alto falante passa de uma barra para duas conforme o campo vai de 0% para 51%)
- Evidência: wwdc2022_10009 (folha 0014, q0118 a q0124, um toggle passa de cinza para azul entre dois quadros quase iguais)
- Evidência: wwdc2022_10139 (folha 0017, q0148 contra q0151, o mesmo parâmetro em verdadeiro e falso, com a barra de status sumindo e voltando)
- Evidência: wwdc2021_10349 (folha 0004, q0032 para q0033, a linha de variante entra no código e os ícones da lista passam de contorno para preenchidos)
- O que isso ensina sobre construir interface: para demonstrar um comportamento, prenda todas as outras variáveis. A comparação entre dois estados quase iguais prova causa de um jeito que uma descrição em texto não prova.

## Cada peça da interface recebe uma etiqueta de texto ligada por linha fina ao elemento, e o vocabulário nomeia a tela peça por peça
- Evidência: wwdc2022_10001 (folhas 0003 a 0017, quase todo mockup carrega rótulo ligado por linha reta, de barra de navegação a ação inativa e descartar)
- Evidência: wwdc2022_10034 (folhas 0004 a 0006, q0036 a q0049, uma etiqueta por componente novo discutido)
- Evidência: wwdc2022_10169 (folha 0010, q0086 e q0087; folha 0013, q0116; folha 0014, q0119 e q0123; folha 0015, q0130, com linha vertical fina separando rótulo e imagem)
- Evidência: wwdc2022_10009 (folha 0015, q0128 a q0130, anotação corrigindo a nomenclatura direto sobre a captura real)
- Evidência: wwdc2021_10283 (folha 0014, q0119 a q0121, linha ligando o rótulo ao bloco e colchete vertical agrupando a lista abaixo)
- O que isso ensina sobre construir interface: nomear a peça na própria imagem elimina a ambiguidade entre o termo e o pixel. A mesma tela aparece várias vezes, mudando só qual parte está anotada.

## A mesma imagem aparece duas vezes, primeiro limpa e depois anotada ou completada, isolando exatamente o que a camada acrescenta
- Evidência: wwdc2022_10169 (folha 0010, q0086 e q0087, mesma captura sem e com o rótulo)
- Evidência: wwdc2021_10288 (folha 0010, q0086, o cartão existia só com o título no quadro anterior e ganha a fileira de quatro ícones)
- Evidência: wwdc2022_10037 (folha 0002, q0013 a q0015, a biblioteca do Apple Music aparece primeiro só com os ícones coloridos e depois com os rótulos ao lado)
- Evidência: wwdc2022_10157 (folha 0004, q0034 a q0036, a tabela pronta recebe o selo de novidade e depois some para deixar o título sozinho)
- O que isso ensina sobre construir interface: mostrar a tela sem os rótulos antes de mostrá-la com eles é um teste de legibilidade feito na frente do público. O que não se entende sem texto precisa de texto.

## Comparação em tabela que isola uma variável por linha, repetindo o mesmo conteúdo em todas as linhas para que só o parâmetro mude
- Evidência: wwdc2021_10349 (folha 0003, q0021 a q0025, quatro variações de cor, três tamanhos de fonte e três escalas de imagem do mesmo rótulo)
- Evidência: wwdc2022_10157 (folha 0004, q0028 a q0033, tabela de modos montada em etapas com os mesmos sete símbolos em colunas fixas)
- Evidência: wwdc2022_10034 (folha 0008, q0064 a q0069, a mesma palavra repetida do peso mais fino ao mais espesso, ao lado de um app real usando aqueles pesos)
- Evidência: wwdc2022_10158 (folha 0011, q0094 a q0098, quatro versões finais do mesmo ícone lado a lado com o nome do modo abaixo)
- O que isso ensina sobre construir interface: para escolher um valor de token, monte a mesma peça em todas as opções na mesma tela. A diferença aparece por comparação direta, não por memória entre um slide e outro.

## Grade regular de ícones de traço fino, brancos sobre preto, com legenda curta centralizada abaixo, espaçamento uniforme e nenhuma caixa separando itens
- Evidência: wwdc2021_10304 (folha 0002, q0010, vinte ícones em quatro linhas de cinco; a mesma grade volta na folha 0019, q0167 a q0169)
- Evidência: wwdc2022_10157 (folha 0002, q0017 e q0018; folha 0003, q0019 e q0020, grades de cerca de oito colunas por quatro linhas com peso visual uniforme)
- Evidência: wwdc2022_10169 (folha 0013, q0109, paleta de quinze círculos em cinco por três; folha 0014, q0126, dezesseis tipos com ícone circular e rótulo abaixo)
- Evidência: wwdc2022_10158 (folha 0006, q0046 a q0050, grade de vinte e sete ícones em três fileiras de nove para mostrar a explosão combinatória)
- Evidência: wwdc2021_10288 (folha 0010, q0086, quatro ícones em fileira de espaçamento igual com legendas curtas centralizadas)
- O que isso ensina sobre construir interface: inventário se mostra em grade regular, sem moldura por item e sem cor, porque o assunto é a quantidade e a coerência de traço. Cor entra depois, quando o assunto passa a ser o estado.

## Um item é retirado da grade e ampliado sozinho no momento exato em que a fala trata dele
- Evidência: wwdc2021_10304 (folha 0002, q0011 para q0012; e folha 0013, q0109 depois q0112 e q0113, onde dois ícones se aproximam e passam a dividir uma legenda única somando as duas condições)
- Evidência: wwdc2021_10283 (folha 0004, q0028 e q0029, os cinco princípios primeiro enfileirados e depois isolados com suas regras empilhadas)
- O que isso ensina sobre construir interface: o zoom dentro do mesmo sistema gráfico preserva a memória do conjunto. A pessoa continua sabendo de onde aquele item saiu porque o desenho não mudou, só a escala.

## O diagrama geométrico abstrato é pareado com a tela real no mesmo enquadramento, e os dois mudam juntos
- Evidência: wwdc2022_10001 (folha 0002, q0017; folha 0011, q0092 a q0094; folha 0012, q0100 e q0101, onde o nó destacado muda de cidade para rota e a captura ao lado muda na mesma proporção)
- Evidência: wwdc2022_10009 (folha 0010, q0082 a q0086, diagrama de três blocos em fundo branco seguido da aplicação literal do mesmo agrupamento na tela real)
- Evidência: wwdc2022_10169 (folha 0007, q0059 a q0063, árvore de parâmetros em texto puro ao lado das telas em que aquelas combinações aparecem)
- Evidência: wwdc2022_10131 (folha 0007, q0055, cubo rotulado ligado a dois retângulos em perspectiva; folha 0008, q0061 e q0062, trapézio saindo do aparelho para representar campo de visão)
- Evidência: wwdc2021_10283 (folha 0009, q0073 a q0076, linhas em leque saindo da base do bloco para os ícones de propriedade, com a tela real do menu ao lado)
- O que isso ensina sobre construir interface: o modelo mental e o produto ficam no mesmo quadro para que a abstração não vire teoria solta. Retângulo, linha e cor de caminho ativo bastam para desenhar hierarquia.

## Materiais translúcidos com o fundo visivelmente borrado e escurecido sustentam camadas temporárias, e o vídeo mostra isso sem comentar
- Evidência: wwdc2022_10037 (folha 0007, q0056 a q0058, a folha de ações entra sobre a tela anterior borrada, e q0060 e q0061 repetem o fundo desfocado no alerta central)
- Evidência: wwdc2021_10283 (folha 0003, q0019 a q0022, lista de ações em vidro fosco na barra de menu e cartões brancos sobre papel de parede desfocado)
- Evidência: wwdc2022_10169 (folha 0009, q0078 a q0080, snippet translúcido deixando ver borrados os ícones da tela inicial, com os quatro níveis de cor de rótulo anotados por cima)
- Evidência: wwdc2021_10349 (folha 0007, q0055 e q0056, o terceiro botão da fila mostra vidro fosco desfocando o fundo atrás da seta)
- Evidência: wwdc2022_10015 (folha 0009, q0073 a q0077, a tela de gerenciamento reaparece semitransparente sobre outro app ao fundo)
- O que isso ensina sobre construir interface: a camada temporária se identifica pelo material, não por uma borda. O conteúdo de baixo continua legível como contexto, desfocado e escurecido o bastante para não competir.

## Cor tem função fixa e reservada, e o vermelho fica só para destruir
- Evidência: wwdc2022_10037 (folha 0010, q0088 a q0090, botão vermelho de remover à esquerda e neutro azul à direita; folha 0009, q0080 e q0081, só a ação recomendada em verde forte e a secundária em cinza)
- Evidência: wwdc2022_10015 (folhas 0008 e 0009, botões de comunicação em laranja preenchido, bolinhas coloridas de status e vermelho reservado ao botão de parar de compartilhar)
- Evidência: wwdc2022_10001 (folha 0016, q0136 e q0137, folha de ação com dois botões empilhados e o destrutivo em vermelho)
- Evidência: wwdc2021_10304 (folha 0022, q0195 a q0198, dentro do cartão flutuante só a ação de excluir aparece em vermelho)
- Evidência: wwdc2022_10139 (folha 0006, q0051; folha 0008; folha 0014, onde o verde marca consistentemente a entrada na experiência compartilhada sem que a fala enuncie a convenção)
- O que isso ensina sobre construir interface: reservar uma cor para uma consequência só funciona se ela nunca aparecer com outro papel. O destaque de recomendação também é cor, então a tela precisa ter no máximo uma ação colorida por vez.

## Estado ativo e seleção são marcados por preenchimento sólido ou contorno azul, nunca só por posição
- Evidência: wwdc2021_10317 (folha 0006, q0050, controle segmentado de três vistas com o item ativo preenchido em verde sólido)
- Evidência: wwdc2021_10288 (folha 0002, q0015, contorno quadrado azul ao redor do ícone selecionado, e o inspetor trocando para o rótulo de seleção múltipla)
- Evidência: wwdc2022_10157 (folha 0005, q0038 e q0039, menu suspenso aberto com o item ativo destacado em azul)
- Evidência: wwdc2022_10158 (folhas 0002 e 0003, célula selecionada com contorno azul na grade; folha 0009, q0073 a q0080, linhas de camada selecionadas em bloco azul)
- Evidência: wwdc2021_10349 (folha 0003, q0026 e q0027, barra de abas com a aba ativa em azul)
- O que isso ensina sobre construir interface: seleção precisa de sinal redundante, forma mais cor, porque a posição sozinha não sobrevive a grade densa, daltonismo ou tela pequena.

## Selo circular verde de novidade no canto e caixa cinza envolvendo a linha recém acrescentada marcam o que mudou naquele ano
- Evidência: wwdc2021_10349 (folha 0003, q0027; folha 0004, q0028 e q0033; folha 0005, q0045; folha 0006, q0049, sempre a caixa cinza na linha nova mais o selo verde)
- Evidência: wwdc2022_10158 (folha 0011, q0097 a q0099; folha 0012, q0100 a q0106, selo verde no canto superior direito dos cartões de resumo)
- Evidência: wwdc2022_10157 (folha 0004, q0034, a tabela pronta recebe o selo verde antes de dar lugar ao título do recurso)
- Evidência: wwdc2021_10288 (folha 0010, q0082, cartão com selo circular verde ao lado do título)
- Evidência: wwdc2021_10283 (folha 0016, q0138 a q0140, a tela já configurada traz selo verde de novidade e a outra traz alerta amarelo)
- O que isso ensina sobre construir interface: diferença entre o que já existia e o que é novo merece marcador gráfico próprio, distinto do marcador de aprovação, mesmo que ambos sejam verdes.

## O componente é apresentado como gabarito fixo com conteúdo variável, e a mesma anatomia reaparece em contextos diferentes
- Evidência: wwdc2022_10015 (folha 0010, q0079 a q0085, banners com avatar circular à esquerda, duas linhas de texto, botão azul e X de descarte, repetidos para edição, comentário, menção, criação e exclusão)
- Evidência: wwdc2022_10139 (folha 0002, q0013; folha 0004, q0029; folha 0015, o mesmo desenho de banner cobrindo eventos diferentes; e folha 0008, q0064 e q0066, o card mantém moldura, título e botão enquanto a lista interna troca de faixas para avatares)
- Evidência: wwdc2022_10037 (folha 0005, q0040 a q0045 e folha 0006, q0046 a q0050, o mesmo template de introdução em contextos distintos; folha 0013, q0109 a q0112, estados vazios de dois apps com esqueleto idêntico)
- Evidência: wwdc2021_10304 (folhas 0018, 0019 e 0020, o cartão de Memory sempre com foto de fundo, ícones no topo, título em negrito e subtítulo na base)
- Evidência: wwdc2022_10001 (folha 0004, q0035 e q0036; folha 0005, q0037 e q0038, telas de detalhe com capa, título, grade de duas por duas métricas e blocos roláveis abaixo)
- O que isso ensina sobre construir interface: quando a moldura é constante e só o conteúdo muda, a pessoa aprende o componente uma vez e reconhece em qualquer lugar. Estados vazios e alertas ganham com esqueleto compartilhado.

## O layout é testado por compressão na tela: a janela encolhe, o texto trunca, os itens caem em ordem
- Evidência: wwdc2022_10009 (folha 0005, q0037 a q0039, os ícones da seção central da toolbar somem primeiro e sobram os grupos das pontas; folha 0003, q0024 a q0027, o título trunca aos poucos até cortar a última letra)
- Evidência: wwdc2021_10283 (folha 0002, q0012 a q0018, a grade de duas colunas no iPhone vira lista vertical compacta no Apple Watch)
- Evidência: wwdc2022_10169 (folha 0011, q0091 e q0092, o mesmo cartão de confirmação no relógio e no telefone, com espaçamento e ícone ajustados)
- Evidência: wwdc2022_10015 (folhas 0003, 0006 e 0007, a mesma hierarquia de blocos em iPad, iPhone e Mac, mudando só moldura de janela, cursor e barra de menu)
- O que isso ensina sobre construir interface: defina antes qual item some primeiro. O comportamento de estreitamento é decisão de design, não resultado do que o layout fizer sozinho.

## Localização é mostrada como mudança real de layout, com a interface espelhada e a caixa crescendo, nunca como conceito
- Evidência: wwdc2022_10034 (folha 0003, q0021 a q0027, wireframe cinza e depois as telas em árabe com a composição espelhada; folha 0004, q0028 a q0032, a numeração do carrossel passa de 1, 2, 3 com setas à direita para 3, 2, 1 com setas à esquerda; folha 0012, q0102 a q0107, grade de pares com destaque roxo só nos ícones que de fato invertem)
- Evidência: wwdc2022_10037 (folha 0014, q0121 a q0124, a mesma caixa fica visivelmente mais alta em tailandês e espelhada em hebraico; folha 0015, q0127, cabeçalhos de dia por extenso em árabe ocupando bem mais espaço que a letra única em inglês)
- Evidência: wwdc2022_10001 (folha 0012, q0105 e q0106, a tela reaparece inteiramente espelhada em hebraico, com botão de voltar, ícones, alinhamento e as próprias anotações trocados de lado)
- Evidência: wwdc2021_10288 (folha 0002, q0018, o inspetor lista os sistemas de escrita cobertos por um símbolo, uma linha por escrita)
- O que isso ensina sobre construir interface: o layout tem que ser projetado para crescer em altura e largura e para espelhar por inteiro, e a inversão é seletiva, alguns símbolos viram e outros não.

## Tela pequena vive de contraste máximo e poucos elementos, e a mesma família aceita extremos opostos de densidade
- Evidência: wwdc2021_10308 (folha 0003, q0026, hora no topo, índice em maiúsculas, valor grande, variação em verde e status em cinza no rodapé sobre preto sólido; folha 0004, q0034, apenas os dígitos da hora em amarelo puro ocupando quase toda a tela)
- Evidência: wwdc2021_110142 (folha 0003, q0025, mesma escada tipográfica no app de ações; folha 0004, q0029 contra q0032, um mostrador denso com data, clima e três complicações ao lado de um mostrador com só a hora gigante)
- Evidência: wwdc2022_10037 (folha 0008, q0066 e q0069 a q0072, ícone ou anel colorido alinhado à hora, título em negrito, corpo menor e botões retangulares de largura total empilhados)
- O que isso ensina sobre construir interface: em superfície pequena, o contraste sustenta a leitura e a hierarquia é puramente vertical. A mesma linguagem precisa cobrir a versão densa e a versão de um único dado.

## O controle mora sobre a imagem da câmera, dentro do campo de atenção, e não numa barra separada
- Evidência: wwdc2022_10131 (folha 0002, q0013 a q0016, HUD mínimo com linha marcada de distância, ícone de escaneamento e botão circular; folha 0005, q0037 e q0038, uma única linha vertical e o valor grande no topo; folha 0008, q0070 a q0072, indicador de fora de campo com texto curto e seta direcional)
- Evidência: wwdc2021_10304 (folha 0004, q0034 e q0035, linha pontilhada, rótulo numérico grande e barra de progresso fina dentro da moldura semitransparente do aparelho; folha 0003, q0026 e q0027, retângulos amarelos marcando cada trecho de texto reconhecido no visor)
- Evidência: wwdc2022_10037 (folha 0010, q0083, a seta de orientação do Panorama fica centralizada no visor)
- Evidência: wwdc2021_10317 (folha 0013, q0110 e q0112, telemetria em fonte monoespaçada pequena sobreposta ao vídeo, sem caixa nem fundo)
- O que isso ensina sobre construir interface: quando a tarefa acontece na imagem, o indicador vai na imagem, pequeno, sem fundo sólido, e só o valor que importa recebe tamanho grande.

## Atualização em tempo real é provada pelo número que muda entre dois quadros consecutivos
- Evidência: wwdc2021_10317 (folha 0008, q0071 para q0072, a contagem regressiva cai dois segundos de um quadro para o outro)
- Evidência: wwdc2022_10131 (folha 0005, q0037 para q0038, o valor da medição muda entre quadros)
- Evidência: wwdc2022_10158 (folha 0003, q0022 e q0023, o campo de porcentagem sai de zero e o desenho do ícone reage)
- Evidência: wwdc2022_10009 (folha 0014, q0118 a q0124, o valor do campo de repetição muda dentro do mesmo cartão flutuante, sem abrir tela nova)
- O que isso ensina sobre construir interface: feedback contínuo precisa de um alvo numérico estável na tela, sempre no mesmo lugar, para que só o valor se mova.

## Medida e limiar são anotados na própria imagem, com o número escrito ao lado do exemplo
- Evidência: wwdc2022_10034 (folha 0011, q0091 a q0094, o mesmo texto rotulado com 0, 10 e 20 por cento de espaçamento, com uma barra fina marcando a emenda entre letras no valor maior; q0095 e q0096, o valor de opacidade anotado embaixo do exemplo)
- Evidência: wwdc2022_10158 (folha 0004, q0031 a q0036, barra horizontal segmentada com marcações numéricas e bolinha indicadora, com o ícone acendendo por partes; folha 0005, q0039 a q0041, a mesma escala com limiares quebrados em 34% e 68%)
- Evidência: wwdc2021_10288 (folha 0004, q0035; folha 0005, q0038 a q0040, seletor de cor com valor percentual ao lado e lista de cores com percentuais próprios por linha)
- Evidência: wwdc2022_10131 (folha 0002, q0013 a q0016, a medida sobreposta à silhueta; folha 0008, q0070, marcador de escala em porcentagem surgindo sobre o objeto)
- O que isso ensina sobre construir interface: número na imagem transforma opinião em especificação. Um controle de faixa contínua fica compreensível quando os limiares são desenhados, não descritos.

## A estrutura interna do elemento é exposta como lista vertical de camadas nomeadas, uma linha por camada com miniatura
- Evidência: wwdc2021_10288 (folha 0006, q0054, lista de camadas com miniatura e nome de cor; folha 0007, q0059 para q0060, a lista passa de uma linha para duas com a ativa em contorno azul)
- Evidência: wwdc2022_10157 (folha 0006, q0052; folha 0007, q0058, q0061 e q0062, losangos empilhados em perspectiva isométrica leve, numerados da base para o topo, com eixo de ordem em profundidade a partir da folha 0009)
- Evidência: wwdc2022_10158 (folha 0008, q0064 a q0071, a lista evolui de uma entrada para três nomeadas por nível, cada linha com miniatura quadrada, nome, campo de porcentagem e ícones de ação)
- Evidência: wwdc2021_10349 (folha 0006, q0049 a q0053, até três cores mapeadas a categorias nomeadas, com a categoria esmaecendo quando o desenho não tem aquela camada)
- O que isso ensina sobre construir interface: quando um elemento tem partes, mostre a pilha nomeada ao lado do resultado. A camada que não existe fica visível e esmaecida, em vez de simplesmente sumir da lista.

## A ferramenta de autoria aparece na tela no seu layout de três colunas, categorias à esquerda, grade ao centro, inspetor à direita
- Evidência: wwdc2021_10288 (folha 0001, q0009 e folha 0002, com a barra lateral separando categorias fixas das coleções do usuário por divisória, contador de itens no cabeçalho e inspetor alternando entre vazio e detalhe)
- Evidência: wwdc2022_10157 (folha 0003, q0023 e q0024, trocar a categoria na barra lateral troca por inteiro a grade central)
- Evidência: wwdc2022_10158 (folhas 0002, 0003 e 0007 a 0011, o painel de inspeção mantém sempre a mesma ordem vertical de seções)
- Evidência: wwdc2022_10034 (folha 0013, q0109 e q0110, o mesmo app no Mac com barra lateral, grade e painel de detalhes mostrando a lista de escritas cobertas)
- O que isso ensina sobre construir interface: navegar, listar e inspecionar pedem três regiões estáveis. O inspetor mantém a ordem das seções mesmo quando o conteúdo delas muda com o modo selecionado.

## Código aparece em dose mínima, sempre colado ao resultado renderizado no mesmo enquadramento
- Evidência: wwdc2021_10349 (folhas 0001 a 0007, código à esquerda em monoespaçada colorida e resultado à direita, do primeiro exemplo até a tabela final, com as notas registrando que essa estrutura não é enunciada na fala)
- Evidência: wwdc2022_10139 (folha 0012, q0105 e q0106; folha 0014, q0119 a q0123; folha 0017, onde a linha em tela preta convive no mesmo quadro com a moldura de iPhone, uma linha curta por conceito, sem editor nem numeração)
- O que isso ensina sobre construir interface: uma linha por conceito, sempre ao lado do efeito visível. O código funciona como legenda do comportamento, não como trecho para copiar.

## O quadro capta a animação no meio do caminho, com a tela nova parcialmente sobre a antiga
- Evidência: wwdc2022_10001 (folha 0010, q0082 e q0083, a tela nova cobre quase toda a anterior vinda da direita; folha 0012, q0104, duas telas sobrepostas em diagonal entre lista e detalhe)
- Evidência: wwdc2022_10015 (folha 0009, q0073 a q0077, o popover se dissolve sob a tela de gerenciamento até ela ficar nítida)
- Evidência: wwdc2021_10288 (folha 0003, q0019 a q0027, a captura escurece em etapas, o título entra semitransparente sobre a tela ainda visível e o app reaparece atrás do texto no fim)
- Evidência: wwdc2021_10304 (folha 0020, q0172 para q0173, quatro cartões saem de leque sobreposto para fileira alinhada e uniformemente espaçada)
- Evidência: wwdc2022_10037 (folha 0010, q0088 a q0090, o mesmo alerta em três variações de brilho, registro de um fade de entrada)
- O que isso ensina sobre construir interface: a transição é parte do componente. Cobertura parcial vinda de uma direção conta a relação entre as telas, e o dissolve marca troca de contexto sem mudar de lugar.

## Movimento contínuo é representado dentro de um quadro parado, por justaposição de poses, dupla exposição ou borrão
- Evidência: wwdc2021_110142 (folha 0007, q0055 e q0056, o mesmo mostrador com duas posições do pé lado a lado e depois três, montando a progressão da animação sem vídeo)
- Evidência: wwdc2022_10131 (folha 0008, q0065 para q0066, a mesma pessoa em duas poses semitransparentes sobrepostas no mesmo quadro)
- Evidência: wwdc2021_10308 (folha 0007, q0058 a q0060, fileira de cinco miniaturas do mesmo mostrador com o dedo em posição ligeiramente diferente; folha 0011, q0097 a q0099, a mão aparece borrada enquanto a tela reage)
- O que isso ensina sobre construir interface: para documentar animação em material estático, congele os quadros extremos e o meio, lado a lado. A nitidez seletiva separa o que se move do que está parado.

## O regime de apresentação da tela muda conforme o assunto: layout vem isolado em fundo neutro, gesto e contexto vêm filmados no corpo da pessoa
- Evidência: wwdc2021_10304 (folhas 0003, 0010, 0011, 0014, 0018, 0019, 0022 e 0023, capturas sempre centralizadas em fundo preto ou dentro de moldura desenhada com notch e barra de status, nunca com uma mão segurando o telefone)
- Evidência: wwdc2021_113 (folha 0008, q0071; folha 0009, q0073; folha 0014, quase todos os quadros, com mãos reais tocando, arrastando e digitando sobre iPad e iPhone)
- Evidência: wwdc2021_110142 (folha 0011, q0093, q0094 e q0099, cada tela aparece pareada com o close da mão executando o gesto correspondente)
- Evidência: wwdc2021_10308 (folha 0004, q0031 e q0032, um dedo toca diretamente a tela e o texto rola entre um quadro e outro)
- O que isso ensina sobre construir interface: mostrar a mão quando o assunto é alcance, toque e postura, e retirar a mão quando o assunto é grade, espaçamento e hierarquia. O enquadramento decide para onde vai a atenção.

## A moldura do aparelho ou da janela entra como sinal de plataforma, não como enfeite
- Evidência: wwdc2021_10349 (folha 0005, q0039 a q0042, uma janela de macOS simulada com os três botões coloridos serve de moldura para mostrar a troca de modo naquele contexto)
- Evidência: wwdc2022_10015 (folhas 0003, 0006 e 0007, a mesma hierarquia em três aparelhos, mudando só moldura, cursor e barra de menu; no Mac, o menu de permissões vira lista de texto sem ícones)
- Evidência: wwdc2021_10304 (folhas 0003, 0010 e 0014, as capturas vêm dentro de moldura com notch e barra de status)
- Evidência: wwdc2021_110142 (folha 0003, q0020 e q0025, a tela aparece no relógio com pulseira, registrada como contexto real de uso)
- O que isso ensina sobre construir interface: a moldura comunica em que sistema aquela regra vale e por que os controles mudam de forma entre plataformas.

## O fluxo é mostrado inteiro, tela por tela, na ordem em que acontece, com telas reais do sistema
- Evidência: wwdc2022_10015 (folha 0003, q0019 a q0027, documento aberto, popover de compartilhamento, composição da mensagem com o card anexado, troca de destinatário, avisos de entrada e o popover final de colaboração)
- Evidência: wwdc2022_10139 (folha 0014, q0119 a q0126, folha de compartilhamento subindo da base, escolha de amigos com preview e teclado, e o resultado como bolha de convite na conversa)
- Evidência: wwdc2022_10001 (folha 0017, q0145 a q0152, empurrar dentro do formulário, modal cobrindo a tela, seletor de fotos em grade com indicador numerado e o retorno ao formulário já com a miniatura marcada)
- Evidência: wwdc2021_10283 (folha 0012, q0100 a q0107, o mesmo parâmetro resolvido primeiro no editor do Mac e depois por voz, com a tela de seleção ao lado do card de pergunta)
- O que isso ensina sobre construir interface: o valor está nas emendas. Mostrar de onde se entra, o que muda no meio e como se volta expõe os pontos em que o fluxo quebra.

## Antes de qualquer tela de produto vem uma abertura narrativa que encena o problema
- Evidência: wwdc2022_10015 (folha 0001, q0008 e q0009; folha 0002, q0010 a q0015, o ícone de e-mail vira avatar com selo de envelope e depois todos os selos viram o ícone de mensagens, encenando a troca de canal)
- Evidência: wwdc2022_10139 (folhas 0001 a 0005, dois minutos e meio de encenação quase toda em preto e branco com vinheta circular nos closes, com corte abrupto para o estúdio colorido em q0042)
- Evidência: wwdc2022_10037 (folha 0001, q0008 e q0009, a palavra cursiva aparece dentro da tela de um Macintosh bege e no quadro seguinte sai da moldura, maior e em gradiente colorido, na mesma caligrafia)
- Evidência: wwdc2022_10157 (folha 0001, q0007 a q0009, grade de três colunas por quatro linhas com a mesma palavra em vários idiomas e escritas, um coração vermelho como única exceção de cor)
- O que isso ensina sobre construir interface: a tese vem antes da tela. A abertura estabelece o problema com imagem e tipografia, sem pedir que a pessoa já saiba ler o produto.

## Analogia física e objeto real substituem a tela quando o assunto é conceito
- Evidência: wwdc2021_10283 (folha 0002, q0010 a q0016, peças de montar coloridas se encaixando ao lado dos blocos de ação para explicar modularidade)
- Evidência: wwdc2022_10139 (folha 0009, q0077, close da mão pousando no braço de um toca-discos, sem nenhuma tela em cena; folha 0019, q0163 a q0165, objetos artesanais fotografados marcando a virada para o fecho)
- Evidência: wwdc2022_10009 (folha 0016, q0140 a q0142, um still life de brinquedo e tigela fica fixo à direita enquanto os bullets entram um por corte)
- Evidência: wwdc2021_10308 (folhas 0001 a 0013, o manequim articulado de madeira sobre pedestal circular se repete de folha em folha como continuidade cênica entre entrevistados)
- O que isso ensina sobre construir interface: um objeto reconhecível carrega o conceito sem jargão e dá âncora visual estável enquanto o texto muda ao lado.

## O wireframe cinza aparece como etapa real do processo, não como figura de linguagem
- Evidência: wwdc2022_10034 (folha 0003, q0021 a q0027, as mesmas três telas reduzidas a blocos cinza de título, imagem, texto, pontos de paginação e barra de abas, e só depois de volta como telas reais)
- Evidência: wwdc2022_10037 (folha 0004, q0033 a q0036, a versão reprovada do aviso é um wireframe denso com título, ícone de alerta, dois parágrafos e botão vermelho grande, contra a versão aprovada reduzida a ícone, título curto, uma frase e botão em cápsula)
- Evidência: wwdc2022_10139 (folha 0016, q0143 e q0144, mapa mental simulado com notas adesivas coloridas ligadas por linhas finas a um nó central, com barra de desenho na base)
- O que isso ensina sobre construir interface: o rascunho de baixa fidelidade prova estrutura sem discutir cor, e serve como o lado errado de um par quando o problema é excesso de conteúdo.

## Acessibilidade é mostrada como estrutura de dados, não como aparência
- Evidência: wwdc2021_10349 (folha 0002, q0014 a q0018, o desenho do símbolo é substituído na coluna da direita pelo texto que seria lido em voz alta, primeiro genérico, depois o nome técnico e por fim a legenda descritiva)
- Evidência: wwdc2022_10037 (folha 0015, q0133 a q0135, cada adesivo aparece com seu identificador técnico entre aspas ao lado da descrição, os três pares empilhados um a um)
- Evidência: wwdc2021_10304 (folha 0011, q0091 a q0096, a foto passa pelo app de fotos, pela ferramenta de marcação com a opção de descrição e chega à conversa com a descrição escrita por pessoa em balão separado)
- O que isso ensina sobre construir interface: a descrição é um campo nomeado que acompanha o elemento, e precisa ser projetada junto com o desenho, não depois.

## O próprio vídeo aplica acessibilidade e atribuição, com intérprete fixo no canto e créditos dentro da imagem
- Evidência: wwdc2021_110142 (folha 0001, q0001 a q0009, o quadro do intérprete aparece sempre na mesma posição e composição, tratado como permanente em todas as folhas)
- Evidência: wwdc2021_113 (folhas 0001 a 0019, retrato quadrado fixo do intérprete sobre fundo cinza claro à direita da cena principal)
- Evidência: wwdc2021_10308 (folhas 0006 a 0008, o aviso de direitos do personagem fica fixo no canto inferior esquerdo da própria tela do relógio)
- Evidência: wwdc2021_10317 (folha 0007, q0057 a q0060, legendas de atribuição sempre no canto inferior direito, mantendo a posição entre imagens de origens diferentes)
- O que isso ensina sobre construir interface: elementos persistentes de acessibilidade e de crédito ganham uma posição reservada que nunca muda, e o layout do resto é desenhado em volta dessa reserva.

## A identificação de pessoa e de produto segue gabarito fixo de legenda, sem caixa de fundo
- Evidência: wwdc2021_113 (folha 0004, q0036; folha 0005, q0037 a q0042, nome em branco maior e cargo em cinza menor, duas linhas alinhadas à esquerda; e folhas 0006 a 0033, o selo de app no canto inferior esquerdo com ícone, nome e etiqueta de status mudando só a palavra)
- Evidência: wwdc2021_10317 (folha 0020, q0176, o logotipo mostrado reúne ícone à esquerda e bloco de texto à direita com dois pesos no nome e tagline em caixa alta com tracking aumentado)
- O que isso ensina sobre construir interface: um par de nome e qualificador em dois pesos, alinhado à esquerda e sem fundo, é suficiente para identificar sobre qualquer imagem, desde que o contraste do vídeo seja controlado.

## O fim de bloco e o fim da sessão têm forma padronizada: rodapé de referência a outra sessão e cartela institucional centralizada em preto
- Evidência: wwdc2021_10288 (folha 0008, q0072; folha 0010, q0089, nome de outra sessão à esquerda e ano do evento à direita, uma vez separados por linha fina; folha 0011, q0095, fecho com a maçã e o nome do evento centralizados)
- Evidência: wwdc2022_10157 (folha 0011, q0099; folha 0012, q0100, mesmo padrão de rodapé com texto pequeno à esquerda e sigla do evento à direita)
- Evidência: wwdc2022_10009 (folha 0016, q0140 a q0142, o slide de encerramento acumula bullets e termina com rodapé apontando outra sessão)
- Evidência: wwdc2021_10308 (folha 0014, q0123 e q0124) e wwdc2022_10131 (folha 0011, q0092 para q0093, onde entre os dois últimos quadros muda apenas o peso e o tom do texto)
- O que isso ensina sobre construir interface: um fecho previsível e silencioso evita competir com o conteúdo, e a referência cruzada tem lugar fixo em vez de virar mais um item da lista.

## A abertura institucional do evento usa grade de centenas de miniaturas de pessoas seguida de explosão de partículas
- Evidência: wwdc2021_10308 (folha 0001, q0001 e q0002, mosaico de rostos em retângulos arredondados azul claro com ícones minúsculos sobrepostos, seguido de partículas como transição)
- Evidência: wwdc2021_10317 (folha 0001, q0001 para q0002, grade de avatares circulares com pílulas sobrepostas e depois duas explosões de confete sobre a mesma grade inalterada)
- O que isso ensina sobre construir interface: repetição de um módulo pequeno em grade regular cria escala e sensação de comunidade sem que nenhum item precise ser legível.

## Achados de fonte única

- O editor de vetores externo aparece com réguas, guia azul e guia vermelha cruzando o ícone e painel de posição, tamanho, opacidade e sombra, e a volta para o app passa por um diálogo modal de substituição com o botão de confirmar em azul como ação padrão: wwdc2021_10288 (folha 0006, q0047 a q0051).
- Colar como texto e colar como imagem produzem resultados diferentes e visíveis: no primeiro caso o símbolo fica na mesma linha de base, cor e peso da palavra ao lado, como se fosse caractere; no segundo vira objeto com alças de seleção e campos numéricos de posição e tamanho: wwdc2021_10288 (folha 0008, q0066; folha 0009, q0080).
- O inspetor de disponibilidade empilha duas entradas para o mesmo desenho, o nome atual com uma linha por modo de renderização e número de versão à direita, e abaixo o nome obsoleto marcado com triângulo de aviso: wwdc2021_10288 (folha 0003, q0019).
- Conteúdo duplicado entre abas é desenhado como colunas com os itens embaixo e, no quadro seguinte, os mesmos nomes repetidos sob mais de uma coluna dentro de caixas tracejadas: wwdc2022_10001 (folha 0007, q0062 e q0063).
- A barra de navegação do modal é decomposta anotação por anotação sobre a mesma tela, incluindo a lista de rótulos alternativos possíveis para o botão da direita e o estado acinzentado desse botão enquanto o formulário está incompleto: wwdc2022_10001 (folha 0015, q0130 a q0135).
- O mesmo botão de fechar é julgado por contexto: aceitável num artigo editorial sem entrada de dados e problemático numa tela de filtro cujos itens recebem marca de seleção entre um quadro e outro: wwdc2022_10001 (folha 0016, q0138 a q0142).
- O painel de personalização da barra de ferramentas mostra os ícones em quadrados arredondados com contorno tracejado amarelo indicando que são arrastáveis, e o corpo do documento continua parado enquanto só a barra muda acima dele: wwdc2022_10009 (folha 0004, q0029 a q0032).
- O menu de edição existe em duas variantes com a mesma ordem interna de itens, horizontal e compacta junto ao texto para toque, vertical em lista com ícone à direita para ponteiro: wwdc2022_10009 (folha 0007, q0056 a q0060).
- A busca e substituição muda de forma conforme o teclado: menu suspenso com opções avançadas ancorado acima do teclado virtual, e barra compacta no rodapé com campo, contador de resultados e setas quando há teclado físico: wwdc2022_10009 (folha 0008, q0064 a q0066).
- Seleção múltipla sem modo de edição: o título é substituído por uma contagem, os cartões ficam destacados e cada rótulo do menu de ações repete o número de itens: wwdc2022_10009 (folha 0011, q0091 a q0096).
- A consolidação de notificações só fica evidente na comparação de quadros: a pilha de banners individuais se acumula, os antigos esmaecem e toda a pilha é substituída por um banner único com contagem de pessoas e de documentos, com o rótulo do botão mudando junto: wwdc2022_10015 (folha 0010, q0082 a q0086).
- O estudo tipográfico tira a letra do contexto e a decompõe em quatro formas posicionais em fila, cada uma com rótulo de posição abaixo, antes de mostrar a grade completa de variações de glifo: wwdc2022_10034 (folha 0007, q0055 a q0058).
- Dois sistemas de numerais são separados por legenda simples embaixo de cada número e depois aplicados em quatro contextos, incluindo calculadora com teclado espelhado e mostrador de relógio com formas e cores bem distintas entre as versões: wwdc2022_10034 (folha 0014, q0118 a q0124).
- O fecho combina a página de diretrizes aberta num laptop com uma colagem em grade reunindo miniaturas de quase todos os exemplos já mostrados na sessão: wwdc2022_10034 (folha 0015, q0127 a q0132).
- O onboarding de ambiente usa três telas de estrutura idêntica, com título curto em maiúsculas, corpo, indicadores de página em pontos e botão de largura total, e sobrepõe ícones verde e vermelho à imagem da câmera para indicar estado de superfície e de luz: wwdc2022_10131 (folha 0006, q0048 a q0052).
- O progresso do escaneamento é uma miniatura de planta tridimensional no canto que ganha formas a cada quadro, acompanhada de contornos neon finos traçando paredes e móveis já detectados, com cancelar e concluir em cantos opostos no topo: wwdc2022_10131 (folhas 0004 e 0009, q0031 e q0032, q0074 a q0078).
- Oclusão como pista de profundidade é demonstrada com o objeto virtual parcialmente escondido atrás de blocos reais sobre a mesa, logo após a lista de cinco pistas em texto puro: wwdc2022_10131 (folha 0009, q0080 e q0081).
- A assimetria do que cada participante vê é mostrada com três molduras iguais, e num quadro seguinte a da esquerda passa a exibir interrogações no lugar da resposta enquanto o botão muda de texto: wwdc2022_10139 (folha 0013, q0109 e q0111).
- A folha de detalhes da sessão separa quem está na chamada de quem está na atividade, com bloco do que está tocando, contagem de pessoas ativas, botão de sair em vermelho e status textual distinto por pessoa: wwdc2022_10139 (folha 0015, q0130 a q0133).
- A curadoria de sinônimos de invocação é mostrada como edição visível de lista, com uma opção já riscada que some no quadro seguinte enquanto as linhas abaixo de certo ponto escurecem: wwdc2022_10169 (folha 0006, q0046 e q0047).
- A equivalência entre diálogo falado e componente visual é declarada por uma equação, com sinal de igual entre o snippet mais diálogo de apoio e o diálogo integral: wwdc2022_10169 (folha 0010, q0089 e q0090).
- A reordenação dinâmica de sugestões é provada com pares de telas em que o cartão da primeira posição troca de item entre quadros, com o app de atalhos à esquerda e as sugestões à direita: wwdc2022_10169 (folha 0012, q0103 a q0107).
- O grau de imersão de uma tela é julgado na imagem: o slide sobre customizar um mostrador acumula linhas de texto ao lado da tela de edição rica e ganha um X no último quadro, seguido do caso simples de apenas trocar de mostrador: wwdc2021_10283 (folha 0005, q0040 a q0044).
- Os três estados de um parâmetro aparecem na mesma forma de bloco com legenda abaixo, sem valor, com valor padrão e com a opção de perguntar sempre, cada um ao lado do dispositivo que resolve aquele caso: wwdc2021_10283 (folha 0015, q0127 a q0129).
- O diagrama de processo muda de forma dentro da narrativa, de linha horizontal com cinco palavras e pontos coloridos para um anel sem pontos, com uma seta triangular no topo marcando a etapa atual e o anel girando de fato entre quadros: wwdc2021_10304 (folha 0007, q0055 para q0057; folha 0016, q0141 para q0142).
- Os mesmos ícones da grade de eixos reaparecem como legenda semitransparente na faixa inferior de uma cena filmada real, anotando contexto sobre a vida cotidiana: wwdc2021_10304 (folha 0008, q0070).
- Uma troca de ícone é comunicada só por par visual, sem rótulo, com o glifo antigo ao lado do novo no mesmo traço fino e na mesma cor: wwdc2021_10304 (folha 0024).
- O contraste de navegação entre dois apps do sistema é posto lado a lado: uma tela traz setas de voltar e avançar antes do título e a outra, mais densa e com seções recolhíveis na barra lateral, não traz controle nenhum desse tipo: wwdc2022_10009 (folha 0009, q0076 contra q0079).
- O símbolo customizado é desenhado de propósito em forma simplificada, um cubo sólido com padrão de grade nas faces, omitindo detalhes do objeto real para sobreviver a tamanhos pequenos: wwdc2022_10158 (folha 0007).
- A falha de contraste é exibida como falha concreta: a versão dentro de um círculo em monocromático vira quase um disco preto sem detalhe, e a correção aparece no quadro seguinte com duas camadas do tipo apagador identificadas por miniatura hachurada: wwdc2022_10158 (folhas 0010 e 0011, q0085 a q0093).
- Os HUDs de jogo em telefone mostrados na premiação compartilham a mesma disposição, controle à esquerda, cluster de habilidades em arco no canto inferior direito, barra de vida sobre o personagem e minimapa no topo: wwdc2021_113 (folhas 0028, 0033 e 0034).
- A leitura assistida é mostrada pela diferença entre dois quadros do mesmo texto, com a palavra destacada mudando de posição e de cor, de amarelo para azul, para indicar o avanço da narração: wwdc2021_113 (folha 0007, q0060 para q0061).
- A separação de estágios de um foguete é comunicada por diagrama em vista explodida, dois componentes isolados e afastados sobre fundo neutro, sem nenhuma legenda: wwdc2021_10317 (folha 0012, q0105).
