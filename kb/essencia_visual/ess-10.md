# Essência visual do lote ess-10

Base: 17 sínteses visuais lidas na íntegra, todas de vídeo (WWDC 2022 e 2023).

## Uma lista de tópicos fixa serve de barra de navegação do vídeo inteiro, com o item ativo em negrito escuro e os demais em cinza claro, sem mudar de tamanho nem de posição
- Evidência: wwdc2022_110340 (folha 0003, q0022 e q0023; folha 0007; folha 0010, q0085; folha 0019, q0165 a q0167)
- Evidência: wwdc2023_10072 (folhas 0006, 0009, 0014 e 0019, q0050, q0075, q0124, q0167)
- Evidência: wwdc2023_10138 (folha 0001, q0007 a q0009; folha 0004, q0035; folha 0009, q0078; folha 0012, q0102)
- Evidência: wwdc2023_10115 (folha 0002, q0013 e q0014; folha 0005, q0041; folha 0008, q0064; folha 0010, q0082)
- Evidência: wwdc2023_10078 (folha 0001, q0005 a q0007, lista sobreposta translúcida no canto direito do plano do apresentador)
- Evidência: wwdc2022_110441 (folha 0003, q0019 a q0021; folha 0010, q0090; folha 0012, q0105, a mesma lista em árabe do lado direito)
- O que isso ensina sobre construir interface: estado de seleção pode ser comunicado só por peso e tom, sem caixa, fundo, marcador ou deslocamento, e o elemento permanece no mesmo pixel entre seções para não custar reorientação ao leitor. Um sumário persistente é mais barato que uma tela de índice repetida.

## Slides e componentes são construídos por acumulação, item entrando um a um enquanto os anteriores permanecem visíveis, em vez de trocar de tela
- Evidência: wwdc2022_110340 (folha 0002, q0014 a q0017, grade de ícones montada em dois tempos, três primeiro e mais três depois; folha 0014, q0118 e q0119, dois ícones e depois mais quatro)
- Evidência: wwdc2022_110381 (folha 0009, q0074 a q0078, recapitulação com ícone de check verde entrando item a item)
- Evidência: wwdc2023_10073 (folha 0010, q0082 e q0083, de três para cinco recomendações; folha 0011, q0094 a q0096, de dois a quatro itens; folha 0014, q0124 a q0126, do título sozinho até quatro itens)
- Evidência: wwdc2023_10078 (folha 0010, q0086 a q0088, título sem itens, depois três, depois um quarto)
- Evidência: wwdc2023_10193 (folha 0004, q0031 a q0033, primeira linha sozinha e a segunda somando no quadro seguinte)
- Evidência: wwdc2022_103 (folhas 0039 e 0040, q0346 a q0356, cada categoria de prêmio ganha uma coluna por vez dentro do mesmo template)
- O que isso ensina sobre construir interface: revelar conteúdo por acréscimo dentro de um contêiner estável evita que o leitor reconstrua o contexto a cada passo, e serve tanto para onboarding quanto para formulários longos e resumos de resultado.

## O par de certo e errado é a convenção didática dominante, com selo de check e selo de X posicionados sempre no mesmo lugar sob cada variação
- Evidência: wwdc2023_10076 (folhas 0004, 0007, 0008, 0011 e 0015, aplicado a cartões de livro, notificações de FaceTime, listas de ajustes e barras de ferramentas)
- Evidência: wwdc2023_10073 (folha 0005, q0038 a q0041, pílula arredondada aprovada contra retângulo de cantos quase retos, e um coração centralizado aprovado contra dois corações sobrepostos)
- Evidência: wwdc2023_10197 (folha 0012, q0103 e q0104, dois ursos idênticos rotulados com e sem camadas de apagar, o segundo recebendo X no quadro seguinte)
- Evidência: wwdc2023_10194 (folha 0002, q0017 e q0018; folha 0004, q0030; folha 0006, q0047, aqui com X e check em cinza neutro, não coloridos)
- Evidência: wwdc2023_10193 (folha 0005, q0039 e q0040, X vermelho sobreposto à versão cujo título repete o nome do app)
- Evidência: wwdc2023_10078 (folha 0009, q0078 a q0080, comparações divididas ao meio por linha vertical com selos fixos no topo de cada metade)
- O que isso ensina sobre construir interface: a regra fica legível quando as duas versões diferem em um atributo só e ficam no mesmo enquadramento, o que vale para documentar um design system tão bem quanto para ensinar numa palestra.

## Medidas em pontos são anotadas em amarelo por cima do componente real, decompondo a área do alvo em desenho visível mais espaço vazio
- Evidência: wwdc2023_10076 (folha 0009, q0077 a q0081, retângulo de 60pt ao redor do coração, depois 8pt nas quatro margens internas, depois marcas de espaçamento entre botões e 16pt escrito na grade de música)
- Evidência: wwdc2023_10073 (folha 0005, q0043 e q0044, 8pt de cada lado do glifo e 44pt marcando a largura do alvo, com o slide de texto vindo só depois)
- Evidência: wwdc2023_10076 (folha 0010, q0082 a q0086, 28pt no disclosure e retângulo tracejado englobando imagem mais texto como um alvo único; folha 0011, q0094, 4pt entre itens de lista; folha 0015, q0134, 20pt de sobreposição do ornament na borda)
- Evidência: wwdc2022_110381 (folha 0002, q0016 e q0017, blocos empilhados marcados 96, 70 e 45 pts; folha 0006, q0049 e q0050, corpos de 42pt a 20pt para igualar a largura final)
- O que isso ensina sobre construir interface: a área tocável não é o desenho do ícone, e mostrar o padding como retângulo explícito impede que ele seja tratado como sobra. Anotar a medida sobre o componente real evita a especificação que ninguém consegue aplicar.

## A grade de referência aparece desenhada por cima da interface pronta, expondo a malha que o texto só descreve em palavras
- Evidência: wwdc2023_10026 (folha 0004, q0028, linhas sobrepostas ao mostrador de anéis de Atividade)
- Evidência: wwdc2023_10138 (folha 0009, q0081; folha 0010, q0082 e q0090; folha 0011, q0091, a malha em cruz e círculos concêntricos sobre o mostrador e depois isolada em linhas verdes sem conteúdo nenhum)
- Evidência: wwdc2023_10194 (folha 0002, q0016, guias verticais verdes nas bordas da pilha de cartões da tela de bloqueio, provando que Live Activities e notificações alinham na mesma margem)
- O que isso ensina sobre construir interface: a coerência entre componentes de layouts diferentes vem de compartilharem a mesma margem, e desenhar essa margem uma vez sobre o produto vale mais que repetir a regra em prosa.

## O rótulo ligado por linha de chamada ao ponto exato da tela nomeia cor, propriedade, API ou parte de componente sem alterar a imagem
- Evidência: wwdc2023_10026 (folha 0005, q0039, "System Green" apontando para o botão primário de um alerta em modo escuro)
- Evidência: wwdc2023_10138 (folha 0011, q0095, ".topBarTrailing" ligado ao ícone no canto superior direito; folha 0013, q0117, e folha 0014, q0118, o modificador de fundo e o de estilo secundário apontando para alvos distintos na mesma tela)
- Evidência: wwdc2022_110342 (folha 0009, q0076 a q0078, a captura do Activity fica imóvel enquanto fios finos apontam primeiro para os anéis e depois para os gráficos de apoio)
- Evidência: wwdc2022_110381 (folha 0007, q0058, o rótulo de título ligado ao texto do card de Memória; folha 0008, q0064 a q0066, marcação de qual parte da manchete usa cada largura)
- Evidência: wwdc2023_10078 (folha 0009, q0074 a q0077, o rótulo do ponto de fuga entra com seta, depois sai e o ponto permanece, depois o ponto é deslocado para fora do centro)
- O que isso ensina sobre construir interface: a anotação permite ensinar a anatomia sem recortar o componente do contexto, e mantém a mesma imagem como referência enquanto o assunto muda de camada.

## A cor entra por último, depois que a estrutura já se sustenta em preto e branco ou em uma única cor
- Evidência: wwdc2022_110340 (folha 0017, q0145 e q0146, as duas séries aparecem só em branco, distinguíveis apenas por círculo e quadrado, e só então surge a legenda colorida; folha 0004, os gráficos de estudo em branco sobre preto enquanto os ícones de conceito são azuis)
- Evidência: wwdc2022_110342 (folhas 0009 e 0010, q0079 a q0085, dois platters idênticos que primeiro divergem em período e escala, depois em cor, depois em estilo de barra)
- Evidência: wwdc2023_10197 (folha 0002, q0010 a q0016, a grade de símbolos parte de preto sobre cinza claro, depois um único símbolo acende em azul, depois mais acendem)
- O que isso ensina sobre construir interface: se o layout só funciona com cor, ele não funciona. Separar forma de cor na própria construção deixa a redundância de codificação visível antes de virar problema de acessibilidade.

## A paleta é validada repetindo a mesma composição sobre fundos e modos diferentes, em grade ou em sequência
- Evidência: wwdc2022_110340 (folha 0018, q0160 a q0162, o mesmo gráfico duplicado em miniaturas de modo escuro e claro com as amostras de cor ao lado; folha 0019, grade de quatro cruzando os dois modos com e sem aumento de contraste)
- Evidência: wwdc2023_10076 (folhas 0006 e 0007, q0050 a q0059, o painel translúcido fica parado na mesma posição enquanto o vídeo de fundo troca por mar, elefante, criatura aquática, campo verde, dinossauros e folhagem)
- Evidência: wwdc2022_110381 (folha 0008, q0064 a q0066, a mesma manchete repetida sobre bege claro, branco e cinza escuro mantendo as anotações)
- Evidência: wwdc2023_10075 (folha 0010, q0086 a q0090, o controle de volume por pessoa repetido sobre quatro fundos; folha 0013, q0112 a q0114, o cartão de convite idêntico sobre três fundos desfocados)
- O que isso ensina sobre construir interface: material translúcido e cor de contraste precisam ser testados contra o pior fundo possível, não contra o fundo escolhido para o mockup, e a grade cruzando modo e contraste é o teste mínimo antes de fechar a paleta.

## O efeito é provado pela diferença entre dois quadros da mesma cena, com um único atributo mudando e todo o resto congelado
- Evidência: wwdc2023_10026 (folha 0007, q0059 a q0062, o World Clock troca de localidade preservando layout e mapa, mudando só hora e posição do indicador)
- Evidência: wwdc2023_10194 (folha 0004, q0028 e q0029, o mesmo cartão de voo com o mesmo texto e a mesma diagramação em azul e depois em amarelo; folha 0008, q0067 e q0068, o cartão de maré passando de azul acinzentado a vermelho escuro no modo noturno sem mover nada)
- Evidência: wwdc2022_103 (folha 0023, q0203 a q0205, a paisagem de montanhas troca de magenta e roxo para azul petróleo e verde mantendo a composição idêntica)
- Evidência: wwdc2023_10138 (folha 0011, q0097 e q0098, com o modificador de tamanho de controle realçado no código, o botão de pausa aparece maior que no quadro anterior)
- O que isso ensina sobre construir interface: variação de tema, de marca ou de estado deve caber numa troca de tokens sobre a mesma estrutura, e essa é a maneira mais barata de verificar se a estrutura realmente aguenta a variação.

## A comparação lado a lado em molduras idênticas é o recurso padrão para provar paridade entre idiomas, plataformas e tamanhos de tela
- Evidência: wwdc2022_110441 (folha 0004, q0028 a q0036, pares de iPhone com inglês à esquerda e árabe à direita, cada par rotulado pelo assunto em teste, imagem, escala de temperatura, ordem dos dias, calendário e gráfico no tempo)
- Evidência: wwdc2022_110381 (folha 0010, q0082 a q0089, a mesma tela do sistema em espanhol, inglês e chinês com estrutura de componentes idêntica e só o texto mudando)
- Evidência: wwdc2023_10138 (folha 0005, q0040 a q0043, o mesmo app de clima em iPad paisagem, depois comparado simultaneamente em três tamanhos até o relógio)
- Evidência: wwdc2023_10076 (folha 0005, q0040 a q0042, colunas rotuladas por plataforma com amostras de corpo e título, a linha do aparelho espacial ficando visivelmente mais grossa)
- O que isso ensina sobre construir interface: o teste de internacionalização e de responsividade é visual e comparativo, não descritivo, e a moldura idêntica nos dois lados é o que torna a diferença atribuível ao conteúdo.

## Anatomia humana e postura entram como diagramas de traço fino, definindo o alcance confortável antes de qualquer decisão de layout
- Evidência: wwdc2023_10072 (folha 0007, q0060 a q0063, pessoa reclinada com os pés apoiados e pessoa sentada ereta, círculo pontilhado em torno da cabeça e uma prancha vertical ao lado representando o conteúdo)
- Evidência: wwdc2023_10073 (folha 0003, q0023 a q0025, a sala renderizada ganha um anel de luz em torno do sofá e em seguida vira diagrama de anéis concêntricos marcados 30, 60 e 90 graus)
- Evidência: wwdc2023_10078 (folha 0002, q0010 a q0012, perfil de cabeça com cérebro, depois dois círculos frontais com linhas pontilhadas convergindo para um alvo; folha 0007, q0057 a q0060, o mesmo perfil recebendo o ícone da cóclea)
- Evidência: wwdc2023_10075 (folhas 0003 e 0004, q0026 a q0029, disco preto no chão, silhuetas brancas sem rosto e formas verdes representando conteúdo, com sombra de contato)
- O que isso ensina sobre construir interface: o limite de conforto físico vem antes da grade, e um vocabulário gráfico abstrato e reutilizável, silhueta, disco, plano, permite discutir posicionamento sem que a aparência do produto atrapalhe.

## O vocabulário cromático dos diagramas é fixo dentro de cada peça, com uma cor reservada só para anotação e outras para papéis semânticos
- Evidência: wwdc2023_10075 (folha 0012, q0100 a q0102, verde com selo de compartilhado para o contexto comum e azul marinho com selo de não compartilhado para a janela pessoal, terminando na composição com tela verde ao fundo e três painéis azuis)
- Evidência: wwdc2023_10073 (folha 0006, q0050 e q0051, e folha 0007, q0055 e q0056, o amarelo aparece só como contorno, linha diagonal e divisor da comparação de escala)
- Evidência: wwdc2023_10076 (folha 0009 a folha 0015, o amarelo é usado exclusivamente para medida e espaçamento, nunca como cor do componente)
- Evidência: wwdc2023_10078 (folha 0002 e folha 0007, o verde marca linha de visão e cones de conforto, e a folha 0006, q0050, acrescenta um terceiro sinal, alerta laranja, para o caso intermediário)
- O que isso ensina sobre construir interface: reservar uma cor para o metanível, ou seja, para anotação e medida, impede que o leitor confunda instrução com produto, e a mesma disciplina vale para overlays de debug dentro do app.

## Telas reais de apps do sistema entram como repertório de referência antes de o princípio ser aplicado ao exemplo em construção
- Evidência: wwdc2022_110340 (folhas 0001, 0009, 0013, 0015 e 0016, cartão translúcido com timeline horária, cartão de tendência com ponto de destaque, cartões de métrica, anéis concêntricos e cartão de rota com perfil de elevação, cada um preservando sua própria linguagem)
- Evidência: wwdc2022_110342 (folha 0001, q0007 a q0009, platters escuros de cantos arredondados com título pequeno, número grande e legenda menor; folha 0006, q0052 e q0053, complicações de mostrador, mini linhas ao lado de ativos e gráfico miúdo dentro de card)
- Evidência: wwdc2023_10138 (folha 0010, q0083 a q0089, os três layouts fundamentais rotulados sobre apps reais e depois pares de relógios trocando de conteúdo por transição translúcida)
- O que isso ensina sobre construir interface: antes de propor um padrão, vale montar a parede de exemplos já existentes no sistema, porque ela fixa a faixa de variação aceitável e evita reinventar um componente que já tem forma canônica.

## Interação é filmada com mão e aparelho físicos, mostrando o dedo entrando, pressionando e saindo em quadros sucessivos
- Evidência: wwdc2022_110340 (folha 0006, q0046 a q0051, e folha 0012, q0101 a q0103, a mão segura o iPhone, o dedo se aproxima, pressiona a barra e é retirado, com um selo escuro surgindo sob o ponto de toque)
- Evidência: wwdc2023_10073 (folha 0014, q0119 a q0121, close do teclado virtual com brilho mais claro nas teclas vizinhas ao ponto de contato, brilho que se desloca junto com o dedo)
- Evidência: wwdc2023_10115 (folha 0006, q0049 e q0050, o dedo gira a Digital Crown e o mapa muda de cidade)
- Evidência: wwdc2023_10138 (folha 0015, q0127, a mesma tela do World Clock primeiro em still de produto e depois em foto real de pulso)
- O que isso ensina sobre construir interface: feedback de toque precisa ser projetado para o instante em que o dedo cobre o alvo, e só a filmagem com mão real revela o quanto do componente fica oculto no momento do contato.

## Esboço à mão e produto final aparecem no mesmo quadro, com setas rotulando cada área da tela antes de ela existir
- Evidência: wwdc2022_103 (folha 0014, q0123 e q0124, metade esquerda com wireframe desenhado à mão e setas nomeando remetente, legendas, saída e participantes, metade direita com a captura real do iPhone em uso)
- Evidência: wwdc2022_113 (folha 0013, q0115 e q0116, o wireframe manuscrito e, no quadro seguinte, ele mesmo colocado ao lado do mockup já implementado; folha 0002, q0013, retângulos desenhados à mão em papel cobrindo o rosto do entrevistado)
- Evidência: wwdc2022_110441 (folha 0003, q0022 a q0025, três telas com conteúdo real, depois reduzidas a blocos cinza sem conteúdo, depois o wireframe já espelhado com o conteúdo árabe recolocado)
- O que isso ensina sobre construir interface: reduzir a tela a blocos cinza é o passo que expõe a estrutura independentemente do conteúdo, e guardar o rascunho ao lado do resultado documenta qual decisão veio da intenção e qual veio da implementação.

## Componentes são mostrados primeiro vazios e depois preenchidos, com o contêiner definido antes do dado
- Evidência: wwdc2022_110342 (folha 0011, q0091 a q0096, a barra horizontal aparece primeiro sem valor e depois com nome e comprimento, e as colunas de dias surgem só com marcação pontilhada antes de receberem barras cinzas e amarelas)
- Evidência: wwdc2023_10078 (folha 0010, q0086 a q0088, o título da lista aparece sem nenhum item antes de qualquer linha entrar)
- Evidência: wwdc2023_10194 (folha 0009, q0074 a q0080, a pílula da Dynamic Island começa vazia e percorre chamada recebida, forma quase quadrada, barra alongada com forma de onda e volta a vazia)
- Evidência: wwdc2023_10138 (folha 0012, q0107 e q0108, três relógios só com fundos sólidos em gradiente, sem ícone nem texto, e no quadro seguinte dois deles recebem conteúdo)
- O que isso ensina sobre construir interface: o estado vazio é parte do componente e não uma exceção, e projetar o contêiner antes do conteúdo é o que garante que a tela não colapse quando o dado faltar.

## Tipografia é apresentada como tabela ou matriz de amostras rotuladas, com o mesmo texto repetido em todas as variações
- Evidência: wwdc2022_110381 (folha 0004, q0028 a q0033, matriz com linhas de largura, Compressed a Expanded, e colunas de peso, Ultralight a Black, iluminando uma linha por vez; folha 0005, q0041 a q0044, o mesmo pangram em quatro linhas, uma por largura; folha 0007, q0061, grade três por três com nove combinações do mesmo título)
- Evidência: wwdc2022_110441 (folha 0006, q0052 e q0053, tabela de coluna dupla com a família latina do mais fino ao mais espesso à esquerda e a árabe nos mesmos pesos à direita; folha 0007, q0058 a q0061, colunas rotuladas por tamanho óptico com a mesma palavra em escalas diferentes)
- Evidência: wwdc2023_10138 (folha 0013, q0112 a q0114, pílulas rotuladas primária, secundária e terciária em opacidade decrescente, ao lado dos mesmos blocos de texto em tamanhos decrescentes)
- O que isso ensina sobre construir interface: a escala tipográfica só se avalia com o mesmo conteúdo em todas as células, porque a diferença que interessa é quanto espaço cada variação consome para dizer a mesma coisa.

## O código fica ao lado do resultado e o trecho realçado muda no mesmo quadro em que a tela muda
- Evidência: wwdc2023_10138 (folha 0006, q0053; folha 0007, q0060 a q0062; folha 0008, q0066 a q0069, o destaque azul passa de uma condição de origem para a inversa dela e o anel de Atividade troca de posição junto)
- Evidência: wwdc2023_10115 (folha 0003, q0026 e q0027, árvore de arquivos à esquerda, editor Swift ao centro e canvas com moldura de iPhone à direita; folha 0004, q0028, o texto azul no canvas corresponde aos modificadores de fonte, peso e cor no código)
- O que isso ensina sobre construir interface: quando a demonstração amarra linha de código e pixel no mesmo instante, a propriedade deixa de ser abstrata, e é esse o argumento para ferramentas de design que renderizam ao vivo em vez de exportar telas estáticas.

## Ferramentas de autoria são filmadas em uso, com painéis, camadas e sliders visíveis, revelando a densidade de controle por trás do resultado simples
- Evidência: wwdc2023_10197 (folha 0011, q0095 a q0099, o app SF Symbols em três colunas, categorias à esquerda, preview grande ao centro, painel de renderização, cor, fundo e camadas à direita, com a lista de camadas ganhando linha e o modo passando de monocromático a multicor)
- Evidência: wwdc2023_10115 (folha 0012, q0100 a q0103, ferramenta parametrizada num iPad com sliders numéricos de tamanho, vão, espessura, opacidade e sombra, grade de miniaturas à direita e seletor de cor abrindo sobre o painel)
- Evidência: wwdc2022_103 (folha 0023, q0202 a q0205, barra de gradientes nomeados, roda de cores, painel modal de recorte e sliders por canal; folha 0025, q0221 a q0224, ferramentas empilhadas à esquerda e cartões de camada nomeados à direita)
- Evidência: wwdc2022_113 (folha 0021, q0185 a q0187, janela de recorte, roda de cores e réguas por canal, e uma segunda ferramenta em que só a imagem de fundo muda entre dois quadros enquanto o painel de gradientes permanece)
- O que isso ensina sobre construir interface: painel lateral persistente com o resultado ao centro é o arranjo recorrente das ferramentas criativas, e mostrar o painel real é o que deixa claro quantos parâmetros estão implícitos numa decisão apresentada como simples.

## Ícones lineares monocromáticos em grade regular servem de vocabulário para conceitos abstratos, e depois reaparecem como marcador do tópico em foco
- Evidência: wwdc2022_110340 (folha 0002, q0014 a q0017, grade de três colunas por duas linhas de quadrados com ícones lineares e legenda pequena abaixo, e os mesmos ícones voltam ancorados ao lado dos gráficos nas folhas 0004, 0009 e 0010)
- Evidência: wwdc2022_110342 (folha 0003, q0020 e q0021, miniaturas azuis monocromáticas em grade dois por dois sob um rótulo de conceito, uma grade para mudança e outra para proporção)
- Evidência: wwdc2023_10115 (folha 0004, q0033, grade de ícones quadrados verdes de cantos arredondados, cada um com símbolo e nome do modificador embaixo)
- Evidência: wwdc2023_10073 (folha 0010, q0090, seis gestos nomeados com setas de direção numa grade de duas linhas)
- Evidência: wwdc2023_10193 (folha 0004, q0035, um raio dentro de contorno para ação e uma caixa tridimensional para entidade, lado a lado com rótulo)
- O que isso ensina sobre construir interface: um conceito ganha reconhecimento quando recebe forma própria e reaparece ancorada ao conteúdo que ilustra, e a grade uniforme comunica que os itens são pares, não uma hierarquia.

## O encerramento condensa a peça inteira num mosaico de miniaturas, sem rótulo, apoiado em um still fotográfico ou numa cartela de sessões relacionadas
- Evidência: wwdc2022_103 (folha 0041, q0364, mosaico de doze ícones em grade de quatro por três, sem nomes)
- Evidência: wwdc2022_113 (folha 0035, q0308 e q0309, grade de quatro colunas por três linhas de ícones sob um título pequeno centralizado, seguida de um quadro liso claro)
- Evidência: wwdc2022_110441 (folha 0014, q0119 a q0122, grade irregular reunindo quase todos os exemplos da sessão, de relógios a wireframes, slides de espaçamento, ícones e telas de app)
- Evidência: wwdc2023_10138 (folha 0015, q0127 e q0128, bloco de fechamento sobre still-life de mesa de madeira com três sessões relacionadas)
- Evidência: wwdc2023_10078 (folha 0010, q0086 a q0088, lista revelada item por item sobre fotografia de mesa de madeira, com o código do evento alinhado à direita em cada linha)
- Evidência: wwdc2023_10026 (folha 0008, q0071 e q0072, relógio de pulseira de couro sobre mesa de madeira recebendo a lista de quatro sessões alinhada à direita)
- O que isso ensina sobre construir interface: um resumo por miniatura funciona porque recupera o reconhecimento visual acumulado, e a superfície fotográfica real quebra a monotonia do slide sem introduzir informação nova.

## Painel de vidro translúcido é o material padrão, sempre demonstrado com o entorno visível através dele e contrastado com o equivalente opaco
- Evidência: wwdc2023_10076 (folhas 0003 e 0004, q0022 a q0032, a janela translúcida em vários ângulos, parte vazia e parte com o app dentro, primeiro em luz clara e depois em ambiente escuro, contra o quadro de painéis sólidos cinza azulados que instrui a evitar janelas opacas)
- Evidência: wwdc2023_10073 (folha 0004, q0028 e q0032 a q0034, um painel grande borrado ao fundo e outro menor e nítido à frente, com retângulo escuro secundário que aparece e some)
- Evidência: wwdc2023_10072 (folha 0003, q0019 a q0027, a janela de música em vidro dentro de uma sala, com a transparência variando a ponto de a janela quase sumir contra a parede clara)
- Evidência: wwdc2023_10075 (folha 0004, q0030 e q0031, cartão de vidro escuro com capa, ícones, título, artista, barra de progresso fina e três botões de transporte)
- O que isso ensina sobre construir interface: transparência é um risco de legibilidade que precisa ser exercitado no pior caso, parede clara ou cena de alto contraste, e o contra-exemplo opaco só convence quando mostrado no mesmo enquadramento.

## Hierarquia é construída por opacidade e profundidade, com o elemento secundário recuando em vez de encolher
- Evidência: wwdc2023_10075 (folha 0004, q0034 e q0035, a janela de biblioteca aparece atrás do cartão em reprodução, mais apagada, com o botão de fechar flutuando acima do conjunto)
- Evidência: wwdc2023_10072 (folha 0012, q0102 a q0104, painel de reprodução pequeno e semiopaco colocado à frente e à esquerda de uma tela grande de cinema; folha 0002, q0015, três palavras sobrepostas separadas só por contraste de opacidade)
- Evidência: wwdc2022_110342 (folha 0004 e folha 0008, o slide de agenda mantém os três tópicos visíveis e apaga os que não estão em curso)
- Evidência: wwdc2023_10138 (folha 0013, q0112 a q0114, três níveis de texto distinguidos só por opacidade decrescente sobre fundo escuro)
- O que isso ensina sobre construir interface: rebaixar por opacidade preserva a posição e a forma do elemento, o que mantém o mapa da tela estável e custa menos ao usuário do que remover ou redimensionar.

## A transformação de um componente em outro é mostrada quadro a quadro, com os pontos de ancoragem permanecendo no lugar
- Evidência: wwdc2023_10026 (folha 0006, q0049 e q0050, o cronômetro passa de mostrador analógico para leitura digital mantendo os mesmos botões nas mesmas posições, com a anotação nomeando o padrão na própria tela)
- Evidência: wwdc2023_10194 (folha 0017, q0151 a q0153, um círculo preto se estica lateralmente até virar duas extremidades ligadas por uma faixa fina e depois se separa em dois círculos independentes; folha 0011, q0094 e q0095, o treino em tela cheia condensa na pílula guardando só ícone e distância)
- Evidência: wwdc2022_110342 (folha 0010, q0089 e q0090, uma barra vertical segmentada em blocos coloridos vira gráfico de barras horizontais nas mesmas cores, ordenadas por comprimento)
- Evidência: wwdc2023_10197 (folha 0009, q0074 a q0079, o símbolo de origem fica ao lado enquanto a forma dentro do plano cresce e se resolve, mais virando check e nuvem com sol virando nuvem com chuva)
- O que isso ensina sobre construir interface: continuidade de identidade depende de manter alguma coisa fixa durante a transição, botão, ícone, cor ou posição, e é isso que separa uma transformação legível de uma troca de tela disfarçada.

## O apresentador divide o quadro com o material em vez de alternar com ele, e a interface costuma aparecer sobreposta ao plano da pessoa
- Evidência: wwdc2023_10078 (folha 0001, q0005 a q0007, a lista de tópicos fica translúcida no canto direito do plano do apresentador, sobre fundo desfocado)
- Evidência: wwdc2022_110340 (folha 0003, q0022 e q0023, a lista de cinco palavras em tela dividida ao lado do apresentador)
- Evidência: wwdc2023_10073 (folha 0011, q0094 a q0096, lista crescente em layout de tela dividida com o apresentador à direita)
- Evidência: wwdc2023_10026 (folha 0003, q0023 e q0024, template de título em negrito, lista simples e fundo cinza claro em composição dividida com o apresentador)
- Evidência: wwdc2022_103 (folhas 0005, 0010, 0022, 0023, 0025 e 0026, a composição dominante coloca o entrevistado e a interface no mesmo quadro, metade rosto e metade tela, em vez de mostrar a interface isolada)
- O que isso ensina sobre construir interface: manter referência e comentário simultâneos na tela evita que o espectador escolha entre olhar a pessoa ou o artefato, e o mesmo raciocínio se aplica a painéis de ajuda que não tapam o conteúdo que explicam.

## Achados de fonte única

- Alvo de toque desenhado como contorno branco espesso muito maior que a barra do gráfico, deixando explícito que a área tocável se estende muito além do desenho da marca, com o rótulo de acessibilidade citado logo abaixo (wwdc2022_110340, folha 0014, q0121 a q0123).
- Anatomia do tooltip de gráfico: retângulo escuro com a data em cinza acima e o valor em negrito maior abaixo, ancorado por uma linha vertical fina que desce até o topo da barra correspondente, testado em três barras seguidas (wwdc2022_110340, folha 0013, q0112 a q0114).
- A mesma descrição de gráfico reescrita em quatro degraus dentro do mesmo card escuro, do rótulo do período ao rótulo com número em destaque, depois frase completa abaixo do gráfico, depois a frase acrescida da variação percentual com seta (wwdc2022_110342, folha 0004, q0031 a q0036).
- Três escalas de leitura de dados rotuladas na tela, com o nível intermediário demonstrado duas vezes, uma com barras destacadas em vermelho contra cinza e outra em amarelo contra cinza, antes das anotações com seta ancoradas em barras específicas (wwdc2022_110342, folha 0005, q0041 a q0044).
- Vínculo entre lista e gráfico demonstrado quadro a quadro: a linha de estatística ganha fundo verde sólido e a barra correspondente acima fica verde, e o destaque migra quando a linha selecionada muda (wwdc2022_110342, folha 0006, q0046 a q0049).
- Compensação de corpo entre larguras tipográficas: todas as linhas primeiro em 20 pts com larguras finais diferentes, depois ajustadas por estilo, de 42 pts na mais estreita a 20 pts na mais larga, para caberem na mesma medida horizontal (wwdc2022_110381, folha 0006, q0049 e q0050).
- Sinalização explícita de risco com triângulo amarelo de alerta, que entra primeiro sobre a coluna de parágrafo mais comprimida e depois também sobre a seguinte, marcando o texto longo que perde legibilidade (wwdc2022_110381, folha 0006, q0052 a q0054).
- Anatomia da letra isolada em quatro etapas, a palavra sem anotação, depois com linha pontilhada medindo a largura de cada estilo, depois com faixas de cor cobrindo as curvas internas, e por fim reduzida a formas de gota abstratas sem texto nenhum (wwdc2022_110381, folha 0005, q0037 a q0040).
- Em layout espelhado, o ícone do sol e o ícone de clima permanecem no mesmo canto físico nas duas versões enquanto o nome da cidade e os textos trocam de lado (wwdc2022_110441, folha 0003, q0026 e q0027).
- Comparação de ícone a ícone em slides de duas linhas rotuladas por idioma, um símbolo por quadro, mostrando que o documento com linhas de texto inverte e o ícone de busca mantém o cabo apontando para o mesmo lado nas duas versões (wwdc2022_110441, folha 0011, q0094 a q0099).
- O espaçamento entre letras anotado em porcentagem embaixo da frase permanece igual em três quadros e cresce a partir do quarto, alongando e rompendo as ligações da escrita cursiva até as letras se separarem artificialmente (wwdc2022_110441, folha 0009, q0076 a q0080).
- HUD de jogo com posições fixas por função, habilidades agrupadas no canto inferior direito, minimapa circular translúcido no canto superior esquerdo e caixa de missão no canto superior direito, e os números de dano passando de valor isolado a pilha sobreposta (wwdc2022_103, folha 0029, q0258 a q0261; folha 0030, q0265 e q0266).
- Ferramenta interna de teste sobreposta à arte final, com caixa de texto monoespaçado listando velocidade, modo de desenho e coordenadas sobre a cena, presente num quadro e ausente no anterior, ou seja, interface de desenvolvimento e não a tela entregue ao jogador (wwdc2022_103, folha 0029, q0255).
- Storyboard de protótipo de rastreamento corporal com nove esboços numerados em grade, marcadores vermelhos e estrelas amarelas nos pontos de captura e o último rotulado como pronto, seguido da pessoa executando os mesmos movimentos (wwdc2022_103, folha 0019, q0163 a q0166).
- Modal de instruções em grade três por três, cada célula com um boneco em pose numerada e marcação vermelha de ponto de contato, terminando num aviso de prontidão, e no quadro seguinte a pessoa executa o movimento no mesmo ambiente (wwdc2022_113, folha 0017, q0150 e q0151).
- Grade de exatamente nove avatares circulares como página fixa de conversas, repetida em dois acabamentos de caixa, coincidindo com o limite de nove conversas fixadas (wwdc2023_10026, folha 0006, q0053 e q0054).
- Diagrama de hardware justificando o sistema de layout, colunas rotuladas por geração com retângulos proporcionais e medidas de 38MM a 49MM sob cada uma, com um relógio físico sobreposto ao centro (wwdc2023_10138, folha 0009, q0079 e q0080).
- Espectro de imersão desenhado como três estágios lado a lado com a mesma silhueta, tela pequena e distante, tela curva parcial sobre um círculo no chão, e esfera em gradiente envolvendo a pessoa (wwdc2023_10072, folha 0015, q0127).
- O botão de sair da imersão fica numa pílula translúcida escura com seta diagonal no canto superior esquerdo e permanece no mesmo canto quando a cena se amplia, restando sozinho quando a barra de miniaturas some (wwdc2023_10072, folha 0019, q0165 e q0166; folha 0021, q0181 e q0182).
- A luz emitida pelo conteúdo é renderizada como reflexo colorido no tampo da mesa sob a janela, mais evidente na aproximação, e como halo na borda de um cartão de foto que cresce (wwdc2023_10072, folha 0013, q0111 e q0112; folha 0016, q0136 e q0137).
- Área de toque definida para a célula composta inteira, imagem mais texto, circundada por retângulo tracejado, e não para a seta visível ao lado dela (wwdc2023_10076, folha 0010, q0084 a q0086).
- Regra de canto concêntrico convertida em diagrama sobre um componente real, com contorno arredondado, círculo marcando o raio e o rótulo somando raio interno e padding sobre a mesma célula (wwdc2023_10076, folha 0011, q0097 e q0098).
- A forma de hover segue o card completo, capa mais texto, como elemento único: os quadros mostram primeiro as células sem contorno e depois cada uma contornada por inteiro (wwdc2023_10076, folha 0011, q0095 e q0096).
- Revelação de rótulo por foco do olhar, com a barra lateral de ícones expandindo o rótulo de compartilhar e, no quadro seguinte, um campo de busca com ícone de microfone ocupando o mesmo lugar (wwdc2023_10073, folha 0009, q0073 a q0075).
- Escala de esforço ocular em três níveis com dois tipos de sinal, olhar para baixo e para os lados aprovados com check verde e olhar para cima e na diagonal marcado com alerta laranja, um terceiro estado que não é nem certo nem errado (wwdc2023_10078, folha 0006, q0049 e q0050).
- Padrão repetitivo demonstrado como falha de convergência: primeiro os dois olhos convergem para o mesmo hexágono da malha, no quadro seguinte cada olho recebe uma cor diferente e converge para um hexágono diferente da mesma malha (wwdc2023_10078, folha 0004, q0029 e q0030).
- No StandBy o fundo do cartão se estende até preencher a tela inteira do aparelho na base, revelando um recorte preto em forma de pílula reservado à região do sensor, que o conteúdo não invade (wwdc2023_10194, folha 0007, q0058 a q0063).
- Colapso de layout por relevância em estados sucessivos: o placar perde a linha de texto do lance, fica esmaecido e substitui o relógio pelo nome do intervalo, reduzindo altura e informação sem trocar de componente (wwdc2023_10194, folha 0005, q0038 a q0040).
- O vão vazio dentro da vista compacta fica visível como espaço considerável entre o ícone à esquerda e o valor à direita da mesma pílula, por exemplo coração com número de um lado e silhueta do outro (wwdc2023_10194, folha 0015, q0129 e q0131).
- Progressão de detalhe entre tamanhos em três estados do mesmo conteúdo: ícone com tempo, depois cartão com nome da linha e estação, depois layout completo com selo de tempo e barra de progresso com as paradas nomeadas (wwdc2023_10194, folha 0016, q0137 a q0139).
- Bolha translúcida com brilho de borda usada como símbolo do limite do contexto compartilhado, com número variável de pessoas dentro, terminando em duas bolhas separadas com uma pessoa em cada (wwdc2023_10075, folha 0007, q0063; folha 0008, q0064 e q0072; folha 0012, q0108).
- Estado de compartilhamento comunicado por um selo em pílula fixado acima de cada janela, verde quando compartilhada e cinza quando não, com duas janelas de estados diferentes convivendo na mesma cena (wwdc2023_10075, folha 0004, q0033 a q0035; folha 0005, q0040 e q0043).
- Placeholder de espera desenhado como cartão de vidro fosco centralizado, com ícone de duas silhuetas, título, uma linha de instrução menor e um botão de ação, que some quando o conteúdo volta a ocupar a mesma tela (wwdc2023_10075, folha 0006, q0046 a q0050).
- Facilidade contra poder ilustrado por um micro-ondas e uma máquina de espresso profissional lado a lado, separados por uma linha vertical fina (wwdc2023_10115, folha 0003, q0023).
- Slide listando, em texto corrido separado por barras, os estados que um design dinâmico precisa resolver, de carregamento, modo escuro, leitor de tela, tipo dinâmico, estados pressionado, vazio e de erro, até layout da direita para a esquerda, localização, escala por aparelho, movimento reduzido e renderização de material (wwdc2023_10115, folha 0005, q0044 e q0045).
- O ícone de app desmontado em diagrama de três camadas rotuladas, as duas de primeiro plano exibidas sobre fundo xadrez para indicar transparência, antes de o ícone circular pronto aparecer com brilho e sombra (wwdc2023_10076, folha 0002, q0013 a q0017).
- O desenho para animação exibido em etapas vetoriais em traço preto, pontos soltos, contorno fechado de cabeça e corpo, círculos tracejados das patas sobrepostos e por fim as patas isoladas sem o corpo (wwdc2023_10197, folha 0011, q0091 a q0094).
- Tamanho da biblioteca comunicado por números grandes sobre textura de centenas de ícones pequenos, um valor emergindo discretamente e o valor maior aparecendo nítido antes de clarear (wwdc2023_10197, folha 0013, q0109 a q0116).
- O cartão de resultado de busca do sistema tem estrutura constante ao longo de todo o vídeo, rótulo pequeno no topo, cartão translúcido com de um a quatro ícones de ação e legenda curta sob cada um, seção de sugestões em lista abaixo e campo de busca com teclado na base (wwdc2023_10193, folhas 0001, 0002, 0005, 0006, 0007 e 0008).
- Os ícones de entidade repetem a forma que o conceito tem dentro do app, círculo para contatos e listas, quadrado para álbuns, carregando detalhes junto, como o coração no canto do álbum de favoritos (wwdc2023_10193, folhas 0005 e 0006).
- Orientação de cor entregue como amostra pura e sem rótulo, uma grade de doze losangos coloridos de cantos arredondados em três linhas de quatro (wwdc2023_10193, folha 0006, q0049).
- Slides de sessões relacionadas com padrão próprio, linha fina horizontal acima de cada item, nome da sessão à esquerda e código do evento alinhado à direita (wwdc2023_10193, folha 0007, q0057 e q0060).
