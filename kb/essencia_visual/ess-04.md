# ess-04, padrões visuais recorrentes

Base: 21 sínteses visuais lidas do começo ao fim, 4 páginas do HIG (widgets, windows, workouts, writing) e 17 vídeos (meet-with-apple 208, 254, 255, 256, 257, 270, 274; tech-talks 801, 802, 803, 10884, 111427, 111461, 111462, 111463, 111466; wwdc2014_223).

## A lista de tópicos fica na tela com o item corrente em branco e os demais apagados, e é ela que marca a virada de capítulo
- Evidência: meet-with-apple_270 (agenda de três tópicos com o item em curso destacado e submenus internos no mesmo padrão, folha 0001, q0003 a q0009)
- Evidência: meet-with-apple_274 (agenda em coluna ao lado do apresentador, item da seção em branco pleno e os outros em cinza, folha 0001, q0002 a q0009)
- Evidência: tech-talks_111462 (slides de agenda em preto e branco, sem ícone, repetidos quatro vezes ao longo do vídeo, folha 0003 q0019 e q0025, folha 0008 q0071, folha 0015 q0131)
- Evidência: tech-talks_10884 (lista de princípios primeiro inteira sobre dois relógios apagados, depois com o item da seção em negrito, folha 0001 q0008, folha 0008 q0064, folha 0009 q0073)
- Evidência: tech-talks_803 (os três princípios como trilha de progresso, terminando com os três em branco para sinalizar o fecho, folha 0001 q0005 e q0006, folha 0006 q0052)
- O que isso ensina sobre construir interface: estado de navegação pode ser comunicado só por peso e opacidade do texto, sem cor, sem ícone e sem moldura de seleção. A mesma lista serve de sumário, de indicador de posição e de transição, com um único atributo variando.

## Rótulo ligado por linha reta a uma parte da tela é o recurso padrão de anatomia, sempre sobre a interface já mostrada limpa antes
- Evidência: meet-with-apple_208 (linhas de chamada em Conversation Headers, Composer, Create Menu e Tab Bar, e no artigo Title, Byline, Image e Paragraph, com os rótulos entrando depois da tela limpa, folha 0023 q0203 para q0204, folha 0027 q0235 a q0238)
- Evidência: meet-with-apple_270 (anatomia da linha de lista desenhada com linhas retas ligando Image à miniatura, Subtitle ao texto secundário e Selection button ao círculo azul, folha 0008, q0068 a q0072)
- Evidência: tech-talks_111463 (rótulos didáticos posicionados fora da moldura do aparelho, ao lado da área que identificam, sem alterar a interface, folha 0013, q0114 a q0116)
- Evidência: tech-talks_10884 (rótulo de defeito com linha vertical apontando a borda esquerda, entre um quadro sem rótulo antes e outro sem rótulo depois, folha 0003, q0019 a q0021)
- Evidência: tech-talks_803 (callouts de seta um por quadro sobre a mesma captura de tela de oferta, folha 0004, q0031 a q0033)
- O que isso ensina sobre construir interface: a anotação nunca substitui a tela, ela entra e sai por cima de uma captura real que o leitor já viu intacta. Nomear cada região com o nome que o time usa é o que transforma um mockup em especificação.

## O julgamento de certo e errado vem em par visual, marcado por selo circular, check verde de um lado e X vermelho do outro
- Evidência: tech-talks_801 (o par de círculo vermelho com X e círculo verde com check aparece pelo menos seis vezes no mesmo formato, em rotação, ícones colados aos cantos, barra de rolagem e botão na área segura, folha 0005 q0037 e q0045, folha 0006 q0046 e q0047, folha 0007 q0056, q0057, q0061 e q0062)
- Evidência: meet-with-apple_270 (três graus na mesma sequência, alerta amarelo na barra com cinco abas rotuladas, X vermelho na barra customizada com pílulas coloridas e check verde na barra nativa com ícone e rótulo, folha 0003 q0024 a q0027, folha 0004 q0028 a q0034)
- Evidência: widgets (par de StandBy, o relógio e o Weather sem cartão recebem check verde, o Weather que mantém o cartão arredondado com sombra recebe X, img 1317 a img 1321)
- Evidência: tech-talks_111462 (check verde no bloco de código que usa contêiner de navegação e X vermelho no que instancia a barra diretamente, folha 0004, q0034 e q0035)
- Evidência: meet-with-apple_256 (dois telefones quase idênticos rotulados com e sem vidro aninhado, tornando visível a dupla translucidez que a fala só descreve, folha 0004, q0034 e q0035)
- O que isso ensina sobre construir interface: o errado vale mais quando é quase igual ao certo. Mudar uma variável só, manter tudo o resto congelado e carimbar o veredito faz o olho achar a diferença sem depender do texto.

## A mesma tela é repetida lado a lado com uma única variável mudando, e é a repetição que prova a regra
- Evidência: widgets (o mesmo widget pequeno de Stocks, layout idêntico, em cor plena, clara, tintada e monocromática, mudando só cor e opacidade, img 1296 a img 1300)
- Evidência: meet-with-apple_255 (a mesma tela do workspace em cinco variações de tema, estrutura idêntica, só cor de cabeçalho e de destaque mudando, folha 0006, q0047 a q0051)
- Evidência: meet-with-apple_257 (quatro iPhones rotulados iOS 12, 14, 18 e 26 com a mesma captura emoldurada, folha 0001, q0007 e q0008)
- Evidência: tech-talks_111461 (o mesmo conteúdo sob legenda de rodapé nomeando a versão de SDK, coluna única, grade de duas colunas e grade de quatro cartões, folha 0001 q0005 a q0009, folha 0002 q0010)
- Evidência: tech-talks_111466 (grade de seis renders do mesmo app em todas as poses do aparelho, repetida duas vezes com conteúdos diferentes, folha 0006 q0047 e q0048, folha 0011 q0093 e q0094)
- O que isso ensina sobre construir interface: se o layout aguenta trocar tema, geração de sistema, aparelho e pose sem se reorganizar, ele é sistema e não desenho. A prova é montar as variantes na mesma composição, não afirmar que funciona.

## Código e resultado ficam no mesmo quadro, com a linha em questão realçada e o realce se movendo enquanto o mockup fica parado
- Evidência: tech-talks_111462 (justaposição sistemática de comentário nomeando a API, trecho com realce de sintaxe e mockup ao lado, em dez folhas, com o realce azul trocando de trecho entre quadros enquanto o Mail fica idêntico, folha 0007, q0061 para q0062)
- Evidência: tech-talks_10884 (painel de código ao lado do relógio, com a linha do modificador de margem inserida e uma seta laranja ligando o trecho ao elemento correspondente na tela, folha 0003, q0022 a q0026)
- Evidência: tech-talks_111461 (painéis pareando SwiftUI e UIKit no mesmo quadro ou em sequência imediata, ao lado do render, folha 0003 q0024 e q0025, folha 0005 q0037 para q0038, folha 0006 q0052 a q0054)
- Evidência: meet-with-apple_270 (nome da API sobreposto ao próprio mockup como anotação, no título da tela e no botão em círculo azul preenchido, folha 0005 q0045, folha 0007 q0055 a q0058)
- Evidência: tech-talks_111463 (código montado linha a linha, com destaque azul temporário que some no quadro seguinte para sinalizar que a linha assentou, folha 0007, q0060 a q0063)
- O que isso ensina sobre construir interface: uma decisão de layout só fica transferível quando a pessoa vê qual linha produz qual pixel. Realce temporário dirige o olho melhor do que numeração ou legenda.

## Medida aparece escrita sobre o próprio desenho, em cotas e setas, e quase sempre a fala não diz o número
- Evidência: meet-with-apple_270 (guias azuis em colchetes ao redor do ícone hexagonal e anotações de 40px, 20px e 10px nas margens do cartão de conquista, com a fala sem citar valores, folha 0014 q0125 e q0126, folha 0015 q0127 e q0128)
- Evidência: tech-talks_801 (linhas, setas e números em azul claro sobre os contornos, com o mesmo par de blocos trocando a unidade entre quadros, primeiro pixels e depois pontos, folha 0001, q0008 para q0009)
- Evidência: tech-talks_802 (retângulos cotados em pixels para cada tamanho de relógio e especificação de ícone com medidas exatas em pixels e pontos para notificação e tela de início, folha 0001 q0004 a q0009, folha 0006 q0053)
- Evidência: tech-talks_10884 (a cota de 41 mm ao lado do par de caixas e as cotas de 41 mm e 45 mm juntas no render seguinte, folha 0001, q0004 e q0005)
- Evidência: windows (a abertura reduz a janela a uma silhueta sem conteúdo com setas de medida de duas pontas nas bordas direita e inferior, img 1324)
- O que isso ensina sobre construir interface: números de espaçamento e de tamanho pertencem à imagem, não à legenda. Quem constrói precisa da cota ao lado do elemento, com a unidade explícita, porque pixel e ponto não são intercambiáveis.

## Camadas de cor sólida ou semitransparente são coladas sobre a captura para tornar visível uma zona que não tem forma própria
- Evidência: tech-talks_802 (a estrutura da tela do watchOS é montada em zonas coloridas sobre um layout de exemplo, barra de título azul, faixa cinza de margem, faixa roxa de área de rolagem, e depois as faixas somem, folha 0003, q0019 a q0027)
- Evidência: tech-talks_801 (blocos verdes sólidos rotulados como área segura reaproveitados em contextos diferentes, e duas camadas de cor separando barra de navegação vermelha de conteúdo verde recuado, folha 0003 q0024 a q0027, folha 0004 q0029 para q0030)
- Evidência: tech-talks_111461 (verde preenchendo a tela inteira para demonstrar concentricidade sem conteúdo em volta, e azul semitransparente que muda de significado entre quadros, de toda a área de conteúdo para uma faixa estreita na borda esquerda, folha 0005 q0037 e q0038, folha 0006 q0052, folha 0007 q0055 a q0057)
- Evidência: tech-talks_111466 (faixa cinza sólida entre as colunas de texto rotulada como margem de layout e faixa azul na borda direita rotulada como recuo de área segura, trocando de cor e de posição de um quadro para o outro, folha 0006, q0050 e q0051)
- O que isso ensina sobre construir interface: margem, área segura e região reservada são retângulos invisíveis que governam o layout. Pintá-los com cores distintas, uma por conceito, impede que sejam confundidos entre si.

## O estado de interação fica registrado na diferença entre dois quadros consecutivos, com o resto do layout congelado
- Evidência: tech-talks_111462 (o ícone de caixa de entrada mostra um número solto ao lado e no quadro seguinte um badge circular vermelho sobre o próprio ícone, sem mais nenhuma mudança, folha 0012, q0107 para q0108)
- Evidência: meet-with-apple_257 (o mesmo cartão de gráfico de maré aparece plano e frontal num quadro e inclinado em perspectiva noutro, tornando visível o efeito que só surge durante o toque, folha 0004, q0033 e q0035)
- Evidência: meet-with-apple_208 (a célula da mensagem desliza e fica azul com a ação de manter como não lida, acima dos botões fixos, folha 0017, q0149 para q0150)
- Evidência: widgets (o mesmo widget de Reminders lado a lado, sete círculos vazios e depois o primeiro e o terceiro preenchidos em vermelho sólido, sem nenhuma outra mudança de layout, img 1307 e img 1308)
- Evidência: tech-talks_801 (três estados rotulados com o mesmo nome de comportamento, o indicador de início como linha fina, com círculo azul sugerindo o toque, e de volta à linha simples, folha 0008, q0065 a q0067)
- O que isso ensina sobre construir interface: estado se documenta por par, não por descrição. Congelar tudo o que não muda é o que faz o leitor enxergar a única coisa que muda.

## Placeholder e andaime reutilizam a geometria do conteúdo final em vez de deixar vazio
- Evidência: widgets (três barras amarelas mais claras de larguras decrescentes no cartão amarelo viram as três linhas de texto real na versão carregada, img 1312 e img 1313)
- Evidência: tech-talks_802 (a área de conteúdo preenchida em verde sólido sempre que o ponto é o espaço disponível e não o conteúdo, mais wireframes com placeholder de imagem em X e texto de preenchimento, folha 0001 q0004 e q0005, folha 0004 q0030 a q0033)
- Evidência: wwdc2014_223 (retângulos cinza cobrindo barra de navegação, miniaturas e tab bar da tela do app Música usada como andaime, e cinco células preenchidas pela repetição das mesmas poucas fotos, folha 0010 q0082 a q0085, folha 0011 q0091 a q0097)
- Evidência: workouts (métrica sem dado aparece preenchida com traços, mantendo o rótulo do ritmo médio no lugar, img 1335)
- O que isso ensina sobre construir interface: o vazio nunca é vazio, é a mesma caixa com preenchimento neutro. Isso mantém o ritmo e a altura de linha estáveis entre carregando, sem dado e carregado.

## A lista cresce item por item enquanto os anteriores ficam intactos, e cada item novo troca a imagem ao lado
- Evidência: meet-with-apple_255 (a fileira de princípios cresce de um para cinco, cada um com ilustração de boneco em desenho de linha e nome em texto pequeno abaixo, folhas 0003 e 0004, q0019 a q0032)
- Evidência: meet-with-apple_256 (a lista de aprendizados é construída item a item, sempre com uma imagem de exemplo diferente ao lado, folhas 0004 e 0005, q0034 a q0038)
- Evidência: tech-talks_111463 (o diagrama de contêineres se monta em camadas, contêineres de navegação em azul, depois de conteúdo em vermelho, depois de layout em verde inserido entre as duas faixas anteriores, folha 0009, q0073, q0078 e q0079)
- Evidência: tech-talks_802 (a tabela de escala tipográfica é construída em duas etapas, primeiro os estilos menores e depois os quatro maiores acrescentados acima, folha 0005, q0042 a q0044)
- Evidência: meet-with-apple_274 (os números de escala são revelados um a um da esquerda para a direita em cards de fundo verde escuro translúcido, folha 0002, q0016 a q0018)
- O que isso ensina sobre construir interface: revelação progressiva sem reflow. O que já entrou não se move, o que entra ocupa espaço já reservado, e a mudança de contexto acontece no painel ao lado.

## O vocabulário é fixado por diagrama abstrato antes de qualquer interface real entrar em cena
- Evidência: tech-talks_111461 (size class explicada primeiro por retângulos cinza com setas de medida, laranja na horizontal e azul na vertical, e formas sem rótulo representando o aparelho dobrado, antes de qualquer app, folha 0003 q0024 para q0025, folha 0004 q0028 a q0030)
- Evidência: wwdc2014_223 (dois retângulos rotulados Slide 1 e Slide 2 com círculos como elementos genéricos, ligados por uma seta cujo rótulo troca enquanto o desenho permanece o mesmo, e só então a captura real da ferramenta entra, folha 0021, q0181 a q0189)
- Evidência: tech-talks_801 (o fator de escala vira diagrama de três círculos de tamanho crescente com rótulos abaixo, associados a cada aparelho, antes de qualquer captura, folha 0001, q0003 e q0004)
- Evidência: tech-talks_10884 (o sistema de botões é apresentado como diagrama de duas colunas nomeadas, com código de cor por hierarquia, verde para primária, cinza para secundária e azul para toolbar, folha 0006, q0046 a q0050)
- Evidência: tech-talks_111463 (o conceito de arranjo é construído em três etapas de diagrama, caixa de entradas, caixa de saídas vazia e a seta ligando as duas já preenchidas, folha 0010, q0086 a q0088)
- O que isso ensina sobre construir interface: nomear a estrutura com formas vazias antes de mostrar o app impede que a pessoa confunda a regra com o exemplo. O diagrama isola a variável, a captura depois só confirma.

## A ferramenta de autoria entra em quadro com painéis e menus abertos, no ponto exato da opção sendo discutida
- Evidência: wwdc2014_223 (menus abertos de máscara em forma oval, de caracteres especiais e o diálogo de exportação com PNG escolhido, além do painel Arrange com tamanho e posição legíveis, folha 0010 q0089 e q0090, folha 0012 q0102 a q0104, folha 0015 q0130 e q0131, folha 0023 q0201 a q0205)
- Evidência: tech-talks_111427 (Figma com biblioteca de assets e camadas, Sketch com artboard nomeado por modelo de iPhone e o Icon Composer com painel de propriedades listando modo de renderização, gradientes, cor e fundo, folhas 0001 e 0003)
- Evidência: tech-talks_802 (o inspetor de atributos do Xcode com o atributo de fixar a view às bordas marcado, ao lado do relógio com o mesmo conteúdo da folha anterior, e o Asset Catalog com o painel de atributos em close, folha 0004 q0028, folha 0006 q0049 a q0052)
- Evidência: meet-with-apple_270 (a página de tab bars das diretrizes, a página de recursos de design com os templates e o app SF Symbols com categorias, grade de símbolos e seletor de peso, folha 0004 q0036, folha 0005 q0037 a q0041)
- Evidência: tech-talks_10884 (a tela do laptop mostra o editor de cor de destaque e o navegador de arquivos do projeto antes de a cena voltar ao painel de código, folha 0005, q0042 a q0045)
- O que isso ensina sobre construir interface: mostrar onde a opção mora na ferramenta é parte da instrução. Sem o painel aberto, a regra fica sabida e não executável.

## Cartão de texto puro sobre preto pontua a apresentação, uma frase curta por quadro e nenhuma imagem de apoio
- Evidência: meet-with-apple_274 (os cartões de transição seguem sempre o mesmo modelo, frase curta única alinhada à esquerda, branco sobre preto, sem imagem, folha 0004, folha 0008 q0066 a q0071, folha 0009)
- Evidência: tech-talks_111462 (uma instrução ganha um cartão tipográfico só dela, texto branco grande centralizado sobre preto, entrando por fade de baixo contraste para branco pleno, folha 0010, q0088 para q0089)
- Evidência: tech-talks_111463 (cards de título em branco sobre preto funcionam como índice paralelo à fala, com hierarquia por tamanho e peso, folha 0003 q0022 e q0027, folha 0006 q0048, folha 0013 q0110, folha 0014 q0125)
- Evidência: tech-talks_111466 (cartões de título pretos com duas linhas, uma em cinza e outra em branco, abrem o vídeo e reaparecem idênticos na virada de seção, folha 0001 q0004, folha 0006 q0046)
- Evidência: tech-talks_802 (cards de texto branco isolado marcam a estrutura entre os blocos visuais, incluindo o título de layout e o de produção gráfica, folhas 0002, 0004, 0005 e 0006)
- O que isso ensina sobre construir interface: uma tela inteira dedicada a uma frase é um recurso de ritmo. O contraste máximo e a ausência de qualquer outro elemento fazem a pausa, sem precisar de animação.

## Resultado se prova com um número gigante e uma legenda mínima, de preferência no formato antes e depois
- Evidência: meet-with-apple_208 (estatísticas em serifada grande com dois sinais de maior entre valor antigo e novo, e legenda pequena sem serifa, folha 0015, q0129 a q0132)
- Evidência: meet-with-apple_254 (tempo de compilação e tamanho do app em tipografia grande no formato antes e depois ligado por seta dupla, e uso de busca reduzido a um multiplicador único, folha 0007, q0059 a q0061)
- Evidência: meet-with-apple_274 (slides de estatística com o maior tipo da folha, percentual em verde saturado, seta cinza para baixo à esquerda e legenda branca abaixo, alinhados à esquerda sobre preto, folha 0007, q0056 a q0060)
- Evidência: tech-talks_803 (o dado de conversão vira gráfico de barras duplo com rótulo numérico acima de cada barra e legenda de cor por métrica, reaproveitado em três enquadramentos e depois escurecido para virar fundo da frase de conclusão, folha 0003, q0022 a q0025)
- O que isso ensina sobre construir interface: hierarquia extrema entre valor e rótulo, com o número dominando a composição, é o mesmo princípio dos widgets de dado único. O par antes e depois carrega a comparação sem precisar de eixo nem de escala.

## A cor tem função fixa dentro do sistema apresentado, nunca decora
- Evidência: tech-talks_10884 (o diagrama de botões usa verde para ação primária, cinza para secundária e dismiss, azul para toolbar, e nos renders a cor segue a função, vermelho para parar, laranja para adicionar, verde para iniciar, folha 0006 q0046 a q0050, folha 0007 q0059 a q0063)
- Evidência: workouts (quatro botões em grade dois por dois, cada um com cor e ícone da função, encerrar em vermelho, retomar em amarelo oliva, novo em verde, segmento em cinza, img 1334)
- Evidência: meet-with-apple_270 (a cor de destaque indigo é anotada em dois usos de estado na mesma tela, concluído nos checks e aba selecionada, enquanto o verde-limão fica restrito a barras de progresso como cor não semântica, folha 0013 q0112 a q0117, folha 0014 q0120 a q0123)
- Evidência: tech-talks_111463 (a cor codifica a família de contêiner no diagrama, azul para navegação, vermelho para conteúdo, verde para layout, e o item destrutivo do menu de contexto fica em vermelho no fim da lista, folha 0004 q0031, folha 0009 q0073 a q0079)
- Evidência: widgets (no widget de Stocks o verde semântico de alta desaparece quando a aparência tintada aplica um único roxo a fundo, texto e gráfico, img 1296 a img 1298)
- O que isso ensina sobre construir interface: uma cor deve significar sempre a mesma coisa dentro de uma tela e entre telas. Quando o modo de exibição apaga a cor semântica, a informação precisa sobreviver noutro canal.

## A estrutura permanece e só a densidade muda quando a tela cresce, com colunas entrando em vez de tipos aumentando
- Evidência: widgets (a progressão de tamanho do widget de Calendário é feita por acréscimo de colunas e de régua de horas, não por aumento de fonte, e o extra grande estende a régua a quatro dias, img 1287 a img 1290)
- Evidência: meet-with-apple_257 (no iPad, barra lateral fixa com busca e seções mais grade de cartões à direita, e no iPhone os mesmos cartões empilhados verticalmente, folha 0005, q0045)
- Evidência: tech-talks_111466 (a mesma tela de edição de lista ganha colunas adicionais de ícones ao passar do aparelho estreito para o largo, e depois divide o espaço com a lista de tarefas quando dobrado, folha 0011, q0097 a q0099)
- Evidência: tech-talks_111461 (o mesmo conteúdo em coluna única, em grade de duas colunas com um cartão a mais e em grade de quatro cartões, conforme o SDK, folha 0001 q0005 a q0009, folha 0002 q0010)
- Evidência: widgets (no visionOS a mesma cena adapta densidade à distância, de longe capa e texto pequeno, de perto um bloco extra com quatro linhas de nomes de faixa, img 1322 e img 1323)
- O que isso ensina sobre construir interface: mais espaço é mais informação, não informação maior. A unidade que se multiplica é a coluna, a linha ou a seção, e a escala tipográfica fica onde está.

## Controles translúcidos flutuam sobre o conteúdo em vez de ocupar barra opaca própria
- Evidência: meet-with-apple_208 (player com três botões circulares translúcidos sobre conteúdo colorido, barra inferior com cinco ícones circulares translúcidos sobre foto e chips de filtro em pílula, folha 0002 q0017, folha 0004 q0032 e q0033)
- Evidência: meet-with-apple_254 (círculos pequenos com ícone central marcando pontos de interesse sobre a foto de produto e barra de navegação lateral translúcida ancorada à esquerda sem tapar o conteúdo fotográfico, folha 0006, q0046, q0048 e q0049)
- Evidência: widgets (o formato acessório inline aparece como uma única linha numa faixa translúcida, sem cartão, e o circular usa ícone pequeno sobre círculo translúcido, img 1292 e img 1294)
- Evidência: windows (a janela do visionOS flutua sobre a sala com fundo de vidro que deixa o ambiente transparecer levemente, img 1330)
- O que isso ensina sobre construir interface: quando o conteúdo é a foto ou o mapa, o cromo precisa ceder espaço óptico. Translucidez mais forma circular ou em pílula mantém a leitura do controle sem cortar um retângulo do conteúdo.

## Os controles se ancoram na borda externa e mudam de eixo sem mudar de ordem
- Evidência: tech-talks_111466 (a coluna presa à borda direita se repete quase idêntica em pelo menos cinco apps do sistema, e-mail, chamadas, lembretes, FaceTime e música, folha 0003 q0019 a q0026, folha 0004 q0028, folha 0012 q0108)
- Evidência: tech-talks_111462 (o mesmo app aparece com a barra de abas horizontal no rodapé e depois com os mesmos três ícones empilhados na borda direita, na mesma ordem, com cabeçalho e lista inalterados, folha 0003, q0023 e q0027)
- Evidência: meet-with-apple_254 (barra de ações vertical na borda direita do conteúdo em tela cheia, ícones translúcidos empilhados com contador numérico abaixo de cada um, padrão que reaparece em várias telas, folhas 0001, 0005 e 0006, q0004 e q0041)
- Evidência: tech-talks_111466 (nos pares de tela dividida cada metade ancora os próprios controles na borda externa, e a troca de posição entre os dois apps mantém essa ancoragem, folha 0005, q0037 a q0040)
- O que isso ensina sobre construir interface: a barra de ações é um conjunto ordenado que pode girar de horizontal para vertical sem reordenar nem renomear. Ancorar na borda externa, e não na borda de leitura, é o que mantém o alcance do polegar em qualquer pose.

## A linha de lista tem sempre a mesma anatomia, ícone à esquerda, rótulo ao centro e controle ou chevron à direita
- Evidência: meet-with-apple_257 (o mesmo alinhamento à esquerda em três telas diferentes, detalhe de estação, suporte e ajustes, com ícone colorido em quadrado arredondado, rótulo e ação à direita, seja chevron, botão ou alternador, folha 0005 q0041, folha 0007 q0060)
- Evidência: meet-with-apple_208 (tela de ajustes com ícone colorido à esquerda e chevron à direita em cada item, e menu escuro com ícones à esquerda dos itens e interruptores à direita, folha 0004 q0035, folha 0038 q0335)
- Evidência: meet-with-apple_270 (catálogo de controles em linhas nomeadas, botão pop-up, stepper, toggle e slider, todos na mesma estrutura de linha, folha 0009, q0073)
- Evidência: writing (o rótulo de configuração é um cartão em fundo preto com título curto à esquerda e interruptor verde à direita, e uma frase de apoio em cinza claro abaixo, img 1341)
- O que isso ensina sobre construir interface: essa linha é o componente mais reutilizado do sistema. Ícone, rótulo e controle terminal formam um gabarito único que absorve ajustes, ações, navegação e itens destrutivos sem inventar layout novo.

## Novidade recebe selo dentro do próprio slide, acrescentado num quadro seguinte sem alterar o conteúdo
- Evidência: tech-talks_111462 (selo circular verde acrescentado ao quadro seguinte sem mudar o código mostrado, e depois sobreposto ao mockup do aparelho, folha 0014, q0119 para q0120 e q0122)
- Evidência: tech-talks_111461 (selo retangular no canto superior direito do slide que traz um rótulo de código, e selo circular verde com o número da versão no slide seguinte, folha 0008, q0064, q0065, q0069 e q0070)
- Evidência: tech-talks_111463 (selo circular verde entrando junto com a linha destacada de consulta de regiões, e depois no diagrama de contêineres de layout, folha 0007 q0060 a q0063, folha 0009 q0079)
- O que isso ensina sobre construir interface: o selo é uma camada que entra e sai, não parte do conteúdo. Isso permite reaproveitar o mesmo slide depois que a novidade deixa de ser nova, apenas removendo a marca.

## A cor de marca do app invade o material de apresentação da Apple e os componentes de sistema
- Evidência: meet-with-apple_255 (slide de seção em gradiente roxo e magenta com o ícone do app à direita, e o pano de fundo do palco na mesma família de cor em boa parte do vídeo, folha 0001 q0006 a q0008, folha 0008)
- Evidência: meet-with-apple_274 (o verde do logotipo se repete como acento nos números de estatística, nos selos circulares das perguntas e no encerramento, folhas 0007, 0010 e 0011)
- Evidência: widgets (na galeria, o botão de adicionar widget aparece na cor de marca do app, amarelo no Notes e azul no Weather, com o cartão modal idêntico nos dois, img 1314 e img 1315)
- Evidência: meet-with-apple_254 (selo circular do design system com indicador percentual e paleta de swatches quadrados ao lado de uma tela com barra de abas de três itens, folha 0003, q0019)
- O que isso ensina sobre construir interface: a identidade entra por acento e por um punhado de elementos, não por reescrever o componente. O cartão, a barra e o botão continuam sendo os do sistema, só a cor de destaque muda.

## Esboço e protótipo aparecem como etapa do trabalho, com os estágios contáveis na imagem
- Evidência: wwdc2014_223 (uma folha coberta de dezenas de wireframes a caneta aparece como fotografia, com pontos azuis marcando quatro esboços específicos e uma lupa circular ampliando o de lista, folhas 0007 a 0009, q0055 a q0073)
- Evidência: meet-with-apple_270 (post-its reais em estágios contáveis, 14 notas soltas no brainstorm, 8 depois de simplificar, três aglomerados e por fim rotulados com cinco, duas e uma nota, sem que a fala dê as contagens, folha 0002, q0013 a q0018)
- Evidência: meet-with-apple_208 (a mesma lista de canais repetida em três iPhones para comparar três cabeçalhos prototipados, concêntrico, cápsula e gradiente, com a anatomia da lista constante, folha 0021, q0183 a q0187)
- Evidência: tech-talks_111461 (uma ferramenta de design no Mac reaparece duas vezes para prototipar as poses do aparelho com o mesmo conteúdo, aberto, fechado e em formato de livro, folha 0002 q0011 a q0013, folha 0007 q0060 e q0061)
- O que isso ensina sobre construir interface: exploração se mostra em volume e em redução, e a contagem de opções é informação. Prototipar a variante estrutural antes do acabamento é o que permite comparar três cabeçalhos com a mesma lista embaixo.

## Concentricidade, os cantos internos acompanham a curvatura do aparelho
- Evidência: meet-with-apple_257 (no slide sobre concentricidade aumentada os cantos dos cartões internos acompanham a curvatura dos cantos do próprio dispositivo, algo que a fala só trata em abstrato, folha 0007, q0058)
- Evidência: tech-talks_111461 (o verde preenche a tela inteira com os cantos coincidindo com o contorno do aparelho, sem conteúdo de app em volta, e o código pareia a forma concêntrica em SwiftUI com a configuração de canto em UIKit, folha 0005, q0037 para q0038)
- O que isso ensina sobre construir interface: o raio de canto de um elemento colado à borda é derivado do raio da tela e do afastamento, não escolhido à mão. Demonstrar isso com uma cor chapada, sem conteúdo, isola a geometria.

## O encerramento é padronizado, três ações concretas e o logotipo, com o mesmo template em toda a série
- Evidência: tech-talks_111461 (o encerramento lista três ações concretas em tipografia branca sobre preto, folha 0009, q0073)
- Evidência: tech-talks_111462 (o encerramento repete o padrão da agenda, com o título e três ações surgindo abaixo dele, folha 0020, q0172 para q0173)
- Evidência: tech-talks_111463 (a lista final de recomendações é construída item a item mantendo os anteriores, com o nome de API diferenciado por fonte monoespaçada e fundo destacado, folha 0014 q0126, folha 0015 q0127 e q0128)
- Evidência: tech-talks_802 (a página de recursos do site aparece antes do slide final preto com o logotipo e o aviso de direitos autorais, folha 0007, q0055 a q0057)
- Evidência: meet-with-apple_256 (o slide de título e o quadro de encerramento com o logotipo seguem o mesmo template dos outros vídeos do grupo, folhas 0001 e 0007, q0059)
- O que isso ensina sobre construir interface: fecho é componente, não improviso. Três ações, um link de referência e a assinatura visual da série, sempre no mesmo lugar, tornam o material reconhecível e reaproveitável.

## As aberturas de página do HIG são ilustrações monocromáticas construídas sobre grade e círculos guia visíveis
- Evidência: workouts (a capa é uma figura correndo em silhueta vermelha sobre fundo laranja, com guias retangulares e circulares de construção, incluindo um círculo centrado no torso, img 1333)
- Evidência: writing (abertura monocromática amarela, prancheta de cantos arredondados atravessada na diagonal por um lápis, sobreposta a linhas de grade retangulares e a um círculo guia central, na mesma lógica das aberturas de outras páginas, img 1338)
- Evidência: windows (a abertura reduz a janela a uma silhueta sem conteúdo, com três botões redondos, bolhas translúcidas e setas de medida nas bordas, img 1324)
- O que isso ensina sobre construir interface: as próprias ilustrações da Apple deixam a grade de construção à vista, uma cor por tema. Reduzir o assunto a silhueta e guias é o que faz cada capa parecer da mesma família sem repetir desenho.

## Achados de fonte única

- A hierarquia tipográfica de uma mesma tela é anotada duas vezes, primeiro por estilo do sistema e depois por variante da família, com título em uma largura, subtítulo em outra e legendas em condensada (meet-with-apple_270, folha 0011 q0095 a q0099 e folha 0012 q0100 a q0108).
- A escala tipográfica completa vem como tabela em grade, cruzando categoria de tamanho de conteúdo nas colunas com estilo de texto nas linhas e o valor em pontos em cada célula, e logo depois a tela de sistema com o controle deslizante de tamanho aparece sobreposta à tabela desfocada, ligando a especificação ao controle que a pessoa usa (tech-talks_802, folha 0005, q0042 a q0045).
- O checklist dos oito elementos obrigatórios de uma tela de assinatura aparece em coluna ao lado da captura real, transformando os callouts pontuais anteriores em lista fechada (tech-talks_803, folha 0004, q0034).
- O mesmo modal de oferta reaparece com título e foto trocados e estrutura, hierarquia e posições idênticas, evidenciando que é gabarito reutilizável e não tela única (tech-talks_803, folha 0002, q0014 para q0015).
- Os parâmetros de animação são tratados como controles de design de produto, com valores legíveis na tela, duração de 0,60 s, direção de baixo para cima, início ao clique, atraso de 0,50 s, e no painel de transição inteligente a opção de casar por objeto, palavra ou caractere com aceleração suavizada nas duas pontas (wwdc2014_223, folhas 0019, 0022 e 0025, q0168 a q0171 e q0190 a q0192).
- A escala física é conferida encenando a comparação, com o documento em zoom reduzido a 25 por cento no laptop ao lado de um iPhone real segurado na mão, na mesma cena (wwdc2014_223, folha 0013, q0114 a q0117).
- O tamanho do documento é customizado por peça em vez de usar um slide padrão, 640 por 1136 para a tela cheia, 640 por 2020 para a lista comprida e 1000 por 1000 para o mapa (wwdc2014_223, folhas 0031 e 0033, q0277 e q0291 a q0296).
- O alinhamento do texto falso é feito por gabarito de transparência, com o fundo virando semitransparente para o texto do app de referência ressurgir por trás e servir de guia de posição e de corpo antes de digitar por cima (wwdc2014_223, folha 0011, q0097 a q0099).
- O design system é auditado como catálogo em modo debug, quatro telas rotuladas por componente com todas as variações empilhadas, alertas, chips, emblemas e botões, exibido em modo claro e depois escuro só com fundo e superfícies invertidos (meet-with-apple_274, folha 0006, q0049 a q0054).
- A arquitetura de informação é auditada por diagrama de árvore com nós retangulares coloridos por categoria em colunas hierárquicas e os nós de topo em amarelo, com rótulos de fluxo por tarefa (meet-with-apple_254, folha 0003, q0021 a q0026).
- Mensagens internas do próprio time viram material de slide, bolhas com avatar circular, nome em negrito, timestamp, corpo e reações, empilhadas em cascata e listando os alvos de redesenho (meet-with-apple_255, folha 0005, q0038 e q0039).
- A permanência da ancoragem em idioma da direita para a esquerda é provada por dois calendários lado a lado, um em inglês e outro em árabe, com o texto espelhando e a coluna de ícones ficando na borda direita nos dois (tech-talks_111462, folha 0007, q0055).
- As reticências recebem tratamento de símbolo reservado, com um quadro inteiro só para os três pontos ampliados sobre preto e depois o mesmo símbolo na base de um painel vertical, separado dos demais por um leve espaço (tech-talks_111462, folha 0017, q0145 e q0150).
- O caso de desativar a barra lateral é mostrado pela calculadora, cuja grade numérica compacta vira faixa horizontal alargada no aparelho dobrável mantendo a mesma contagem de botões (tech-talks_111462, folha 0019, q0164).
- A dobradiça vira divisor de layout, com elementos flutuantes saindo do centro para a faixa da dobra, o diálogo de nova pasta e os controles de transporte do player descendo para esse eixo (tech-talks_111463, folha 0005, q0037 a q0044).
- Um app imersivo é a exceção declarada ao recuo, com o círculo verde centralizado no aparelho estreito passando a preencher a tela inteira no aparelho aberto, enquanto os demais exemplos mantêm o conteúdo afastado dos controles (tech-talks_111466, folha 0009, q0077 para q0078).
- O teclado do watchOS é desenhado sem contornos ao redor das teclas, com o ícone de apagar dentro do campo de texto e não entre as teclas, e um ícone de chave sinalizando contexto de senha (tech-talks_10884, folha 0009, q0074 a q0076).
- A altura extra de um display novo é isolada como faixa verde no topo do bloco, separada da parte azul compartilhada com o display menor, com as três cotas anotadas, em vez de aparecer apenas como um número maior (tech-talks_801, folha 0002, q0010).
- Capturas do mesmo app são empilhadas com transparência e alinhadas para comparar tamanhos, a lista de favoritos em três camadas e a barra de abas de cinco ícones em quatro camadas alinhadas (tech-talks_801, folha 0002 q0017 e q0018, folha 0003 q0020).
- As páginas de diretriz seguem template fixo, título grande do componente, parágrafo de definição, caixa lateral de plataformas suportadas com ícones de dispositivo e um cartão de exemplo em fundo gradiente cuja cor muda conforme o componente (tech-talks_111427, folha 0005, q0038 a q0041).
- O único fluxo de captura de dado mostrado é a janela do Feedback Assistant, com barra lateral de itens salvos, formulário de campos rotulados empilhados, dois menus de triagem, zona de arrastar arquivo e botão de envio em roxo sólido contra um secundário em cinza (tech-talks_111427, folha 0007).
- No macOS os três estados de janela são diferenciados por três canais ao mesmo tempo, cor dos botões, profundidade do empilhamento e rótulo de texto, e a janela chave da ilustração é o painel de cores, não a janela principal do app (windows, img 1327).
- No visionOS os dois estilos de contêiner são distinguidos pela forma antes de qualquer conteúdo, a janela como plano fino duplo e inclinado em azul monocromático com contornos tracejados e o volume como cubo translúcido de faces tracejadas com a face inferior mais sólida (windows, img 1328 e img 1329).
- Uma mesma mensagem muda de tom por cor, temperatura e composição junto com as palavras, o aviso grave em degradê azul e roxo escuro com o botão de emergência acima do botão de dispensar, e a conquista em fundo colorido desfocado com anel de atividade e número concreto (writing, img 1339 e img 1340).
- A frase de apoio de um interruptor descreve apenas o que acontece com a função ligada, sem explicar o estado desligado (writing, img 1341).
- No Apple Watch o mesmo cartão de evento recebe três tratamentos conforme o contexto, faixa com fundo texturizado bege e traço rosa claro, complicação retangular com fundo preto sólido e traço vermelho, e cartão claro flutuando destacado sobre o preto no Smart Stack (widgets, img 1303 a img 1305).
- Em pouca luz o StandBy passa tudo a vermelho monocromático, inclusive os números do mostrador, e o widget no visionOS ganha moldura branca espessa, sombra e profundidade preservando as cores plenas (widgets, img 1299 a img 1302 e img 1317 a img 1321).
- Três telas de um mesmo fluxo no Watch usam o fundo preto e a hora no canto superior como âncora comum, variando só o conteúdo central entre grade de botões, pilha de métricas e controles de reprodução, com indicadores de página em pontos mudando de posição entre elas (workouts, img 1334 a img 1336).
- A instrução de produção gráfica aparece escrita em cartão de texto, preparar o gráfico em escala 2x e salvar como PDF (tech-talks_802, folha 0006).
- Um quadro isolado abandona o mockup e usa metáfora espacial, controles em cápsulas soltas flutuando em perspectiva sobre um piso quadriculado, agrupados por proximidade, com o botão vermelho à parte, sem equivalente em nenhuma outra folha do vídeo (tech-talks_111462, folha 0009, q0074).
- O ponto exato em que a demonstração deixa de ser real e passa a ser encenada fica visível, a prévia de câmera apontada para o prato troca, no toque do obturador, por uma foto estática dentro da tela de postagem, e depois uma grade de dezoito miniaturas quase idênticas dessa mesma tela funciona como storyboard quadro a quadro (wwdc2014_223, folhas 0036 e 0037, q0316 a q0328).
- Uma interface de agente de código integrada ao editor aparece na tela sem ser nomeada na fala, com balão de prompt pedindo boas práticas de redimensionamento e uma linha de status de atualização em andamento (tech-talks_111461, folha 0008, q0069 para q0070).
