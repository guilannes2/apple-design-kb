# wwdc2025 (parte 1)

## Create icons with Icon Composer (id: wwdc2025_361, 14.6 min)

- Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/361/.
- Tese central: o Icon Composer é a ferramenta que consolida, num único arquivo, a criação de ícones de app com Liquid Glass para iPhone, iPad, Mac e Watch, eliminando a necessidade de exportar dezenas de tamanhos e variações manualmente.

O processo de design que a Apple descreve:
1. Desenhar no software de preferência (recomenda-se um que exporte SVG, para escalabilidade), usando um dos templates de ícone da Apple Design Resources (Figma, Sketch, Photoshop, Illustrator).
2. Organizar a arte em camadas (layers), pensando em profundidade Z: fundo na base, elementos empilhados acima. Separar cores em camadas distintas dá mais controle depois.
3. Manter a arte "reduzida à essência gráfica": chata, opaca, fácil de controlar, porque efeitos como blur, sombra, especular, opacidade e translucidez são aplicados depois, dentro do Icon Composer, como propriedades do Liquid Glass, não devem ser "assados" na arte de origem.
4. Exportar camadas como SVG (texto precisa virar contorno, pois SVG não preserva fontes); usar PNG só para gradientes customizados, imagens raster ou o que não puder ser expresso em SVG. Nunca exportar a máscara de recorte (retângulo arredondado ou círculo), pois ela é aplicada automaticamente depois.
5. Importar no Icon Composer, ajustar aparência (default, dark, mono, e as variantes clear/tinted derivadas), plataformas e propriedades de glass.
6. Exportar o arquivo .icon e arrastar para o Xcode.

Princípios enunciados e o porquê:
- Um artwork, quatro plataformas: dá identidade consistente ao app onde quer que ele apareça.
- Grupos controlam como elementos se empilham e recebem propriedades de glass; o limite é de até quatro grupos por ícone, porque a Apple concluiu que esse número já contempla a complexidade visual adequada para um ícone.
- Algumas propriedades (opacidade, blend mode, fill) são configuráveis por aparência (light/dark/mono); outras se aplicam a todas, por serem mais consistentes entre modos.
- Legibilidade em mono: pelo menos um elemento do ícone deve ficar branco (geralmente o mais reconhecível), e as demais cores mapeadas para tons de cinza; a conversão automática existe, mas precisa ser ajustada para o melhor contraste.

Técnicas concretas de construção de interface:
- Canvas de 1024px para iPhone, iPad e Mac (unificado nesta atualização); Watch usa 1088px, que "ultrapassa" o retângulo arredondado, mas segue a mesma grade, facilitando a tradução entre plataformas.
- Especular highlight: tratamento de borda automático aplicado mesmo a ícones enviados como imagens individuais (sem passar pelo Icon Composer).
- Seis aparências testáveis: Default, Dark, Clear light, Clear dark, Tinted light, Tinted dark (renomeadas neste ano para default, dark e mono, com clear e tinted derivados automaticamente da arte).
- Sombras neutras (preset) versus sombras cromáticas: usar cromáticas quando a cor sobre fundo branco pode "vazar" para o fundo, criando efeito de luz e fisicalidade do material; é possível manter sombra neutra em dark/mono criando uma variante.
- Ajustes ópticos ao migrar do retângulo arredondado para o círculo do Watch: elementos tocando a borda do canvas precisam ser escalados para tocar a borda de novo, ou o designer pode desenhar já pensando em "bleed" (sangria).
- Painel de preview permite trocar o fundo (para simular contexto e testar legibilidade sobre wallpapers), sobrepor grades do ícone e ver como a luz se move.

Exemplos citados:
- Messages: exemplo de ícone simples, um foreground e um background.
- Home: usa os quatro grupos disponíveis, cada camada como uma peça única de glass.
- Translate: as bolhas de fala e o texto são separados em camadas distintas para permitir blur na sobreposição, sombra sutil e, no modo dark, trocar apenas um fill.
- Calendar (o número do dia): ilustra o problema de especular ficando "pillowy" (estufado) em áreas estreitas; resolve-se desligando o especular do grupo ou o glass da camada.
- Dictionary: sem ajuste de fill, o marcador de página some contra preto no modo dark; a solução é trocar o fill.
- Siri: exemplo de erro comum, exportar a camada já com a máscara de recorte aplicada, quando ela deveria ser deixada de fora do arquivo exportado.

Citações curtas:
"It's the same tool we used this year to update all our own icons."
"Icon Design is moving from a past of simply static images to a future of expressive, multi-layered artworks."

<!-- visual:wwdc2025_361 -->
### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.
- A tela anota a medida do canvas do Watch com uma etiqueta azul sobre uma seleção vetorial com alças de redimensionamento, escrita "1088 x 1088", em cima de um quadrado com grade de círculos concêntricos e linhas de guia (folha 0006, q0046). O mesmo tipo de grade de construção aparece aberto dentro de dois aplicativos de design distintos, um claro com painel de camadas à esquerda e abas Design/Prototype, outro escuro com painel de camadas à direita e a camada "App Icon Template" realçada em vermelho (folha 0005, q0041 e q0042).
- A interface do Icon Composer recebe um tour anotado por setas e rótulos de texto que nomeiam cada região: "Sidebar" apontando a lista de camadas, "Preview panel" apontando o ícone central e "Inspector" apontando o painel de propriedades (folha 0009, q0074 a q0076; folha 0011, q0092). A barra inferior do canvas é anotada em duas seções, "Platforms" à esquerda e "Appearances" à direita (folha 0010, q0087 e q0088).
- A anatomia do inspetor aparece campo a campo, com valores numéricos legíveis. No painel de uma camada estão Color, Opacity 100%, Blend Mode Normal e Fill Automatic, mais Composition com Visible, a imagem "4_House.svg" e Layout em X, Y e escala 100% (folha 0011, q0091 e q0092). Nos painéis de grupo, a seção Liquid Glass traz Mode Individual, Specular ligado, Blur 50%, Translucency 60% e Shadow Chromatic 100%, com Composition mostrando Visible e Layout (folha 0011, q0099; folha 0012, q0101; folha 0014, q0123). Cada seção traz um rótulo de escopo ao lado do título, "Default" ou "All", dizendo se a propriedade vale para uma aparência ou para todas.
- A diferença entre dois quadros mostra a mudança de granularidade de controle: no nível de camada o Liquid Glass é um único toggle "Effects", e de q0098 para q0099 o mesmo painel se abre em cinco campos separados no nível de grupo (folha 0011). Um menu de contexto flutuante junto ao campo Shadow oferece explicitamente "Vary for Default" e "Vary for iOS / macOS" (folha 0012, q0104).
- A profundidade Z é desenhada como ilustração isométrica de folhas empilhadas na diagonal, colada ao lado da lista real de camadas, e o par de quadros contrasta as duas organizações possíveis: quatro camadas de casa dentro de um único grupo (q0084) contra as mesmas quatro distribuídas em quatro grupos separados (q0085), com a pilha isométrica crescendo junto (folha 0010).
- A nomenclatura de exportação é mostrada literalmente numa fileira de miniaturas sobre fundo quadriculado de transparência, numeradas em ordem de camada de "0_Background.svg" a "4_Glyph.svg", cada uma exibindo a arte da sua camada (folha 0008, q0066). Ao lado, dois glifos "A" com o da direita selecionado exibindo contorno azul e pontos de âncora quadrados nas hastes, ilustrando a conversão de texto em contorno vetorial (q0067).
- Um catálogo visual de quatro tipos de conteúdo de camada pareia um exemplo genérico com um ícone real de app para cada categoria: gradiente de malha, ilustrativo, modelado em 3D e fotográfico (folha 0008, q0069 e q0071).
- Pares de aparência isolam uma variável por vez, sempre com o ícone renderizado ao lado do painel e um selo abaixo: sombra Neutral no ícone de Telefone contra sombra Chromatic no ícone de coração, depois a mesma sombra cromática ganhando a linha extra "Dark: Neutral" com o selo mudando de "Default" para "Dark" (folha 0013, q0109 a q0111).
- O caso do preenchimento por aparência aparece em três quadros seguidos do mesmo ícone "Aa": fundo claro com selo "Default", o mesmo ícone sobre preto com selo "Dark" e a amostra de cor aparentemente inalterada, e então a amostra trocada por um vermelho visivelmente mais vivo (folha 0013, q0113 a q0115). Logo adiante, o painel Composition mostra dois arquivos associados à mesma camada, um padrão e um "loupe-dark.png" só para o modo escuro (q0116).
- Variações de cor do mesmo ícone de Clima são dispostas em fileiras horizontais sob rótulos de plataforma, sempre sobre fundo preto: seis tons na linha "iOS iPadOS" com um ícone azul isolado abaixo (folha 0002, q0017 e q0018), depois uma segunda linha de seis para "macOS" com um ícone circular isolado embaixo, esse sem rótulo legível (folha 0003, q0019), e num quadro seguinte mais uma linha com um ícone circular junto do texto "watchOS" (q0021).
- O painel de aparência flutuante mostra os controles concretos: alternância Light/Dark e uma chave "Tinted" com barra de gradiente colorido (folha 0010, q0089) e, no quadro seguinte, "Dark" selecionado, "Tinted" ativado e duas barras deslizantes, uma de arco-íris e outra em escala de cinza (q0090), tudo aplicado a três exemplares do mesmo ícone de casa sobre fundo branco, preto e roxo.
- O mesmo ícone de casa é posto contra sete fundos diferentes em sequência, trocando só o que está atrás dele: verde-oliva liso, gradiente de nebulosa, textura de gelo, foto de tulipas, tecido laranja, água com borboleta e cinza claro padronado; o ícone passa de opaco a translúcido e assume o tom de cada fundo (folha 0015, q0127 a q0133). Dois closes extremos em seguida revelam o brilho e a borda do vidro e fragmentos de uma grade de formas de casa em volta (q0134 e q0135).
- Uma lista de quatro etapas sobreposta ao vídeo do apresentador funciona como marcador de progresso recorrente, sempre com a etapa corrente em branco ou preto e negrito e as demais em cinza apagado: "Deliver" destacada na folha 0005 (q0038), "Export layers" na folha 0007 (q0062), "Icon Composer" na folha 0008 (q0072) e "Deliver" de novo no fechamento (folha 0016, q0136 e q0137).
- Dois exemplos de material de vidro são isolados como cartões de teste rotulados, "Blur" com auréola difusa ao redor e "Shadow" com sombra definida embaixo, em quadrados brancos sobre fundo preto (folha 0007, q0060). O painel de camadas do exemplo de Traduzir nomeia os elementos por convenção, "Glyph", "Bubble" e "Background", com o item selecionado em azul (q0055 e q0056).
- Grades de ícones do sistema abrem e fecham o vídeo, primeiro em recortes parciais sobre fundo cinza claro (folha 0001, q0004 a q0006) e depois como duas telas iniciais densas ocupando o quadro inteiro (folha 0016, q0139 e q0141). Um quadro quase todo preto isola um ícone escuro de contraste baixíssimo, quase invisível contra o fundo (q0138).
Proporção visual: a maior parte dos quadros é ícone, slide ou interface do Icon Composer; o apresentador aparece em cortes curtos entre as demonstrações em quase todas as folhas, e a última folha (0017, q0145) é só ele, com tingimento rosa de encerramento.
Divergências ou limites registrados: as notas marcam pares de quadros sem diferença visível apurável (folha 0002, q0017 para q0018; folha 0003, q0023 para q0024 e q0026 para q0027) e um ícone circular cujo rótulo de plataforma não ficou claramente legível (folha 0003, q0019), além de um quadro com selo "Mono" em página aparentemente vazia (folha 0014, q0118).
<!-- /visual:wwdc2025_361 -->

## What's new in SF Symbols 7 (id: wwdc2025_337, 22.9 min)

- Base: transcrição e 16 de 16 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/337/.
- Tese central: SF Symbols 7 introduz o sistema Draw, que permite que símbolos se desenhem ao longo do próprio caminho vetorial (como caligrafia), além de gradientes e melhorias em Magic Replace, exigindo que designers anotem seus próprios símbolos customizados com pontos-guia para habilitar essas animações.

O processo de design que a Apple descreve:
- Cada símbolo é desenhado a partir de um único ponto vetorial que cria um caminho contínuo; cada curva e ângulo precisa ser deliberado, equilibrado e visualmente comunicativo.
- Um símbolo não é apenas um contorno visível: é construído a partir de formas com contorno cuidadoso, permitindo controle preciso de proporções, espaço negativo e peso visual.
- Algumas formas usam dois caminhos distintos, orientados em direções opostas, o que refina a aparência de cada caminho individualmente e é peça importante para como eles podem animar.
- Para anotar Draw: começar sempre pelo peso "regular" (é a única espessura onde se pode adicionar/remover pontos-guia); o sistema interpola automaticamente para os outros dois pesos-modelo (ultralight e black); é preciso garantir que os pontos-guia associados fiquem na mesma ordem entre regular, ultralight e black (a numeração de pontos-guia ajuda a identificar e corrigir desalinhamentos, marcados em laranja quando sobrescritos).

Princípios enunciados e o porquê:
- Draw foi desenhado para ser flexível: cada símbolo define sua própria direção de desenho (por exemplo, "wind" desenha da esquerda para a direita para sugerir movimento; um caractere árabe desenha da direita para a esquerda, seguindo a direção de escrita).
- Não existe uma única forma correta de posicionar pontos-guia: é tentativa e erro, cabe ao designer testar diferentes posicionamentos.
- Símbolos suportam nove pesos e três escalas, mas o designer só precisa anotar três (o sistema cuida do resto).

Técnicas concretas de construção de interface:
- Dois novos presets de animação: Draw On (anima o símbolo aparecendo) e Draw Off (anima saindo), com opções de playback: By Layer (padrão, cada caminho desenha com atraso escalonado), Whole Symbol (todos os caminhos começam e terminam juntos) e Individually (nova, desenha camada por camada, esperando a anterior terminar).
- Draw suporta formas compostas, como setas com duas formas que se comportam como uma, permitindo que a ponta da seta viaje junto com o caminho.
- Variable draw: renderiza o caminho numa porcentagem específica sobre uma versão com opacidade reduzida da camada, útil para mostrar progresso (download, temperatura, sessão de yoga). Um símbolo pode suportar variable color e variable draw, mas apenas um é escolhido em tempo de renderização (ou "default", que usa o modo preferido do sistema).
- Magic Replace agora reconhece invólucros (enclosures) coincidentes entre dois símbolos e os preserva, substituindo só as camadas diferentes; combina isso com Draw Off (símbolo que sai) e Draw On (símbolo que entra).
- Gradientes: geram um gradiente linear suave a partir de uma única cor-fonte, disponível em cores do sistema e customizadas, em todos os modos de renderização; recomendados especialmente em instâncias maiores.
- Pontos-guia: no mínimo dois por caminho (ponto de início, círculo aberto; ponto de fim, círculo fechado); caminhos mais complexos podem precisar de pontos adicionais, incluindo pontos de canto (corner points, indicados por losango) para curvas com dobras acentuadas.
- Anexos (attachments): elemento não desenhado (como a ponta de uma seta) associado a um ponto-guia, arrastado sobre o ponto para "grudar" e seguir o caminho conforme ele se desenha; a ponta da seta precisa ser um caminho separado da base para permitir isso.
- End caps adaptativos: por padrão os caminhos desenham com ponta arredondada; end caps adaptativos usam o estilo real do caminho durante a animação, disponíveis apenas em símbolos que desenham em uma única direção.
- Símbolos construídos por múltiplos subcaminhos (ex.: um círculo) tratam o primeiro ponto-guia como início e fim simultaneamente (indicado por uma cápsula na borda final do ponto); por padrão desenham em sentido horário, revertível pelo menu de contexto; só suportam animação em direção única, não bidirecional.
- Desenho bidirecional: símbolos com direcionalidade implícita a partir do centro (ex.: wave.3.up) podem ter o ponto inicial no centro e pontos adicionais de cada lado; o sistema reconhece automaticamente a bidirecionalidade.
- Opção avançada: segurar a tecla option e arrastar um lado do ponto-guia ao longo do caminho sem afetar o ponto associado, para ajustar posicionamento padrão que não seja o ideal.

Exemplos citados:
- line.diagonal: primeiro exemplo simples de anotação com dois pontos-guia.
- scribble (variable): tem largura variável, então não pode simplesmente ter o traço "stroked" para construir as animações; precisa de mais pontos-guia nas curvas fechadas.
- line.3.horizontal: exemplo de múltiplos caminhos no mesmo símbolo, cada linha com sua própria direção de desenho; arrastar o ponto inicial sobre outro ponto-guia inverte a direção da seta.
- wave.3.up: exemplo de desenho bidirecional a partir do centro.
- Thermometer: exemplo de variable draw ativado em apenas uma camada (o "meter"), para que só essa parte transmita progresso.

Citações curtas:
"Every curve and angle must feel deliberate, balanced, and visually communicative."
"There is no one correct way to place guide points."

<!-- visual:wwdc2025_337 -->
### O que as imagens mostram
Base: 16 de 16 folhas de quadros vistas, todos os códigos conferidos.
- A tela constrói um glossário visual de notação com convenção fixa: ponto vazado marca o início do traço, ponto preenchido marca o fim, pontos menores intermediários marcam guias ao longo de curvas, e setinhas ao lado indicam o sentido de desenho (folha 0007, q0058 a q0060). Um quadro de resumo reúne seis exemplos em grade dois por três, cada um com sua legenda funcional: linha diagonal, rabisco, três linhas horizontais, seta circular, "Same Start & End point" e "Corner points" (q0061).
- Uma prancha técnica azul antecipa, bem antes da explicação falada, o vocabulário inteiro de anotação sobre o símbolo "scribble.variable": rótulos "Guide Points", "Start/Corner/End", "Attachment/Follow Path", uma cota "Variable Width a != b" apontando duas larguras diferentes do mesmo traço, e miniaturas de dois pesos no rodapé (folha 0002, q0016).
- A anatomia do app aparece sempre no mesmo arranjo de três colunas, barra lateral de categorias, canvas central com o símbolo e inspetor à direita, repetido do catálogo padrão para o modo Custom Symbols, que acrescenta um painel de camadas abaixo do inspetor de animação (folha 0004, q0028 a q0030; folha 0007, q0063; folha 0008, q0064). O inspetor empilha campos com rótulo à esquerda e controle à direita: menus de Animation e Repeat, botões segmentados "Whole Symbol / By Layer" e campo Direction.
- A diferença entre dois quadros revela uma regra de estado da interface: o campo "Reverse" com chave só aparece quando a animação selecionada muda de "Draw On" para "Draw Off" (folha 0004, q0029 para q0030).
- A anotação é mostrada acontecendo passo a passo no canvas, com o símbolo em cinza translúcido e os pontos sobrepostos em azul escuro: a linha diagonal ganha primeiro um ponto vazado e depois o ponto fechado com a seta de direção, e a miniatura na lista de camadas se atualiza junto, funcionando como indicador de progresso (folha 0008, q0064 a q0066).
- Um par de quadros torna concreta a densidade de pontos que uma curva fechada exige: o mesmo traço em S aparece com poucos guias e curvas ainda soltas e depois com guias extras preenchendo exatamente as dobras apertadas (folha 0008, q0069 para q0070).
- O painel de camadas lista cada subcaminho como uma linha própria rotulada "Fill", e o destaque azul migra de linha para linha enquanto cada uma das três horizontais recebe seus guias, com a do meio exibindo seta em sentido diferente das outras duas (folha 0009, q0073 a q0076). Nas ondas concêntricas os pontos se concentram na base central com setas saindo para os dois lados, e um deles aparece selecionado com alça quadrada de arrasto (q0078 a q0081).
- Menus de contexto ancorados a um ponto específico expõem as escolhas disponíveis em texto: "Default Endcap" e "Adaptive Endcap" sobre o quadrado arredondado (folha 0010, q0085), e "Automatic / Guide Point / Corner Point / End Point" sobre o traço de eletrocardiograma (folha 0012, q0106 e q0108).
- Um ponto que marca início e fim ao mesmo tempo tem forma própria na tela: no topo do círculo o marcador aparece como cápsula alongada, distinta dos pontos redondos de início e fim vistos nos demais símbolos (folha 0010, q0089 e q0090).
- Um código de cor separa o que anima do que não anima: azul para "Drawing components" e verde para "Non-drawing components", aplicado ao marcador de "list.bullet" e à cabeça da seta em "arrow.trianglehead.clockwise"; o marcador passa de contorno cinza a preenchido de verde entre dois quadros (folha 0011, q0093 para q0094). A ancoragem da cabeça de seta a um ponto é mostrada como forma translúcida ligada por uma linha fina ao ponto (q0095 a q0097), e dois diagramas finais rotulam as partes como "Path A" e "Path B" para justificar a separação (q0098 e q0099).
- Faixas de cor sobrepostas ao símbolo "arrow.trianglehead.pull" segmentam visualmente o que pertence a cada subcaminho, uma faixa verde "Path A" na base reta, um rótulo "Path B" na ponta curva e uma faixa azul "Path A & B" na extensão comum, com o item "Subpath 1" selecionado no painel de camadas do app (folha 0012, q0102 e q0103).
- A legenda lateral do eletrocardiograma cresce entre quadros de três tipos de ponto para quatro, e o item novo, "Corner point", ganha marcador em losango em vez do círculo usado pelos demais (folha 0012, q0107 para q0108). Diagramas complementares mostram o ponto de canto como par "Side A" e "Side B" no mesmo lado do traço (folha 0013, q0109 e q0110).
- A grade de pesos é a ferramenta de verificação mostrada na tela: colunas nomeadas de Ultralight a Black com a coluna Regular em negrito como base, primeiro com três desenhos esmaecidos, depois nítidos e com barra de escala, depois com pontos-guia sobrepostos e, por fim, expandida para as nove colunas preenchidas (folha 0013, q0113 a q0116).
- A mesma grade ganha marcação de diagnóstico: números pequenos junto a cada ponto-guia, um leque angular vermelho entre dois pontos na coluna Black e, no quadro seguinte, linhas laranja ligando pontos específicos (folha 0013, q0117; folha 0014, q0118 a q0120).
- A interface usa realce por escurecimento para ensinar onde clicar: todo o painel fica esmaecido menos um botão, com linha e rótulo "Enable Variable Draw" apontando para ele, e o alvo muda de uma camada do termômetro para a outra entre dois quadros (folha 0014, q0124 para q0125).
- Os gradientes aparecem primeiro como sistema aplicado, seis ícones com o mesmo sombreado direcional, e depois dentro de uma moldura de iPhone numa tela de Face ID, com os ícones de exemplo ao lado para comparar escala (folha 0006, q0049 e q0050). No app, a chave "Gradients" aparece ligada tanto com Rendering Mode em "Multicolor" quanto em "Monochrome" (q0051 para q0052).
- Os blocos de código comparam a mesma função nas três formas de escrever, com comentários de cabeçalho por framework, e um realce azul claro que avança de trecho em trecho conforme a API citada muda, de drawOff para individually, depois variableValueMode e colorRenderingMode (folha 0015, q0128 a q0132).
Proporção visual: a maior parte dos quadros é diagrama técnico, tela do app SF Symbols, cartela de símbolos ou código; a apresentadora aparece em cortes curtos intercalados em quase todas as folhas, às vezes com a lista de tópicos sobreposta, e ocupa os quadros finais do encerramento (folha 0016, q0139 e q0140).
Divergências ou limites registrados: as notas marcam um par de quadros sem mudança visível apesar da expectativa (folha 0006, q0053 para q0054), identificam o símbolo de ondas concêntricas com ressalva ("wave.3.up ou similar", folha 0009), tratam o arco-íris e a lista com seta como prováveis exemplos genéricos e não como os exemplos citados na fala (folha 0003, q0025 e q0026), e registram que os três últimos quadros da grade final ficaram pretos porque o vídeo termina antes de completar a folha (folha 0016). As notas também se contradizem sobre o quadro q0105 da folha 0012, descrito ora como a seta "arrow.trianglehead.pull", ora como o eletrocardiograma, então ele não é citado como prova de nenhum dos dois.
<!-- /visual:wwdc2025_337 -->

## Optimize your custom environments for visionOS (id: wwdc2025_305, 32.8 min)

- Base: transcrição e 28 de 28 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/305/.
- Tese central: é possível levar ambientes imersivos de qualidade cinematográfica (renderizados previamente, com mais de 100 milhões de polígonos) para performance em tempo real no Vision Pro usando um fluxo procedural em Houdini que explora especificamente os limites do "Immersive Boundary" (a área que a pessoa pode fisicamente percorrer).

Este vídeo é primariamente técnico (pipeline 3D/gráfico), não um vídeo de design de interface de usuário tradicional, mas trata de decisões que afetam diretamente a experiência espacial percebida pela pessoa.

O processo de design/otimização que a Apple descreve:
1. Imagem pré-renderizada, capturando iluminação cinematográfica, detalhe rico e materiais de alto padrão.
2. Geometria e texturas otimizadas com base no que o espectador realmente experimenta (usando o Immersive Boundary como referência).
3. A imagem pré-renderizada é transferida (baked) para o ambiente otimizado.
4. Tudo é montado num editor em tempo real, como Reality Composer ou Unity.

Princípios enunciados e o porquê:
- Entender exatamente onde a pessoa pode se mover e olhar (o Immersive Boundary) permite não renderizar tudo em qualidade máxima, só as partes que importam; essa é a chave da otimização.
- Em imersão total, cada pixel é renderizado (ao contrário da imersão mista, onde só parte da tela é renderizada sobre o passthrough), tornando a performance mais desafiadora.

Técnicas concretas descritas (com números exatos quando falados):
- Redução adaptativa de polígonos: baseada em múltiplos pontos de vista amostrados ao longo do Immersive Boundary, preservando detalhe nas silhuetas e reduzindo onde não é preciso.
- Billboards para objetos distantes: a partir de 1 km (Boundary Camera indica que pistas de profundidade e paralaxe começam a achatar entre 1 e 3 km), converte-se geometria 3D complexa em geometria plana orientada ao Boundary, preservando a silhueta original vértice por vértice (sem usar transparência).
- Culling: Backface Removal (remove polígonos voltados para longe do Boundary; no caso da lua, quase 60.000 triângulos removidos) e Occlusion Culling (ray casting de milhões de pontos; 110.000 triângulos removidos no exemplo); juntas, removem cerca de 50% dos triângulos restantes.
- Resultado no case da Lua: de mais de 100 milhões de triângulos para 350.000 após redução adaptativa e billboards; depois do culling, 180.000 triângulos; no final, menos de 200.000 triângulos totais, com menos de 100.000 visíveis em tela a qualquer momento graças ao Frustum Culling.
- UVs: dentro dos primeiros 5 metros do Boundary, usa-se mapeamento de UV baseado em área de superfície (para manter densidade de texel consistente de qualquer ângulo); fora do Boundary, usa-se mapeamento baseado em projeção/screen space (projeção esférica), porque a superfície só é vista de ângulos e distâncias limitadas.
- Problema identificado na projeção esférica única: sobreposição de UV, escalonamento incorreto de texel ao se mover, e uma única captura panorâmica não conseguir ver tudo; solução: projetar UVs de múltiplos ângulos (Mesh Partition HDA divide a malha em ilhas mínimas; Multi-Projection HDA projeta cada partição do ponto onde ela aparece maior em screen space).
- Texturas finais: todo o ambiente cabe em duas texturas (uma para dentro do Boundary, escalada por área de superfície; outra para o resto, escalada por screen space); a lua inteira foi comprimida para menos de 250 megabytes de memória de textura, partindo de dezenas de gigabytes de mapas PBR de alta fidelidade.
- Frustum Culling via hierarquia USD: dentro do Boundary usa-se Boundary Partition HDA; fora, Frustum Partition HDA, dividindo a malha em blocos progressivamente maiores.
- Números finais do case: menos de 200 entidades totais, tipicamente menos de 100 draw calls por frame.

Exemplos citados:
- Ambiente da Lua: case de estudo principal, ilustrando cada etapa do pipeline.
- Joshua Tree, Mount Hood, Haleakala: outros ambientes citados como exemplos de tipos de cena (rochoso, atmosférico).
- Sala de conferência/teatro (interior de superfície dura): exemplo de ambiente que não precisa de otimização pesada porque já é modelado à mão de forma eficiente.

Citações curtas:
"High-fidelity content doesn't have to be expensive."
"You don't have to reduce the complexity, you just need the right system to take control of it."

<!-- visual:wwdc2025_305 -->
### O que as imagens mostram
Base: 28 de 28 folhas de quadros vistas, todos os códigos conferidos.

- O roteiro da apresentação é visível na tela por hierarquia de opacidade, não só pela fala: o slide de tópicos mostra o item corrente em preto e negrito, o já tratado em cinza claro e os futuros em cinza mais claro ainda, e a passagem acontece quadro a quadro (folha 0004, q0028 com "Optimize geometry" em negrito e q0029 acrescentando "UV projection" enquanto o anterior recua para cinza; o mesmo padrão reaparece nas folhas 0007, 0011, 0013, 0015, 0021 e 0022).
- O mesmo desenho de diagrama de fluxo volta a cada técnica nova: caixa de origem vermelha ligada por seta a uma caixa laranja de resultado nas duas primeiras (folha 0009, q0076, "Source content" para "Adaptive reduce"; folha 0012, q0106, o mesmo par para "Vista billboard"), e encadeamento de várias caixas quando o assunto é a sequência inteira (folha 0014, q0118, quatro caixas laranja até "Occlusion culling"; folha 0019, q0171, fluxograma vertical com caixa de entrada laranja e etapas roxas).
- O certo e o errado são marcados com selo gráfico sobre a imagem, e as notas registram o quadro exato em que o selo entra: na folha 0008, q0066 mostra os dois wireframes comparados sem marcação e q0067 traz a mesma comparação já com "X" vermelho de um lado e check verde do outro, sobre imagens de malha diferentes; na folha 0022, q0191 acrescenta a foto de "Surface projection" sob a de "Spherical projection" e só q0192 sobrepõe o círculo vermelho com X na primeira e o círculo verde com check na segunda.
- O mesmo conteúdo aparece sucessivamente em estilos diferentes de visualização, com o símbolo de escala fixo atravessando todos eles: cilindro verde translúcido, disco ou anel vermelho no chão e figura humana estilizada, amarela nas primeiras folhas e laranja nas seguintes, aparecem sobre diagrama abstrato (folha 0004, q0036), viewport de cima (folha 0007, q0058), wireframe com overlay vermelho e azul (folha 0025, q0217), textura cinza realista (q0218), grade de teste xadrez (q0221) e fotografia final (q0222).
- A construção do diagrama se dá por adição controlada de elementos, não por corte para a versão pronta: na folha 0002 o "Optimization workflow" aparece primeiro só com o título (q0011), depois com dois cartões (q0012), depois com os quatro coloridos (q0013) e num quadro seguinte os mesmos quatro esmaecidos em cinza (q0014); na folha 0026 o slide "Memory" ganha duas linhas de texto entre q0228 e q0229 mantendo a mesma imagem.
- Medidas e números exatos ficam escritos sobre a própria cena 3D ou como legenda discreta ao lado da imagem: "1.5m radius of traversable space" (folha 0004, q0036), rótulo "1km" sobre o terreno (folha 0007, q0060), resolução "14,400 x 7200" no render panorâmico (folha 0017, q0146), "2.5m" e "1km" separando os dois grupos de mosaico (folha 0021, q0181), e "Position 1" e "Position 2" com linhas de chamada finas apontando para pontos da cratera (folha 0027, q0236 e q0237).
- Números de resultado recebem tratamento de texto de destaque isolado, sem gráfico e sem moldura, entre blocos de demonstração técnica: frase sobre custo do render em fundo cinza claro (folha 0001, q0008), "Over 100 million polygons!" (folha 0005) e "350,000 polygons." (folha 0013). O contraste entre origem e resultado já vem em outro formato, um par de imagens da mesma formação rochosa legendadas "100,000,000 source" e "180,000 optimized" (folha 0015, q0129).
- Existe um template rígido de slide de métrica na conclusão, repetido três vezes quase sem variação: título curto, duas ou três linhas de texto sempre com "<" ou "~" antes do número, e uma imagem de prova à direita ocupando cerca de 45% da largura (folha 0026, "Geometry" em q0226 e q0227, "Memory" em q0228 e q0229, "Draw calls" em q0230 e q0231).
- A ferramenta de produção aparece como interface real, com nomes de nó e campos editáveis legíveis, e não como esquema: layout de três painéis com viewport, rede de nós e painel "Adaptive Reduce" contendo Prims To Keep, Sample Points, o bloco "Weights" e uma curva "Distance Ramp" com alça de controle (folha 0010, q0083 em diante), além de nomes reais como adaptive_reduce1, boundary_sample1, filecache_rocks_high e occlusion_culling1 (folhas 0009, 0010 e 0014).
- A troca de paleta do heatmap marca qual otimização está em cena, sem depender do texto: laranja e vermelho no ajuste inicial de pesos e azul e vermelho depois da mudança de parâmetros no mesmo monte (folha 0010, q0083 contra q0086), pontos amarelos de densidade sobre terreno cinza nas primeiras capturas do Houdini (folha 0006, q0049 e q0050) e tons de roxo, azul e ciano na etapa de culling (folhas 0013 e 0014).
- Uma grade quadriculada preto e branco com letras e números nos quadrados é usada como instrumento de diagnóstico de UV, reaparecendo em três momentos distantes entre si (folha 0018, q0156, com boneco central e setas verdes de "Projection position"; folha 0020, q0176, com as projeções sobrepostas; folha 0025, q0221, aplicada de volta à cena do limite imersivo).
- A cor carrega julgamento, não só distinção: verde para dentro do limite imersivo e vermelho ou rosa para fora dele ou para área problemática, visto no diagrama de zonas (folha 0016, q0137 e q0138), nas manchas rosa que marcam sobreposição de UV (folha 0017, q0153; folha 0018, q0154 e q0155, com as manchas ficando mais tênues entre um quadro e outro) e nos selos de erro e acerto da folha 0022.
- O resultado do pipeline aparece como estrutura de dados na tela, não só como render: planilha escura de atributos ao lado de uma árvore de hierarquia USD com ícones por tipo de primitiva, texto "name > USD prim name, groups > USD GeomSubset", campos em fonte monoespaçada com "name: immersive_boundary" e lista de "group:partition_N", terminando no nome de arquivo exportado visível na tela (folha 0024, q0209 a q0216).
- O fechamento constrói uma grade de exemplos por revelação gradual, de uma miniatura para pares e daí para 3x3 completa de nove ambientes com legendas, depois destaca uma delas com borda preta grossa antes da transição (folha 0027, q0238 a q0243; folha 0028, q0244), e o slide final troca de registro visual, usando fotografia de still-life de mesa de madeira com objetos decorativos em vez de captura de tela, com rodapé de crédito de outra sessão separado por linha fina (folha 0028, q0246 e q0247).

Proporção visual: pelas notas, a grande maioria dos quadros é slide, render, diagrama ou captura real de software, com o apresentador aparecendo em quadros de corte isolados entre blocos, e só no encerramento em sequência mais longa (folha 0028, q0248 a q0252); a tela troca de cenografia do apresentador na segunda metade, do fundo laranja e branco para uma sala de reunião com Mac Studio a partir da folha 0022, q0196.

Divergências ou limites registrados: várias folhas registram transições incompletas com títulos sobrepostos ou texto fantasma legível por baixo (folha 0016, q0136; folha 0017, q0145; folha 0022, q0194, com "High-end visuals. Minimal footprint."; folha 0026, q0232, com "Build robust tools." residual); algumas legendas aparecem cortadas na borda da folha e ficaram incompletas nas notas ("Geometry..." em q0101, "UV a..." em q0135, "Frustum Partiti[on]" em q0207); e as notas marcam como interpretação provável, e não como leitura confirmada, o overlay azul da folha 0015 e o significado do heatmap vermelho e azul da folha 0025, além de anotarem dúvida sobre quadro duplicado em q0209.
<!-- /visual:wwdc2025_305 -->

## Make a big impact with small writing changes (id: wwdc2025_404, 16.0 min)

- Base: transcrição e 11 de 11 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/404/.
- Tese central: quatro pequenas mudanças de escrita (remover palavras de preenchimento, evitar repetição, liderar com o "porquê", e criar uma lista de palavras) têm impacto desproporcionalmente grande na clareza da UX writing de um app.

O processo de design que a Apple descreve:
- Ler a escrita em voz alta para identificar palavras de preenchimento e repetições, e saber onde apertar o texto.
- Fazer uma pausa a cada advérbio/adjetivo descritivo encontrado e perguntar: "essa palavra agrega valor?"
- Criar uma lista de palavras (word list) desde o início do desenvolvimento (mas pode ser feita a qualquer momento), documentando: termo escolhido, termos evitados para a mesma coisa, e uma definição simples.

Princípios enunciados e o porquê:
- Não existe cota mínima de palavras: ao contrário de uma redação escolar, o app não precisa preencher todo espaço vazio; geralmente o oposto é verdade, é melhor remover palavras.
- Advérbios e adjetivos ("simply", "quickly", "fast", "simple") costumam ser fillers; quando aparecem, vale pausar para checar se são necessários. Mas descrição pode ser útil quando esclarece comportamento (ex.: "automatically" explica que o app alimenta os pets segundo um cronograma, não só manualmente).
- Interjeições ("uh oh", "oops") e cortesias ("sorry", "please", "thank you") podem parecer que humanizam o app, mas quando não agregam significado devem ser removidas; em mensagens de erro, interjeições podem soar como se o problema não estivesse sendo levado a sério, e desculpas podem soar insinceras num alerta.
- Pontuação desnecessária (como ponto de exclamação) pode funcionar como filler e minimizar a gravidade de uma situação para quem está esperando algo importante.
- Repetição de linguagem é outra forma de filler: dizer a mesma coisa de formas diferentes deve ser evitado; a economia de linguagem é central à UX writing.
- Liderar com o "porquê": mensagens são mais eficazes quando dizem por que o próximo passo é útil, interessante ou benéfico, antes de dar a instrução. Formato mental: "para fazer/obter uma coisa, primeiro faça outra".
- Consistência via lista de palavras ajuda qualquer pessoa que trabalhe no app a saber como ele deve soar; rótulos de botão são um bom item para constar na lista.

Técnicas concretas de construção de interface (exemplos de reescrita):
- "Simply enter your license plate number to quickly pay for parking." → "Enter your license plate number to pay for parking." (remoção de "simply" e "quickly", sem perda de clareza).
- Notificação de entrega: de "Uh oh. We're running late" + "We're sorry, your delivery driver won't make it on time. They'll be there in 10 short minutes! Check the app for your driver's location." para, após remover fillers, "We're running late. Your delivery driver won't make it on time. They'll be there in 10 minutes. Check the app for your driver's location."; depois, combinando ideias repetidas, o headline vira "Delivery delayed 10 minutes." e o corpo mantém só "Check the app for your driver's location."
- "Enter your phone number to get reservation updates." → "To get reservation updates, enter your phone number." (mover o benefício para o início da frase).
- Exemplo de app de jogo: escolher "alias" como termo oficial para nome dentro do jogo, evitando "Handle", "User Name", "Title"; e "health" evitando "lives", "hearts", "energy", "stamina", cada um com definição simples registrada na lista.

Exemplos citados:
- App de estacionamento em garagem (experiência pessoal da autora, de viagem): ilustra como um filler ("simply", "quickly") pode soar irônico quando a experiência real não é simples nem rápida.
- App fictício de dispensador de comida para pets: ilustra quando manter uma palavra descritiva ("automatically") é necessário para clareza de comportamento.
- Apple News+ Puzzles: notificação "Keep your streak going by solving today's crossword" como exemplo eficaz de liderar com o porquê.
- Tela de configuração do teste auditivo dos AirPods Pro: usado como exemplo final que aplica as quatro técnicas juntas (sem fillers no headline "Test Your Hearing", parágrafos que lideram com o porquê, botão "Next" consistente em todas as telas, sem repetição entre headline e descrição).

Citações curtas:
"Fortunately, your app doesn't have a minimum word count."
"Read your writing out loud."

<!-- visual:wwdc2025_404 -->
### O que as imagens mostram
Base: 11 de 11 folhas de quadros vistas, todos os códigos conferidos.

- A lista dos quatro tópicos é montada na tela item por item, em coluna alinhada à esquerda ao lado da apresentadora, com o item corrente em negrito preto e os já citados em cinza claro, hierarquia feita por peso e cor e não por tamanho (folha 0001, q0006 a q0008, com o texto sumindo por completo em q0009); a mesma lista volta a cada virada de tópico (folhas 0004, 0005, 0006 e 0007) e reaparece no fechamento como lista de princípios acumulada ao lado das telas (folhas 0009 e 0010).
- A edição do texto acontece diante do espectador, com marcação editorial visível: a tela do app de estacionamento aparece vazia, só com o rótulo do app, ganha o cartão com a frase completa e num quadro seguinte a palavra "Simply" aparece tachada dentro da própria frase (folha 0002, q0016 para q0017 para q0018).
- Antes de cortar, a tela destaca em negrito um trecho por vez para dirigir a atenção, e só depois remove: no cartão de notificação de entrega o negrito passa de "Uh oh." para "We're sorry," e daí para "10 short minutes!", e apenas nos quadros seguintes o título perde a interjeição e o corpo perde o pedido de desculpas e o ponto de exclamação (folha 0004, q0029 a q0035).
- A cor azul marca o que foi acrescentado ou reordenado, contra o preto do restante do texto: a palavra "Automatically" entra em azul no início da frase sobre alimentar os bichos (folha 0003, q0022 para q0023) e o trecho de benefício aparece em azul quando é movido para o começo da frase do app de reservas (folha 0006, q0051 para q0052).
- O cartão de notificação tem anatomia fixa, reaproveitada nas folhas 0004, 0005 e 0008: ícone quadrado de cantos arredondados à esquerda, título em negrito, corpo em texto normal, etiqueta "now" no canto superior direito, cantos arredondados e sombra sutil. O cartão de formulário segue outra anatomia, com rótulo do app acima à esquerda, cartão branco arredondado com sombra leve, texto de instrução, campo com placeholder e botão preto cheio "Next" (folha 0002), e volta com campo e botão no exemplo do jogo (folha 0008, q0067).
- A reescrita final aparece como fusão de duas frases numa só, e o julgamento vem por selo: o corpo do cartão primeiro destaca em negrito o trecho a ser fundido enquanto o resto fica em cinza claro, depois o título vira a frase curta com o número, e por fim os dois cartões aparecem empilhados, o antigo com círculo vermelho de X e o novo com círculo verde de check (folha 0005, q0037 a q0040). Esse par de certo e errado aparece uma única vez no vídeo.
- Há dois níveis de fidelidade de moldura de aparelho: o contorno de smartphone simples, só a silhueta arredondada, sem barra de status nem chrome, aparece no exemplo conceitual do app de reservas (folha 0006, q0050), enquanto os outros exemplos conceituais de texto ficam em cartões sem moldura nenhuma (folhas 0002 e 0003); a moldura real de iPhone, com notch, barra de status com hora, sinal, wifi e bateria, barra de progresso em pontos no topo e botão azul arredondado no rodapé, fica reservada ao exemplo de produto real no fim (folha 0009, q0075).
- As listas de exemplos de vocabulário aparecem em coluna única, alinhadas à esquerda e com espaçamento generoso: quatro palavras no cartão de advérbios e adjetivos (folha 0002, q0014 e q0015) e a lista de interjeições e cortesias passando de três para seis itens entre um quadro e o seguinte, dentro do mesmo slide (folha 0003, q0025 para q0026).
- A tabela de vocabulário é construída célula a célula na frente do espectador, simulando o ato de montar o documento: primeiro só os cabeçalhos de três colunas, depois o termo aceito, depois os termos evitados, depois a definição, e então a linha seguinte começa vazia (folha 0007, q0057 a q0063); o formato é sem bordas verticais, cabeçalho pequeno em cinza e linhas separadas por traço fino horizontal.
- A consistência terminológica é demonstrada percorrendo três componentes de natureza diferente com o mesmo termo, e o vídeo os mostra primeiro isolados e depois lado a lado com a palavra em negrito nos três: cartão de formulário, campo de busca com ícone de lupa e cartão de notificação de partida (folha 0008, q0067, q0068, q0070 e q0071), com a tabela de referência ganhando uma quarta linha no meio desse percurso (q0069).
- O exemplo final usa capturas reais de um fluxo de onboarding e vai acumulando os princípios ao lado das telas: dois iPhones lado a lado com a tela de ajuste e a tela de ambiente silencioso, ilustração de orelha em escala de cinza para instrução física e indicador textual com ponto verde para o nível de ruído, enquanto a lista lateral ganha os itens um a um até completar os quatro (folha 0009, q0077 a q0081; folha 0010, q0084 e q0085).
- O encerramento troca de registro visual: a tela esvazia para cinza, aparece o título de referências sobre uma fotografia still de mesa de madeira com coleira e brinquedo de cachorro, e a lista de palestras citadas usa exatamente o mesmo padrão de tabela sem bordas verticais da lista de vocabulário (folha 0010, q0089 e q0090; folha 0011, q0091).
- Um filtro de cor sobre a cena das duas apresentadoras à mesa marca só a abertura e o fechamento: overlay roxo e rosa que se dissolve no começo (folha 0001, q0002 para q0003) e overlay azulado aplicado no último quadro (folha 0011, q0092 para q0093).
- Um detalhe registrado nas notas mostra a lista de agenda adiantando o roteiro: no quadro em que "Lead with the why" está em negrito como item atual, "Make a word list" já aparece também em negrito abaixo dos itens cinza, antes de ter sido citado (folha 0001, q0008).

Proporção visual: pelas notas, quase todo quadro com conteúdo traz componente de interface, cartão de texto, lista ou tabela, muitas vezes no mesmo quadro que a apresentadora; quadros só da apresentadora, ou das duas à mesa, entram como cortes curtos entre os exemplos e nas viradas de tópico, e em sequência mais longa na abertura e no encerramento (folhas 0001, 0010 e 0011).

Divergências ou limites registrados: as notas se contradizem em dois pontos, e aqui vale o que a folha descreve quadro a quadro. Na folha 0005 o registro de quadros diz que o cartão antigo com X vermelho entra abaixo do novo, enquanto o resumo das notas põe o antigo em cima, por isso só o empilhamento é afirmado, não a ordem. Nas folhas 0002 e 0003 o resumo fala em contorno de smartphone, mas as folhas descrevem cartões sem moldura de aparelho, e a folha 0003 diz isso de forma explícita. O botão do exemplo final é registrado como "Get Started" na folha 0009 e como "Next" no resumo das notas.
<!-- /visual:wwdc2025_404 -->

## Explore video experiences for visionOS (id: wwdc2025_304, 25.9 min)

- Base: transcrição e 22 de 22 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/304/.
- Tese central: o Vision Pro, como computador espacial, permite que vídeo seja apresentado em muito mais formas do que uma tela plana tradicional, do 2D/3D embutido até formatos totalmente imersivos como Apple Immersive Video, e o visionOS 26 expande esse leque com novos perfis de projeção não-retilínea.

Este é um vídeo primariamente técnico/de engenharia sobre formatos de mídia, não de metodologia de design de interface, mas descreve decisões de apresentação que afetam diretamente a experiência do espectador.

O processo/framework que a Apple descreve (perfis de vídeo e onde cada um se encaixa):
- 2D e 3D (projeção retilínea): linhas retas permanecem retas, sem curvatura de lente; por isso parecem corretas numa superfície plana. Pode ser embutido (inline) na UI, expandido numa tela flutuante no espaço compartilhado, ou ancorado (docked) num ambiente virtual customizado.
- Spatial Video: vídeo estéreo com metadados adicionais, captável por pessoas comuns (iPhone), não só produtores profissionais; por padrão aparece numa janela com leve brilho nas bordas; pode expandir para apresentação imersiva em escala real, onde a borda do quadro desaparece.
- 180°, 360° e wide FOV: novos no visionOS 26, projetados sobre superfícies curvas (meia esfera, esfera completa, ou malha curva que recria o perfil da lente de uma câmera de ação).
- Apple Immersive Video: a experiência mais imersiva, com vídeo estéreo de altíssima resolução, calibrado para a lente exata que capturou.

Princípios enunciados e o porquê:
- Vídeos retilíneos parecem corretos numa tela plana porque não têm curvatura; vídeos não-retilíneos (180°/360°/wide FOV) precisam de superfície curva justamente para não distorcer.
- Reprodução imersiva é sensível a movimento de câmera, porque coloca a cabeça do espectador exatamente onde a câmera estava na captura; por isso o sistema inclui detecção automática de alto movimento (em QuickLook, AVKit e RealityKit), que reduz a imersão automaticamente em cenas de muito movimento, com opção de ajuste na sensibilidade em Configurações.
- MV-HEVC (MultiView HEVC) é usado para vídeo estéreo porque a imagem do olho esquerdo e do direito são muito parecidas; comprimir apenas as diferenças entre os dois olhos economiza tamanho de arquivo, especialmente importante em streaming.

Técnicas concretas de construção de interface, com números exatos quando falados:
- Vídeo 360°: mapeado numa esfera via projeção equirretangular; o quadro retangular usado tem o dobro da largura em relação à altura, cobrindo 360° na largura e 180° na altura.
- Vídeo 180°: projeção meia-equirretangular, quadro quadrado.
- Wide FOV: câmeras de ação como GoPro HERO13 e Insta360 Ace Pro 2 capturam campo de visão horizontal tipicamente entre 120° e 180°; usa "projeção imersiva paramétrica", definida por parâmetros de distância focal, skew e distorção da lente.
- Apple Immersive Video (câmera URSA Cine Immersive, Blackmagic): captura estéreo com 8160 x 7200 pixels por olho, ou seja, 59 megapixels por olho, a 90 quadros por segundo, totalizando mais de 10 bilhões de pixels por segundo; campo de visão de até 210° horizontalmente e 180° verticalmente.
- Pipeline de criação de Apple Immersive Video: 1) captura na URSA Cine Immersive; 2) edição no DaVinci Resolve Studio; 3) pré-visualização e validação nos apps Apple Immersive Video Utility (macOS e visionOS); 4) segmentação no Compressor para distribuição via HLS (HTTP Live Streaming).
- Per-shot edge blends: cada plano de um Apple Immersive Video pode definir uma curva de mistura de borda customizada (blend curve dinâmica de alpha, não uma máscara fixa), que funde a borda do plano com um ambiente de fundo customizado.
- Novo formato de arquivo APMP (Apple Projected Media Profile): perfil QuickTime que suporta nativamente 180°, 360° e wide FOV no visionOS 26; suportado para reprodução expandida e imersiva, mas não para reprodução embutida inline.
- Conversão automática para APMP: vídeos estéreo 180° do sistema Canon EOS VR, vídeos 360° de GoPro MAX e Insta360 X5, vídeos equirretangulares em formato Google Spherical Video v1/v2, e vídeos brutos de câmeras de ação como GoPro HERO13 e Insta360 Ace Pro 2.
- Spatial video pode ser capturado no iPhone 15 Pro, iPhone 16 e iPhone 16 Pro (Camera app ou APIs AVCaptureDevice), no próprio Vision Pro, e com as câmeras Canon R7 e R50 com lente dual Canon.

Exemplos citados:
- Destination Video (sample code project): mostra vídeo transicionando de tela expandida para ancorado (docked) num ambiente de estúdio customizado feito com Reality Composer Pro, com "dynamic light spill" para parecer parte integral do ambiente.
- Apple TV+ "Wild Life" (elefantes no Sheldrick Wildlife Trust, Quênia): exemplo de Apple Immersive Video, descrito como transportando o espectador a uma cena quase impossível de vivenciar na realidade.
- Freeform: exemplo de reprodução inline de vídeo 2D dentro de um board com outros conteúdos.
- Apple Park (pond e "rainbow"): exemplos de captura 180° e 360°.

Citações curtas:
"They're not just limited to a flat screen in front of the viewer."
"It's like being there."

<!-- visual:wwdc2025_304 -->
### O que as imagens mostram
Base: 22 de 22 folhas de quadros vistas, todos os códigos conferidos.
- A orientação do espectador é feita por uma trilha de agenda vertical no canto inferior esquerdo, sobre a própria filmagem do apresentador, sem caixa nem borda: o item atual em preto e negrito, os já citados em cinza claro, crescendo um item por vez (folha 0001, q0007 a q0009; reaparece nas folhas 0002 q0010, 0004 q0028 a q0030, 0008 q0072, 0017 q0152 e 0020 q0176).
- Existe um vocabulário de diagrama repetido ao longo do vídeo: silhueta humana branca de contorno fino sobre piso de grade em perspectiva e, à frente dela, a superfície que recebe o vídeo. Só a forma muda conforme o formato explicado, esfera cheia, disco ou meia esfera, faixa curva, retângulo com grade azul (folhas 0003 q0026, 0006 q0050, 0009 q0073 a q0078, 0013 q0111 e q0112, 0018 q0162, 0020 q0174). O fundo não é sempre o mesmo: preto nas folhas 0009 e 0013, cinza claro nos diagramas da folha 0006.
- As medidas são desenhadas como cotas de desenho técnico em cima do próprio diagrama: linha lateral "180°" e linha de base "360°" no quadro equirretangular (folha 0010, q0085 para q0086), cotas em pixel no topo e na lateral do quadro lado a lado (folha 0011, q0092), e legenda de campo de visão "170°" centralizada abaixo da fotografia real (folha 0012, q0107 e q0108).
- A anatomia dos slides descritivos é estável: título em preto forte e subtítulo em cinza no canto superior esquerdo, itens de lista um por linha e nomes de API em fonte monoespaçada dentro de um chip cinza azulado, por exemplo AVCaptureDevice e PreviewApplication (folhas 0006 q0052 a q0054, 0007 q0055, 0016 q0137). O marcador da lista varia conforme a folha: traço simples na folha 0006, nenhum marcador nas folhas 0007, 0016 e 0018. Novidade é marcada por um selo verde arredondado junto ao título (folhas 0003 q0026, 0006 q0054, 0007 q0063, 0015 q0127).
- Referência a outra sessão vira um rodapé padronizado: linha fina separadora, nome da sessão à esquerda em cinza pequeno e o ano do evento à direita, aparecendo como camada adicional entre um quadro e o seguinte (folha 0007, q0058 para q0059 e q0062 para q0063; folha 0017, q0150 para q0151).
- Quase todo slide de texto ou diagrama é construído em camadas ao longo de vários quadros em vez de aparecer pronto. A lista de especificações da câmera cresce a cada quadro em ritmo irregular, um item em q0157, mais dois em q0158 e mais um em q0159 (folha 0018), o diagrama de pipeline ganha as caixas Capture e Edit e só depois Preview e Segment, ligadas por setas pontilhadas (folha 0019, q0165 a q0167), e o slide de conversão automática ganha um grupo de ícones por vez (folha 0015, q0130 a q0134).
- Os formatos não retilíneos têm codificação fixa por forma e cor, repetida sempre que reaparecem: cúpula azul, forma laranja redonda e cunha verde (folhas 0008 q0071, 0014 q0125 e q0126, 0015 q0131 a q0134, 0020 q0179). Os retilíneos só ganham ícone próprio no recapitulativo, como retângulos verticais achatados em cinza, vermelho e azul escuro, ao lado de um sétimo ícone dourado para o formato imersivo da Apple (folha 0020, q0178 a q0180).
- Conceito técnico isolado ganha um cartão de definição diferente do resto: termo em tipografia enorme, negrito, centralizado, com legenda pequena embaixo e nenhuma imagem, caso do cartão "HEVC" com a expansão da sigla (folha 0011, q0097 e q0098).
- A comparação de antes e depois é feita por sobreposição de grade em vez de rótulos de certo e errado. A mesma foto aparece colorida com grade azul de perspectiva e depois dessaturada, mantendo as linhas azuis (folha 0008, q0066 para q0067). Na folha 0013, a imagem corrigida com grade azul aparece junto de uma miniatura no canto com a captura original distorcida (q0114).
- A transição entre níveis de imersão aparece como desfoque progressivo de borda, não como corte seco. A janela de vídeo perde a moldura retangular e as bordas se dissolvem em vinheta borrada ao entrar em imersão (folha 0005, q0038 para q0039), e a mesma linguagem volta na redução automática de imersão, quando a cena perde nitidez até deixar ver os móveis reais atrás (folha 0016, q0142 a q0144, com retorno à nitidez na folha 0017, q0148).
- Uma tela real de Ajustes do visionOS mostra a anatomia do painel: coluna lateral com ícones coloridos por categoria, categoria ativa destacada em azul claro, e painel principal com título, interruptor verde ligado, texto explicativo, duas opções de rádio e um controle segmentado de três posições para sensibilidade a movimento (folha 0017, q0149).
- A captura de app embutido mostra a construção de uma janela típica: cartão branco de cantos arredondados, barra de título fina no topo com ícone e nome do documento, colagem de vídeos de tamanhos irregulares com rótulos de texto, e uma barra de ferramentas flutuante em cápsula abaixo do cartão (folha 0002, q0011).
- A correspondência estéreo é ilustrada com marcadores circulares amarelos ligados por linhas finas entre os painéis esquerdo e direito, somando pontos a cada quadro até formar uma grade de correspondências entre céu, horizonte, água e pedras (folha 0012, q0100 para q0101).
- A curva de mistura de borda do formato imersivo é desenhada como um contorno pontilhado de pontos amarelos ao redor do recorte circular, visualmente diferente da borda borrada usada para spatial video (folha 0020, q0174).
- Tabelas densas só aparecem no fechamento: sete colunas, uma por perfil com seu ícone no topo, e linhas de critério à esquerda, com destaque de fundo azul claro em células específicas e marcas de verificação verdes aplicadas só a certas colunas (folha 0021, q0182 para q0183 e q0184).
- O encerramento repete a identidade de cor da abertura: o último quadro recebe uma camada magenta saturada sobre a cena inteira, ecoando o cartão inicial "WWDC25" (folha 0022, q0191 para q0192, contra a folha 0001, q0001).
Proporção visual: pelas notas, o apresentador sozinho ocupa poucos trechos de ligação entre blocos, sobretudo as folhas 0001 e 0022 e quadros isolados no meio; a maior parte dos quadros é slide, diagrama, captura de interface ou filmagem de exemplo, e em alguns momentos ele divide a tela com o slide (folhas 0006 q0051 a q0054, 0016 q0136 e q0137, 0019 q0163, q0168 e q0169).
<!-- /visual:wwdc2025_304 -->

## Build a SwiftUI app with the new design (id: wwdc2025_323, 22.3 min)

- Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/323/.
- Tese central: adotar o novo design system e o material Liquid Glass no SwiftUI é, em grande parte, automático ao recompilar com o Xcode 26 SDK, mas há novas APIs específicas para estrutura de app, toolbars, busca, controles e elementos de glass customizados que permitem refinar ainda mais a experiência.

O processo de design que a Apple descreve (aplicado ao app de exemplo Landmarks):
1. Atualizar componentes estruturais (NavigationSplitView, TabView, Sheets).
2. Atualizar toolbars (agrupamento, espaçamento, badges, ícones monocromáticos).
3. Atualizar experiência de busca (posicionamento consistente).
4. Deixar controles (botões, sliders, menus) ganharem Liquid Glass automaticamente.
5. Adotar glass em elementos de UI customizados quando necessário.

Princípios enunciados e o porquê:
- Liquid Glass é um material adaptativo: muda de claro para escuro automaticamente conforme o conteúdo abaixo, ao rolar a tela.
- Controles ganham vida durante interação (toggles, sliders, pickers segmentados viram liquid glass ao serem tocados), criando uma experiência "delightful".
- Ícones usam renderização monocromática em mais lugares (incluindo toolbars) para reduzir ruído visual e enfatizar o conteúdo do app; tint deve ser usado para "transmitir significado" (uma chamada para ação, um próximo passo), não só por efeito visual.
- Concentricidade de cantos (corner concentricity): botões e containers devem compartilhar o mesmo centro de canto com o container em que estão (ex.: um botão no fundo de uma sheet deve ter cantos concêntricos aos cantos da sheet); a shape "concentric rectangle" resolve isso automaticamente em diferentes telas.
- Glass não pode "amostrar" outro glass: elementos próximos em containers diferentes geram comportamento visual inconsistente; por isso GlassEffectContainer agrupa elementos para compartilhar a região de amostragem, sendo "essencial para correção visual".

Técnicas concretas de construção de interface:
- backgroundExtensionEffect: permite que views se estendam além da safe area sem recortar conteúdo; a imagem é espelhada e borrada fora da safe area, estendendo a obra sem clipar o conteúdo visível.
- tabBarMinimizeBehavior: configura a tab bar do iPhone para flutuar sobre o conteúdo e minimizar ao rolar (ex.: onScrollDown, usado pelo app TV); reexpande ao rolar na direção oposta.
- tabViewBottomAccessory: coloca uma view acima da tab bar (ex.: mini player da Music), aproveitando o espaço extra do colapso da tab bar; o ambiente expõe tabViewBottomAccessoryPlacement para adaptar o conteúdo do acessório quando colapsado.
- Sheets: em altura parcial no iOS 26, têm fundo Liquid Glass por padrão, inseridas (bordas inferiores "puxadas para dentro" encaixando nas curvas do display); ao transicionar para altura total, o fundo de glass se torna gradualmente opaco.
- Navigation zoom transition: sheets podem "morfar" para fora do botão que as apresenta, marcando o item da toolbar como fonte e o conteúdo da sheet como destino da transição.
- ToolbarSpacer: com espaçamento fixo, separa itens de toolbar em grupos visuais distintos (ex.: "favorite" e "add to collection" agrupados separadamente do share link e inspector); com espaço flexível, cria espaço expansível entre itens (usado pela Mail para item de filtro à esquerda e grupo de busca/compor à direita).
- sharedBackgroundVisibility: separa um item de toolbar em seu próprio grupo, sem fundo (usado pelo avatar do usuário no app Books).
- badge modifier: adiciona indicador em itens de toolbar em uma linha de código.
- scrollEdgeEffectStyle: ajusta a nitidez do efeito de borda de rolagem (scroll edge effect, um blur/fade sutil sob toolbars) em UIs densas com muitos elementos flutuantes, como no Calendar.
- Busca: no toolbar, o campo fica na parte inferior da tela (fácil alcance); em iPad/Mac, aparece na posição superior-direita da toolbar; searchToolbarBehavior permite optar explicitamente pelo comportamento minimizado quando busca não é central à experiência do app.
- Busca como aba dedicada: definir role de busca numa aba do TabView; ao ser selecionada, o campo de busca substitui a tab bar (padrão usado pelo Health app).
- Botões com borda: forma de cápsula por padrão; controles mini, small e medium no macOS mantêm forma de retângulo arredondado (preservando densidade horizontal); alturas de controles atualizadas no macOS (controles ligeiramente mais altos, mais espaço ao redor do rótulo, alvos de clique maiores); há suporte para botões extra grandes; novos estilos glass e glassProminent.
- Sliders: agora suportam marcas de escala (tick marks), aparecem automaticamente ao inicializar com parâmetro step, ou manualmente via closure de ticks (exemplo dado: marcas em 60% e 90%); parâmetro neutralValue permite iniciar o preenchimento da trilha em um ponto não-inicial (útil para valores de velocidade de playback que podem subir ou descer a partir de um padrão).
- glassEffect modifier: aplica glass dentro de forma de cápsula por padrão; texto dentro do glass usa cor vibrante automaticamente adaptativa para legibilidade; modifier interactive faz o glass reagir a interação (escala, quica, brilha).
- GlassEffectContainer + glassEffectID: agrupam múltiplos elementos de glass para que interajam e se fundam entre si; usados no app de exemplo Landmarks para criar "morphing" fluido de badges ao expandir e recolher.

Exemplos citados:
- Landmarks (app de exemplo da Apple): usado ao longo de todo o vídeo como caso de aplicação de cada API nova.
- TV app: usa tabBarMinimizeBehavior com onScrollDown.
- Music app: usa tabViewBottomAccessory para o mini player.
- Mail app: usa ToolbarSpacer flexível para separar filtro (leading) de busca/compor (trailing).
- Books app: usa sharedBackgroundVisibility para isolar o avatar do usuário sem fundo compartilhado.
- Maps: exemplo de controles customizados de glass flutuando sobre o mapa, citado como bom candidato ao efeito de camada flutuante.

Citações curtas:
"Sometimes, in life, to gain clarity and focus on what's truly important, you may need to re-invent yourself."
"Only use this to convey meaning, like a call to action or next step, but not just for visual effect."

<!-- visual:wwdc2025_323 -->
### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.
- O formato dominante é o par código Swift mais mockup do resultado, quase sempre com o código à esquerda e o aparelho à direita, e um trecho específico do código realçado a cada troca de assunto. Só a imagem mostra a sintaxe exata dos modificadores, nomes de parâmetros e aninhamento (folhas 0004 q0031, 0005 q0039, 0011 q0093, 0014 q0125, 0016 q0136). Em parte dos quadros o mockup fica abaixo do código, não ao lado (folha 0010, q0086).
- Prática recomendada e desencorajada são marcadas por ícones, não por palavras: círculo vermelho com X junto ao código de fundo customizado de apresentação (folha 0006, q0049) e no diagrama de duas regiões de amostragem sobrepostas (folha 0015, q0135); check verde junto ao código de transição de zoom (folha 0006, q0050) e ao lado da tela "Sahara Desert" no quadro seguinte ao que trazia o rótulo de anotação (folha 0009, q0076 para q0077).
- A estrutura do vídeo é marcada por um índice visual recorrente: a lista de tópicos aparece sobre a filmagem do apresentador, com o item atual em negrito e os demais em cinza claro, chegando a cinco itens (folha 0003, q0022 a q0024; repete nas folhas 0007 q0057, 0009 q0079, 0011 q0099, 0014 q0121). Nas quatro primeiras vezes ela é seguida por um cartão de título isolado com o nome do tópico (folhas 0003 q0025, 0007 q0058, 0009 q0080, 0012 q0100); na quinta, o quadro seguinte ao destaque já é um mockup de mapa, sem cartão de título.
- API nova recebe selo verde apontando para a linha exata dentro do próprio bloco de código (folha 0004, q0031 para q0032, no modificador de extensão de fundo).
- Medidas exatas aparecem em diagrama: o slide de tamanhos de botão traz cinco alturas em pontos, de 16 a 36, uma por tamanho nomeado (folha 0012, q0105), e o slide anterior separa por faixa de tamanho quem usa retângulo arredondado e quem usa cápsula, com a caixa de código dos dois modificadores sobreposta ao mesmo diagrama (q0103 para q0104). Pelas notas, a fala trata do aumento das alturas sem citar esses números.
- Estados de um mesmo componente são comparados de duas maneiras: dois aparelhos lado a lado, um com a tab bar cheia e outro com ela recolhida (folha 0005, q0040), e o mesmo elemento em quadros consecutivos, como a alça do slider que muda de posição, tamanho e opacidade de um quadro para o outro, sugerindo repouso e interação (folha 0002, q0013 para q0014).
- Rótulos de anotação com linha apontam para o elemento exato da tela: "Search Field" sobre os campos de busca do MacBook e do iPad (folha 0010, q0085), "Edge Effect" sobre a área da toolbar da tela "Sahara Desert" e "Hard edge effect" sobre o topo da tela do app de Calendário (folha 0009, q0076 e q0078), e "Badge" sobre o indicador numérico vermelho no ícone de sino (folha 0008, q0071).
- A anatomia da toolbar é mostrada pela evolução do destaque no código sobre a mesma tela de resultado: o realce passa do espaçador fixo para o item de inspector sem que o mockup mude (folha 0007, q0062 para q0063), e o avatar isolado ganha um leve fundo circular quando o modificador que oculta o fundo compartilhado é realçado (folha 0008, q0065 para q0066).
- O efeito do material aparece por mudança de cor e forma do mesmo elemento entre quadros consecutivos: o badge passa de retângulo arredondado para cápsula verde ao receber tingimento (folha 0015, q0127 para q0128), depois vai de verde para amarelo dourado (q0129 para q0130) e de dourado para laranja rosado (q0130 para q0131), acompanhando o bloco de código de vidro interativo.
- O conceito de amostragem de vidro é explicado por diagrama abstrato: uma pílula rotulada como vista com efeito de vidro cercada por sua região de amostragem, e depois duas dessas regiões se sobrepondo, marcadas com X vermelho (folha 0015, q0133 a q0135).
- A animação de agrupamento é mostrada pela contagem de elementos entre quadros: os badges circulares empilhados à direita da tela aumentam de dois para vários e depois voltam a dois, enquanto o bloco de código com o container e os identificadores permanece à esquerda (folha 0016, q0136 a q0139).
- Quase toda tela de resultado é enquadrada no desenho físico do aparelho, às vezes com o mesmo app em MacBook, iPad e iPhone ao mesmo tempo (folhas 0003 q0019 e q0020, 0007 q0059 e q0060, 0008 q0072), às vezes em dois aparelhos apenas, MacBook e iPad (folha 0010, q0083 e q0084), o que reforça visualmente a ideia de família entre plataformas.
- Um efeito de camada semitransparente e desfocada ao redor da tela aparece como recurso de apresentação em dois momentos, no iPad e depois nos três aparelhos juntos (folha 0004, q0028 para q0029; folha 0007, q0060 para q0061).
- Controles do sistema são apresentados soltos como referência de design antes de qualquer código: zoom, botão simples, botão tintado, toggle, picker em lista e controle segmentado, primeiro sobre um iPhone central e depois sem ele (folha 0002, q0011 para q0012).
- O slider aparece com ícones simbólicos nas extremidades em vez de texto, lupas em um caso e tartaruga e coelho no outro. O preenchimento já começa de um ponto interno do trilho no quadro da tartaruga e do coelho, antes de o código mudar, e se desloca mais para a direita quando o parâmetro de valor neutro entra no código (folha 0013, q0110 a q0113).
Proporção visual: pelas notas, o apresentador sozinho ocupa trechos curtos de ligação entre tópicos e a folha final inteira (folha 0017), enquanto da folha 0004 até a 0016 a maior parte dos quadros é código, diagrama ou mockup de aparelho.
Divergências ou limites registrados: as notas marcam o quadro q0114 (folha 0013), um menu de contexto de sistema com itens de desfazer, refazer, copiar e duplicar, como sem ligação aparente com o conteúdo de sliders ao redor, possivelmente um instante de transição capturado entre cortes.
<!-- /visual:wwdc2025_323 -->

## Elevate the design of your iPad app (id: wwdc2025_208, 15.3 min)

- Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/208/.
- Tese central: iPadOS 26 introduz novos blocos de construção (navegação fluida, janelas com redimensionamento livre, novo ponteiro, menu bar completo) que, juntos, permitem elevar um app de iPad muito além do que era possível antes; a base de tudo é a simplicidade.

O processo de design que a Apple descreve:
1. Escolher o padrão de navegação (sidebar ou tab bar).
2. Fazer a navegação adaptar-se a tamanhos menores.
3. Estender o conteúdo ao redor da navegação.
4. Ajustar o app ao novo sistema de janelas (multitasking).
5. Considerar o novo ponteiro e o hover effect.
6. Construir a menu bar do app.

Princípios enunciados e o porquê:
- Sidebar é ideal para apps com muitas subvisões ou conteúdo profundamente aninhado (ex.: Mail); tab bar é mais compacta e flexível, permitindo mostrar mais conteúdo e sensação mais imersiva. Recomenda-se começar com tab bar se houver dúvida, pois ela pode "morfar" para sidebar conforme o app escala.
- Ao adaptar a navegação a mudanças de tamanho, a mudança de layout deve ser não-destrutiva: redimensionar o app não deve alterar permanentemente seu layout; deve-se ser "oportunista" e reverter ao estado inicial sempre que possível.
- O conteúdo é o motivo de as pessoas usarem o app, então deve-se usar o máximo do display possível para a experiência mais imersiva (via scroll edge effect, estendendo conteúdo abaixo do toolbar e da sidebar).
- Sobre multitasking: cada documento deve abrir em sua própria janela (comportamento aditivo), ao invés do antigo "Open in Place" que limpava o contexto anterior; isso exige nomear cada janela de forma descritiva (ex.: título do documento), porque senão a nova lista de janelas no menu do app não ajuda a encontrar a janela certa.
- O novo ponteiro rastreia a entrada diretamente 1 para 1, sem magnetizar ou "rubber band" para nenhum alvo; é mais preciso porque, sob o capô, o ponteiro sempre foi capaz de mais precisão do que o dedo aproxima.
- Itens de menu devem permanecer sempre no mesmo lugar, mesmo quando inativos (aparecem esmaecidos); escondê-los é desorientador, porque obriga a pessoa a reescanear o menu inteiro a cada abertura, sem poder confiar na memória espacial. O mesmo vale para menus inteiros: nunca escondê-los por completo, mesmo quando nada dentro deles é acionável no momento.

Técnicas concretas de construção de interface:
- Sidebar pode morfar fluidamente em tab bar (e vice-versa) por meio de um botão na própria sidebar (exemplo: Music app).
- Wrap do toolbar ao redor dos window controls: para apps atualizados ao iPadOS 26, os controles de janela devem ficar em linha na borda de saída (leading) do toolbar do app, evitando reservar uma safe area permanente acima do toolbar (que é o comportamento de compatibilidade para apps não atualizados); isso libera espaço para mais conteúdo sem aumentar o tamanho da janela.
- Handle no canto inferior direito de cada janela permite arrastar para redimensionar; os window controls, no canto superior esquerdo, aumentam ao toque revelando funcionalidade, e se pressionados e segurados expandem para mostrar atalhos de layouts de janela.
- Ponteiro: novo formato (deixou de ser circular, aproximando o dedo) para um formato mais preciso e responsivo; novo highlight effect é uma "plataforma" (platter) de liquid glass que materializa sobre os botões ao passar o ponteiro, dobrando e refratando os elementos abaixo para indicar o botão selecionado.
- Menu bar: revelada movendo o ponteiro até a borda superior, ou deslizando para baixo com o dedo; contém o app menu, menus padrão fornecidos pelo sistema, e menus customizados do app.
- Organização de menu customizado (exemplo: menu "Message" do Mail): popular com toda ação relacionada ao nome do menu; ordenar por frequência de uso, não alfabeticamente; agrupar ações relacionadas em suas próprias seções; mover ações secundárias para submenus quando o menu ficar longo; atribuir um símbolo a cada item (idealmente igual ao usado no app); atribuir atalhos de teclado às ações mais comuns.
- Popular o menu "View" (fornecido pelo sistema) com as abas do app (se organizado por abas) e um toggle de navegação (mostrar/ocultar sidebar).

Exemplos citados:
- Mail: sidebar lista caixas de correio e múltiplas contas, expondo a hierarquia de conteúdo ao nível superior; navegação mais rápida porque a sidebar "achata" a navegação.
- Music: sidebar com biblioteca e playlists; tem botão que morfa a sidebar em tab bar.
- TV app: usa tabBarMinimizeBehavior com onScrollDown para o multitasking.

Citações curtas:
"At its core, iPad is about simplicity."
"Hiding menu items is not recommended because people will find this disorienting."

<!-- visual:wwdc2025_208 -->
### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.
- Marcação fixa de certo e errado como método pedagógico: um check verde no canto superior direito assina a composição aprovada e um X vermelho assina a reprovada. O par completo aparece em dois temas, o documento aberto em janela própria contra a janela que substitui conteúdo (folha 0009, X em q0079 e check em q0083) e o menu com todos os itens contra o menu reduzido (folha 0015, q0132 a q0135). Na folha 0008 aparece só a marcação negativa, sobre a faixa acima da toolbar (q0070).
- Anotação de erro por linha tracejada vermelha: a folha 0008 desenha uma linha tracejada horizontal acima da toolbar do Mail, junto do X vermelho (q0070 e q0072), e antes disso mostra os três círculos de controle de janela em close com uma régua de medida acima indicando distância (q0069). O que a tela marca é essa faixa acima da toolbar; a explicação de safe area reservada a apps não atualizados vem da fala, não do quadro.
- Rótulos de texto sobrepostos à interface real para nomear a estrutura: palavras em cinza como "Mailboxes", "Accounts", "Tabs", "Library", "Playlists" ficam ao lado das sidebars do Mail e do Music, como camada didática que a interface final não tem (folha 0003, q0023 a q0026).
- Comparação dos dois padrões de navegação sobre a mesma tela de conteúdo: a barra vertical recebe o rótulo "Sidebar" e a barra horizontal recebe "Tab bar", e a sequência seguinte mostra a mesma tela do Music passando de um formato para o outro e de volta (folha 0004, q0028 a q0036).
- A adaptação por largura é demonstrada em três estados do mesmo app: tela cheia dentro de moldura de iPad, a mesma interface girada em perspectiva e janela flutuante menor sobre um ambiente físico desfocado (folha 0005, q0039 a q0045), e depois janelas de tamanhos variados com a Dock do iPad aparecendo por baixo (folha 0006, q0046 a q0054).
- Anatomia dos controles de janela: cápsula translúcida esbranquiçada com sombra reunindo três círculos coloridos no padrão vermelho, amarelo, verde, mais um ícone de sidebar ao lado, no canto superior esquerdo da janela, isolada em close por três quadros quase idênticos que sugerem animação lenta de destaque (folha 0007, q0061 a q0063).
- Acúmulo de janelas mostrado por sobreposição com deslocamento diagonal e sombra: duas janelas de Fotos ("Recents" e "Timelapse") na folha 0009 e três janelas de Notas ("Roadtrip To Do's", "Presentation Notes", "Bird Spotting") aparecendo uma a uma na folha 0010 (q0085 a q0087).
- O antes e depois da nomeação de janela aparece dentro do próprio menu: o menu "Open Windows" primeiro lista "Notes 1, Notes 2, Notes 3" com check na janela ativa (folha 0010, q0088 e q0090) e depois lista os títulos reais dos documentos, já com check verde de aprovação no canto do quadro (folha 0011, q0091 a q0093).
- Anatomia do highlight do ponteiro: três ícones de toolbar dentro de uma única cápsula translúcida branca recebem um círculo cinza de destaque que se desloca do ícone central para o da direita entre quadros, com selo verde "NEW" e cursor de seta apontando para o alvo no quadro do meio (folha 0012, q0101 a q0104).
- A barra de menu de desktop aparece reproduzida integralmente no iPad, com itens de texto simples (Mail, File, Edit, View, Mailbox, Message, Format, Window, Help) e o item aberto destacado em azul. O menu "File" do Mail traz atalhos de teclado alinhados à direita, comando N e comando O entre eles (folha 0002, q0012), enquanto o menu "Message" isolado em close lista os itens com setas de submenu e sem atalhos visíveis (folha 0013, q0116 e q0117).
- Popular o menu View é mostrado com dois apps, mas com conteúdos diferentes: no Clock as próprias abas viram itens do menu, com atalhos numerados, comando 1 em "World Clock" e comando 4 em "Timers" (folha 0014, q0121 a q0126); no Music o menu View lista ações de mostrar e ocultar painéis (Show Sidebar, Show Now Playing, Show Lyrics), cada uma com seu atalho (folha 0015, q0127 a q0129).
- Os slides funcionam como barra de progresso tipográfica: a mesma lista de quatro temas reaparece a cada troca de seção com o item atual em preto forte e os demais em cinza claro (folhas 0002, 0007, 0011 e 0012), e na folha 0016 os quatro aparecem igualmente destacados, sinalizando o fim do percurso. Os slides de recomendação seguem um único padrão, título grande em negrito e itens em peso regular, montados por acréscimo, primeiro o título sozinho e depois as linhas (folha 0007, q0055 para q0056; folha 0016, q0139 para q0140).
- A tela mostra a moldura preta de iPad com cantos arredondados quando a intenção é situar o app no dispositivo, e retira a moldura quando o foco é um componente isolado, toolbar, menu ou cursor sobre fundo cinza vazio (folhas 0004, 0011, 0012 e 0013).
Proporção visual: das 17 folhas, apenas a última é só apresentador, e os quadros de apresentador nas demais são isolados; o volume está em capturas de apps reais (Mail, Music, Fotos, Notas, Clock), quase sempre dentro de moldura de iPad, mais uma dezena de slides de texto de título e resumo.
Divergências ou limites registrados: as notas registram que o sistema de marcação verde e vermelho não é mencionado na fala, assim como os rótulos didáticos sobrepostos à interface; que a indicação visual de quanto foi rolado, citada na fala, não aparece de forma explícita nos quadros da folha 0006; que na folha 0003 o botão que transforma sidebar em tab bar é descrito na fala mas não aparece nos quadros; e que a lista de temas troca de nome ao longo do vídeo, com "Layout" no lugar de "Navigation" já na folha 0007, "Arrow Pointer" no lugar de "Pointer" a partir da folha 0012 e "Windowing" e "Menu Bar" na lista final da folha 0016.
<!-- /visual:wwdc2025_208 -->

## Build a UIKit app with the new design (id: wwdc2025_284, 25.9 min)

- Base: transcrição e 19 de 19 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/284/.
- Tese central: assim como no SwiftUI, apps UIKit recebem grande parte do novo design system (Liquid Glass) automaticamente ao recompilar com o novo SDK, mas há novas APIs específicas para tab views, split views, bars, apresentações, busca, controles e elementos de glass customizados.

O processo de design que a Apple descreve (equivalente UIKit ao vídeo SwiftUI):
1. Tab views e split views adotam o novo design e flutuam sobre o conteúdo.
2. Navigation bars e toolbars ficam transparentes, com botões de liquid glass, dando mais espaço ao conteúdo.
3. Apresentações (sheets, alerts, action sheets) ganham transição de zoom atualizada.
4. Experiência de busca atualizada com mais opções de posicionamento.
5. Controles (botões, switches, sliders) ganham novo visual.
6. Elementos de UI customizados podem adotar Liquid Glass via API própria.

Princípios enunciados e o porquê:
- Liquid Glass é distinto de outros efeitos visuais como UIBlurEffect: é desenhado para ser uma "camada interativa" que flutua acima do conteúdo, bem abaixo da ponta dos dedos, fornecendo os controles principais que a pessoa toca; por isso deve ser limitado aos elementos mais importantes do app, preferindo views e controles do sistema onde possível.
- Fundo das bars é transparente por padrão; customizações de fundo (UIBarAppearance, backgroundColor) interferem na aparência de glass e devem ser removidas.
- Grupos de itens em glass separado devem ser usados para distinguir ações relacionadas de ações com comportamento distinto (ex.: botões de imagem compartilham fundo entre si; botões de texto, "Done"/"Close" do sistema, e estilo prominente têm fundos próprios).
- Glass não pode amostrar outro glass: manter elementos de glass próximos em containers diferentes gera comportamento inconsistente (mesmo princípio do vídeo de SwiftUI); UIGlassContainerEffect resolve compartilhando a região de amostragem e reforçando uma adaptação uniforme.

Técnicas concretas de construção de interface:
- UITabBarController: tabBarMinimizeBehavior (ex.: TV app com .onScrollDown); bottomAccessory via UITabAccessory (ex.: mini player da Music), com trait tabAccessoryEnvironment para adaptar o accessory view quando colapsado inline.
- UIBackgroundExtensionView: cobre toda a largura, incluindo o inset de safe area leading da sidebar; input é uma content view (ex.: image view) posicionada na hierarquia e estendida para preencher o espaço vazio; por padrão preenche a safe area em todas as bordas com inset positivo; pode-se desligar automaticallyPlacesContentView para posicionar manualmente com AutoLayout (ex.: extensão só na borda leading para a sidebar, mas não no topo, se a navigation bar tiver pouco conteúdo que possa cobrir a arte).
- Navigation bars/toolbars: itens são automaticamente agrupados em conjuntos visuais com fundo de glass compartilhado; usar fixedSpace para separar itens em grupos distintos; bar buttons usam labelColor por padrão (legibilidade); tintColor customizado transmite significado de ação (ex.: systemOrange no botão "Flag"); estilo prominent tinge o próprio fundo do botão.
- flexibleSpace: por padrão separa o fundo entre itens; usar hidesSharedBackground = false para distribuir itens uniformemente mantendo um único fundo compartilhado.
- UINavigationItem: nova subtitle renderizada abaixo do título (exemplo: Mail mostra número de e-mails não lidos); largeSubtitleView permite mostrar um botão (ex.: filtro ativo) abaixo do título grande.
- Large titles agora ficam no topo do scroll view e rolam junto com o conteúdo; é preciso estender o scroll view totalmente sob a navigation bar para manter o título grande visível.
- Edge effect: tratamento visual automático (blur/fade) aplicado a scroll views sob navigation/toolbars, garantindo legibilidade de conteúdo sobreposto; pode ser aplicado a containers customizados via ScrollEdgeElementContainerInteraction; estilo .hard disponível para UIs densas com muitos elementos flutuantes (aparência semelhante aos fundos de bar do iOS 18).
- Zoom transition interruptível: a transição de navegação padrão (slide) agora é sempre interativa e interruptível, como já era em iOS 18 para o zoom transition; permite swipe back a qualquer momento durante a transição, inclusive em áreas de conteúdo não-leading (content backswipe gesture), verificando automaticamente interações concorrentes (ex.: swipe actions têm prioridade sobre o content backswipe).
- Presentations: menus e popovers originados de um botão glass fazem o botão "morfar" no overlay, mantendo continuidade visual; sheets podem adotar isso definindo preferredTransition como .zoom e retornando o barButtonItem de origem; action sheets no iPhone agora se ancoram à view de origem (sourceItem/sourceView no popoverPresentationController), igual ao iPad; sem source, o action sheet aparece centralizado com botão cancelar.
- Busca: no iPhone, a barra de busca move automaticamente para o toolbar via searchBarPlacementBarButtonItem; no iPad, segue o padrão do toolbar do macOS na borda trailing da navigation bar (searchBarPlacementAllowsExternalIntegration = true), ideal para split views; UITabBarController pode ter uma aba distinta de busca à direita, que expande ao ser tocada (automaticallyActivateSearch = true ativa o campo automaticamente); integratedCentered centraliza a barra de busca no iPad.
- Controles: UISwitch com tamanhos atualizados; thumbs de switch e segmentedControl ganham aparência liquid glass automaticamente durante interação; UIButtonConfiguration ganha .glass() e .prominentGlass(); sliders preservam momentum e "esticam" ao mover, suportam tick marks via TrackConfiguration (exemplo: slider de velocidade limitado a 5 valores com allowsTickValuesOnly), neutralValue para ancorar o preenchimento em qualquer ponto da trilha, e estilo "thumbless" (parece barra de progresso) para playback de mídia.
- API para glass customizado: UIVisualEffectView com UIGlassEffect; forma de cápsula por padrão, customizável via cornerConfiguration (.containerRelative adapta automaticamente para manter concentricidade); glass adapta aparência conforme tamanho (maior = mais opaco; menor = mais "clear" e alterna entre claro/escuro para aumentar contraste); isInteractive = true para reação de escala/bounce ao toque; sempre preferir animar a propriedade "effect" (não o alpha) para materializar/dematerializar corretamente.

Exemplos citados:
- TV app: sidebar com conteúdo vibrante por baixo (poster com UIBackgroundExtensionView), tabBarMinimizeBehavior.
- Music app: mini player como bottom accessory da tab bar.
- Mail: subtitle mostrando contagem de e-mails não lidos; filtro atual em largeSubtitleView; agrupamento de bar buttons com fixedSpace.
- Notes: usado para demonstrar a transição de navegação interruptível (swipe back a qualquer momento).
- Maps: botões customizados de glass flutuando sobre o mapa; ao expandir a sheet, os botões são removidos para não sobrepor glass a glass.

Citações curtas:
"Liquid Glass is designed to be an interactive layer."
"For that reason, limit Liquid Glass to the most important elements of your app."

<!-- visual:wwdc2025_284 -->
### O que as imagens mostram
Base: 19 de 19 folhas de quadros vistas, todos os códigos conferidos.
- O formato dominante é código Swift ao lado da captura do app afetado, e a diferença entre quadros mostra a linha nova e o efeito dela na tela ao mesmo tempo: na folha 0007, a linha de espaçamento fixo entra no código e a captura ganha um vão perceptível entre os ícones da barra de navegação (q0055 para q0056), e logo depois a linha de cor de destaque entra e o ícone de bandeira passa de preto para laranja (q0058 para q0059).
- Anatomia do agrupamento de botões na barra de navegação do app de flores: um botão de texto isolado à esquerda, um bloco de três ícones de imagem no meio (compartilhar, pasta, bandeira) e um botão de confirmação sozinho à direita (folha 0006, q0051). Quem nomeia a regra é o slide ao lado, que lista primeiro quem compartilha fundo de vidro e no quadro seguinte acrescenta quem recebe fundo próprio (q0052 para q0053).
- Anotações de rótulo com linha fina apontando para regiões da captura nomeiam as partes do mecanismo de extensão de fundo, sempre sobre a mesma tela de iPad do app TV: "UIBackgroundExtensionView" na parte inferior da tela (folha 0004, q0034 e q0035), "Content view" apontando para o centro da imagem (q0035) e, na folha seguinte, "Content view" e "Extension" juntos, este último na faixa entre a sidebar e a arte (folha 0005, q0041 a q0043).
- O efeito de borda aparece nos dois estilos e com rótulo apontando para a faixa exata: o escurecimento gradual do conteúdo que rola sob a barra na tela de e-mail (folha 0009, q0075 para q0076), o mesmo efeito aplicado a um container customizado atrás de dois botões no rodapé de uma tela de confirmação, com a etiqueta "Edge Effect" (q0077 a q0079), e o estilo sólido e opaco na barra superior do calendário (q0080 e q0081).
- Anatomia da área de título: título grande "Inbox" com subtítulo menor em cinza abaixo, e depois um botão de filtro em formato de pílula ocupando a linha sob o título grande, mostrado em iPhone e iPad na mesma composição (folha 0008, q0068 a q0071). O slide que abre a seção monta a lista de novidades um item por quadro (q0064 a q0067).
- Diferença entre quadros que mostra a transição da busca como aba: a tela do app de saúde passa de "Summary" para "Search" com lista de categorias (folha 0013, q0114 para q0115) e no quadro seguinte o teclado do sistema sobe, tornando visível a ativação automática do campo (q0116 para q0117). O mesmo par se repete em outro app, de "Library" para "Search" com miniaturas recentes e teclado (folha 0014, q0118 para q0119).
- Três posicionamentos de busca são mostrados em telas diferentes: campo em cápsula na barra inferior do iPhone ao lado do botão de adicionar (folha 0012, q0108), campo à direita da barra de navegação do iPad em layout de duas colunas (folha 0013, q0112 e q0113) e campo centralizado horizontalmente no topo sobre uma grade de cartões coloridos de categoria (folha 0014, q0121 a q0123).
- Vitrine de controles isolados, um componente por slide, centralizado sobre fundo neutro com o trecho de código em fonte monoespaçada pequena abaixo: switch verde ligado, botão de vidro simples ao lado do botão de vidro proeminente em azul, e slider azul entre ícones de tartaruga e coelho (folha 0015, q0127 a q0129).
- A anatomia do slider é demonstrada por deslocamento do thumb entre quadros: com marcas de escala, o thumb aparece em duas posições distintas, sempre alinhado a uma marca (q0130 para q0131); com valor neutro, o thumb muda de lado mas o preenchimento azul continua nascendo do mesmo ponto interno da trilha, e não da ponta (q0132 para q0133); e o estilo sem thumb aparece como barra lisa (q0134). Onde o preenchimento começa só fica claro na imagem.
- A adoção de vidro em view customizada é encenada como camadas acumuladas sobre o mesmo objeto, sempre sobre a mesma foto de folha verde com flor amarela: cantos fixos viram cantos relativos ao container, a origem do frame se desloca, o tamanho muda entre dois valores, um rótulo "WWDC25" entra dentro do vidro, o texto e o fundo recebem azul de destaque, e depois o texto some por alpha antes de o efeito ser removido (folhas 0017 e 0018, q0145 a q0158).
- Duas cápsulas de vidro dentro do mesmo container mostram o comportamento de proximidade: aparecem separadas por um espaçamento definido em código e depois se fundem em uma forma única maior (folhas 0018 e 0019, q0162 a q0164).
- A continuidade entre botão e apresentação é mostrada por crescimento a partir da origem: um popover cresce do botão de origem no iPad em quadros sucessivos (folha 0011, q0094 e q0095). Logo depois, a sheet de escolha de pasta do Mail aparece ao lado do código da transição de zoom, em cartão com cantos arredondados, título centralizado, botão de fechar e lista de pastas com ícone colorido e contagem (q0097); a origem dessa sheet no botão de pasta está no código e na fala, não num movimento visível entre quadros.
- Uma metáfora visual encena o vidro como camada física: um cartão de mensagem inclinado em ângulo isométrico, com sombra pronunciada, gira e se aproxima até se achatar contra a tela do iPhone, com uma segunda camada semitransparente atrás (folha 0016, q0137 a q0140).
- Slide de advertência com ícone de alerta em amarelo alaranjado lista as duas customizações de fundo de barra a evitar, acrescentando as linhas entre quadros (folha 0009, q0073 para q0074), e os slides de tópicos usam hierarquia por opacidade, item atual em preto forte e os demais em cinza claro, repetida em quase toda a apresentação.
Proporção visual: nenhuma das 19 folhas é só apresentador; ela aparece em quadros isolados de transição, e o volume está em capturas de apps reais (TV, Música, Mail, Notas, Contatos, Saúde, Maps, Calendário, Weather e um app de detalhes de local) quase sempre pareadas com trechos de código Swift, mais slides de título e lista que se montam por acréscimo.
Divergências ou limites registrados: as notas apontam que na folha 0011 o conteúdo do popover muda entre q0095 e q0096, o que indica dois exemplos diferentes e não um mesmo elemento em transição; e registram várias sequências de quadros consecutivos sem diferença perceptível na tela, umas com o código ao lado avançando (folhas 0012, 0013 e 0014) e outras sem mudança de nenhum dos dois lados (folhas 0004, 0010 e 0016).
<!-- /visual:wwdc2025_284 -->

## Meet SwiftUI spatial layout (id: wwdc2025_273, 20.4 min)

- Base: transcrição e 15 de 15 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/273/.
- Tese central: no visionOS 26, o sistema de layout do SwiftUI (com seus conceitos e ferramentas de 2D já conhecidos) passa a funcionar nativamente em três dimensões, permitindo construir experiências espaciais declarativas sem precisar do RealityKit para tudo.

Este vídeo é majoritariamente técnico (APIs de layout 3D em SwiftUI), com aplicação direta em construção de interface espacial.

O processo de design que a Apple descreve (usando o app de exemplo BOT-anist):
- Views em visionOS calculam largura, altura, profundidade e posição Z (não só X e Y).
- Views com quadro fixo (ex.: Model3D) versus flexível (ex.: RealityView, GeometryReader3D, que ocupam toda profundidade proposta por padrão).
- Uma janela (Window) propõe profundidade fixa ao conteúdo; um volume (Volume) propõe profundidade também redimensionável.
- Stacks (ZStack, HStack, VStack) já são 3D no visionOS, com comportamentos padrão sensatos para profundidade; ZStack compõe profundidade como VStack compõe altura.

Princípios enunciados e o porquê:
- Usar o sistema de layout do SwiftUI (em vez de posicionamento manual) dá suporte embutido a animações, redimensionamento e gerenciamento de estado automaticamente: ao remover um robô do carrossel, o SwiftUI anima as posições e tamanhos dos demais para acomodar o novo espaço.
- Efeitos visuais (rotation3DEffect, scaleEffect, offset) não impactam o layout: a HStack não "sabe" da geometria rotacionada de uma view, o que é bom para animar algo sem afetar vizinhos, mas ruim quando se quer que o layout reaja à rotação, por isso existe o rotation3DLayout, que modifica o frame da view rotacionada dentro do sistema de layout.
- Alinhamento de profundidade padrão em Stacks é "back"; pode ser customizado com depthAlignment (.front, .center, .back) ou com um alinhamento de profundidade totalmente customizado, implementando o protocolo DepthAlignmentID.

Técnicas concretas de construção de interface:
- scaledToFit3D: usado junto com resizable() para manter a proporção de aspecto de um Model3D (evitando "esticar" o modelo) enquanto ainda escala para caber na largura, altura e profundidade disponíveis.
- Model3DAsset: permite pré-carregar o modelo 3D de forma reutilizável.
- Depth Podium (exemplo customizado): três robôs alinhados de forma escalonada em profundidade, o primeiro alinha as costas (back) com o centro do segundo, e o centro do segundo alinha com a frente (front) do terceiro, implementado com uma struct que conforma ao protocolo DepthAlignmentID e um valor default (.front).
- rotation3DLayout: aplicado a um HStack com um modelo de foguete e um card de descrição, rotacionando 90° no eixo X (ou 45° em outro exemplo) e ajustando corretamente o tamanho/posicionamento do HStack para dar espaço ao objeto rotacionado, evitando que ele "esbarre" no card ou saia do volume.
- debugBorder3D (modifier customizado, ensinado ao final do vídeo): usa spatialOverlay para renderizar a borda no mesmo espaço 3D da view; internamente usa dois ZStacks e um rotation3DLayout para colocar bordas nas faces leading, trailing, back e front.
- SpatialContainer: posiciona múltiplas views no mesmo espaço 3D "como bonecas russas" (nesting dolls), aplicando um alinhamento 3D comum (ex.: bottomFront, topTrailingBack).
- spatialOverlay: similar ao SpatialContainer mas para sobrepor uma única view a outra no mesmo espaço 3D, com suporte a alinhamentos 3D (usado, por exemplo, para sobrepor um anel de seleção ao redor do robô selecionado, alinhado pelo fundo/bottom).
- MyRadialLayout (custom layout reaproveitado do vídeo "Compose custom layouts with SwiftUI"): posiciona views em círculo; combinado com rotation3DLayout (90° no eixo X) e um rotation3DEffect contrário de -90° em cada robô individualmente, para orientar o carrossel horizontalmente mantendo os robôs "em pé".

Exemplos citados:
- BOT-anist: app de exemplo usado para demonstrar customização de robôs, coleção de robôs num carrossel radial 3D, cartão de perfil de robô (RobotProfile) com nome/descrição alinhado à frente (front) para legibilidade, e anel de seleção via spatialOverlay.
- Rocket model + card de descrição: exemplo usado para contrastar rotation3DEffect (não afeta layout, causa sobreposição) versus rotation3DLayout (ajusta o layout corretamente).

Citações curtas:
"SwiftUI is a great tool for building 3D apps, but there are many use cases where you'll still want to reach for RealityKit."
"I love how I can compose these existing 2D SwiftUI modifiers with new 3D APIs to make something completely new."

<!-- visual:wwdc2025_273 -->
### O que as imagens mostram
Base: 15 de 15 folhas de quadros vistas, todos os códigos conferidos.

- O formato dominante do vídeo é um slide de dois painéis: à esquerda um comentário em cinza seguido de código Swift colorido por sintaxe, ao lado o resultado, que é uma miniatura de iPhone nos exemplos 2D e uma cena 3D renderizada da galeria de robôs nos exemplos visionOS. Esse pareamento aparece da folha 0003 à folha 0014, e é o que deixa visível qual linha de código corresponde a qual mudança na tela.
- Há anotação de medida explícita sobre o diagrama de layout: na folha 0003, o quadro q0022 traz setas e valores em pontos para posição Y de 40, posição X de 35, altura de 50 e largura de 100, ao lado do código da imagem da cabeça do robô e da miniatura de iPhone com a moldura vermelha correspondente.
- A convenção de cor dos contornos de depuração é fixa e carrega significado o vídeo inteiro: vermelho sólido para o frame da view individual ou para a geometria visual, amarelo para o frame do container composto, e azul tracejado para o frame que o sistema de layout enxerga. O amarelo aparece envolvendo um VStack na folha 0003, um ZStack na folha 0005 e um HStack nas folhas 0006 e 0007, e o par vermelho mais azul tracejado aparece nas folhas 0010 e 0011.
- O par certo e errado mais claro está na folha 0007: em q0060 o cartão de nome do robô fica escondido e cortado atrás do modelo, com alinhamento de profundidade padrão pelas costas, e em q0061 e q0062, depois de aplicado o alinhamento de profundidade pela frente, o mesmo cartão aparece inteiro e legível diante do robô. A folha mostra antes o mesmo conceito em 2D, com alinhamento ao centro em q0057 e pela base em q0058, usando a miniatura de iPhone como analogia.
- A prova visual da diferença entre efeito visual e layout está na folha 0010: em q0083 e q0084 o foguete girado colide com o cartão de detalhes, com o contorno vermelho e o azul tracejado visivelmente desalinhados, em q0085 a câmera lateral mostra o foguete saindo do quadro em direção à parede, e em q0090 os dois contornos coincidem e o foguete se posiciona ao lado do cartão sem sobreposição. A conclusão aparece escrita sobre a própria cena em q0086, como intertítulo curto.
- A folha 0011 repete a mesma checagem com outro ângulo: em q0092 e q0093 o foguete gira 45 graus e em q0094 os dois contornos de depuração aparecem exatamente sobrepostos, confirmando que a geometria girada e o frame de layout passaram a ser o mesmo.
- Diagramas abstratos servem de ponte antes da cena realista. Na folha 0008, os quadros q0068 e q0069 mostram três blocos coloridos primeiro em vista isométrica e depois em vista de cima, com linha pontilhada indicando qual está mais à frente. Na folha 0009, q0073 a q0076 evoluem esse diagrama de topo passo a passo, um quadrado mudando de profundidade por vez conforme cada linha de guia de alinhamento entra no código, e só em q0077 a cena real da galeria mostra os três robôs escalonados.
- Para explicar views que ocupam o mesmo espaço tridimensional, a folha 0013 usa caixas aninhadas em estilo boneca russa: q0112 mostra três caixas encaixadas, q0113 e q0114 mostram a mesma composição reposicionada em cantos opostos conforme o parâmetro de alinhamento muda, e q0115 reduz para duas caixas, marcando visualmente a diferença entre o contêiner de várias views e a sobreposição de duas.
- APIs novas recebem um selo verde escrito "NEW" colado sobre a palavra exata do código, não sobre o slide inteiro. Isso aparece na folha 0005 no modificador que ajusta a escala do modelo, na folha 0006 no tipo de recurso do modelo 3D, nas folhas 0007 a 0011 nos alinhamentos de profundidade customizados e no modificador de rotação que afeta o layout, e na folha 0013 no contêiner espacial e na sobreposição espacial.
- O código é construído por acréscimo, com a linha nova destacada em fundo azul claro sobre o trecho já existente, o que deixa o antes e o depois de cada adição visível quadro a quadro. É o caso do perfil de robô entre as folhas 0006 e 0007, do alinhamento de pódio entre as folhas 0008 e 0009, do carrossel entre as folhas 0011 e 0012, e do modificador de borda de depuração na folha 0014.
- A folha 0012 mostra a montagem do carrossel etapa por etapa dentro da cena: em q0102 a câmera se afasta e revela a disposição circular, em q0103 e q0104 os robôs aparecem deitados após a rotação de 90 graus no eixo X vista de cima, em q0105 e q0106 voltam a ficar em pé após a contra rotação individual, e em q0107 o conjunto inteiro desce até a base da sala com o uso de um espaçador.
- A folha 0014 monta a própria ferramenta de depuração na tela: em q0121 o robô aparece dentro de um contorno simples, em q0124 as bordas viram duas faces verticais cruzadas depois da rotação de 90 graus no eixo Y, e em q0125 um segundo empilhamento acrescenta frente e fundo, fechando a caixa de arestas em todas as faces.
- A lista de tópicos da sessão funciona como barra de progresso feita só de tipografia: o item ativo em negrito preto e os demais em cinza claro sobre fundo bege, reaparecendo nas folhas 0003, 0006, 0009 e 0012, cada vez com um único item trocando de peso. Na folha 0003 ela ainda ganha um quarto item entre q0019 e q0020.
- Cartões de legenda com nome em negrito e descrição curta abaixo flutuam junto aos objetos 3D nas folhas 0001, 0006, 0007, 0008 e 0009, sem moldura de janela e sem botões, mais próximos de etiqueta de museu do que de interface de app. A UI de app propriamente dita aparece em outros dois formatos: o painel do aplicativo de customização na folha 0001, com abas e paletas de cor em círculos organizados em grade, e o painel compacto de jogo na folha 0002, com título curto e dois botões lado a lado.
- O estado de seleção de um objeto 3D é comunicado por dois elementos combinados, vistos nas folhas 0013 e 0014: um anel branco sob os pés do robô e um painel flutuante pequeno acima dele com o nome do item e dois ícones circulares de ação, um de edição em forma de lápis e um vermelho anotado nas notas como de excluir ou parar.
- O encerramento, na folha 0015, revela a lista de próximos passos um item por quadro, de q0127 a q0130, acrescentando por último uma linha divisória e um rodapé com o nome da sessão recomendada à esquerda e a identificação do evento à direita, na mesma tipografia das listas de tópicos usadas ao longo do vídeo.

Proporção visual: cerca de quatro quintos dos quadros registrados mostram slide de código, diagrama ou cena tridimensional renderizada, e o apresentador sozinho aparece em blocos curtos intercalados, concentrados na abertura, nas trocas de tópico e no fecho.

Divergências ou limites registrados: quatro quadros tiveram o texto de código sobreposto e ilegível ou parcialmente ilegível por dupla exposição de transição de slide, em q0032 e q0034 da folha 0004, q0059 da folha 0007 e q0116 da folha 0013. As notas também registram trechos capturados com o código ainda incompleto, como o ângulo vazio em q0091 na folha 0011, e uma mudança de tom da camisa do apresentador entre q0002 e q0003 na folha 0001, anotada como possível corte de câmera.
<!-- /visual:wwdc2025_273 -->

## Design foundations from idea to interface (id: wwdc2025_359, 19.1 min)

- Base: transcrição e 15 de 15 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/359/.
- Tese central: um app bem desenhado responde com clareza a três perguntas em cada tela ("onde estou", "o que posso fazer", "para onde posso ir"), e chegar lá é um processo iterativo que passa por estrutura, navegação, conteúdo e design visual, nessa ordem.

O processo de design que a Apple descreve (demonstrado ao longo de um app fictício de coleção de discos de vinil):
1. Estrutura: escrever tudo que o app faz (recursos, fluxos, "nice-to-haves") sem julgar ou cortar nada ainda; depois imaginar como e quando as pessoas usariam o app, o que ajuda e o que atrapalha; só então limpar, removendo o que não é essencial, renomeando o que não é claro, e agrupando o que pertence junto. Esse processo é chamado de information architecture (organizar e priorizar informação para que as pessoas encontrem o que precisam, sem fricção).
2. Navegação: usar o aprendizado da arquitetura de informação para decidir o que vira aba na tab bar (perguntando "o que é realmente essencial? o que merece uma aba?"); nomear e escolher ícones (SF Symbols) que ajudem a entender o propósito de cada aba sem precisar interagir; usar o toolbar para resolver "onde estou" (título da tela, não menu ou branding) e "o que posso fazer" (ações específicas da tela).
3. Conteúdo: separar tipos de conteúdo misturados; aplicar progressive disclosure (mostrar só o necessário no início, revelando mais ao interagir); escolher o layout mais claro (lista versus grid) conforme o tipo de conteúdo; agrupar conteúdo por temas (tempo, sazonalidade, progresso, padrões) para reduzir sobrecarga de escolha.
4. Design visual: revisar como tipografia, cor e imagem trabalham juntas; construir hierarquia visual (o que deve ser visto primeiro); usar estilos de texto do sistema para hierarquia flexível sob diferentes condições de tela; escolher paleta de cores e regras simples para aplicá-la; usar cores semânticas (não hardcoded) para qualquer elemento dinâmico.

Princípios enunciados e o porquê:
- As três perguntas centrais de clareza: "onde estou", "o que posso fazer", "para onde posso ir a partir daqui", quando um app responde a essas perguntas com facilidade, ele parece convidativo e fluido, sinal de uma base sólida.
- Menus (hambúrguer) no topo da tela são vagos e imprevisíveis, porque o que a pessoa precisa primeiro é contexto, não uma lista escondida.
- Cada aba extra na tab bar é mais uma decisão que a pessoa precisa tomar, e pode apresentar o app como mais complexo do que realmente é; por isso simplificar a tab bar importa.
- Tabs são para navegação, não para tomar ação (referência direta às Human Interface Guidelines), por isso um botão de ação primária (como "Add") deve ficar dentro de uma seção, não na tab bar.
- Progressive disclosure: mostrar só o necessário logo de cara, revelando mais conforme a pessoa interage, evita sobrecarregar com escolhas.
- Agrupar conteúdo por tempo, sazonalidade, progresso ou padrões reduz a sobrecarga de escolha (choice overload) e faz o app parecer "um passo à frente", entendendo o que a pessoa vai precisar a seguir.
- Cores semânticas (nomeadas por propósito, como "label" ou "secondarySystemBackground", não por aparência como "preto" ou "roxo") são dinâmicas: mudam automaticamente conforme contraste, ambiente de tela e modos claro/escuro; usar accent color com cuidado para não atrapalhar essas mudanças dinâmicas, legibilidade geral, ou o conforto das pessoas.
- Elementos de design não devem ser tratados como projetos isolados: o impacto real vem de como eles trabalham juntos, contribuindo para o significado geral da interface.
- Design nunca está realmente terminado, e não há uma única resposta certa.

Técnicas concretas de construção de interface:
- Toolbar substituindo menu/branding: inclui título da tela (define expectativas sobre o conteúdo, ajuda a manter orientação ao navegar e rolar) e ações específicas da tela usando SF Symbols (só o essencial, já que o espaço é limitado).
- Disclosure control ao lado de um título de seção, para revelar mais grupos sob demanda (progressive disclosure aplicado a uma lista de "crates"/grupos).
- List (em vez de grid) recomendada quando o grid ocupa espaço demais para poucos itens e não lida bem com texto mais longo; list é descrita como flexível, altamente usável, familiar, facilita escaneamento rápido, e ocupa menos espaço vertical que imagens (mais itens cabem na tela); template de list vem dos Apple Design Resources.
- Collection (para grandes volumes de imagens: fotos, vídeos, produtos que rolam para fora/dentro da tela): espaçamento consistente entre itens, evitar texto demais sobre eles.
- Quatro temas de agrupamento de conteúdo citados: por tempo (ex.: arquivos recentes, "continuar assistindo"), por sazonalidade/eventos atuais, por progresso (ex.: rascunhos de e-mail, uma aula em andamento), por padrões (relações entre itens, ex.: produtos relacionados).
- Hierarquia visual: tornar o elemento mais importante maior ou com mais contraste para que atraia o olho primeiro; usar estilos de texto do sistema (system text styles) em vez de tamanhos "no olho" ou estilos customizados, porque suportam Dynamic Type e se mantêm legíveis sob diferentes condições (texto mais longo, idiomas diferentes, tamanhos de texto maiores).
- Fundo sutil (gradiente ou blur) atrás de texto sobreposto a imagem, para melhorar legibilidade sem atrapalhar o design.
- Paleta de cores fechada (quatro cores no exemplo) mais algumas formas retrô, aplicadas com regras simples de mix-and-match, para estabelecer estética coesa; fonte mais ousada e expandida para títulos de grupo, distinguindo-os do texto de lista.

Exemplos citados:
- App fictício de coleção de discos de vinil (criado pela autora para a demonstração): usado do início ao fim para ilustrar cada etapa, desde a versão inicial confusa (menu no topo, título como branding, "Records" revelado só no fim na tab bar) até a versão final (tab bar com três seções claras: Records com Add embutido, Swaps, Saves).
- Streaming de vídeo ("continue watching"), rascunhos de e-mail, aula em andamento: exemplos citados de agrupamento por progresso.

Citações curtas:
"Menus can be vague and unpredictable."
"Design is never really finished, and there's no single right answer."

<!-- visual:wwdc2025_359 -->
### O que as imagens mostram
Base: 15 de 15 folhas de quadros vistas, todos os códigos conferidos.

- O marcador de agenda é feito só de tipografia: uma coluna de quatro palavras alinhadas à esquerda, com o tópico atual em preto e mais espesso e os demais em cinza claro fino, sem ícone, numeração ou barra de progresso, cercada de bastante espaço vazio. Ele reaparece nas folhas 0001, 0002, 0004, 0005, 0006, 0007, 0009, 0011 e 0012, e alguns quadros acrescentam um segundo nível de subtítulo, como na folha 0006, onde o item da barra de abas já aparece em cinza e o da barra de ferramentas em preto.
- As perguntas que guiam a sessão aparecem em dois formatos diferentes. Primeiro como tela branca com uma única frase centralizada em negrito na folha 0002, em q0017 e q0018, uma sobre o que a pessoa pode fazer e outra sobre para onde ela pode ir. Depois como anotação aplicada sobre a interface real na folha 0007, onde q0059 aponta uma terceira pergunta, sobre onde a pessoa está, simultaneamente para o título no topo e para a barra de abas no rodapé, e q0060 troca o rótulo pela pergunta de para onde ir, apontando só para a barra de abas.
- O diagnóstico da versão inicial do app é mostrado na própria tela, não descrito em slide: na folha 0003, os quadros q0022 a q0025 mostram um botão de menu sanduíche dentro de um círculo branco translúcido sobreposto à capa de álbum no canto superior esquerdo, e q0026 e q0027 revelam a barra de abas com cinco itens rotulados e o botão central de adicionar elevado num círculo colorido acima da linha dos demais.
- A simplificação da navegação é registrada em etapas, não em um corte único: na folha 0005 a barra vai de cinco itens em q0038 e q0042 para quatro em q0044 e para três em q0045. O quadro q0042 ainda traz uma seta curva saindo de um sinal de mais isolado e pousando sobre a primeira aba, ilustrando para onde a ação foi movida, e q0043 mostra a página real das diretrizes de interface humana no site da Apple, com menu lateral e ilustração de exemplo, aparecendo como referência ao lado dessa mudança.
- A crítica a rótulos e ícones ambíguos ganha uma representação literal na folha 0005: em q0039 a mesma barra de abas mantém texto e posições, mas quatro dos cinco símbolos são trocados por carinhas genéricas, uma delas com expressão de confusão.
- A renomeação aparece como troca controlada de variável: na folha 0006, q0047 e q0048 mostram os mesmos três espaços de aba mudando apenas rótulo e ícone, e q0050 e q0051 colocam as duas telas lado a lado sobre a mesma grade de conteúdo, rotuladas por extenso como versão anterior e versão nova, com a única diferença sendo a barra de abas.
- A anatomia da barra de ferramentas é dissecada com linha fina e rótulo curto na folha 0007: q0056 aponta o título no canto superior esquerdo e q0057 e q0058 apontam o grupo de três ícones de ação no canto superior direito, que inclui adicionar, sincronizar e um menu de reticências.
- A separação de conteúdos misturados aparece como par de estados na folha 0008: q0064 anota duas categorias convivendo na mesma grade, e q0065 mostra a tela já reorganizada com cabeçalho de seção próprio. Em seguida, q0068 mostra a seção reduzida a duas miniaturas com uma seta de revelação ao lado, e q0069 e q0070 mostram a tela cheia resultante, com contagem de itens no topo, enquanto q0071 anota o controle de voltar à esquerda e as ações à direita da nova barra.
- A escolha entre grade e lista é resolvida com comparação direta na folha 0009: q0074 e q0075 mostram a seção em grade de miniaturas quadradas, q0076 mostra a mesma seção convertida em lista de texto com seta de navegação por linha, e q0077 põe as duas versões lado a lado com etiquetas de antes e depois. O quadro q0078 mostra a captura de uma biblioteca de componentes em tema escuro, com modelos de lista, diálogo de permissão e controles de alternância, indicando a origem do componente usado.
- Os temas de agrupamento de conteúdo ganham pictogramas próprios na folha 0010, apresentados um por quadro e só depois reunidos numa linha: calendário para tempo em q0083 e q0084, medidor circular para progresso em q0085, grade de quatro quadrados para padrões em q0086, e os três juntos em preto sólido sobre branco em q0087. Logo em seguida a tela do app mostra uma seção de coleção com dois cartões grandes em gradiente colorido em q0089 e q0090, com o rótulo de coleção apontando para eles, e na folha 0011, em q0092, um indicador de contagem no canto de um desses cartões é anotado como leitura de progresso.
- O problema de hierarquia visual é demonstrado por exagero antes da solução: na folha 0012, q0100 e q0101 mostram a tela com fundo verde limão e o título do álbum em letras enormes atravessando a largura toda, repetido decorativamente ao fundo.
- A tabela tipográfica do sistema aparece completa em q0104 da folha 0012, com cada linha renderizada no próprio estilo que nomeia e o tamanho em pontos declarado: título grande em 34, os três níveis de título em 28, 22 e 20, cabeçalho em 17 semibold, corpo em 17, chamada em 16, subtítulo em 15, nota de rodapé em 13 e as duas legendas em 12 e 11. Na sequência, q0105 aplica esses estilos como anotação sobre uma capa em tela cheia, ligando cada rótulo de estilo ao texto correspondente.
- O limite de legibilidade também é mostrado, não só afirmado: na folha 0012, q0107 e q0108 trazem a mesma tela com título e subtítulo sobre uma ilustração colorida de borboleta e flores, com um dos quadros anotando a camada de fundo e o texto visivelmente disputando contraste com a arte.
- A busca por coerência visual aparece como processo na folha 0013: q0109 e q0110 mostram a lista de grupos ganhando uma miniatura por linha, q0112 e q0113 mostram uma grade densa de dezenas de miniaturas em estilos incompatíveis entre si, misturando fotos de rosto, formas geométricas e ilustrações retrô, e q0114 mostra a tela final com paleta reduzida e formas consistentes.
- As cores do sistema são ensinadas pelo nome de função ligado por linha fina ou ponto de anotação a uma área concreta da tela, em dois diagramas complementares: q0115 na folha 0013 e q0118 na folha 0014 cobrem seis papéis, entre texto, fundo de tela, fundo de linha de lista, separador e cor do item de aba selecionado. Na folha 0014, q0119 e q0120 mostram um mockup em tema escuro onde uma única cor de acento azul percorre botões, seleção e controles, e q0121 fecha com a carta de referência que reúne os quatro níveis de rótulo, cerca de doze pastilhas de cor do sistema e três níveis de fundo, cada bloco duplicado em modo claro e modo escuro.
- O encerramento, na folha 0015, mostra em q0127 e q0128 um mosaico denso de miniaturas da mesma tela do app em dezenas de identidades visuais distintas, com paletas, fundos e tipografias diferentes, em grade regular e sem legenda, e nenhuma miniatura se repete entre os dois quadros.

Proporção visual: a maior parte dos quadros registrados mostra telas do app em moldura de iPhone, slides de tópico, diagramas anotados ou cartas de referência, e a apresentadora sozinha aparece em intervalos curtos entre os blocos, inclusive nos dois últimos quadros da folha 0015.

Divergências ou limites registrados: várias sequências foram anotadas como repetição de enquadramento sem alteração perceptível, incluindo q0011 a q0014 na folha 0002, q0053 e q0054 na folha 0006, q0057 e q0058 na folha 0007, q0093 e q0094 na folha 0011 e q0119 e q0120 na folha 0014. As notas também registram quadros de transição sem conteúdo, como q0016 na folha 0002, e quadros de transição de zoom com silhueta de iPhone sobreposta, como q0113 na folha 0013.
<!-- /visual:wwdc2025_359 -->

## Explore prompt design & safety for on-device foundation models (id: wwdc2025_248, 22.2 min)

- Base: transcrição e 17 de 17 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/248/.
- Tese central: projetar boas experiências com o modelo de linguagem on-device da Apple (Foundation Models framework) exige entender as limitações específicas de um modelo pequeno (cerca de 3 bilhões de parâmetros) e aplicar uma abordagem de segurança em camadas, já que nenhuma camada isolada é suficiente.

Este vídeo é sobre engenharia/prompt design para IA generativa, com implicações diretas de design de produto e UX de segurança, não sobre construção visual de interface tradicional.

O processo de design que a Apple descreve:
1. Entender as limitações do modelo on-device antes de desenhar a funcionalidade (tarefas que exigem raciocínio complexo devem ser quebradas em passos simples; evitar usá-lo como calculadora ou gerador de código; ter cuidado com conhecimento de mundo limitado e data de corte de treinamento).
2. Escrever prompts como comandos claros, dar poucos exemplos (menos de cinco) diretamente no prompt quando necessário, usar comandos em caixa alta tipo "DO NOT" para reforçar restrições.
3. Usar "instructions" (prompt especial que define como o modelo deve se comportar para todos os prompts subsequentes) separadamente de prompts vindos de pessoas usando o app.
4. Camada de segurança: prompt design é a primeira ferramenta; depois vêm os guardrails nativos do framework (aplicados tanto à entrada quanto à saída do modelo); depois instruções de segurança escritas pelo desenvolvedor; depois controle de como a entrada da pessoa é incluída nos prompts; por fim, mitigações específicas do caso de uso.
5. Avaliação e teste: curar datasets de qualidade e de segurança, cobrindo os principais casos de uso do app e também prompts que podem gerar problemas de segurança; automatizar a execução ponta a ponta; inspecionar manualmente datasets pequenos ou usar outro LLM para avaliar em escala; testar também o "caminho infeliz" (unhappy path) de erros de segurança.

Princípios enunciados e o porquê:
- O modelo on-device é otimizado e comprimido para caber no bolso (cerca de 3 bilhões de parâmetros), muito menor que modelos de servidor com centenas de bilhões de parâmetros; por isso não faz tudo que um LLM grande faz.
- O modelo tem conhecimento de mundo limitado e pode alucinar (inventar respostas completamente) para o que não sabe; em lugares onde fatos são críticos (como instruções), não se deve arriscar alucinações que possam enganar as pessoas. Para gerar fatos, fornecer informação verificada escrita no próprio prompt, e checar cuidadosamente as saídas para qualquer prompt novo.
- O nível de conhecimento impreciso pode ser aceitável em alguns contextos (ex.: diálogo de personagens num jogo de padaria) mas não em outros (uma enciclopédia de bagels).
- O modelo obedece instructions com precedência sobre prompts; por isso instructions são um ótimo lugar para melhorar a segurança das respostas, mas instructions devem vir só do desenvolvedor, nunca de conteúdo não confiável ou entrada do usuário; entrada do usuário deve ir em prompts, não em instructions.
- Camadas de segurança funcionam como fatias de queijo suíço: cada camada tem buracos, mas um problema só passa se os buracos de todas as camadas se alinharem ao mesmo tempo.
- Para uma funcionalidade proativa (não iniciada por ação do usuário), um erro de segurança pode simplesmente ser ignorado sem interromper a UI; para uma funcionalidade iniciada pelo usuário, é preciso dar feedback de UI apropriado explicando que o app não pode processar o pedido, possivelmente com ações alternativas.

Técnicas concretas de construção de interface (com exemplos de prompt):
- Controlar o tamanho da saída ("in three sentences", "in a few words" para encurtar; "in detail" para alongar).
- Controlar estilo e voz especificando um papel/role no prompt (exemplo: "a fox who speaks Shakespearean English").
- Guided generation: dá controle sobre o que o modelo deve gerar (strings, números, arrays, ou estrutura de dados customizada), melhorando confiabilidade.
- Xcode Playgrounds (#Playground): forma recomendada de experimentar prompts, com resposta aparecendo imediatamente no canvas.
- Três padrões para incluir entrada do usuário num prompt, do mais arriscado ao mais seguro: (1) usar a entrada do usuário diretamente como prompt (mais flexível, mais risco, exige instruções cuidadosas para lidar com ampla variedade de entradas); (2) combinar prompt próprio do app com a entrada do usuário; (3) oferecer uma lista de prompts pré-definidos para a pessoa escolher (menos flexível, mas controle total sobre o prompt, permitindo curar o que realmente funciona bem com o modelo).
- Mitigação de caso de uso: exemplo do app de sabores de bagel, alertar sobre alérgenos na UI, ou adicionar configurações de restrição alimentar para filtrar receitas; exemplo de app de trivia, adicionar instruções extras ou uma lista de palavras-chave proibidas, ou treinar um classificador para uma solução mais robusta.

Exemplos citados:
- App de diário (diary app): instructions definem o modelo como assistente que ajuda a escrever entradas de diário fazendo perguntas; demonstra tanto o uso de instructions quanto o risco de segurança quando a entrada da pessoa vira prompt diretamente.
- Gerador de sabores de bagel: ilustra tanto limitação de conhecimento de mundo (descrição incorreta de bagel simples) quanto mitigação de risco de alergia.
- Image Playground: citado como exemplo de UI que oferece "desfazer" o prompt que causou um erro de segurança.
- App de trivia (fictício): ilustra mitigação de tópicos controversos ou inadequados para a audiência.

Citações curtas:
"Prompts impact safety."
"You can imagine the layers as a stack of Swiss cheese slices."

<!-- visual:wwdc2025_248 -->
### O que as imagens mostram
Base: 17 de 17 folhas de quadros vistas, todos os códigos conferidos.

- Quase todos os slides de conteúdo repetem um único template, da folha 0001 até a 0017: título em preto forte alinhado à esquerda no topo, subtítulo secundário em cinza claro logo abaixo, e itens de lista surgindo um por quadro em coluna única, sem numeração, sobre fundo cinza claro. O subtítulo é o que muda entre slides vizinhos, mantendo o título fixo, como acontece na folha 0004, onde o mesmo cabeçalho troca de tema e reinicia a lista vazia em q0032.
- Muitos blocos de afirmação carregam um selo de estado no canto superior direito, funcionando como semáforo: círculo laranja com exclamação para risco e círculo verde com check para uso aprovado. Ele aparece nas folhas 0004, 0005, 0006, 0007, 0011, 0013 e 0016, e está ausente em outras, como as folhas 0010 e 0014. O acendimento é visível quadro a quadro na folha 0004, onde o ícone passa de apagado em q0028 para laranja aceso em q0029, junto com o primeiro item da lista.
- O diagrama de fluxo do modelo é o mesmo desenho reaproveitado e ampliado ao longo da sessão: uma caixa de texto de entrada, seta colorida, um ícone quadrado de nós conectados representando o modelo, e uma caixa de saída. Na folha 0002 ele aparece primeiro com a saída vazia e um cursor piscando em q0013, depois preenchida em q0015, e em q0016 o mesmo desenho serve a outro caso de uso, com entrada e saída de reescrita de tom.
- Esse mesmo diagrama cresce para explicar a diferença entre instrução e prompt na folha 0008: q0068 mostra só a caixa de instrução ligada ao modelo, q0070 acrescenta abaixo uma segunda linha com a caixa de prompt e sua saída, e q0071 empilha três linhas, a instrução e dois prompts diferentes, cada linha com seu próprio ícone de modelo e sua própria resposta.
- A diferença de escala entre modelos é mostrada como visualização de área na folha 0003: em q0025 e q0026 dois círculos proporcionais aparecem lado a lado, o grande em roxo claro rotulado como modelo de servidor acima de cem bilhões de parâmetros e o pequeno em roxo escuro rotulado como modelo no dispositivo com três bilhões, cada um com bolinha indicadora de cor.
- A origem da entrada é marcada graficamente: a partir da folha 0009, o prompt que vem de uma pessoa usando o app ganha ao lado uma silhueta humana preta e minimalista, vista em q0076, recurso que não existia nos diagramas anteriores em que o prompt vinha do desenvolvedor. O mesmo ícone volta na folha 0012, em q0104, ligando o pedido do usuário à resposta empática do modelo.
- A progressão de risco no código é ensinada por três blocos consecutivos com o mesmo selo de estado, na folha 0013: q0110 mostra a entrada do usuário virando prompt diretamente, com alerta laranja, q0111 mostra a entrada interpolada dentro de um prompt fixo, ainda com alerta, e q0112 mostra uma enumeração com casos nomeados alimentando o prompt, agora com check verde.
- A edição de instruções é mostrada como diferença entre dois quadros na folha 0012: q0103 traz a caixa de instrução original e q0104 traz a mesma caixa com uma linha extra acrescentada, destacada com fundo azul claro dentro do bloco de código, seguida do efeito dela na resposta gerada.
- O diagrama de proteção usa código de cor próprio e cresce entre folhas: na folha 0010, q0090 mostra um balão vermelho com símbolos de palavrão, seta até um cadeado laranja e seta até um cartão rosa claro de violação, em sequência linear. Na folha 0011, q0091 reposiciona o modelo ao centro e coloca um cadeado antes e outro depois dele, tornando visível que a checagem ocorre na entrada e na saída.
- A única captura real de ferramenta está na folha 0007, em q0060 a q0062: o Xcode com painel de código à esquerda e canvas de resultado à direita, o canvas dividido em blocos colapsáveis de sessão, resposta, prompt e conteúdo, um ícone de olho ao lado do campo de conteúdo para expandir a string, a resposta gerada dentro de um cartão claro em fonte serifada e uma marca de duração da execução. O quadro q0061 mostra duas janelas lado a lado e q0062 as mesmas janelas levemente reposicionadas.
- A única captura de app real está na folha 0011, em q0096: um iPhone em tema escuro com barra de status, botão de fechar, a mensagem de erro centralizada sugerindo descrever outra coisa, um botão de desfazer e uma fileira de sugestões com avatares circulares coloridos abaixo. É o tratamento de erro mostrado em layout real, não em esquema.
- O tratamento de erro também aparece como classificação em slide, na folha 0011: q0093 traz só a categoria de funcionalidade proativa e q0095 acrescenta a categoria iniciada pelo usuário, montando o par em dois quadros.
- Um único momento da sessão abandona o estilo chapado dos slides: a folha 0005 traz ilustração em pixel art de um personagem diante de um balcão de padaria em q0038 e, em q0039, acrescenta o balão de fala em pixel art e o check verde, sinalizando visualmente que esse é o cenário tolerante a erro.
- O resumo de segurança vira um cartão composto na folha 0015, em q0127: um bloco com ícone de engrenagens reunindo as mitigações de responsabilidade do app em dois botões cinza em formato de chip, e abaixo outro bloco com o ícone do modelo e um botão laranja sólido para as proteções nativas, com a diferença de cor separando o que é do desenvolvedor do que vem pronto.
- O encerramento tem duas marcas visuais próprias: na folha 0016 a lista final cresce de um item em q0141 para cinco itens em q0143, reunindo num só lugar pontos já vistos em slides anteriores, e na folha 0017 o slide de recursos troca o fundo cinza chapado por uma fotografia real de bancada de madeira com um iPhone físico e fatias de queijo suíço, com a lista de recursos em texto simples sobre a foto, fechando em q0149 com uma sobreposição roxa translúcida sobre a cena ao vivo.

Proporção visual: a maior parte dos quadros mostra slides de texto, diagramas esquemáticos e blocos de código Swift, com apenas duas sequências de captura real, a do ambiente de desenvolvimento na folha 0007 e a do app na folha 0011, e as apresentadoras aparecendo em planos curtos intercalados entre os blocos.

Divergências ou limites registrados: as notas apontam que a metáfora das camadas de queijo suíço citada na fala não aparece ilustrada em nenhum quadro, e que as fatias de queijo do slide final da folha 0017 são elemento decorativo de fotografia, possivelmente uma referência tardia, sem o diagrama de camadas descrito verbalmente. Também há várias repetições de quadro quase idênticas anotadas, em q0025 e q0026 na folha 0003, q0065 e q0066 na folha 0008, q0074 e q0075 na folha 0009, e q0112 e q0113 na folha 0013.
<!-- /visual:wwdc2025_248 -->

## What's new in Xcode 26 (id: wwdc2025_247, 36.9 min)

- Base: transcrição e 29 de 29 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2025/247/.
- Tese central: o Xcode 26 traz ganhos de performance e tamanho de download, além de novas ferramentas de produtividade (Playgrounds inline, Icon Composer integrado, assistente de código com LLMs) e de depuração/performance/testes que, juntas, aceleram o ciclo de desenvolvimento.

Este vídeo é um resumo de ferramenta de desenvolvimento (Xcode), não um vídeo de metodologia de design de interface; é incluído aqui porque faz parte do grupo indicado, e traz duas seções com relevância direta a design de interface: Icon Composer e o framework de código assistido por IA (uso de imagens/sketches para gerar UI).

O processo/fluxo que a Apple descreve nas partes relevantes a design:
- Icon Composer (mencionado en passant, com detalhe completo no vídeo dedicado id wwdc2025_361): app empacotado com o Xcode 26 para criar ícones multi-camada com efeitos de material em um único arquivo, cobrindo modos claro, escuro e tinted, além do novo visual do watchOS.
- Assistente de código com LLMs: pode receber imagens (sketches de UI) como anexo à consulta, já que muitos LLMs conseguem gerar código a partir de um esboço de interface.

Técnicas concretas de construção de interface citadas:
- String Catalogs: geração automática de comentários de contexto para tradutores, usando o modelo on-device para analisar onde e como uma string localizada é usada no projeto.
- Voice Control em "Swift mode": permite escrever código Swift falando naturalmente, com o sistema entendendo sintaxe Swift (espaçamento, operadores, camelCase); demonstrado adicionando um campo ao inspector de "landmark" para "continent".
- Playground (#Playground macro): permite iterar em qualquer código (não só UI) com resultados aparecendo no canvas; usado no vídeo para depurar um bug de coordenadas erradas num mapa, revelando que uma regex não capturava corretamente o sinal de menos (longitude negativa), colocando o Grand Canyon no lugar errado.
- Assistente de código (integração com ChatGPT, Claude 4 Opus e Sonnet, ou modelos locais via Ollama/LM Studio): pode referenciar símbolos com "@", anexar arquivos e imagens à consulta, aplicar mudanças automaticamente ou pedir revisão antes, e manter contexto de conversa entre mensagens sucessivas (usado para adicionar um recurso de avaliação por estrelas a "landmark collections", incluindo ajustar a UI para exibir as estrelas).
- UI automation recording: grava interações reais no simulador e gera código de teste automaticamente; Automation Explorer no relatório de teste permite inspecionar atributos de cada elemento identificável após a falha de um teste (exemplo: um TextField esperado que na verdade virou um TextView por suportar múltiplas linhas).

Nota de honestidade: como este vídeo é majoritariamente sobre ferramentas de desenvolvimento (performance de build, debugger, Instruments, testes), a maior parte do conteúdo não trata de "design de interface" no sentido do briefing deste grupo; o cartão acima cobre apenas os trechos com relevância direta a construção de UI ou fluxo de design assistido por IA. Números de performance (ex.: "24% smaller", "40% faster to load a workspace", "up to 50%" de latência de digitação, "up to 16 times faster" em Lists) aparecem no texto mas dizem respeito a performance de ferramenta, não a técnicas de interface, por isso não foram detalhados aqui.

Exemplos citados:
- App Landmarks (sample project): usado ao longo do vídeo para demonstrar Playgrounds, Voice Control, e o assistente de código adicionando avaliação por estrelas.

Citações curtas:
"With Icon Composer, you can create beautifully designed, sophisticated, multi-layered icons that work across multiple platforms and software versions."
"Images are especially useful, since many large language models can generate code from just a sketch of a user interface."

<!-- visual:wwdc2025_247 -->
### O que as imagens mostram
Base: 29 de 29 folhas de quadros vistas, todos os códigos conferidos.

- A lista lateral de tópicos da sessão funciona como barra de progresso do talk inteiro e usa hierarquia só por peso e cor de fonte: item ativo em preto bold, demais em cinza claro. Ela aparece já na abertura e troca de item entre quadros vizinhos (folha 0001, q0005 para q0006), ganha um segundo nível com subitens quando o tópico se subdivide (folha 0002, q0012 para q0013) e reaparece a cada virada de assunto (folha 0021, q0188; folha 0023, q0204), inclusive logo depois da troca de apresentador, quando o segundo apresentador entra já com o tópico seguinte em destaque (folha 0014, q0118 para q0119).
- Números viram tela inteira: um quadro vazio antecede o dado, que entra sozinho em tipografia grande sem nenhum outro elemento. O quadro que antecede é branco na abertura, com "Xcode is 24% smaller." (folha 0001, q0008 para q0009), e cinza claro antes do dado sobre carregamento de workspace (folha 0002, q0010 para q0011). O mesmo tratamento isolado é dado a um nome de recurso, "String Catalogs" (folha 0008, q0066).
- A composição dominante das capturas é três zonas fixas: navegador de arquivos ou painel de chat à esquerda, editor de código ao centro, preview de iPhone ou painel de resultado à direita. Ela se repete em quase todas as folhas de 0002 a 0015, e a síntese das notas registra que a fala nunca nomeia essa estrutura, falando apenas em editor e preview (folha 0010, q0082; folha 0011, q0099).
- O Icon Composer aparece com anatomia de app de design em três colunas: painel de camadas à esquerda, preview central do ícone e painel de propriedades à direita com controles nomeados de material e valores percentuais, entre eles blur, translucidez, specular e sombra (folha 0007, q0056). Em seguida a mesma tela dá lugar a uma grade de comparação com plataformas nas linhas e modos de aparência nas colunas, mostrando que o mesmo ícone gera até seis variações e que o watchOS tem só uma (folha 0007, q0058 a q0060).
- Pares de antes e depois aparecem na própria edição ao vivo: o preview do iPhone não tem o campo de continente e passa a ter depois que o bloco condicional se completa no código (folha 0004, q0031 para q0032); e a fileira de estrelas do preview aumenta quando o intervalo do laço muda no código, com o rótulo de acessibilidade acompanhando a contagem (folha 0011, q0095 para q0096).
- O realce de fundo sobre o texto é o jeito recorrente de dizer "isto importa aqui", com cores diferentes por finalidade: amarelo para termos de busca dentro do código (folha 0003, q0022) e azul para a seleção feita por voz (folha 0004, q0029). No resultado da expressão regular a marcação muda de forma, não é fundo colorido no código e sim um selo de correspondência ao lado do valor numérico extraído, dentro do canvas (folha 0006, q0049 a q0051).
- O azul marca o que está selecionado ou ativo em contextos completamente diferentes: trilha de timeline (folha 0019, q0164), opção de menu suspenso (folha 0017, q0150), trecho de chamada de API dentro do código (folha 0027, q0239 para q0240) e opção escolhida em menu de configuração, ali acompanhada de checkmark (folha 0028, q0247). O tom varia conforme o contexto, sólido na trilha da timeline e claro no trecho de código.
- O canvas do playground mostra resultado como árvore de propriedades expansível ao lado do código, e valores de tipo especial trazem visualização embutida em vez de texto: a propriedade de coordenada abre um mapa em miniatura com pino, e uma segunda linha de código faz surgir um segundo mapa, mais amplo, abaixo do primeiro (folha 0005, q0043 a q0045; folha 0006, q0047).
- A correção de erro segue a mesma coreografia de três passos nas folhas 0012, 0013 e 0015, visível na comparação entre quadros: erro sublinhado em vermelho ou em popup sobre a própria linha, depois um botão de ação nomeado para aquele erro específico, depois o estado já corrigido. Aparece com "Generate Fix for Issue" (folha 0012, q0106 para q0107), cujo resultado corrigido só se vê na folha seguinte, no arquivo com o enum ajustado (folha 0013, q0110), e com "Add NSCameraUsageDescription", que leva ao editor de capacidades, onde um campo obrigatório vazio fica com aviso amarelo, é preenchido e perde o aviso, e o texto digitado reaparece literalmente no popup de permissão do sistema no preview do iPhone (folha 0015, q0127 a q0134).
- O painel de assistente tem anatomia própria: histórico de conversa em lista vertical, popup de ações rápidas ancorado ao campo de texto com quatro opções (folha 0009, q0074 para q0075), respostas estruturadas em passos numerados por arquivo com rodapé contando o alcance da mudança, "4 Changes in 3 Files" (folha 0010, q0090), botões de cancelar e restaurar para andar pelo histórico de versões do código (folha 0012, q0100 para q0101) e a possibilidade de colapsar o painel a uma faixa estreita para devolver espaço ao editor e ao preview (folha 0011, q0096 para q0099).
- Existe um slide de ficha técnica padronizado: título em negrito grande, subtítulo cinza menor quando há, lista de frases curtas em peso normal e, no rodapé separado por linha fina, o nome da sessão de referência à esquerda e o ano do evento à direita. Ele aparece assim nas folhas 0020 (q0175), 0022 (q0193) e 0027 (q0236 a q0238). O mesmo desenho de título mais lista curta aparece sem rodapé de referência no slide do Processor Trace (folha 0017).
- Esses slides são construídos por camadas, não de uma vez: o título entra sozinho, os itens aparecem depois e o rodapé de referência entra por último (folha 0027, q0236 para q0237 para q0238). No slide de encerramento o título também entra sozinho, mas os itens e o rodapé de links chegam juntos no quadro seguinte (folha 0028, q0250 para q0251).
- Em quase todo tópico novo, antes da captura real da ferramenta, entra um ícone ou diagrama esquemático simples com rótulo: lupa sobre chip para "Processor Trace" (folha 0016, q0141), três ícones quadrados de estágio de build em fileira (folha 0022, q0191), três ícones conectados por linhas retas para otimização de CPU (folha 0018, q0160) e engrenagens duplas em traço preto para segurança (folha 0023). Só depois a janela real aparece.
- As janelas do Instruments compartilham uma composição fixa, timeline colorida por trilha no topo e tabela de dados embaixo, repetida em quatro instrumentos diferentes (folha 0016, q0143; folha 0017, q0152 a q0153; folha 0019, q0163; folha 0019, q0170), enquanto os painéis de configuração usam o mesmo bloco de formulário com nome à esquerda, controle à direita e texto explicativo em cinza menor abaixo, também em editores de função muito distinta (folhas 0017, 0023 e 0028).
- Dados de diagnóstico vêm embalados em cartão: popover branco de cantos arredondados com sombra, texto curto e gráfico de barras em miniatura embutido (folha 0021, q0181), e gráfico de barras por versão do app com a barra atual em azul escuro mais um tooltip de recomendação em dois níveis, valor em destaque e origem em cinza menor (folha 0021, q0184 a q0187).
- A gravação de teste de interface é mostrada como par sincronizado: simulador à direita, editor à esquerda, e cada interação na tela faz nascer uma linha nova de código, passo a passo (folha 0024, q0211 a q0216). A barra de status do editor é o indicador de estado que muda de texto ao longo do processo, algo que só a leitura dos quadros em sequência revela (folha 0025, q0220 para q0224).
- A falha de teste é examinada num explorador com lista de eventos à esquerda, linha de falha em fundo vermelho claro com o erro detalhado, e um popover que abre sobre o vídeo do simulador trazendo o tipo real do elemento e o trecho de código sugerido (folha 0026, q0232 para q0233).

Proporção visual: das 29 folhas, apenas a última é só apresentador; o corpo do vídeo alterna slides de texto, ícones e diagramas com capturas reais de Xcode, Instruments, Organizer e simulador, e o apresentador aparece sobretudo nas viradas de tópico, às vezes reduzido a um recorte de vídeo arredondado no canto da tela de código (folha 0004, q0028).

Divergências ou limites registrados: as notas marcam quadros praticamente idênticos, sem mudança perceptível, em vários pontos (folha 0017, q0150 para q0151; folha 0019, q0170 para q0171; folha 0022, q0191 para q0192; folha 0021, q0184 a q0186); um quadro com ícone sobreposto ao código é descrito como parcialmente legível (folha 0010, q0087); e o esmaecimento de tela cheia usado entre transições é atribuído à edição do vídeo, não à interface do produto (folhas 0016 a 0021 e folha 0026).
<!-- /visual:wwdc2025_247 -->

## O que este grupo revela sobre o jeito Apple

- Liquid Glass, o novo material adaptativo introduzido em 2025, permeia praticamente todo o grupo (ids wwdc2025_361, wwdc2025_337, wwdc2025_323, wwdc2025_284, wwdc2025_208) como o fio condutor do redesenho de interface deste ciclo: ícones, símbolos, controles do SwiftUI e do UIKit, e até o ponteiro do iPad recebem a mesma linguagem de material translúcido, dinâmico, que reage a interação e à luz do conteúdo abaixo.
- Há uma disciplina recorrente de separar "o que é desenhado" de "o que é computado depois": ícones devem ser exportados chatos e opacos, com efeitos de glass aplicados no Icon Composer (id wwdc2025_361); símbolos são desenhados como formas com contorno, não apenas traços, para permitir controle fino de animação depois (id wwdc2025_337). O sistema separa consistentemente a arte-fonte da camada de comportamento dinâmico.
- Convergência entre SwiftUI e UIKit é explícita e paralela: os vídeos id wwdc2025_323 e id wwdc2025_284 cobrem essencialmente os mesmos conceitos (tab bars flutuantes, toolbars com glass, sheets adaptativas, GlassEffectContainer/UIGlassContainerEffect) com API própria para cada framework, sinalizando que a Apple trata os dois frameworks como peers de primeira classe neste redesenho.
- Regra recorrente de "não escondê-lo, esmaecê-lo": tanto no menu bar do iPad (id wwdc2025_208) quanto implicitamente na filosofia de UI writing (id wwdc2025_404) e na tese de clareza (id wwdc2025_359), a Apple prioriza previsibilidade espacial e cognitiva sobre economia de espaço: itens inativos ficam visíveis e esmaecidos, telas sempre respondem "onde estou / o que posso fazer / para onde vou".
- O grupo mistura sessões de design de interface tradicional com sessões mais técnicas de engenharia (visionOS/Houdini id wwdc2025_305, formatos de vídeo id wwdc2025_304, layout 3D no SwiftUI id wwdc2025_273, Foundation Models id wwdc2025_248, Xcode id wwdc2025_247) mas todas compartilham a mesma postura: otimizar radicalmente em função de como a pessoa realmente vai experimentar o produto (o Immersive Boundary no id wwdc2025_305, a atenção a movimento de câmera no id wwdc2025_304, a limitação de conhecimento do modelo on-device no id wwdc2025_248).
- O tema espacial (visionOS) aparece em três vídeos distintos com abordagens complementares: otimização de geometria/textura (id wwdc2025_305), formatos e apresentação de vídeo (id wwdc2025_304), e layout declarativo 3D no SwiftUI (id wwdc2025_273), juntos formam uma cobertura relativamente completa de como a Apple pensa profundidade e espaço como dimensão de design, não só de engenharia gráfica.
- Escrita e clareza de conteúdo recebem tratamento equivalente ao visual: o vídeo de UX writing (id wwdc2025_404) e o de fundamentos de design (id wwdc2025_359) tratam texto, hierarquia e estrutura de informação como parte do mesmo processo de design, não como etapa separada ou secundária.

## Sem transcrição

Nenhum dos 12 arquivos deste grupo ficou sem transcrição; todos continham título, fonte, duração, descrição e a transcrição falada completa.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_361.md, 60 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_337.md, 99 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_305.md, 108 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_404.md, 64 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_304.md, 80 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_323.md, 85 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_208.md, 78 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_284.md, 94 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_273.md, 69 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_359.md, 81 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_248.md, 88 linhas lidas, sim, até o fim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2025_247.md, 120 linhas lidas, sim, até o fim.

Nenhum arquivo foi truncado pela ferramenta Read; todos couberam integralmente numa única leitura (o maior tinha 120 linhas, bem abaixo do limite padrão de 2000 linhas).
