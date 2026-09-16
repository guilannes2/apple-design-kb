# ess-11 (lote de vídeo, 19 palestras)

## A lista de tópicos é o único indicador de progresso, resolvida só por peso e cor no mesmo corpo tipográfico
- Evidência: wwdc2023_10229 (folha 0001, q0005; folha 0002, q0014; folha 0005, q0039; folha 0007, q0062; folha 0009, q0081; item corrente em preto forte, os demais em cinza claro)
- Evidência: wwdc2024_10112 (folhas 0001, 0006, 0008, 0010 e 0012; a lista parte de um item e chega a cinco, e os cartões de seção recebem seus subitens um a um)
- Evidência: wwdc2024_10140 (folha 0001, q0004; folha 0005, q0039 a q0041; folha 0008, q0065 e q0066; folha 0011, q0098; as notas registram explicitamente que não há barra de progresso)
- Evidência: wwdc2024_10176 (folha 0005, q0041; folha 0006, q0048 e q0053; a mesma lista de quatro subtópicos muda apenas qual item está em negrito)
- Evidência: wwdc2024_10096 (folhas 0002, 0006, 0007, 0008, 0011, 0013 e 0015; a coluna com "Setting", "Interactions" e "Audience" reaparece a cada virada de bloco e a fala nunca a comenta)
- O que isso ensina sobre construir interface: posição numa sequência pode ser comunicada sem componente algum, só por contraste de peso e opacidade dentro de uma lista que nunca muda de lugar. O item inativo continua legível, então o mapa inteiro permanece disponível enquanto o foco fica inequívoco.

## O código é ensinado por realce translúcido que se desloca entre quadros, nunca por reescrita do bloco
- Evidência: wwdc2023_10229 (retângulo azul claro sobre a linha recém-adicionada em quase todas as folhas de código: folha 0003, q0019 para q0020; folha 0006, q0049 para q0050; folha 0007, q0058 para q0059; folha 0009, q0074 para q0075)
- Evidência: wwdc2024_10151 (folha 0017, q0145 a q0149, em que o texto não muda entre quadros e só o realce migra de token em token, do nome da função para o deslocamento, a cor e a posição)
- Evidência: wwdc2024_10145 (folha 0003, q0020 para q0021, o realce sai de matchedTransitionSource e vai para o sourceID dentro do modifier de zoom; volta nas folhas 0006, 0007 e 0008)
- Evidência: wwdc2024_10152 (folhas 0004 a 0011, fundo azul claro sempre sobre o trecho recém-acrescentado, recurso que a fala não menciona)
- Evidência: wwdc2024_10147 (folha 0004, q0031 e q0032; folha 0005, q0044 e q0045; folha 0008, q0070 a q0072, com três chamadas entrando de uma vez)
- Evidência: wwdc2024_10094 (folhas 0005, 0006 e 0011, destaque roxo translúcido avançando linha a linha, sem cursor visível)
- O que isso ensina sobre construir interface: apontar a mudança com uma camada de fundo custa menos leitura do que refazer o bloco, e dispensa cursor, seta ou legenda. O mesmo vale em produto: quando algo muda dentro de um texto ou de uma lista, marcar o delta preserva o contexto em volta.

## Certo e errado aparecem com a mesma fidelidade, separados por selo verde de check e selo vermelho de X fora do artefato
- Evidência: wwdc2023_10229 (folha 0003, q0021 a q0023, painéis "Recommended" com três cartões e check verde contra "Not recommended" com quatro cartões e X vermelho, cada exemplo ruim rotulado pelo defeito)
- Evidência: wwdc2024_10085 (folha 0003, q0019 e q0020, alerta de download reprovado; folha 0006, q0051 a q0054, HUD desproporcional no iPad mini com X e a versão corrigida sem marcação; folha 0008, q0064 a q0070, enquadramentos comparados; folha 0017, q0146 a q0153, o mesmo HUD passa de X para check quando os botões trocam de lado)
- Evidência: wwdc2024_10116 (folha 0008, q0069 a q0072, três pares sob títulos de regra, entre eles miniaturas em tom neutro aprovadas contra miniaturas com bordas coloridas reprovadas)
- Evidência: wwdc2024_10176 (folha 0003, q0025 e q0026, quatro chips fixos com X contra um único chip com parâmetro editável e check; folha 0004, q0030, grade dois por dois separando ação de gesto de ação de tarefa)
- Evidência: wwdc2024_10145 (folha 0006, q0047 a q0049, o mesmo slide passa de X para check quando os comentários de reset de estado entram nas funções antes vazias)
- O que isso ensina sobre construir interface: o veredito mora numa camada separada do exemplo, com cor e forma redundantes, e o erro é desenhado com o mesmo capricho do acerto. Rotular qual defeito cada variante ruim carrega ensina mais que só apontar a boa.

## O esquema abstrato vem antes do produto real e depois os dois aparecem pareados
- Evidência: wwdc2024_10112 (folha 0002, q0011 a q0013, wireframe de contorno azul fino sem preenchimento mostrando cluster e grade de apps, e só em q0014 a q0021 entram as renderizações fotorrealistas de volante)
- Evidência: wwdc2023_10309 (folha 0003, q0024 a q0027, diagramas com moldura pontilhada rosa e texto substituto, e folha 0004, q0028 a q0032, cada diagrama colado ao lado do widget real correspondente)
- Evidência: wwdc2024_10151 (folha 0007, q0061 para q0062, a malha três por três de pontos com linhas brancas é deformada por arraste antes de qualquer código aparecer)
- Evidência: wwdc2024_10152 (folha 0003, q0023 a q0026, a cápsula com avatar é desmontada em estados inativo, ativo e expandido antes de virar API)
- Evidência: wwdc2024_10116 (folhas 0004 e 0005, q0037 a q0040, caixas nomeadas ligadas por seta desenham a anatomia dos componentes antes do primeiro bloco Swift)
- O que isso ensina sobre construir interface: o esquema define anatomia e slots, o produto prova que a anatomia fecha. Pareá-los lado a lado é a forma mais econômica de mostrar que um gabarito abstrato aceita conteúdo real sem se deformar.

## Rótulos ficam fora da tela e chegam até o elemento por linha de chamada fina, em vez de cobrir o pixel discutido
- Evidência: wwdc2024_10085 (folha 0004, q0028 e q0029, linhas ligando a barra ao rótulo "Show progress" e os botões a "Allow replay"; folha 0007, q0060 a q0063, retângulos semitransparentes de safe area com chamadas para Home indicator e Dynamic Island; as notas registram que essa anotação não é descrita na fala)
- Evidência: wwdc2024_10147 (folha 0008, q0066 a q0069, colchete horizontal sob as abas levando "Customizable", depois "Pinned" apontando a lupa e "Sidebar only" apontando um trecho de código)
- Evidência: wwdc2024_10087 (folha 0006, q0047 a q0049, desenho técnico de corte da galeria recebendo rótulos de zona em três etapas, primeiro a seção central, depois cinco, por fim o sexto)
- Evidência: wwdc2023_10257 (folha 0011, q0094 para q0095, dois cubos em contorno com setas rotuladas pela porcentagem de escala e pela compensação de peso, com o traço visivelmente mais grosso na segunda)
- O que isso ensina sobre construir interface: anotar por cima da captura real dispensa o diagrama paralelo que envelhece junto com o produto. O rótulo vive na margem, ligado por traço fino, e a tela continua inteira e verificável embaixo.

## O artefato é montado peça por peça na ordem em que as peças dependem umas das outras
- Evidência: wwdc2024_10116 (folha 0001, q0005 a q0009, primeiro a caixa de AVFoundation alimentada pelo ícone de filme, depois a seta e a caixa de RealityKit, depois AVKit acima ligada a quatro blocos menores, na mesma ordem de dependência que a fala descreve)
- Evidência: wwdc2023_10229 (folha 0004, q0028 a q0030, o cartão de dica ganha primeiro título, texto e fechar, depois o ícone de estrela, depois o botão de ação azul, sempre ao lado do código correspondente; folha 0006, q0049 a q0054, a regra por evento cresce em quatro passos encadeados)
- Evidência: wwdc2024_10094 (folha 0011, q0091 a q0093, o fluxo de detecção de controle parte de uma caixa e termina ramificado em duas caixas menores com mini trechos de código dentro)
- Evidência: wwdc2023_10257 (folha 0011, q0097 a q0099 e folha 0012, q0100, a cartela de restrições cresce do título às quatro regras completas)
- Evidência: wwdc2024_10087 (folha 0002, q0016 a q0018, o blockout sai do menu de primitivas e vira planos e rampa formando o volume do ambiente)
- O que isso ensina sobre construir interface: a ordem de aparição carrega informação que o diagrama pronto perde. Quem monta na tela na ordem real de dependência ensina a arquitetura junto com o desenho, sem precisar narrar a hierarquia.

## Só uma variável muda por vez, com o componente isolado em fundo neutro e o dado fixo no centro
- Evidência: wwdc2024_10112 (folha 0004, q0029 a q0036, o mesmo gauge com "60" ao centro tem o anel engrossando em preto até cobrir quase todo o círculo e só depois troca para gradiente azul petróleo; folha 0005, q0038 a q0045, a alternativa analógica surge por transformação do mesmo componente)
- Evidência: wwdc2024_10151 (folhas 0009 a 0011, q0079 a q0093, a transição é acumulada sobre o mesmo avatar, primeiro sem efeito, depois escala, depois escala com opacidade, por fim a struct que soma desfoque, rotação e brilho)
- Evidência: wwdc2024_10086 (folha 0003, q0025 a q0027, o mesmo objeto passa de silhueta translúcida a wireframe com peças explodidas e a render final dentro da sala)
- Evidência: wwdc2024_10087 (folha 0004, q0028 e q0029, o mesmo tronco em malha triangular densa e depois em malha decimada, com o rótulo mudando junto)
- Evidência: wwdc2023_10258 (folha 0005, q0037 a q0045, o roteador de wifi alterna entre azul sólido e tom apagado conforme o booleano, e só depois o segundo efeito entra encadeado)
- O que isso ensina sobre construir interface: para provar que um atributo importa, congele todo o resto. Fundo neutro, mesmo enquadramento e um único delta por quadro tornam a comparação verificável e impedem que a melhora seja creditada à variável errada.

## Código à esquerda e resultado dentro da moldura do aparelho à direita, na mesma tela e com layout congelado
- Evidência: wwdc2024_10151 (folhas 0002 a 0019, convenção rígida de código monoespaçado à esquerda e dispositivo à direita, sempre nessa ordem)
- Evidência: wwdc2024_10152 (folhas 0004 a 0007, 0011 e 0012, simulador do Vision Pro rodando o app de vídeo o tempo todo, com o botão de perfil demonstrando fisicamente o efeito que o código acabou de declarar)
- Evidência: wwdc2024_10145 (folha 0003, layout fixo em duas colunas, bloco monoespaçado à esquerda e mockup de iPhone à direita, mudando só o realce)
- Evidência: wwdc2024_10147 (folha 0005, q0044 e q0045, quando a linha da aba de busca entra no código o ícone de lupa aparece no topo da barra lateral do aparelho, no mesmo quadro)
- Evidência: wwdc2023_10258 (folhas 0004 a 0011, o ícone ou o controle desenhado colado ao bloco que o gera, incluindo o botão de fundo azul muito claro ao lado do ícone de antena na folha 0006, q0048 a q0053)
- O que isso ensina sobre construir interface: causa e efeito no mesmo enquadramento eliminam a memória de curto prazo do leitor. O layout não se mexe entre quadros, então qualquer movimento na imagem é informação, não ruído de composição.

## Opacidade e saturação carregam estado, tanto no produto quanto na condução do olhar
- Evidência: wwdc2024_10085 (folha 0003, q0027 e folha 0004, q0028 e q0029, capítulo bloqueado em opacidade reduzida com aviso de espera, botão laranja para concluído e verde para o atual)
- Evidência: wwdc2024_10140 (folha 0008, q0067 a q0070, o realce progressivo acende uma palavra do título junto do bloco correspondente enquanto rodapé, botão e demais blocos perdem opacidade, seguindo a ordem de leitura da tela)
- Evidência: wwdc2023_10309 (folha 0007, q0055 e q0056, o widget de medicação é ampliado num balão branco enquanto os demais ficam apagados e translúcidos ao fundo)
- Evidência: wwdc2024_10094 (folhas 0007 e 0008, q0062 e q0064, três retângulos iguais em fileira com o estado em discussão pintado sólido e os demais só em contorno cinza claro)
- Evidência: wwdc2024_10096 (folha 0012, q0100 a q0106, a cena perde saturação e contraste até quase branco para sinalizar a saída do portal)
- O que isso ensina sobre construir interface: apagar o entorno é mais barato que ampliar, mover ou emoldurar o que está em foco, e o mesmo mecanismo serve para indisponibilidade, para seleção e para ênfase didática. Como o item apagado permanece no lugar, o layout nunca salta.

## A adaptação entre plataformas é provada pela mesma interface em molduras diferentes, recompondo colunas em vez de escalar a tela
- Evidência: wwdc2024_10085 (folha 0001, q0004 a q0008, a mesma cena de jogo em MacBook, iPad e iPhone; folha 0006, q0051 a q0054, o HUD é reposicionado e redimensionado no iPad mini em vez de encolhido inteiro)
- Evidência: wwdc2024_10147 (folha 0010, q0088 a q0090 e folha 0011, q0091 a q0093, a mesma sidebar em janela de macOS com os três pontos coloridos, em janela flutuante de visionOS sobre uma sala 3D e em TV widescreen como lista escura sem moldura de aparelho)
- Evidência: wwdc2023_10229 (folha 0002, q0010 a q0013, iPad e MacBook em dupla exposição e um Apple Watch exibindo o mesmo cartão de dica em versão compacta com botão "Open")
- Evidência: wwdc2024_10145 (folha 0002, q0018, iPad em grade de três colunas e iPhone em grade de duas, mesmo desenho de cartão)
- Evidência: wwdc2024_10098 (folha 0003, q0020 e q0021, iPhone e relógio lado a lado e depois o mesmo cartão de entrega já abaixo do mostrador)
- O que isso ensina sobre construir interface: responsividade é recontagem de colunas, reposicionamento de controles e troca de densidade, nunca redução proporcional. O componente mantém sua anatomia e muda de arranjo.

## O mesmo gabarito de cartão se repete entre contextos, e o conteúdo é a única coisa que troca
- Evidência: wwdc2024_10098 (folhas 0003, 0005 e 0007, fundo escuro translúcido, cantos bem arredondados, elemento gráfico à esquerda e texto de status à direita, incluindo a variação de música com botão de pausa circular; folha 0007, q0056, o cartão customizado de café mantém margens e proporções idênticas às dos padrão)
- Evidência: wwdc2024_10140 (folhas 0003, 0004 e 0005, card de notificação com material translúcido escuro, brilho colorido desfocado atrás, ícone circular à esquerda, título em negrito, texto secundário menor e marca de tempo no canto superior direito)
- Evidência: wwdc2024_10176 (folhas 0002 a 0007, uma pílula branca com ícone colorido circular à esquerda, verbo em preto e parâmetro em azul serve de notação para o vídeo inteiro, variando só o conteúdo)
- Evidência: wwdc2023_10309 (folha 0005, q0042 a q0045, a mesma moldura com três círculos tracejados recebe ícones de app, complicações de clima e fotos de contato)
- O que isso ensina sobre construir interface: quando o gabarito não varia, o olho para de reaprender a leitura a cada instância e passa a comparar conteúdo. Identidade própria cabe dentro dele por cor e ícone, sem mexer em margem nem proporção.

## O quadro intermediário da animação é mostrado de propósito, e não só as duas pontas
- Evidência: wwdc2024_10116 (folha 0002, q0015 para q0016, a tela única aparece se desdobrando em duas telas retangulares semitransparentes, estado que nem a fala nem um quadro final mostrariam)
- Evidência: wwdc2024_10145 (folha 0001, q0004 para q0005, um cartão semitransparente com as miçangas roxas aparece sendo puxado para fora da grade antes de a tela de edição existir)
- Evidência: wwdc2024_10152 (folha 0003, q0023 a q0026, a cápsula surge já larga porém vazia, isto é, a forma expandida antes do texto entrar)
- Evidência: wwdc2024_10140 (folha 0013, q0112 a q0114, o botão azul do alerta aparece primeiro apagado e depois sólido enquanto o fundo clareia, registrando a entrada como animação)
- Evidência: wwdc2024_10112 (folha 0005, q0038, uma forma de cápsula escura serve de quadro de passagem entre o gauge digital e o analógico)
- O que isso ensina sobre construir interface: transição é um estado com anatomia própria, que precisa de decisão de forma, opacidade e ordem. Projetar só o antes e o depois entrega ao motor de animação a parte que o usuário mais olha.

## Amplitude de um sistema se mostra por catálogo em grade de células idênticas, com rótulo curto embaixo
- Evidência: wwdc2023_10258 (folha 0002, q0010 a q0012, os sete efeitos em quatro colunas por duas linhas, ícones azuis de mesmo peso de traço e mesmo tamanho, rótulo pequeno centralizado abaixo, sem cartão nem borda)
- Evidência: wwdc2024_10112 (folha 0006, q0048, mosaico com cerca de vinte miniaturas de gauges e widgets; folha 0012, q0100 e q0101, dez cartões escuros de mesmo tamanho em duas linhas de cinco, rotulados por categoria)
- Evidência: wwdc2023_10257 (folha 0010, q0080 a q0084, grade de 27 ícones de pasta em três linhas por nove colunas; folha 0012, q0101, catálogo da mesma caixa 3D combinada a molduras e badges diferentes em células uniformes)
- Evidência: wwdc2024_10176 (folha 0002, q0013 e q0014, a frase única ampliada dá lugar a dez exemplos reais em duas colunas de cinco, todos no mesmo estilo)
- Evidência: wwdc2024_10094 (folha 0004, q0034, cinco ícones de gesto em duas fileiras, três em cima e dois embaixo, todos na mesma linguagem de linha fina)
- O que isso ensina sobre construir interface: a variedade só fica legível quando o gabarito não varia. Célula de tamanho igual, mesmo peso de traço e legenda curta abaixo transformam um inventário grande em uma leitura única.

## Regra combinatória vira matriz, com cor apenas dentro da célula
- Evidência: wwdc2023_10258 (folha 0004, q0032, tabela cruzando os sete efeitos com os quatro comportamentos, linhas zebradas sutis, cabeçalho pequeno em cinza e o check verde como único elemento de cor)
- Evidência: wwdc2023_10257 (folha 0012, q0106 e folha 0013, q0112 para q0113, matriz de tamanho por peso desenhada em contorno fino que fica visivelmente mais esparsa quando o valor de compatibilidade muda no rodapé)
- Evidência: wwdc2024_10094 (folha 0012, q0101, matriz cruzando tipos de input com tipos de espaço, cada célula com visto verde ou X vermelho circulados e uma coluna destacada por halo azul)
- O que isso ensina sobre construir interface: quando a pergunta é "esta combinação existe", a matriz responde sem texto. A grade fica em contorno fino e neutra, a cor entra só na marca de célula, e mudar um filtro esvazia a matriz na frente do leitor.

## Translucidez é usada como camada que nunca disputa, com um só elemento opaco por composição
- Evidência: wwdc2024_10086 (folha 0010, q0088 a q0090, painel de vidro escuro com sidebar e grade de capas fixo no espaço, mostrado de três ângulos sem base nem moldura extra; folha 0012, q0101 e q0102, o fundo translúcido deixa ver a sala e o logotipo é o único elemento opaco de identidade)
- Evidência: wwdc2024_10116 (folha 0002, barra de reprodução em material de vidro flutuando abaixo da tela, não acoplada a ela)
- Evidência: wwdc2024_10096 (folha 0016, q0141 a q0144, cartão escuro semitransparente de cantos arredondados ancorado no chão real, que cresce em menu com dois botões empilhados e volta ao estado reduzido)
- Evidência: wwdc2023_10271 (folha 0003, q0021 e q0026, teclado com teclas redondas de vidro translúcido e leve relevo flutuando em ângulo; folha 0003, q0027 e folha 0004, painéis translúcidos com cabeçalho de data e local sobre fundo escuro)
- O que isso ensina sobre construir interface: o vidro é para a moldura e o chrome, não para o dado. Deixar o ambiente atravessar o painel e reservar a opacidade para identidade ou conteúdo mantém a hierarquia legível sobre qualquer fundo.

## A cada bloco novo, um selo verde pequeno e sempre igual marca só o que é novidade
- Evidência: wwdc2023_10257 (folha 0008, q0067, selo "NEW" ao lado do diagrama de equação que apresenta symbol components)
- Evidência: wwdc2024_10145 (folha 0007, q0056, círculo com "NEW" sobre a chamada de spring de meio segundo, com a linha também em destaque azul)
- Evidência: wwdc2024_10147 (folha 0004, q0031 a q0035, selo circular verde na mesma linha do título quando a API é nova, dentro de uma anatomia fixa de slide)
- Evidência: wwdc2024_10152 (folha 0002, q0014 e folha 0011, q0095, o selo aparece no slide da API de efeitos customizados e depois no efeito vazio usado na alternativa de acessibilidade, nunca decorativamente)
- O que isso ensina sobre construir interface: um marcador de novidade só funciona enquanto for escasso, constante em forma e cor e ancorado no elemento exato, não no cabeçalho da tela inteira.

## O encerramento troca a tela pela fotografia de um objeto físico e as conclusões entram uma por quadro
- Evidência: wwdc2024_10116 (folha 0009, q0073 a q0078, fone de ouvido azul claro sobre madeira com copo desfocado ao fundo, texto preto à esquerda e as duas linhas surgindo uma a cada quadro; as notas registram o mesmo padrão em outro vídeo da leva)
- Evidência: wwdc2024_10145 (folha 0009, q0078 a q0081, fotografia da pulseira física sobre superfície reflexiva, título grande à esquerda e a lista crescendo uma linha por quadro)
- Evidência: wwdc2024_10152 (folha 0012, q0103 a q0105, objetos artesanais sobre mesa de madeira à direita e três recomendações entrando uma a uma à esquerda)
- Evidência: wwdc2024_10140 (folha 0015, q0131, natureza morta de caneca e iPhone sobre mesa clara com o título no canto superior esquerdo)
- Evidência: wwdc2023_10229 (folha 0010, q0089 e q0090, cubos coloridos translúcidos e a traseira de um iPhone sobre mesa clara ao lado de três recomendações, a terceira em cinza mais claro)
- Evidência: wwdc2024_10094 (folha 0012, q0104 a q0106, fotografia de natureza morta sobre madeira recebendo as três recomendações e depois uma linha de referência no rodapé)
- O que isso ensina sobre construir interface: mudar de registro no fim marca o fechamento melhor que um slide de lista. A imagem calma ocupa metade da composição, e o texto entra devagar para que a última leitura não seja densa.

## Rodapé fino separado por linha guarda crédito e referência cruzada, com dois pontos de alinhamento
- Evidência: wwdc2023_10258 (folha 0002, q0012, rodapé separado por linha horizontal fina creditando outra sessão à esquerda e o evento à direita)
- Evidência: wwdc2024_10145 (folha 0009, q0078 a q0081, tabela de rodapé de duas linhas com nome do recurso à esquerda e ano do evento à direita, separada por linha fina)
- Evidência: wwdc2024_10152 (folha 0001, q0007, selo circular com a versão no canto superior direito e rodapé citando a sessão anterior sobre apps em janela)
- Evidência: wwdc2024_10151 (folha 0012, barra de rodapé cinza citando uma sessão anterior como referência cruzada)
- O que isso ensina sobre construir interface: metadado não disputa com conteúdo quando vive numa faixa separada por uma linha de um pixel, com esquerda e direita em papéis fixos. É a mesma mecânica de uma barra de status.

## Quadros vazios e telas em branco funcionam como pontuação entre blocos
- Evidência: wwdc2024_10140 (folha 0001, q0006 e q0008; folha 0002, q0013 e q0015; folha 0003, q0024 e q0026, sempre em pares em torno de um quadro do apresentador, recurso que só aparece na sequência de imagens)
- Evidência: wwdc2024_10152 (folha 0005, q0044; folha 0007, q0057 e q0062; folha 0010, q0088, quadros brancos vazios, imagens fantasma do código anterior esmaecido e um círculo verde isolado ao centro)
- Evidência: wwdc2024_10151 (folhas 0012 a 0018, um iPad de tela em branco aparece entre blocos de código como pausa de edição, sem conteúdo)
- Evidência: wwdc2024_10176 (folhas 0001, 0003 e 0004, quadros totalmente brancos ou pretos nos cortes entre o apresentador e os gráficos)
- O que isso ensina sobre construir interface: espaço vazio é recurso de ritmo, não desperdício. Um intervalo curto antes de um bloco denso separa assuntos melhor que uma linha divisória ou uma troca de cor de fundo.

## Objeto 3D só ganha tamanho quando a cena traz figura humana e sombra de contato
- Evidência: wwdc2024_10087 (folha 0003, q0023 a q0025, figura poligonal cinza sem rosto e com proporções simplificadas em pé sobre um círculo demarcado no piso, servindo de régua de escala dentro da cena em tamanho real)
- Evidência: wwdc2024_10096 (folha 0003, q0021 a q0026, silhueta humana em linha fina com sombra elíptica no chão marcando ancoragem, mantida idêntica nos três tipos de conteúdo para que só o volume azul mude)
- Evidência: wwdc2024_10086 (folha 0002, q0015 e q0016, o motor a jato flutua inteiro dentro de uma sala com plantas e poltronas e depois recebe a mão do usuário tocando o compartimento interno; folha 0009, o carro de corrida renderizado em escala real com texturas legíveis)
- O que isso ensina sobre construir interface: escala é relação, nunca número. Uma figura de referência e uma sombra de contato dizem mais sobre o tamanho de um elemento espacial do que qualquer medida escrita ao lado.

## Som é desenhado como anéis ou esferas concêntricas saindo de um ponto marcado no espaço
- Evidência: wwdc2023_10271 (folha 0002, q0016, anéis concêntricos brancos com gradiente do centro para fora saindo de um ponto no chão da sala, notação repetida na folha 0011, q0093, em vários pontos simultâneos, e na folha 0010, q0089, com alto-falantes embutidos nos nichos)
- Evidência: wwdc2024_10086 (folha 0008, ambiente doméstico desenhado só em linhas cinza com esferas azuis translúcidas concêntricas ao redor de uma figura humana em pé)
- O que isso ensina sobre construir interface: fenômeno invisível precisa de notação fixa e reutilizável. O mesmo desenho aplicado em contextos diferentes vira vocabulário, e o ambiente pode ficar em wireframe para que a notação seja o único elemento com peso visual.

## Achados de fonte única

- Medida numérica emparelhada com o elemento no tamanho real, número grande à esquerda e moldura de aparelho à direita: "17pt Default" e "11pt Minimum" para corpo de texto em iPhone e iPad, e "44pt Default" com "28pt Minimum" para alvo de toque aparecendo em dois passos sobre o mesmo menu, mais "28pt Default" para Mac com um cursor pousado sobre o botão (wwdc2024_10085, folha 0010, q0087 a q0090; folha 0011, q0094, q0095 e q0097). As próprias notas registram que os valores do Mac citados na fala não chegam a aparecer na tela.
- Economia de um sistema de símbolos mostrada como aritmética visual: uma grade de 27 ícones de pasta em três linhas por nove colunas de um lado e, do outro, apenas três desenhos rotulados como os extremos e o meio da escala de peso (wwdc2023_10257, folha 0010, q0080 a q0084).
- Ponte explícita entre ferramenta e código dentro da própria ferramenta: menu de contexto de duas linhas oferecendo copiar a configuração atual para Swift ou para Objective-C (wwdc2023_10257, folha 0003, q0023).
- Escala de tom como componente de interface e não como conceito: quatro barras horizontais rotuladas por atributo, cada uma com trilha pontilhada e um marcador retangular azul cuja posição indica a intensidade, empilhadas num cartão de cantos arredondados e repetidas em três cenários diferentes para comparação direta das posições (wwdc2024_10140, folha 0012, q0102 a q0104; folha 0013, q0109 a q0111 e q0116 e q0117).
- Método de definição de voz documentado em estágios visuais: título sem nota alguma, duas notas, cerca de dezesseis espalhadas, reagrupadas em aglomerados soltos e por fim organizadas em colunas com dois post-its de cabeçalho em azul destacando-se dos amarelos, depois compactadas em pilhas com leve deslocamento sugerindo espessura de papel (wwdc2024_10140, folha 0006, q0049 a q0054; folha 0007, q0055 e q0056).
- Placeholder abstrato antes de qualquer conteúdo concreto: cinco chips de verbo genérico empilhados com o parâmetro representado por uma barra cinza vazia, mostrando a forma da estrutura antes de um exemplo real (wwdc2024_10176, folha 0003, q0023).
- Jornada emocional desenhada como escada de barras de altura crescente e decrescente, com o degrau alcançado em cinza escuro, os seguintes em cinza claro e um emoji de expressão facial acima de cada degrau; numa segunda passada os blocos genéricos são trocados por fotos reais do produto sem mudar a estrutura (wwdc2024_10096, folha 0015, q0128 a q0132).
- Grau de participação quantificado por contagem de miniaturas: o mesmo diagrama isométrico ganha abaixo uma barra de cenas ligadas por setas azuis finas, cujo número cresce de zero para quatro, cinco e seis conforme o rótulo passa de pouca a muita interação, fechando com duas miniaturas empilhadas que representam desfechos alternativos (wwdc2024_10096, folha 0014, q0121 a q0126).
- Interface de depuração mostrada como produto real sobreposta ao exemplo: quatro controles deslizantes no topo da tela do iPhone, rotulados como tempo, amplitude, frequência e decaimento, cada um com alça circular branca sobre trilha cinza fina, com a alça de um deles mudando de posição entre dois quadros (wwdc2024_10151, folha 0019, q0166 a q0168).
- Hierarquia interna de texto explicada com caixas azuis aninhadas desenhadas por cima do código borrado, a caixa externa de layout contendo linha e a linha contendo uma fileira de runs e fatias de run com reticências indicando continuidade; no quadro seguinte o diagrama some e o código volta legível (wwdc2024_10151, folha 0014, q0125 e q0126).
- Convenção editorial de remoção no código: texto riscado sobre a linha que está sendo substituída quando o comentário muda para remover conteúdo, e no quadro seguinte as linhas riscadas desaparecem, deixando só a versão final e mais curta (wwdc2024_10116, folha 0006, q0050 e q0051).
- Mixagem espacial anotada com emojis posicionados sobre a fotografia: dois sapos nas margens esquerda e direita da foto noturna, depois três agrupados à esquerda mais um isolado à direita, depois o da direita bem maior para sugerir aproximação (wwdc2023_10271, folha 0008, q0071 para q0072; folha 0009, q0074 a q0077).
- Estágio de blockout deixado visível na própria cena: grupos de caixas de papelão ocupando o lugar de bancos e assentos em várias folhas, detalhe que a tela entrega e a fala não menciona (wwdc2024_10087, folhas 0004, 0005, 0007 e 0008).
- Guia de atenção como contorno luminoso animado e não como estado estático: o disco vazio que convida a carregar uma faixa ganha um anel pulsante ao redor do ícone de música (wwdc2024_10086, folha 0014, q0122 e q0123).
- Fonte variável provada com o glifo isolado em fundo branco liso: o número "35" centralizado aparece em peso fino, depois em peso bem mais grosso, depois de volta ao fino, sem nenhum outro elemento na tela (wwdc2024_10112, folha 0003, q0025 a q0027).
- Máquina de estados reciclada para ensinar quatro cenários diferentes: dois círculos de aparecido e desaparecido ligados por duas setas curvas com os callbacks como pontos nomeados ao longo delas, mudando só o subtítulo do cenário e a posição do ponto vermelho, com um ponto vermelho e outro branco vazado simultâneos no caso cancelado, tudo pareado com a transição real acontecendo ao lado (wwdc2024_10145, folhas 0004 e 0005, q0032 a q0040).
- Classificação didática colada ao exemplo: três cartões reais recebem abaixo de cada um o rótulo da razão pela qual existem, progresso, ação e importância, recurso de comparação lado a lado que a fala não enuncia nesses termos (wwdc2024_10098, folha 0006, q0046 a q0048).
- Regra de exclusividade encenada pela composição: três cartões sobrepostos e cortados nas bordas com o do centro sempre ampliado e em foco enquanto os outros ficam parcialmente fora de quadro (wwdc2024_10098, folha 0006, q0051 a q0053).
- Ramificação de comportamento com código de cor fixo: caixas cinzas para os estados fixos de entrada e saída, caixas verdes para as etapas de interação e setas finas pretas, e o ponto alto quando a sequência linear de quatro caixas vira uma grade de seis opções paralelas com contorno azul claro (wwdc2024_10096, folha 0013, q0112 a q0117).
- As cores das caixas do diagrama reaparecem como cores de sintaxe no código, verde para controlador de experiência e gerenciador, roxo para o player e azul escuro para o browser, criando uma associação entre conceito e implementação que a fala não verbaliza (wwdc2024_10116, folhas 0005 e 0006).
- Barra de instalação anotada com tempo e estado: faixa dividida em trecho azul rotulado como jogável e trecho cinza rotulado como não baixado, que no quadro seguinte ganha as anotações de quinze minutos e download em segundo plano, e depois aparece sobreposta ao rodapé do gameplay real com o trecho azul avançando a cada quadro (wwdc2024_10085, folha 0003, q0021 a q0026).
- Letterbox estudado com quatro preenchimentos diferentes em quadros seguidos, da cena original para branco, para gradiente azul escuro e de volta à cena, ilustrando as opções de preencher com arte ou neutralizar (wwdc2024_10085, folha 0009, q0075 a q0078).
- Diferença entre controle físico e toque resolvida por direção de seta: caixas de entrada e de jogo ligadas por uma seta única no caso do controle com TV, e o mesmo par com seta dupla no caso do toque, aí com o HUD virtual de D-pad, botões de ação e dois círculos de joystick sobreposto à cena (wwdc2024_10085, folha 0014, q0122 a q0125).
- Modularidade do painel mostrada por recomposição sucessiva do mesmo espaço: três módulos, depois cinco menores, depois de novo três com outro conteúdo, cada módulo delimitado por traço fino dentro de um contêiner de cantos arredondados, e num par de quadros os módulos somem, resta só o papel de parede e voltam em faixa horizontal fina e semitransparente (wwdc2024_10112, folha 0009, q0076 a q0081).
- Recapitulação como tela própria de miniaturas: sob o título, três fotos reais de mesmo tamanho e bordas retas em fileira retomando os três momentos já mostrados, primeiro só o título e depois o título com as fotos (wwdc2024_10096, folha 0011, q0094 para q0095).
