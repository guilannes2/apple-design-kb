# ess-06: padrões visuais recorrentes

Lote de 15 vídeos WWDC (2018 e 2019). Cada padrão abaixo aparece em pelo menos duas sessões diferentes.

## A agenda da sessão fica na tela o tempo todo, com um item em branco pleno e os outros em cinza
- Evidência: wwdc2018_806 (folha 0005, q0042 a q0045; reaparece nas folhas 0009, 0014 e 0016; as notas registram que a fala não verbaliza a troca)
- Evidência: wwdc2019_239 (folha 0003, q0022 a q0025, lista de oito palavras sem numeração nem marcador, retomada nas folhas 0008, 0010, 0015, 0021, 0023 e 0025)
- Evidência: wwdc2019_802 (lista fixa de seis palavras reaparecendo nas folhas 0002, 0005, 0010, 0014, 0015, 0019, 0033 e 0039)
- Evidência: wwdc2019_520 (folha 0014, q0118 a q0120; folha 0015, q0128 a q0132)
- Evidência: wwdc2019_803 (cartão verde de índice com quatro saídas, folha 0017, q0145 a q0150; o mesmo cartão volta para os quatro insumos na folha 0029, q0254 a q0256)
- O que isso ensina sobre construir interface: opacidade sozinha já resolve "onde estou" sem barra de progresso, numeração ou componente novo. O mesmo elemento serve de índice, de marcador de posição e de recapitulação.

## Listas e tabelas crescem um item por quadro e nunca aparecem prontas
- Evidência: wwdc2018_803 (folhas 0041 a 0043, q0373 a q0378, um ou dois bullets por quadro, com o próximo antecipado em cinza)
- Evidência: wwdc2019_211 (folha 0018, q0158 a q0161, a lista de boas práticas vai de um critério a três)
- Evidência: wwdc2019_803 (folha 0009, q0080 e q0081, o checklist começa com um item e chega a quatro na folha 0010)
- Evidência: wwdc2018_804 (folha 0004, q0028 a q0033, bullets empilhados sem marcador gráfico, uma linha por quadro)
- Evidência: wwdc2019_223 (folha 0020, q0174 a q0180, a tabela de comparação fica vários quadros com uma coluna só antes de a segunda entrar)
- O que isso ensina sobre construir interface: revelação progressiva é controle de atenção, não decoração. Nenhum item some quando o seguinte entra, então o leitor mantém o contexto acumulado.

## A medida aparece escrita em cima do desenho, não só na fala
- Evidência: wwdc2018_803 (folha 0035, q0311 a q0313, círculo tracejado rotulado "Hysteresis 10pt" sobre a foto)
- Evidência: wwdc2019_206 (camada de cota em magenta sobre o mesmo layout de teste, com os valores 18, 16, 29 e 90, folha 0007, q0061 a q0063; e alturas de contêiner 24, 36 e 44 para o mesmo texto de 17 pontos, folha 0005, q0040 a q0043)
- Evidência: wwdc2019_211 (folha 0019, q0165 a q0168, duas molduras de área segura com 60 no topo e base e 90 nas laterais, contra 125, 365 e 90 no Carousel)
- O que isso ensina sobre construir interface: a decisão de espaçamento vira verificável quando o número está ancorado ao pixel que ele descreve. A comparação entre duas especificações se lê de relance porque os dois desenhos usam a mesma escala.

## A área de toque é desenhada maior que o botão visível
- Evidência: wwdc2018_803 (folha 0034, q0304 a q0306, o botão "9" da Calculadora ganha círculo tracejado externo com um ponto na borda; na folha 0035, q0307, o mesmo em volta do "8")
- Evidência: wwdc2018_804 (círculo branco translúcido marcando o dedo sempre junto à borda do botão e nunca no centro, folha 0009, q0080; folha 0010, q0082 a q0084; folha 0012, q0103 a q0105)
- Evidência: wwdc2019_803 (folha 0034, q0298 a q0303, manchas azuis cobrindo área maior que a tecla desenhada do teclado, depois removidas)
- O que isso ensina sobre construir interface: o alvo é maior que a forma pintada, e essa folga só existe se for especificada. Mostrar o toque na borda, não no centro, é a prova de que o componente aguenta mira imprecisa.

## Código é lido com uma faixa de destaque que anda linha a linha entre quadros
- Evidência: wwdc2018_803 (folha 0032, q0282 a q0287, retângulo cinza percorrendo de decelerationRate até a linha do canto mais próximo)
- Evidência: wwdc2019_520 (folha 0012, q0100 a q0105, faixa azul clara acompanhando a fala, com comentário em cinza sempre acima da linha relevante)
- Evidência: wwdc2019_223 (folha 0029, q0254 a q0261, retângulo azul semitransparente grifando a linha em discussão)
- Evidência: wwdc2019_244 (folha 0002, q0016 a q0018, a faixa sai da condicional e vai para a linha de fallback)
- Evidência: wwdc2019_206 (folha 0021, q0187 para q0188, o realce azul aparece só no quadro seguinte, sobre a linha que mudou)
- O que isso ensina sobre construir interface: quando o conteúdo é denso e imutável, o cursor de leitura é o que muda. Um retângulo translúcido move o foco sem reescrever nada em volta.

## Negação é marca gráfica sobre o próprio texto, com o original ainda legível
- Evidência: wwdc2018_802 (folha 0010, q0085 para q0086, os passos 1 e 2 do treino recebem risco e a numeração original continua visível)
- Evidência: wwdc2019_802 (folha 0008, q0065, a lista de sete passos aparece sobre a foto da quadra com os itens 4 e 5 riscados)
- Evidência: wwdc2018_801 (folha 0027, q0235, o termo recebe um traço cortando a palavra em vez de ser negado só na fala)
- Evidência: wwdc2018_803 (folha 0037, q0329, X vermelho grande sobre um nome de classe enquanto os outros dois ficam intactos acima)
- O que isso ensina sobre construir interface: apagar o item destrói a comparação. Riscar mantém o antes e o depois no mesmo quadro, e é assim que se prova que algo foi eliminado.

## Pares de certo e errado vêm com rótulo que nomeia o defeito
- Evidência: wwdc2018_803 (folha 0015, q0127 a q0129, dois círculos destacados em vermelho com o rótulo "Too much visual change"; folha 0010, q0090, uma tela recebe "Not spatially consistent" ao lado)
- Evidência: wwdc2018_811 (folha 0004, q0032 a q0034, e folhas 0005 a 0008, itens com ícone circular verde de verificação para fazer e vermelho com "x" para evitar, um por quadro)
- Evidência: wwdc2019_244 (folha 0006, q0049 para q0054, os círculos de cor viram marca de verificação verde e "X" vermelho no mesmo layout de lista)
- O que isso ensina sobre construir interface: o erro precisa de nome, não só de aparência. O rótulo transforma um julgamento estético em critério repetível por outra pessoa.

## Comparação isola uma variável por vez, tudo o mais igual
- Evidência: wwdc2018_803 (folha 0005, q0040, quatro mãos tocando o mesmo círculo rotuladas "no lag", "50ms", "100ms" e "200ms"; folha 0015, q0131 a q0137, mesma forma em 30fps e 60fps e depois Normal, Motion Blur e Motion Stretch)
- Evidência: wwdc2018_804 (folha 0007, q0062, nove variações de botão de uma vez, três formatos por três tratamentos)
- Evidência: wwdc2019_206 (folha 0013, q0110 a q0113, duas telas gêmeas com a mesma frase e o mesmo layout, mudando só o ícone, uma marcada como sistema antigo e outra como novo)
- Evidência: wwdc2019_211 (folha 0016, q0142 a q0144 para folha 0017, q0149 a q0153, a mesma composição do Carousel ganha sinopse e ficha técnica à direita)
- Evidência: wwdc2018_801 (folha 0024, q0212 a q0216, grade de doze variações da mesma letra em três linhas por quatro colunas)
- O que isso ensina sobre construir interface: a grade de variações resolve a discussão que a alternância entre telas não resolve. Ver tudo junto revela a família; ver um por vez revela o efeito.

## Antes e depois no mesmo enquadramento, marcado por uma etiqueta discreta
- Evidência: wwdc2019_104 (folha 0030, q0262 para q0264, a foto aparece com a etiqueta "ORIGINAL" no canto e no quadro seguinte sem etiqueta e com cor diferente)
- Evidência: wwdc2019_206 (folha 0026, q0226 para q0227, o mesmo pop-over perde duas palavras e ganha ícones em linha, do tamanho da fonte ao redor)
- Evidência: wwdc2019_802 (folhas 0021 e 0022, a demo antiga com valores fixos na barra inferior contra a versão por gesto com popup e régua numerada)
- O que isso ensina sobre construir interface: quando o enquadramento não muda, a diferença salta sozinha. Uma etiqueta pequena no canto substitui um slide inteiro de explicação.

## Diagramas são montados por acréscimo e apagam o que não está em discussão
- Evidência: wwdc2018_804 (folha 0003, q0021 a q0026, ciclo de seis nós com três apagados para restar só um em branco forte; a manobra se repete na folha 0009, q0076 a q0078, e as notas registram que a fala não descreve o recurso)
- Evidência: wwdc2019_803 (a caixa "Interface" com o ícone de pessoa na folha 0004, q0036, ganha a camada "Model" na folha 0006 e se subdivide na folha 0007, q0055 a q0058, até os quatro itens de cada lado na folha 0016)
- Evidência: wwdc2019_211 (folha 0021, q0183 a q0189, a hierarquia de classes acende em três estágios, primeiro a caixa verde, depois as laranja, depois as azuis)
- Evidência: wwdc2019_520 (folha 0001, q0008 e q0009, diagrama de camadas do sistema com cor por faixa e corte de câmera fechando no trecho relevante)
- Evidência: wwdc2018_803 (folha 0007, q0057 e q0058, os mesmos quatro blocos passam de fileira com seta para grade dois por dois)
- O que isso ensina sobre construir interface: um diagrama só sobrevive a uma hora de sessão se puder ser reusado em estados. Rearranjar os mesmos blocos comunica outra relação sem introduzir vocabulário novo.

## Cor carrega significado fixo que a fala nunca declara
- Evidência: wwdc2019_223 (azul claro para eventos transientes e para a trilha háptica, laranja para contínuo e para rampas, folha 0009; as notas registram que é convenção do material, não do texto falado)
- Evidência: wwdc2019_520 (verde reservado à faixa que contém o assunto da palestra, azul para as APIs já existentes, vermelho para o hardware, folhas 0001 e 0002)
- Evidência: wwdc2019_206 (folha 0012, q0104 a q0108, verde para símbolo de sistema, azul para customizado, roxo para imagem comum)
- Evidência: wwdc2019_104 (folhas 0003 e 0004, q0020 a q0034, categorias em contorno neon rosa e azul enquanto as demais saem em branco sólido, sem menção na fala)
- Evidência: wwdc2019_239 (folha 0004, q0034 a q0036, duas árvores idênticas distinguidas só pelo amarelo do grupo do Xcode contra o azul da pasta do Finder)
- O que isso ensina sobre construir interface: uma paleta de três a quatro cores com papel fixo faz o diagrama se explicar sozinho ao longo de dezenas de slides. A cor vira legenda implícita, e trocar o significado no meio quebraria tudo.

## O layout fica parado e só o valor muda entre dois quadros
- Evidência: wwdc2018_802 (folha 0020, q0172 para q0173, o slider muda de posição e de cor com a lista abaixo intacta; folha 0010, q0082 e q0083, o contador vai de 2/20 para 3/20)
- Evidência: wwdc2019_104 (folha 0027, q0242 para q0243, Temperature passa de 9% para 15% e Tint de 5% para 8% no mesmo painel)
- Evidência: wwdc2019_802 (folha 0006, q0047 e q0048, mesmo cabeçalho, mesmo título e mesmos dois números, trocando só a mídia do rodapé do cartão)
- Evidência: wwdc2018_803 (folha 0024, q0209 a q0214, STIFFNESS sobe de 40 para 100 e DAMPING de 10 para 40 com a bola mudando de posição junto)
- Evidência: wwdc2019_211 (folha 0010, q0088 para q0089, o chevron neutro ganha círculo de fundo azul translúcido ao entrar em foco)
- O que isso ensina sobre construir interface: estado é diferença, e a diferença só é legível quando o resto não se mexe. Isso vale igual para provar um recurso e para desenhá-lo.

## Transição é mostrada no meio, como estado intermediário, nunca como corte
- Evidência: wwdc2019_211 (folha 0011, q0096 e q0098, dois pôsteres na tela ao mesmo tempo, um saindo e outro entrando, com as sinopses se misturando; folha 0039, q0345 a q0349, wipe com faixa vertical clara)
- Evidência: wwdc2018_806 (folha 0015, q0134 e q0135, um cartão é puxado para fora da pilha e deslocado à direita para ser explicado sozinho)
- Evidência: wwdc2018_803 (folha 0011, q0094 a q0098, um terceiro quadrado rotulado "Hinting" surge com brilho entre o estado inicial e o final, e depois vem o card real crescendo)
- Evidência: wwdc2018_802 (folha 0007, q0055 a q0061, a mesma captura cresce ao longo de sete quadros revelando etiqueta, rótulos de nota e ícone de pausa)
- Evidência: wwdc2018_801 (folha 0016, q0136 a q0139, o item ativo da agenda cresce em negrito enquanto os demais esmaecem até sumir, virando cartão de seção)
- O que isso ensina sobre construir interface: o quadro do meio é o que ensina o mecanismo. Projetar a transição como estado, e não como efeito, é o que permite interrompê-la e revertê-la.

## O componente é arrancado da tela e dissecado sozinho
- Evidência: wwdc2018_803 (folha 0040, q0352 a q0355, o interruptor aparece fora de qualquer app, depois só o knob flutuando com sombra e sem a trilha, isolando o plano elevado)
- Evidência: wwdc2019_802 (folha 0034, q0299 a q0304, o interruptor nativo ampliado nos dois estados e em seguida pequeno dentro do painel real, com destaque circular translúcido ligando os dois)
- Evidência: wwdc2018_806 (folha 0022, o cartão de notificação desenhado como retângulo plano fora de qualquer moldura de aparelho, no formato de peça de especificação)
- Evidência: wwdc2019_206 (folha 0006, q0048 e q0049, cinco ícones de volume em fileira com o nome técnico escrito abaixo de cada um)
- O que isso ensina sobre construir interface: tirar a peça do contexto expõe camada, sombra e estado, que a tela cheia esconde. A volta ao contexto real, no quadro seguinte, é o que impede a peça de virar abstração.

## Um contorno colorido aponta o componente exato dentro da foto ou da captura
- Evidência: wwdc2019_223 (folha 0021, q0185 a q0189, círculo verde fino sobre o botão home, a coroa e o seletor, em três molduras enfileiradas)
- Evidência: wwdc2019_520 (folha 0002, q0015 e q0017, caixa de contorno verde arredondado sobre a foto do interior do aparelho, rotulada como o motor háptico)
- Evidência: wwdc2019_211 (folha 0017, q0152 e q0153, caixa de contorno ciano vazada só em volta do bloco novo, depois só em volta da coluna nova)
- Evidência: wwdc2019_244 (folha 0005, q0041, e folha 0006, q0051, contorno verde fixo apontando o item recém-chegado nas telas de Ajustes)
- Evidência: wwdc2019_802 (folha 0032, q0283 a q0285, contorno azul claro marcando o ícone de compartilhar que surgiu entre as duas telas de mapa)
- O que isso ensina sobre construir interface: a anotação vazada não cobre o que está embaixo, então serve para dirigir o olhar sem falsificar a tela. É o mesmo raciocínio de um foco temporário na UI real.

## O mesmo componente aparece em vários aparelhos ao mesmo tempo
- Evidência: wwdc2018_806 (folha 0021, q0188 e q0189, diagrama de anotação com linhas ligando elementos correspondentes entre telefone e relógio, no lugar das capturas; folha 0026, q0226 a q0229, três pares lado a lado com o relógio mais compacto)
- Evidência: wwdc2019_802 (folha 0038, q0335 a q0338, iPad e iPhone lado a lado exibindo o mesmo editor de cor em cruz na mesma proporção de layout)
- Evidência: wwdc2019_520 (folha 0002, q0013, fileira de seis iPhones com springboard real sob a frase sobre consistência entre produtos)
- O que isso ensina sobre construir interface: o argumento de consistência precisa dos dois tamanhos no mesmo quadro. Ligar os elementos equivalentes com linha é mais claro que descrever a correspondência em texto.

## Interface nunca aparece solta: vem em moldura de aparelho ou mockup
- Evidência: wwdc2019_104 (folha 0006, q0046 a q0051, iPad, MacBook e iPhone em moldura real ou mockup com notch visível, apoiados em pedestal ou em perspectiva)
- Evidência: wwdc2019_803 (folha 0018, q0160 e q0161, os exemplos entram na moldura do aparelho com a interface nativa reproduzida, nunca como esboço solto)
- Evidência: wwdc2018_802 (folha 0003, q0020, o mapa aparece dentro do aparelho quando a cena é de uso ou demonstração)
- Evidência: wwdc2019_223 (folha 0008, q0064 a q0070, dois iPhones em moldura realista com notch e relógio, rotulados como mundo real e mundo digital)
- O que isso ensina sobre construir interface: a moldura devolve escala e distância de leitura, que uma captura recortada perde. Sem ela, todo componente parece maior do que é na mão.

## O protótipo é fotografado na mão, fora do slide
- Evidência: wwdc2018_804 (folha 0008, q0069 e q0070, mão segurando um iPhone físico contra fundo claro desfocado; folhas 0011 e 0013, a mesma tela ampliada no telão com uma mão em primeiro plano segurando o aparelho real)
- Evidência: wwdc2019_520 (folha 0011, q0092 a q0094, único trecho com aparelho físico, um círculo vermelho correndo pela tela conforme o aparelho é inclinado, com a palavra "Demo" sobreposta)
- Evidência: wwdc2018_803 (folha 0006, q0052 e q0053, iPhone segurado em mão trocando de Mensagens para a tela de multitarefa no meio do gesto)
- Evidência: wwdc2018_802 (folha 0011, q0097, foto das mãos com o aparelho exibindo o verso de carta que serviu de protótipo inicial)
- O que isso ensina sobre construir interface: gesto, inclinação e alcance do polegar só são demonstráveis com o objeto físico. A captura de tela prova layout; a foto na mão prova ergonomia.

## A ferramenta de projeto entra em cena com painéis e valores legíveis
- Evidência: wwdc2019_206 (folha 0009, q0073 a q0077, o traço se propaga célula a célula no template do Sketch com o painel de exportação aberto; folha 0015, q0132 a q0135, painel do Xcode com Point Size, Scale e Weight e guias azuis de centralização)
- Evidência: wwdc2019_244 (folha 0003, q0019 a q0022, MacBook com o painel de sobreposição de ambiente e o controle de tipo dinâmico ao lado do simulador rodando o app)
- Evidência: wwdc2019_239 (folha 0016, q0140 a q0143, os checkboxes do esquema sendo marcados um de cada vez, na mesma ordem falada)
- Evidência: wwdc2018_803 (folha 0024, q0209 a q0214, painel de três sliders de massa, rigidez e amortecimento com escala e valor ao lado da bola animada)
- Evidência: wwdc2019_802 (folha 0029, q0254 a q0256, software de animação com canvas, camadas, linha do tempo e quadros-chave, e a expressão do personagem mudando entre quadros)
- O que isso ensina sobre construir interface: mostrar o painel com os valores torna o resultado reproduzível. Quem assiste sai sabendo qual controle mexer, não só qual efeito admirar.

## Artefatos de processo entram como prova, do rabisco à prancha de especificação
- Evidência: wwdc2019_802 (folha 0002, q0011 a q0013, prancha real com paletas primária e secundária, tabela de estados de componente, especificação tipográfica com alfabeto completo e concept art a lápis anotada à mão; folha 0037, q0325 a q0329, três níveis de fidelidade do mesmo editor, de caixas cinza até a versão final)
- Evidência: wwdc2019_104 (folha 0021, q0182, e folha 0026, q0227, colagens de bastidores com esboço a mão em papel e wireframes)
- Evidência: wwdc2018_802 (folha 0011, q0097, carta de baralho fotografada como protótipo inicial; folhas 0014 e 0015, formulário e desenhos de patente em traço fino com peças numeradas em vista explodida)
- Evidência: wwdc2018_801 (folha 0024, q0212 a q0216, a técnica de caricatura tipográfica mostrada em etapas, da letra em traço fino até a grade de doze variações)
- O que isso ensina sobre construir interface: o caminho até a forma final é argumento, não bastidor. Mostrar a versão feia anterior valida a decisão que sobreviveu.

## O que não se vê vira gráfico ao lado da tela, e o arquivo de texto ganha equivalente gráfico imediato
- Evidência: wwdc2018_803 (folha 0009, q0077 a q0079, a curva de aceleração vertical do dedo aparece ao lado das telas, quase reta, depois com queda, depois com um pico verde marcando o instante da pausa)
- Evidência: wwdc2019_520 (folha 0014, q0123 a q0126, dois gráficos empilhados no mesmo eixo de tempo mostram o bloco contínuo perdendo altura exatamente na região afetada pelo parâmetro)
- Evidência: wwdc2019_223 (folha 0033, q0289 a q0297, o arquivo é montado chave por chave em JSON e logo em seguida os mesmos valores reaparecem como duas barras de intensidade e nitidez)
- O que isso ensina sobre construir interface: sensação e temporização precisam de representação visual para virar objeto de projeto. Colocar o dado bruto e a forma gráfica lado a lado ensina a ler um pelo outro.

## Estatística é imagem: número enorme, legenda minúscula, nada mais
- Evidência: wwdc2019_803 (folha 0011, q0094 e q0096, "75%" sobre a palavra Accuracy; folha 0012, q0102 e q0103, a mesma composição com a razão do Face ID)
- Evidência: wwdc2018_802 (folha 0016, q0136 a q0140, número isolado com legenda pequena em cinza, depois grade densa de pictogramas humanos com um único destacado em branco)
- Evidência: wwdc2019_244 (folha 0003, q0023 para q0024, a estatística sobre sensibilidade a movimento entra colada na mesma tela de app já em cena, sem slide separado)
- Evidência: wwdc2019_802 (folha 0038, q0335 a q0338, número grande com a legenda de nomes de cor ao lado das duas telas)
- O que isso ensina sobre construir interface: um número sem contexto gráfico não fixa; encostado na tela que ele descreve, vira consequência. Contraste de corpo entre número e legenda faz a hierarquia inteira.

## Uma palavra ou frase sozinha em tipografia grande sobre preto pontua o raciocínio
- Evidência: wwdc2019_104 (fundo preto absoluto, uma palavra por vez em branco sem serifa e centralizada, do primeiro título na folha 0001 até cada prêmio novo nas folhas 0032, 0036 e 0045)
- Evidência: wwdc2018_802 (folha 0001, q0007 a q0009, e folha 0028, q0244 a q0246, o cartão de palavra isolada é o recurso dominante e retém só o rótulo final do raciocínio)
- Evidência: wwdc2018_806 (folhas 0003 e 0008 a 0011, frases curtas em branco grande servindo de divisória entre blocos, quase sempre sem imagem de produto junto)
- Evidência: wwdc2019_520 (folha 0017, q0149 e q0150, duas perguntas em tipografia grande sobre tela preta, sem nenhum outro elemento)
- Evidência: wwdc2019_239 (folha 0024, q0208 a q0211, a mesma frase curta cresce em três tamanhos até ocupar a tela sozinha)
- O que isso ensina sobre construir interface: o slide guarda a conclusão, a fala carrega o argumento. Tela vazia é ritmo, e funciona porque o resto da sessão é denso.

## Um pictograma ou emoji gigante carrega o conceito no lugar de texto
- Evidência: wwdc2018_801 (folha 0015, q0131 a q0134, emojis isolados de rosto pensativo, óculos escuros e piano, centralizados em fundo preto com muito vazio ao redor)
- Evidência: wwdc2019_520 (folha 0007, q0056 a q0060, cada tipo de evento aparece como coluna com um ícone que carrega a metáfora, martelo, violino e alto-falante)
- Evidência: wwdc2018_811 (folha 0002, q0011 a q0013, a estrutura inteira da palestra é um diagrama de três ícones pictóricos com legenda curta abaixo, retomado no fechamento na folha 0010)
- Evidência: wwdc2018_806 (folha 0007, q0061 a q0063, um emoji de rosto pensativo surge entre as duas rotas de permissão antes de o modal desaparecer)
- O que isso ensina sobre construir interface: um símbolo bem escolhido segura um conceito por uma sessão inteira e volta como âncora no resumo. Legenda curta embaixo evita que o símbolo dependa de interpretação.

## Hierarquia de ação por cor e área: primária cheia, secundária neutra, destrutiva vermelha e separada
- Evidência: wwdc2019_104 (folha 0022, q0197, ação secundária em cinza neutro contra a primária em amarelo-lima e com área maior, na mesma barra)
- Evidência: wwdc2018_806 (folha 0004, q0033 a q0035, azul sólido marcando a ação recomendada entre botões empilhados; folha 0013, q0110 a q0113, o botão destrutivo em vermelho separado dos demais numa segunda camada de confirmação dentro do mesmo cartão)
- Evidência: wwdc2019_211 (folha 0009, q0078 a q0081, "Play" branco sólido empilhado sobre "More Info" cinza, ancorados no terço inferior)
- Evidência: wwdc2019_803 (folha 0031, q0272 a q0275, botão azul de largura total na conclusão e, na tela de Ajustes, a ação destrutiva em vermelho abaixo dos interruptores)
- O que isso ensina sobre construir interface: peso visual e tamanho comunicam consequência antes da leitura do rótulo. Separar a ação destrutiva do grupo é parte do desenho, não detalhe.

## Seleção é contorno ou cor de destaque sobre um item que não muda de forma
- Evidência: wwdc2019_802 (folha 0004, q0034, três cartões de opção iguais com o ativo em contorno amarelo; folha 0008, q0069, o mesmo padrão em outro app com contorno vermelho)
- Evidência: wwdc2019_104 (folha 0028, q0249 a q0251, a barra de proporções mostra todas as opções e realça a escolhida em laranja, com a foto virando quadrada no quadro seguinte)
- Evidência: wwdc2019_211 (folha 0028, q0246 a q0249, avatares circulares com anel de seleção no ativo; folha 0010, q0085 e q0086, um ponto de paginação vira forma retangular azul)
- Evidência: wwdc2019_239 (folha 0016, q0136 a q0138, lista de texto puro com o item escolhido em azul e marca de seleção, sem ícone nem medidor)
- O que isso ensina sobre construir interface: manter forma e tamanho de todos os itens e mudar só a marcação preserva a leitura da grade. A seleção precisa ser reconhecível a distância, não sutil.

## Blocos de cor pura vêm antes da interface real para fixar proporção
- Evidência: wwdc2019_211 (folha 0008, q0069 a q0071, retângulo grande verde para o conteúdo e retângulos pequenos embaixo para doca e fileira, sem texto nem imagem dentro; folha 0032, q0281 e q0282, barra de abas laranja e conteúdo amarelo mudando de posição vertical)
- Evidência: wwdc2019_239 (folha 0005, q0037 a q0042, retângulos verticais no formato de tela passando de nuvem desordenada para grade regular e depois para blocos ligados por linha)
- Evidência: wwdc2019_802 (folha 0037, q0325, protótipo de baixa fidelidade com caixas retangulares cinza e texto, sem cor e sem ícone)
- Evidência: wwdc2018_803 (folha 0030, q0266 a q0270, retângulo dividido em quatro regiões de canto em contorno fino, com um retângulo amarelo saltando entre elas)
- O que isso ensina sobre construir interface: proporção e posição são decisões anteriores a cor, ícone e texto. Blocos sem conteúdo impedem que a discussão escorregue para acabamento cedo demais.

## Em jogo, a interface some: o HUD fica no mínimo e nos cantos
- Evidência: wwdc2019_802 (folha 0015, q0129 a q0131, apenas um ícone de pausa no canto superior esquerdo em toda a sequência; folhas 0024 e 0025, q0215 a q0224, só o indicador de nível e um botão no canto oposto, sem barra de vida)
- Evidência: wwdc2019_104 (folhas 0041 a 0043, q0361 a q0385, badges circulares de contagem, placar e rótulo de nível em tipografia branca fina nos cantos, sem moldura)
- Evidência: wwdc2018_801 (folha 0020, q0176 a q0178, ambiente isométrico com grade de quebra-cabeça translúcida sobre o cenário, sem números, botões ou tutorial visíveis)
- O que isso ensina sobre construir interface: quando o conteúdo é a experiência, cada elemento persistente precisa justificar a própria presença. Cantos e translucidez são o que sobra quando se corta o resto.

## O layout do HUD não se mexe enquanto o mundo e os números mudam
- Evidência: wwdc2019_104 (folha 0024, q0199 a q0216, velocímetro, cronômetro e ícones mantêm posição idêntica por rua noturna, túnel e rodovia molhada, com a velocidade variando de quadro a quadro e textos efêmeros de conquista surgindo e sumindo sem deslocar nada)
- Evidência: wwdc2019_802 (folha 0003, q0021 a q0027, HUD de corrida com posição e velocímetro subindo de 85 para 110 e 146, e o selo de modo aparecendo entre dois quadros sem alterar o resto)
- O que isso ensina sobre construir interface: elemento efêmero entra em camada própria e nunca empurra o layout. Posição fixa é o que permite ler um número em movimento.

## As telas menos glamourosas entram como prova, ajustes inclusive
- Evidência: wwdc2018_806 (folha 0012, q0108, e folha 0013, q0115 a q0117, três telas de configuração diferentes compartilhando o mesmo componente de lista com chave à direita, variando só ícone e linha de descrição)
- Evidência: wwdc2019_244 (folha 0004, q0031 para q0032, a lista de Ajustes ganha um item por quadro, e o novo recebe contorno verde na folha 0005, q0041)
- Evidência: wwdc2019_802 (folha 0032, q0281 a q0283, a coesão do jogo é demonstrada indo até a tela de configurações, com interruptores nativos alinhados à direita dos rótulos)
- Evidência: wwdc2019_803 (folha 0031, q0274 e q0275, Ajustes com interruptores verdes e ação destrutiva em vermelho fechando o fluxo de calibração)
- O que isso ensina sobre construir interface: um sistema se prova na tela chata, onde o componente padrão aparece sem maquiagem. Repetir o mesmo componente de lista em três contextos é o argumento de coerência.

## O apresentador é subordinado ao conteúdo, quase nunca sozinho na tela
- Evidência: wwdc2019_206 (durante as demonstrações ele fica reduzido a uma miniatura no canto inferior esquerdo, e sozinho só na abertura, nas trocas e no encerramento)
- Evidência: wwdc2019_520 (o esqueleto do slide já prevê o apresentador pequeno, centralizado ou à direita, abaixo ou ao lado do texto, em toda a palestra)
- Evidência: wwdc2018_806 (folha 0015, o slide de código traz o apresentador semitransparente atrás do bloco, e quadros só de apresentador ficam restritos a closes avulsos)
- Evidência: wwdc2019_244 (nas oito folhas não há nenhuma registrada só com a apresentadora; até os slides de princípio a mostram pequena em cena)
- Evidência: wwdc2019_211 (em boa parte das folhas ele aparece pequeno ao lado da projeção, não no lugar dela)
- O que isso ensina sobre construir interface: a moldura da apresentação segue a mesma regra da interface, conteúdo primeiro e chrome reduzido. A pessoa entra como escala e ritmo, não como assunto.

## Citação tem anatomia própria e constante, e nunca se mistura com lista
- Evidência: wwdc2018_801 (folha 0003, q0026 e q0027, e folha 0004, q0030 a q0036, bloco grande com nome e função em texto pequeno e cinza logo abaixo, enquanto a pergunta da entrevistadora usa outro alinhamento e nenhuma atribuição)
- Evidência: wwdc2018_811 (folhas 0003, 0004, 0008 e 0009, frase grande entre aspas centralizada com o nome do autor pequeno e cinza abaixo, sempre em tela própria)
- O que isso ensina sobre construir interface: dar componente próprio a um tipo de conteúdo evita que o leitor tenha que decidir de quem é a voz. A atribuição fixa no mesmo lugar sustenta citações longas quebradas em vários quadros.

## Sobreposição semitransparente costura a tela ao mundo físico
- Evidência: wwdc2018_802 (folha 0005, q0045, tela do app fundida à foto de rua; folha 0015, q0130 a q0132, desenho de patente sobre fotos de bagageiro e cockpit; folha 0027, q0240, tela do relógio sobre a foto de uma mão)
- Evidência: wwdc2019_802 (folha 0008, q0065 e q0070, a lista de passos aparece sobre a fotografia real da quadra, e o esqueleto de linhas laranja entra sobre as articulações do jogador)
- Evidência: wwdc2019_803 (folha 0008, q0064 a q0066, a frase entra sobreposta à matriz de fotos que ela descreve, em vez de ocupar um slide próprio)
- O que isso ensina sobre construir interface: sobrepor no lugar de justapor mantém a causa e o efeito no mesmo quadro. É a mesma lógica de uma camada de anotação que pode ser ligada e desligada.

## Verde marca o que é novo
- Evidência: wwdc2019_206 (folha 0025, selo verde de novidade no canto dos slides de código, junto com o realce azul que aponta a linha alterada)
- Evidência: wwdc2019_211 (folha 0021, q0183 a q0189, cada estágio do diagrama traz selo circular verde no canto, recurso repetido nos slides técnicos das folhas 0029 a 0033)
- Evidência: wwdc2019_244 (folha 0005, q0041, e folha 0006, q0051, contorno verde fixo em volta do item recém-adicionado nas telas de Ajustes)
- O que isso ensina sobre construir interface: uma marca única e constante para novidade poupa o leitor de comparar versões de cabeça. Ela precisa ser periférica o bastante para não competir com o conteúdo.

## Abertura e fechamento seguem cartela sóbria, com crédito em corpo pequeno
- Evidência: wwdc2019_244 (folha 0001, q0002, fundo escuro, título branco alinhado à esquerda, marcação do evento pequena no canto e nome e cargo em corpo menor; folha 0008, q0067, encerramento com a maçã branca centralizada sobre preto e um bloco pequeno de texto legal)
- Evidência: wwdc2019_520 (folha 0009, q0075 a q0077, a troca de palestrante é marcada por slide de crédito com nome e função em texto pequeno no canto; folha 0018, q0154 a q0161, o fecho encadeia resumo, tabela de horários e cartela final com a maçã)
- Evidência: wwdc2019_104 (folha 0031, q0275, e folhas 0035 e 0036, legenda no rodapé com ícone do app e nome da equipe, e a folha 0052 fecha com o logotipo em contorno fino)
- Evidência: wwdc2019_803 (folha 0042, q0376 e q0377, slide de referências seguido do logotipo, sem nenhum efeito)
- O que isso ensina sobre construir interface: o crédito fica em corpo pequeno e posição fixa, longe do conteúdo. A moldura da sessão é sempre a mesma, o que faz cada abertura ser reconhecida sem ser lida.

## Tipografia gigante cortada pela borda serve de fundo atrás da pessoa
- Evidência: wwdc2018_801 (folha 0006, q0047 e q0049, letras enormes em cinza claro cortadas na borda da tela atrás de um close da apresentadora, às vezes com palavras soltas, às vezes com o nome do entrevistado que entra em seguida; repetido nas folhas 0018 e 0019)
- Evidência: wwdc2019_520 (folha 0009, q0075 a q0077, a transição é capturada em quadro intermediário com o fragmento de texto ampliado atrás do novo apresentador)
- O que isso ensina sobre construir interface: texto ampliado além da moldura funciona como textura de fundo e dá profundidade sem ilustração. A legibilidade parcial é aceitável quando o papel do elemento é ambiente, não informação.

## Parâmetro abstrato vira régua com exemplos que o público já tocou
- Evidência: wwdc2019_223 (folha 0025, q0217 a q0225, o mesmo eixo linear nasce vazio, ganha rótulo nos dois polos e recebe dois marcadores ancorados a exemplos reais, o botão de lanterna perto do extremo e o alternador de apps mais ao centro)
- Evidência: wwdc2019_520 (folha 0007, q0061 a q0063, e folha 0008, q0064 a q0067, a mesma régua de 0.0 a 1.0 se preenche em etapas, primeiro os polos, depois um marcador com o botão de lanterna, depois um segundo com miniatura emoldurada do alternador de apps)
- O que isso ensina sobre construir interface: um valor numérico sem referência não orienta escolha. Ancorar as pontas e um ou dois pontos conhecidos transforma a escala em julgamento possível.

## Fluxo de execução desenhado como diagrama vivo, com lista numerada de um lado e objetos mudando de estado do outro
- Evidência: wwdc2019_223 (folhas 0027 e 0028, q0235 a q0244, a lista cresce à esquerda enquanto blocos coloridos por tipo de objeto trocam de etiqueta entre parênteses, com marcações de conclusão, até o sétimo passo em q0244)
- Evidência: wwdc2019_520 (folha 0010, q0082 a q0089, a mesma estrutura com cor fixa por tipo, setas ligando os objetos e uma seta verde apontando da etapa ativa para o objeto correspondente)
- O que isso ensina sobre construir interface: sequência e estado são duas informações diferentes e cabem no mesmo quadro. A lista dá a ordem, as caixas dão a consequência, e a seta amarra as duas.

## Achados de fonte única

- Reparametrização de um mesmo controle: o painel troca massa, rigidez e amortecimento por dois sliders, amortecimento em porcentagem e resposta em segundos, e o gráfico de valor por tempo muda de forma a cada par, subindo sem ultrapassar em um ajuste e criando pico e oscilação em outro (wwdc2018_803, folha 0025, q0217 a q0220, fechando com um feixe denso de curvas sobrepostas em q0223 e q0224).
- Ponto de luz verde marcando o contato exato, com rastro de gradiente na direção do movimento e a lista de dados inferidos ao lado, posição, velocidade, rapidez e força (wwdc2018_803, folha 0012, q0101 a q0103); o mesmo ponto fica aceso no canto do botão enquanto a tela troca de conteúdo, indicando pressão contínua (folha 0013, q0110 a q0112).
- Anatomia do seletor rolável: três colunas de valores com a linha central maior e mais clara, e as adjacentes perdendo contraste conforme se afastam, com ajuste de opacidade e nitidez sugerindo o assentamento após a rolagem (wwdc2018_803, folha 0028, q0244 a q0246).
- Nos cartões de notificação rica, os botões são sempre empilhados em largura total e nunca lado a lado, com o cartão ganhando um fechamento circular no canto e a mídia em largura total acima do texto (wwdc2018_806, folha 0017, q0148 a q0152).
- O pedido de permissão prolonga o próprio cartão da notificação para baixo e põe os dois botões dentro dele, reaproveitando o par de ações do modal sem abrir modal nenhum (wwdc2018_806, folha 0006, q0053 e q0054).
- No relógio, cada tipo de interação recebe controle próprio dentro da notificação, sobre fundo preto de tela cheia: fileira de cinco estrelas mais botão de pagamento, dois botões redondos de menos e mais com o valor mudando entre quadros, mostrador circular com número dentro de um anel, e lista com caixas de marcação redondas (wwdc2018_806, folhas 0022 e 0023, q0194 a q0206).
- Um código de leitura óptica ocupa o mostrador inteiro em branco, sem nenhum outro elemento de interface na tela (wwdc2018_806, folha 0024, q0214 e q0215).
- As escalas de símbolo chegam como matriz pré-desenhada, grade de duas dimensões com pesos nas colunas e escalas nas linhas, a mesma no app de design e no ambiente de desenvolvimento, em vez de cálculo em tempo real (wwdc2019_206, folha 0008, q0068 a q0070, e folha 0009, q0078 e q0079).
- A linha de base é desenhada como medida visível, com deslocamentos anotados em laranja de menos 3,5 e mais 4,5 para dois ícones diferentes, e um retângulo de contorno delimitando os limites do ícone (wwdc2019_206, folha 0019, q0165 a q0169).
- Alinhamento horizontal demonstrado com guia amarela pontilhada atravessando a coluna de avatares de uma lista de comentários, seguida de uma seta bidirecional medindo a distância até o texto (wwdc2019_206, folha 0020, q0175 a q0177).
- A demo de código é gravada ao vivo e não pós-produzida: aparecem popups de autocompletar por cima do texto sendo digitado, avisos amarelos na margem enquanto a estrutura está incompleta e um erro vermelho depois que os casos são preenchidos (wwdc2019_211, folha 0022, q0195 a q0198, e folha 0024, q0212 a q0216).
- Recapitulação como nuvem de palavras hierarquizada por corpo de fonte, com todos os princípios da seção em uma tela só (wwdc2019_211, folha 0012, q0104).
- Dois temas visuais convivem na mesma palestra sem conflito: o protótipo aparece em tema claro com cabeçalho cinza escuro sobre fundo claro, enquanto a tela inicial real e o carrossel aparecem sempre escuros (wwdc2019_211, folha 0014, q0120 a q0123, e folha 0020, q0177).
- Quatro rodas de cor de doze fatias enfileiradas, rotuladas como visão normal e três tipos de daltonismo, cada uma das três últimas com um círculo de cor de referência abaixo, mostrando matizes distintos colapsando em tons parecidos (wwdc2019_244, folha 0005, q0044).
- Diagrama de escala tipográfica em duas colunas ligadas por seta, a da esquerda com os onze nomes de estilo todos no mesmo corpo pequeno e a da direita com cada nome renderizado no seu tamanho e peso reais (wwdc2019_244, folha 0002, q0013).
- O modelo de três fases ganha forma gráfica própria, três discos alaranjados vistos de perfil, apresentados juntos e sem ênfase na primeira aparição e depois com o disco da fase corrente destacado a cada bloco (wwdc2018_804, folha 0005, q0045; folha 0008, q0071; folha 0011, q0097).
- Comparação de som feita com coluna de círculos rotulados A, B e C ao lado de uma tela de app que não muda, um círculo aceso por vez, e depois um círculo verde com marca de verificação confirmando a escolha (wwdc2018_804, folhas 0018 e 0019, q0156 a q0159).
- Estado pressionado feito só por escurecimento da mesma cor, sem mudança de forma, borda ou sombra, com o ponto de toque nas bordas do botão (wwdc2018_804, folha 0010, q0087 a q0090).
- Duas ações empilhadas na mesma tela, a de cima esmaecida e a de baixo viva, exibindo ao mesmo tempo a ação disponível e a ação ativa em vez de cortar entre telas (wwdc2018_804, folhas 0013, 0014 e 0018, q0126, q0156 e q0159).
- Anel circular de progresso com o número de repetições dentro, nome do exercício em maiúsculas abaixo, três ícones pequenos em linha para anterior, atual e próximo, e barra linear no topo (wwdc2018_802, folha 0010, q0082 e q0083).
- Grade de três colunas de botões circulares com pictograma branco sobre fundo escuro, rótulo abaixo de cada ícone e confirmação no canto superior direito (wwdc2018_802, folha 0009, q0079).
- Slide de definição de dicionário para fixar um termo, com a palavra em negrito, transcrição fonética em itálico, classe gramatical e significados numerados alinhados à esquerda (wwdc2018_802, folha 0016, q0141, e folha 0009, q0077).
- O mesmo layout de app de clima se repete idêntico entre cidades, variando apenas a cor de fundo e a cena em arte de pixel no rodapé conforme clima e hora (wwdc2018_802, folha 0018, q0155 e q0158 a q0160).
- Cor vira o próprio conteúdo do slide: cada resposta sobre cor favorita ocupa a tela inteira naquela cor, com rótulo fixo no mesmo tamanho e posição, seguida de uma cartela de amostra com moldura branca e legenda e de uma grade de amostras do sistema em duas fileiras com etiqueta pequena sob cada bloco (wwdc2018_801, folhas 0034 e 0035, q0299 a q0313).
- Personagem ilustrado no lugar de foto de usuário, atravessando a palestra inteira e mudando de papel, inclusive como fileira de três personas nomeadas com legenda de duas linhas (wwdc2018_811, folha 0006, q0053, e folhas 0005, 0008 e 0010).
- Estrutura narrativa desenhada como diagrama de linha minimalista, traço branco fino sobre fundo preto, sem cor nem textura, evoluindo de um degrau único para uma sequência de degraus subindo e descendo, cada um com seu rótulo (wwdc2018_811, folha 0008, q0071 e q0072; as notas registram que a fala não descreve o recurso).
- Histórico de versões representado como grafo abstrato, uma linha azul central com ramos amarelo e verde de círculos conectados, sem um único rótulo de texto (wwdc2019_239, folha 0009, q0078 e q0079).
- O rótulo de seção entra sobreposto à própria captura de ferramenta, no canto superior esquerdo, dispensando um slide separado de transição (wwdc2019_239, folha 0018, q0154 para q0155, e folha 0022, q0193 para q0194).
- O indicador de progresso da cerimônia é construído sobre a grade do palco: uma fileira de oito retângulos de cantos arredondados com contorno tracejado, inicialmente vazios, que vai recebendo o ícone de cada app premiado, de cinco até nove ícones ao longo do evento (wwdc2019_104, folha 0007, q0062; folhas 0032, 0036, 0040, 0045 e 0050).
- Dados espaciais desenhados em vez de tabelados: meia quadra simplificada com pontos vermelhos para erro e laranja para acerto marcando a posição de cada tentativa, com o vídeo embutido no topo da mesma tela e a estatística ao lado (wwdc2019_104, folha 0047, q0418 para q0419).
- O feedback explícito evolui reutilizando o mesmo componente: dois botões redondos surgem sobre a tela escurecida, viram itens dentro do menu de ação nativo e no fim são trocados, no mesmo menu, por opções que nomeiam a consequência (wwdc2019_803, folhas 0035 e 0036, q0313 a q0324).
- O erro é apresentado como par de retratos em moldura branca tipo crachá, primeiro um sozinho e depois ao lado de um homem parecido, e na folha seguinte as mesmas molduras escurecem para receber a frase de destaque (wwdc2019_803, folhas 0012 e 0013, q0106 a q0110).
- O ensino do gesto é desenhado como camada sobre a própria cena do jogo, com a frase de explicação e o rótulo da ação acompanhado do ícone circular do botão correspondente, em vez de painel separado (wwdc2019_802, folha 0003, q0027).
- Vocabulário geométrico fixo para um sentido que não se vê: barra reta, gota arredondada, triângulo pontudo e bloco largo aparecem soltos primeiro e depois são formalizados dentro de um plano cartesiano com os dois eixos rotulados de 0.0 a 1.0 (wwdc2019_223, folhas 0003, 0004 e 0013, q0027 a q0031 e q0115 e q0116).
- Contraste comunicado por densidade de elementos, não por forma: o slide de um lado traz poucas barras em pares simples e o do outro acumula bem mais barras na mesma trilha (wwdc2019_223, folha 0016, q0137 a q0141).
- Fotografia real do mecanismo como argumento de causalidade: engrenagens douradas e prateadas com rubis, em aproximações sucessivas de câmera, até o close tridimensional da coroa serrilhada com anel vermelho (wwdc2019_223, folha 0010, q0086 a q0090).
- Camada da especificação que só existe no diagrama: a árvore hierárquica do formato, em caixas com efeito de pilha de cartões, expõe elementos que não tinham sido construídos no código das folhas anteriores (wwdc2019_223, folha 0034, q0299 e q0300).
