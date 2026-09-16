# ess-14

Lote de vídeo. Fontes: wwdc2026_322 (13 folhas de quadros) e wwdc2026_8012 (43 folhas de quadros).

## O estado atual é marcado por peso e cor, e tudo que não é o foco esmaece

- Evidência: wwdc2026_322 (folha 0004, q0029, q0030 e q0033; folha 0009, q0074, q0079 e q0080; folha 0012, q0107: item ativo da lista em branco negrito e os demais em cinza esmaecido, com o destaque avançando de item em item)
- Evidência: wwdc2026_322 (folha 0010, q0082 para q0083 e q0084: a transcrição sai de negrito uniforme em todas as linhas para só a primeira em preto negrito e as outras em cinza claro)
- Evidência: wwdc2026_8012 (folhas 0002 e 0003, q0022 e q0023: linha selecionada da árvore de camadas com destaque azul e o elemento correspondente no canvas com contorno azul; folha 0021, q0181 e q0186 a q0188: menu de Blend Mode com marca de seleção no item ativo e destaque azul no item sob o cursor)
- O que isso ensina sobre construir interface: seleção e foco não precisam de rótulo, bastam duas variáveis já disponíveis, peso da fonte e saturação, aplicadas de forma consistente. E o destaque vem sempre acompanhado do rebaixamento do resto, não sozinho.

## Parâmetro e resultado moram no mesmo quadro, e a diferença fica visível entre quadros vizinhos

- Evidência: wwdc2026_322 (folha 0004, q0031 para q0032: a capa em gradiente passa de nítida a desfocada quando o modificador de blur com raio 30 entra no código; folha 0008, q0067 para q0068 e q0070 a q0072: primeiras manchas onduladas quando o cálculo de offset entra, depois manchas mais largas e contrastadas com a segunda amostragem deslocada; folha 0011, q0095 para q0096 e q0097: o valor no closure muda de base para topo e a etiqueta no diagrama isométrico muda de posição)
- Evidência: wwdc2026_8012 (folha 0005, q0037 a q0042: o cursor percorre o controle de refração e as pétalas do ícone vão de bordas suaves a bordas cada vez mais onduladas; folha 0006, q0046 a q0048: o sub-item Chromatic da sombra é editado enquanto o brilho ao redor das bordas fica mais visível)
- O que isso ensina sobre construir interface: quem ajusta um valor precisa ver o efeito sem trocar de tela nem esperar. Colocar controle e resultado no mesmo campo de visão transforma parâmetro abstrato em relação observável.

## O rótulo na tela carrega vocabulário que a fala não pronuncia

- Evidência: wwdc2026_322 (folha 0003, q0019 a q0024: as caixas do pipeline trazem nomes de etapa como "Shader effects" e "Timeline input", legendas técnicas ausentes da narração naquele trecho)
- Evidência: wwdc2026_8012 (folhas 0002 a 0007: as imagens mostram os nomes exatos e a ordem fixa dos campos do inspetor, que a fala trata em termos gerais; folha 0007, q0055 e q0056: painel flutuante de aparência com alternância clara e escura, interruptor de tonalização e barra de gradiente, componente que a narração não descreve)
- O que isso ensina sobre construir interface: a nomenclatura visível é a documentação real do produto. Se o nome do campo estiver errado ou vago, nenhuma explicação verbal em volta conserta, porque é o rótulo que a pessoa vai repetir depois.

## O mesmo artefato é mostrado dentro de várias molduras, lado a lado ou em sequência

- Evidência: wwdc2026_322 (folha 0012, q0104: a tela final com transcrição, timestamp e controles aparece replicada em iPad ao lado do iPhone)
- Evidência: wwdc2026_8012 (folha 0006, q0049 a q0054: o mesmo ícone em moldura quadrada arredondada, moldura circular, de volta à quadrada, versão colorida sobre fundo escuro e versão monocromática sobre fundo claro; folha 0040, q0356 a q0359: o ícone do app de mapas como quadrado com guia de corte circular, depois como círculo cheio com o marcador recentralizado, depois de volta ao quadrado)
- O que isso ensina sobre construir interface: um componente só está pronto quando sobrevive a mais de um recorte. Testar a mesma peça em molduras diferentes revela cedo o que depende do enquadramento e o que precisa ser recentralizado.

## Efeito e propriedade pertencem a um nível da hierarquia, e a diferença de nível é ensinada graficamente

- Evidência: wwdc2026_322 (folha 0005, q0043 a q0045, contra folha 0006, q0049 e q0050: o efeito por pixel liga um ponto de entrada a um ponto de saída, enquanto o efeito de camada delimita um quadrado maior de região amostrada ligado por seta a um pixel de saída; folha 0010, q0087 a q0089: dois retângulos laranja rotulados como view container e subview ganham uma linha pontilhada central comum)
- Evidência: wwdc2026_8012 (folha 0003, q0022 a q0027: com o grupo selecionado o inspetor mostra a seção de vidro com modo, especular, desfoque, refração, translucidez e sombra; com a camada selecionada mostra opacidade, mistura, preenchimento, o interruptor que decide se aquela camada recebe o efeito, a imagem de origem e o layout)
- O que isso ensina sobre construir interface: decidir em que nível cada propriedade vive é decisão de arquitetura, não de painel. Material e efeito no grupo, cor e participação na camada, e a interface deve deixar esse limite óbvio ao trocar o que exibe conforme a seleção.

## A anotação é sobreposta ao próprio objeto, não colocada como legenda ao lado

- Evidência: wwdc2026_322 (folha 0005, q0041 a q0045: caixas de rótulo amarelas e setas ligando pixel de entrada a pixel de saída direto sobre a grade de pixels azul; folha 0010, q0088 e q0089: linha pontilhada de alinhamento traçada por cima dos dois retângulos; folha 0011, q0093: etiquetas laranja de topo e base encostadas na subview em perspectiva)
- Evidência: wwdc2026_8012 (folha 0040, q0356: guia circular tracejada desenhada por cima do ícone quadrado para indicar a área de corte; folhas 0002 a 0006: contorno azul de seleção desenhado ao redor do elemento no canvas)
- O que isso ensina sobre construir interface: medida, limite e área de corte devem ser desenhados em cima do elemento, na mesma escala dele. Legenda separada obriga o olho a ir e voltar e perde a correspondência exata.

## O enquadramento se fecha sobre o detalhe para inspecionar material e acabamento

- Evidência: wwdc2026_322 (folha 0003, q0026 para q0027: uma vinheta circular escura emoldura o preview do resultado e se fecha mais entre um quadro e o seguinte; folhas 0002 e 0003: lentes circulares acopladas ao cano mostram miniatura do conteúdo naquele ponto exato do fluxo)
- Evidência: wwdc2026_8012 (folha 0004, q0031, e folha 0006, q0046 a q0048: o zoom do canvas sobe bem acima do tamanho natural para conferir contorno de seleção e brilho de sombra nas bordas das pétalas)
- O que isso ensina sobre construir interface: ampliação aqui é instrumento de conferência, não de navegação. Detalhe de borda, brilho e sombra precisam de uma escala de inspeção própria, maior do que a de uso.

## Translucidez e desfoque só aparecem por cima de conteúdo colorido de verdade

- Evidência: wwdc2026_8012 (folha 0007, q0057 para q0058: o fundo do canvas troca de cinza sólido para uma imagem em gradiente colorido ocupando toda a área, e o ícone passa a mostrar a refração do fundo através do material, com a barra de ferramentas ganhando controles extras de pré-visualização; volta ao cinza em q0061)
- Evidência: wwdc2026_322 (folha 0012, q0100 a q0102: os controles de reprodução translúcidos ficam sobre fundo em gradiente colorido com a transcrição sobreposta; folha 0004, q0032: o desfoque é demonstrado sobre a imagem de capa em gradiente, não sobre superfície lisa)
- O que isso ensina sobre construir interface: material translúcido é invisível contra fundo neutro. O teste válido é contra o conteúdo real e variado que vai passar por baixo, e vale ter esse fundo disponível na própria ferramenta.

## A troca de contexto é sinalizada por uma transição explícita, esmaecimento ou tela neutra

- Evidência: wwdc2026_322 (folha 0001, q0004; folha 0002, q0011; folha 0004, q0034; folha 0012, q0108: telas brancas vazias separam blocos)
- Evidência: wwdc2026_8012 (folhas 0002, 0007, 0021 e 0022: nas quatro entradas e saídas de tela do primeiro bloco os apresentadores aparecem parcialmente transparentes atrás do ícone ampliado; folha 0028, q0244 a q0247, e folha 0030, q0264 a q0267: o cartão de pergunta entra e sai por esmaecimento gradual, visível quadro a quadro; folha 0040, q0359: saída por esmaecimento simples)
- O que isso ensina sobre construir interface: mudança de contexto merece um quadro próprio. Um estado intermediário curto, neutro ou semitransparente, evita o corte seco que faz a pessoa perder de onde veio.

## Cada parte ganha nome próprio, e a nomeação é a estrutura visível

- Evidência: wwdc2026_322 (folha 0002, q0016 a q0018: o cano de entrada rotulado como interface original abre em três saídas com preview próprio; folha 0003, q0019 a q0024: cada caixa do pipeline nomeia a transformação que aplica)
- Evidência: wwdc2026_8012 (folhas 0002, 0003, 0004 e 0006: camadas nomeadas uma a uma dentro de grupos aninhados, com indentação marcando o nível; folha 0040: as camadas do arquivo do app de mapas são nomeadas por função e destino, com sufixos indicando a variante de relógio)
- O que isso ensina sobre construir interface: hierarquia legível vem de nomes específicos mais indentação, não de ícones. Nome que diz função e destino permite entender o arquivo sem abrir cada camada.

## A mesma estrutura se repete sem variação do começo ao fim, e é isso que torna a leitura barata

- Evidência: wwdc2026_322 (folhas 0002 e 0003: notação estável o vídeo inteiro, lente circular igual a estado do dado, caixa retangular igual a transformação, bifurcação em Y igual a branch, cruzamento em X igual a merge; folhas 0004, 0006 a 0010: sempre bloco de código de um lado e mockup de iPhone do outro)
- Evidência: wwdc2026_8012 (folhas 0002 a 0007, 0021, 0022 e 0040: sempre o mesmo layout de três painéis, árvore de camadas à esquerda, canvas ao centro, inspetor à direita, em todas as folhas em que o aplicativo aparece)
- O que isso ensina sobre construir interface: fixar o gabarito e mudar só o conteúdo faz o custo de leitura cair a cada repetição. O vocabulário gráfico funciona como API, muda de valor mas nunca de forma.

## A explicação é construída por acréscimo, um elemento entrando por vez

- Evidência: wwdc2026_322 (folha 0010, q0087 sem a linha de alinhamento, q0088 e q0089 com ela; q0085 para q0086: caixas de timestamp em cinza escuro surgem acima de cada bloco de texto; folha 0011, q0093: as etiquetas laranja de topo e base só aparecem aí; folha 0004: a lista de tópicos cresce de três para cinco itens ao longo do vídeo; folha 0005, q0041 para q0042, e folha 0006, q0047 para q0048: o destaque de sintaxe em azul claro percorre as três assinaturas de shader uma por vez)
- Evidência: wwdc2026_8012 (folha 0005, q0043 a q0045: a caixa de valor de translucidez entra em modo de edição enquanto o ícone permanece estável; folha 0007, q0058: a barra de ferramentas ganha controles extras de pré-visualização junto com o fundo de teste; folha 0003, q0021, e folha 0004, q0030: os menus suspensos revelam o conjunto fechado de opções só quando abertos)
- O que isso ensina sobre construir interface: nunca mostrar o diagrama completo de uma vez. Uma camada de informação por passo, com o resto do quadro parado, dá tempo de ligar cada elemento novo ao que já estava lá.

## Achados de fonte única

- Paleta de destaque de sintaxe usada em todos os blocos de código: comentário em cinza, string em vermelho ou laranja, parâmetro e tipos em roxo, nome de função em verde (wwdc2026_322, folhas 0004 e 0006 a 0010).
- Código em par rotulado, um lado SwiftUI e outro Metal, mostrando a mesma feature nas duas linguagens no mesmo quadro (wwdc2026_322, folhas 0006 e 0007). Na folha 0008 o par some e fica só o bloco de Metal, e nas folhas 0009 e 0010 volta a ser só SwiftUI.
- Grade de pixels em tons de azul rotulada como entrada e saída, com setas ligando um lado ao outro, usada para distinguir tipos de shader: em um par o que se anota é posição na entrada e cor na saída, em outro são duas posições diferentes ligadas por setas cruzadas (wwdc2026_322, folha 0005, q0041 a q0045).
- Textura de ruído aberta em três miniaturas de canal rotuladas R, G e B, cada uma com um ponto branco marcando a posição de amostragem e uma barra de escala de zero a um abaixo; entre dois quadros o ponto muda de lugar nos três canais ao mesmo tempo (wwdc2026_322, folha 0008, q0064, q0065 e q0067).
- Metáfora explicada como objeto físico e não como diagrama: tubulação metálica 3D com juntas, medidor de fluxo em vidro e cromado rotulado "BYTES" e válvula vermelha na abertura, e uma chave de cano real ao lado de um iPhone sobre madeira no encerramento (wwdc2026_322, folha 0001, q0007 e q0008; folha 0013, q0109 a q0114).
- Alinhamento explicado em duas fases, primeiro em dois retângulos planos e depois a mesma relação em perspectiva isométrica com pontos de ancoragem coloridos (wwdc2026_322, folha 0010, q0090, e folha 0011, q0091 a q0093).
- Controle de refração bidimensional, um campo de duas dimensões com dois valores percentuais ao lado, em vez de dois sliders separados (wwdc2026_8012, folha 0005, q0037 a q0042).
- Conjuntos de opção deliberadamente curtos e fechados: preenchimento com automático, sólido, gradiente, claro do sistema e escuro do sistema (wwdc2026_8012, folha 0003, q0021); especular com desligado, automático, interno e contorno (folha 0004, q0030); mistura com dez modos em lista vertical (folha 0021, q0181).
- Painel flutuante de aparência sobre o canvas reunindo alternância claro e escuro, interruptor de tonalização e uma barra horizontal de gradiente arco-íris com cursor para escolher a cor (wwdc2026_8012, folha 0007, q0055 e q0056).
- Cartão de pergunta da audiência padronizado: retângulo de cantos arredondados, fundo escuro semitransparente, texto branco alinhado à esquerda no terço inferior, nome do autor em negrito e contagem de votos em verde ao lado (wwdc2026_8012, folhas 0008, 0010, 0012, 0017, 0020, 0024, 0025, 0027, 0029, 0030, 0033 a 0035, 0039 e 0041).
- Cenografia de conversa em vez de palco: mesa curva de madeira clara, painel de ripas verticais ao fundo com letreiro luminoso, microfones de mesa e laptops abertos diante de cada participante, com a câmera alternando entre plano geral dos cinco e planos de dois ou de um (wwdc2026_8012, folha 0001 em diante).
- Encerramento com marca d'água do logotipo e aviso de direitos autorais em texto pequeno centralizado sobre a imagem do painel (wwdc2026_8012, folha 0043, q0380 para q0381).
- Proporção de demonstração muito baixa no formato de painel: de 43 folhas, só nove mostram a interface do aplicativo, e as notas registram trechos longos em que a fala trata de temas visuais como modos de mesclagem, contraste e camadas sem nada correspondente na tela (wwdc2026_8012, folhas 0023, 0026, 0031, 0032, 0036 a 0038 e 0042).
- No formato de sessão técnica não há demonstração de ferramenta ao vivo em nenhum momento, apenas código estático ao lado do resultado já renderizado (wwdc2026_322, observação de proporção visual).
