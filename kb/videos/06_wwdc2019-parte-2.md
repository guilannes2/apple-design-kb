# wwdc2019 (parte 2)

## Designing Award Winning Apps and Games (id: wwdc2019_802, 46.7 min)

Base: transcrição e 40 de 40 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2019/802/.

Tese central: os apps e games premiados no Apple Design Awards não têm uma fórmula de critérios, mas compartilham valores recorrentes (inovação, confiança, refinamento, beleza, inclusão e atenção ao detalhe), e cada valor aparece ilustrado por uma história de processo de design de um app ou jogo específico.

O processo de design que a Apple descreve, por valor:
- Inovação (Asphalt 9, HomeCourt): questionar as premissas básicas do domínio desde o início ("por que fazemos assim, só porque sempre foi assim?"), converter problemas em ideias, testar e iterar antes de assumir a solução como definitiva. No caso de HomeCourt, o time removeu obstáculos um de cada vez (tripé, iluminação, desenho manual de linhas) até restar uma experiência sem fricção.
- Confiança (Pixelmator Photo): quando um recurso usa machine learning, revelar visualmente a causa e o efeito da ação ("atribuição"), para que a pessoa entenda o que está sendo ajustado e possa intervir.
- Refinamento (The Gardens Between, Butterfly iQ): explorar direções bem distantes do resultado final antes de convergir; testar metáforas do mundo real com o público-alvo e descartar as que não funcionam, mesmo que pareçam óbvias.
- Beleza (Thumper, ELOH, Ordia): simplicidade radical na tela para sustentar imersão; contratar especialistas dedicados (ilustrador, sound designer) quando a estética é central à experiência; manter coerência visual em todas as telas.
- Inclusão (Pixelmator Photo, Ordia): usar componentes nativos do sistema para herdar acessibilidade; simular deficiências (daltonismo) sobre o próprio design e reequilibrar cores.
- Atenção ao detalhe (Flow by Moleskine): resolver primeiro os fundamentos da interação (protótipos com botões de texto puro, sem estilo visual) antes de investir em design visual e animação.

Princípios enunciados e o porquê:
- "Question assumptions from the start": Asphalt 9 largou os controles tradicionais de corrida (aceleração, freio, curva) porque a curva manual era propensa a erro do jogador; substituíram por seleção de caminho e item via swipe, e isso reduziu a frustração e liberou atenção para a estratégia.
- Simplificar até o que a pessoa quer fazer, sem tirar valor: HomeCourt automatizou detecção de aro, linha de três pontos, pernas e depois pose completa do corpo via ML, eliminando a necessidade de tripé e luz perfeita, até rodar seguro apoiado no chão.
- Revelar a inteligência do modelo de ML na interface (atribuição): em Pixelmator Photo, o botão de "Magic Wand" aplica um modelo treinado, mas os parâmetros (exposição, tom de pele etc.) animam de forma visível e ficam editáveis individualmente, o que gera confiança porque a pessoa vê causa e efeito.
- Não copiar metáforas do mundo físico sem testar: Butterfly iQ tentou replicar diretamente os discos físicos (dial) do carrinho de ultrassom tradicional na tela do iPhone; em teste com médicos isso ocupava espaço valioso da imagem sem necessidade, então o time se inspirou no app Câmera do iOS e moveu contraste e profundidade para gestos (pan lateral = contraste, swipe vertical = profundidade), sem persistência visual constante dos discos.
- Refinar é diferente de acertar de primeira: os artefatos de design de The Gardens Between mostravam versões do jogo com Branca de Neve e a Bela Adormecida, completamente distintas do resultado final, evidenciando exploração ampla antes de convergir.
- A estética pode ter função prática, não só decorativa: em ELOH, a ilustração e o som reforçam a legibilidade dos elementos interativos (poucos, mas cuidados) e o ritmo de dificuldade; a cada nível especialmente difícil resolvido, o próximo é mais simples, o que dá espaço para notar a estética de novo.
- Usar componente nativo em vez de recriar: Pixelmator Photo trocou os checkboxes do app de Mac por switches nativos de iOS na versão de iPad porque comunicam estado com mais clareza e já vêm com suporte a acessibilidade (rótulos ativáveis em Ajustes).
- Simular a limitação do usuário sobre o próprio produto: Ordia testou o jogo em modo monocromático completo e aplicou filtros que simulam diferentes tipos de daltonismo sobre capturas de tela, depois reequilibrou cores para manter todos os elementos distinguíveis.

Técnicas concretas de construção de interface citadas:
- Interação: TouchDrive (Asphalt 9) usa swipe para seleção de caminho/item e tap-and-hold para nitro/boost, substituindo aceleração, freio e curva manual.
- Machine learning aplicado à interface: modelo de Pixelmator Photo treinado com 20 milhões de fotos profissionais, acionado por um único botão.
- Gestos mapeados a parâmetros: em Butterfly iQ, "panning left and right changes the contrast and swiping up and down changes the depth"; uma régua aparece na lateral direita durante o swipe de profundidade e recolhe quando não está em uso.
- Onboarding minimalista (Thumper): título com sequência épica logo na abertura; botão de pause que se transforma numa barra diagonal simples e "desaparece"; instrução "Swipe Up to Jump" combinada com contagem regressiva 3, 2, 1 antes mesmo do jogador perguntar quando; seta sutil de reforço de gesto; som avisando quando fazer o swipe.
- Estado de vitalidade sem HUD (Thumper): a vitalidade é mostrada nas próprias asas do besouro jogável ("full wings at full health, no wings at half health"), sem números ou barra separada, para manter o foco na pista.
- Ícone de app derivado da própria marca do produto (HomeCourt): as letras H e C emergem das linhas de contorno de uma quadra de basquete; o fundo laranja remete à cor da bola.
- Design language coerente ponta a ponta (Ordia): tema orgânico "blobby" aplicado a menus, transições, níveis e personagens; cor usada para comunicar se uma criatura é amigável, hostil ou de navegação; ícone de Share padrão do iOS usado para reforçar pertencimento à plataforma.
- Acessibilidade: switch nativo em vez de checkbox custom (Pixelmator Photo); modo daltônico com paleta rebalanceada e teste em monocromia total (Ordia), citando o dado de "over 300 million people worldwide with some form of colorblindness".
- Cor e tipo (Flow by Moleskine): seletor de ferramenta e cor com "over 1,400 unique color names" no app; protótipos de interação construídos primeiro só com botões de texto puro, sem estilo visual, para validar a interação antes de desenhar visualmente.
- Animação como comunicação: no editor de ferramenta de Flow, animação de transição de estado reforça como usar a interface e atrai atenção, segundo a fala.

Exemplos citados e o que cada um ensina:
- Asphalt 9 (TouchDrive): questionar controles padrão de um gênero inteiro pode abrir uma categoria nova de jogabilidade.
- HomeCourt: cada obstáculo de configuração removido (tripé, luz, marcação manual) é uma barreira a menos entre a pessoa e o valor do app.
- Pixelmator Photo: um resultado gerado por ML só gera confiança quando o ajuste é visível e editável, não uma caixa-preta.
- The Gardens Between: os artefatos de design revelam que o resultado final raramente parece com os primeiros rascunhos.
- Butterfly iQ: metáforas do mundo físico ajudam a criar familiaridade, mas precisam ser testadas com o público real antes de virar padrão de interface.
- Thumper: simplicidade radical na tela sustenta imersão; feedback sonoro e visual mínimo ainda ensina a mecânica.
- ELOH: um ilustrador e um sound designer dedicados elevam elementos interativos que, sozinhos, são poucos e simples.
- Ordia: uma linguagem visual consistente ("mesmo ambiente" em toda a experiência) e testes de acessibilidade (daltonismo, monocromia) elevam a percepção de qualidade.
- Flow by Moleskine: protótipos de baixa fidelidade (texto puro) resolvem a interação antes de qualquer decisão visual.

Citações curtas: "When we first launched, the experience was actually not magical." (fundador da HomeCourt, sobre a versão inicial do app que exigia tripé e luz perfeita).

<!-- visual:wwdc2019_802 -->
### O que as imagens mostram
Base: 40 de 40 folhas de quadros vistas, todos os códigos conferidos.

- A palestra usa uma prancha de design real de jogo como evidência do vocabulário visual de um produto: paletas rotuladas "PRIMARY COLORS" e "SECONDARY COLORS" em blocos quadrados, uma tabela de estados de componente com os rótulos NORMAL, PRESSED, TOGGLE e DISABLED, setas triangulares ciano numeradas de 1 a 3, botões "CLAIM" e "BUY", especificação tipográfica com "RAJDHANI Medium" e "RAJDHANI Semibold" e o alfabeto completo em maiúsculas, minúsculas e números, além de concept art a lápis anotada à mão (folha 0002, q0011 a q0013).
- O fio condutor da apresentação é uma lista fixa de seis palavras (Innovation, Trust, Refinement, Aesthetics, Inclusion, Attention to detail) que reaparece a cada troca de tema, com o item ativo em branco pleno e negrito e os demais em cinza apagado, ou seja, hierarquia por opacidade (folhas 0002, 0005, 0010, 0014, 0015, 0019, 0033, 0035, 0036, 0038 e 0039). Na folha 0023 a mesma lista aparece ao lado de três ícones de app, sem que as notas registrem qual item estava destacado.
- Dois apps diferentes aparecem com o mesmo padrão de tela de configuração: cartões de opção de igual tamanho, cada um com ícone-diagrama, rótulo curto e estado de seleção marcado por contorno colorido. No Asphalt 9 são três cartões, "TOUCHDRIVE" selecionado com contorno amarelo, "TAP TO STEER" e "TILT TO STEER", com um slider "SWIPE SENSITIVITY" abaixo (folha 0004, q0034); no HomeCourt são dois cartões em "DEVICE SETUP", com "GROUND" selecionado em contorno vermelho e legendas curtas de uma linha em cada opção (folha 0008, q0069).
- O onboarding do jogo é desenhado como camada sobre a própria cena, não como painel separado: sobre a imagem de corrida aparecem a frase de explicação e o rótulo "HOLD TO DRIFT" acompanhado do ícone circular do botão correspondente (folha 0003, q0027). Nos quadros de jogo anteriores da mesma folha só há HUD de corrida, com posição, velocímetro subindo de 85 para 110 e depois 146, e o selo "TOUCHDRIVE ON" surgindo entre q0021 e q0022.
- A eliminação de passos manuais é encenada em duas etapas. Na folha 0007 a lista numerada de sete passos aparece como texto puro, sem moldura de telefone, e logo depois com os itens 1 a 5 esmaecidos e os itens 6 e 7 em branco pleno (q0058 e q0059). Na folha 0008 a mesma lista reaparece sobreposta a uma fotografia real de quadra, agora com os itens 4 e 5 riscados por uma linha, enquanto a detecção aparece como retângulo vermelho sobre a tabela e, em quadros seguintes, como esqueleto de linhas laranja nas articulações do jogador, que muda de postura entre q0070 e q0071 (q0065, q0066, q0070 e q0071).
- A anatomia do cartão de feed do HomeCourt fica visível por diferença entre dois quadros consecutivos: mesmo cabeçalho de usuário, mesmo título de treino, mesmas estrelas e os mesmos dois números de estatística (12 e 20), trocando apenas a mídia inferior, que passa de miniatura de vídeo para um gráfico em forma de "U" com percentuais por zona da quadra, entre eles 71% e 67% (folha 0006, q0047 e q0048).
- O inspetor de ajustes do Pixelmator Photo aparece em layout de três zonas, imagem central com histograma no canto, painel direito com nome de parâmetro mais interruptor mais controle deslizante, e barra inferior de predefinições em miniaturas coloridas. A sequência de quadros mostra o estado mudando de fato: foto escura e dessaturada com interruptores acendendo em azul, depois foto clara, depois sliders saindo de zero para percentuais preenchidos (folha 0011, q0095 a q0099).
- O painel avançado do mesmo app mostra controle direto de cor além dos sliders lineares: Exposure, Highlights com valor negativo, Shadows, Brightness, Contrast e Black Point, e abaixo uma seção "Color Balance" com roda de cores circular rotulada "Master" mais a opção "3-Way Color", e uma seção "Selective Color" com gráfico de faixas de matiz, numa ordem que vai do global ao granular (folha 0013, q0112 a q0117).
- O componente nativo de iOS é dissecado na tela: o interruptor aparece ampliado e isolado nos dois estados, ligado com fundo azul e círculo à direita, desligado com fundo cinza e círculo à esquerda, e também pequeno dentro do painel real do app junto ao rótulo "White Balance", com um destaque circular translúcido aproximando o mesmo controle (folha 0034, q0299 a q0304).
- O caso do Butterfly iQ é construído por comparação direta de versões e de referências: na folha 0021 a demo de 2016 traz valores fixos na barra inferior, "11cm" de Depth e "38%" de Gain, ao lado de dois ícones quadrados, com os botões "Freeze" e "Record" abaixo (q0181 a q0183); na folha 0022 um segundo iPhone ao lado mostra o app Câmera do iOS, com ícones no topo, rótulos de modo na base e obturador circular branco, e a versão por gesto exibe um popup central "Gain/TGC" com percentual e régua vertical numerada na borda direita da imagem (q0191 a q0195). Na folha 0022 aparece ainda a medição sobre a imagem, dois pontos azuis ligados por linha amarela tracejada com o valor fixado na base.
- Os artefatos de processo mostrados são documentos técnicos, não ilustrações genéricas: uma prancha com título em caixa alta sobre um trecho de nível, desenho central e linhas vermelhas de anotação para caminho, fluxo de água e material, que ganha blocos de notas escritas entre q0158 e q0159; e uma segunda prancha sobre uma cena de despedida, com desenho de linha, diagrama em losango com círculos nos vértices e coluna de miniaturas de esboço à esquerda (folha 0018, q0158 a q0161).
- A progressão de fidelidade aparece encenada em telas reais. No Flow by Moleskine, o protótipo de baixa fidelidade é só caixas retangulares cinza com texto, sem cor e sem ícone, com um rabisco vermelho no centro; depois vem uma versão intermediária com barra de gradiente rotulada "Marker" e deslizante triangular; depois o editor final em layout de cruz, com nome da cor, valor "SIZE 5" e ícone de confirmação (folha 0037, q0325 a q0329). Em ELOH, o mesmo personagem passa de traço preto sobre branco para versão colorida em gradiente roxo e turquesa, e só então recebe a palavra de avaliação ao lado (folha 0028, q0247 a q0249).
- O mesmo componente é mostrado em dois tamanhos de tela ao mesmo tempo, iPad e iPhone lado a lado exibindo o editor de cor em cruz na mesma proporção de layout, ao lado do número grande "1,400" com a legenda de nomes de cor (folha 0038, q0335 a q0338).
- Nos jogos, a tela quase não tem interface: The Gardens Between mostra apenas um ícone de pausa no canto superior esquerdo em toda a sequência (folha 0015, q0129 a q0131), e Thumper mantém no canto superior esquerdo somente o indicador de nível, "LEVEL 2-1" em q0215 e "LEVEL 1-5" na folha 0025, com um botão de pausa ou um ícone circular numerado no canto superior direito, sem barra de vida nem outros elementos de HUD, e com a faixa indicadora de gesto do próprio iOS na base (folhas 0024 e 0025, q0215 a q0224).
- A coesão de linguagem visual de Ordia é demonstrada indo até a tela menos glamourosa: cartão translúcido de conquista no topo, mapa com contador "10/10" e a tela "SETTINGS" com interruptores nativos alinhados à direita dos rótulos, incluindo modo daltônico e sincronização, mais um botão de redefinir progresso; e uma comparação de duas telas de mapa em que o ícone de compartilhar surge ao lado do botão de play entre q0283 e q0285, destacado por contorno azul-claro em um dos dois quadros comparados (folha 0032, q0281 a q0285).
- Ferramenta de produção na tela: uma captura de software de animação em MacBook Pro, com canvas à esquerda, painel de camadas à direita, timeline horizontal com marcadores de quadro-chave e miniatura de pré-visualização no canto; entre quadros consecutivos, a expressão do rosto do personagem muda sutilmente, evidenciando o ajuste de quadros-chave (folha 0029, q0254 a q0256).

Proporção visual: pelas notas, predominam slides tipográficos e capturas de app, jogo, prancha de design e fotografia; quadros só de apresentador aparecem em boa parte das folhas, sempre em minoria dentro de cada uma, e as notas não registram nenhuma demonstração ao vivo, apenas capturas, fotografias e mockups em moldura de dispositivo.

Divergências ou limites registrados: as notas abrem uma exceção para q0072, tratado fora da descrição por quadro porque o recorte da folha 0008 traz três telas de iPhone distintas na linha inferior; na folha 0040 parte das anotações manuscritas é declarada ilegível na distância do quadro; e na folha 0035 o mesmo trio de telas aparece duas vezes seguidas sem alteração visível entre q0307 e q0310.
<!-- /visual:wwdc2019_802 -->

## Designing Great ML Experiences (id: wwdc2019_803, 57.8 min)

Base: transcrição e 42 de 42 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2019/803/.

Tese central: projetar uma boa experiência de machine learning exige desenhar tanto o modelo (os dados usados para ensiná-lo e as métricas usadas para avaliá-lo) quanto a interface (como os resultados do modelo são apresentados como output e como as pessoas dão input de volta ao modelo); design de ML vai além da tela.

O processo de design que a Apple descreve:
- Definir a experiência desejada antes de coletar dados: entender o que se quer construir e então decidir intencionalmente quais dados coletar, em vez de apenas amostrar os clientes existentes ou usar datasets acadêmicos prontos, porque isso pode reforçar vieses sistêmicos em vez de refletir o mundo desejado.
- Escolher métricas alinhadas a valores, não só a números fáceis de medir: métricas são proxies para conceitos abstratos difíceis de medir (boa experiência, cliente satisfeito, marca forte); se a experiência parece ruim mas a métrica diz que está boa, a métrica é que está errada.
- Agrupar casos de falha por categoria e cenário, decidir se cada tipo de erro é melhor resolvido com design (não-ML) ou com um modelo melhor, e desenhar deliberadamente para o cenário de falha (não só o caminho feliz) ao esboçar a experiência.
- Depois de definir dados e métricas, desenhar a interface em duas frentes: outputs (como o resultado do modelo é apresentado) e inputs (como a pessoa interage e realimenta o modelo).

Princípios enunciados e o porquê:
- "You shouldn't optimize for the customers you have. You should optimize for the customers you want" e "you should reflect a better world, that world that you want it to be": coleta de dados enviesada (por exemplo, reconhecimento facial que historicamente não funcionava bem para pessoas de cor) exige coleta intencional entre raças, culturas e cenários, não amostragem passiva.
- Métricas não contam a história toda: no Face ID, a métrica "uma chance em um milhão de um estranho destravar o telefone por acaso" foi comunicada publicamente, mas a Apple também precisou comunicar a limitação de irmãos gêmeos ou parecidos, porque cada falha é uma pessoa e um cenário reais.
- Prefira outputs com múltiplas opções quando o modelo não pode saber tudo sobre a preferência da pessoa: em Maps, em vez de uma única rota "ótima", três rotas distintas (uma para a região norte da baía, duas para a leste) dão controle real à pessoa, porque a rota ideal depende de preferências que o modelo não captura (rota cênica, sem pedágio, sem rodovia).
- Use atribuição para explicar decisões com fatos objetivos, não suposições sobre gosto ou emoção: a App Store explica recomendações dizendo "porque você baixou o app X" em vez de alegar entendimento do gosto da pessoa, porque perfilar emoções e preferências deixa as pessoas com sensação de serem mal compreendidas ou "encaixotadas".
- Traduza confiança (confidence) em linguagem compreensível: em vez de dizer "85% match", a App Store usa "recommendations based on apps you've downloaded"; já o app de clima usa porcentagem diretamente (30% de chance de chuva) porque as pessoas já aprenderam a interpretar esse número ao longo do tempo; o app de passagens Hopper evita porcentagem (não diz "65% de chance de cair o preço") e em vez disso recomenda a ação direta (esperar ou comprar agora), porque a diferença entre 65% e 70% não é acionável para a maioria das pessoas.
- Prefira faixas (ranges) a números pontuais quando a precisão exata é falsa: o app de caronas Lyft mostra uma faixa de horário de chegada em vez de um horário único, porque trânsito e paradas extras tornam qualquer número exato enganoso.
- Peça confirmação quando a confiança é baixa em vez de agir sozinho: o Photos pede confirmação de identidade de uma pessoa antes de rotular automaticamente futuras fotos dela.
- Comunique limitações e ofereça alternativas: quando o Memoji não consegue reconhecer o rosto (câmera coberta, ambiente escuro, rosto fora de quadro), a Apple usa dicas de coaching inline; quando a Siri não pode criar um timer no Mac, ela sugere um lembrete em vez de simplesmente dizer que não pode, porque entende que o objetivo (ser avisado em um horário) é o mesmo.
- Priorize feedback negativo sobre positivo em explicit feedback: feedback positivo pode ser inferido implicitamente (ler, salvar, compartilhar um artigo), então pedir "amar" cada item sobrecarrega a pessoa; para feedback negativo, usar linguagem de consequência clara ("suggest less", "hide the suggestion") em vez de rótulos ambíguos como "Dislike".
- Corrections como padrão preferencial: deixar a pessoa corrigir o resultado do modelo usando controles já conhecidos (reescrever uma palavra no teclado, arrastar o slider de rotação/corte do Photos) em vez de criar uma interface nova; isso funciona como feedback implícito para melhorar o modelo sem esforço extra percebido.

Técnicas concretas de construção de interface, com números quando falados:
- Métrica de exemplo de acurácia de modelo: "the model gave the correct prediction 75% of the time".
- Segurança do Face ID: "one-in-a-million chance that a random person could unlock your phone using Face ID".
- Confiança traduzida versus bruta: exemplo rejeitado de "85% match" trocado por texto explicativo; clima usa "30% chance" diretamente; Hopper evita casas como "65%" vs "70%" por não serem acionáveis; exemplo de má prática citado: "I'm 72% confident you'll get there at 1:30".
- Siri watch face: até 19 fontes de dados customizáveis ("customize up to 19 different data sources").
- Calibração mínima: Face ID pede para escanear o rosto duas vezes ("It asks you to scan your face twice") e depois nunca mais recalibra, mesmo com mudança de óculos, penteado ou idade; HomeCourt calibra automaticamente apontando a câmera frontal para o aro, sem desenhar linhas manuais e sem múltiplos ângulos.
- Feedback implícito no teclado: o tamanho da área de toque de cada tecla aumenta ou diminui de acordo com a palavra provável, sem alterar a aparência visual do teclado.
- Padrões de saída (outputs) descritos: multiple options, attribution, confidence, limitations.
- Padrões de entrada (inputs) descritos: calibration, implicit feedback, explicit feedback, corrections.

Exemplos citados e o que cada um ensina:
- Photos (busca "dog"): o valor de um recurso de ML não está só na interface de busca, mas nas categorias reconhecidas e no nível de qualidade de cada categoria, decisões de design tanto quanto a tela em si.
- Maps: várias rotas distintas superam uma única "melhor" rota quando as preferências da pessoa são desconhecidas ao modelo.
- Siri watch face: selecionar um subconjunto pequeno e relevante de muitas fontes possíveis (19) evita sobrecarregar uma tela pequena.
- App Store: atribuição factual ("baixou X") evita alegar entendimento de gosto; conteúdo editorial complementa recomendações puramente dirigidas por métrica de tempo de uso, para não prender a pessoa a um nicho (o exemplo dado é jogos).
- Weather / Hopper / Lyft: mesma variável (confiança/incerteza) traduzida de três formas diferentes conforme o quanto a pessoa já está acostumada ao número (porcentagem) ou precisa de ação direta (comprar agora) ou faixa (horário estimado).
- Memoji / Siri (timer no Mac): comunicar limitação no momento certo e sugerir alternativa mantém a confiança na função em vez de simplesmente falhar.
- Photos (reconhecimento de rosto), Safari (sugestões Siri), teclado (autocorreção de "Angie"/"angle"): exemplos de calibration, explicit feedback e corrections respectivamente.

Citações curtas: nenhuma citação literal entre aspas foi usada pelos apresentadores neste vídeo; o conteúdo é majoritariamente exposição direta da equipe de design da Apple (Kayur, Rubii, Cas), sem falas de terceiros citadas entre aspas.

<!-- visual:wwdc2019_803 -->
### O que as imagens mostram
Base: 42 de 42 folhas de quadros vistas, todos os códigos conferidos.

- O diagrama conceitual é montado por acréscimo, folha após folha: primeiro só a caixa verde "Interface" e um ícone de pessoa ligados por duas setas (folha 0004, q0036), depois a camada azul "Model" acima dela (folha 0006, q0052 a q0054), depois cada camada se divide em duas subcaixas, Data e Metrics dentro de Model, Outputs e Inputs dentro de Interface (folha 0007, q0055 a q0058), e por fim as subcaixas de Interface exibem quatro itens cada (folha 0016, q0144). Perto do fim o bloco reaparece sozinho, só com Interface, Outputs e Inputs (folha 0039, q0349 a q0351), e o conjunto completo, com o Model azul no topo e o ícone de pessoa embaixo, volta uma última vez (folha 0040, q0353, q0355 e q0356).
- A diferença entre código tradicional e modelo é mostrada pela mesma cadeia horizontal com a peça do meio trocada: foto de animal, logotipo do Swift, caixa de saída com o rótulo de cão, e uma hiena recebendo esse mesmo rótulo em quadros seguidos (folha 0005, q0039 a q0043). Depois o logotipo do Swift sai e entra uma barra azul vertical "Model", primeiro com três fotos de animais entrando e três rótulos saindo (folha 0006, q0048) e em seguida como três fluxos empilhados de entradas diferentes, microfone, foto e texto sendo digitado (q0049 e q0050).
- Os dados ganham tela própria: matriz uniforme de fotos com legenda de categoria sob cada imagem (folha 0007, q0062 e q0063), que volta preenchendo quase toda a tela e recebe a frase sobreposta de que os dados determinam o comportamento do modelo (folha 0008, q0064 a q0066, com a frase entrando em q0065). Em seguida vem um mosaico de rostos de etnias, idades e gêneros diferentes (folha 0008, q0069 e q0070), que ganha a legenda sobre coleta intencional em q0071.
- Os slides de recomendação prática seguem um template de checklist progressivo: título fixo no alto à esquerda, itens empilhados sem marcador, cada um entrando conforme a fala avança e permanecendo na tela. "Data Needs to Be Designed" começa com um item só (folha 0009, q0080 e q0081) e chega a quatro (folha 0010, q0082 a q0086, q0089 e q0090), e "Metrics Reflect Values" repete a mesma mecânica (folha 0015, q0128 a q0131 e q0135).
- Métrica isolada tem cartão próprio, com número enorme e rótulo pequeno embaixo, usado duas vezes na mesma composição: "75%" sobre "Accuracy" (folha 0011, q0094 e q0096) e "1 in 1,000,000" sobre "Face ID" (folha 0012, q0102, q0103 e q0105).
- O erro é apresentado como par de imagens: o retrato do apresentador em moldura branca tipo crachá aparece sozinho (folha 0012, q0106) e ganha ao lado o retrato de um homem parecido (q0107 e q0108); na folha seguinte as mesmas molduras escurecem para receber a frase de destaque sobre erros não serem todos iguais (folha 0013, q0109 e q0110).
- Cartão verde de índice com item ativo: os quatro outputs aparecem no mesmo cartão, um item em branco pleno e os demais acinzentados, percorridos um a um antes do slide de definição (folha 0017, q0145 a q0150) e retomados com o item de confiança em destaque (folha 0022, q0197 e q0198); na folha 0021 esse cartão aparece esmaecido atrás do slide de definição (q0183 e q0184). O mesmo cartão se repete para os quatro inputs, trocando o item em negrito a cada quadro (folha 0029, q0254 a q0256).
- Os exemplos nunca aparecem como esboço solto: entram na moldura do aparelho com a interface nativa reproduzida. Mapas no MacBook com painel lateral listando três rotas de 1 hr 3 min, 1 hr 5 min e 1 hr 13 min (folha 0018, q0160 e q0161); App Store no iPhone cuja legenda de atribuição muda de uma frase genérica sobre apps baixados para a citação de um app específico (folha 0021, q0184 a q0189); e, mais adiante, a mesma App Store com o selo "85% Match" (folha 0023, q0199 e q0200).
- Três tratamentos diferentes de incerteza aparecem em folhas vizinhas: o app de passagens com preço grande, botão primário azul e cartão de previsão com seta laranja para queda e vermelha para alta (folha 0024, q0208 a q0213); o app de transporte com rota roxa e lista de opções com preço alinhado à direita (folha 0025, q0219 a q0221); o app de clima com temperatura em corpo grande e faixa horária (folha 0023, q0203 a q0205).
- A calibração é mostrada como fluxo completo, não como conceito: o app de basquete com ícone laranja e, em seguida, a tela de iPad com o vídeo da quadra e a instrução de enquadrar jogador e aro (folha 0029, q0260 e q0261), depois o pedido de um arremesso e a tela verde de confirmação (folha 0030, q0262 a q0265); o Face ID com anel de progresso ao redor do rosto, "Cancel" e opções de acessibilidade nas bordas (folha 0002, q0013 e q0014), o anel completando em estágios (folha 0031, q0276 a q0278), a tela de conclusão com botão azul de largura total (folha 0031, q0272) e a tela de Ajustes com interruptores verdes e ação destrutiva em vermelho (folha 0031, q0274 e q0275).
- O ajuste invisível do teclado é tornado visível por sobreposição didática: a mesma tela de teclado aparece normal em uma série de quadros e, nos do meio, com manchas azuis cobrindo área maior do que a tecla desenhada, voltando ao normal em seguida (folha 0034, q0298 a q0303).
- A evolução do feedback explícito reutiliza o mesmo componente em vez de criar outro: dois botões redondos de coração surgem sobre a tela escurecida do Safari (folha 0035, q0313 a q0315), viram itens dentro do menu de ação nativo (folha 0036, q0317 e q0318) e no fim são trocados, no mesmo menu, por opções que nomeiam a consequência, sugerir menos de determinada fonte e esconder a sugestão (folha 0036, q0322 a q0324).
- A correção também usa controle já conhecido: em Mensagens, a palavra digitada aparece sublinhada sendo trocada pela sugestão e em seguida abre o menu com as duas opções de não corrigir (folha 0037, q0331 a q0333); depois vem a edição no app Fotos com barra inferior de ferramentas, ícones de rotação e slider, e a mesma foto em modo retrato (folha 0038, q0341 e q0342; folha 0039, q0343 a q0345).
- O fechamento troca de linguagem visual já no fim da folha 0040: slide e captura de tela dão lugar a cenas de vídeo com uma palavra sobreposta, pulso com Apple Watch e corrida (folha 0040, q0359 e q0360), cadeira de rodas e objetos sendo identificados com o iPhone em punho (folha 0041, q0361 a q0369), eletrocardiograma no relógio e desenho com caneta (folha 0042, q0371 a q0373), terminando no slide de referências e no logotipo (folha 0042, q0376 e q0377).
- A troca de apresentador é encenada no palco, não apenas anunciada: uma silhueta entra por uma escotilha no chão ao lado de uma miniatura do diagrama (folha 0016, q0140) e, na segunda troca, o novo apresentador aparece primeiro em cena ao lado do diagrama reduzido (folha 0028, q0249) e depois caminhando sozinho em fundo preto sem plateia (q0252).

Proporção visual: quase todas as 42 folhas registram slide, diagrama ou tela de produto, com os quadros só de apresentador funcionando como intervalos curtos entre esses blocos (folhas 0003, 0011 e 0032, por exemplo), e apenas as folhas 0041 e parte da 0042 ficam sem nenhuma interface na tela.
Divergências ou limites registrados: na folha 0041 as notas registram que o iPhone aparece sendo segurado e apontado para objetos, mas sem que a tela fique legível o bastante para descrever a interface; nas folhas 0025 e 0026 a tela de confirmação de rostos é registrada como um app chamado "Rubii", sem que as notas determinem de que app se trata.
<!-- /visual:wwdc2019_803 -->

## Designing Great Shortcuts (id: wwdc2019_806, 20.7 min)

Base: transcrição e 16 de 16 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2019/806/.

Tese central: um bom shortcut precisa ser escolhido com critério (nem toda ação do app vale virar shortcut), precisa ser descoberto de forma discreta dentro do app, e, quando envolve voz, precisa ser desenhado como uma conversa real com Siri, com diálogo tratado com o mesmo cuidado dado aos pixels da interface visual.

O processo de design que a Apple descreve:
1. Listar todas as coisas que o app faz e cogitar quais fazem sentido repetir por voz.
2. Avaliar cada candidato por três critérios: é valioso ou interessante repetir; é fazível por voz sem depender de visual ou toque; é invocável em muitos contextos (não só numa janela curta de tempo).
3. Tornar o shortcut descobrível dentro do app de forma discreta (não em todo item de lista), de preferência logo após a pessoa repetir uma ação que já indicou interesse.
4. Para shortcuts com Siri interativa, desenhar a conversa como um roteiro (script) primeiro, cobrindo todos os caminhos possíveis, e depois consolidar num diagrama de fluxo com todos os estados e transições.
5. Escrever e testar o diálogo repetidamente: "When in doubt, test it. Listen to Siri speak your dialog." e avaliar como o texto soa na terceira e na décima vez que é ouvido.

Princípios enunciados e o porquê, com o exemplo do app fictício SoupChef:
- Nem toda ação vira shortcut: navegar o cardápio (muito visual, exige rolagem e toque, não muda de invocação a invocação) não é um bom candidato; checar status do pedido só serve numa janela curta de tempo; ver pedidos passados não é algo que as pessoas checam com frequência; já fazer o pedido em si é valioso e repetível, logo é um bom candidato.
- Botão Add to Siri deve ser usado com moderação: colocar o botão em cada item de um menu principal "looks ugly" e não é relevante, porque a pessoa provavelmente está tentando fazer o primeiro pedido, e sugerir repetir algo nunca pedido antes não faz sentido; melhor mostrá-lo logo depois que a pessoa já fez um pedido, quando há um sinal claro de que ela pode querer repetir.
- Frases de invocação devem ser curtas: em torno de três palavras ou menos, limitadas a um substantivo próprio ou verbo mais objeto, para reduzir a chance de a pessoa trocar a ordem das palavras ou esquecer termos ao tentar lembrar a frase.
- Minimizar prompts de desambiguação apresentando uma lista de opções logo de cara quando há um conjunto fechado de opções, em vez de um prompt aberto.
- Ao ler opções em voz alta (AirPods, HomePod, "Hey Siri"), especificar dicas de pronúncia separadamente do texto visual, e ler em voz alta só o que diferencia as opções entre si (por exemplo "Beef or Veggie?" em vez de repetir "Noodle Soup" em cada opção).
- Prever sinônimos para cada opção, porque a pessoa pode responder com uma variação natural da pergunta feita (se a pergunta usa um tom mais casual, a resposta esperada também deve reconhecer esse tom).
- Usar parameter confirmation prompt com parcimônia, só para casos de consequência real, porque isso desacelera a interação.
- Usar confirmation prompt de ação inteira principalmente quando a ação tem alta consequência; para a categoria "ordering" no App Store, o sistema exige confirmação obrigatória da pessoa.
- Diálogo de voz não deve incluir uma pergunta que a Siri já formula automaticamente por categoria (categorias determinam a pergunta e o status de resposta padrão que a Siri gera; o diálogo customizado é anexado ao final).
- Prover mensagens de erro claras para reprompt automático de valores inválidos, e nunca apresentar como opção algo já sabido como inválido no momento da execução.
- Ao apresentar UI de shortcut, toda a área tocável abre o app (não desenhar elementos que pareçam individualmente interativos, porque não são), e o app deve abrir já preenchido com as informações fornecidas até aquele ponto.

Regras de escrita de diálogo (voz como interface):
- Não ser excessivamente educado nem injetar personalidade demais, porque a pessoa ouvirá o mesmo texto repetidamente e isso se torna irritante.
- Não incluir o nome do app no diálogo (o app já é atribuído visualmente pelo ícone na UI de confirmação/resposta).
- Não incluir o nome da pessoa no diálogo, porque a Siri pode já falar o nome dela no HomePod para verificação de identidade, soando repetitivo.
- Evitar pronomes em primeira pessoa ("I"/"we") porque a Siri não está executando a ação, o app está; usar "I" pode fazer a pessoa achar que a Siri entende o app melhor do que de fato entende, levando a tentativas de ação de acompanhamento que não funcionam. Preferir termos neutros como "here" ou "there are a few options".

Técnicas concretas de construção de interface citadas:
- Botão Add to Siri padrão com corner radius customizável e aparência que muda automaticamente conforme modo claro/escuro.
- Toque no botão Add to Siri revela um sheet padrão de edição/exclusão do shortcut, mostrando a frase configurada.
- Categoria do shortcut selecionada no Xcode determina a pergunta de confirmação padrão da Siri e o status padrão de resposta.
- Padrões de conversa: prompt aberto, disambiguation prompt, parameter confirmation prompt, confirmation prompt final.

Exemplos citados e o que cada um ensina:
- SoupChef (app fictício de pedido de sopa): ilustra o funil completo, da priorização de qual ação virar shortcut até o roteiro de conversa de pedido (tipo de sopa, entrega ou retirada, local ou balcão).
- "Hey Siri, bus schedule" via HomePod: mostra o caso de uso mãos e olhos livres, com resposta falada.
- Rotina noturna encadeada (pedir sopa, tocar música, mostrar rota): exemplo de shortcut multi-etapas combinando ações de vários apps.

Citações curtas: nenhuma citação literal entre aspas de terceiros aparece no texto; o vídeo é a fala direta do apresentador (Jay, designer do time Siri e Shortcuts) descrevendo diretrizes, sem trechos citados de outra pessoa.

<!-- visual:wwdc2019_806 -->
### O que as imagens mostram
Base: 16 de 16 folhas de quadros vistas, todos os códigos conferidos.

- A triagem de qual função vira atalho é feita na tela como ficha de avaliação: slide com o nome do recurso em itálico e bullets que se acumulam ao lado da captura correspondente, com um X vermelho aparecendo sobre o aparelho quando o recurso é descartado (folha 0003, q0021, q0023 e q0024, com o X entrando em q0024), um ícone de alerta laranja quando o recurso serve só em contexto específico (folha 0003, q0026) e selo positivo quando o recurso é aprovado (folha 0004, q0029), fechando com o slide dos três critérios (folha 0004, q0030).
- O erro de colocar o botão em todo item é mostrado como par: a lista de sopas com um botão "Add to Siri" repetido em cada linha, marcada com X vermelho (folha 0004, q0033, q0034 e q0036; folha 0005, q0037), contra a tela de status do pedido com um único botão no rodapé e selo verde de certo (folha 0005, q0038 e q0041).
- O botão tem anatomia mostrada peça por peça: pílula escura com o ícone colorido da Siri ao lado do texto (folha 0004, q0032), depois quatro variações de raio de canto lado a lado em um slide de fundo claro (folha 0005, q0042 e q0044) e, no quadro seguinte, um desses botões convertido no estado de atalho já adicionado, com a frase configurada e ícone de check (folha 0005, q0045).
- O fluxo de configuração aparece inteiro, tela a tela: folha modal escura listando os itens do pedido com quantidade, nome e sinal de mais azul (folha 0006, q0047 e q0049), que ganha a frase sugerida entre aspas abaixo do título em q0049, e em seguida o formulário do sistema com campo de frase preenchido, seção da ação com o ícone do app em uma linha e botão azul de largura total no rodapé (folha 0006, q0054; folha 0007, q0056 e q0060).
- O editor de ação é mostrado como frase corrida, com os valores editáveis destacados em azul dentro do texto (folha 0008, q0065 e q0067); ao lado dele entra um segundo iPhone com a pergunta de desambiguação (q0066), que evolui para a lista fechada de quatro sopas (q0068) e depois para a tela de confirmação com resumo e dois botões (q0070 e q0071).
- O roteiro de conversa aparece como artefato físico, não como texto de slide: folha de papel datilografada com as falas rotuladas alternando entre sistema e pessoa, que vira duas e depois três folhas sobrepostas conforme mais caminhos são considerados (folha 0009, q0074 a q0076), com a linha do caminho de opção indisponível realçada em azul claro (folha 0009, q0078 e q0079).
- Cada padrão de conversa recebe rótulo próprio em slide com captura ao lado: prompt de desambiguação (folha 0010, q0083), prompt com lista de opções (q0085 e q0087) e lista de opções sem display (q0088 a q0090). O cartão de exemplo repete a mesma estrutura, nome do app em corpo pequeno no topo, pergunta em negrito e as opções listadas, uma delas com fundo em gradiente indicando foco.
- A leitura em voz alta é encenada com dois aparelhos na mesma tela: HomePod com um balão de fala trazendo o texto falado, com os nomes das opções em cores diferentes dentro do balão, ao lado do iPhone mostrando a versão visual da mesma pergunta (folha 0010, q0089 e q0090); o mesmo pareamento volta no slide de dica de pronúncia, com outro texto no balão (folha 0011, q0091 e q0092).
- Os sinônimos aparecem como camadas que crescem sobre o mesmo cartão: cada opção ganha uma segunda linha em itálico com as variações aceitas, e essa linha fica mais longa de um quadro para o outro (folha 0011, q0093 a q0095). Em seguida vem a confirmação de parâmetro com valor numérico em corpo grande e dois botões de resposta (folha 0011, q0096) e a variação que propõe o pedido habitual (q0097).
- A confirmação da ação é mostrada nos dois registros: a tela com cabeçalho do app, linha de item, total e dois botões no rodapé (folha 0012, q0100, q0102 e q0104) e o mesmo momento com o balão do HomePod dizendo em voz alta tempo de entrega e preço, informações que na versão visual só aparecem de forma implícita no resumo (folha 0012, q0105, q0106 e q0108).
- A autoria do texto é marcada na própria imagem: etiquetas apontando qual trecho da frase é escrito pelo desenvolvedor e qual é determinado pela categoria (folha 0013, q0116) e, no quadro seguinte, o mesmo contraste feito por opacidade, trecho do sistema apagado e trecho customizado em branco cheio (q0117); antes disso vem a lista de categorias com verbos agrupados e a opção de pedido marcada com check (q0114 e q0115).
- Erro e contexto ganham telas de pergunta com o texto exato em vez de descrição (folha 0014, q0119 e q0120), e a área tocável recebe anotação de especificação, uma seta com rótulo apontando para todo o cartão para dizer que ele é um botão único, com a câmera se aproximando até a anotação ocupar a tela (folha 0014, q0122, q0123 e q0125).
- As regras de escrita de diálogo são demonstradas em frases isoladas com selo: saudação excessiva marcada com X e depois repetida em cópias esmaecidas ao redor para simular o efeito de ouvir aquilo muitas vezes (folha 0015, q0127 e q0128), nome da marca no texto com X (q0130), nome da pessoa com a etiqueta indicando que a Siri já acrescenta isso sozinha (q0132), e a troca da primeira pessoa por uma formulação neutra passando de X para check verde (q0133 a q0135).
- O fechamento segue o mesmo padrão de lista que se acumula, com dois bullets principais em branco e uma nota complementar em cinza abaixo, antes do corte para a tela de encerramento (folha 0016, q0136, q0137 e q0139).

Proporção visual: praticamente toda folha traz slide, captura de tela ou boneco de aparelho, e os quadros só com o apresentador funcionam como respiro entre exemplos, presentes nas folhas 0001, 0002, 0003, 0005, 0007, 0009 e 0016.
Divergências ou limites registrados: as notas observam que a fala menciona a passagem do conjunto de roteiros para um diagrama de fluxo, mas os quadros registram apenas o estágio de roteiro em papel empilhado, sem que esse diagrama chegue a aparecer.
<!-- /visual:wwdc2019_806 -->

## Building Great Shortcuts (id: wwdc2019_805, 11.9 min)

Base: transcrição e 10 de 10 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2019/805/.

Tese central: este é primariamente um vídeo de engenharia (API de Shortcuts, INIntent, Donation, input/output) apresentado por um engenheiro do time de Shortcuts; ainda assim, várias decisões de implementação carregam consequências diretas de design de texto e de descoberta que valem registrar.

Processo descrito (do ponto de vista de construção da funcionalidade, com reflexo em design):
1. Definir os parâmetros da action no arquivo de definição do Intent; cada parâmetro tem um display name mostrado até a pessoa preencher um valor.
2. Escrever o "parameter summary", uma frase que descreve o que o shortcut fará quando executado.
3. Escolher, entre os parâmetros, qual é o "key parameter" (o mais identificável para a pessoa) para que ele apareça nas sugestões do sistema.
4. Fazer "Donation" (INInteraction + Donate) toda vez que a pessoa realiza a ação no app, para alimentar sugestões na Gallery, Lock Screen e Spotlight Search.
5. Definir input e output de cada action para permitir encadear várias actions num shortcut de múltiplos passos.

Princípios enunciados e o porquê:
- O parameter summary deve ler como uma frase e começar com um verbo, sem repetir o nome do app (que já aparece no topo da action, ao lado do ícone do app), para não redundar informação já visível.
- Manter o summary curto e incluir só os parâmetros obrigatórios para a action funcionar; os demais ficam recolhidos sob "Show More", editáveis mas não expostos por padrão, para não sobrecarregar a leitura inicial.
- O display name de cada parâmetro deve sempre ficar em maiúscula inicial ("always capitalized"), porque às vezes é exibido como título em uma UI de configuração.
- A frase de invocação sugerida (suggestedInvocationPhrase) deve ser curta, descritiva da ação e fácil de falar e lembrar, porque será dita em voz alta pela pessoa.
- O app deve preencher o intent com o máximo de informação possível no momento da doação, para que o shortcut consiga repetir a ação sem perguntas de acompanhamento desnecessárias.
- O key parameter deve ser o mais identificável para a pessoa, não necessariamente o tecnicamente mais relevante: SoupChef escolheu o tipo de sopa como key parameter em vez de quantidade ou acompanhamentos, porque é o que a pessoa mais associa ao pedido.
- Incluir uma imagem para o key parameter ao doar; sem imagem, o ícone do app é usado no lugar, o que é menos específico.
- Actions devem produzir output (um tipo customizado, com propriedades) para que outras actions consigam usar o resultado como input automaticamente, reduzindo passos manuais de seleção em shortcuts de múltiplas etapas.

Técnicas concretas de construção de interface e de texto, com números quando falados:
- Botão Add to Siri: a partir do iOS 13, a pessoa pode digitar ou ditar a frase em vez de só falar, com o app pré-preenchendo suggestedInvocationPhrase.
- Seção "Do" do Add to Siri mostra uma prévia do que o shortcut fará; se o intent estiver configurável, a pessoa pode tocar para customizar valores antes de confirmar.
- Gallery do app Shortcuts, na aba mais à direita, ganhou em iOS 13 uma seção de shortcuts sugeridos a partir dos apps mais usados no aparelho.
- Editor de shortcuts mostra categorias de actions embutidas (mídia, lembretes, scripting como Loops e If) e uma lista de actions sugeridas com base no uso do dispositivo, incluindo apps de terceiros.
- Exemplo StickyNote: uma action "Find StickyNote" produz um tipo de saída com identifier, name, content e data de modificação; a action seguinte ("Add Text to Note") declara esse tipo como parâmetro de input, preenchendo-o automaticamente quando encadeada.

Exemplos citados e o que cada um ensina:
- SoupChef (pedido de sopa): ilustra parameter summary variando entre "pickup" e "delivery" conforme os valores preenchidos pela pessoa, e a escolha de key parameter.
- StickyNote (app de notas fictício): ilustra como input/output entre actions elimina seleção manual repetida ao encadear um shortcut de múltiplos passos.

Citações curtas: nenhuma citação literal entre aspas de terceiros aparece no texto; a fala é inteiramente do apresentador (Ian, engenheiro do time de Shortcuts) descrevendo a API e as recomendações de uso.

<!-- visual:wwdc2019_805 -->
### O que as imagens mostram
Base: 10 de 10 folhas de quadros vistas, todos os códigos conferidos.
- O card de ação do editor de Shortcuts é a unidade visual que se repete em quase todo o vídeo, sempre com a mesma anatomia: cabeçalho com ícone do app e nome em caixa alta pequena, frase resumo com os parâmetros em azul sublinhado e link "Show More" com seta para o que está recolhido (folha 0002, q0013 a q0018).
- Parâmetro ainda não preenchido tem tratamento visual próprio, fundo cinza claro com borda pontilhada em volta do texto, o que marca o campo como editável e vazio sem precisar de rótulo extra (folha 0002, aproximação de q0013 para q0014).
- O mesmo template de card aparece em dois apps fictícios diferentes, Soup Chef e StickyNote, sem variação de estrutura, ou seja, a identidade do app entra só pelo ícone e pelo nome, não pelo desenho do card (folhas 0002 e 0008).
- A ligação entre API e pixel é feita por legenda de código em caixa escura monoespaçada colada ao elemento que aquela propriedade produz, primeiro no campo "When I say" e depois no campo "Do" do modal (folha 0004, q0029 e q0032).
- O selo circular verde "NEW" marca pontos de novidade da API sobre o mockup, tanto no modal quanto na visão detalhada da Gallery (folha 0004, q0029; folha 0005, q0038).
- Duas rotas de código diferentes aparecem anotadas sobre o mesmo tipo de card de sugestão em quadros seguidos, INVoiceShortcutCenter.setShortcutSuggestions e depois ININteraction com donate, o que mostra na imagem que o mesmo elemento de tela pode vir de caminhos distintos (folha 0005, de q0041 para q0043).
- O bloco de código cresce em camadas ao lado de um card que não muda, primeiro só a criação do intent e a doação, depois as linhas de INImage, e o efeito mostra qual acréscimo de código produz a foto real do prato dentro do círculo de sugestão (folha 0007, q0058 a q0060).
- Sugestão do sistema usa foto real do prato em recorte circular, não ícone genérico, dentro do card "Suggestions" com subtítulo cinza sobre uso do iPhone e botão "+" ao fim da fileira (folha 0007).
- Ênfase entre itens irmãos é feita por opacidade: dos três cards da StickyNote, o em foco mantém cor plena e os outros dois escurecem, sem mudança de tamanho, posição ou moldura (folha 0008, de q0066 para q0067).
- O conceito de saída de ação é desenhado como bloco azul sólido rotulado "Sticky" com quatro propriedades empilhadas em branco, ligado ao card de origem por uma seta vertical simples (folha 0008, de q0067 para q0068).
- O encadeamento entre ações aparece como transformação de estado do parâmetro: o campo passa de placeholder genérico para um chip de variável azul com o nome "Note", enquanto o Xcode ao lado mostra o campo "Input Parameter: note" com moldura verde e texto de ajuda (folha 0009, de q0079 para q0081 e q0080).
- Um elemento de interface que surge só nesta folha, sem equivalente nas anteriores, é o dropdown azul "Select a Magic Variable" sobreposto ao card de ação, listando as variáveis disponíveis (folha 0009, q0076).
- Os slides usam fundo preto sólido e hierarquia só por peso e cor: o item corrente da agenda em branco bold, os outros dois em cinza claro, sem ícone ou marcador de posição (folha 0001, q0003 a q0009).
- A entrada do slide de agenda é animada em perspectiva, o título aparece inclinado e depois se endireita até a horizontal final, mantendo o item ativo já em negrito (folha 0001, de q0006 para q0007 e de q0007 para q0009).
- O editor de Intent no Xcode segue paleta e estrutura únicas em todas as telas mostradas, tema escuro, item ativo em azul sólido na lista lateral e formulário em seções com título em caixa alta pequena (folhas 0003, 0007, 0008 e 0009); numa dessas telas o próprio formulário embute um preview do card final (folha 0003).
- A grade de categorias do editor de Shortcuts diferencia os grupos por forma e cor do ícone, círculo cinza translúcido para "Apps", losango laranja para "Favorites", octógono preto para "Scripting", losango vermelho para "Media", em duas fileiras de quatro com rótulo pequeno abaixo (folha 0006, de q0052 para q0053).
- No fechamento, o slide "Summary" reaproveita exatamente o layout da agenda inicial, mas deixa "Discoverability" em negrito e os outros dois itens em cinza, sem estado visual que indique os três tópicos cobertos (folha 0010, de q0083 para q0084).
Proporção visual: praticamente todas as folhas mostram interface, mockup de iPhone, janela do Xcode ou slide anotado, e o apresentador aparece sozinho apenas na abertura e em passagens curtas, quase sempre em miniatura sobreposta ou ao lado da tela ampliada.
<!-- /visual:wwdc2019_805 -->

## Great Developer Habits (id: wwdc2019_239, 34.6 min)

Base: transcrição e 26 de 26 folhas de quadros vistas, códigos conferidos. Fonte: https://developer.apple.com/videos/play/wwdc2019/239/.

Aviso de escopo: este vídeo não trata de design de interface (layout, tipografia, cor, materiais, movimento, som, háptica). É uma palestra sobre hábitos de engenharia e processo de desenvolvimento (organização de projeto Xcode, controle de versão, comentários e documentação, testes, análise de performance, code review, pacotes e dependências), apresentada por um evangelista de tecnologia que também é marceneiro amador e usa a marcenaria como analogia recorrente. Está incluída no grupo porque faz parte dos ids listados, mas as seções de técnica de interface abaixo ficam vazias ou mínimas por não se aplicarem ao conteúdo real do vídeo.

Tese central: craft em desenvolvimento de app significa transformar práticas de cuidado (organização, controle de versão, comentários, testes, análise, code review, modularização, diligência com dependências) em hábitos automáticos, da mesma forma que se automatiza qualquer habilidade prática com repetição.

O processo/hábitos que a Apple descreve (não é processo de design visual, é processo de engenharia):
- Organização do projeto Xcode: usar groups que espelham a estrutura de pastas no disco (a partir do Xcode 9, criar um group também cria uma pasta real); dividir storyboards grandes em múltiplos arquivos ligados por storyboard references, em vez de um único storyboard gigante; manter o formato do projeto atualizado quando o Xcode oferecer a atualização; usar o build system novo do Xcode, padrão desde o Xcode 10.
- Controle de versão: sempre ativar Git ao criar o projeto (mesmo sendo desenvolvedor solo); commits pequenos e frequentes, localizados; mensagens de commit úteis, escritas como nota ao "eu do futuro"; usar branches para bugs e features, depois squash de volta para a branch principal.
- Comentários e documentação: um bom comentário explica o "porquê", não o "o quê" (código bem escrito já é autoexplicativo sobre o algoritmo); usar nomes de variáveis descritivos em vez de abreviações de uma letra; gerar stub de documentação no Xcode com Option-Command-Barra (opção+comando+/) posicionando o cursor na assinatura da função.
- Testes: escrever testes unitários como parte da prática regular, mesmo em trechos que parecem simples demais para quebrar, e rodá-los antes de cada commit; testes são parte de integração contínua.
- Análise e depuração: usar o Network Link Conditioner para simular rede celular típica ou ruim; ativar Address Sanitizer (corrupção de memória, buffer overflow), Thread Sanitizer (data races), Undefined Behavior Sanitizer (divisão por zero, overflow, ponteiros desalinhados) e Main Thread Checker (uso inválido de UIKit/AppKit fora da main thread); usar Debug Gauges (CPU, memória, disco, rede) e o Time Profiler do Instruments para achar trechos custosos de código.
- Code review: entender cada linha alterada, de fato compilar e rodar o projeto (não assumir que quem fez o commit já testou), rodar os testes, ler comentários e documentação, checar erros ortográficos inclusive em nomes de variáveis; na Apple, nenhum código entra em um projeto sem code review.
- Pacotes e frameworks: extrair código compartilhado (inclusive entre app principal e extensions) para frameworks, o que reduz o tamanho do binário e permite reuso entre apps; documentar bem qualquer pacote ou framework compartilhado.
- Dependências externas: antes de adicionar uma dependência, entender o que ela faz com dados do usuário, se coleta métricas desnecessárias, se envia dados para fora do dispositivo, quais outras dependências ela carrega junto, e ter um plano para o caso de ela quebrar, ficar sem manutenção ou desaparecer.

Princípios enunciados e o porquê:
- "Craft is defined as skill in planning, making, and executing": cuidado no código (não só no visual) é craft tanto quanto design de interface, mesmo que o cliente final nunca veja diretamente essas escolhas, porque elas afetam performance, confiabilidade e estabilidade.
- Detalhes de engenharia raramente são vistos diretamente pelo cliente, mas são sentidos indiretamente através de performance, confiabilidade e estabilidade.
- Código comentado "só por garantia" deve ser removido, não guardado, porque já existe no histórico do controle de versão caso seja necessário recuperar.
- Zero-warning practice: nunca commitar código com warnings, tratando warnings como erros durante a escrita, porque projetos que acumulam milhares de warnings deixam de notar novos warnings relevantes.
- Um teste unitário simples pode capturar uma regressão futura mesmo quando, no momento da escrita, não parece haver risco de quebra (exemplo pessoal do apresentador com um round-trip de serialização de Struct para dicionário).

Técnicas concretas de construção de interface: não aplicável a este vídeo (conteúdo é sobre processo de engenharia, não sobre layout, tipografia, cor, materiais, movimento, som, háptica, interação ou escrita de interface). A única menção próxima de "escrita" é sobre comentários e documentação de código, não texto voltado ao usuário final.

Exemplos citados e o que cada um ensina:
- Analogia da marcenaria (bancada organizada vs. bagunçada): espaço de trabalho desorganizado no Xcode custa tempo do mesmo jeito que uma bancada bagunçada custa tempo físico.
- Bug de serialização Struct/dicionário no app "DubDub": um teste unitário simples, sugerido por um colega (Marshall), pegou uma regressão introduzida semanas depois, que só apareceria mais tarde na UI se não fosse pego antes.
- Code review como prática de equipe na Apple: nenhum código entra sem revisão, o que uniformiza estilo e aumenta a familiaridade de todo o time com a base de código.

Citações curtas: nenhuma citação literal entre aspas de terceiros aparece no texto; a fala é inteiramente do apresentador (Josh, do time de Technology Evangelism), incluindo um diálogo reconstruído com o colega Marshall que não vem marcado como citação direta entre aspas no texto da transcrição.

<!-- visual:wwdc2019_239 -->
### O que as imagens mostram
Base: 26 de 26 folhas de quadros vistas, todos os códigos conferidos.
- A tela não mostra interface de app de usuário final em nenhum momento: o material visual é slide conceitual, foto de metáfora, diálogo do sistema e captura de ferramenta de desenvolvimento, e o único mockup de produto é um cartão de avaliação de App Store no encerramento (folha 0026, q0230 e q0231).
- Uma lista vertical de oito palavras funciona como mapa de navegação da palestra inteira, com o item corrente em branco negrito e os demais em cinza claro, sem numeração nem marcador gráfico (folha 0003, q0022 a q0025; reaparece nas folhas 0008, 0010, 0015, 0021, 0023 e 0025).
- No fechamento, essa mesma lista anda item a item quadro a quadro, acompanhando a recapitulação, sem que nada mais na composição mude de posição (folha 0025, de q0218 até q0225).
- Os slides de resumo de seção são construídos por build, com as linhas surgindo uma por quadro em vez de aparecerem juntas (folha 0008, de q0064 para q0065; folha 0013, de q0111 para q0112; folha 0018, q0157 a q0159; folha 0022, de q0196 para q0197; folha 0024, q0212 a q0214).
- O espelhamento entre projeto e disco é mostrado por duas colunas simétricas com a mesma árvore de três arquivos, distinguidas só pela cor do ícone de pasta, amarelo para o grupo do Xcode e azul para a pasta do Finder (folha 0004, q0034 a q0036).
- A ideia de dividir storyboards é feita só com forma e posição: retângulos verticais no formato de tela de app passam de nuvem desordenada para grade regular e depois para blocos ligados por linha, com cartões brancos marcando o que está ativo e cinzas o resto (folha 0005, q0037 a q0042).
- O histórico de versões vira grafo abstrato, uma linha azul central com ramos amarelo e verde de círculos conectados, sem um único rótulo de texto (folha 0009, q0078 e q0079).
- O trecho de código evolui em três estados sucessivos sobre a mesma linha, comentário fraco, comentário explicativo de duas linhas e por fim a variável renomeada de "id" para "cmsApplicationIdentifier", mantendo o mesmo valor de string (folha 0011, q0095 a q0099).
- Teste passando e depois falhando é narrado por três ícones de estado em sequência, spinner, losango verde com marca de certo e losango vermelho com X, sem nenhuma tela de teste real (folha 0014, q0122 a q0126).
- As capturas do painel de esquema do Xcode mostram os checkboxes sendo marcados um de cada vez, na mesma ordem falada, Address Sanitizer, Thread Sanitizer, Undefined Behavior Sanitizer e depois Main Thread Checker em outra seção (folha 0016, q0140 a q0143; folha 0017, de q0145 para q0146).
- O menu de perfis de rede aparece como lista de texto puro sobre fundo branco, com o item escolhido em azul e marca de seleção, e a escala de qualidade comunicada só pelo nome do perfil, sem ícone ou medidor (folha 0016, q0136 a q0138).
- As telas de diagnóstico seguem densidade alta e padrão próprio: o Disk Report abre com cartões numéricos no topo, gráficos vermelhos e tabela monoespaçada; o Instruments usa barra lateral de instrumentos e tabela hierárquica com barras de porcentagem dentro das células (folha 0017, q0149, q0150 e q0153).
- O rótulo da seção entra sobreposto à própria captura de ferramenta, no canto superior esquerdo, em vez de exigir um slide separado de transição (folha 0018, de q0154 para q0155; folha 0022, de q0193 para q0194).
- Passos de revisão de código viram três slides de frase única na mesma grade de composição, texto alinhado à esquerda no meio da tela, apresentador pequeno abaixo à direita e plateia como faixa escura no rodapé (folha 0020, q0176 a q0180).
- A ênfase antes de fechar um bloco é feita por zoom tipográfico, a frase "Have a plan." em três tamanhos crescentes até ocupar a tela sem o apresentador, seguida pelo título da seção entrando em baixa opacidade (folha 0024, q0208 a q0211).
- Transição de assunto é marcada por cor chapada e símbolo isolado, tela azul sólida sem nenhum elemento e depois um balão de fala branco sobre o mesmo azul para abrir o tópico de comentários (folha 0010, q0088 a q0090; folha 0011, q0093 e q0094).
Proporção visual: a maior parte dos quadros é apresentador no palco com slide conceitual ou foto de metáfora ao lado, com capturas reais de ferramenta concentradas nas folhas 0006, 0008, 0012, 0016 a 0018 e 0022, e vários trechos em que só o apresentador aparece, sem nada na tela.
Divergências ou limites registrados: as notas marcam texto não legível em três pontos, a linha extra em baixa opacidade no cartão "Track" (folha 0009, q0081), o texto pequeno abaixo da ilustração do novo cenário (folha 0013) e o texto do cartão de avaliação cortado na borda da tela (folha 0026); as notas também registram que, das folhas 0014 a 0026, não aparece nenhuma comparação lado a lado de certo e errado, moldura de aparelho, esboço à mão ou anotação de medida.
<!-- /visual:wwdc2019_239 -->

## O que este grupo revela sobre o jeito Apple

- Machine learning nunca é tratado como recurso mágico neutro: em wwdc2019_802 (Pixelmator Photo, HomeCourt) e em wwdc2019_803 inteiro, o discurso recorrente é que confiança só existe quando o resultado do modelo é visível, editável e explicável (atribuição), nunca uma caixa-preta.
- Simplicidade radical na interface aparece como valor tanto em jogos de entretenimento puro (Thumper, ELOH em wwdc2019_802) quanto em ferramentas utilitárias (HomeCourt, Butterfly iQ, também em 802), sugerindo que "remover obstáculo até sobrar só o essencial" é um padrão de julgamento transversal a categorias de produto muito diferentes.
- Voz é tratada como superfície de design com as mesmas exigências de rigor do visual: tanto wwdc2019_806 quanto wwdc2019_803 (padrões de confidence e attribution) repetem a instrução de nunca usar percentuais ou termos técnicos crus com o usuário final, e wwdc2019_806 detalha regras específicas de escrita de diálogo (sem nome do app, sem primeira pessoa, testar ouvindo repetidamente).
- Testar decisões de design diretamente com o público-alvo, e estar disposto a descartar ideias que "pareciam certas", aparece tanto em contexto totalmente humano (Butterfly iQ testando com médicos reais em wwdc2019_802) quanto em contexto de acessibilidade (Ordia simulando daltonismo sobre o próprio jogo, também em 802).
- Os dois vídeos de Shortcuts (wwdc2019_806, design; wwdc2019_805, engenharia) mostram a mesma ideia vista de dois ângulos: nem toda funcionalidade do app deve virar atalho, e a decisão de qual parâmetro é "mais identificável para a pessoa" (o key parameter, em 805) é, na prática, uma decisão de design aplicada dentro do código.
- wwdc2019_239 é o único vídeo do grupo cujo "cuidado" declarado (craft) está inteiramente do lado de dentro do código e do processo de engenharia, não da interface visível; isso mostra que, para a Apple, a noção de craft e atenção ao detalhe (tema também citado em wwdc2019_802, seção Flow by Moleskine) se estende explicitamente do pixel ao código-fonte.

## Sem transcrição

Nenhum dos cinco arquivos do grupo estava sem transcrição; todos continham título, fonte, duração, descrição e a transcrição falada completa.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_802.md, 194 linhas lidas (arquivo com 193 linhas segundo wc -l, sem quebra de linha final; conteúdo integral, do cabeçalho até "[ Applause ]"), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_803.md, 203 linhas lidas (arquivo com 202 linhas segundo wc -l, sem quebra de linha final; conteúdo integral, do cabeçalho até "[ Applause ]"), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_806.md, 60 linhas lidas (arquivo com 59 linhas segundo wc -l, sem quebra de linha final; conteúdo integral, do cabeçalho até "[ Applause ]"), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_805.md, 66 linhas lidas (arquivo com 65 linhas segundo wc -l, sem quebra de linha final; conteúdo integral, do cabeçalho até "[ Applause ]"), lido até o fim: sim.
- /Users/guilhermelannes/Downloads/apple-design-kb/text/transcripts/wwdc2019_239.md, 147 linhas lidas (arquivo com 146 linhas segundo wc -l, sem quebra de linha final; conteúdo integral, do cabeçalho até "[ Applause ]"), lido até o fim: sim.

Todos os cinco arquivos foram lidos em uma única chamada de Read cada, sem aviso de truncamento; nenhum precisou de leitura em partes com offset/limit.
