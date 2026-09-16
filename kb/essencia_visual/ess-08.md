# ess-08: padrões visuais recorrentes

Lote de 16 vídeos (WWDC 2020 e 2021), lido a partir das sínteses visuais folha a folha.

## O índice da sessão vive na tela como coluna persistente, com o item corrente aceso e os anteriores apagados em cinza
- Evidência: wwdc2020_10175 (folha 0001, q0007 a q0009; folha 0021, q0187 a q0189)
- Evidência: wwdc2021_10097 (folha 0002, q0010 a q0014; retornos nas folhas 0005, 0007, 0009 e 0014)
- Evidência: wwdc2021_10275 (folha 0004, q0031; folha 0017, q0147; folha 0028, q0248 a q0250)
- Evidência: wwdc2021_10245 (folha 0001, q0007; folha 0008, q0068 a q0070; folha 0015, q0127 a q0129)
- Evidência: wwdc2021_10126 (folha 0003, q0025 e q0026)
- Evidência: wwdc2021_10184 (folha 0002, q0016 a q0018; folha 0005, q0043 e q0044)
- Evidência: wwdc2020_10640 (folhas 0001 e 0013)
- Evidência: wwdc2021_10250 (folha 0001, q0004 a q0007; folha 0013, q0117)
- O que isso ensina sobre construir interface: orientação dentro de um fluxo longo não precisa de barra de progresso nem numeração, basta manter a lista inteira visível e variar peso e opacidade do item atual. Vários registros anotam que a fala não menciona esse recurso, ou seja, ele carrega sozinho a função de "onde estou".

## Cada regra vem acompanhada do par certo e errado, selado por círculo verde de check e vermelho de X no mesmo enquadramento
- Evidência: wwdc2020_10206 (folha 0024, q0208 a q0216, com os itens revelados um a um ao lado de dois aparelhos)
- Evidência: wwdc2020_10640 (folha 0005; folha 0017, q0146 a q0150; folha 0025, q0217 e q0218)
- Evidência: wwdc2021_10250 (folha 0008, q0064 a q0069; folha 0017, q0146 a q0148)
- Evidência: wwdc2020_10207 (folha 0006, q0049 a q0052; folha 0016, q0141)
- Evidência: wwdc2021_10097 (folha 0008, q0069 e q0070, "Path" aprovado contra "Stroked path" reprovado)
- Evidência: wwdc2021_10126 (folha 0009, q0077 e q0078)
- Evidência: wwdc2020_10175 (folha 0009, q0079 a q0081, X cinza e visto verde aplicados ao código e ao resultado ao mesmo tempo)
- O que isso ensina sobre construir interface: a norma só fica clara quando o desvio é mostrado junto. O selo é um elemento estranho à interface, sobreposto de fora, e isso é proposital: separa o julgamento do produto. O par eficaz isola uma variável, mantendo todo o resto idêntico entre os dois lados.

## A medida é desenhada sobre o próprio elemento, em guias e réguas coloridas com o valor em pontos ao lado
- Evidência: wwdc2020_10640 (diâmetro "19pt" ao lado do ponteiro, folha 0004, q0033; padding de 12pt com bezel contra 24pt sem bezel, folha 0018; raios de 21pt, 15pt e 8pt em vermelho, folha 0019; traço de 4.5pt contra 1pt, folha 0025)
- Evidência: wwdc2021_10250 (folha 0003, q0024, linhas guia azuis rotuladas "left-margin Regular-M" e "right-margin Regular-M")
- Evidência: wwdc2020_10207 (folha 0016, q0136 a q0139, guias verticais verde água numeradas, caixas laranja pontilhadas e guias tracejadas amarelas de centralização)
- Evidência: wwdc2021_10029 (folha 0021, q0183 e q0184, réguas azuis de 800px e 400px sobre a foto)
- Evidência: wwdc2020_10175 (folha 0002, q0015 e q0016, barras verticais coloridas marcando espaçamento entre letras; folha 0004, q0029 a q0032, barras horizontais como réguas junto ao glifo)
- Evidência: wwdc2021_10275 (folha 0023, q0205 a q0207, razões de contraste anotadas sobre a mesma caixa de diálogo em duas versões)
- O que isso ensina sobre construir interface: número solto numa tabela não convence, número ancorado no pixel que ele governa convence. Quando a medida aparece por cima do desenho, a decisão fica auditável e replicável por quem for implementar.

## Linhas de chamada com rótulo nomeiam a parte da interface direto sobre a captura real
- Evidência: wwdc2020_10206 (folha 0004, q0028 a q0034, "Empty space" apontando a área vazia e depois "Fill with content" e "Fast navigation" empilhados)
- Evidência: wwdc2020_10205 (folha 0013, q0112 a q0117, "Currently selected color" e "Saved colors")
- Evidência: wwdc2021_10029 (folha 0012, q0103 e q0105, "Safe area" e a variável de inset apontando a faixa verde; folha 0013, q0111, quatro rótulos ligados às quatro bordas)
- Evidência: wwdc2021_10097 (folha 0013, q0115, "Accent" e "Multicolor" apontando partes distintas da mesma pasta; folha 0008, q0072, "Emphasize" ligado à seta)
- Evidência: wwdc2021_10275 (folha 0023, q0199 a q0201, rótulos ligados a dois pontos coloridos; folha 0020, q0173 a q0178, rótulo ligado à seção nova de festival)
- Evidência: wwdc2021_10126 (folha 0005, q0038 e q0039, linha cinza ligando o ícone de três traços ao seu nome)
- Evidência: wwdc2021_10184 (folha 0005, q0037 e q0038, seta desenhada apontando um ícone pequeno que passaria despercebido)
- Evidência: wwdc2021_10081 (folha 0002, q0016 a q0018, chamada apontando o selo de suporte a controle no card da App Store)
- O que isso ensina sobre construir interface: nomear o elemento na imagem é o que transforma uma captura em documentação. Vale tanto para apontar o problema quanto para apontar a solução, e funciona melhor quando o rótulo fica fora do elemento, ligado por linha fina neutra, sem cobrir a interface.

## O argumento é a diferença entre dois quadros consecutivos, com uma variável trocada e todo o resto congelado
- Evidência: wwdc2021_10029 (folha 0003, q0021 a q0023, a meta tag entra e a barra do navegador vira de amarelo para verde; folha 0009, a faixa de newsletter some e a cor passa a preencher sem interrupção)
- Evidência: wwdc2020_10175 (folha 0015, q0127 a q0129, o mesmo parágrafo com leading apertado e depois folgado)
- Evidência: wwdc2021_10278 (folha 0008, q0069 a q0071, o retângulo de destaque cobre o caminho do arquivo de áudio e o valor muda entre um quadro e o outro)
- Evidência: wwdc2021_10275 (folha 0006, q0047 a q0053, a lista mantém checkbox e pontos de categoria enquanto cada item é reescrito; folha 0007, q0056 a q0060, a grade de duas colunas fica e só fotos e nomes trocam)
- Evidência: wwdc2020_10640 (folha 0016, q0137 e q0138, o botão sem destaque e depois com halo azulado)
- Evidência: wwdc2021_10126 (folha 0007, q0055 a q0059, a lista de funcionalidades e a tela do protótipo mudam em sincronia)
- O que isso ensina sobre construir interface: comparação limpa exige congelar o contexto. Quando duas coisas mudam ao mesmo tempo, a demonstração perde o poder de prova, e é por isso que praticamente toda comparação do lote reaproveita o mesmo layout, o mesmo texto de exemplo e o mesmo enquadramento.

## Código e resultado renderizado ficam lado a lado, com um retângulo de destaque saltando de trecho em trecho
- Evidência: wwdc2021_10029 (folhas 0003, 0004, 0007 a 0010 e 0012 a 0016; a ordem dos lados chega a inverter entre blocos, código à esquerda na folha 0003 e à direita nas folhas 0008 a 0010)
- Evidência: wwdc2021_10081 (folha 0010, q0085 a q0088, o mesmo bloco Swift fica parado enquanto o destaque cinza percorre declaração, condição e os dois blocos de efeito)
- Evidência: wwdc2021_10278 (folha 0007, q0057 a q0060; folha 0010, q0085 e q0086; folha 0012, q0102, com o destaque passando de uma linha isolada para um bloco inteiro)
- Evidência: wwdc2020_10207 (folha 0008, q0064 a q0067, progressão de código em três passos com a prévia ao lado)
- Evidência: wwdc2020_10175 (folha 0020, q0173 a q0180, a construção em SwiftUI avança de texto centralizado até a pilha com margem lateral)
- O que isso ensina sobre construir interface: o destaque móvel resolve o problema de dizer onde olhar sem recortar o contexto. Vale registrar o limite honesto do recurso, anotado em wwdc2020_10175: em várias sequências o resultado renderizado fica idêntico enquanto o código cresce, e nesses trechos a imagem não prova nada.

## As listas entram por acréscimo, um item por quadro, e o que já passou continua visível em cinza
- Evidência: wwdc2021_10081 (folha 0001, q0005 a q0007; folha 0006, q0052 e q0053; folha 0009, q0077 a q0080)
- Evidência: wwdc2021_10245 (folha 0013, q0114 a q0116, o slide sai do título sozinho para três linhas e depois quatro)
- Evidência: wwdc2021_10278 (folha 0010, q0082 a q0084 e folha 0013, q0110 a q0112, com subitens surgindo primeiro esmaecidos)
- Evidência: wwdc2020_10640 (folha 0027, q0235 a q0239, item atual em preto e anteriores em cinza, alinhados ao lado do rosto)
- Evidência: wwdc2020_10206 (folha 0024, q0208 a q0216, o próximo item já visível em cinza antes de acender)
- Evidência: wwdc2021_10184 (folha 0003, q0022 e q0023, a seção de áudio entra abaixo das exceções já existentes)
- O que isso ensina sobre construir interface: a revelação progressiva mantém o contexto acumulado em vez de trocar a tela inteira. Deixar o próximo item pré visível em cinza antecipa a estrutura sem competir com o item atual, um comportamento aplicável direto a listas de onboarding e a formulários longos.

## Interface aparece dentro de moldura de aparelho, e a mesma tela é repetida em várias larguras lado a lado
- Evidência: wwdc2020_10206 (folha 0001, q0006 e q0009, o Mail em MacBook com três colunas, iPad com duas e iPhone com uma; folha 0019, q0171, cinco aparelhos alinhados com apps diferentes e a mesma estrutura de barra lateral)
- Evidência: wwdc2021_10029 (as notas registram que toda demonstração de site aparece em moldura de dispositivo, nunca como captura solta; folha 0012, q0102, três iPhones lado a lado)
- Evidência: wwdc2020_10205 (folha 0009, q0079 a q0081, a mesma lista em iPhone, iPad e janela de Mac em sequência)
- Evidência: wwdc2021_10275 (folha 0014, q0119 e q0120, de dois para quatro iPhones enfileirados em tamanhos de texto crescentes)
- Evidência: wwdc2020_10175 (folha 0017, q0149 e q0150, tabela comparando estilo a estilo entre iOS em escala reduzida e macOS)
- O que isso ensina sobre construir interface: adaptação não se explica, se mostra em paralelo. Pôr as larguras juntas no mesmo quadro faz a regra de colunas, de densidade e de tamanho de texto aparecer como uma decisão só, em vez de três telas desconexas.

## A anatomia do componente é construída em wireframe de traço fino, etapa por etapa, com as partes nomeadas
- Evidência: wwdc2020_10205 (folha 0003, q0022, lista de quatro itens com legendas "Label" e "Icon", depois um segundo exemplo com cabeçalho e separador de hierarquia)
- Evidência: wwdc2020_10206 (folhas 0021 a 0025, a barra lateral nasce do título e das abas, ganha seção recolhível, caixa de seleção, botão de adicionar e por fim um estado de edição com item em azul)
- Evidência: wwdc2020_10207 (folha 0008, q0069 a q0072, a janela do Mac passa por wireframe cinza, versão colorida e grade de anotação rosa e vermelha de margens)
- O que isso ensina sobre construir interface: tirar cor e conteúdo isola a estrutura. O wireframe construído por etapas ensina a ordem de decisão, primeiro o esqueleto, depois as seções, depois os estados, e evita discutir acabamento antes de a hierarquia estar fechada.

## O desenho vetorial é aberto em pontos de âncora e alças, e os contornos sobrepostos mostram a interpolação
- Evidência: wwdc2020_10175 (folha 0004, q0035 e q0036, a letra vira contorno com nós numerados; folha 0005, q0044 e q0045, setas indicam a direção de deslocamento de cada ponto)
- Evidência: wwdc2021_10097 (folha 0007, q0061, âncoras quadradas e ponto de controle redondo ligando reta e curva; folha 0008, q0064, três variantes sobrepostas em contorno ciano)
- Evidência: wwdc2021_10250 (folha 0007, q0057 a q0063, a coroa avança de silhueta com pontos até o preto sólido sem pontos; folha 0015, q0127 a q0135, contornos vermelho e azul sobrepostos com linhas ligando cada ponto ao correspondente)
- O que isso ensina sobre construir interface: a presença ou ausência dos pontos de âncora vira indicador de estado, modo de edição contra resultado final. E mostrar a correspondência ponto a ponto explica por que duas formas só interpolam se tiverem a mesma contagem e a mesma ordem de caminhos.

## As ferramentas de trabalho aparecem por dentro, com painel de camadas de um lado e painel de propriedades do outro
- Evidência: wwdc2020_10207 (folhas 0004 e 0005, q0034 a q0042, camadas nomeadas item por item e propriedades com opacidade, sombra, fonte e alinhamento)
- Evidência: wwdc2021_10250 (folha 0006, q0054, variantes por peso e escala à esquerda, matriz ao centro, preenchimento, bordas, sombras e desfoque à direita; folha 0011, q0091 a q0099, painel de renderização com camadas, visibilidade e opacidade)
- Evidência: wwdc2020_10175 (folha 0006, q0049 a q0054, painel escuro com sliders de peso e de tamanho óptico, e o glifo mudando junto com o campo numérico)
- Evidência: wwdc2021_10278 (folha 0006, q0047 a q0049, o navegador de arquivos do Xcode aparece ao lado do slide de instruções, no mesmo quadro)
- O que isso ensina sobre construir interface: mostrar a ferramenta junto do resultado conecta a decisão de design ao controle que a produz. O layout de três zonas, navegação à esquerda, palco ao centro e inspetor à direita, repete em ferramenta após ferramenta e serve de referência para qualquer editor.

## O app SF Symbols e afins seguem o mesmo esqueleto de três colunas, com categorias, grade e painel de inspeção
- Evidência: wwdc2021_10250 (folha 0005, q0037 a q0045, com moldura azul no item selecionado e seção "Custom Symbols" separada na base da barra lateral)
- Evidência: wwdc2021_10097 (folha 0014, q0122 a q0123, o painel direito passa de disponibilidade para controles ativos de renderização, cor e fundo)
- Evidência: wwdc2020_10207 (folha 0009, q0078 a q0081, prévia, disponibilidade por versão de sistema e restrições de uso no painel de detalhes)
- O que isso ensina sobre construir interface: o inspetor troca de conteúdo conforme o modo, informativo quando não há o que editar e cheio de controles quando há, sem mudar de posição nem de largura. A célula da grade carrega o glifo mais o nome técnico embaixo, o que torna a busca visual e a cópia do identificador a mesma ação.

## Variantes são organizadas em matriz, a mesma unidade repetida cruzando duas dimensões
- Evidência: wwdc2021_10097 (folha 0004, q0033 e q0034, colunas de variante e linhas de preenchimento aplicadas ao mesmo coração; folha 0015, q0129 e q0130, quatro linhas de aparência por colunas de matiz; folha 0016, q0143, quatro modos por cinco símbolos)
- Evidência: wwdc2021_10250 (folha 0006, q0054, pesos de Ultralight a Black nos tamanhos S, M e L)
- Evidência: wwdc2020_10207 (folha 0010, q0086 a q0090, template de exportação em três linhas por nove colunas, uma dimensão de escala e outra de peso)
- Evidência: wwdc2020_10175 (folha 0018, q0155 a q0159, uma coluna de estilos cresce até sete colunas de tamanho, de xSmall a xxxLarge)
- O que isso ensina sobre construir interface: a matriz prova cobertura e expõe buracos. Ao fixar um elemento de amostra e variar apenas os eixos, fica visível que o sistema é combinatório, e qualquer célula ausente vira uma pergunta imediata.

## Diagramas usam cor como código de papel, e essa convenção quase nunca é dita na fala
- Evidência: wwdc2021_10081 (folha 0002, q0010 a q0012, caixas azul escuro para as classes de entrada, verde e vermelha para conexão e desconexão; folha 0007, q0056 e q0057, azul para configuração e verde para o objeto resultante; as notas registram que a fala não menciona a convenção)
- Evidência: wwdc2021_10278 (folha 0005, q0037 a q0039, engine em azul escuro, player em azul claro e pattern em verde, revelados em três passos)
- Evidência: wwdc2020_10206 (folha 0020, q0177 a q0180, blocos azuis para o nível principal e cinza para o subordinado, setas duplas para alternância e descendentes para hierarquia)
- Evidência: wwdc2021_10250 (folha 0018, q0154 a q0159, caixas azuis de requisito apontando para caixas verdes de template)
- O que isso ensina sobre construir interface: a cor carrega a taxonomia sem legenda, o que acelera a leitura de quem já conhece o sistema e deixa quem não conhece sem apoio. Se a cor é a única portadora do papel, o diagrama precisa de rótulo redundante, o mesmo princípio que aparece nas telas de acessibilidade do lote.

## O suporte a direita para esquerda é provado com a mesma tela espelhada, não apenas afirmado
- Evidência: wwdc2020_10175 (folha 0011, q0097 a q0099, a palavra em inglês e em árabe recebem as mesmas setas de medida e em seguida dois iPhones com Ajustes em árabe)
- Evidência: wwdc2020_10207 (folha 0012, q0103 a q0105, calendário em inglês e em árabe com o menu de contexto no lado oposto e o texto alinhado à direita)
- Evidência: wwdc2021_10097 (folha 0007, q0057 a q0059, o par rotulado com as duas direções no símbolo de bateria, depois aplicado a duas telas em espelho com check verde na correta)
- Evidência: wwdc2021_10275 (folha 0017, q0149, grade de ícones com navegação e alinhamento invertidos)
- O que isso ensina sobre construir interface: espelhar é decisão por elemento, não interruptor global. Símbolos direcionais viram, símbolos de objeto ficam, e a única forma de verificar isso é montar a tela inteira nos dois sentidos e olhar.

## O alinhamento entre símbolo e texto é ensinado com as linhas tipográficas rotuladas e o glifo ao lado de uma letra
- Evidência: wwdc2020_10207 (folha 0002, q0013 a q0015, marcações de cap height, x-height e baseline, esta em vermelho, revelando que o símbolo fica ligeiramente acima da linha de base)
- Evidência: wwdc2021_10097 (folha 0003, q0019 e q0020, "Vertical alignment" com as mesmas guias e "Horizontal alignment" com guias verticais pontilhadas; q0027 põe o coração ao lado de uma letra minúscula)
- Evidência: wwdc2021_10250 (folha 0002, q0014 e q0015 e retornos nas folhas 0003, 0009, 0014 e 0016, matriz com a letra à esquerda de cada fileira e os símbolos alinhados pela linha de base)
- O que isso ensina sobre construir interface: ícone ao lado de texto é problema tipográfico, não gráfico. Alinhar pelo centro da caixa produz desalinhamento óptico, e a referência correta são as linhas da fonte, o que também define escala e peso do traço para casar com o corpo do texto.

## Estado ativo é marcado por check mais realce da linha inteira, e a lista de opções repete esse vocabulário
- Evidência: wwdc2020_10205 (folha 0004, q0030 a q0033, marca de verificação no item ativo e realce de cor cobrindo a linha em foco, dois tratamentos distintos no mesmo menu; folha 0007, q0056 e q0057, check simultâneo em dois eixos independentes)
- Evidência: wwdc2021_10097 (folha 0014, q0125 e folha 0017, q0147, seletor de cor como lista vertical com check azul no item ativo)
- Evidência: wwdc2021_10250 (folha 0011, q0094 a q0096, menu de cores com amostra quadrada ao lado do nome e check na opção ativa; folha 0005, moldura azul no item selecionado da barra lateral)
- O que isso ensina sobre construir interface: seleção e foco são coisas diferentes e precisam de tratamentos diferentes no mesmo componente. E um menu pode carregar seleções de eixos independentes ao mesmo tempo sem confundir, desde que separados por linha divisória.

## O limite do sistema é mostrado na tela, em alerta amarelo ou em cartão de erro, e não escondido
- Evidência: wwdc2020_10175 (folha 0007, q0055, triângulo amarelo quando o valor pedido fica fora do alcance disponível)
- Evidência: wwdc2020_10207 (folha 0013, q0109 a q0117, cartão de erro rosa sobreposto à janela avisando que o símbolo não existe antes de determinada versão do sistema)
- Evidência: wwdc2021_10126 (folha 0006, q0046, ícone de alerta amarelo isolado logo abaixo da barra com seis abas)
- Evidência: wwdc2021_10250 (folha 0014, q0118 a q0120, trio de selos com círculo amarelo de exclamação ao lado do verde de ponto e do verde de check)
- Evidência: wwdc2021_10275 (folha 0025, q0218 a q0221, o campo alterna entre contorno vermelho com mensagem específica logo abaixo e contorno neutro sem mensagem)
- O que isso ensina sobre construir interface: o aviso mora junto do controle que o gerou e diz o que está fora do alcance, não apenas que algo falhou. O amarelo separa o estado "atenção" do vermelho de erro e do vermelho de destruição, três significados que não devem dividir a mesma cor.

## Mãos e aparelhos físicos entram no quadro, em vez de captura de tela pura
- Evidência: wwdc2020_20022 (folhas 0004, 0005 e 0007, enquadramento com mãos e dispositivo nos três apps de criação; folha 0005, q0038 a q0040, o modelo no tablet, a máquina de corte a laser e as peças resultantes na mão)
- Evidência: wwdc2020_10640 (folha 0032, q0284 e q0285, foto real de mão sobre trackpad sobreposta ao canto da tela do iPad)
- Evidência: wwdc2021_10126 (folha 0012, q0105 a q0107, demonstração real de riscar texto com a caneta, com o traço avançando entre quadros)
- Evidência: wwdc2021_10278 (o iPhone físico na mão aparece em sete folhas, e nenhum quadro traz tela de simulador)
- Evidência: wwdc2021_10245 (telas de software em uso real, seguradas na mão, em nove folhas)
- Evidência: wwdc2020_10207 (folha 0006, q0046, a grade de símbolos numa tela de laptop com uma mão tocando os símbolos)
- O que isso ensina sobre construir interface: interações de entrada só ficam compreensíveis com o corpo no quadro. A mão dá escala ao alvo de toque, mostra oclusão e prova o alcance, coisas que uma captura limpa apaga.

## Slides conceituais são pretos, com texto branco e quase nenhum grafismo, e a hierarquia vem de peso e opacidade
- Evidência: wwdc2021_10081 (folha 0001, q0005 a q0007, título em branco negrito no alto à esquerda e lista menor abaixo com espaçamento vertical generoso, sem nenhum grafismo)
- Evidência: wwdc2021_10250 (folha 0002, q0016 a q0018, o slide de margens mostra só o símbolo entre marcas de eixo, e o de escalas só o mesmo símbolo em três tamanhos)
- Evidência: wwdc2021_10278 (folha 0004, q0028 a q0032, fundo preto, título no canto superior esquerdo e um ícone esquemático de aparelho à direita, variando minimamente de um princípio para o outro)
- Evidência: wwdc2020_10640 (as notas registram hierarquia por peso e opacidade em lugar de marcadores nas listas de recomendação)
- Evidência: wwdc2021_10126 (folha 0004, q0031 a q0034, dez itens em duas colunas de texto branco sobre preto, depois numerados, depois com destaque nos três primeiros)
- O que isso ensina sobre construir interface: quando o fundo é preto e o conteúdo é texto, a única variável de ênfase que sobra é tipográfica. Peso, tamanho e opacidade dão três níveis de hierarquia sem introduzir cor nem caixa, e o mesmo slide aguenta ser reusado dezenas de vezes mudando só qual linha está acesa.

## Estados intermediários de transição são capturados, com camadas translúcidas antes de assentarem
- Evidência: wwdc2020_10205 (folha 0004, q0029 a q0032, o menu aparece primeiro translúcido sobre a tela e depois opaco; folha 0011, q0097 a q0099, o cartão de calendário surge semitransparente antes de ficar sólido)
- Evidência: wwdc2020_10206 (folha 0019, q0163 a q0165, a terceira coluna do Mail aparece sobreposta com transparência antes de assentar; folha 0017, q0147 a q0153, a barra lateral passa por expandida, recolhida a faixa fina, sobreposta como camada semitransparente e escondida)
- Evidência: wwdc2021_10029 (folha 0013, q0112 e q0113, a rotação acontece em quadros intermediários com desfoque de movimento, em vez de corte seco)
- Evidência: wwdc2021_10126 (folha 0010, q0089 e q0090, o botão obturador passa de translúcido para branco sólido conforme o reconhecimento avança)
- O que isso ensina sobre construir interface: o meio do caminho é parte do componente. Opacidade e sobreposição comunicam que o elemento ainda não está comprometido, e mostrar o ciclo completo de estados de um painel, em vez de só aberto e fechado, é o que define de fato o comportamento.

## Menus e popovers nascem ancorados no controle que os originou, com seta apontando o elemento exato
- Evidência: wwdc2020_10205 (folha 0005, q0041 a q0045, menus surgindo sob o botão de adicionar, acima da barra de anotação e junto aos controles de edição de vídeo)
- Evidência: wwdc2020_10206 (folha 0007, q0057 a q0061, o popover de evento com seta para o bloco da grade, o de calendários com seta só para o botão do rodapé, e a mesma lista virando coluna fixa sem seta nem sobreposição)
- Evidência: wwdc2020_10200 (folha 0002, q0010, cartão ancorado na base da tela com o ícone do app de origem à esquerda do endereço e rótulo secundário identificando a procedência)
- O que isso ensina sobre construir interface: a âncora é o que conta de onde a interface veio e sobre o que ela age. Quando o mesmo conteúdo ganha espaço permanente na tela, a seta some junto com a sobreposição, sinal de que ele deixou de ser resposta a um toque e virou estrutura.

## Apps reais do sistema servem de prova de cada conceito abstrato
- Evidência: wwdc2020_10175 (folhas 0012 a 0015, Calendário, Mail, Fitness, Maps, Book Store, Lembretes e o cabeçalho do app de música identificado como estilo de título grande)
- Evidência: wwdc2020_10205 (a maior parte dos quadros é tela real de Lembretes, Fotos, Música, Podcasts, Files, Messages, Mail e Safari)
- Evidência: wwdc2020_10640 (folhas 0029 a 0033, planilha, documento de texto, calendário, Mapas e Central de Controle como estudos de caso na segunda metade)
- Evidência: wwdc2021_10097 (folha 0004, q0035 e q0036, a tabela de variantes esmaece sobre uma tela real do Mail com ação de swipe revelada)
- O que isso ensina sobre construir interface: o exemplo genérico prova que a regra é implementável, o app real prova que ela foi implementada. A transição de tabela abstrata para captura real, feita por esmaecimento no mesmo enquadramento, é o gesto que amarra as duas camadas.

## O vídeo é emoldurado por abertura e encerramento idênticos, e fecha com recapitulação mais sessões relacionadas
- Evidência: wwdc2020_10200 (folhas 0001, 0005 e 0006, a mesma composição de adesivos na tampa do laptop no começo e no fim)
- Evidência: wwdc2020_10640 (folha 0035, q0307 e q0308, o mesmo MacBook com adesivos da abertura, em dois enquadramentos)
- Evidência: wwdc2020_10205 (folha 0001, q0006 e folha 0014, q0121, a mesma vitrine dos três componentes, mudando apenas qual está em foco)
- Evidência: wwdc2021_10081 (folha 0012, q0100 e q0103, slide com título, chamada à ação e lista de sessões com etiqueta do evento à direita, depois a cartela preta)
- Evidência: wwdc2021_10184 (folha 0007, q0055 a q0057, recapitulação com os quatro itens completos e depois a cartela final)
- Evidência: wwdc2021_10278 (folha 0013, q0110 a q0112, painel lateral na metade esquerda, lista crescendo até a seção de recursos e rodapé separando nome da sessão do código do evento)
- Evidência: wwdc2021_10245 (folha 0017, q0145 a q0151, o apresentador de abertura volta ao cenário inicial para fechar, seguido do slide com duas referências cruzadas)
- O que isso ensina sobre construir interface: o fecho repete a moldura da abertura e devolve ao leitor a estrutura inteira já percorrida, mais os caminhos adjacentes. É um padrão de saída aplicável a qualquer fluxo longo, e usa o mesmo componente de lista do índice persistente, agora com todos os itens acesos.

## O cenário do apresentador marca o papel e o bloco, e ele divide o quadro com o material em vez de alternar por corte
- Evidência: wwdc2021_10029 (dois cenários fixos separam conceito de demonstração, a apresentadora na mesa clara nas folhas 0001 a 0007 e o segundo apresentador no cenário escuro nas folhas 0008 a 0010)
- Evidência: wwdc2021_10245 (cada troca entre os cinco apresentadores vem com corte completo de mesa, decoração e computador ao fundo, nunca com transição gradual)
- Evidência: wwdc2021_10081 (a mesma mesa com fileira de controles reaparece em quase todas as folhas, mudando só o controle na mão conforme o tópico avança)
- Evidência: wwdc2020_10200 (um retrato pequeno da apresentadora fica ancorado ao lado de praticamente todo mockup nas folhas 0001 a 0004)
- Evidência: wwdc2021_10275 (folha 0004, q0031, a lista das seis práticas empilhada ao lado do rosto do apresentador)
- O que isso ensina sobre construir interface: a coexistência de pessoa e material no mesmo quadro mantém a continuidade da explicação, e a troca de cenário funciona como separador de capítulo sem precisar de cartela. O contraste do texto tem que acompanhar o fundo do cenário, como registrado em wwdc2021_10275, onde o item ativo é preto sobre fundo claro em umas folhas e branco em outras.

## A novidade é sinalizada por selo verde dentro do próprio slide, junto do item a que se refere
- Evidência: wwdc2020_10175 (folha 0017, q0145 a q0148, selo circular verde "NEW" no canto do cartão, com o texto revelado linha a linha; reaparece nas folhas 0010 e 0016)
- Evidência: wwdc2020_10207 (folha 0008, q0064 a q0067 e folha 0017, q0146, selo verde no canto dos quadros de código e do item novo na barra lateral)
- Evidência: wwdc2021_10184 (folha 0006, q0046 a q0049, rótulo "NEW" em caixa verde junto do item de lista)
- O que isso ensina sobre construir interface: o marcador de novidade fica colado ao item, nunca no título do bloco, o que permite misturar itens novos e antigos na mesma lista sem ambiguidade. Verde saturado em campo pequeno é suficiente e não compete com o conteúdo.

## A limitação é declarada dentro do próprio material, em vez de omitida
- Evidência: wwdc2020_10175 (folha 0017, q0145 a q0148, o cartão do macOS acrescenta a frase sobre ausência de suporte a Dynamic Type)
- Evidência: wwdc2021_10278 (folha 0011, q0091 a q0093, na tabela comparativa a ausência de suporte é uma célula vazia, e a classe básica só tem marcação na primeira coluna)
- Evidência: wwdc2020_10207 (folha 0013, q0109 a q0117, comparação de nomes antigos e novos com legenda vermelha sob as formas depreciadas e seção dedicada a nomes depreciados no painel de detalhes)
- Evidência: wwdc2021_10126 (folha 0002, q0013 a q0018, o onboarding em carrossel é montado tela por tela justamente para ser descartado em seguida)
- O que isso ensina sobre construir interface: mostrar o que não funciona, o que foi depreciado e o que não existe em determinada versão é parte da documentação do componente. Célula vazia em tabela comunica ausência melhor que um X, porque não compete com o vocabulário de reprovação usado nos pares de certo e errado.

## O passado físico é usado como âncora do conceito digital
- Evidência: wwdc2020_10175 (folha 0003, q0022 a q0027, mãos folheando um exemplar do século 18 com legendas em versalete, depois o par de letras em dois corpos e as mesmas letras sobre grade de pixels; folha 0011, q0091 a q0094, fundo fotográfico de tipos metálicos enferrujados no cartão sobre entrelinha)
- Evidência: wwdc2021_10245 (folhas 0001 a 0003, computador bege com dois drives, teclado integrado, tela verde fósforo com cursor piscando, o Macintosh original com barra de menu de quatro rótulos e o iPhone original com a faixa de destravar)
- Evidência: wwdc2020_20022 (folha 0003, q0024 e q0025, esboços a lápis com anotações técnicas de figurino ao lado dos bonecos, seguidos da ilustração acabada)
- O que isso ensina sobre construir interface: termos herdados do impresso, como entrelinha e corpo do tipo, ficam claros quando o objeto de origem aparece. A mesma lógica vale para justificar por que uma convenção antiga continua valendo, mostrando a linha inteira em vez de apenas o estado atual.

## Números grandes isolados sobre fundo liso funcionam como pausa e ênfase entre blocos
- Evidência: wwdc2020_10206 (folha 0006, q0047, a cifra de aumento entra como elemento tipográfico isolado com efeito de fumaça, fora de qualquer interface)
- Evidência: wwdc2021_10097 (folha 0006, q0050, a contagem de símbolos em tipografia grande sobre o mesmo fundo pontilhado das grades anteriores)
- O que isso ensina sobre construir interface: um dado que sustenta todo um argumento merece ocupar a tela inteira sozinho. Reaproveitar o fundo do bloco anterior mantém a continuidade visual enquanto muda completamente a densidade.

## Gráfico com eixos rotulados é usado para justificar uma decisão de design, não só para reportar dado
- Evidência: wwdc2020_10175 (folha 0008, q0071 e q0072 e folha 0009, q0073 a q0075, curva de tracking com eixos de tamanho e de espacejamento, áreas de fundo por zona, e a evolução de dois rótulos com corte único para um rótulo contínuo com dois limites marcados)
- Evidência: wwdc2021_10278 (folha 0005, q0040 a q0044, o QuickLook do arquivo háptico com curva de intensidade em laranja e barras verticais azuis, mais chamadas rotulando os dois tipos de evento; folha 0010, q0090, dezenas de barras muito próximas contrastando com os três eventos esparsos do outro asset)
- O que isso ensina sobre construir interface: quando a curva do sistema aparece, o valor específico deixa de parecer arbitrário. E usar a mesma visualização para dois arquivos diferentes transforma densidade em comparação imediata, sem precisar de número.

## Controle escondido é substituído por controle nomeado, e a ação primária nunca entra no menu secundário
- Evidência: wwdc2020_10205 (folha 0007, q0059 a q0062, o ícone de compor fica isolado no canto superior direito, fora do menu, enquanto selecionar, fixar e editar ficam agrupados dentro do menu secundário)
- Evidência: wwdc2021_10126 (folha 0023, q0204 a q0207 e folha 0024, q0209 a q0213, o ícone de reticências no canto do card dá lugar a um botão de texto verde em linha, e o menu que ele abre passa a listar frases completas com ícones de força diferente)
- O que isso ensina sobre construir interface: visibilidade é a decisão, não a estética do ícone. O que a pessoa faz toda hora fica exposto e rotulado, o resto se agrupa, e dentro do agrupamento o texto completo vale mais que o ícone quando a consequência da ação não é óbvia.

## Achados de fonte única

- Região de toque desenhada como moldura tracejada maior que o ícone visível, com os quadros mostrando o contorno primeiro deslocado e depois coincidindo com o desenho, e dois ícones vizinhos passando a compartilhar uma faixa tracejada contínua sem vão entre eles. Referência: wwdc2020_10640 (folha 0010, q0082 a q0085; folha 0018, q0160 e q0161).
- O algoritmo de magnetismo do ponteiro ganha sua única representação gráfica como espiral de pontos tracejados turquesa em círculos concêntricos sobre a tela inicial, que some no quadro seguinte com o ponteiro já fixado no ícone. Referência: wwdc2020_10640 (folha 0013, q0109 a q0111).
- Anatomia do efeito de elevação do ponteiro como diagrama explodido em três dimensões, com as camadas nomeadas e reveladas progressivamente, primeiro reflexo especular e elemento, depois radiosidade e sombra. Referência: wwdc2020_10640 (folha 0015, q0130 e q0131).
- Ponto de ancoragem da forma do ponteiro marcado por um ponto amarelo, posto na ponta inferior do conta gotas, fora do centro geométrico, e depois no centro exato de um círculo, comparando as duas escolhas em quadros consecutivos. Referência: wwdc2020_10640 (folha 0026, q0232 e q0233).
- Barra em degradê de preto a branco usada como escala de contraste para escolher o material do ponteiro, com marcador circular que muda de posição entre quadros ao lado do mesmo botão com e sem fundo. Referência: wwdc2020_10640 (folha 0022, q0191 e q0192).
- Alinhamento óptico documentado com margem negativa: o zoom progressivo sobre o ícone de pasta mostra a linha guia da direita entrando por dentro do desenho, e o emblema ultrapassando o contorno na pilha de ícones. Referência: wwdc2020_10207 (folha 0010 até q0084; folha 0011, q0091 a q0093).
- Botão destrutivo posicionado acima do botão neutro na folha de confirmação, nunca ao lado, mostrado em dois apps na mesma sequência de dois passos. Referência: wwdc2020_10205 (folha 0008, q0068 a q0072; folha 0009, q0076 e q0077).
- Entrada numérica direta substituindo a roda giratória: teclado de teclas quadradas grandes abaixo do campo de hora, e o seletor de mês e ano virando lista rolável de duas colunas com o item central maior e em negrito. Referência: wwdc2020_10205 (folha 0011, q0091 e q0094).
- Confirmação por toque fora do campo mostrada como par de quadros sem passo intermediário: a caixa de contorno azul ao redor do valor some e a data vira texto simples. Referência: wwdc2020_10205 (folha 0012, q0102 e q0103).
- Espaço ocioso medido em proporção: a barra de ferramentas com poucos ícones pequenos e muito espaço negativo ao redor, seguida do cartão de recomendação e da mesma tela com os botões reposicionados mais perto do conteúdo. Referência: wwdc2020_10206 (folha 0026, q0226 a q0230).
- Progressão de densidade mostrada em três degraus na mesma tela inicial, de grade espaçada para grade cheia e depois com widgets no lugar de parte dos ícones, e o gerenciador de arquivos passando de ícones grandes para ícones bem menores com muito mais itens visíveis. Referência: wwdc2020_10206 (folha 0005, q0038 a q0043).
- Renomeação em linha dentro da própria grade de arquivos contraposta ao modal clássico centralizado sobre conteúdo escurecido, com miniatura, campo em foco e teclado ocupando a faixa inferior. Referência: wwdc2020_10206 (folha 0006, q0054; folha 0007, q0055 e q0056).
- A tese de que a moldura do navegador deve sumir é encenada literalmente: a janela dos anos 1990, com menus e campo de URL, vai perdendo conteúdo e contraste até restar um retângulo cinza quase vazio com uma barra estreita no topo. Referência: wwdc2021_10029 (folha 0002, q0010 a q0012).
- A variação de uma medida de sistema é convertida em gradação visual, três aparelhos idênticos com a mesma tela coberta por camada verde de opacidade crescente, recurso que a fala expressa só em palavras. Referência: wwdc2021_10029 (folha 0012, q0102).
- Proporção fixa explicada em três registros no mesmo bloco: réguas de medida sobre a foto, um cartão que vira quadrado e depois cresce em altura para caber o conteúdo aparecendo em quatro larguras, e diagramas geométricos com listas de declarações equivalentes. Referência: wwdc2021_10029 (folha 0021, q0183 e q0184; folha 0022, q0194 a q0199; folha 0023, q0202 a q0207).
- Espaçamento entre itens flexíveis demonstrado por três estados da mesma barra de navegação, itens colados, itens quebrando em duas linhas, e itens uniformemente espaçados depois que a declaração entra no código. Referência: wwdc2021_10029 (folha 0024, q0214 a q0216).
- Grade comparativa de cartões brancos rotulados um a um para exibir o conjunto inteiro de controles nativos redesenhados de uma vez. Referência: wwdc2021_10029 (folha 0025, q0224 e q0225).
- Localização tratada como sistema paramétrico e não como tradução: a mesma estrutura de célula, livro, balão de fala, letra com expoente e letra em moldura, repetida com a letra latina e com a tailandesa, e depois em grade densa cobrindo sete escritas. Referência: wwdc2021_10097 (folha 0006, q0053 e q0054; folha 0007, q0055).
- Opacidade de camada anotada em número sobre o próprio símbolo, com um par rotulado trazendo os percentuais acima de cada ícone, contrastado com a versão monocromática. Referência: wwdc2021_10097 (folha 0014, q0119 e q0120).
- Comparação de matizes próximos feita com dois círculos grandes e o nome abaixo, para separar cores que se confundem no catálogo. Referência: wwdc2021_10097 (folha 0015, q0131 e q0132).
- Escolha entre configuração estática e variável traduzida em quantidade visível: o diagrama de pontos passa de nove pontos por linha para três, com as guias verticais reposicionadas. Referência: wwdc2021_10250 (folha 0006, q0049 a q0051).
- Interação entre camadas explicada com diagrama de três círculos sobrepostos comparando o comportamento que mescla no cruzamento com o que limpa o que está atrás, sobreposto ao próprio ícone antes de ser isolado em tela cheia. Referência: wwdc2021_10250 (folha 0012, q0106 a q0108).
- Problema de ordem de caminhos demonstrado colorindo cada caminho de uma cor e numerando os pontos, com os contornos internos revelando que os dois desenhos não coincidem. Referência: wwdc2021_10250 (folha 0009, q0073 a q0078).
- Fluxograma de decisão de distribuição com colunas de versão mínima de sistema apontando para as caixas de template compatíveis, uma coluna apontando para os dois e duas apontando só para o mais novo. Referência: wwdc2021_10250 (folha 0018, q0154 a q0159).
- A câmera do app desenhada como alvo e não como instrução: overlay escuro, contorno tracejado no formato do objeto procurado, texto curto centralizado e obturador que passa de translúcido a sólido conforme o reconhecimento avança, com o texto trocando de procura para instrução de enquadramento. Referência: wwdc2021_10126 (folha 0010, q0089 e q0090; folha 0011, q0094 e q0095).
- Feedback confirmado em escala maior que o próprio controle: o coração pequeno no canto da foto dá lugar a um coração preenchido grande no centro da imagem, com uma legenda curta de consequência. Referência: wwdc2021_10126 (folha 0013, q0109 e q0110).
- Pista de gesto dada por conteúdo parcialmente visível, com miniaturas cortadas surgindo nas bordas esquerda e direita da foto principal e trocando de conteúdo entre quadros. Referência: wwdc2021_10126 (folha 0014, q0120 a q0123).
- Campo de busca com exemplos concretos de ingrediente e lugar no lugar do texto genérico, apresentado com o marcador vermelho apenas na versão descartada. Referência: wwdc2021_10126 (folha 0010, q0085).
- Glossário visual de gestos padrão em grade de três por dois, com símbolos abstratos azuis sobre preto e rótulo em texto abaixo de cada um. Referência: wwdc2021_10126 (folha 0012, q0102).
- Fileira de três ícones de pilares usada como recurso de foco: os ícones das pontas esmaecem e o do centro é substituído por uma captura real, marcando a passagem de conceito abstrato para exemplo concreto. Referência: wwdc2021_10184 (folha 0003, q0019 e q0020).
- Zonas de distância anotadas como anéis concêntricos luminosos ao redor do alto falante, com marcadores numerados sobre a linha entre os dois aparelhos e um zoom revelando a lista de parâmetros que variam por zona, entre eles posição e escala do banner, desfoque de fundo, força do háptico, luz do aparelho e áudio. Referência: wwdc2021_10245 (folha 0009, q0078 a q0081).
- O mesmo espaço da interface muda de função conforme a distância sem mudar de posição: o botão de direções com distância e tempo vira o botão de encontrar quando o alvo está perto, mantendo o par de botões no mesmo lugar do cartão. Referência: wwdc2021_10245 (folha 0006, q0048 a q0052).
- A cor do fundo como único portador de estado numa tela minimalista: a mesma estrutura de seta central e linha de distância alterna entre fundo escuro neutro e verde sólido para marcar alinhamento com a direção certa. Referência: wwdc2021_10245 (folha 0012, q0101 e q0102; folha 0016, q0138 e q0139).
- Sobreposição gráfica ilustrativa que não é captura de tela: o cone de luz verde saindo do topo do telefone em direção ao sofá, criado para comunicar a ideia de a tela se acender. Referência: wwdc2021_10245 (folha 0007, q0060).
- Exemplo negativo mostrado como lista em que todos os destinos de áudio têm o mesmo peso visual, independentemente de estarem perto ou longe, com o aparelho atual marcado só por um ícone de seleção. Referência: wwdc2021_10245 (folha 0014, q0120).
- Balões brancos de ponta triangular sobrepostos à captura real trazendo entre aspas o que o leitor de tela anunciaria para aquele elemento específico. Referência: wwdc2021_10275 (folha 0015, q0132 e q0135).
- Estrutura de formulário revista de campos fixos de papel para campos repetíveis com seletor de papel ao lado do nome e botão de adicionar membro. Referência: wwdc2021_10275 (folha 0011, q0092 a q0098).
- Adaptação de conteúdo por região e não só tradução: os cartões de receita saem de pratos ocidentais traduzidos para pratos locais e surge uma seção de festival que antes não existia. Referência: wwdc2021_10275 (folha 0020, q0173 a q0178).
- Material translúcido empilhado sobre material translúcido no Centro de Controle, com o painel de tamanho de texto sobre o painel de atalhos de acessibilidade e o traço do dedo visível. Referência: wwdc2021_10275 (folha 0016, q0138 a q0140).
- Uma moldura única de painel reaproveitada para categorias completamente diferentes na criação de personagem, cabeçalho colorido, grade de blocos quadrados, contorno de destaque na opção escolhida e botão de voltar, servindo igual para tom de pele, penteado e idioma de voz. Referência: wwdc2021_10275 (folha 0027, q0241 a q0243).
- Gênero tratado primeiro por tipografia, com uma lista de termos em tipo grande cada um numa cor do gradiente do verde ao magenta, e só depois como componente, comparando três opções fixas com um campo de texto livre com botão de limpar e chave de privacidade. Referência: wwdc2021_10275 (folha 0008, q0068 e q0069; folha 0026, q0231 a q0233).
- Especificação organizada por canal sensorial em três linhas paralelas, visual, háptico e áudio, cada uma com um badge colorido nomeando o arquivo correspondente, reveladas em etapas e depois duplicadas para comparar assets alternativos. Referência: wwdc2021_10278 (folha 0006, q0052 a q0054; folha 0007, q0055 e q0056).
- Controle virtual em tela como painel translúcido sobre o jogo, com manche esquerdo cinza, manche direito laranja maior, botões de ação em círculos pequenos translúcidos com a letra centralizada e barra de progresso fina na base, percorrendo variações de posição, tamanho e formato entre quadros. Referência: wwdc2021_10081 (folha 0006, q0047 a q0051).
- A mesma instrução escrita duas vezes no slide mudando apenas o símbolo de botão embutido no meio da frase, para provar que o glifo precisa corresponder ao controle real. Referência: wwdc2021_10081 (folha 0004, q0035).
- Grade de chamada de vídeo com legenda de cidade e país no canto inferior de cada participante servindo de estrutura para o vídeo inteiro, com a moldura alternando entre vários participantes e um em destaque no momento da reação. Referência: wwdc2020_20022 (folhas 0001, 0002 e 0006, q0007 em diante e q0047 a q0054).
- Ponte entre projeto digital e peça física em três quadros seguidos, manipulação do modelo no tablet, máquina de corte em operação e mãos segurando as peças resultantes. Referência: wwdc2020_20022 (folha 0005, q0038 a q0040).
- Interface quase ausente como escolha deliberada no app de desenho, tela cheia de cor com poucos ícones nos cantos e nenhum controle visível, deixando o quadro inteiro para o gesto com a caneta. Referência: wwdc2020_20022 (folha 0007, q0058 a q0060).
- Ponto de entrada de sugestão captado na origem e no destino como par de telas em sequência, a conversa com o endereço e o mapa já com o mesmo endereço preenchido. Referência: wwdc2020_10200 (folha 0001, q0009 e q0010).
- Substituição na mesma posição da tela inicial: a pilha de widgets genéricos paginada por pontos dá lugar a um widget dedicado listando as duas próximas aulas, ocupando a largura de dois ícones. Referência: wwdc2020_10200 (folha 0004, q0033 e q0034).
- Automação de mais de um app representada numa única linha de cartão, com dois ícones de app lado a lado antes do texto do gatilho e da ação. Referência: wwdc2020_10200 (folha 0005, q0041).
- Tabela tipográfica de duas colunas com a mesma frase de amostra repetida de 12 a 26 pontos e a linha do tamanho ativo destacada em branco enquanto as demais ficam cinzas, com a linha destacada subindo entre quadros. Referência: wwdc2020_10175 (folha 0002, q0013 e q0014).
- Ligadura preservada e ligadura desmontada mostradas na mesma palavra sob os selos de reprovado e aprovado, provando o efeito colateral de alterar espacejamento em código. Referência: wwdc2020_10175 (folha 0010, q0082).
- Tabela de ajuste de entrelinha em pontos com colunas de valor padrão, apertado e folgado e uma linha por plataforma, ao lado da captura do painel do ambiente de desenvolvimento com a opção de otimizar a interface destacada em azul. Referência: wwdc2020_10175 (folha 0014, q0125 e q0126; folha 0017, q0151 a q0153).
