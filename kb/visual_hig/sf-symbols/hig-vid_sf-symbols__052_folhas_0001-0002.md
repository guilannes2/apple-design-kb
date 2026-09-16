### hig-vid_sf-symbols__052 · folha 0001 · código F5D19

Quadros: q001 a q009, t=0.0s a t=4.5s. Três símbolos sobre fundo branco: uma engrenagem, um ventilador de mesa e um ícone de órbita (dois pontos girando em anéis concêntricos ao redor de um ponto central).
- De q001 para q002: o desenho interno da engrenagem (o padrão de raios que liga o centro à borda) muda de ângulo; o contorno externo dentado da engrenagem mantém o mesmo formato geral. As pás do ventilador giram de posição, alternando entre um desenho em "X" (pás na diagonal) e um desenho mais alinhado aos eixos vertical/horizontal. No ícone de órbita, os dois pontos que giram ao redor do centro mudam de posição ao longo de seus respectivos anéis.
- De q002 para q003: os raios internos da engrenagem voltam a um ângulo parecido com o de q001; as pás do ventilador voltam à configuração diagonal; os pontos do ícone de órbita avançam mais um pouco em suas trajetórias circulares.
- De q003 para q004: o mesmo padrão de alternância se repete nos três símbolos, cada um avançando na sua rotação.
- De q004 para q005: pás do ventilador alternam de novo entre as duas configurações observadas; raios da engrenagem mudam de ângulo; pontos da órbita continuam avançando.
- De q005 para q006: mesma alternância nos três ícones.
- De q006 para q007, de q007 para q008 e de q008 para q009: o padrão se mantém, com a engrenagem alternando o ângulo dos raios internos, o ventilador alternando a orientação das pás, e os dois pontos do ícone de órbita mudando de posição ao longo dos anéis concêntricos a cada quadro, sem nunca coincidirem na mesma posição relativa observada nos quadros anteriores.

### hig-vid_sf-symbols__052 · folha 0002 · código 66D9D

Quadros: q010 a q015, t=5.0s a t=8.0s (últimos quadros do vídeo, 15 quadros distintos ao todo).
- De q010 para q011: a engrenagem muda o ângulo de seus raios internos; as pás do ventilador alternam entre as duas orientações já vistas; os pontos do ícone de órbita seguem avançando em suas trajetórias, com o ponto do anel mais externo visivelmente deslocado em relação ao quadro anterior.
- De q011 para q012: mesma alternância nos três símbolos.
- De q012 para q013: raios da engrenagem, pás do ventilador e pontos da órbita continuam a progressão de rotação observada.
- De q013 para q014 e de q014 para q015: o padrão de rotação se mantém até o último quadro capturado, sem indicação de desaceleração ou parada.

Construção de interface: a animação "rotate" gira internamente cada símbolo, mas de formas diferentes conforme sua geometria: a engrenagem tem o contorno externo dentado fixo enquanto o padrão de raios internos gira; o ventilador tem sua base e moldura fixas enquanto as pás giram; o ícone de órbita mantém o ponto central e os anéis-guia fixos enquanto os dois pontos orbitais se deslocam ao longo dos anéis, aparentemente em velocidades diferentes um do outro (não estão sempre alinhados). Os três símbolos giram ao mesmo tempo, ao contrário do "breathe" do outro vídeo desta página, em que só um símbolo muda de opacidade por vez.

Com a descrição oficial: a descrição fala em uma engrenagem que gira, um ventilador de mesa com pás giratórias e dois pontos girando em órbitas concêntricas ao redor de um centro, o que bate com o que os quadros mostram. A descrição diz que "alguns símbolos giram inteiramente, enquanto em outros só partes do símbolo giram"; nos quadros vistos, é a engrenagem e o ventilador que parecem ter só uma parte interna girando (raios da engrenagem, pás do ventilador) enquanto a moldura externa permanece fixa, e o ícone de órbita tem apenas os pontos girando ao redor de um centro e anéis-guia estáticos.

## Síntese visual da página sf-symbols

- As animações de símbolo são demonstradas com os mesmos três ícones por vídeo, lado a lado sobre fundo branco em preto sólido, sem cor, texto ou UI de aplicativo ao redor: o foco visual é só a mudança do próprio símbolo (hig-vid_sf-symbols__051 folha 0001 a 0004; hig-vid_sf-symbols__052 folha 0001 e 0002).
- Cada efeito é isolado por vídeo: "breathe" é só variação cíclica de opacidade/tom (preto a cinza claro e de volta), símbolo por símbolo, em rodízio, sem mudança de forma ou de ângulo (hig-vid_sf-symbols__051, todas as folhas). "Rotate" é só variação de ângulo/posição de uma parte interna do símbolo (raios da engrenagem, pás do ventilador, pontos orbitais), com os três símbolos girando ao mesmo tempo e sem variação de opacidade (hig-vid_sf-symbols__052, folhas 0001 e 0002).
- Em "rotate", cada símbolo tem uma parte fixa (contorno dentado da engrenagem, moldura e base do ventilador, anéis-guia e ponto central da órbita) e uma parte móvel (raios internos, pás, pontos orbitais), mostrando que a animação se aplica a um subconjunto de camadas do símbolo, não ao ícone inteiro como bloco único.
- Em "breathe", a variação de opacidade passa de um símbolo para o próximo em blocos de tempo (onda sonora, depois balão de tradução, depois anéis concêntricos), nunca nos três ao mesmo tempo dentro da janela observada, sugerindo que a intenção didática da página é mostrar o efeito em cada símbolo isoladamente dentro do mesmo clipe, não uma sincronia entre eles.
- Cada quadro traz o número (qNNN) e o tempo em segundos no canto superior esquerdo, sobre fundo preto, como identificação de amostragem de vídeo, não parte da interface real da Apple.
