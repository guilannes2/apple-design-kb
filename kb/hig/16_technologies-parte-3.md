# Technologies (parte 3)

## SharePlay (slug: shareplay)

### O que governa
Rege como um app oferece experiências compartilhadas em tempo real entre pessoas em dispositivos diferentes, sincronizadas pelo sistema e coordenadas com FaceTime ou Messages, incluindo o comportamento espacial dessas experiências em visionOS.

### Por que
A intenção central é presença: fazer com que pessoas em locais diferentes sintam que estão fazendo algo juntas, no mesmo momento. Por isso o sistema sincroniza a atividade entre dispositivos e mantém a comunicação (voz, vídeo) rodando em paralelo. Em visionOS, a Apple leva esse princípio adiante criando um "contexto espacial compartilhado": todos veem o conteúdo na mesma posição relativa, o que permite apontar, discutir e interagir como se o objeto estivesse fisicamente ali, reforçando interação autêntica e intuitiva. As decisões de template espacial (lado a lado, ao redor, conversacional) derivam de uma pergunta de design mais ampla: a atividade pede foco no conteúdo (lado a lado), interação social ao redor de um objeto (surround) ou companhia enquanto o app faz algo em segundo plano (conversacional)?

### Faça e evite
- Use SharePlay para experiências em tempo real; para colaboração assíncrona, ofereça uma forma de compartilhar ou salvar depois que a sessão termina.
- Desenhe a experiência de acordo com a natureza da atividade: visão compartilhada única para assistir/navegar, ou visão adaptada ao papel de cada pessoa para jogos.
- Construa experiências que funcionem entre plataformas Apple diferentes.
- Dê um caminho claro e reconhecível para iniciar uma atividade, como um botão com o símbolo do SharePlay; use também o share sheet do sistema.
- Deixe as pessoas entrarem na atividade sem atrito: leve-as rapidamente ao conteúdo compartilhado, evite telas irrelevantes, e adie etapas não essenciais (sign-in, download, assinatura) para o momento certo.
- Ofereça acesso provisório a quem não é assinante, ou suporte Family Sharing, para reduzir a barreira de entrada.
- Descreva atividades de forma clara e concisa em convites, sem truncamento.
- Ajude as pessoas a entenderem por que a atividade mudou quando a ação de uma pessoa afeta todos (ex.: pausar um filme pausa para todos).
- Use o termo "SharePlay" corretamente: como substantivo ou verbo, nunca com adjetivo (evite "virtual SharePlay" ou "spatial SharePlay") e nunca flexionado (SharePlayed, SharePlays, SharePlaying).
- Em iOS, iPadOS e macOS, suporte Picture in Picture para vídeo compartilhado.
- Em visionOS, prefira iniciar a experiência a partir de uma janela (compartilhável pelo botão Share ao lado da window bar); para espaço imersivo, é preciso UI customizada.
- Resolva conflitos de forma natural: se só uma pessoa pode usar um objeto por vez, não mostre UI que deixe outra pessoa assumir o controle; deixe as pessoas negociarem por voz ou gesto, com uma regra simples como "a última mudança vence".
- Reserve visões únicas/personalizadas só para momentos que realmente pedem isso; em geral, mantenha visões e níveis de imersão sincronizados.
- Ao mudar o nível de imersão, verifique se isso interromperia a tarefa de alguém; se sim, deixe a pessoa escolher quando entrar, em vez de puxá-la automaticamente.
- Deixe cada participante customizar ajustes pessoais (volume, legendas) sem afetar os demais.
- Facilite sair e voltar à atividade, com um controle claro para reentrar.
- Suporte pessoas que não aparecem como spatial Persona (quem entra de outro dispositivo, ou desligou a Persona), oferecendo alternativas na UI quando a experiência depende de expressões faciais ou gestos.
- Adote o spatial template que melhor se encaixa na atividade, ou crie um template customizado se nenhum servir.
- Divida uma atividade complexa em estágios, cada um com seu próprio template; prefira misturar templates do sistema e customizados a desenhar um único template complexo.
- Vincule transições de template a uma ação explícita da pessoa (evite trocas inesperadas de papel ou assento).
- Mantenha transições suaves: evite trocas frequentes ou que exijam muito movimento; use fade ao mover alguém de assento e dê pistas visuais de reorientação.
- Para templates customizados: contabilize pessoas fisicamente presentes (vistas por passthrough, não como Persona); ofereça a orientação de assento ideal para o conteúdo; suporte o número máximo de assentos (definindo todos antecipadamente); posicione assentos a pelo menos um metro de distância; defina a ordem de preenchimento dos assentos de forma balanceada; mantenha papéis (player, spectator, team member) independentes dos assentos, exceto quando um papel realmente exige um lugar específico (ex.: anfitrião à cabeceira).

### Especificações exatas
- Apple Vision Pro suporta até 5 spatial Personas em uma atividade.
- Assentos devem ficar posicionados a pelo menos 1 metro de distância entre si.
- Se uma spatial Persona chega perto demais de outra, ela é substituída por uma foto de contato.

### Diferenças por plataforma
- tvOS: sem considerações adicionais. watchOS: não suportado.
- iOS, iPadOS, macOS: suporte a Picture in Picture para vídeo compartilhado (janela PiP em iPhone/iPad; janela que pode ser trazida à frente no Mac).
- visionOS: seção extensa e própria, cobrindo design de atividades compartilhadas, Personas, spatial templates (side-by-side, surround, conversational) e templates customizados, como detalhado acima.

### Ligações com outros artigos
Cita: Immersive experiences (para orientação sobre transições de imersão); Writing and Inclusion não é citado aqui, mas o artigo remete a documentação de desenvolvedor (Group Activities, Synchronizing data during a SharePlay activity, Adding spatial Persona support, Configure your visionOS app for sharing with people nearby, Building a guessing game for visionOS, SpatialTemplateSeatElement, isSpatial e isNearbyWithLocalParticipant).

---

<!-- visual:shareplay -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- O ícone de abertura (contorno de pessoa dentro de dois arcos concêntricos, em azul escuro sobre degradê azul) é mostrado como desenho de construção com grade retangular tracejada e circunferências concêntricas que partem exatamente do centro do símbolo e passam além dos arcos, sugerindo que o raio dos arcos deriva dessas guias (img 1020).
- A tela de vídeo compartilhado no iPhone sobrepõe ao vídeo pausado os controles de voltar, pausar e avançar 10 segundos, traz no topo uma faixa com avatar pequeno e a indicação de quem começou a atividade, botão X no canto superior esquerdo, barra de progresso com tempo decorrido e restante, e a miniatura da outra pessoa no canto inferior direito (img 1021).
- A tela de quem iniciou é idêntica à do participante, mesmo vídeo, mesma faixa e mesmo tempo, e só a pessoa na miniatura muda, o que mostra que os dois lados da sessão usam a mesma interface (img 1021, 1022).
- O botão recomendado é um retângulo azul de cantos arredondados com o símbolo do SharePlay à esquerda e o rótulo "Start Activity" em branco à direita, apresentado pronto, sem grade nem cota (img 1023).
- No template lado a lado, seis silhuetas enfileiradas numa curva olham todas para um painel retangular verde, e não umas para as outras; uma silhueta branca entre as cinza marca a posição de quem vê (img 1024).
- No template surround, cinco silhuetas formam um círculo voltado para dentro, em torno de uma esfera verde no centro da plataforma (img 1025).
- No template conversacional, cinco silhuetas ficam mais próximas, num meio círculo fechado, e o painel verde vai para a borda do grupo, deixando as pessoas mais voltadas entre si do que para o conteúdo (img 1026).
- Os três templates compartilham a mesma linguagem: fundo quase preto, plataforma circular escura com leve brilho em perspectiva, silhuetas cinza sem rosto nem roupa detalhada e a cor reservada ao conteúdo, sempre verde saturado; não há texto, régua ou anotação, e a diferença entre eles é comunicada só pela posição relativa entre pessoas e objeto (img 1024, 1025, 1026).
<!-- /visual:shareplay -->

## ShazamKit (slug: shazamkit)

### O que governa
Rege o uso de reconhecimento de áudio (correspondência de amostra sonora contra o catálogo ShazamKit ou um catálogo customizado) dentro de apps, com foco em privacidade no uso do microfone e no armazenamento de músicas reconhecidas.

### Por que
A lógica de privacidade domina: como o recurso depende do microfone do dispositivo, a Apple exige pedido de permissão explicado e limita a gravação ao tempo mínimo necessário, para que as pessoas não sintam que o microfone "fica ligado" sem necessidade. Da mesma forma, mesmo quando tanto o controle de Music Recognition quanto o app Shazam mostram o app como fonte da música reconhecida, a Apple valoriza dar às pessoas controle explícito sobre quais apps podem gravar conteúdo na biblioteca do iCloud, reconhecendo que a atribuição visível não substitui o consentimento.

### Faça e evite
- Solicite acesso ao microfone somente quando necessário e explique por que está pedindo (ver Privacy).
- Pare de gravar o quanto antes: grave apenas o tempo necessário para obter a amostra.
- Deixe as pessoas optarem (opt-in) por armazenar as músicas reconhecidas pelo app na biblioteca do iCloud, mesmo que a atribuição do app já apareça no Music Recognition e no Shazam.

### Especificações exatas
Nenhum número, medida ou valor numérico consta no texto.

### Diferenças por plataforma
Nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Cita Privacy para orientação sobre pedidos de permissão.

---

<!-- visual:shazamkit -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página não tem vídeo.
- O ícone da tecnologia (losango arredondado azul escuro com camadas curvas onduladas empilhadas, como ondas sonoras, e uma forma central que lembra um S) é apresentado como desenho de construção sobre degradê azul, com grade retangular tracejada e circunferências concêntricas centradas no símbolo, no mesmo tratamento do ícone do SharePlay; confere com a descrição oficial (img 1027).
- A única tela de interface da página não mostra o reconhecimento de áudio em si, e sim o pedido de acesso ao microfone: um alerta modal do sistema centralizado, com título que nomeia o app e o microfone e um corpo curto explicando o motivo (img 1028).
- No alerta, os dois botões ficam lado a lado com hierarquia de cor: recusar ("Not Now") à esquerda em cinza claro e permitir ("Allow") à direita em azul de destaque (img 1028).
- O alerta cobre o meio da tela de boas-vindas do app fictício (degradê azul esverdeado com símbolos matemáticos e o nome do app ao fundo), e o botão "Get Started" do app continua visível atrás dele, na parte de baixo (img 1028).
<!-- /visual:shazamkit -->

## Sign in with Apple (slug: sign-in-with-apple)

### O que governa
Rege como e quando oferecer o login com Apple ID, quais dados coletar, e a aparência exata (botões padrão do sistema e customizados) do controle de Sign in with Apple.

### Por que
O princípio central é confiança combinada com conveniência: dar às pessoas uma forma rápida e privada de entrar sem lembrar múltiplas senhas, e usar isso para reduzir atrito de cadastro. A Apple reforça repetidamente o princípio de minimizar coleta de dados e respeitar escolhas de privacidade (como o endereço de e-mail de retransmissão privado), porque isso é a base da confiança que sustenta o recurso. Do lado visual, a padronização estrita do botão (cores, proporções, textos permitidos) existe para que Sign in with Apple seja instantaneamente reconhecível e não seja confundido ou diluído por variações de marca, e por isso passa por App Review.

### Faça e evite
- Ofereça Sign in with Apple em todas as versões do app ou site, em todas as plataformas, inclusive não Apple.
- Peça login apenas em troca de valor claro; explique brevemente os benefícios de entrar.
- Adie o login o máximo possível; deixe a pessoa explorar o app antes de exigir compromisso.
- Se uma conta é obrigatória, explique por que antes de pedir a criação, e só depois ofereça as opções de login.
- Considere permitir vincular uma conta existente ao Sign in with Apple, antes ou depois do login na conta existente.
- Em apps de comércio, espere até depois da compra para pedir criação de conta; se suportar checkout como convidado, ofereça criação de conta rápida após a transação (e não peça de novo nome/e-mail já fornecidos via Apple Pay).
- Assim que o Sign in with Apple for concluído, dê boas-vindas imediatamente; não atrase a experiência pedindo informação não obrigatória.
- Indique quando a pessoa está conectada via Sign in with Apple (ex.: "Using Sign in with Apple" nas configurações).
- Minimize pedidos de dados adicionais; explique por que precisa deles e mostre claramente os dados recebidos.
- Deixe claro se um dado adicional é obrigatório (legal/contratual) ou apenas recomendado.
- Nunca peça senha às pessoas que usam Sign in with Apple.
- Evite pedir e-mail pessoal quando a pessoa já forneceu um endereço de retransmissão privado; em vez disso, permita ver o endereço de retransmissão no app, direcione para Settings > Apple Account > Password & Security > Apps using Apple Account, ou use outros identificadores (número de pedido, telefone).
- Dê à pessoa a chance de usar o app antes de pedir dados opcionais, e nunca bloqueie acesso a recursos por recusa de dado opcional.
- Seja transparente sobre os dados coletados, por exemplo, saudando a pessoa pelo nome ou e-mail compartilhado.
- Exiba o botão de Sign in with Apple com destaque, não menor que outros botões de login, e sem exigir rolagem para vê-lo.
- Prefira os botões fornecidos pelo sistema (ASAuthorizationAppleIDButton, WKInterfaceAuthorizationAppleIDButton, ou a versão web), que garantem aparência aprovada, proporções corretas, tradução automática do título e rótulo de VoiceOver.
- Use apenas os títulos aprovados: "Sign in with Apple", "Sign up with Apple", "Continue with Apple" (iOS, macOS, tvOS, web); watchOS usa apenas "Sign in".
- Escolha o estilo (branco, branco com contorno, ou preto) de acordo com o contraste do fundo; nunca use branco sem contorno sobre fundo claro, nem preto sobre fundo escuro.
- No watchOS, o botão preto na verdade usa um cinza-escuro definido pelo sistema (não é preto puro), para contrastar com o fundo preto puro do Apple Watch.
- Ao criar um botão customizado, use apenas a arte do logo baixada em Apple Design Resources; nunca crie um logo Apple customizado; não use o logo isolado como botão; combine a altura do arquivo de logo com a altura do botão; não recorte o arquivo de logo nem adicione padding vertical.
- Não altere: os títulos permitidos, a forma geral (retangular para logo+texto; circular ou retangular para logo apenas), e as cores do logo e do título (sempre preto ou branco, nunca cores customizadas).
- Pode-se ajustar: fonte do título (peso e tamanho), caixa do título (tudo maiúsculo é permitido), aparência de fundo (textura ou gradiente sutil mantendo preto/branco), raio dos cantos, bezel e sombra do botão.
- Use arquivo PNG apenas em botões de 44 pt de altura (padrão em iOS); use SVG/PDF para qualquer altura.
- Prefira a fonte do sistema para o título; mantenha a mesma proporção entre altura do botão e tamanho da fonte do sistema.
- Preserve o estilo de capitalização padrão (primeira letra maiúscula em "Sign"/"Continue" e em "Apple"; demais letras minúsculas) a menos que a interface use apenas maiúsculas.
- Alinhe verticalmente o título ao centro do botão, depois adicione o logo com altura igual à do botão.
- Para botão apenas com logo: não adicione padding horizontal (a arte já inclui); use máscara para mudar o formato quadrado padrão (círculo, retângulo arredondado); nunca recorte a arte da Apple para reduzir o padding embutido.

### Especificações exatas
- Botão logo+texto (iOS, macOS, web): largura mínima 140 pt (140 px @1x, 280 px @2x); altura mínima 30 pt (30 px @1x, 60 px @2x); margem mínima 1/10 da altura do botão.
- Fonte do sistema: tamanho da fonte do título é 43% da altura do botão; equivalentemente, a altura do botão é 233% do tamanho da fonte do título (arredondado ao inteiro mais próximo). Exemplos citados: botão de 44 pt de altura com fonte de 19 pt; botão de 56 pt de altura com fonte de 24 pt.
- Margem mínima entre o título e a borda direita do botão: pelo menos 8% da largura do botão.
- Botão apenas com logo: usar PNG apenas em botões de 44x44 pt; proporção sempre 1:1.
- Margem mínima ao redor do botão apenas com logo: pelo menos 1/10 da altura do botão.

### Diferenças por plataforma
Nenhuma consideração adicional específica para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS além das já descritas (watchOS tem título único "Sign in" e cor de fundo dark gray em vez de preto puro).

### Ligações com outros artigos
Cita Creating a custom Sign in with Apple button (guia relacionado), Authentication Services, e o botão "Sign in with Apple button" como recurso relacionado.

---

<!-- visual:sign-in-with-apple -->
### O que as ilustrações mostram
Base: 7 de 7 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura é o desenho de construção do logo da Apple em azul escuro sobre degradê azul, com grade retangular tracejada e circunferência guia centralizada no logo, o mesmo tratamento dos ícones de SharePlay e ShazamKit (img 1053).
- A oferta depois da compra aparece numa tela de pedido concluído com X de fechar no topo, círculo verde com check, título de compra completa e uma linha secundária sobre a confirmação por e-mail; embaixo, dois botões empilhados: "Create Account" em cinza claro, neutro, e, abaixo dele, "Sign up with Apple" em preto com o logo (img 1054).
- Os três títulos do botão do sistema aparecem no mesmo estilo de botão preto com logo e texto em branco, trocando só o texto: entrar, cadastrar e continuar (img 1055, 1056, 1057).
- O watchOS tem botão próprio, ao lado dos equivalentes das outras plataformas: só "Sign in", mais estreito e num preto levemente acinzentado (img 1058); sobre fundo preto puro, esse cinza escuro é justamente o que separa o botão do fundo (img 1067).
- O estilo branco é ensinado por par certo e errado com o botão idêntico e só o fundo variando: sobre cinza escuro sólido o contraste é alto e leva check verde (img 1059, 1060); sobre cinza claro o botão quase se confunde com o fundo e leva X cinza em círculo (img 1061, 1062); os marcadores ficam isolados, sem texto dentro da imagem.
- O branco com contorno ganha um traço fino escuro que o separa do fundo cinza claro, mantendo a legibilidade (img 1063); sobre fundo cinza bem escuro, o mesmo contorno quase desaparece e a moldura parece contínua com o fundo (img 1064).
- O estilo preto contrasta bem sobre cinza bem claro (img 1065) e, sobre cinza escuro, quase se funde com o fundo e perde a definição das bordas (img 1066).
- O raio de canto é uma progressão no mesmo botão preto: cantos retos de 90 graus na legenda de raio mínimo (img 1068), arredondamento moderado no padrão do sistema (img 1069) e raio máximo, com os lados curtos totalmente arredondados em forma de cápsula (img 1070).
- Ao lado de outros provedores, duas telas de iPhone mostram dois arranjos: quatro botões empilhados de mesma largura e altura, o da Apple preto com o logo real e os fictícios X, Y e Z em cinza claro com círculo, quadrado e triângulo preenchidos no lugar do logo (img 1071, esquerda); ou um campo de texto no topo, o rótulo "Sign in with:" e quatro botões quadrados pequenos lado a lado, o da Apple em preto com o logo e três cinza com as mesmas formas (img 1071, direita).
- A área livre mínima ao redor do logo isolado é desenhada como uma borda grossa sombreada em volta do quadrado do logo, nas duas polaridades: logo preto em quadrado branco com borda cinza escura (img 1072) e logo branco em quadrado preto com borda clara (img 1073).
- As proporções do botão customizado com logo e texto vêm cotadas: chave vertical de 44 pt de altura com chamada de fonte de 19 pt (img 1074) e, no botão maior, 56 pt de altura com fonte de 24 pt, numa razão entre altura e fonte quase igual à anterior, perto de 2,3 nos dois casos (img 1075); são as únicas imagens da página com cotas numéricas explícitas.
- O botão só com logo é o mesmo quadrado preto com logo branco sob três máscaras: retângulo arredondado (img 1076), sem máscara, com cantos retos (img 1077), e círculo completo (img 1078).
<!-- /visual:sign-in-with-apple -->

## Siri (slug: siri)

### O que governa
Rege como um app expõe suas ações (intents) e conteúdo (entities) para Siri e Apple Intelligence, e como escrever as respostas e diálogos que Siri entrega em nome do app.

### Por que
O princípio de fundo é que Siri deve entender o app com o mínimo de trabalho extra: por padrão o sistema não sabe o que um app faz, então o App Intents framework e os App schema domains existem para que apps comuns (e-mail, música, fotos) herdem lógica pronta, com conversação natural e entendimento contextual mais profundo, em vez de cada app reinventar tudo. A Apple também insiste em consistência de voz e comportamento: usar terminologia familiar ao usuário (não ao app), evitar publicidade dentro das respostas de Siri, e manter as respostas curtas e sem humor forçado, porque Siri é ouvida repetidamente e cansaço/irritação surgem rápido com respostas prolixas. Há também um princípio de neutralidade e inclusão nas respostas (evitar pronomes de gênero desnecessários) e de device-independence, já que uma solicitação pode começar em um dispositivo e terminar em outro.

### Faça e evite
- Identifique as ações mais populares do app e os contextos (ex.: mãos livres, dispositivo específico) em que ocorrem, para priorizar quais ações/entidades expor.
- Use termos familiares às pessoas para o conteúdo e ações do app (ex.: "faixa", "música" ou "podcast", conforme o que o público reconhece).
- Ofereça conteúdo relevante ao contexto pessoal (buscas recentes, favoritos, wishlist) em vez do catálogo inteiro, exceto categorias como e-mail/mensagens, onde acesso expandido faz sentido.
- Não inclua propaganda, marketing ou pitch de compra no conteúdo que Siri entrega.
- Só forneça uma resposta customizada se as respostas padrão não atenderem às necessidades do app.
- Escreva diálogo de resposta claro e descritivo; personalize perguntas de follow-up para clareza (ex.: "Which soup?" em vez de "Which one?").
- Mantenha respostas o mais sucintas possível, usando o contexto da conversa para remover detalhes desnecessários; evite palavras supérfluas ou tentativas de humor.
- Forneça respostas que Siri possa entregar tanto audível quanto visualmente, garantindo que a resposta em voz funcione sozinha sem depender de elementos visuais.
- Desenhe interações inclusivas, evitando pronomes específicos quando desnecessários (ex.: "Who should I send it to?" em vez de "What's his or her name?").
- Faça uma pergunta aberta quando a lista completa de opções for longa demais para Siri ler a tempo.
- Mantenha respostas independentes de dispositivo sempre que possível, já que a solicitação pode começar em um dispositivo e valer em outro.
- Omita o nome do app das respostas; o sistema já fornece atribuição verbal e visual.
- Use linguagem apropriada e respeite controles parentais; não inclua linguagem ofensiva.
- Ajude as pessoas a entenderem erros e falhas com descrições específicas à situação (ex.: "Sorry, we're out of chicken noodle soup" em vez de "Sorry, we can't complete your order").
- Refira-se a Siri pelo nome, nunca por pronomes (ela, ele); nunca personifique ou reproduza a funcionalidade de Siri, nem dê resposta que pareça vir da Apple.
- Não use frases reservadas como "Call 911" ou "Hey Siri".
- Em contexto localizado, traduza apenas a palavra "Hey" na frase "Hey Siri"; "Siri" nunca é traduzido (tabela extensa de traduções por locale está no artigo, incluindo pt_BR: "E aí Siri").

### Especificações exatas
Nenhuma medida de pixel, ponto, tempo ou proporção consta no texto; o conteúdo é majoritariamente de comportamento e diálogo. A única "tabela numérica" é de traduções de locale para a frase "Hey Siri", sem valores de medida.

### Diferenças por plataforma
O artigo não tem seção própria de "Platform considerations" separada por sistema além da introdução geral; a Siri AI é descrita como disponível "em dispositivos suportados" via Apple Intelligence, sem detalhamento por SO no texto lido.

### Ligações com outros artigos
Cita App Shortcuts, Snippets, Writing and Inclusion, Guidelines for Using Apple Trademarks, e documentação de desenvolvedor (App Intents, App schema domains, Apple Intelligence and Siri AI).

---

<!-- visual:siri -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página tem uma única ilustração e nenhum vídeo.
- O símbolo é um anel circular em azul mais escuro com uma linha ondulada em forma de S cruzando o interior, sobre fundo em degradê azul; confere com a descrição oficial de desenho tingido de azul com grade retangular e circular (img 1079).
- Além da grade retangular tracejada, há uma circunferência guia menor, concêntrica ao anel, que marca a proporção do traço interno em relação ao contorno externo (img 1079).
- É o único material visual da página e repete a linguagem de construção dos ícones de SharePlay, ShazamKit e Sign in with Apple (grade tracejada, guia circular concêntrica, azul sobre degradê azul); nenhuma tela de interface ou exemplo de resposta é mostrado (img 1079).
<!-- /visual:siri -->

## Tap to Pay on iPhone (slug: tap-to-pay-on-iphone)

### O que governa
Rege como um app de pagamento em iOS integra o Tap to Pay on iPhone (aceitação de pagamento por aproximação sem hardware externo), desde a aceitação de termos pelo comerciante até checkout, exibição de resultado e usos adicionais como cartões de fidelidade.

### Por que
A lógica central é confiabilidade no momento do checkout: como checkout é uma ação sensível ao tempo, a Apple orienta a preparar o recurso com antecedência (configurar o dispositivo assim que o app inicia e a cada retorno ao primeiro plano) para que o comerciante nunca precise esperar. Há também um princípio de clareza de rótulo e prevenção de erro: o texto "Tap to Pay on iPhone"/"Tap to Pay" deve ser reservado exclusivamente para ações de pagamento, para que o comerciante nunca confunda um botão de pagamento com um de outra finalidade (como leitura de cartão de fidelidade), e o logo da Apple nunca pode aparecer no botão, para não sugerir endosso direto da Apple à transação comercial.

### Faça e evite
- Ajude comerciantes a aceitar os termos e condições do Tap to Pay on iPhone antes de começarem a interagir com clientes (ex.: dentro de fluxos de onboarding ou mensagens no app).
- Apresente os termos e condições apenas a um usuário administrador; se um não administrador tentar ativar, explique que acesso de administrador é necessário.
- Garanta que o dispositivo do comerciante esteja atualizado antes de apresentar os termos, se o PSP exigir versão específica do iOS.
- Ofereça um tutorial descrevendo os tipos de pagamento suportados e como usar o recurso (via Learn More, apresentação automática após aceite dos termos, apresentação a novos usuários, ou local consistente como configurações/ajuda).
- No tutorial próprio, mostre como iniciar checkout para cada tipo de pagamento, posicionar cartão/carteira digital, e lidar com entrada de PIN (inclusive modo de acessibilidade).
- Ofereça Tap to Pay on iPhone como opção de checkout esteja o recurso habilitado ou não; ao tocar o botão, apresente os termos se necessário e mostre a tela automaticamente quando a configuração terminar.
- Prepare o recurso assim que o app inicia e imediatamente após cada transição para primeiro plano, para minimizar tempo de espera.
- Mantenha a opção de checkout disponível mesmo durante configuração em segundo plano, exibindo indicador de progresso (indeterminado, ou determinado se a API indicar progresso contínuo).
- Se o app suporta múltiplos métodos de pagamento, torne o botão Tap to Pay fácil de encontrar sem rolagem; se for o único método, abra automaticamente ao iniciar o checkout.
- Facilite a alternância entre Tap to Pay on iPhone e acessórios de hardware suportados, sem exigir ida às configurações do app durante o checkout.
- Use o rótulo "Tap to Pay on iPhone" ou, se o espaço for limitado, "Tap to Pay"; exceção: se for o único método suportado, pode reaproveitar botões existentes como "Charge" ou "Checkout"; se usar ícone, use os SF Symbols `wave.3.right.circle` ou `wave.3.right.circle.fill`; nunca inclua o logo da Apple no botão.
- Use o rótulo "Tap to Pay on iPhone" apenas para ações de pagamento, nunca para ações que não são de pagamento.
- Determine o valor final antes de iniciar a experiência Tap to Pay (ex.: apresente opções de gorjeta antes); exiba o valor final na tela do Tap to Pay.
- Exiba opções de pré-pagamento (como tipo de pagamento) antes da tela do Tap to Pay.
- Comece a processar a transação assim que possível, mesmo antes da animação de checkmark terminar (API returnReadResultImmediately).
- Exiba indicador de progresso de autorização somente após a animação da tela do Tap to Pay terminar, para transição visual suave.
- Exiba claramente o resultado da transação, aprovada ou recusada, e ofereça opções de recibo digital (QR code, mensagem de texto) quando possível.
- Ajude o comerciante a completar o checkout quando o pagamento não puder ser concluído via Tap to Pay (nova tela ou reuso da tela de checkout, checkout por outro método, ou relançar o Tap to Pay).
- Para SCA (Strong Customer Authentication) em algumas regiões, esteja preparado para exibir a tela de entrada de PIN em vez do resultado da transação.
- Se o sistema retornar um erro que o comerciante precisa resolver, exiba descrição clara do problema e recomendação (ex.: alerta para atualizar o iOS).
- Facilite que o comerciante obtenha ajuda para problemas que não consegue resolver (conteúdo de ajuda no app/site, ação de contato com suporte).
- Para leitura de cartão sem valor de transação (consulta, verificação, reembolso), use rótulo genérico como "Look Up", "Store Card", "Verify" ou "Refund", nunca "Tap to Pay on iPhone" ou "Tap to Pay".
- Se o app suporta transação independente de cartão de fidelidade, use um botão separado e claramente rotulado, evitando termos relacionados a pagamento no rótulo (ex.: use "Loyalty Card", não "Tap to Pay on iPhone - Loyalty").

### Especificações exatas
Nenhuma medida numérica (pt, px, ms, proporção) consta no texto; o conteúdo é inteiramente comportamental e de fluxo.

### Diferenças por plataforma
Sem considerações adicionais para iOS. Não suportado em iPadOS, macOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Cita Progress indicators, Alerts, Additional interactions (dentro do próprio artigo), e Tap to Pay on iPhone marketing guidelines, além de documentação de desenvolvedor (ProximityReader, ProximityReaderDiscovery API, PaymentCardReaderSession.ReadError, prepare(using:), PaymentCardReader.Event.updateProgress(_:), PaymentCardReader.Event.readyForTap).

---

<!-- visual:tap-to-pay-on-iphone -->
### O que as ilustrações mostram
Base: 5 de 5 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura é conceitual, sem interface: um círculo escuro central com o símbolo de ondas de pagamento por aproximação, sobre degradê azul com grade pontilhada retangular e circular (img 1121).
- As telas de ativação seguem a mesma hierarquia dentro da moldura de iPhone: título, corpo curto, ação primária num botão azul cheio de bloco e ação secundária num link de texto logo abaixo, com um espaço reservado de imagem cinza no rodapé; na primeira, habilitar e saber mais (img 1122); na segunda, fazer uma transação de teste ou deixar para depois (img 1123).
- O tutorial fica acessível numa célula padrão de lista dos Ajustes, na tela "Tutorials", com título em negrito, subtítulo cinza e seta de disclosure à direita (img 1124).
- O tutorial aparece numa folha modal com X circular cinza no canto superior direito, um rótulo pequeno em maiúsculas acima do título em negrito, uma ilustração escura de iPhone pedindo para aproximar o cartão com um cartão laranja mostrando nome do comerciante e valor, e passos numerados embaixo (img 1125).
- Na preparação do checkout, uma barra de progresso azul fina fica colada logo abaixo da barra de navegação (voltar e título "Checkout"), acima do texto de preparo e do valor centralizado em destaque tipográfico grande (img 1126); a tela seguinte mantém tudo igual com a barra cheia, que a descrição oficial trata como indicador indeterminado (img 1127).
- Na autorização, a barra some e entra um spinner cinza ao lado do rótulo "Authorizing", sobre o mesmo valor grande (img 1132).
- O botão de pagamento é uma forma azul de largura total com o símbolo de ondas à esquerda e o texto centralizado, marcado como certo com selo verde (img 1128, 1129); o mesmo botão com o logo da Apple no lugar das ondas é marcado como errado com selo cinza de X (img 1130, 1131); os selos ficam isolados, fora do botão.
- O resultado usa um selo circular grande centralizado acima do valor, com "Done" no canto direito da barra, o pedido de escolher o recibo e três blocos cinza vazios empilhados como opções (img 1133); na recusa, o layout é idêntico e só o selo muda, de check verde para X vermelho (img 1134).
- Quando o pagamento não se completa, o botão de voltar reaparece na barra, o selo vermelho vem com o texto de pagamento não concluído e uma lista de quatro métodos empilhados em que o de aproximação é o primeiro, em azul sólido, e os demais ficam em cinza (img 1135).
- Os botões de fidelidade mantêm a mesma forma azul, mas só com texto e sem o símbolo de ondas: um rotulado "Loyalty Card" (img 1136) e uma variante cujo rótulo junta o nome do recurso à palavra "Loyalty" (img 1137).
<!-- /visual:tap-to-pay-on-iphone -->

## VoiceOver (slug: voiceover)

### O que governa
Rege como um app fornece descrições, rótulos e ordem de leitura para que o leitor de tela VoiceOver torne a interface e o conteúdo acessíveis a pessoas cegas ou com baixa visão.

### Por que
O princípio orientador é que a informação visual precisa ter um equivalente audível fiel e proporcional: nem tudo precisa ser descrito (imagens puramente decorativas devem ser excluídas, por respeito ao tempo da pessoa e para reduzir carga cognitiva), mas tudo que é funcionalmente relevante (imagens com significado, gráficos, relações espaciais entre elementos, mudanças de layout) precisa ser explicitamente comunicado ao VoiceOver, porque relações que pessoas videntes percebem por proximidade e alinhamento visual são invisíveis para quem não vê a tela. O agrupamento de elementos (como imagem+legenda em um único frame) existe para que a ordem de leitura corresponda ao sentido lógico do conteúdo, não à disposição bruta na tela.

### Faça e evite
- Forneça rótulos alternativos descritivos para todos os elementos-chave da interface, além dos rótulos genéricos padrão dos controles do sistema; mantenha as descrições atualizadas conforme a interface muda.
- Descreva imagens com significado; descreva apenas a informação que a própria imagem transmite (não o contexto ao redor, como legendas próximas).
- Torne gráficos e infográficos totalmente acessíveis: forneça descrição concisa do que cada infográfico transmite, e disponibilize interações equivalentes para quem usa VoiceOver, se a versão visual permite interação.
- Exclua imagens puramente decorativas do VoiceOver.
- Use títulos e cabeçalhos para ajudar na navegação da hierarquia de informação; ofereça títulos únicos e sucintos, e cabeçalhos de seção precisos.
- Especifique como os elementos estão agrupados, ordenados ou vinculados, já que proximidade e alinhamento visual (pistas apenas visuais) não chegam ao VoiceOver por padrão.
- Lembre que VoiceOver lê elementos na ordem de leitura do idioma/locale ativo (em inglês dos EUA: de cima para baixo, da esquerda para a direita); agrupe imagem e legenda correspondente em um único frame de VoiceOver.
- Informe o VoiceOver quando ocorrem mudanças visíveis de conteúdo ou layout, para que a pessoa possa atualizar seu entendimento.
- Suporte o VoiceOver rotor quando possível, identificando cabeçalhos, links e outros tipos de conteúdo; o rotor também pode acionar o teclado braille.

### Especificações exatas
Nenhum número, medida ou valor consta no texto.

### Diferenças por plataforma
Nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS ou watchOS.
visionOS: gestos customizados não são acessíveis por padrão quando VoiceOver está ligado; apps e jogos que definem gestos customizados não recebem entrada de mão por padrão, para garantir que a pessoa possa explorar a interface por voz sem que o app reaja simultaneamente a gestos de mão. Uma pessoa pode optar pelo modo Direct Gesture, que desativa os gestos padrão do VoiceOver e permite que o app processe entrada de mão diretamente.

### Ligações com outros artigos
Cita Accessibility, Inclusion e Charts.

---

<!-- visual:voiceover -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura combina a figura de acessibilidade dentro de um círculo aberto azul marinho com um alto falante com ondas sonoras à esquerda, em azul escuro sobre degradê azul mais claro no canto superior esquerdo, com grade tracejada e círculo guia concêntrico ao símbolo humano (img 1224).
- O exemplo errado de agrupamento é uma tela de iPhone com voltar e mais opções no topo, parágrafo de texto provisório, duas fotos lado a lado (mangas e alcachofras), cada uma com legenda abaixo, e outro parágrafo; um retângulo preto fino envolve as duas fotos e as duas legendas como um único grupo, e um X branco em círculo cinza o acompanha (img 1225, 1226).
- O exemplo certo repete exatamente a mesma tela e o mesmo conteúdo, mas o retângulo envolve só a foto das mangas com a sua legenda, enquanto a foto das alcachofras e a legenda dela ficam fora de qualquer borda; um check branco em círculo verde o acompanha (img 1227, 1228).
- O par isola uma única variável, o lugar onde a borda de agrupamento é desenhada, e os marcadores de certo e errado aparecem sozinhos em quadros próprios, logo depois de cada exemplo, nunca desenhados sobre a captura (img 1225 a 1228).
<!-- /visual:voiceover -->

## Wallet (slug: wallet)

### O que governa
Rege como um app cria, adiciona, exibe e atualiza passes digitais (cartões, ingressos, cartões de fidelidade etc.) e pedidos rastreáveis no Apple Wallet, incluindo especificações exatas de imagens e verificação de identidade via Wallet.

### Por que
O fio condutor é que Wallet mantém um estilo visual consistente para construir familiaridade e confiança, então o design de um passe não deve apenas replicar a aparência da versão física, mas parecer nativo do Wallet. A hierarquia de campos (o que fica visível quando o passe está colapsado versus expandido) reflete o princípio de mostrar primeiro a informação essencial (data do evento, saldo da conta) e reservar o restante para quando a pessoa realmente precisar. Para pedidos (order tracking), a Apple prioriza confirmação imediata (a pessoa precisa saber que o pedido foi recebido mesmo que detalhes de fulfillment ainda não existam) e atualização contínua de status, porque isso reduz a ansiedade da espera. Na verificação de identidade, o princípio dominante é minimização e momento certo: pedir só o dado estritamente necessário (idade mínima em vez de data de nascimento), só no instante em que é preciso, e ser transparente sobre por quanto tempo o dado será retido, porque isso sustenta a confiança que torna o Verify with Wallet viável.

### Faça e evite
- Ofereça adicionar novos passes ao Wallet com um toque quando uma ação gera um passe (compra de ingresso, registro em programa de recompensas); para ações previsíveis e frequentes, pode adicionar em segundo plano após autorização única.
- Ajude a adicionar um passe criado fora do app (via site ou outro dispositivo); se a pessoa recusar, não pergunte de novo.
- Adicione passes relacionados como grupo (ex.: cartões de embarque de um voo com conexão) de uma vez só.
- Exiba um botão "Add to Apple Wallet" para permitir adicionar um passe existente que ainda não está no Wallet.
- Permita pular do app diretamente para o passe no Wallet, com um link do tipo "View in Wallet".
- Informe o sistema quando os passes expiram (data de expiração, data relevante, propriedade "voided"), para que o Wallet oculte passes expirados corretamente.
- Sempre peça permissão antes de excluir passes do Wallet.
- Ajude o sistema a sugerir um passe no momento relevante (ex.: aparecer na Lock Screen quando a pessoa chega à academia); para certos tipos, o sistema pode iniciar uma Live Activity.
- Mantenha os passes atualizados, refletindo mudanças (ex.: atraso de voo, mudança de portão).
- Use mensagens de mudança (change messages) apenas para atualizações de informação crítica em tempo; nunca para marketing.
- Use semantic tags (obrigatórias para poster event e semantic boarding passes) para habilitar layout automático; inclua também pass fields nesses casos para compatibilidade com versões antigas do iOS.
- Use Pass Designer para desenhar e pré-visualizar passes.
- Desenhe um passe que funcione bem em todos os dispositivos (Apple Watch mostra menos informação e imagens; não coloque informação essencial em elementos que podem estar ausentes; evite padding em imagens, pois watchOS recorta espaços em branco).
- Mantenha a frente do passe limpa: mostre informação essencial no cabeçalho (visível quando colapsado); reserve detalhes pouco usados para a folha de informações adicionais.
- Torne o passe instantaneamente identificável, usando cores de marca e elementos visuais (imagens, ícones, fundos de arte completa).
- Garanta contraste suficiente entre fundo e cor de texto.
- Use linguagem que funcione em qualquer dispositivo (evite frases específicas de um dispositivo, como "Slide to view", que não se aplica ao Apple Watch).
- Reserve imagens do passe apenas para conteúdo visual; use campos de texto e semantic tags para informação textual (texto embutido em imagem não é acessível); use Pass Designer ou APIs para código de barras, não embuta em imagem.
- Mantenha o tamanho de arquivo de imagem pequeno para downloads rápidos.
- Forneça um ícone de passe (pode reaproveitar o ícone do app ou desenhar um separado).
- Evite sombras internas (inner drop shadow) na arte do logo, pois reduzem a legibilidade.
- Para order tracking: facilite adicionar um pedido ao Wallet (ex.: com PKPaymentOrderDetails/ApplePayPaymentOrderDetails, ou o botão "Track with Apple Wallet" via AddOrderToWalletButton); torne a informação do pedido disponível imediatamente após a compra, mesmo que incompleta (com status como "Check back later for full order details"); forneça informação de fulfillment assim que disponível e mantenha o status atualizado; forneça logo em alta resolução com fundo não transparente; forneça imagens de produto distintas, em alta resolução, com fundo não transparente e representação direta (evitar contexto "lifestyle" ou fundo poluído); mantenha o texto breve; use linguagem clara e localizada, garantindo que o preço exibido bata com o preço final confirmado.
- Para detalhes de fulfillment: forneça um link para a área de gerenciamento do pedido (idealmente universal link); descreva claramente cada item; liste uma prioridade de apps instalados para o sistema linkar; evite notificações duplicadas; facilite o contato com o comerciante oferecendo múltiplos métodos (no mínimo, um link para o site do comerciante); ajude a rastrear o pedido com link direto da transportadora, código de barras para retirada, e instruções claras; mantenha a tela de fulfillment centrada em rastreamento, priorizando essa informação sobre outros conteúdos promocionais; escolha valores de status de shipping compatíveis com os dados disponíveis (nome da transportadora se souber, ou status genérico "shipped" se não tiver acesso a detalhes intermediários); seja direto e completo ao descrever status "Issue" ou "Canceled".
- Para verificação de identidade: apresente a opção de verificação via Wallet apenas quando o dispositivo suportar, com um fallback caso não suporte; peça a informação de identidade apenas no momento exato em que é necessária, nunca antes; descreva clara e sucintamente por que está pedindo a informação (purpose string em sentença completa, direta, específica, caixa de sentença, sem voz passiva, terminando em ponto); peça apenas o dado realmente necessário (ex.: limiar de idade mínima em vez de idade/data de nascimento exata); indique claramente se manterá o dado e por quanto tempo; escolha o botão de verificação do sistema adequado ao caso de uso ("Verify Age", "Verify Identity", "Continue", ou "Verify" genérico, cada um com variante multilinha para espaço restrito); o botão de verificação sempre usa letras brancas sobre fundo preto, com opção de contorno claro para contraste em fundos escuros; pode ajustar o raio dos cantos para combinar com outros botões.

### Especificações exatas
- Logo: largura mínima 50 pt, largura máxima 160 pt, altura 50 pt. Arquivo: logo.png.
- Primary logo: largura mínima 30 pt, largura máxima 126 pt, altura 30 pt. Arquivo: primaryLogo.png.
- Secondary logo: largura mínima 12 pt, largura máxima 135 pt, altura 12 pt. Arquivo: secondaryLogo.png.
- Icon: largura 38 pt, altura 38 pt (quadrado; cantos arredondados aplicados automaticamente pelo sistema). Arquivo: icon.png.
- Strip image: largura 375 pt, altura 144 pt. Arquivo: strip.png (suportado em coupon e store card).
- Thumbnail: largura mínima 60 pt, largura máxima 90 pt, altura 90 pt. Arquivo: thumbnail.png (event ticket e generic pass).
- Background (non-poster, event tickets): largura 343 pt, altura 503 pt. Arquivo: background.png.
- Background (poster, event tickets e poster generic passes): largura 358 pt, altura 448 pt. Arquivo: artwork.png.
- Footer (apenas airline boarding passes): largura 268 pt, altura 15 pt. Arquivo: footer.png.
- Imagens de logo e produto para order tracking: 300x300 pixels, formato PNG ou JPEG, fundo não transparente.
- Imagens de passe em geral: formato PNG, em @2x e @3x.

### Diferenças por plataforma
Nenhuma consideração adicional para iOS, iPadOS, macOS ou visionOS. Não suportado em tvOS.
watchOS: Wallet exibe passes em um carrossel de cartões roláveis; a pessoa pode adicionar o passe ao Apple Watch mesmo sem um app específico para watch; tocar em um passe revela uma tela de detalhes com rolagem. Cada estilo de passe define os campos e imagens que cabem nas três áreas básicas de layout (linha superior com logo e campo essencial; segunda linha com campo primário; terceira linha com campos secundário e auxiliar); informação que não cabe aparece na tela de detalhes rolável. Em todo estilo, watchOS recorta a imagem de strip para caber na proporção do cartão e pode recortar espaço em branco de outras imagens. O artigo detalha o layout específico de watchOS para boarding pass, coupon, store card, event ticket e generic pass (cada um com três linhas de conteúdo específico).

### Ligações com outros artigos
Cita Apple Pay, ID Verifier, Add to Apple Wallet guidelines, e documentação de desenvolvedor extensa (Wallet, PKPassLibrary.Capability.backgroundAddPasses, PKAddPassesViewController, PKAddPassButton, Pass, Wallet Passes, Wallet Orders, Order, LineItem, Merchant, ShippingFulfillment, VerifyIdentityWithWalletButton, PKIdentityIntentToStore, PKIdentityButton.Label, PKIdentityButton.Style.blackOutline, FinanceKitUI, FinanceKit, PassKit).

---

<!-- visual:wallet -->
### O que as ilustrações mostram
Base: 14 de 14 folhas de ilustrações abertas (img 1229 a 1283), todos os códigos conferidos; a página não tem vídeo nas notas.
- O ícone do Wallet é desenhado sobre uma grade de guias pontilhadas simétricas, com círculos concêntricos e retângulos alinhados ao centro do ícone, e a imagem inteira aparece tingida de azul (img 1229).
- Todos os estilos de passe repetem o mesmo esqueleto: cabeçalho com logo à esquerda e um dado curto à direita, corpo com o campo primário ou uma imagem de destaque, rodapé com a identificação da pessoa e o código de barras ou QR; entre passes muda a cor de fundo, não a estrutura de campos (img 1230, 1242 a 1249). No cartão de embarque a hierarquia desce da rota em letras grandes, com o ícone de avião entre os dois aeroportos, para o nome e selos arredondados de status, depois uma grade de colunas operacionais, e termina num QR grande centralizado (img 1242).
- Cada estilo trata a imagem de um jeito. O cupom usa uma faixa ilustrada estreita no topo com o valor do desconto em tipografia grande, e um diagrama com retângulos tracejados mostra que o campo primário fica sobreposto à própria faixa, não ao lado dela (img 1243, 1258). O ingresso poster tem ilustração dominante e um entalhe arredondado no topo do cartão (img 1244). O mesmo ingresso aparece com foto borrada de fundo mais miniatura e depois só com miniatura sobre azul sólido, mantendo campos e miniatura redonda nas mesmas posições e o código na parte inferior (img 1245, 1246). O passe genérico dispensa imagem de fundo e usa roxo sólido (img 1249).
- Contraste é ensinado em pares separados por marcadores, um check verde para o certo e um X cinza para o errado, nunca dentro da mesma imagem: o passe roxo com texto branco é legível, o mesmo passe com texto rosa quase se funde ao fundo (img 1236 a 1239); sobre imagem de fundo colorida e borrada, o texto branco em peso forte continua nítido (img 1240).
- Chamadas anotadas fixam a posição de cada elemento de marca: logo no canto superior esquerdo, antes do nome em texto (img 1250); logo primário quadrado acompanhado de texto de marca, ou logo só tipográfico e retangular ocupando o mesmo espaço (img 1253, 1254); logo secundário como emblema circular no canto inferior direito, junto ao nome do local (img 1255); miniatura quadrada de cantos arredondados no canto superior direito (img 1259). O par do saco de papel mostra a mesma silhueta plana e depois com uma faixa de sombra interna que a deixa com aspecto afundado, este último como o exemplo a evitar (img 1251, 1252). O ícone do passe aparece em dois lugares: à esquerda do texto no banner da tela de bloqueio, com cantos arredondados, e sobreposto no canto inferior esquerdo do QR dentro do cartão aberto (img 1256, 1257).
- Para as artes de fundo em tela cheia, a mesma ilustração é mostrada acabada e depois coberta por blocos azuis sólidos que marcam as zonas reservadas: no topo, barras para o cabeçalho (duas na arte do crânio, uma na da cachoeira), e embaixo um bloco maior para código e rodapé, em forma de T no passe com QR; as notas leem que a área reservada muda de tamanho conforme o código seja QR ou barras retangulares (img 1261 a 1264).
- O passe se encaixa em superfícies do sistema com regras visíveis: o botão preto de adicionar ao Wallet fica colado logo abaixo do passe, mais estreito que a tela e dentro do fluxo de rolagem da página (img 1231); o banner da tela de bloqueio traz uma miniatura reduzida do passe à direita do texto, acima dos atalhos de lanterna e câmera (img 1232); a Live Activity condensa o ingresso em três colunas de números grandes centralizados, sobre cartão preto (img 1233); as ações em destaque ficam fora do cartão, em blocos lado a lado com ícone colorido, título em negrito e subtítulo cinza (img 1234, 1257).
- O Pass Designer no Mac organiza a edição numa árvore lateral por tipo de campo (cabeçalho, primário, rodapé, verso) e mostra a prévia do passe à direita com uma etiqueta de versão mínima do iOS acima dele (img 1235).
- A tela de pedido é um template único que muda por estado: com o pedido feito há barra de progresso verde parcialmente preenchida; entregue, a barra some, entra um check verde ao lado do status e surge um link azul de rastreio (img 1265, 1266). Um diagrama numerado aponta cada campo, de logo e nome do comerciante até status, descrição, link de rastreio e itens com imagem, título, quantidade e preço (img 1268). Entrega e retirada dividem o mesmo template, trocando endereço por horário, local e um botão preto de código de barras (img 1271).
- No painel de pedidos, os ativos têm status em verde e miniaturas, enquanto o histórico do mês fica compacto, em cinza e sem miniaturas (img 1267). Os métodos de contato aparecem como lista de ações em texto azul com botão de cancelar, não como ícones (img 1270). A imagem de produto é especificada com réguas de 300 px nas duas bordas, sobre fundo sólido (img 1269).
- Os quatro botões de verificação de identidade usam um único desenho: fundo preto arredondado, ícone colorido do Wallet à esquerda e duas linhas de texto branco, a de ação menor e a de marca maior, mudando apenas a primeira linha (img 1272 a 1275).
- No Apple Watch os passes formam uma pilha vertical com o próximo cartão espiando por baixo, e ao abrir um passe o QR vai para uma área própria de fundo branco abaixo do cartão colorido (img 1276, 1277). Um diagrama de três linhas define o esqueleto (logo e dado essencial, depois primário, depois secundário e auxiliar) e é repetido por estilo: o cupom usa faixa de imagem na linha do meio e deixa a terceira sem uso; o cartão de loja deixa sem uso o topo direito; o ingresso põe texto do evento no meio; o genérico usa faixa no meio e nome e número embaixo; o número de linhas nunca muda (img 1278 a 1283).
Divergências registradas: a img 1241, apresentada como o exemplo de contraste insuficiente do ingresso de show, não mostra nesta cópia diferença perceptível em relação à img 1240; a folha 0014 tem só três imagens, a última da página é a img 1283.
<!-- /visual:wallet -->

## O que este grupo revela sobre o jeito Apple

1. Presença sobre tela: em SharePlay, o objetivo declarado não é "sincronizar dados" mas fazer pessoas sentirem que estão juntas, e isso molda desde a mecânica técnica (contexto espacial compartilhado) até regras de etiqueta social no design (resolver conflitos "naturalmente", deixar a pessoa optar por mudanças de imersão em vez de puxá-la). Ver shareplay.
2. Minimização de dados como princípio recorrente, não isolado: aparece em sign-in-with-apple (peça só o necessário, use idade mínima em vez de data de nascimento), em wallet (peça idade em vez de aniversário, retenha só pelo tempo necessário) e em shazamkit (grave o mínimo de áudio possível). É um valor transversal, não uma regra de uma única tecnologia. Ver sign-in-with-apple, wallet, shazamkit.
3. Terminologia de marca tratada como ativo legal e de reconhecimento, não como estilo: Siri nunca é traduzido nem tem pronome; SharePlay nunca leva adjetivo ou flexão; Sign in with Apple tem títulos de botão fechados a três opções; Tap to Pay on iPhone é reservado só para ações de pagamento. A Apple protege esses termos com regras quase jurídicas dentro do próprio guia de design. Ver siri, shareplay, sign-in-with-apple, tap-to-pay-on-iphone.
4. Especificação numérica extremamente detalhada quando envolve produção de ativos visuais (Wallet e o botão Sign in with Apple trazem tabelas de pt/px exatas), mas quase ausente quando o artigo é sobre comportamento conversacional ou de fluxo (Siri, Tap to Pay, VoiceOver, ShazamKit não têm nenhuma medida). Isso sugere que a Apple documenta com precisão numérica o que será produzido como asset gráfico, e com precisão de linguagem/comportamento o que será conversação ou lógica de app.
5. Timing como variável de design explícita: "peça login o mais tarde possível" (sign-in-with-apple), "peça identidade só no momento exato" (wallet), "pare de gravar assim que possível" (shazamkit), "prepare o Tap to Pay assim que o app abre" (tap-to-pay-on-iphone). O momento em que uma ação ou pedido acontece é tratado como tão importante quanto o conteúdo do pedido.
6. Fallback e degradação graciosa são exigidos, nunca opcionais: Wallet exige uma via alternativa quando o dispositivo não suporta verificação; Tap to Pay exige alternativa quando o pagamento falha; SharePlay exige alternativa para quem não tem spatial Persona; VoiceOver exige alternativa (Direct Gesture) para gestos customizados. Ver wallet, tap-to-pay-on-iphone, shareplay, voiceover.
7. Respeito ativo pela atenção e repetição: Siri adverte contra respostas longas porque "as pessoas podem ouvir a mesma resposta várias vezes"; SharePlay adverte contra transições frequentes de template; Wallet reserva change messages só para o crítico. A Apple trata a repetição de uma interação como motivo para cortar, não para enriquecer. Ver siri, shareplay, wallet.
8. Confiança do usuário como justificativa recorrente e explícita para regra de design, não apenas para privacidade: Sign in with Apple fala em "build on the trust that people have"; Wallet fala em "to help people trust your app"; Tap to Pay fala em impedir confusão de rótulo para não comprometer a confiança na transação. Confiança aparece como conceito de produto, não só de compliance. Ver sign-in-with-apple, wallet, tap-to-pay-on-iphone.
9. Consistência de rótulo do sistema versus liberdade visual do app: em quase todo artigo há uma linha rígida (texto do botão, nome do recurso, símbolo obrigatório) cercada de uma zona de liberdade explícita para cor, forma, fonte e sombra, desde que a marca Apple e a função fiquem imediatamente reconhecíveis. Isso aparece em sign-in-with-apple, tap-to-pay-on-iphone e wallet (botões de Verify with Wallet).
10. Multi-plataforma como preocupação de primeira classe, não pós-pensamento: SharePlay e Wallet dedicam seções inteiras a como a mesma experiência se comporta de forma diferente e ainda assim coerente em iPhone, Apple Watch e visionOS (cortes de imagem no watchOS, spatial templates no visionOS), reconhecendo que o mesmo passe ou atividade pode ser vivido por pessoas em dispositivos completamente diferentes ao mesmo tempo. Ver shareplay, wallet.

## Evidência de leitura
| Arquivo | Linhas lidas | Lido até o fim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/shareplay.md | 81 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/shazamkit.md | 28 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/sign-in-with-apple.md | 150 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/siri.md | 89 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/tap-to-pay-on-iphone.md | 104 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/voiceover.md | 50 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/wallet.md | 291 | sim |

Todos os 7 artigos do grupo foram lidos por inteiro em uma única chamada de Read cada, sem truncamento reportado pela ferramenta.
