# Foundations (parte 1)

## Accessibility (slug: accessibility)

**O que governa:** os princípios e padrões para tornar uma interface acessível a pessoas com deficiências visuais, auditivas, motoras, de fala e cognitivas, incluindo tamanhos mínimos, contraste e comportamento de recursos assistivos do sistema.

**Por que:** a Apple define uma interface acessível como intuitiva (interações familiares e consistentes), perceptível (não depende de um único canal sensorial) e adaptável (responde tanto aos recursos de acessibilidade do sistema quanto às preferências pessoais de configuração). O raciocínio de fundo é que projetar para acessibilidade amplia o público e torna a experiência mais inclusiva para todos, não apenas para quem usa recursos assistivos.

**Faça e evite:**
- Suporte tamanhos de texto maiores; idealmente permita ampliar em pelo menos 200% (ou 140% em apps watchOS), via Dynamic Type ou UI customizada.
- Siga os tamanhos padrão e mínimos recomendados por plataforma para estilos de tipo customizados.
- Considere que fontes de peso fino (thin) precisam de tamanhos maiores que o recomendado para manter legibilidade.
- Busque atingir os padrões mínimos de contraste de cor (WCAG Level AA é usado pelo Accessibility Inspector).
- Se o app não atinge o contraste mínimo por padrão, ofereça ao menos um esquema de maior contraste quando a configuração de sistema Increase Contrast estiver ativa; verifique o contraste tanto no modo claro quanto no escuro.
- Prefira cores definidas pelo sistema, que já têm variantes acessíveis que se adaptam automaticamente a preferências de cor.
- Transmita informação por mais de um canal além da cor (formas, ícones), porque pessoas com daltonismo têm dificuldade com pares como vermelho-verde e azul-laranja.
- Descreva a interface e o conteúdo do app para o VoiceOver.
- Ofereça formas baseadas em texto de aproveitar áudio e vídeo: legendas (captions), subtítulos (subtitles), audiodescrição e transcrições, cada uma com um propósito distinto.
- Use hápticos além dos sinais sonoros (ex.: Music Haptics e Audio graphs em iOS/iPadOS) para quem não percebe o áudio.
- Reforce sinais de áudio com sinais visuais, especialmente em jogos e apps espaciais onde conteúdo importante pode estar fora da tela.
- Ofereça controles com tamanho suficiente e espaçamento adequado entre eles para reduzir toques errados.
- Suporte gestos simples para interações comuns; evite gestos customizados com múltiplos dedos ou múltiplas mãos.
- Ofereça alternativas a gestos: garanta que a funcionalidade principal esteja acessível por mais de um tipo de interação física (ex.: um botão além de um swipe para dispensar uma view).
- Rotule elementos de interface apropriadamente para permitir o uso do Voice Control.
- Integre com Siri e Shortcuts para permitir realizar tarefas só por voz.
- Suporte tecnologias assistivas relacionadas a mobilidade: VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control e Switch Control.
- Mantenha ações simples e intuitivas; prefira gestos e comportamentos já familiares do sistema a gestos customizados.
- Minimize elementos de interface com temporizador que se auto-dispensam; prefira dispensar views com uma ação explícita.
- Considere oferecer acomodações de dificuldade em jogos (ajustar critério de sucesso, tempo de reação, assistência de controle).
- Deixe as pessoas controlarem a reprodução de áudio e vídeo; evite autoplay sem controles de início/parada disponíveis e descobríveis.
- Permita que as pessoas optem por não ver luzes piscando em vídeos (configuração Dim Flashing Lights).
- Seja cauteloso com animações rápidas e piscantes; quando Reduce Motion estiver ativo, reduza animações automáticas e repetitivas, incluindo zoom, escala e movimento periférico.
- Boas práticas adicionais para reduzir movimento: apertar molas de animação para reduzir efeitos de quique, rastrear animações diretamente com os gestos das pessoas, evitar animar mudanças de profundidade no eixo z, substituir transições nos eixos x, y e z por fades, e evitar animar entrando e saindo de blurs.
- Otimize a interface para o Assistive Access (iOS/iPadOS): identifique a funcionalidade central, remova fluxos e elementos não essenciais, divida fluxos em múltiplas etapas em telas separadas focadas em uma única interação, e sempre peça confirmação duas vezes para ações difíceis de reverter, como excluir um arquivo.

**Especificações exatas:**

Tamanhos de tipo padrão e mínimo por plataforma:
| Plataforma | Tamanho padrão | Tamanho mínimo |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Contraste mínimo (WCAG Level AA, usado pelo Accessibility Inspector):
| Tamanho do texto | Peso do texto | Razão mínima de contraste |
|---|---|---|
| Até 17 pts | Todos | 4,5:1 |
| 18 pts | Todos | 3:1 |
| Todos | Negrito | 3:1 |

Tamanho de controle padrão e mínimo por plataforma:
| Plataforma | Tamanho padrão do controle | Tamanho mínimo do controle |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Espaçamento entre controles: cerca de 12 pontos de padding ao redor de elementos com bezel; cerca de 24 pontos de padding ao redor de elementos sem bezel.

Ampliação de texto recomendada: pelo menos 200% (140% em watchOS).

**Diferenças por plataforma:** o texto afirma explicitamente que não há considerações adicionais para iOS, iPadOS, macOS, tvOS ou watchOS além do já coberto. Em visionOS, há considerações específicas de conforto por causa da natureza imersiva: manter elementos de interface dentro do campo de visão da pessoa, preferir layouts horizontais a verticais (que podem causar tensão no pescoço), evitar exigir atenção em locais diferentes em rápida sucessão, reduzir velocidade e intensidade de objetos animados (especialmente na visão periférica), ser cuidadoso com movimento de câmera e vídeo, evitar ancorar conteúdo à cabeça da pessoa (pode prevenir o uso de Pointer Control) e minimizar a necessidade de gestos grandes e repetitivos. O visionOS oferece Pointer Control de cabeça e mão, e um recurso de Zoom.

**Ligações com outros artigos:** Inclusion, Typography, VoiceOver.

<!-- visual:accessibility -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações e 4 folhas de vídeo (2 vídeos, 2 folhas cada) vistas, todos os códigos conferidos.
- A abertura desenha o símbolo de acessibilidade em silhueta marrom escura sobre degradê amarelo, com grade retangular e circular pontilhada e diagonais marcando centro e proporções (img 0000); cada subtema (Vision, Hearing, Mobility, Speech, Cognitive) recebe o mesmo módulo, uma faixa amarela arredondada com exatamente cinco pictogramas marrons em compartimentos igualmente espaçados, trocando só os ícones (img 0001, 0012, 0014, 0019, 0020).
- Peso e tamanho de fonte são comparados com a mesma palavra no mesmo tipo de cartão cinza claro: pequena e em negrito num cartão menor, grande e em peso fino, com traços delgados, num cartão maior (img 0002, 0003).
- O contraste de botão vem em par certo e errado com a mesma forma de pílula: azul claro com título em azul mais escuro que quase some, marcado com X cinza (img 0004, 0005), contra azul royal com título branco, marcado com check verde (img 0006, 0007).
- A cor adaptativa é demonstrada num cartão partido ao meio com rótulos "Light" e "Dark": o systemRed padrão fica praticamente igual sobre os dois fundos (img 0008), enquanto a variante acessível escurece e satura no lado claro e clareia puxando para rosa no lado escuro (img 0009).
- Para não depender só de cor, dois círculos verde e vermelho que diferem apenas no tom (img 0010) ganham forma e símbolo: check branco no verde e octógono com X branco no vermelho (img 0011).
- Em audição, um iPhone em contorno preto com linhas de vibração nas laterais e um balão escuro com nota musical acima mostra música acompanhada de vibração (img 0013).
- O espaçamento entre controles aparece em dois estados da mesma fileira de três botões redondos azuis (voltar, play, avançar): com folga generosa (img 0015) e com contornos vermelhos tracejados sobre as áreas de toque, que se encostam sem espaço entre si (img 0016).
- A alternativa ao gesto é mostrada na mesma lista: em modo de edição, cada linha tem um botão vermelho de menos sempre visível (img 0017); com swipe, uma linha desliza e o botão "Delete" cobre parte do título e do subtítulo (img 0018).
- O Assistive Access simplifica a Câmera em fundo preto: a primeira tela tem só três alvos grandes, dois quadrados lado a lado (amarelo para foto, verde para vídeo) e um botão preto de voltar embaixo (img 0021); a tela seguinte troca as duas opções por uma prévia grande, um botão amarelo de tirar foto e o voltar (img 0022).
- O Zoom em visionOS é uma lente circular de contorno cinza sobre uma janela flutuante num ambiente doméstico real, ampliando só a região sob ela, ao contrário das ilustrações planas do resto da página (img 0023).
- No vídeo do Pointer Control por mão, uma linha branca reta com ponto na ponta sai da mão até uma estrela amarela sobre a foto do motor na janela "Rockets"; a mão fica aberta e quase parada (q001 a q003), aproxima polegar e indicador (q004 a q006), abre de novo (q007 a q009), segue em pinça leve (q010 a q012) e em q013 chega mais perto do canto inferior direito da janela; a origem e o ângulo da linha mudam, e a estrela nunca sai do lugar (vídeo 000, folhas 0001 e 0002, q001 a q013).
- No vídeo do Pointer Control por cabeça, nenhuma mão aparece: a estrela fica parada um pouco à esquerda do centro da tela enquanto janela e ambiente giram para um lado (q001 a q003), estabilizam com a janela maior e centralizada (q004 a q006), giram no sentido oposto (q007 a q009), seguem girando e revelam mais poltronas à direita (q010 a q012), invertem de novo suavemente (q013 a q015) e em q016 voltam perto do enquadramento inicial; o conteúdo se move sob um alvo fixo, em vez de um cursor se mover sobre conteúdo parado (vídeo 001, folhas 0001 e 0002, q001 a q016).
Divergências registradas: no vídeo 000, a descrição oficial fala de uma linha cujo ponteiro muda de posição conforme a mão se move, mas nos 13 quadros amostrados a cada 0,5 s o destino (a estrela) fica sempre no mesmo ponto e só a origem e o ângulo da linha variam. No vídeo 001 a descrição confere, mas não menciona a oscilação da rotação de um lado para o outro nem o retorno perto do enquadramento inicial.
<!-- /visual:accessibility -->

## App icons (slug: app-icons)

**O que governa:** como projetar o ícone do app, incluindo estrutura em camadas, forma, efeitos visuais, aparências (claro/escuro/tintado/claro translúcido) e especificações técnicas por plataforma.

**Por que:** o ícone é um elemento crucial da marca e da experiência do usuário porque aparece em múltiplos locais do sistema (Tela de Início, busca, notificações, configurações, compartilhamento). Camadas dão mais controle sobre como o design é representado, permitindo que o sistema aplique efeitos visuais que respondem ao ambiente e às interações das pessoas, criando sensação de profundidade e vitalidade. A simplicidade é valorizada porque ícones com muitos detalhes finos ficam "carregados" quando o sistema aplica sombras e destaques, e detalhes ficam difíceis de perceber em tamanhos pequenos.

**Faça e evite:**
- Prefira bordas claramente definidas nas camadas de primeiro plano; evite bordas suaves e esmaecidas para que destaques e sombras desenhados pelo sistema fiquem bem.
- Varie a opacidade nas camadas de primeiro plano para aumentar a sensação de profundidade e vivacidade.
- Projete um fundo que se destaque e ao mesmo tempo enfatize o conteúdo em primeiro plano; se usar gradiente, garanta que responda bem aos efeitos de iluminação do sistema.
- Prefira gráficos vetoriais (SVG ou PDF) ao trazer camadas para o Icon Composer; para gradientes mesh e arte rasterizada, prefira PNG.
- Produza camadas sem máscara, no formato apropriado (quadradas para iOS/iPadOS/macOS/visionOS/watchOS, retangulares para tvOS), deixando o sistema aplicar o mascaramento final.
- Mantenha o conteúdo principal centralizado para evitar corte quando o sistema ajustar cantos ou aplicar máscara.
- Abrace a simplicidade: encontre um conceito ou elemento que capture a essência do app, com número mínimo de formas.
- Prefira um fundo simples (cor sólida ou gradiente) que dê ênfase ao design principal.
- Forneça um design de ícone visualmente consistente em todas as plataformas suportadas.
- Considere basear o design em formas sólidas sobrepostas, especialmente combinadas com transparência e desfoque, para dar sensação de profundidade.
- Inclua texto somente quando essencial; texto não suporta acessibilidade nem localização, costuma ser pequeno demais para ler e pode deixar o ícone com aspecto carregado. Evite palavras não essenciais como "Watch", "Play", "New" ou "For visionOS".
- Prefira ilustrações a fotos e evite replicar componentes de UI ou capturas de tela do próprio app.
- Não use réplicas de produtos de hardware da Apple (protegidos por direitos autorais).
- Deixe o sistema cuidar de desfoque e outros efeitos visuais; não é necessário incluir destaques especulares, sombras entre camadas, bordas chanfradas, desfoques ou brilhos.
- Crie agrupamentos de camadas para aplicar efeitos a várias camadas de uma vez, quando fizer sentido para o design.
- Mantenha os recursos visuais do ícone consistentes entre as aparências (padrão, escura, clara translúcida, tintada); evite trocar elementos entre variantes.
- Use o ícone claro como base para o ícone escuro, escolhendo cores complementares e evitando imagens excessivamente brilhantes.
- Considere oferecer ícones alternativos em iOS, iPadOS, tvOS e apps compatíveis rodando em visionOS; cada ícone alternativo precisa permanecer relacionado ao conteúdo e experiência do app, e ícones alternativos em iOS/iPadOS exigem suas próprias variantes escura, clara translúcida e tintada.

**Especificações exatas:**

Layout, forma final, tamanho, estilo e aparências por plataforma:
| Plataforma | Forma do layout | Forma do ícone após mascaramento | Tamanho do layout | Estilo | Aparências |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Quadrado | Retângulo arredondado (quadrado) | 1024x1024 px | Em camadas | Padrão, escura, clara translúcida, escura translúcida, tintada clara, tintada escura |
| tvOS | Retângulo (paisagem) | Retângulo arredondado (retangular) | 800x480 px | Em camadas (Parallax) | N/A |
| visionOS | Quadrado | Circular | 1024x1024 px | Em camadas (3D) | N/A |
| watchOS | Quadrado | Circular | 1088x1088 px | Em camadas | N/A |

Espaços de cor suportados: sRGB (cor), Gray Gamma 2.2 (escala de cinza), Display P3 (cor de gamut amplo em iOS, iPadOS, macOS, tvOS e watchOS apenas).

Camadas em tvOS: entre duas e cinco camadas.
Camadas em visionOS: uma camada de fundo mais uma ou duas camadas sobrepostas.
Camadas em iOS, iPadOS, macOS e watchOS: uma camada de fundo e uma ou mais camadas de primeiro plano.

**Diferenças por plataforma:** iOS, iPadOS e macOS usam ícones quadrados com máscara para cantos arredondados combinando com a curvatura de outros elementos e o bisel do próprio dispositivo. tvOS usa ícones retangulares, também com bordas concêntricas; requer zona de segurança porque o sistema pode cortar conteúdo nas bordas durante o foco e o efeito parallax, e recomenda-se evitar preto no fundo do ícone segundo o texto sobre watchOS (evitar que o ícone se funda com o fundo do display, aplicável a watchOS). Em visionOS e watchOS, a máscara é circular; em visionOS, evitar formas que pareçam buraco ou área côncava no fundo, pois sombra e destaques especulares do sistema fariam a forma se destacar em vez de recuar.

**Ligações com outros artigos:** Apple Design Resources, Icon Composer, Icons, Images, Dark Mode.

<!-- visual:app-icons -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações e 2 folhas de vídeo (1 vídeo) vistas, todos os códigos conferidos; parte das ilustrações tem versão clara e escura.
- A abertura é o esboço do "A" da App Store sobre amarelo, com grade tracejada retangular, circular e diagonal, círculo inscrito e diagonais cruzando os cantos; na versão clara há um segundo quadrado arredondado deslocado atrás do principal, que some na escura, onde o fundo vira dourado mais escuro e o ícone amarelo claro, invertendo o contraste (img 0077).
- A mesma flor de Fotos troca só de moldura por plataforma, com o conteúdo interno idêntico: quadrado arredondado para iOS, iPadOS e macOS, retângulo arredondado alongado para tvOS e círculo para visionOS e watchOS; na versão escura apenas o fundo da página fica preto e os ícones continuam claros (img 0078).
- O Icon Composer aparece como ferramenta real: camadas nomeadas em grupos aninhados à esquerda, a flor montada no centro e, à direita, as propriedades da camada selecionada, com opacidade 100%, blend mode normal, preenchimento sólido, "Liquid Glass Effects" ligado, imagem em SVG, posição x e y em 0 pt e escala 100%; no modo escuro a interface escurece e a arte mantém as cores (img 0079).
- A engrenagem de Ajustes é construída sobre grade quadriculada dupla (módulos finos e uma malha mais grossa por cima), círculo grande inscrito tocando as bordas internas, círculo menor concêntrico e diagonais em X de canto a canto (img 0080); a mesma grade é reaplicada ao retângulo de tvOS, com quadriculado e diagonais esticados e círculos ainda centrados (img 0081), e ao círculo, com a grade num quadrado imaginário inscrito (img 0082).
- Nas versões escuras dessas grades, a engrenagem e a posição de cada guia não mudam; fundo e linhas trocam para preto e branco, e o quadriculado fino desaparece no retângulo de tvOS e fica discreto perto das bordas do círculo, restando círculo de referência e diagonais (img 0080, 0081, 0082).
- A economia de formas é mostrada em ícones do sistema: Podcasts, em roxo, com círculos concêntricos que afunilam até um centro claro de onde desce uma gota alongada (img 0083), e Home, em branco, com casa laranja em camadas aninhadas até uma porta bege, mais uma chaminé lateral (img 0084).
- A profundidade por sobreposição é ensinada em par certo e errado sobre fundo quadriculado de transparência, com o mesmo par de círculos azuis concêntricos: a primeira versão recebe o selo X cinza (img 0085, 0086); na aprovada, o círculo externo não tem contorno e tem preenchimento semitransparente que deixa o xadrez aparecer, e o círculo sólido parece pousado sobre ele, com selo de check verde (img 0087, 0088).
- As aparências formam uma grade de 3 por 2 com a flor de Fotos e rótulo sob cada célula: em cima padrão colorido, clara translúcida (fundo cinza translúcido, flor em cinza e branco) e tintada clara (fundo roxo, flor em roxo claro); embaixo escura (fundo preto, flor colorida), escura translúcida (fundo preto translúcido, flor cinza) e tintada escura (preto arroxeado, flor em roxo escuro). Na versão escura da folha só o fundo da página muda (img 0089).
- A zona segura de tvOS é um retângulo tracejado branco dentro do ícone azul acinzentado, apontado pela chamada "Safe zone"; a engrenagem cabe inteira nele, com margem visível até a borda externa, e no modo escuro só a página em volta muda (img 0090).
- No vídeo, a tela inicial do visionOS mostra ícones circulares sobre o ambiente real desfocado em duas fileiras: a da frente nítida (Safari, Fotos, Notes) e a de trás desfocada e cortada no topo, o que sugere hierarquia de foco por nitidez e desfoque, não por escala (vídeo 004, folha 0001, q001 a q009).
- No ícone de Fotos, q001 mostra pétalas com menos brilho e, de q004 a q009, o fundo branco parece avançar levemente e as pétalas ganham definição, o que sugere pequena mudança de profundidade entre as camadas, sem deslocamento lateral perceptível do ícone na tela (vídeo 004, folha 0001, q001 a q009).
- Na segunda folha, Freeform entra à esquerda de Safari e Notes sai pela direita, com o resto da composição estável de q010 a q015, o que mostra a fileira de ícones rolando na horizontal (vídeo 004, folha 0002, q010 a q015).
Divergências registradas: a descrição oficial do vídeo fala de movimento para mostrar paralaxe no ícone de Fotos, mas os quadros mostram só variação discreta de nitidez e de profundidade entre as camadas, sem deslocamento lateral perceptível; a troca de ícones na fileira (entra Freeform, sai Notes) não é citada na descrição.
<!-- /visual:app-icons -->

## Branding (slug: branding)

**O que governa:** como expressar a identidade de marca de um app ou jogo de forma reconhecível, sem comprometer a familiaridade e a experiência consistente da plataforma.

**Por que:** a lógica central é que a marca deve reforçar, não competir com, a experiência da plataforma e o conteúdo do app. Usar padrões e componentes já familiares faz a experiência parecer confiável desde o início, permitindo que as pessoas foquem no que torna o app único. Espaço de tela usado só para exibir um ativo de marca é espaço tirado do conteúdo que as pessoas realmente querem.

**Faça e evite:**
- Use a voz e o tom exclusivos da marca em toda comunicação escrita.
- Aplique a cor de destaque (accent color) da marca com critério; usá-la amplamente demais pode sobrecarregar a interface e diluir seu impacto. Minimize seu uso em controles e reserve-a para ações primárias ou indicadores de status (como badges de conteúdo não lido, ou o ícone da aba selecionada em uma tab bar). Para expressar a marca por cor, considere mover a cor para a camada de conteúdo, onde ela rola sob controles em Liquid Glass e é captada dinamicamente.
- Considere usar uma fonte customizada, desde que legível em todos os tamanhos e compatível com recursos de acessibilidade como negrito e Dynamic Type; pode funcionar bem usar a fonte customizada para títulos e subtítulos enquanto usa fontes do sistema para corpo de texto e legendas.
- Expresse a marca usando componentes familiares; ao customizar a aparência de um componente, garanta que tamanho, posicionamento e comportamento continuem preservando uma experiência familiar e apropriada para a plataforma.
- Garanta que a marca sempre ceda espaço ao conteúdo; incorpore a marca de forma refinada e discreta.
- Ajude as pessoas a se sentirem confortáveis usando padrões consistentes: posicione a UI em locais esperados, use símbolos padrão para ações comuns, confie em convenções estabelecidas de navegação e modalidade.
- Resista à tentação de exibir o logo repetidamente pelo app, a menos que seja essencial para dar contexto.
- Evite usar uma launch screen como oportunidade de branding, já que ela desaparece rápido demais para transmitir informação; considere em vez disso uma tela de boas-vindas ou onboarding que incorpore conteúdo de marca no início da experiência.
- Siga as diretrizes de marca registrada da Apple; marcas registradas da Apple não podem aparecer no nome ou nas imagens do app.

**Especificações exatas:** o texto não traz números, medidas ou valores específicos nesta página.

**Diferenças por plataforma:** o texto afirma explicitamente que não há considerações adicionais para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

**Ligações com outros artigos:** App Store Marketing Guidelines, Show more with app previews, Color.

<!-- visual:branding -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (2 de 2), todos os códigos conferidos; nenhum vídeo listado para a página.
- A abertura é um megafone em contorno marrom escuro sobre degradê amarelo, com grade tracejada retangular e círculo centralizado servindo de guia de construção; conforme a descrição oficial, o megafone sugere comunicação e o amarelo é uma das seis cores do logo da Apple (img 0184).
- O exemplo a evitar é o Mapas no iPhone com o mapa em cinza claro quase monocromático, pontos de interesse em vermelho vivo, pino de localização num tom entre roxo e azul e a cor de destaque azul espalhada pelos controles: barra de busca e botão circular de navegação (img 0185).
- O exemplo recomendado repete a mesma composição do mapa do aeroporto, mas leva o azul para a camada de conteúdo, com o mapa em tons de azul claro e médio e prédios em azul, sem aplicar a cor aos controles; os pontos de interesse continuam vermelhos para manter o contraste (img 0187).
- Os dois exemplos são variações quase idênticas do mesmo mapa, com o layout reaproveitado para o antes e o depois; o que os contrapõe é onde a cor de marca está aplicada, nos controles ou no conteúdo (img 0185, img 0187).
- O julgamento vem de um par fixo de selos, sempre isolados e centralizados em fundo branco, sem nenhum elemento da interface: X cinza em círculo cinza claro para o errado (img 0186) e check verde em círculo verde para o certo (img 0188).
- As duas folhas trazem apenas versões claras das imagens (img 0184 a 0188).
<!-- /visual:branding -->

## Color (slug: color)

**O que governa:** o uso de cor em apps e jogos, incluindo cores do sistema, cores customizadas, cor em Liquid Glass, gestão de espaço de cor, e as definições de cores dinâmicas por plataforma.

**Por que:** o uso criterioso de cor melhora a comunicação, evoca a marca, dá continuidade visual, comunica status e feedback, e ajuda as pessoas a entender informação. Cores do sistema já são definidas para funcionar bem em diferentes fundos e modos de aparência, e podem se adaptar automaticamente a configurações de vibrância e acessibilidade, o que torna a experiência "em casa" no dispositivo.

**Faça e evite:**
- Evite usar a mesma cor para significar coisas diferentes; use cor de forma consistente, especialmente quando ela comunica status ou interatividade.
- Garanta que todas as cores do app funcionem bem em contextos claro, escuro e de contraste aumentado; quando possível, use cores do sistema, que já definem variantes para esses contextos. Se definir cor customizada, forneça variantes clara e escura, e uma opção de contraste aumentado para cada variante. Mesmo que o app tenha apenas um modo de aparência, forneça cores claras e escuras para suportar a adaptividade do Liquid Glass.
- Teste o esquema de cores do app sob diferentes condições de iluminação (luz forte deixa cores mais escuras e foscas; ambientes escuros deixam cores mais brilhantes e saturadas); em visionOS, cores podem parecer diferentes conforme as cores do ambiente físico ao redor refletem luz.
- Teste o app em dispositivos diferentes, incluindo displays True Tone e diferentes perfis de cor.
- Considere como arte e translucidez afetam cores próximas.
- Se o app permite que as pessoas escolham cores, prefira os controles de cor fornecidos pelo sistema.
- Evite depender só de cor para diferenciar objetos, indicar interatividade ou comunicar informação essencial; ofereça a mesma informação de forma alternativa (rótulos de texto, formas de glifo).
- Evite cores que dificultem a percepção do conteúdo; contraste insuficiente faz ícones e texto se misturarem ao fundo.
- Considere como as cores usadas podem ser percebidas em outros países e culturas (ex.: vermelho comunica perigo em algumas culturas, mas tem conotação positiva em outras).
- Evite codificar valores de cor do sistema diretamente no código (hard-code); os valores reais podem flutuar entre versões. Use APIs como Color para aplicar cores do sistema.
- Evite redefinir o significado semântico de cores dinâmicas do sistema (ex.: não usar a cor de separador como cor de texto).
- Em Liquid Glass, aplique cor com moderação ao material e a símbolos ou texto sobre o material; reserve cor para elementos que realmente se beneficiam de ênfase, como indicadores de status ou ações primárias. Para enfatizar ações primárias, aplique cor ao fundo, não a símbolos ou texto. Evite adicionar cor ao fundo de múltiplos controles ao mesmo tempo.
- Evite usar cores semelhantes em rótulos de controle se o app tiver um fundo colorido; prefira aparência monocromática para toolbars e tab bars em apps com fundos ricos visualmente, ou escolha uma cor de destaque com diferenciação visual suficiente.
- Esteja atento à posição da cor na camada de conteúdo, evitando sobreposição de cores semelhantes entre a camada de conteúdo e os controles.
- Aplique perfis de cor às imagens para garantir que as cores apareçam como pretendido em diferentes displays.
- Use cor ampla (wide color) para melhorar a experiência visual em displays compatíveis; quando apropriado, use o perfil de cor Display P3 a 16 bits por pixel (por canal) e exporte imagens em PNG.
- Forneça variações de imagem e cor específicas por espaço de cor, se necessário, para evitar problemas de gradientes cortados em displays sRGB.

**Especificações exatas:**

Contraste mínimo entre cores (Dark Mode, artigo Color): razão de contraste não inferior a 4,5:1; para cores customizadas de primeiro e segundo plano, buscar razão de 7:1, especialmente em texto pequeno (esta especificação aparece no artigo Dark Mode, referenciado a partir de Color).

Cores do sistema (valores RGB, aparência padrão clara e escura, e contraste aumentado claro e escuro): Red, Orange, Yellow, Green, Mint, Teal, Cyan, Blue, Indigo, Purple, Pink, Brown, cada uma com quatro variantes de valor RGB documentadas na tabela de especificações da página (Default light, Default dark, Increased contrast light, Increased contrast dark). visionOS usa os valores padrão de cor escura (dark) para as cores do sistema.

Cores de cinza do sistema em iOS/iPadOS: systemGray, systemGray2, systemGray3, systemGray4, systemGray5, systemGray6, cada uma com variantes de valor RGB para padrão claro, padrão escuro, contraste aumentado claro e contraste aumentado escuro.

Perfil de cor wide color: Display P3 a 16 bits por pixel (por canal), formato de exportação PNG.

**Diferenças por plataforma:**
- iOS, iPadOS: define dois conjuntos de cores de fundo dinâmicas (system e grouped), cada um com variantes primária, secundária e terciária; define cores dinâmicas de primeiro plano como label, secondaryLabel, tertiaryLabel, quaternaryLabel, placeholderText, separator, opaqueSeparator e link.
- macOS: define uma extensa lista de cores dinâmicas do sistema (ex.: controlAccentColor, controlBackgroundColor, labelColor, linkColor, separatorColor, windowBackgroundColor, entre outras), acessíveis também no painel de cores padrão. A partir do macOS 11, é possível especificar uma cor de destaque (accent color) do app para customizar botões, realce de seleção e ícones de sidebar; se a pessoa define sua cor de acento do sistema para algo diferente de "multicolor", o sistema substitui a cor do app pela escolhida, exceto para ícones de sidebar com cor fixa.
- tvOS: considere uma paleta de cores limitada que combine com o logo do app; evite usar apenas cor para indicar foco (escala sutil e animação responsiva são os meios primários).
- visionOS: use cor com moderação, especialmente sobre vidro (glass), pois o Material padrão deixa luz e objetos do ambiente físico aparecerem através do vidro, afetando a legibilidade; prefira cor em texto em negrito e áreas grandes; em experiência totalmente imersiva, mantenha níveis de brilho equilibrados para conforto visual, evitando objetos muito brilhantes sobre fundos muito escuros.
- watchOS: use cor de fundo para apoiar conteúdo existente ou fornecer informação adicional (ex.: cada view de infográfico em Activity tem fundo que combina com a cor do anel); evite cor de fundo em tela cheia em views que ficam visíveis por longos períodos, como treino ou reprodução de áudio; reconheça que complicações gráficas podem preferir modo tintado (cor única baseada na cor selecionada pela pessoa) em vez de cor plena.

**Ligações com outros artigos:** Dark Mode, Accessibility, Materials, Apple Design Resources.

<!-- visual:color -->
### O que as ilustrações mostram
Base: 42 folhas de ilustrações vistas (hig-img_color), todas abertas e com códigos conferidos; a página não tem vídeo.
- A ilustração de abertura desenha uma paleta de pintor com uma grade de construção pontilhada sobreposta, com linhas verticais, horizontais e um círculo concêntrico. Na versão escura a relação de luminosidade se inverte: a paleta, antes mais escura que o fundo amarelo, passa a ser creme sobre um fundo mostarda (img 0254).
- A mesma tela do Notes aparece em quatro versões com composição idêntica: padrão claro, contraste aumentado claro, padrão escuro e contraste aumentado escuro. O botão de confirmação no canto superior direito mantém o fundo amarelo em Liquid Glass nas quatro; o que muda é o símbolo, branco nas versões padrão e preto nas de contraste aumentado. A seleção de texto usa realce amarelo claro atrás da palavra, com o menu de edição de texto visível (img 0255, 0256, 0257, 0258).
- Inclusão cultural de cor é mostrada com o mesmo gráfico do Stocks, mesmos valores e mesma curva: em inglês a alta é uma linha verde com gradiente verde que se dissolve em transparente abaixo dela; em chinês a mesma alta é vermelha, com as abas de período traduzidas e o período de um mês selecionado nos dois (img 0259, 0260).
- Cor no Liquid Glass é ensinada com recortes isolados do controle, sem moldura de aparelho. O botão circular azul com check branco não muda de tom sobre fundo branco e sobre fundo preto; só o fundo em volta inverte (img 0261).
- Na tab bar em cápsula, de cantos bem arredondados e sombra leve, o item selecionado leva azul no ícone e no rótulo e ganha um fundo levemente acinzentado atrás do ícone. O item não selecionado nunca recebe a cor de destaque: ícone preto no claro, branco no escuro, rótulo em cinza; no escuro a barra fica translúcida e escura (img 0262).
- O vidro absorve a cor do conteúdo atrás dele: um botão de compartilhar sobre uma foto de flores e montanha aparece visivelmente tingido de rosa e azul (img 0263).
- O par de uso excessivo e uso comedido reaproveita a mesma barra de ferramentas acima de um título em negrito, com um X à esquerda, um par de botões ao centro e um check à direita. Numa versão os três controles têm fundo azul; na outra só o do check é azul e os demais ficam em cinza neutro, claro no modo claro e escuro no modo escuro. Na versão com os três azuis, entre os modos só mudam o fundo da tela e o título, que passa a branco no escuro (img 0264, 0266). Os marcadores isolados de exemplo aparecem como um círculo cinza com X branco e um círculo verde com check branco, sem texto (img 0265, 0267).
- A gestão de espaço de cor é explicada com o diagrama de cromaticidade em forma de língua e dois triângulos de contorno preto: o maior rotulado Display P3 contém o menor rotulado sRGB. Na versão escura só o fundo em volta muda (img 0268).
- A cor de destaque do macOS aparece como painel de ajustes real: a linha de cor tem nove círculos em ordem fixa (multicolor, azul, roxo, rosa, vermelho, laranja, amarelo, verde, cinza), o multicolor selecionado com anel azul, e abaixo o seletor da cor de realce de texto com um círculo em gradiente. A versão escura mantém ordem e seleção (img 0269).
- As cores do sistema são documentadas como cartões mínimos: um quadrado de cantos arredondados com os três valores RGB escritos ao lado, sem nome da cor nem contexto de uso. Cada cartão é mostrado sobre fundo branco e sobre fundo preto com valor idêntico, de modo que só o fundo muda. Os cartões vêm em blocos de quatro por matiz, e o terceiro de cada bloco é sempre o mais escuro; no vermelho, por exemplo, 255, 56, 60, depois 255, 66, 69, depois 233, 21, 45 e por fim 255, 97, 101 (img 0270 a 0317). Inferência: a contagem de quatro por matiz coincide com as quatro variantes que o texto documenta, mas as imagens não rotulam qual cartão é qual variante.
- A escala de cinzas do iOS e iPadOS usa o mesmo formato de cartão em 24 imagens, fora de ordem de luminosidade, com valores entre 28, 28, 30 no mais escuro e 242, 242, 247 no mais claro. Alguns valores se repetem em posições diferentes (142, 142, 147 nas img 0318, 0319 e 0324; 174, 174, 178 nas img 0321, 0322 e 0328). Nos extremos o contraste com o fundo cai muito: o cinza mais claro tem contraste bem sutil sobre branco, e o mais escuro fica quase indistinguível sobre preto (img 0318 a 0341).

Divergências registradas: a legenda oficial trata a img 0265 como marca de uso incorreto, mas a imagem mostra apenas um botão cinza neutro com X branco, sem sinal visual de erro.
<!-- /visual:color -->

## Dark Mode (slug: dark-mode)

**O que governa:** a configuração sistêmica de aparência escura, incluindo a paleta de cores, o uso de ícones e imagens, e o tratamento de texto na aparência escura.

**Por que:** Dark Mode fornece uma experiência de visualização confortável adaptada a ambientes de pouca luz. As pessoas esperam que os apps respeitem essa preferência sistêmica; ter uma configuração de aparência específica do app cria trabalho extra para as pessoas, que teriam de ajustar mais de uma configuração, e pode dar a impressão de que o app está quebrado por não responder à escolha sistêmica.

**Faça e evite:**
- Evite oferecer uma configuração de aparência específica do app.
- Garanta que o app fique bem nos dois modos de aparência, incluindo a configuração Auto, que alterna entre claro e escuro conforme as condições mudam ao longo do dia, potencialmente enquanto o app está em execução.
- Teste o conteúdo para garantir legibilidade confortável nos dois modos, incluindo com Increase Contrast e Reduce Transparency ativados (separadamente e juntos); atenção especial a texto escuro sobre fundo escuro no Dark Mode.
- Em casos raros, considere usar apenas uma aparência escura na interface, por exemplo em um app que suporta visualização imersiva de mídia, para que a UI recue e ajude o foco no conteúdo.
- Abrace cores que se adaptam à aparência atual: cores semânticas (como labelColor e controlColor em macOS, ou separator em iOS/iPadOS) se adaptam automaticamente. Para cor customizada, adicione um Color Set asset no catálogo de assets do Xcode, especificando as variantes clara e escura. Evite valores de cor fixos que não se adaptam.
- Amoleça a cor de fundos brancos: se exibir uma imagem de conteúdo com fundo branco, considere escurecer levemente a imagem para evitar que o fundo "brilhe" no contexto do Dark Mode.
- Use SF Symbols sempre que possível, pois eles se adaptam automaticamente ao Dark Mode.
- Projete ícones de interface separados para as aparências clara e escura, se necessário (ex.: um ícone de lua cheia pode precisar de um contorno escuro sutil no fundo claro, mas nenhum no fundo escuro).
- Garanta que imagens e ícones coloridos fiquem bons nas duas aparências; use o mesmo asset se funcionar em ambas, ou crie assets separados via catálogo de assets.
- Use as cores de rótulo (label) fornecidas pelo sistema, que se adaptam automaticamente.
- Use views do sistema para desenhar campos e views de texto, para que o texto fique bom em todos os fundos, ajustando automaticamente à presença ou ausência de vibrância.

**Especificações exatas:**
- Razão de contraste mínima entre cores: 4,5:1.
- Para cores customizadas de primeiro e segundo plano, buscar razão de contraste de 7:1, especialmente em texto pequeno.

**Diferenças por plataforma:** o texto afirma que não há considerações adicionais para tvOS, e que Dark Mode não é suportado em visionOS nem em watchOS.
- iOS, iPadOS: usa dois conjuntos de cores de fundo no Dark Mode, chamados base e elevated, para reforçar a percepção de profundidade quando uma interface escura está em camada sobre outra. As cores base são mais escuras (fazendo interfaces de fundo parecerem recuar) e as elevated são mais claras (fazendo interfaces de primeiro plano parecerem avançar). O sistema muda automaticamente de base para elevated quando uma interface está em primeiro plano, como um popover ou modal sheet, e também usa a cor elevated para dar separação visual entre apps em multitarefa e entre janelas.
- macOS: quando a pessoa escolhe a cor de destaque "graphite" nas configurações gerais, o macOS faz os fundos de janela captarem cor do papel de parede atual do desktop (chamado desktop tinting). Recomenda-se incluir alguma transparência em fundos de componentes customizados quando apropriado, para que eles captem cor do fundo da janela quando o desktop tinting estiver ativo, mas apenas em componentes com fundo ou bezel visível, e apenas em estado neutro (sem uso de cor).

**Ligações com outros artigos:** Color, Materials, Typography, Accessibility.

<!-- visual:dark-mode -->
### O que as ilustrações mostram
Base: 4 folhas de ilustrações vistas (hig-img_dark-mode), todas abertas e com códigos conferidos; a página não tem vídeo.
- A ilustração de abertura mostra três anéis concêntricos, cada um com metade preenchida em marrom e metade vazia, alternando o lado entre anéis, com uma grade de construção pontilhada de linhas retangulares e diagonais sobreposta. Na versão escura o fundo fica dourado e as metades antes marrons passam a amarelo quase branco: figura e fundo trocam de papel, mantendo a mesma matiz amarela, em vez de uma simples troca de preto por branco (img 0411).
- Uma captura real do Stocks no iPhone em modo escuro mostra a construção inteira sobre fundo preto: cabeçalho com S&P 500 e AAPL, cartão preto com o detalhe da ação, gráfico de linha verde do último mês e tabela de dados abaixo, com texto em branco e verde (img 0412).
- As cores do sistema são apresentadas como uma grade 2 por 2 de amostras (azul, verde, roxo, magenta) dentro de um quadrado arredondado. No par, o quadrado passa de cinza claro a quase preto e as quatro amostras mudam apenas um pouco de saturação, sem perder a identidade (img 0413, 0414).
- Para ícone simples, a solução é uma borda: a gota preta sólida dispensa contorno sobre fundo branco, e sobre fundo preto a mesma forma preta ganha um contorno branco fino que a mantém visível (img 0415, 0416).
- Para ilustração complexa, a solução é refazer os valores internos, não pôr borda. A cena em traço de duas pessoas a uma mesa redonda, legível sobre branco, perde os contornos quando colocada sobre preto, porque cabelo, roupa e cadeiras escuros se fundem ao fundo; na versão corrigida roupas e cadeiras passam a branco ou cinza claro e os cabelos clareiam, e a cena volta a ler (img 0417, 0418, 0419).
- O par de texto mostra a palavra de rótulo em preto sobre branco, solta e sem forma de botão, e depois em branco dentro de um retângulo preto de cantos arredondados centralizado, onde a forma de botão aparece desenhada (img 0420, 0421).
- A hierarquia de rótulos é uma escala de quatro linhas empilhadas com contraste decrescente: label no contraste máximo, secondaryLabel em cinza claro, tertiaryLabel em cinza médio e quaternaryLabel em cinza escuro quase invisível. A mesma escala se repete, na mesma ordem, sobre preto (base), sobre cinza escuro um pouco mais claro que o preto (elevated) e sobre branco, onde label passa a preto (img 0422, 0423, 0424).

Divergências registradas: a descrição oficial da img 0420 fala em ilustração de um botão na aparência clara, mas a imagem mostra só a palavra solta, sem retângulo, borda ou preenchimento de botão.
<!-- /visual:dark-mode -->

## Icons (slug: icons)

**O que governa:** o design de ícones de interface (glifos), distintos dos ícones de app: sua simplicidade, consistência visual, alinhamento óptico, formato de arquivo, e o catálogo de SF Symbols padrão para ações comuns. Cobre também ícones de documento no macOS.

**Por que:** ao contrário do ícone de app, que pode usar detalhes visuais ricos, um ícone de interface precisa comunicar uma ideia única de forma instantânea e universal. Muitos detalhes tornam o ícone confuso ou ilegível; formas visuais familiares diretamente relacionadas à ação ou ao conteúdo tornam o reconhecimento mais rápido.

**Faça e evite:**
- Crie um design reconhecível e altamente simplificado, usando metáforas visuais familiares.
- Mantenha consistência visual entre todos os ícones de interface do app: tamanho, nível de detalhe, espessura de traço (peso) e perspectiva consistentes, sejam ícones customizados ou do sistema.
- Combine o peso dos ícones de interface com o peso do texto adjacente, a menos que se queira enfatizar um ou outro.
- Se necessário, adicione padding a um ícone customizado para alcançar alinhamento óptico (não apenas geométrico), especialmente em ícones assimétricos.
- Forneça uma versão de estado selecionado de um ícone de interface somente se necessário; componentes padrão do sistema (toolbars, tab bars, botões) já atualizam a aparência do estado selecionado automaticamente.
- Use imagens inclusivas: prefira figuras humanas neutras em gênero e evite imagens difíceis de reconhecer entre culturas ou idiomas diferentes.
- Inclua texto no design somente quando essencial para o significado; se precisar exibir caracteres individuais, localize-os; se precisar sugerir um trecho de texto, desenhe uma representação abstrata e inclua versão espelhada para contextos da direita para a esquerda.
- Se criar um ícone de interface customizado, use formato vetorial como PDF ou SVG, que escala automaticamente para displays de alta resolução; alternativamente, crie um SF Symbol customizado.
- Forneça rótulos de texto alternativo (descrições de acessibilidade) para ícones de interface customizados, para que o VoiceOver possa descrevê-los.
- Evite usar réplicas de produtos de hardware da Apple; use apenas imagens disponíveis em Apple Design Resources ou os SF Symbols que representam produtos Apple.

**Especificações exatas:** a página traz uma extensa tabela de "ícones padrão" mapeando ações comuns (Cut, Copy, Paste, Done, Cancel, Delete, Undo, Redo, Compose, Duplicate, Rename, Move to, Attach, Add, More, Select, Deselect, Superscript, Subscript, Bold, Italic, Underline, Align Left, Center, Justified, Align Right, Search, Find, Filter, Share, Print, Account, Dislike, Like, Bring to Front, Send to Back, Bring Forward, Send Backward, Alarm, Archive, Calendar) aos nomes exatos de SF Symbols correspondentes (ex.: `scissors`, `document.on.document`, `checkmark`, `xmark`, `trash`, `arrow.uturn.backward`, `square.and.pencil`, `folder`, `paperclip`, `plus`, `ellipsis`, `checkmark.circle`, `textformat.superscript`, `bold`, `italic`, `underline`, `text.alignleft`, `magnifyingglass`, `square.and.arrow.up`, `printer`, `person.crop.circle`, `hand.thumbsdown`, `hand.thumbsup`, `square.3.layers.3d.top.filled`, `square.3.layers.3d.bottom.filled`, `alarm`, `archivebox`, `calendar`, entre outros listados).

Ícones de documento no macOS, tamanhos das imagens de fundo (background fill):
- 512x512 px @1x, 1024x1024 px @2x
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

Tamanhos da imagem central (center image), medindo metade do canvas do ícone de documento:
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

Margem para a imagem central: cerca de 10% do canvas da imagem; a imagem deve ocupar cerca de 80% do canvas (ex.: em canvas de 256x256 px, a maior parte da imagem central caberia em área de 205x205 px).

Menor tamanho de exibição de um ícone de documento: 16x16 px.

**Diferenças por plataforma:** o texto afirma que não há considerações adicionais para iOS, iPadOS, tvOS, visionOS ou watchOS.
- macOS: cobre em detalhe os ícones de documento (document icons), tradicionalmente com aparência de papel com o canto superior direito dobrado; se o app não fornecer ícone de documento para um tipo de arquivo suportado, o macOS cria um automaticamente compondo o ícone do app com a extensão do arquivo. É possível fornecer combinação de fundo (background fill), imagem central e texto; deve-se evitar colocar conteúdo importante no canto superior direito do fundo, pois o sistema desenha ali a dobra branca. O sistema exibe por padrão a extensão do arquivo na base do ícone, mas é possível fornecer um termo mais descritivo (ex.: "scene" em vez de "scn"); o sistema capitaliza automaticamente cada letra do texto.

**Ligações com outros artigos:** App icons, SF Symbols.

<!-- visual:icons -->
### O que as ilustrações mostram
Base: 29 folhas de ilustrações vistas (hig-img_icons), todas abertas e com códigos conferidos; a página não tem vídeo.
- A ilustração de abertura traz o símbolo da tecla Command com guias de construção por cima, feitas de linhas retas e um círculo tracejado. Na versão escura o traço passa a creme sobre um fundo dourado mais escuro e opaco, e a grade continua visível, mais discreta (img 0561).
- A consistência de tamanho é ensinada com uma faixa de quatro glifos sólidos (câmera, coração, envelope, despertador) entre duas linhas tracejadas que marcam o limite comum de altura, com uma linha vermelha sólida no meio marcando o centro óptico. Só os sinos do despertador passam um pouco da linha superior, e apenas nos detalhes finos, não no corpo. Numa segunda versão os detalhes internos (lente da câmera, linhas do envelope) aparecem em azul como marcação didática. No escuro a faixa fica vinho, os glifos ficam creme e as guias permanecem no mesmo lugar (img 0562, 0563).
- A centralização óptica vem em três etapas sobre o mesmo glifo de download dentro de um disco. Primeiro, barras rosa de altura igual no topo e na base marcam o centro geométrico. Depois o glifo sobe alguns pixels em relação a essas barras, deixando mais espaço embaixo, e um retângulo rosa translúcido sobre o glifo mostra o padding que já incorpora o deslocamento. Por fim, os dois discos aparecem lado a lado sem marcação alguma, e a diferença é só um leve deslocamento vertical. Nas versões escuras discos e glifo invertem de cor, mas marcações e medidas não saem do lugar (img 0564, 0565, 0566).
- O estado selecionado aparece numa cápsula de barra de ferramentas com dois botões sobre fundo compartilhado: o ativo, maior, tem o círculo inteiro preenchido de azul com o glifo de filtro em branco; o inativo mostra só as reticências em cor neutra sobre o cinza claro da cápsula. No escuro o azul do selecionado não muda, e as reticências passam de preto a branco (img 0567).
- A localização de glifos é mostrada no próprio painel do app SF Symbols: quadro grande com o símbolo, nome técnico em negrito embaixo e uma lista de localização com uma linha por idioma, cada uma com a miniatura do caractere localizado à esquerda e o nome à direita. Para o símbolo de página de texto, a lista tem duas linhas, esquerda para direita e direita para esquerda, cada miniatura mostrando as linhas de texto na orientação correspondente (img 0568, 0569).
- Os ícones padrão de ação são apresentados como glifo único, isolado e centralizado, sem grade nem cartão, preto sobre branco e branco sobre preto com forma idêntica (img 0570 a 0610). Ações inversas são o espelhamento horizontal da mesma seta curva, como em desfazer e refazer (img 0576, 0577). O mesmo lápis muda de sentido pela composição: sozinho para renomear, sobreposto à quina de um quadrado para compor (img 0578, 0580). Selecionar é um check dentro de um círculo só contornado; desmarcar é um X solto, sem moldura (img 0585, 0586).
- Os ícones de formatação usam a própria letra como corpo e aplicam nela a variação que a ação representa: A com um 1 pequeno acima ou abaixo, B em peso bem mais grosso, I em itálico, U com traço de mesma espessura logo abaixo (img 0587 a 0591). Os quatro ícones de alinhamento são sempre quatro linhas empilhadas, e só o alinhamento varia: bordas à esquerda, eixo central, bordas à direita em espelho do primeiro, e larguras todas iguais no justificado (img 0592 a 0595).
- Glifos compostos e hierarquia por preenchimento: localizar sobrepõe uma lupa pequena ao canto inferior direito de um documento com linhas (img 0597); a conta de usuário é um círculo de contorno com cabeça e ombros abstratos, sem rosto, os ombros cortados pela borda (img 0601); curtir e não curtir usam a mesma mão só em contorno, com o polegar para cima ou para baixo (img 0602, 0603). Na ordenação de camadas, losangos isométricos empilhados na diagonal, três para frente e fundo e dois para avançar e recuar uma camada, indicam a camada em foco apenas por preenchimento sólido contra contorno, sem mudar a forma (img 0604 a 0607).
- Os ícones de documento do macOS compartilham a mesma silhueta de folha com canto superior direito dobrado e variam só fundo, imagem central e rótulo em maiúsculas na base (JPG em cinza; AR OBJECT, SWIFT e SCENE). O de projeto preenche todo o corpo de azul, com o rótulo numa faixa horizontal na base, e o do TextEdit enche o corpo com uma página de texto corrido, sem símbolo central nem rótulo visível (img 0611, 0612, 0613, 0614, 0619, 0624).
- A composição em camadas aparece desmontada antes do resultado: primeiro o preenchimento de fundo sozinho, uma grade rosa que clareia para baixo, cortada por uma linha branca de eletrocardiograma e sem contorno de página; depois o coração vermelho isolado; depois a palavra do rótulo em cinza, que no escuro vira cinza claro e não branco puro; e por fim as três camadas compostas no ícone de documento (img 0615, 0616, 0617, 0618).
- A mesma arte se simplifica ao encolher: na primeira redução, pixelizada, a grade tem menos linhas, o eletrocardiograma engrossa e o texto ainda aparece; na seguinte a grade some, o texto fica ilegível e o coração continua reconhecível; na mínima resta só o coração borrado num quadrado rosa muito claro (img 0618, 0620, 0621, 0622).
- A margem do ícone é a única medida numérica anotada na página: um quadrado externo rosa com um quadrado branco centralizado dentro, o coração ocupando quase todo o branco, e um colchete no topo com a marca de 10% para a largura da margem. No escuro a margem vira vinho e o quadrado interno fica preto, com a marca no mesmo lugar (img 0623).

Divergências registradas: na img 0623 a margem aparece em rosa, enquanto o texto alternativo oficial fala em azul. Na img 0564 o texto alternativo fala em barras nas duas imagens, mas a marcação aparece só na figura da direita.
<!-- /visual:icons -->

## Images (slug: images)

**O que governa:** como entregar arte com resolução, formato e escala apropriados para cada dispositivo e plataforma, incluindo fator de escala, formatos de arquivo recomendados, imagens em camadas com efeito parallax (tvOS), fotos e cenas espaciais (visionOS), e PDFs autoescaláveis (watchOS).

**Por que:** dispositivos diferentes exibem imagens em resoluções diferentes; um ponto é uma unidade abstrata de medida que mantém o conteúdo visual consistente independentemente de como é exibido. Fornecer assets de alta resolução para cada fator de escala garante que a arte não fique pixelada, esticada ou comprimida em diferentes densidades de pixel.

**Faça e evite:**
- Forneça assets de alta resolução para todas as imagens bitmap do app, para cada dispositivo suportado, identificando o fator de escala com "@1x", "@2x" ou "@3x" no nome do arquivo.
- Em geral, projete imagens na resolução mais baixa e escale para cima para criar os assets de alta resolução; ao usar formas vetorizadas redimensionáveis, posicione pontos de controle em valores inteiros para alinhamento limpo em 1x (que se mantém alinhado em 2x e 3x, múltiplos de 1x).
- Inclua um perfil de cor em cada imagem.
- Sempre teste imagens em uma variedade de dispositivos reais.
- Em tvOS, use elementos de interface padrão para exibir imagens em camadas, para que recebam o tratamento parallax automaticamente ao entrar em foco.
- Em tvOS, identifique camadas lógicas de primeiro plano, meio e fundo: primeiro plano para elementos proeminentes (personagem de jogo, texto em capa de álbum ou pôster), meio para conteúdo secundário e efeitos como sombras, fundo como pano opaco.
- Em tvOS, mantenha texto em primeiro plano, a menos que se queira obscurecê-lo.
- Em tvOS, mantenha a camada de fundo opaca (obrigatório; gera erro se não for opaca).
- Em tvOS, mantenha a camada simples e sutil (o parallax é projetado para ser quase imperceptível).
- Em tvOS, deixe uma zona de segurança ao redor das camadas de primeiro plano, já que conteúdo pode ser cortado quando a imagem em camadas escala e se move ao ser focada.
- Em tvOS, sempre pré-visualize imagens em camadas ao longo do processo de design, e finalmente em uma TV real.
- Em visionOS, prefira arte vetorial para imagens 2D, evitando conteúdo bitmap que pode não escalar bem.
- Em visionOS, se precisar usar imagens rasterizadas, equilibre qualidade e performance ao escolher a resolução; resoluções acima de @6x podem impactar a performance de execução.
- Em visionOS, para fotos espaciais, use o formato stereo HEIC; prefira o efeito de fundo de vidro emplumado (feathered glass background effect) para exibir texto sobre fotos espaciais.
- Em visionOS, exiba fotos e cenas espaciais em views isoladas (não embutidas junto com outro conteúdo), para evitar desconforto visual.
- Em watchOS, em geral evite transparência para manter os arquivos de imagem pequenos, exceto em imagens de complicação, ícones de menu e outros ícones de interface que servem como imagens de modelo (template images), onde o sistema usa a transparência para determinar onde aplicar cor.
- Em watchOS, use PDFs autoescaláveis para fornecer um único asset para todos os tamanhos de tela, projetando para as telas de 40mm e 42mm em 2x.

**Especificações exatas:**

Fatores de escala recomendados por plataforma:
| Plataforma | Fatores de escala |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x e @3x |
| visionOS | @2x ou superior |
| macOS, tvOS | @1x e @2x |

Formatos recomendados por tipo de imagem:
| Tipo de imagem | Formato |
|---|---|
| Trabalho bitmap ou raster | Arquivos PNG des-interlaçados |
| Gráficos PNG que não requerem 24-bit full color | Paleta de 8-bit |
| Fotos | Arquivos JPEG (otimizados) ou HEIC |
| Fotos estéreo ou espaciais | Stereo HEIC |
| Ícones planos e outra arte plana que precisa de escala em alta resolução | PDF ou SVG |

Escala de imagem para PDF autoescalável em watchOS, por tamanho de tela:
| Tamanho da tela | Escala da imagem |
|---|---|
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

Camadas em imagens em camadas (tvOS): entre duas e cinco camadas distintas.

**Diferenças por plataforma:** o texto afirma que não há considerações adicionais para iOS, iPadOS ou macOS.
- tvOS: cobre em detalhe o efeito parallax e imagens em camadas; imagens em camadas são obrigatórias para o ícone do app tvOS, e fortemente recomendadas (mas opcionais) para outras imagens focáveis, incluindo Top Shelf images. É possível incorporar imagens em camadas no app ou obtê-las de um servidor de conteúdo em tempo de execução, usando o formato `.lcr` gerado a partir de arquivos LSR ou Photoshop via ferramenta de linha de comando `layerutil`.
- visionOS: pessoas podem visualizar imagens em uma faixa muito maior de tamanhos do que em qualquer outra plataforma, e o sistema escala dinamicamente a resolução da imagem para o tamanho atual; ícones de app são compostos de duas a três camadas que se movem em taxas sutilmente diferentes ao entrar em foco. Cobre spatial photos (fotos estéreo com metadados espaciais, capturadas no iPhone 15 Pro ou posterior, Apple Vision Pro ou câmera compatível) e spatial scenes (imagem 3D gerada de uma imagem 2D, com efeito parallax responsivo ao movimento da cabeça).
- watchOS: cobre PDFs autoescaláveis e a recomendação de evitar transparência para tamanho de arquivo, com exceções para imagens de template.

**Ligações com outros artigos:** Apple Design Resources; App icons (para o Layer design de ícone visionOS); Color management.

<!-- visual:images -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações (hig-img_images) e 4 folhas de vídeo (hig-vid_images__012, quadros q001 a q037) vistas, todas abertas e com códigos conferidos.
- A ilustração de abertura coloca o glifo de imagem, com moldura arredondada, círculo e silhueta de montanhas, num retângulo de cantos arredondados em gradiente amarelo, com o glifo num amarelo mais escuro e semitransparente. Por cima vêm guias de construção: linhas pontilhadas horizontais, verticais e diagonais em X, mais uma grade de círculos concêntricos alinhada ao glifo (img 0630).
- O fator de escala é mostrado com a mesma forma, um círculo preto, desenhada sobre grades de pixels quadrados visíveis de tamanho crescente: 10 por 10 células, depois cerca de 20 por 20, depois cerca de 30 por 30. Na menor, a borda é serrilhada e usa pixels cinza intermediários para suavizar; na maior, os pixels quase não se percebem. A forma não muda, só a contagem de pixels por lado (img 0631, 0632, 0633).
- O vídeo do ícone de app do tvOS separa camadas pela velocidade de movimento: o cartão vermelho de cantos arredondados e o anel branco ficam praticamente fixos, enquanto o rosto do panda vermelho, em primeiro plano, passa da esquerda para quase o centro e depois para a direita, repetindo essa trinca ao longo de toda a amostra (vídeo, folha 0001, q001 a q009; folhas 0002 a 0004, até q037).
- O fundo não fica totalmente parado: um brilho diagonal claro surge no canto superior esquerdo do cartão nos quadros em que o rosto está quase no centro e some nas posições extremas, quando a luz fica plana (vídeo, folha 0001, q002 e q005).
- A intensidade desse brilho muda de um ciclo para outro, com a mesma amplitude de deslocamento do rosto: em q012 ele fica mais forte e mais amplo, cobrindo quase um quarto do cartão, em q027 aparece mais amplo e mais claro que nos quadros centrais vizinhos, e em q014 e q017 é mais discreto (vídeo, folhas 0002 e 0003).
- Há indício de escala junto com a translação: em q036 o cartão aparece mais estreito nas laterais, como se a composição se aproximasse, com o rosto quase centralizado, e em q037 volta a uma largura próxima da dos quadros anteriores (vídeo, folha 0004, q035 a q037).

Divergências registradas: a descrição oficial do vídeo diz apenas que o ícone se move para mostrar a paralaxe; os quadros acrescentam o movimento lateral cíclico e a variação de brilho no fundo, que a descrição não menciona. Nenhum quadro mostra o ícone parado ou um estado final diferente, e a amostra de 37 quadros parece cobrir só uma repetição contínua do mesmo ciclo, sem início nem fim distintos.
<!-- /visual:images -->

## Immersive experiences (slug: immersive-experiences)

**O que governa:** o design de experiências imersivas em visionOS: os estilos de imersão (mixed, progressive, full), transições entre eles, uso de passthrough, exibição de mãos virtuais e criação de ambientes customizados.

**Por que:** em visionOS, apps podem rodar no Shared Space (junto com outras experiências, como no Mac) ou em um Full Space (sozinhos, ocultando outras experiências). O raciocínio central é o conforto e o controle da pessoa: nem toda tarefa se beneficia de imersão, e mesmo quando se beneficia, as pessoas frequentemente querem permanecer ancoradas ao seu entorno físico e manter a capacidade de usar outros apps e recursos do sistema simultaneamente.

**Faça e evite:**
- Ofereça múltiplas formas de usar o app, incluindo suporte aos recursos de acessibilidade que as pessoas usam para personalizar a interação.
- Prefira lançar o app no Shared Space ou usar o estilo de imersão `mixed`, dando às pessoas mais controle para escolher quando aumentar a imersão.
- Reserve a imersão para momentos e conteúdos significativos; nem toda tarefa precisa ser totalmente imersiva.
- Ajude as pessoas a se engajarem com momentos-chave usando pistas como dimming, tinting, movimento e escala, começando com pistas sutis e reforçando-as apenas quando houver boa razão.
- Prefira cores de tinta sutis para o passthrough (disponível a partir do visionOS 2), evitando tons brilhantes ou dramáticos que distraiam e diminuam a sensação de imersão.
- Seja cuidadoso com o conforto visual: prefira posicionar conteúdo 3D dentro do campo de visão das pessoas, e exiba movimento de formas confortáveis enquanto o app roda em um Full Space.
- Escolha um estilo de imersão que suporte os movimentos que as pessoas podem fazer durante o uso; evite os estilos `progressive` ou `full`, ou volte para `mixed`, se as pessoas puderem precisar se mover além do limite de 1,5 metro.
- Evite incentivar movimento durante uma experiência progressive ou totalmente imersiva; projete formas de interagir com o conteúdo sem se mover (ex.: trazer um objeto virtual para perto da pessoa em vez de esperar que ela se aproxime).
- Se usar o estilo `mixed`, evite obscurecer demais o passthrough.
- Adote ARKit se quiser combinar conteúdo customizado com o entorno da pessoa; solicite permissão quando precisar de dados sensíveis como posição das mãos.
- Projete transições suaves e previsíveis ao mudar de nível de imersão, evitando transições súbitas e desorientadoras.
- Deixe as pessoas escolherem quando entrar ou sair de uma experiência mais imersiva, fornecendo uma ação clara de entrada/saída; evite exigir controles do sistema para reduzir a imersão.
- Indique o propósito de um controle de saída (se retorna a um contexto menos imersivo ou encerra a experiência por completo).
- Ao exibir mãos virtuais, prefira que correspondam a características familiares (posições e gestos das mãos da pessoa); use cautela com mãos virtuais maiores que as mãos reais da pessoa, pois podem obstruir a visão e parecer desproporcionais; se houver interrupção nos dados de rastreamento de mão, esmaeça as mãos virtuais e revele as mãos reais da pessoa, sem deixá-las congeladas.
- Ao criar um ambiente customizado, minimize conteúdo distrativo, ajude a distinguir objetos interativos (por proximidade), mantenha a animação sutil, crie um ambiente expansivo (evitando sensação de claustrofobia), use Spatial Audio para criar atmosfera evitando repetição excessiva, evite usar uma imagem 360 graus plana isolada (prefira malhas de objeto com iluminação e shaders), ajude as pessoas a se sentirem ancoradas fornecendo um plano de chão (ground plane mesh), e minimize a redundância de assets.

**Especificações exatas:**
- O sistema define um limite (boundary) que se estende cerca de 1,5 metro a partir da posição inicial da cabeça da pessoa nos estilos `progressive` e `full`. Quando a cabeça se aproxima desse limite, a experiência começa a esmaecer e o passthrough aumenta; ao ultrapassar o limite, os visuais imersivos são substituídos no espaço pelo ícone do app.
- Faixa padrão de imersão no estilo `progressive`: de 120 a 360 graus (é possível definir uma faixa customizada).
- O estilo `full` exibe um ambiente customizado de 360 graus que substitui completamente o passthrough.

**Diferenças por plataforma:** este artigo é específico de visionOS; o texto afirma explicitamente que não é suportado em iOS, iPadOS, macOS, tvOS ou watchOS.

**Ligações com outros artigos:** Spatial layout, Motion, Accessibility, Privacy.

<!-- visual:immersive-experiences -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações (hig-img_immersive-experiences) e 3 folhas de vídeo (hig-vid_immersive-experiences__013, quadros q001 a q020) vistas, todas abertas e com códigos conferidos.
- A ilustração de abertura usa uma forma abstrata côncava, parecida com uma ampulheta deitada de laterais retas e bordas superior e inferior curvadas para dentro, em amarelo mais escuro semitransparente sobre retângulo arredondado em gradiente amarelo, com grade reta em X e grade de círculos concêntricos por cima. A forma lembra a armação de um visor, mas não é um desenho literal do aparelho (img 0638).
- O esmaecimento do passthrough é mostrado com a mesma sala de estar e o mesmo painel grande de vidro fosco e embaçado ao centro, sem conteúdo legível. Na primeira versão o ambiente em volta está nítido e com luz normal; na segunda ele fica visivelmente mais escuro, com sombras mais profundas, enquanto o painel mantém aproximadamente o mesmo brilho, o que aumenta a diferença de tom entre janela e entorno (img 0639, 0640).
- No estilo misto, objetos do app entram no espaço real e convivem com a mobília da sala: uma cadeira de diretor dobrável, um tripé com câmera de filmagem antiga e uma escrivaninha de madeira de desenho diferente do resto. Ao fundo aparecem uma escada e uma porta envidraçada que não estavam nas duas imagens anteriores (img 0641).
- No estilo progressivo, os mesmos objetos de primeiro plano e o painel ficam iguais, mas o entorno muda: paredes mais estreitas, escada à esquerda, luz geral mais escura e amarelada, banquinho e cadeira mais angulosos à direita, misturando elementos com aparência real a uma ambientação escura e uniforme (img 0642).
- No estilo total, o primeiro plano continua o mesmo e o entorno vira uma galeria fechada de paredes terracota, com pinturas abstratas coloridas emolduradas dos dois lados, sem nenhum vestígio da sala (img 0643).
- A série isola uma única variável: o painel de vidro fosco fica na mesma posição e proporção em todas as capturas (img 0639 a 0643), e os objetos do app ficam fixos da img 0641 à 0643, de modo que só muda quanto do ambiente real é substituído.
- O vídeo abre com uma paisagem externa (lago, pedras ocres, árvores, morro, céu azul) e um recorte retangular menor, levemente rotacionado, no canto superior esquerdo, com outra cena de água e vegetação. O enquadramento se abre a cada quadro, a faixa de pedras ocres ganha área e mais árvores entram pela direita, enquanto o recorte fica praticamente no mesmo lugar e tamanho. Nesse trecho não há borda, texto nem controle (vídeo, folha 0001, q001 a q009).
- Em q010 surge um controle circular pequeno, cinza translúcido, com ícone de montanhas, à direita do recorte, e ele fica praticamente no mesmo lugar dali em diante enquanto o fundo muda por trás (vídeo, folha 0002, q010 a q018; folha 0003, q019 e q020).
- A troca de ambiente é uma mescla gradual, não um corte: a partir de q015 uma cena interna com estante de madeira e luminária articulada entra pela direita em transparência sobre a paisagem, cresce quadro a quadro e empurra o exterior para a esquerda, com uma linha diagonal de transição bem visível em q016, q017 e q018 (vídeo, folha 0002, q014 a q018).
- No fim, a sala interna (sofá cinza, almofada azul escura, planta, estante, mesa de centro, tapete, quadro na parede) ocupa quase todo o quadro, restando no canto superior esquerdo só uma fração da paisagem e do recorte original; o controle circular agora aparece sobre a parede clara. Entre q019 e q020 quase nada muda (vídeo, folha 0003, q019 e q020).

Divergências registradas: a descrição oficial do vídeo fala em ajuste pela Digital Crown que revela mais do ambiente físico, mas os quadros não mostram mão nem Digital Crown, só o resultado da transição. Inferência, não registrada nas notas como divergência: as notas tratam a paisagem externa como passthrough e a sala interna como ambiente customizado, leitura oposta à da descrição oficial, que fala em revelar mais do ambiente físico.
<!-- /visual:immersive-experiences -->

## Inclusion (slug: inclusion)

**O que governa:** os princípios de design inclusivo: linguagem acolhedora, identidade de gênero, representação de pessoas e ambientes, como evitar estereótipos, acessibilidade e considerações de idioma/localização.

**Por que:** apps e jogos inclusivos colocam as pessoas em primeiro lugar, priorizando comunicação respeitosa e apresentando conteúdo e funcionalidade de formas que todos possam acessar e entender. O raciocínio da Apple é que um app "não ofensivo" não é necessariamente um app inclusivo; o foco deve estar em criar uma experiência acolhedora para todos, o que exige empatia para entender como pessoas com perspectivas diferentes podem responder ao conteúdo e às experiências criadas. Design inclusivo é descrito como um processo iterativo que exige tempo e disposição para examinar as próprias suposições.

**Faça e evite:**
- Considere o tom da redação (copy) a partir de perspectivas diferentes; seja claro, direto e respeitoso.
- Preste atenção em como se refere às pessoas: geralmente funciona bem usar "você" e "seu"; referir-se indiretamente como "o usuário" ou "o jogador" pode deixar a experiência distante; reserve "nós" e "nosso" para representar o software ou a empresa.
- Evite termos técnicos ou especializados sem defini-los.
- Substitua expressões coloquiais por linguagem simples, pois expressões coloquiais costumam ser específicas de cultura e difíceis de traduzir, e algumas têm origens excludentes (o texto cita "peanut gallery" e "grandfathered in" como exemplos de frases com origem opressiva).
- Considere cuidadosamente antes de incluir humor, que é altamente subjetivo e difícil de traduzir entre culturas.
- Apresente uma interface clara e direta, e construa formas de aprender a usar o app, como um fluxo de onboarding.
- Evite referências desnecessárias a gêneros específicos; prefira linguagem neutra em gênero (o texto dá um exemplo de reescrita de frase para remover pronomes de gênero desnecessários).
- Evite referenciar um gênero específico em avatar, emoji, glifo ou personagem de jogo; prefira dar às pessoas ferramentas para customizar esses itens como quiserem.
- Se precisar retratar uma pessoa genérica, use uma imagem humana não generizada; SF Symbols oferece muitos glifos não generizados.
- Se precisar de informação de gênero (por razões de saúde ou legais), considere opções inclusivas como não binário, autoidentificação e "prefiro não dizer", e considere permitir que as pessoas especifiquem os pronomes que usam.
- Ao retratar pessoas, mostre uma variedade de características e atividades humanas; evite representações estereotipadas (ex.: mostrar só médicos homens ou enfermeiras mulheres).
- Revise os ambientes e objetos mostrados; prefira mostrar lugares, casas, atividades e itens familiares e identificáveis pela maioria das pessoas.
- Esteja consciente de vieses e generalizações inconscientes que podem influenciar decisões de design; evite basear decisões em definições estereotipadas (o texto dá o exemplo de um app de gerenciamento de acesso familiar que assume uma definição estereotipada de família).
- Evite perguntas de segurança baseadas em experiências específicas de cultura ou capacidade (o texto dá exemplos de perguntas problemáticas e de alternativas mais universais).
- Suporte recursos de acessibilidade da Apple (VoiceOver, Display Accommodations, legendas fechadas, Switch Control, Speak Screen); evite assumir que uma deficiência impediria alguém de querer aproveitar a experiência.
- Reconheça que cada deficiência é um espectro, e que todos podem experimentar deficiências, incluindo temporárias e situacionais.
- Evite imagens e linguagem que excluam pessoas com deficiência; use linguagem centrada na pessoa (people-first) ao escrever sobre pessoas com deficiência, e descubra como a pessoa ou comunidade se autoidentifica.
- Priorize simplicidade e perceptibilidade.
- Prepare o software para lidar com idiomas e regiões diferentes do seu próprio (internacionalização) antes de fornecer texto e recursos traduzidos para localidades específicas; usar SF Symbols pode ajudar a simplificar a localização, incluindo glifos específicos de idioma e glifos para contextos da esquerda para a direita e da direita para a esquerda.
- Esteja atento a como usa cor ao localizar, já que cores têm significados fortemente específicos de cultura (o texto cita branco associado à morte ou luto em alguns lugares, e à pureza ou paz em outros).

**Especificações exatas:** o texto não traz números, medidas ou valores específicos nesta página; é uma página inteiramente de princípios e diretrizes qualitativas.

**Diferenças por plataforma:** o texto afirma explicitamente que não há considerações adicionais para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

**Ligações com outros artigos:** Writing inclusively, Accessibility, Localization, Right to left.

<!-- visual:inclusion -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (hig-img_inclusion), aberta e com códigos conferidos; a página não tem vídeo.
- A ilustração de abertura esboça duas figuras humanas genéricas lado a lado, cada uma com cabeça circular e corpo em meia elipse, dentro de um retângulo de cantos arredondados tingido de amarelo. Por cima há uma grade pontilhada de linhas horizontais e verticais e um círculo grande que emoldura as duas cabeças, marcando o alinhamento geométrico das figuras no quadro (img 0667).
- O símbolo de pessoa em círculo é uma silhueta preta sólida de cabeça e ombros dentro de um círculo só contornado, sem nenhum traço que indique gênero (img 0668).
- O símbolo de grupo mostra três silhuetas idênticas e preenchidas, de cabeça e ombros, lado a lado com leve sobreposição lateral, todas do mesmo tamanho aparente e no mesmo plano (img 0669).
- O símbolo de figura acenando é uma silhueta preta de corpo inteiro, em pé, com um braço erguido bem acima da cabeça, sem contorno nem detalhe de gênero (img 0670).
- Nos três símbolos da seção sobre identidade de gênero, a neutralidade vem da ausência de rosto, cabelo e roupa numa silhueta sólida preta, e não de um símbolo abstrato diferente (img 0668, 0669, 0670).

Divergências registradas: a legenda oficial da img 0669 descreve profundidade, com a figura da esquerda em primeiro plano e as outras duas ao fundo, mas a imagem mostra as três com o mesmo tamanho aparente e sem diferença visível de plano ou opacidade, apenas com leve sobreposição horizontal.
<!-- /visual:inclusion -->

## Layout (slug: layout)

**O que governa:** os princípios de hierarquia visual, adaptabilidade a diferentes tamanhos de tela e configurações de multitarefa, size classes, guias de layout e áreas seguras, e especificações de grade e margem por plataforma.

**Por que:** o layout fornece a estrutura para que as pessoas entendam o conteúdo desde o momento em que abrem o app. Relações familiares entre controles e conteúdo permitem uso e descoberta imediatos, e fazem o design parecer "em casa" em cada plataforma. As pessoas esperam que a experiência permaneça familiar quando giram o dispositivo, redimensionam uma janela, adicionam outro display ou trocam de dispositivo.

**Faça e evite:**
- Ordene o conteúdo por importância relativa; como as pessoas costumam ler de cima para baixo e da borda inicial (leading) para a final (trailing), coloque os itens mais importantes perto do topo e da borda inicial da janela ou display. Para idiomas da direita para a esquerda, prefira componentes padrão do sistema que se adaptam automaticamente.
- Alinhe elementos para facilitar a leitura em varredura, e use indentação para transmitir hierarquia; itens alinhados são percebidos como relacionados, e itens com indentação são percebidos como subordinados.
- Agrupe itens relacionados usando espaço negativo, formas de contêiner ou linhas separadoras.
- Use divulgação progressiva (progressive disclosure) para tornar layouts mais limpos e fáceis de interagir: triângulos de divulgação, menus, views aninhadas, ou seções roláveis.
- Diferencie controles do conteúdo: aproveite o material Liquid Glass nas plataformas que o suportam para dar aparência distinta aos controles; use um efeito de borda de rolagem (scroll edge effect) para elevar visualmente os controles acima do conteúdo, em vez de aplicar cor de fundo sólida ou semi-opaca sob eles. Para conteúdo de fundo em tela cheia, estenda-o sob sidebars, toolbars e tab bars.
- Se escalar uma imagem de fundo até a borda da janela cobrir componentes como sidebars ou inspetores, use um efeito de extensão de fundo (background extension effect) para espelhar e desfocar a imagem sob os componentes adjacentes.
- Projete um layout que se adapte com elegância e consistência; respeite áreas seguras, margens e guias definidas pelo sistema, e especifique modificadores de layout para ajustar o posicionamento das views.
- Mesmo que o app fique travado em uma orientação (ex.: um jogo só paisagem), garanta que a interface redimensione bem em diferentes dispositivos e tamanhos de janela.
- Prepare-se para mudanças de tamanho de texto (Dynamic Type), ajustando o layout para acomodar texto em tamanhos maiores (ex.: views adjacentes horizontalmente podem precisar empilhar verticalmente; linhas de tabela podem precisar crescer em altura).
- Pré-visualize o app em múltiplos dispositivos, size classes, localizações e tamanhos de texto; teste primeiro os layouts maiores e menores.
- Quando necessário, escale a arte de fundo em resposta a mudanças de display, sem alterar a proporção da arte (evitando cortes, letterbox ou pillarbox).
- Determine o layout com base em size classes, não em tipo de dispositivo ou orientação, já que size classes descrevem o espaço real disponível.
- Considere todas as combinações possíveis de size classes.
- Mantenha a funcionalidade igual conforme as size classes mudam (pode-se mudar a quantidade de funcionalidade visível na tela, mas não a funcionalidade em si); considere aproveitar espaços maiores para trocar de Tab bars para Sidebars ou expor funcionalidade que ficaria em um menu de overflow.
- Mantenha o layout reconhecível e familiar à plataforma mesmo ao redimensionar, já que o idioma do dispositivo (idiom) permanece o mesmo mesmo quando as size classes mudam.

**Especificações exatas:**

tvOS, área segura: recuar o conteúdo principal 60 pontos do topo e da base da tela, e 80 pontos das laterais.

tvOS, grades de foco (unfocused content width, espaçamento horizontal, espaçamento vertical mínimo):
| Grade | Largura de conteúdo não focado | Espaçamento horizontal | Espaçamento vertical mínimo |
|---|---|---|---|
| Duas colunas | 860 pt | 40 pt | 100 pt |
| Três colunas | 560 pt | 40 pt | 100 pt |
| Quatro colunas | 410 pt | 40 pt | 100 pt |
| Cinco colunas | 320 pt | 40 pt | 100 pt |
| Seis colunas | 260 pt | 40 pt | 100 pt |
| Sete colunas | 217 pt | 40 pt | 100 pt |
| Oito colunas | 184 pt | 40 pt | 100 pt |
| Nove colunas | 160 pt | 40 pt | 100 pt |

visionOS: espaço mínimo ao redor de controles de forma que seus centros fiquem a pelo menos 60 pontos de distância um do outro.

watchOS: no máximo três botões com glifos, ou dois botões com texto, lado a lado em uma linha.

**Diferenças por plataforma:** o texto afirma que não há considerações adicionais para iOS ou iPadOS além do já coberto.
- macOS: evite colocar controles ou informação crítica na parte inferior da janela (as pessoas costumam mover janelas de forma que a borda inferior fique abaixo da tela); evite exibir conteúdo atrás do alojamento da câmera (camera housing) na borda superior da janela.
- tvOS: exigências de área segura e de grade detalhadas acima; inclua padding adequado entre elementos focáveis, já que um elemento aumenta de tamanho ao entrar em foco; mantenha espaçamento consistente para que o conteúdo pareça uma grade; torne o conteúdo parcialmente oculto simétrico (mesma largura em cada lado da tela).
- visionOS: layout dentro de janela, volume 3D delimitado ou espaço imersivo; suporte redimensionamento por padrão, mantendo o conteúdo centralizado horizontalmente em tamanhos muito grandes; é possível definir tamanho mínimo e máximo para janelas, volumes e ornamentos, mas não como forma de impedir redimensionamento; use conteúdo 3D com moderação dentro de janelas, reservando-o para momentos significativos; exiba conteúdo suplementar em uma janela adjacente, não em um ornamento.
- watchOS: no máximo dois ou três controles lado a lado; suporte autorrotação em views que as pessoas podem querer mostrar a outros (ex.: um QR code).

**Ligações com outros artigos:** Right to left, Spatial layout, Layout and organization.

<!-- visual:layout -->
### O que as ilustrações mostram
Base: 5 de 5 folhas de ilustrações vistas (img 0680 a 0696, todas em versão clara), códigos conferidos; a página não tem vídeo.
- A abertura da seção desenha a posição de um elemento dentro da janela como um retângulo sólido menor encaixado no quadrante superior esquerdo de um retângulo maior, com grade de guias retangulares e círculo de alinhamento central sobrepostos, o mesmo esquema de construção das outras aberturas do HIG (img 0680).
- A hierarquia visual aparece numa composição real de app de iPad: barra lateral à esquerda com itens e ícones, foto do Monte Fuji ocupando a metade superior da área de conteúdo e três parágrafos de texto abaixo dela; é o único exemplo de app completo na página, o resto são diagramas abstratos (img 0681).
- O efeito de extensão de fundo fica visível na mesma captura: onde a foto encontra a barra lateral, a imagem continua por baixo dela espelhada e borrada, e perto do topo a foto ganha leve desfoque sob os itens de barra de ferramentas agrupados à direita (img 0681).
- As size classes são desenhadas como uma janela azul clara vazia sobre o mesmo fundo abstrato bege e dourado, variando só a proporção: estreita e curta em compact width e compact height (img 0682), mais alta em compact width e regular height (img 0683), larga e baixa em regular width e compact height (img 0684) e grande nas duas dimensões em regular width e regular height (img 0685). Largura e altura crescem de forma independente.
- A área segura do tvOS é anotada como faixa rosa entre a moldura da TV e a área de conteúdo, com as medidas em vermelho: 60 no topo e na base, 80 nas laterais (img 0686).
- O espaçamento entre itens focáveis do tvOS mostra três cartões lado a lado em que o central aparece maior e com sombra, indicando foco, e faixas verticais rosa preenchem o padding entre ele e os vizinhos (img 0687).
- As grades do tvOS são uma sequência de telas com a mesma moldura: de duas a oito colunas cheias, cada linha termina com uma coluna extra cortada na borda direita, e a primeira grade também corta uma linha na base, sugerindo conteúdo além da área visível (img 0688 a 0694).
- Em cada grade um único item aparece em destaque, branco e com "Title" abaixo; na grade de duas colunas ele fica na primeira linha, ao lado de um item cinza claro, e nas seguintes fica na segunda linha, na coluna do meio da grade de três, na segunda da de quatro, na terceira da de cinco, na quarta das de seis e sete e na quinta das de oito e nove, que na grade de nove colunas é a posição central (img 0688 a 0695).
- A grade de nove colunas é a única sem coluna cortada: as nove colunas cabem inteiras dentro da moldura, em três linhas completas (img 0695).
- Nos diagramas do tvOS o vermelho funciona como cor de anotação das medidas e o rosa marca as zonas de margem e de padding (img 0686, img 0687).
- No watchOS a ilustração mostra um único botão de texto em pílula na base da tela, com fundo semitransparente e texto branco, sobre degradê de azul marinho para magenta, com a hora no canto superior direito (img 0696).
Divergências registradas: as quatro imagens de size classes não desenham moldura de iPad, embora a descrição oficial fale em iPad em paisagem (img 0682 a 0685); a partir da seção "Two-column grid", cada imagem mostra a contagem de colunas seguinte à do cabeçalho sob o qual aparece, batendo com a legenda da própria imagem e não com o título da seção (img 0689 a 0695); a imagem do watchOS mostra um só botão e nenhuma linha de texto, enquanto a descrição oficial fala em dois botões lado a lado sob três linhas de texto (img 0696).
<!-- /visual:layout -->

## O que este grupo revela sobre o jeito Apple

1. O sistema, não o desenvolvedor, é o dono dos efeitos visuais finais. Em app-icons, icons e color, a orientação recorrente é "deixe o sistema aplicar" (mascaramento, destaques especulares, sombras, efeitos de Liquid Glass) em vez de embutir esses efeitos manualmente; isso aparece de forma quase idêntica em app-icons (seção Visual effects) e icons (SF Symbols, ícones sem máscara pré-aplicada).

2. Simplicidade não é estética, é função. accessibility, app-icons, icons e branding convergem no mesmo argumento: menos detalhe é mais reconhecível e mais robusto em contextos variados (tamanhos pequenos, diferentes aparências, tradução cultural), não apenas "mais bonito".

3. Cor tem função semântica antes de decorativa. color, dark-mode, accessibility e branding compartilham a regra de não usar cor sozinha para comunicar informação, e de reservar cor de destaque para poucos elementos de alta importância (ações primárias, status), nunca aplicada de forma ampla.

4. Toda escolha visual precisa sobreviver a estados alternativos do sistema, não apenas ao estado padrão. accessibility, color e dark-mode exigem testar contraste sob Increase Contrast, Reduce Transparency, Reduce Motion e Dark Mode simultaneamente, tratando essas configurações como parte do design, não como exceção.

5. A marca deve ceder à plataforma e ao conteúdo, nunca competir com eles. branding é explícito ("ensure branding always defers to content"), e o mesmo princípio reaparece em layout (diferenciar controles de conteúdo, não decorar) e em color (aplicar accent color com moderação).

6. Consistência entre variantes é tratada como requisito de reconhecimento, não de gosto. app-icons exige que as características centrais do ícone permaneçam as mesmas entre as aparências (padrão, escura, tintada); icons exige consistência de peso, tamanho e perspectiva entre todos os ícones de interface de um app.

7. Existe uma hierarquia declarada de fontes de verdade sobre "quanto espaço eu tenho": layout instrui explicitamente a usar size classes, não o tipo de dispositivo ou a orientação, como base para decisões de layout, porque size classes descrevem o espaço real disponível.

8. Texto embutido em elementos gráficos é tratado como problema, não recurso, de forma consistente entre app-icons, icons e inclusion: texto não localiza bem, não dá acessibilidade e costuma ficar ilegível em tamanhos pequenos.

9. O padrão de segurança em ambientes imersivos ou multitela sempre favorece dar controle explícito à pessoa sobre transições, em vez de decisões automáticas ou abruptas: immersive-experiences (entrar/sair de imersão por ação explícita) e layout (redimensionamento livre, sem impedir via min/max size) repetem esse padrão.

10. Localização e inclusão são tratadas como parte do design central, não como camada adicionada depois: inclusion, color (conotações culturais de cor), icons (localização de caracteres e direção de texto) e layout (idiomas da direita para a esquerda) mostram a mesma preocupação aplicada em diferentes artigos.

11. A Apple distingue explicitamente dois tipos de ícone com regras diferentes: app icons (ícone de app, rico em camadas e efeitos, representando personalidade) versus interface icons (glifos, simples e funcionais); tratar um pelas regras do outro é apontado como erro (por exemplo, não replicar o app icon como ícone de interface).

12. Conforto físico e psicológico da pessoa é elevado a critério de design formal, não apenas de usabilidade: immersive-experiences dedica uma seção inteira a "Promoting comfort" com limites de distância mensuráveis (1,5 metro), e accessibility trata Reduce Motion com uma lista concreta de técnicas de animação a evitar.

## Evidência de leitura

| Arquivo | Linhas lidas | Lido até o fim |
|---|---|---|
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/accessibility.md | 147 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/app-icons.md | 107 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/branding.md | 39 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/color.md | 184 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/dark-mode.md | 68 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/icons.md | 170 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/images.md | 103 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/immersive-experiences.md | 89 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/inclusion.md | 99 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/layout.md | 170 | sim |

Todos os 10 arquivos do grupo foram lidos integralmente em uma única chamada de Read cada, sem necessidade de offset/limit (nenhum arquivo excedeu o limite padrão de leitura), e cada leitura terminou na linha final visível (seção "Change log" ou "Resources", conforme o artigo).
