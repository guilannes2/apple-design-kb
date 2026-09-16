# Technologies (parte 1)

## AirPlay (slug: airplay)

### O que governa
Como um app deve integrar, exibir e nomear o AirPlay, o recurso que transmite conteúdo de áudio e vídeo sem fio de iOS, iPadOS, macOS e tvOS para Apple TV, HomePod e TVs e alto-falantes compatíveis.

### Por que
A Apple prioriza consistência e confiança do usuário sobre customização: o player de mídia do sistema já resolve chapters, legendas e streaming de forma testada e familiar, então divergir dele custa engenharia sem ganho perceptível. O raciocínio de continuidade de playback ("as pessoas esperam que o programa continue enquanto checam o e-mail") governa várias regras: o app não é dono do momento de consumo, é só o canal. Na nomenclatura, a lógica é proteger a marca AirPlay como substantivo técnico e nunca como verbo ou selo do próprio app, para que o reconhecimento do usuário do ícone e do nome permaneça estável em qualquer app que o use.

### Faça e evite
- Prefira o media player fornecido pelo sistema; considere um player customizado só se o sistema não atender às necessidades do app.
- Forneça conteúdo na resolução mais alta possível na playlist HLS, cobrindo toda a faixa de resoluções.
- Não transmita conteúdo que só faz sentido dentro do contexto do app, como loops de fundo.
- Suporte tanto AirPlay streaming quanto mirroring.
- Suporte eventos de controle remoto (play, pause, fast forward) via lock screen, Siri ou HomePod.
- Não interrompa o playback quando o app for para segundo plano ou o dispositivo travar.
- Não interrompa o playback de outro app, exceto se o próprio app começar a tocar conteúdo imersivo.
- Mantenha o app funcional durante o AirPlay; não deixe outros vídeos do app começarem a tocar e interromperem o streaming.
- Se precisar de player customizado, replique aparência e comportamento dos botões do sistema, incluindo estados visuais distintos, e posicione o ícone AirPlay no canto inferior direito (iOS 16 e iPadOS 16 em diante).
- Use o ícone preto do AirPlay em fundos brancos ou claros, quando outros ícones de tecnologia também aparecerem em preto; use o branco em fundos escuros; use cor customizada quando outros ícones também usarem essa cor.
- Não use o ícone ou o nome AirPlay em botões ou elementos interativos customizados; use apenas de forma não interativa.
- Combine o ícone com o nome AirPlay corretamente, usando a mesma fonte do resto do layout.
- Dê mais destaque ao nome ou identidade do app do que ao AirPlay.
- Capitalize corretamente: "AirPlay", A e P maiúsculos, resto minúsculo; use versão toda maiúscula apenas se o layout for todo em maiúsculas.
- Use sempre AirPlay como substantivo, nunca como verbo ("Use AirPlay to listen", nunca "AirPlay to your speaker" ou "You can AirPlay with [App Name]").
- Use termos como "works with", "use", "supports", "compatible"; não diga "[App Name] has AirPlay".
- Pode combinar "Apple" com "AirPlay" ("Compatible with Apple AirPlay").

### Especificações exatas
- Posição do ícone AirPlay em player customizado: canto inferior direito, a partir de iOS 16 / iPadOS 16.

### Diferenças por plataforma
Sem considerações adicionais para iOS, iPadOS, macOS, tvOS ou visionOS. Não suportado em watchOS.

### Ligações com outros artigos
Cita Apple Trademark List e Guidelines for Using Apple Trademarks and Copyrights (uso de marca); referencia AVFoundation e AVKit (documentação de desenvolvedor).

---

<!-- visual:airplay -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (7 imagens, em aparência clara), códigos conferidos; sem vídeos.
- A abertura desenha o ícone AirPlay, um retângulo arredondado de tela com um triângulo encaixado na base, em azul escuro sobre degradê azul, com grade retangular e circular pontilhada; é a mesma construção das páginas accessibility e action-button, agora tingida de azul (img 0039).
- O player padrão do sistema, em pausa, sobrepõe controles translúcidos ao vídeo: no topo fechar, picture in picture, AirPlay e compartilhar; ao centro retroceder 10 segundos, pausar e avançar 10 segundos; embaixo a barra de progresso com tempo decorrido e restante; legendas e áudio no canto inferior direito (img 0040).
- Os ícones AirPlay aparecem como par fixo: áudio à esquerda, um triângulo sob três arcos concêntricos, e vídeo à direita, um triângulo sob um retângulo arredondado de tela (img 0041).
- O mesmo par é repetido três vezes na mesma disposição e só a cor muda com o fundo: preto sobre branco, branco dentro de um retângulo preto sólido e azul vibrante sobre branco, formando um guia de cor por contexto (img 0041, img 0042, img 0043).
- Na parte de nomenclatura, certo e errado usam selos isolados, check verde em círculo verde e X cinza em círculo cinza, cada um em sua própria célula, sem estarem emparelhados na mesma imagem como em outras páginas (img 0044, img 0045).
<!-- /visual:airplay -->

## Always On (slug: always-on)

### O que governa
Como um app deve se comportar quando o dispositivo entra no estado Always On (tela sempre ativa em baixo consumo), presente em iPhone 14 Pro / Pro Max e Apple Watch.

### Por que
O princípio central é "informação útil e vislumbrável de forma privada e de baixo consumo": o sistema escurece a tela e reduz movimento para poupar energia e não expor dados a observadores casuais. A regra de "não parar movimento instantaneamente, mas transicionar graciosamente" existe para que a transição não pareça um erro ao usuário. A regra de manter layout consistente evita que mudanças na interface chamem atenção indesejada quando o telefone está deitado com a tela virada para cima, situação em que o movimento na tela fica visível mesmo sem o usuário olhar diretamente.

### Faça e evite
- Oculte informação sensível, como saldos bancários ou dados de saúde, incluindo o que poderia aparecer em notificação.
- Mantenha outros tipos de informação pessoal vislumbráveis quando fizer sentido (por exemplo, ritmo cardíaco durante treino no Apple Watch); o usuário pode desligar o Always On se não quiser nenhuma informação visível.
- Mantenha conteúdo importante legível e escureça conteúdo não essencial (texto secundário, imagens, preenchimentos de cor).
- Mantenha um layout consistente; evite mudanças de interface distrativas ao entrar ou sair do Always On.
- Ao entrar no Always On, prefira transicionar um componente interativo para uma aparência indisponível em vez de simplesmente removê-lo.
- Dentro do Always On, faça atualizações infrequentes e sutis (por exemplo, um app esportivo pausa atualizações jogada a jogada e só atualiza o placar quando muda).
- Transicione graciosamente o movimento para um estado de repouso; não pare instantaneamente.

### Especificações exatas
Nenhum número, medida ou valor padrão presente no texto.

### Diferenças por plataforma
Sem considerações adicionais para iOS ou watchOS. Não suportado em iPadOS, macOS, tvOS ou visionOS.
- No iPhone 14 Pro e iPhone 14 Pro Max, o sistema exibe itens da Lock Screen como Widgets e Live Activities quando o dispositivo é colocado virado para cima e parado.
- No Apple Watch, ao abaixar o pulso, o sistema escurece o mostrador e continua exibindo a interface do app, desde que ele esteja em primeiro plano ou rodando uma sessão em segundo plano.

### Ligações com outros artigos
Cita Notifications (para orientação sobre ocultar informação pessoal em notificações) e Designing for watchOS.

---

<!-- visual:always-on -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (1 imagem, em aparência clara), código conferido; sem vídeos.
- O sketch de abertura é um retângulo vertical de cantos arredondados, silhueta de relógio ou de tela, em azul escuro sobre degradê de azul para roxo (img 0052).
- O interior da silhueta é preenchido por hachura de listras diagonais paralelas e uniformes, e não por um pictograma figurativo nítido (img 0052).
- Um pequeno retângulo sólido se destaca no canto superior esquerdo da forma, lido como coroa digital ou botão lateral (img 0052).
- A grade circular e retangular pontilhada sobreposta e a tinta monocromática em degradê repetem o padrão das outras páginas de ícone único, mudando apenas a cor e a forma interna (img 0052).
Divergências registradas: a descrição oficial fala de um Apple Watch com uma pessoa correndo, mas na imagem não se distingue figura humana; o que aparece é só a hachura diagonal uniforme.
<!-- /visual:always-on -->

## App Clips (slug: app-clips)

### O que governa
Como projetar, distribuir e sinalizar visualmente um App Clip, versão leve de um app ou jogo que oferece uma experiência instantânea sem exigir download do app completo.

### Por que
O princípio é velocidade e foco: um App Clip existe para resolver uma tarefa pontual ("in-the-moment") ou demonstrar o app completo, preservando a privacidade das pessoas por tempo limitado. A Apple restringe funcionalidades (sem tab bars, sem operações em segundo plano, dados apagados entre lançamentos) porque o contrato implícito com o usuário é "isso é leve e temporário, não estou instalando nada permanente". A ênfase em não pedir criação de conta e em oferecer Apple Pay/Sign in with Apple decorre do mesmo princípio: reduzir atrito e reduzir a superfície de dados pessoais coletados num contexto transitório. As regras de App Clip Code (impressão, cor, tamanho) existem para garantir uma experiência de leitura confiável e para proteger a marca Apple, já que qualquer distorção do código reduz a taxa de escaneamento com sucesso.

### Faça e evite
Design do App Clip
- Permita completar uma tarefa ou demo inteiramente no App Clip, sem exigir instalação do app completo.
- Foque em recursos essenciais; reserve recursos avançados para o app completo.
- Não use App Clips só para fins de marketing nem para exibir anúncios.
- Evite web views; use componentes e frameworks nativos.
- Projete uma interface linear, fácil de usar e focada, sem tab bars nem navegação complexa.
- No lançamento, mostre a parte mais relevante do App Clip, pulando etapas desnecessárias.
- Garanta uso imediato: inclua todos os assets necessários, omita splash screens, nunca faça a pessoa esperar.
- Mantenha o App Clip pequeno para lançamento rápido; reduza código e assets desnecessários; evite baixar dados adicionais.
- Torne o App Clip compartilhável via link, inclusive para pontos específicos dentro dele.
- Facilite o pagamento; considere Apple Pay para checkout expresso.
- Evite exigir criação de conta antes de entregar valor; se for necessária, limite a informação pedida (ex.: Sign in with Apple).
- Ao instalar o app completo, ofereça experiência familiar e focada, sem exigir novo login.

Privacidade
- Limite a quantidade de dados armazenados; não dependa de dados salvos anteriormente, pois o sistema pode ter removido o App Clip e apagado seus dados.
- Se armazenar dados de login, guarde-os de forma segura fora do dispositivo.
- Considere Sign in with Apple.
- Ofereça forma segura de pagamento, como Apple Pay.

Mostrar o app completo
- Não comprometa a experiência pedindo instalação do app completo de forma abusiva.
- Escolha o momento certo para recomendar o app (quando a pessoa completa uma tarefa ou chega a uma pausa natural), usando SKOverlay.
- Recomende de forma não intrusiva e educada; não peça repetidamente nem interrompa a tarefa; não use push notifications para isso.

Notificações
- App Clips podem agendar e receber notificações por até 8 horas após o lançamento.
- Peça permissão para período estendido só se realmente necessário.
- Mantenha notificações focadas na tarefa; não envie notificações puramente promocionais.

App Clips para negócios
- Use branding consistente, priorizando a marca do negócio sobre a do provedor da plataforma.
- Trate múltiplos negócios/localizações corretamente, verificando a localização ao lançar.

Conteúdo do App Clip Card
- Seja informativo sobre o que o App Clip oferece.
- Prefira fotografia e gráficos a screenshots da interface do app.
- Evite texto na imagem de cabeçalho (não é localizável).
- Use imagem PNG ou JPEG de 1800x1200 px sem transparência.
- Use copy conciso: título de até 30 caracteres e subtítulo de até 56 caracteres.
- Escolha o verbo do botão de ação: View (mídia ou conteúdo educacional/informativo), Play (jogos), Open (demais casos).

App Clip Codes
- Use sempre os designs fornecidos pela Apple, seguindo tamanho, posicionamento e regras de impressão.
- Escolha entre o design com badge (com logo do App Clip) ou sem logo quando o espaço for limitado.
- Inclua o logo do App Clip quando o espaço permitir; use o design sem logo em itens de papel/plástico descartável ou associados a jogos de azar/bebida (cartas de baralho, fichas de poker, porta-copos de bar).
- Coloque o código em superfície plana ou cilíndrica; em superfície cilíndrica, a largura do código não pode exceder um sexto da circunferência.
- Evite materiais deformáveis (papel, plástico, tecido) que dobram ou amassam; se necessário, monte em algo rígido como um cartão.
- Garanta iluminação suficiente para escaneamento confiável e evite exigir ângulo muito amplo.
- Não sobreponha texto, logos ou imagens; nunca anime ou escureça o código.
- Exiba o código sempre na posição correta (não rotacionado).
- Nunca crie sua própria variação do design; não aplique filtros, glows, sombras, gradientes ou reflexos; ao escalar, não altere a proporção e escale todos os atributos (incluindo espessura de traço) proporcionalmente.
- Deixe espaço livre mínimo ao redor do código igual ao espaço entre o glifo central e o código circular.

Impressão
- Teste códigos impressos antes de distribuir, verificando escaneamento de vários ângulos.
- Use materiais de impressão de alta qualidade e não texturizados, acabamento fosco; evite brilho, verniz reflexivo ou holográfico; use laminado fosco se laminar; use materiais resistentes a UV em ambientes externos.
- Trabalhe com impressão flexográfica em serviço profissional; use impressora jato de tinta em impressão própria.
- Use imagens de alta resolução; calibre a impressora.
- Converta o SVG (sRGB) para CMYK com intenção colorimétrica relativa (media-relative); use perfil ICC "Generic CMYK" (impressoras CMYK) ou "Gracol 2013 ICC profile" (impressoras CMYKOV), com tolerância de cor CIELab Delta E de 2,5.
- Em impressora só em escala de cinza, gere apenas códigos em escala de cinza.
- Para código com NFC integrado, use tags NFC Tipo 5.

Verificação de calibração da impressora
- Use as folhas de teste de calibração fornecidas pela Apple para verificar o par de cores escolhido e as configurações de escala de cinza.

### Especificações exatas
- Imagem do App Clip Card: 1800x1200 px, PNG ou JPEG, sem transparência.
- Título do App Clip Card: máximo 30 caracteres.
- Subtítulo do App Clip Card: máximo 56 caracteres.
- App Clip Code impresso: diâmetro mínimo de 3/4 polegada (1,9 cm).
- App Clip Code digital: tamanho mínimo de 256x256 px, arquivo PNG ou SVG.
- App Clip Code com NFC integrado: tag NFC de no mínimo 35 mm de diâmetro (ou tamanho equivalente); se a tag NFC embutida for de 35 mm, o código impresso precisa ter no mínimo 1,37 polegada (3,48 cm) de diâmetro.
- Distância de leitura para tamanho do código: proporção de no máximo 20:1; proporção recomendada de 10:1. Exemplo dado: um código lido a 40 polegadas (101 cm) de distância precisa ter no mínimo 4 polegadas (10,16 cm) de diâmetro.
- Largura do código em superfície cilíndrica: no máximo um sexto (60 graus) da circunferência.
- Resolução mínima ao rasterizar o SVG: 600 ppi; impressão com resolução mínima de 300 dpi.
- Tolerância de cor na conversão CMYK: CIELab Delta E de 2,5.
- Notificações de App Clip: disponíveis por até 8 horas após o lançamento.

### Diferenças por plataforma
Sem considerações adicionais para iOS ou iPadOS. Não suportado em macOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Cita Apple Pay, Sign in with Apple, Guidelines for Using Apple Trademarks, NFC (mensagens de call-to-action com NFC) e Legal requirements (uso de marcas registradas da Apple).

---

<!-- visual:app-clips -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações vistas (24 imagens, em aparência clara), códigos conferidos; sem vídeos.
- A abertura desenha um ícone de app em azul com os quatro cantos feitos de traços curtos separados, expondo que o formato nasce de arcos de canto alinhados a uma grade de eixos horizontal, vertical e diagonal centrada (img 0053).
- O cartão do App Clip ocupa a metade inferior da tela de bloqueio, sobre o papel de parede, com hierarquia clara: título em negrito, descrição curta em duas linhas, botão azul "Open" à direita e atribuição discreta abaixo, com ícone pequeno do app e link para a App Store (img 0054).
- Aberto, o App Clip é uma tela funcional completa, não uma prévia: lista vertical de itens com miniatura circular, nome, preço e controles de quantidade, fechando num botão arredondado de pedido que mostra a contagem (img 0055).
- Dois cartões lado a lado repetem a mesma estrutura de moldura, imagem de fundo, título, descrição e botão, cada um com seu próprio conteúdo, e o verbo do botão muda com o tipo: Play para o jogo e Open para o app (img 0056).
- O código tem duas variantes: badge arredondado com anéis concêntricos tracejados ao redor de um ícone de câmera e o logotipo App Clip dentro, e o círculo de anéis solto, sem moldura nem texto (img 0057, img 0058).
- A anatomia é ensinada com linhas de chamada horizontais, primeiro pela estrutura (ícone central, código visual dos anéis, logotipo) e depois pela cor (fundo, cor gerada no tom intermediário dos anéis, primeiro plano no ícone e no texto) (img 0059, img 0076).
- O uso físico é contado em dois planos ligados por um círculo azul de destaque: pessoas numa mesa de cafeteria com um totem e, ao lado, o close da tela do telefone reconhecendo o código; na versão de mensagem clara, o close mostra título acima do código e frase de instrução abaixo, como uma peça única (img 0060, img 0071).
- Para superfície cilíndrica, um círculo é dividido em seis fatias iguais e o arco do código ocupa uma delas, com cota angular de 60 graus (img 0061).
- A orientação correta tem o glifo central em pé; as variantes erradas mostram o glifo deitado e o glifo girado em losango, julgadas por selos isolados de check verde e X cinza (img 0062 a 0066).
- O diâmetro mínimo aparece como seta dupla com cota de 3/4 de polegada, aplicada separadamente ao badge e ao círculo sem logotipo (img 0067, img 0068).
- Um App Clip Code e um QR code ficam em retângulos rosa de mesma altura, marcada por linha vermelha no topo; o espaço livre é uma faixa rosa com a mesma cota x repetida em todos os lados de cada código (img 0069, img 0070).
- A customização permitida aparece numa fileira de quatro cores (badge vermelho e verde, círculo azul e laranja) com a mesma estrutura, e os erros vêm um por vez, isolando uma única variável: proporção ovalada, gradiente de fundo e sombra projetada (img 0072, img 0073, img 0074, img 0075).
Divergências registradas: para img 0064 a descrição oficial fala do código girado 90 graus para a esquerda, mas na imagem só o glifo central muda de orientação e os anéis externos parecem iguais, então a rotação do código inteiro não é visualmente óbvia na célula isolada.
<!-- /visual:app-clips -->

## Apple Pay (slug: apple-pay)

### O que governa
Como oferecer, integrar, customizar e nomear o Apple Pay em apps e sites, incluindo o checkout, o payment sheet, botões, o Apple Pay mark, assinaturas e doações.

### Por que
O princípio dominante é confiança e simplicidade no ponto de pagamento: o payment sheet deve refletir exatamente o que será cobrado, de quem, e quando, porque dinheiro real está em jogo. A regra de "tornar o Apple Pay a opção primária quando há credenciais disponíveis" reflete a lógica de que o Apple Pay resolve o atrito de digitar dados de cartão, e esconder essa opção é considerado um desserviço ao usuário. As regras sobre o Apple Pay mark versus botão (nunca usar o mark como botão) e sobre nunca personalizar a API dos botões nascem do mesmo compromisso de reconhecimento visual consistente que aparece em AirPlay: qualquer variação criada por terceiros quebra a confiança de que aquele é realmente um fluxo Apple Pay seguro. A exigência de comunicar claramente valores pendentes, assinaturas e cobranças futuras (ex. "Amount Pending") decorre do princípio de transparência financeira: nunca deixar a pessoa autorizar um valor sem entender o que está autorizando.

### Faça e evite
Oferecendo Apple Pay
- Ofereça Apple Pay em todos os dispositivos e navegadores que o suportam; não apresente a opção se o dispositivo não suportar.
- Torne o Apple Pay a opção de pagamento primária quando houver credenciais disponíveis (mas não necessariamente a única); não o separe em um fluxo à parte.
- Use botões Apple Pay somente para iniciar pagamento ou, quando apropriado, o processo de configuração.
- Se usar botão customizado para iniciar o Apple Pay, ele não pode exibir "Apple Pay" nem o logo; deve haver o Apple Pay mark ou referência textual na mesma página.
- Use o Apple Pay mark apenas para comunicar que o Apple Pay é aceito; nunca como botão de pagamento.
- Não esconda um botão Apple Pay nem o faça parecer indisponível; se não puder ser usado ainda, sinalize o problema após o toque/clique.
- Informe mecanismos de busca que o Apple Pay é aceito, via marcação semântica.
- Todo site que oferece Apple Pay precisa de política de privacidade e deve aderir às regras de uso aceitável.

Checkout
- Ofereça experiência de checkout coesa, com a marca do app/site mantida; evite abrir novas páginas/janelas.
- Presuma que as pessoas querem usar o Apple Pay quando disponível; considere mostrá-lo em primeiro lugar, maior, ou separado visualmente.
- Ofereça botões Apple Pay em páginas de produto para compra rápida de item individual; se o item já estiver no carrinho, remova-o do carrinho após a compra.
- Ofereça checkout expresso para compras com múltiplos itens.
- Suporte cupons e códigos promocionais diretamente no payment sheet, especialmente em fluxos de checkout expresso.
- Colete informação necessária (cor, tamanho) antes do botão Apple Pay; sinalize e navegue automaticamente até o campo problemático se faltar dado.
- Colete informação opcional (mensagens de presente, instruções de entrega) antes do checkout ou mesmo depois da compra concluída, pois não há como inserir dado opcional no payment sheet.
- Reúna múltiplos métodos e destinos de envio antes de mostrar o payment sheet, já que ele só permite um método/destino por pedido.
- Para retirada em loja, ajude a escolher o local antes de mostrar o payment sheet.
- Prefira as informações de checkout vindas do Apple Pay, assumindo que estão completas e atualizadas.
- Evite exigir criação de conta antes da compra; peça na página de confirmação do pedido, com campos pré-preenchidos.
- Reporte resultados da transação no payment sheet, incluindo mensagens de erro.
- Exiba página de confirmação/agradecimento após a compra; mencionar Apple Pay na confirmação é opcional, mas se mencionar, mostre após os últimos quatro dígitos da conta ou como nota separada (ex.: "1234 (Apple Pay)" ou "Paid with Apple Pay").

Customizando o payment sheet
- Apresente e peça apenas informação essencial, para evitar confusão ou preocupação com privacidade.
- Mostre o cupom/código ativo, ou permita inserção no próprio sheet.
- Deixe escolher o método de envio no sheet, com descrição, custo e, opcionalmente, data estimada de entrega/retirada.
- Use line items para explicar cobranças adicionais, descontos, custos pendentes, doações adicionais, pagamentos recorrentes e futuros; não use line items para listar itens do pedido.
- Mantenha line items curtos, cabendo em uma linha sempre que possível.
- Forneça o nome do negócio após a palavra "Pay" na mesma linha do total (ex.: "Pay [Business_Name]").
- Se não for o comerciante final, identifique ambos os negócios (ex.: "Pay [End_Merchant_Business_Name (via Your_Business_Name)]").
- Divulgue claramente quando custos adicionais podem ocorrer após a autorização, usando um line item "Amount Pending" quando o total não for conhecido no momento do checkout.
- Trate erros de entrada e pagamento de forma clara, ajudando a resolver rapidamente.
- Não adicione spinners ou indicadores de progresso adicionais; o payment sheet já cuida disso.

Ícone do site
- Sites que suportam Apple Pay podem fornecer um ícone que aparece durante autorização de pagamento, notavelmente no Handoff.

Tratando problemas
- Verifique dados no aparecimento do sheet, em mudanças de campo e após autenticação; use mensagens claras e consistentes.
- Não force conformidade com a lógica de negócio própria; ignore dados irrelevantes e infira dados ausentes quando possível (ex.: ignorar dígitos extras de CEP em vez de exigir correção).
- Reporte problemas ao sistema com o código de status correto.
- Explique o problema de forma clara e sucinta, referenciando o campo relevante; use frases nominais com capitalização de sentença e sem pontuação final; procure manter mensagens em até 128 caracteres para evitar truncamento.
- Ao ocorrer interrupção (cancelamento, timeout), cancele qualquer pagamento em andamento; a pessoa pode reiniciar tocando novamente no botão.

Assinaturas
- Esclareça os detalhes da assinatura antes de mostrar o payment sheet (frequência de cobrança, termos).
- Inclua line items reiterando frequência de cobrança, descontos e taxas adicionais; se nenhum pagamento for exigido na autorização, divulgue quando a cobrança ocorrerá.
- Comunique claramente os termos do período de teste, incluindo valor do teste (mesmo que $0), valor regular após o teste e data de início da cobrança regular.
- Esclareça o valor atual sendo cobrado no momento da autorização, na linha de total.
- Só mostre o payment sheet quando a mudança de assinatura resultar em taxas adicionais; se o custo diminuir ou permanecer igual, autorização não é necessária.
- Trate o campo de acordo de faturamento (billing agreement) como resumo em linguagem simples, não substituto dos termos formais; deixe em branco na dúvida.

Doações
- Use um line item para identificar a doação (ex.: "Donation $50.00").
- Ofereça valores de doação predefinidos e uma opção "Other Amount".

Botões Apple Pay
- Use sempre a API fornecida pela Apple para criar botões; nunca crie designs customizados nem tente replicá-los.
- Escolha o tipo de botão que melhor se encaixa na terminologia do fluxo (Buy, Pay, Check Out, Continue, Book, Donate, Subscribe, Reload, Add Money, Top Up, Order, Rent, Support, Contribute, Tip, ou o genérico Apple Pay).
- Use o botão "Set Up Apple Pay" em Settings, perfil ou página interstitial quando o dispositivo suporta mas a pessoa não configurou ainda.

Estilo dos botões
- Use o estilo automático para deixar a aparência do sistema decidir; ou escolha manualmente: preto (fundos claros com contraste suficiente, nunca em fundo escuro), branco com contorno (fundos claros sem contraste suficiente, nunca em fundo escuro/saturado), branco (fundos escuros com contraste suficiente, nunca em fundo claro).

Tamanho e posição do botão
- Exiba o botão Apple Pay com destaque; não o torne menor que outros botões de pagamento; evite exigir rolagem para vê-lo.
- Em layout lado a lado, posicione o botão Apple Pay à direita de um botão "Add to Cart"; em layout empilhado, posicione acima.
- Pode ajustar o raio de canto para combinar com o resto da interface (cantos retos ou formato cápsula).
- Mantenha tamanho mínimo e margens; a tradução do título pode variar de tamanho por localidade, se não couber, o sistema substitui pelo botão Apple Pay simples (não há substituição automática para "Set Up Apple Pay").

Apple Pay mark
- Use apenas a arte fornecida pela Apple, sem alterações além da altura; a altura deve ser igual ou maior que outras marcas de bandeira de pagamento no fluxo.
- Não ajuste largura, raio de canto ou proporção; não adicione símbolo de marca registrada nem outro conteúdo; não remova a borda; não adicione sombras, glows ou reflexos; não inverta, rotacione ou anime.
- Mantenha espaço livre mínimo ao redor do mark.

Referindo-se ao Apple Pay
- Use "Apple Pay" exatamente como consta na Apple Trademark List; nunca no plural nem possessivo.
- Capitalize com A e P maiúsculos, resto minúsculo; tudo maiúsculo só se necessário para conformar a um estilo tipográfico existente.
- Nunca use o logo da Apple para representar a palavra "Apple" em texto.
- Nos EUA, use o símbolo de marca registrada (®) na primeira aparição em corpo de texto; não inclua o símbolo quando Apple Pay aparecer como opção de seleção no checkout.
- Coordene a fonte com o app/site; não imite a tipografia da Apple.
- Nunca traduza "Apple Pay" ou qualquer marca Apple.
- Em contexto de seleção de pagamento, só use descrição só-texto do Apple Pay se todas as demais opções também forem só-texto; caso contrário, use o Apple Pay mark.
- Ao promover o Apple Pay em um app, siga as diretrizes de marketing da App Store.

### Especificações exatas
- Ícone do site: @2x = 60x60 pt (120x120 px); @3x = 60x60 pt (180x180 px).
- Botão "Apple Pay" (genérico): largura mínima 100pt (100px @1x, 200px @2x), altura mínima 30pt (30px @1x, 60px @2x), margem mínima de 1/10 da altura do botão.
- Botão "Book with Apple Pay": largura mínima 140pt (140px @1x, 280px @2x), altura mínima 30pt (30px @1x, 60px @2x), margem mínima de 1/10 da altura do botão (mesma regra vale para Buy, Check Out, Donate, Set Up, Subscribe with Apple Pay, conforme tabela da fonte).
- Espaço livre mínimo ao redor do Apple Pay mark: 1/10 de sua altura.
- Mensagens de erro de validação: procurar manter até 128 caracteres para evitar truncamento.

### Diferenças por plataforma
Sem considerações adicionais para iOS, iPadOS, macOS, visionOS ou watchOS. Não suportado em tvOS.

### Ligações com outros artigos
Cita In-app purchase (para venda de bens virtuais), PKPaymentAuthorizationController, applePayCapabilities, Offering Apple Pay in Your App, Checking for Apple Pay availability, PKDateComponentsRange, paymentSummaryItems, Supporting donations, PKPaymentAuthorizationViewControllerDelegate, PKPaymentError, Apple Pay Status Codes, PKPaymentButtonType, PKPaymentButtonStyle, WKInterfacePaymentButton, App Store marketing guidelines, e Apple Pay Marketing Guidelines page.

---

<!-- visual:apple-pay -->
### O que as ilustrações mostram
Base: 14 folhas de ilustrações vistas (54 imagens, em aparência clara), códigos conferidos; sem vídeos.
- O payment sheet no iPhone tem estrutura em blocos: X de fechar no canto superior esquerdo, marca Apple Pay centralizada, título com Pay e o nome do negócio, valor total como o maior texto da tela, cartão em gradiente, linha do método de pagamento, linhas de resumo com valor alinhado à direita e, no rodapé, a indicação de confirmar pelo botão lateral (img 0094).
- Com botão customizado, a marca Apple Pay fica empilhada acima do botão de ação "Order Now", ambos centralizados num cartão cinza, marcado com check verde; a versão errada repete "Apple Pay" no texto do botão e recebe X cinza (img 0095 a 0098).
- A confirmação pós compra coloca check verde e agradecimento com número do pedido no topo, e só abaixo oferece criar conta, cadastro com Apple e campos de login com botão desabilitado (img 0099).
- Os line items formam um bloco próprio separado por divisória acima de Subtotal, com rótulo à esquerda e valor à direita em coluna; na web o sheet é mais largo e espaçoso, com cabeçalho de nome e domínio, total em negrito, Cancel no canto superior direito no lugar do X e confirmação por símbolo de impressão digital (img 0100, img 0101, img 0104, img 0108).
- O erro de validação é sinalizado só por texto vermelho no campo de envio e no rótulo de atualizar endereço, sem ícone de alerta e sem mudar o layout, em app e web; na web o erro aparece também dentro do seletor de endereços recentes, item por item (img 0103, img 0104, img 0105).
- Assinaturas ganham um bloco de recorrência com ícone circular laranja de setas, valor mensal e datas de início e fim; a variável troca o valor pelo título "Amount Pending", e a sem cobrança na autorização mostra $0.00 no topo reforçado por um bloco de teste gratuito com a data em que a cobrança começa (img 0106, img 0107, img 0109).
- O botão do sistema pode exibir o cartão ativo: logotipo Pay à esquerda, uma barra vertical fina e a miniatura do cartão à direita (img 0111).
- Todos os botões seguem um único template, retângulo preto de cantos arredondados com texto branco centralizado e o símbolo da Apple no lugar da palavra, variando só o verbo inicial; há a versão mínima só com símbolo e Pay e a de configuração (img 0112 a 0128).
- Os três estilos são mostrados em pares de fundo claro e escuro: preto, branco com contorno e branco; o uso errado se revela pela perda de contraste, com o botão quase sumindo no fundo, sem check nem X (img 0129 a 0134).
- Tamanho e ordem usam sempre os mesmos dois botões trocando uma só variável: mesma largura e altura contra Apple Pay menor; lado a lado, colados, com Apple Pay à direita de "Add to Cart"; empilhados e alinhados à esquerda, com Apple Pay acima; o raio de canto reto, padrão ou cápsula é aplicado igual aos dois (img 0135 a 0143).
- Os diagramas de medida usam contorno rosa e cotas em pontos: altura mínima de 30, largura mínima de 100 para o botão só com Pay e de 140 para o botão de doação, e margem mínima de 1/10 da altura (img 0144, img 0145).
- A marca Apple Pay, com fundo branco e contorno cinza fino, fica numa fileira com três outras marcas de bandeira, todas no mesmo tamanho e formato retangular arredondado, e é tratada como uma bandeira de pagamento entre as outras, não como botão (img 0146).
Divergências registradas: as notas apontam que o texto que antecede img 0117 fala de reservas, enquanto o botão mostrado é o de doação, ligado ao parágrafo seguinte.
<!-- /visual:apple-pay -->

## Augmented reality (slug: augmented-reality)

### O que governa
Como projetar experiências de realidade aumentada em iOS e iPadOS com ARKit: coaching, posicionamento de objetos, interação, experiências multiusuário, reconhecimento de objetos reais, comunicação com o usuário e tratamento de interrupções.

### Por que
O princípio central é a "ilusão convincente": tudo, desde escala e iluminação de objetos virtuais até a taxa de atualização de cena, existe para que o objeto pareça realmente habitar o mundo físico. A regra de atualizar a cena 60 vezes por segundo, por exemplo, decorre diretamente disso: abaixo dessa taxa, o objeto "pula ou pisca" e a ilusão quebra. As regras de segurança e conforto (introduzir movimento gradualmente, evitar fadiga, evitar movimentos perigosos) refletem que AR tira a atenção do ambiente físico real, criando risco real de acidente. As regras de comunicação evitando termos técnicos como "ARKit" ou "tracking" refletem o princípio de acessibilidade: AR é conceito avançado que pode intimidar, então a linguagem deve ser amigável e orientada à ação (o que fazer), não ao diagnóstico técnico.

### Faça e evite
- Ofereça recursos de AR apenas em dispositivos capazes; se o app depende primariamente de AR, restrinja a dispositivos com suporte a ARKit; se opcional, não mostre erro, apenas omita o recurso.
- Use o máximo da tela para mundo físico e objetos virtuais; evite poluir com controles e informação.
- Busque ilusões convincentes: texturas realistas, escala e posicionamento corretos em superfícies detectadas, refletir condições de iluminação e simular grão de câmera, sombras difusas de cima para baixo, atualizar a cena 60 vezes por segundo.
- Prefira superfícies refletivas pequenas ou ásperas, já que os reflexos do ARKit são aproximações.
- Use áudio e hápticos para reforçar a imersão (confirmar contato de objeto virtual com superfície).
- Minimize texto no ambiente; mostre só a informação necessária.
- Considere exibir informação/controles adicionais em screen space (espaço de tela fixo, não preso ao ambiente AR).
- Considere controles indiretos (2D em screen space) para controles persistentes; use translucidez para não bloquear a cena.
- Comunique claramente requisitos e expectativas do app para diferentes ambientes reais.
- Seja atento ao conforto das pessoas; posicione objetos a distância que reduza necessidade de aproximar o dispositivo; em jogos, mantenha níveis curtos com pausas.
- Introduza movimento gradualmente se o app encoraja movimento físico.
- Seja atento à segurança; evite encorajar movimentos rápidos, amplos ou súbitos.

Coaching
- Use a coaching view integrada para mostrar o que fazer e dar feedback durante a inicialização; também pode ajudar na relocalização após interrupção.
- Oculte a UI desnecessária do app enquanto a coaching view estiver presente.
- Ofereça coaching customizado apenas se necessário, usando a view do sistema como referência.

Posicionamento de objetos
- Mostre quando é possível localizar superfície e posicionar objeto, alinhando o indicador visual ao plano detectado.
- Integre o objeto imediatamente ao ambiente AR ao ser posicionado; refine sutilmente a posição depois, se necessário (ex.: "empurrar" de volta para dentro da superfície detectada).
- Considere guiar para objetos virtuais fora da tela com pistas visuais ou sonoras.
- Evite alinhar objetos precisamente às bordas de superfícies detectadas, pois são aproximações.
- Incorpore classificação de plano (ex.: só permitir móveis em plano "floor", tabuleiro de jogo em plano "table").

Interações com objetos
- Prefira manipulação direta (tocar diretamente no objeto) quando possível; controles indiretos funcionam melhor quando a pessoa está se movendo.
- Use gestos padrão e familiares (arrastar com um dedo para mover, girar com dois dedos para rotacionar).
- Mantenha interações simples, já que gestos de toque são bidimensionais mas AR é tridimensional.
- Responda a gestos dentro de proximidade razoável de objetos interativos, já que precisão é difícil em objetos pequenos, finos ou distantes.
- Permita escala de objeto quando fizer sentido no app (ex.: mundo imaginário sim; app de móveis reais não, pois escalar não ajuda a visualizar o tamanho real).
- Nunca use escala como forma de ajustar distância percebida de um objeto.
- Cuidado com gestos potencialmente conflitantes (pinça de dois dedos versus rotação de dois dedos); teste a interpretação correta.
- Busque movimento de objeto consistente com a física do ambiente AR; evite objetos que pulem, desapareçam e reapareçam.
- Explore métodos de interação além de gestos, como movimento e proximidade.

Experiência multiusuário
- Cada participante mapeia o ambiente independentemente e o ARKit funde os mapas automaticamente.
- Considere permitir oclusão: pessoas capturadas pela câmera podem ocluir objetos virtuais posicionados atrás delas.
- Quando possível, permita que novos participantes entrem em experiência AR em andamento (map merging implícito).

Reagindo a objetos do mundo real
- Use imagens e objetos de referência 2D/3D para que o ARKit detecte quando e onde aparecem no ambiente atual.
- Ao uma imagem detectada desaparecer, considere atrasar a remoção de objetos virtuais anexados por até um segundo antes de esmaecer ou remover, para evitar flickering.
- Limite o número de imagens de referência ativas simultaneamente; a detecção funciona melhor com 100 ou menos imagens distintas. Se precisar de mais, alterne o conjunto ativo conforme o contexto (ex.: usar localização para saber em qual parte do museu a pessoa está).
- Limite o número de imagens de referência que exigem posição precisa, pois atualizar a posição consome mais recursos; use tracked image quando a imagem pode se mover ou quando a animação/objeto anexado é pequeno comparado ao tamanho da imagem.

Comunicando com as pessoas
- Se precisar exibir texto instrucional, use terminologia acessível; evite termos técnicos como "ARKit", "world detection" e "tracking".
- Prefira dicas em 3D em contexto tridimensional (ex.: indicador de rotação 3D ao redor do objeto) em vez de texto 2D, exceto se a pessoa não responder às dicas contextuais.
- Torne texto importante legível: use screen space para rótulos e instruções críticas; se precisar exibir texto no espaço 3D, garanta que fique de frente para a pessoa e no mesmo tamanho de tipo independente da distância.
- Se necessário, forneça um jeito de obter mais informação, com indicador visual apropriado.

Tratando interrupções
- ARKit não consegue rastrear posição/orientação durante interrupção (ex.: troca de app, chamada); após a interrupção, objetos previamente posicionados provavelmente aparecem na posição errada.
- Use relocalização para restaurar objetos à posição original usando novas observações.
- Considere usar a coaching view para ajudar na relocalização, guiando a pessoa de volta à posição/orientação anterior.
- Considere ocultar objetos virtuais previamente posicionados durante a relocalização, para evitar flickering, e reexibi-los na nova posição.
- Minimize interrupções se o app suporta experiências AR e não AR, embutindo a experiência não AR dentro da AR quando possível.
- Permita cancelar a relocalização, já que ela pode continuar indefinidamente sem sucesso; ofereça botão de reset ou outra forma de reiniciar.
- Indique quando a câmera frontal não consegue rastrear um rosto por mais de cerca de meio segundo, com indicador visual; se precisar de texto, mantenha mínimo.

Sugerindo resolução de problemas
- Permita reiniciar a experiência se não atender às expectativas, sem forçar espera por melhores condições.
- Sugira correções possíveis para problemas de detecção de superfície (falta de luz, superfície muito reflexiva, superfície sem detalhe suficiente, movimento excessivo de câmera).

Ícones e badges
- Apps podem exibir o ícone AR em controles que iniciam experiências baseadas em ARKit.
- Use o glifo AR apenas para iniciar experiência baseada em ARKit; nunca altere (exceto tamanho e cor), nem use para outros fins, nem em conjunto com experiências AR não criadas com ARKit.
- Mantenha espaço livre mínimo ao redor do glifo AR.
- Apps com coleções de produtos podem usar badges para identificar itens visualizáveis em AR.
- Use os badges AR (colapsado ou expandido) apenas para identificar objetos visualizáveis em AR via ARKit; nunca altere ou mude a cor.
- Prefira o badge AR completo ao badge só-glifo; use o só-glifo em espaços restritos.
- Use badging apenas quando o app misturar objetos visualizáveis em AR e objetos que não são; se todos os objetos forem visualizáveis em AR, badging é redundante.
- Mantenha posicionamento de badge consistente (mesmo canto), legível e não muito grande a ponto de ocluir detalhe importante da foto.
- Mantenha espaço livre mínimo ao redor do badge AR.

### Especificações exatas
- Taxa de atualização de cena AR: 60 vezes por segundo.
- Espaço livre mínimo ao redor do glifo AR: 10% da altura do glifo.
- Espaço livre mínimo ao redor do badge AR: 10% da altura do badge.
- Atraso ao esconder objeto de imagem que desapareceu: até um segundo antes de fade out/remoção.
- Limite recomendado de imagens de referência ativas simultaneamente: 100 ou menos.
- Indicação de perda de rastreamento de rosto: cerca de meio segundo sem rastreio.

### Diferenças por plataforma
Sem considerações adicionais para iOS ou iPadOS. Não suportado em macOS, tvOS ou watchOS.
- visionOS: ARKit pode ser usado para detectar superfícies no ambiente da pessoa, usar posições de mão e dedos para informar gestos customizados, e suportar interações que incorporam objetos físicos próximos em experiências imersivas.

### Ligações com outros artigos
Cita Playing haptics, Playing audio, Gestures, Occluding virtual content with people, Detecting Images in an AR Experience, Managing Session Life Cycle and Tracking Quality, Designing custom gestures in visionOS, Immersive experiences, e a documentação de desenvolvedor ARKit.

---

<!-- visual:augmented-reality -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações (23 imagens, em aparência clara) e 1 folha de vídeo (8 quadros) vistas, códigos conferidos.
- A abertura mostra seis setas azul escuras saindo de um centro comum como eixos tridimensionais, sobre gradiente azul com grade e círculo; o glifo AR reaproveita o mesmo traço, isolado em preto sobre branco, sem gradiente nem grade (img 0160, img 0175).
- No Measure, a medição é um círculo branco translúcido com linha pontilhada e rótulo de valor perto da ponta, enquanto os controles 2D persistentes ficam na barra inferior (desfazer, botão central grande de adicionar, captura) e nas abas da base, sobre a cena real da câmera (img 0161).
- Coaching e relocalização reaproveitam o mesmo indicador de superfície translúcido e pontilhado, e o texto muda: no início, um plano em trapézio no chão com um iPhone ilustrado e o pedido para mover o iPhone; após interrupção, numa tela cinza escura, o pedido para voltar à área anterior, acrescido de um botão "Start Over" em cápsula escura (img 0162, img 0172).
- O indicador de posicionamento próprio do app combina oval azul claro com arco espesso preenchido na base, círculo tracejado externo, ponto central cruzado por linha horizontal e quatro colchetes de mira nos cantos do cartão escuro (img 0163).
- Manipulação direta e controle indireto usam o mesmo cubo cinza: no primeiro, o dedo toca a quina com linha pontilhada e seta curva de arraste; no segundo, dois botões quadrados pretos de rotação, horária e anti-horária, ficam abaixo do objeto (img 0164, img 0165).
- As restrições de movimento usam uma esfera cinza clara: sobre grade isométrica, dois eixos pontilhados, vermelho e azul, com setas nas quatro direções do plano; para rotação num só eixo, uma linha vertical pontilhada e uma faixa azul em seta envolvendo a esfera (img 0166, img 0167).
- A dica 3D destaca em azul a face frontal esquerda do cubo e o circunda com uma seta curva completa; a alternativa 2D troca isso por um rótulo "Rotate" em cápsula escura sobre a grade, logo abaixo do cubo (img 0168, img 0169).
- Etiquetas pretas com texto e seta ficam ligadas por linhas finas à mesa e à cadeira na vista de câmera, com botão circular de voltar no canto superior esquerdo; a tela de detalhe seguinte é cheia e dividida em duas colunas, objeto à esquerda e nome, preço, dimensões e botão preto de compra à direita, com X no canto superior direito (img 0170, img 0171).
- Iluminação suficiente e insuficiente são a mesma cena de mesa e cadeira, no mesmo ângulo, apenas em tom claro e em tom escuro, sem marcador de certo ou errado (img 0173, img 0174).
- O glifo aparece em composição num botão azul "View in AR", branco à esquerda do texto, e como selo pequeno no canto superior esquerdo de cada item de uma grade de colecionáveis (img 0176, img 0178).
- Os selos expandido, com glifo e texto AR, e só glifo ficam num retângulo cinza claro arredondado sobre fundo quadriculado de transparência; o espaço livre mínimo do glifo e de cada selo é marcado por um quadro rosa translúcido, sem cotas numéricas (img 0179, img 0180, img 0177, img 0181, img 0182).
- No vídeo, um meteoro 3D texturizado gira em ritmo e sentido constantes acima de uma mesa real, com a etiqueta "meteor" ancorada logo abaixo e parada durante a rotação; uma barra lateral translúcida escura à esquerda lista arquivos com miniatura, nome, data e tamanho, com botões Select e Search, e fica fixa em todos os quadros enquanto a sala permanece estática (vídeo 005, folha 0001, q001 a q008).
Divergências registradas: para img 0163 a descrição oficial fala de formas em ângulo reto emoldurando um quadrado e de um indicador em perspectiva 3D com a borda mais longa embaixo, mas o desenho visto é essencialmente frontal, com a base sugerida só pelo arco mais grosso; a descrição oficial do vídeo não menciona a barra lateral de arquivos nem a etiqueta ancorada, visíveis em todos os quadros.
<!-- /visual:augmented-reality -->

## CareKit (slug: carekit)

### O que governa
Como projetar apps CareKit, usados para gerenciar planos de cuidado relacionados a doenças crônicas, recuperação de lesão/cirurgia, ou metas de saúde e bem-estar, incluindo privacidade de dados, integração com HealthKit/ResearchKit e as views de tarefas, gráficos e contatos.

### Por que
O princípio dominante e explícito é a proteção de dados extremamente sensíveis: "nada é mais importante do que proteger a privacidade das pessoas e salvaguardar os dados extremamente sensíveis que seu app CareKit coleta e armazena". Isso explica por que a permissão de acesso a dados de saúde deve ser pedida no contexto exato de uso (não no lançamento do app) e por que o gerenciamento de compartilhamento de dados de saúde deve passar exclusivamente pelas configurações de privacidade do sistema, nunca por telas próprias do app: a Apple quer um único ponto de controle e confiança para o usuário. Na parte de conteúdo, a lógica das cinco variações de task view (simple, instructions, log, checklist, grid) é dar precisão sem verbosidade: descrever a tarefa com o mínimo de palavras necessárias, porque a pessoa já está em contexto de tratamento e a clareza reduz erro. A regra de branding refinado e não intrusivo decorre do mesmo raciocínio de "não é publicidade, é cuidado": distrair de um plano de saúde com marca é visto como prejudicial ao propósito do app.

### Faça e evite
Dados e privacidade
- Forneça uma política de privacidade clara com URL acessível na App Store.
- Peça permissão antes de acessar dados via recursos e capacidades do iOS, protegendo tanto dados inseridos manualmente quanto dados obtidos do dispositivo/sistema.

Integração com HealthKit
- Peça acesso a dados de saúde apenas quando necessário no contexto (ex.: peso, no momento de registrar peso, não no lançamento do app).
- Esclareça a intenção do app com mensagens descritivas na tela padrão de permissão; evite telas customizadas que repliquem o comportamento da tela padrão.
- Gerencie compartilhamento de dados de saúde apenas via Settings > Privacy do sistema; não construa telas adicionais no app para isso.

Dados de movimento
- Com permissão, obtenha dados de movimento do dispositivo (parado, andando, correndo, pedalando, dirigindo) e, ao andar/correr, contagem de passos, ritmo e lances de escada.
- Dados de movimento podem incluir dados customizados de fisioterapia (ex.: tarefas ResearchKit testando flexibilidade, amplitude de movimento, capacidade ambulatorial).

Fotos
- Com permissão, acesse câmera e fotos para compartilhar imagens de progresso de tratamento com a equipe de cuidado.

Integração com ResearchKit
- Incorpore recursos ResearchKit para exibir pesquisas, tarefas e gráficos relacionados, se apropriado; use o módulo de consentimento informado para pedir permissão de coleta/compartilhamento de dados.

Views do CareKit
- Use cada tipo de view (tarefas, gráficos, contatos) para seu propósito pretendido, mantendo consistência.
- Tarefas apresentam ações prescritas (tomar medicação, comer alimentos específicos, exercitar-se, reportar sintomas); gráficos exibem dados/tendências de progresso; contatos exibem informação de contato com suporte a telefone, mensagem, e-mail e mapa.

Tarefas
- Use o estilo simple para tarefa de uma etapa.
- Use o estilo instructions quando precisar adicionar texto informativo a uma tarefa simples.
- Use o estilo log para ajudar a registrar eventos, com timestamp automático a cada registro.
- Use o estilo checklist para listar ações/etapas de uma tarefa multi-etapa.
- Use o estilo grid para exibir grade de botões em tarefa multi-etapa de forma mais compacta; é o único estilo com acesso à collection view subjacente, permitindo elementos de UI customizados.
- Considere usar cor para reforçar o significado dos itens de tarefa (ex.: uma cor para medicações, outra para atividades físicas), mas nunca como único meio de transmitir informação.
- Combine precisão com simplicidade ao descrever tarefa e etapas (ex.: nome comercial do medicamento em vez de descrição química); minimize palavras quando o contexto já esclarece o significado.
- Considere complementar tarefas complexas ou multi-etapa com vídeos ou imagens.

Gráficos
- Considere destacar narrativas e tendências para ilustrar progresso.
- Rotule elementos do gráfico de forma clara e sucinta, evitando repetir a mesma informação (ex.: usar "BPM" no rótulo do eixo em vez de em cada ponto de dado).
- Use cores distintas; evite tons diferentes da mesma cor para significados diferentes; garanta contraste suficiente.
- Considere fornecer uma legenda quando as cores não forem imediatamente claras.
- Denote claramente as unidades de tempo (segundos, minutos, horas, dias, semanas, meses, anos).
- Consolide grandes conjuntos de dados para maior legibilidade.
- Se necessário, deslocar (offset) dados para manter gráficos proporcionais quando houver diferença significativa entre pontos.

Contact views
- Considere usar cor para categorizar membros da equipe de cuidado.

Notificações
- Minimize notificações, já que planos de cuidado variam de paciente para paciente; considere consolidar múltiplos itens em uma única notificação.
- Considere fornecer uma detail view de notificação para permitir ação imediata sem abrir o app.

Símbolos e branding
- A maioria dos estilos de view funciona melhor com os símbolos fornecidos pelo CareKit; a exceção é a grid-style task view, altamente customizável.
- Em grid view, considere SF Symbols para símbolos relevantes ao conteúdo do app.
- Projete um símbolo de cuidado relevante, relacionado ao app ou ao conceito geral de saúde/bem-estar; evite símbolo puramente decorativo ou logo corporativo.
- Incorpore branding refinado e discreto; as pessoas não querem ver publicidade em app CareKit.

### Especificações exatas
Nenhum número, medida, duração ou valor padrão presente no texto (a estrutura de views é descrita qualitativamente, sem dimensões).

### Diferenças por plataforma
Sem considerações adicionais para iOS ou iPadOS. Não suportado em macOS, tvOS, visionOS ou watchOS. Apple Watch pode exibir notificações do app CareKit (remete a Notifications).

### Ligações com outros artigos
Cita Color, Accessibility, HealthKit, ResearchKit, Notifications, e a documentação de desenvolvedor CareKit, Core Motion, UIImagePickerController, requestAuthorization(toShare:read:completion:) e Protecting user privacy.

---

<!-- visual:carekit -->
### O que as ilustrações mostram
Base: 4 folhas de ilustrações vistas (img 0216 a 0229), todos os códigos conferidos; sem vídeo.
- O símbolo do CareKit é desenhado sobre grade tracejada com círculo guia de construção: um coração com traço de eletrocardiograma dentro de uma forma azul em três camadas empilhadas, como cartões sobrepostos, em contorno azul escuro sobre degradê azul (img 0216).
- A tela típica é uma pilha vertical: fileira de sete círculos de dia no topo (dias completos com check vermelho preenchido, o dia selecionado com contorno mais grosso), a data e, abaixo, cartões de tarefa e de gráfico empilhados, incluindo um gráfico de barras vermelhas e cinzas com legenda de cor (img 0217).
- A anatomia do cartão é anotada com linhas de chamada: header com título e disclosure indicator no canto superior direito, separador horizontal e subview de conteúdo embaixo (img 0219); header com disclosure indicator e separador reaparecem sem marcações nos estilos instructions, log e checklist (img 0221 a 0223), e o contato detalhado também abre com header e separador (img 0229).
- Os estilos de tarefa reaproveitam o mesmo cartão branco de cantos arredondados e trocam só o subview: simple com um círculo vermelho grande e check branco, sem instrução (img 0220); instructions com texto de instrução e botão retangular cinza claro "Completed" em texto vermelho (img 0221); log com botão vermelho sólido "Log" e carimbo de hora do registro com ícone de relógio abaixo (img 0222); checklist com três linhas separadas por fio fino, cada uma com seu círculo de check, e instrução no rodapé (img 0223).
- O exemplo associado ao estilo grid compacto repete o cartão de horários: três círculos, dois com check vermelho preenchido e um só com contorno vazio, junto do texto de instrução (img 0219, 0224).
- Os estados de conclusão são codificados pelo preenchimento: círculo vermelho cheio com check para feito, círculo apenas contornado para pendente, e o header resume o que falta, como "1 remaining" (img 0219, 0223, 0224).
- Os três estilos de gráfico usam o mesmo cartão, título, eixo Y com linhas de grade tracejadas em 2.0 e 4.0, eixo X com as iniciais dos sete dias e legenda de cor com quadrado vermelho; muda só a marca de dado, barra (img 0225), ponto (img 0226) ou linha contínua (img 0227), e o dia do pico aparece destacado num círculo vermelho preenchido no eixo (img 0225, 0226).
- O contato vem em dois níveis do mesmo cabeçalho (avatar circular cinza, nome em negrito, especialidade abaixo): simple é uma linha única com disclosure indicator (img 0228); detailed acrescenta separador, texto descritivo, fileira de três botões quadrados com ícone e rótulo vermelhos para ligar, mensagem e e-mail, e um bloco cinza claro de endereço com seta de navegação à direita (img 0229).
- A tela de contatos repete dois cartões com a estrutura do detalhado: foto de perfil genérica, texto descritivo, três botões pequenos lado a lado com ícone e texto vermelhos para ligar, mensagem e e-mail, e uma linha de endereço com ícone de navegação à direita (img 0218).
- Uma única cor de destaque, o vermelho, atravessa checks, seletor de dias, barras, botão de registro e ações de contato, enquanto fundos e botões secundários ficam em branco e cinza claro (img 0217 a 0229).
<!-- /visual:carekit -->

## CarPlay (slug: carplay)

### O que governa
Como projetar apps CarPlay usando os templates definidos pelo sistema (áudio, comunicação, navegação, abastecimento), cobrindo interações com iPhone, áudio, layout, cor, ícones/imagens e tratamento de erros.

### Por que
O princípio central, declarado explicitamente, é que "CarPlay é projetado para motoristas usarem enquanto dirigem": toda regra decorre da premissa de que a pessoa está com atenção limitada e não pode nem deve manusear o iPhone. Isso explica por que interações no iPhone devem ser eliminadas quando o CarPlay está ativo, por que o app nunca pode travar o acesso ao CarPlay exigindo entrada no iPhone (que pode estar na mala do carro), e por que erros devem ser reportados no CarPlay e nunca redirecionar a pessoa para pegar o iPhone. A regra de áudio (não iniciar playback automaticamente, não mudar o volume geral) reflete que o app coexiste com outras fontes de áudio do carro, como rádio, e o motorista, não o app, deve controlar o volume final. A regra de testar cores em condições reais de luz do carro reflete que o ambiente de uso é imprevisível (dia, noite, reflexos), diferente de testar numa tela de computador.

### Faça e evite
Interações com iPhone
- Elimine interações do app no iPhone quando o CarPlay estiver ativo; qualquer setup deve ocorrer antes do veículo em movimento.
- Nunca trave o CarPlay porque o iPhone conectado exige entrada; o app precisa funcionar mesmo com o iPhone inacessível (na bolsa, no porta-malas).
- Garanta que o app funcione sem exigir que o iPhone esteja desbloqueado, já que a maioria usa CarPlay com o iPhone travado.

Áudio
- Deixe a pessoa escolher quando iniciar o playback; evite início automático, exceto se o propósito do app for tocar uma única fonte de áudio ou estiver retomando áudio interrompido.
- Evite iniciar sessão de áudio antes de estar pronto para tocar, pois isso silencia outras fontes (rádio do carro).
- Inicie o playback assim que o áudio tiver carregado o suficiente; o sistema mantém a seleção destacada e mostra indicador de atividade até o app sinalizar que está pronto.
- Exiba a tela Now Playing quando o áudio estiver pronto; não atrase o playback esperando informação descritiva completar o carregamento, mostre-a quando disponível.
- Retome o playback após interrupção apenas quando apropriado (ex.: após chamada telefônica); interrupções permanentes (como playlist iniciada pela Siri) não são retomáveis.
- Ajuste automaticamente níveis de áudio quando necessário, mas não altere o volume geral; a pessoa controla o volume final de saída.

Layout
- Forneça informação útil e de alto valor em layout limpo, fácil de escanear a partir do banco do motorista; não polua com detalhes não essenciais.
- Mantenha aparência geral consistente; elementos com funções similares devem parecer similares.
- Garanta que o conteúdo primário se destaque e pareça acionável; itens grandes parecem mais importantes e são mais fáceis de tocar; em geral, coloque o conteúdo e controles mais importantes na metade superior da tela.

Cor
- Prefira paleta de cores limitada, coordenada com o logo do app.
- Evite usar a mesma cor para elementos interativos e não interativos.
- Teste o esquema de cores sob várias condições de iluminação em um carro real, considerando brilho à noite e washout sob luz solar direta.
- Garanta boa aparência em ambientes claro e escuro, já que o CarPlay suporta ambas aparências e pode ajustar automaticamente conforme a iluminação.
- Escolha cores que comuniquem efetivamente com todos, considerando diferenças de percepção de cor.

Ícones e imagens
- Forneça imagens de alta resolução com fatores de escala @2x e @3x para toda a arte do app no CarPlay.
- Espelhe o ícone do app do iPhone; um bom ícone funciona bem em ambos sem precisar de segundo design.
- Não use preto para o fundo do ícone; clareie um fundo preto ou adicione borda para não se misturar com o fundo da tela.

Tratamento de erros
- Reporte erros no CarPlay, não no iPhone conectado; nunca direcione a pessoa a pegar o iPhone para ler ou resolver um erro.

### Especificações exatas
- Tamanhos de tela comuns citados: 800x480 px (5:3), 960x540 px (16:9), 1280x720 px (16:9), 1920x720 px (8:3).
- Ícone do app CarPlay: @2x = 120x120 px; @3x = 180x180 px.

### Diferenças por plataforma
Sem considerações adicionais para iOS. Não suportado em iPadOS, macOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Cita Inclusive color e a documentação de desenvolvedor CarPlay App Programming Guide.

---

<!-- visual:carplay -->
### O que as ilustrações mostram
Base: 1 folha de ilustração vista (img 0230), código conferido; sem vídeo.
- O único desenho da página é o símbolo de abertura: um "C" em contorno azul escuro grosso com um triângulo de play centralizado dentro dele (img 0230).
- O símbolo fica sobre fundo em degradê de azul arroxeado para azul claro, com grade de linhas tracejadas e círculo guia de construção, o mesmo sistema de desenho de ícones temáticos usado em outras páginas do HIG (img 0230).
- Nenhuma tela de CarPlay, template, layout, paleta aplicada ou ícone de app é ilustrada; o material visual só confirma o esboço do ícone descrito oficialmente, e as medidas de tela e de ícone da página não têm apoio em imagem (img 0230).
<!-- /visual:carplay -->

## Game Center (slug: game-center)

### O que governa
Como integrar Game Center (rede social de jogos da Apple) em um jogo: access point, Game Overlay/dashboard, achievements, leaderboards, challenges e atividades multiplayer.

### Por que
O princípio declarado é ampliar descoberta e conexão social do jogo através do sistema (App Store, notificações, app Games), então a integração deve ser "seamless" e não competir visualmente com o próprio jogo. Isso explica regras como "evite exibir o access point durante gameplay ativo, splash screens ou tutoriais": o Game Center deve aparecer nos momentos de pausa natural (menu, configurações), não interromper a imersão. A regra de terminologia correta (usar "Game Center", "Achievements", "Leaderboards" e não sinônimos como "Trophies" ou "Rankings") busca uma linguagem uniforme entre jogos para que o jogador reconheça o sistema em qualquer app. Nas challenges, a regra de rastrear a pontuação mais recente em vez de progresso geral ou recorde pessoal existe explicitamente para manter jogadores regulares e novos em pé de igualdade ("level playing field"), evitando vantagem injusta a jogadores veteranos.

### Faça e evite
Acessando o Game Center
- Determine se o jogador está conectado à conta Game Center do sistema ao lançar o jogo; se não estiver, inicialize o jogador nesse momento, para experiência mais fluida e maximizar oportunidades de descoberta (ex.: Top Played chart, recomendações sociais).

Access point
- Exiba o access point em telas de menu; considere adicioná-lo ao menu principal ou área de configurações.
- Evite exibir o access point durante gameplay ativo, em splash screens temporárias, fluxos cinemáticos ou tutoriais que precedam o menu principal.
- Evite posicionar controles perto do access point, já que ele tem versão colapsada e expandida; verifique sobreposição com UI importante.
- Considere pausar o jogo enquanto o Game Overlay ou dashboard estiver presente.

UI customizada
- Use a arte que o Game Center fornece em links customizados, preservando a aparência sem ajustar dimensões ou efeitos visuais.
- Use a terminologia correta em links customizados: "Game Center" (não GameKit, GameCenter, game center), "Game Center Profile" (não Profile, Account, Player Info), "Achievements" (não Awards, Trophies, Medals), "Leaderboards" (não Rankings, Scores, Leaders), "Challenges" (não Competitions), "Add Friends" (não Add, Add Profiles, Include Friends).

Achievements
- Alinhe-se aos quatro estados de achievement do Game Center: locked, in-progress, hidden, completed; o sistema agrupa por status de conclusão.
- Determine a ordem de exibição no momento do upload, já que essa é a ordem final (ex.: seguindo o caminho mais comum pelo jogo).
- Seja sucinto ao descrever achievements: título e descrição limitados a duas linhas cada, com truncamento além disso; use title-style capitalization no título e sentence-style na descrição.
- Dê senso de progresso ao usar achievements progressivos, que exibem mensagens motivacionais automáticas de progresso.
- Projete imagens ricas e de alta qualidade; evite reutilizar o mesmo asset para mais de um achievement; sem asset fornecido, o card mostra imagem placeholder.
- Mantenha o conteúdo centralizado, já que o sistema aplica máscara circular à imagem de achievement.

Leaderboards
- Escolha o tipo de leaderboard: classic (rastreia melhor pontuação de todos os tempos, sempre ativo, sem fim) ou recurring (reseta em intervalo definido, como semanal ou diário).
- Use leaderboard sets para organizar múltiplos leaderboards, agrupando por temas ou experiências de jogo (modos de dificuldade, tipos de atividade, gêneros/temas).
- Adicione imagens de leaderboard para reforçar a estética visual do jogo; crie imagem única para cada leaderboard que reflita a jogabilidade envolvida.
- Em iOS, iPadOS e macOS, use uma única imagem; em tvOS, forneça conjunto de imagens que anima quando em foco.
- Esteja atento a como o corte (cropping) pode afetar a arte: em iOS/iPadOS/macOS o sistema corta arte de leaderboards que fazem parte de um set; em tvOS o efeito de foco pode cortar camadas nas bordas; mantenha o conteúdo primário confortavelmente visível.

Challenges
- Crie challenges engajantes: atividades curtas e baseadas em habilidade, com forma clara de medir realização; crie challenges de 1 a 5 minutos de jogabilidade que o jogador completa individualmente.
- Evite criar challenges que rastreiem progresso geral ou pontuações pessoais recordes, pois dão vantagem injusta a jogadores regulares; em vez disso, rastreie a pontuação mais recente de cada tentativa, para manter todos os jogadores em pé de igualdade.
- Facilite o acesso ao challenge: sempre faça deep-link para o modo/nível exato onde o desafio começa; ajude jogadores de primeira viagem a completar onboarding inicial antes de começar.
- Crie arte de alta qualidade que encoraje engajamento; evite posicionar o conteúdo primário onde o título/descrição do challenge possa cobri-lo; forneça versões localizadas de texto na imagem via App Store Connect ou Xcode.

Atividades multiplayer
- Use party codes para convidar jogadores para atividades multiplayer em tempo real.
- Permita que jogadores entrem tarde, saiam cedo e retornem depois; forneça forma de visualizar o código atual do grupo no jogo; permita inserção manual do código.
- Suporte atividades multiplayer via UI dentro do jogo, aproveitando o Game Overlay e o dashboard do Game Center, que ajudam a encontrar jogadores sem sair do jogo.
- Forneça arte de atividade envolvente, já que a imagem de preview aparece em vários pontos do sistema.

### Especificações exatas
- Party codes do Game Center: tipicamente oito caracteres alfanuméricos (exemplo dado: "2MP4-9CMF").
- Duração recomendada de uma challenge: 1 a 5 minutos de jogabilidade.
- Título e descrição de achievement: limitados a duas linhas cada, com truncamento além disso.

Imagem de achievement (iOS, iPadOS, macOS, visionOS):
| Atributo | Valor |
| Formato | PNG, TIF ou JPG |
| Espaço de cor | sRGB ou P3 |
| Resolução | 72 DPI (mínimo) |
| Tamanho da imagem | 512x512 pt (1024x1024 px @2x) |
| Diâmetro da máscara | 512 pt (1024 px @2x) |

Imagem de achievement (tvOS):
| Atributo | Valor |
| Formato | PNG, TIF ou JPG |
| Espaço de cor | sRGB ou P3 |
| Resolução | 72 DPI (mínimo) |
| Tamanho da imagem | 320x320 pt (640x640 px @2x) |
| Diâmetro da máscara | 200 pt (400 px @2x) |

Imagem de leaderboard (iOS, iPadOS, macOS):
| Atributo | Valor |
| Formato | JPEG, JPG ou PNG |
| Espaço de cor | sRGB ou P3 |
| Resolução | 72 DPI (mínimo) |
| Tamanho da imagem | 512x512 pt (1024x1024 px @2x) |
| Área recortada | 512x312 pt (1024x624 px @2x) |

Imagem de leaderboard (tvOS):
| Atributo | Valor |
| Formato | PNG, TIF ou JPG |
| Espaço de cor | sRGB ou P3 |
| Resolução | 72 DPI (mínimo) |
| Tamanho da imagem | 659x371 pt (1318x742 px @2x) |
| Tamanho em foco | 618x348 pt (1236x696 px @2x) |
| Tamanho fora de foco | 548x309 pt (1096x618 px @2x) |

Imagem de challenge:
| Atributo | Valor |
| Formato | JPEG, JPG ou PNG |
| Espaço de cor | sRGB ou P3 |
| Resolução | 72 DPI (mínimo) |
| Tamanho da imagem | 1920x1080 pt (3840x2160 px @2x) |
| Área recortada | 1465x767 pt (2930x1534 px @2x) |

Imagem de atividade multiplayer: mesmas dimensões da imagem de challenge (1920x1080 pt / 3840x2160 px @2x, área recortada 1465x767 pt / 2930x1534 px @2x).

Imagem do dashboard tvOS:
| Atributo | Valor |
| Tamanho da imagem | 600x180 pt (1200x360 px @2x) |
| Formato | PNG, TIF ou JPG |
| Espaço de cor | sRGB ou P3 |
| Resolução | 72 DPI (mínimo) |

### Diferenças por plataforma
Sem considerações adicionais para iOS, iPadOS, macOS ou visionOS.
- Em iOS, iPadOS e macOS, o access point leva ao Game Overlay, um overlay do sistema.
- Em visionOS e tvOS, o access point leva ao in-game dashboard, uma view em tela cheia sobre o jogo; em visionOS, a localização do access point varia conforme o tipo de jogo (imersivo ou baseado em volume).
- tvOS: pode-se exibir uma imagem opcional no topo do dashboard (não usar o ícone do app para isso).
- watchOS: recursos e API do GameKit estão disponíveis, mas não há UI do Game Center invocável no watchOS; o conteúdo aparece no iPhone conectado.

### Ligações com outros artigos
Cita Designing for games, Game controls, Apple Design Resources, Focus and selection, e a documentação de desenvolvedor GameKit, Creating activities for your game, Creating engaging challenges from leaderboards, Create games for Apple platforms, Game Porting Toolkit, Adding an access point to your game, Rewarding players with achievements, Finding multiple players for a game.

---

<!-- visual:game-center -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações vistas (img 0490 a 0512), todos os códigos conferidos; sem vídeo.
- O símbolo de abertura são três anéis azul escuro entrelaçados, sem preenchimento, sobre cartão azul com grade retangular e circular de construção (img 0490); todas as telas de exemplo usam o mesmo jogo fictício de tema marítimo, com paleta azul escura constante no Game Overlay (img 0491 a 0509).
- O access point é um botão circular translúcido com símbolo de foguete na diagonal, sozinho no canto superior esquerdo da tela de título, sem nenhum outro controle agrupado perto dele e com a arte do jogo livre ao redor (img 0491).
- O Game Overlay muda de apresentação conforme o aparelho sem mudar o conteúdo: no iPhone cobre a tela inteira, com fundo escurecido e cartão translúcido no topo sobre a lista de atalhos; no iPad a mesma lista vira uma faixa vertical estreita na borda trailing e a arte continua visível na maior parte da tela (img 0492).
- Na visão geral de conquistas, um contador grande de concluídas com avatares de amigos abre a tela; as conquistas obtidas são círculos com imagem colorida, data em arco ao redor e texto legível, e as bloqueadas são círculos cinza uniformes com cadeado, sem título visível (img 0493). O detalhe acrescenta a lista de jogadores com tempo relativo e a porcentagem global de quem obteve (img 0494).
- A anatomia do cartão de conquista é anotada com chamadas: imagem circular centralizada no topo, título grande em duas linhas, descrição menor abaixo e avatares de jogadores na base (img 0495).
- A máscara circular é desenhada sobre o quadrado da imagem: em iOS, iPadOS, macOS e visionOS o círculo de 512 pt toca as quatro bordas do quadrado de 512x512 pt (img 0496); no tvOS o círculo de 200 pt fica centralizado num quadrado de 320x320 pt, deixando margem quadrada larga fora da máscara (img 0497).
- Os diagramas de asset seguem uma linguagem comum: um quadrado ou retângulo em cinza, lilás ou rosa para o tamanho da imagem, uma segunda forma em rosa, roxo ou tracejado marcando a máscara, o corte ou os tamanhos de foco, e valores em pt anotados (img 0496, 0497, 0500, 0501, 0505, 0511).
- A arte de leaderboard é um quadrado de 512x512 pt do qual só uma faixa horizontal central de 512x312 pt é mantida, com sobra acima e abaixo (img 0500); no tvOS três retângulos concêntricos e centralizados mostram a imagem de 659x371 pt, o tamanho em foco de 618x348 pt e o tamanho fora de foco de 548x309 pt, os dois últimos tracejados (img 0501).
- Leaderboards seguem o padrão de visão geral mais detalhe: contador de leaderboards com avatares de amigos e seções de classificados e atividade de amigos, com cartões de mapa que trazem uma fração numérica e avatares (img 0498); no detalhe, botões de jogar e desafiar lado a lado, abas de amigos e global, ranking numerado com pontuação e, no fim, convite a mais amigos (img 0499).
- Challenges e atividades multiplayer compartilham o mesmo cartão anotado: arte de fundo, título, número de jogadores e um degradê escuro fornecido pelo sistema na base para dar legibilidade ao texto sobre a arte (img 0504, 0510); as telas de desafio mostram convites com botão de aceitar, posição destacada como "3RD" e tempo restante com botões de jogar e adicionar jogadores (img 0502, 0503).
- A arte de challenge e a de atividade multiplayer usam o mesmo diagrama: retângulo de 1920 por 1080 pt com área de corte central rotulada 1465x1080 pt, que preserva a altura total e descarta margens lilás estreitas nas laterais (img 0505, 0511); a imagem opcional do topo do dashboard no tvOS é só um retângulo lilás de 600x180 pt com o rótulo no centro, sem área de corte (img 0512).
- No multiplayer, a visão geral lista cartões de nível com mapa, título e faixa de jogadores (img 0506); o detalhe traz código de grupo, compartilhamento de link, busca de contatos com status e caixa de seleção à direita, fechando com o botão de entrar (img 0507); a UI própria do jogo abre um modal com criar código, campo de oito dígitos em dois grupos de quatro e botão de entrar, sobre a mesma tela de nível que aparece inteira, com partida aleatória e convite a amigos, quando o modal sai (img 0508, 0509).
Divergências registradas: em img 0507 as notas apontam que a descrição oficial "in-game UI starting a multiplayer activity" corresponde melhor à img 0509, embora o conteúdo de 0507 seja coerente com a seção de convite.
<!-- /visual:game-center -->

## Generative AI (slug: generative-ai)

### O que governa
Princípios de design para incorporar inteligência artificial generativa a apps e jogos: responsabilidade, transparência, privacidade, escolha de modelo/dataset, tratamento de inputs e outputs, e melhoria contínua.

### Por que
O princípio-chave, definido logo no início, é "Responsible AI": design e desenvolvimento intencional que considera os impactos diretos e indiretos sobre pessoas, sistemas e sociedade, porque IA generativa é imprevisível por natureza (pequenas mudanças no input, ou até o mesmo input repetido, produzem resultados muito diferentes, ao contrário da programação clássica). Isso justifica quase todas as regras subsequentes: manter as pessoas no controle (permitir descartar, reverter, refazer) decorre da ideia de que a IA manipula e cria conteúdo, mas a agência decisória continua sendo humana. A insistência em transparência (nunca enganar alguém fazendo-o pensar que interage com um humano) e em privacidade (processar localmente quando possível, pedir permissão antes de usar dados pessoais) reflete que dados sensíveis frequentemente alimentam ou são processados por esses modelos. A regra sobre viés e inclusão nasce do fato de que modelos aprendem de dados e tendem a favorecer a informação mais comum, o que pode reproduzir estereótipos prejudiciais se não houver correção deliberada. Já as regras sobre alucinação (comunicar que o conteúdo pode conter erros, evitar pedir informação factual sem confiança de que o modelo tem acesso a dados verificados) derivam do reconhecimento de que modelos generativos "sabem" produzir conteúdo plausível, mas não necessariamente verdadeiro.

### Faça e evite
Boas práticas gerais
- Desenhe a experiência de forma responsável, considerando impactos diretos e indiretos sobre pessoas, sistemas e sociedade.
- Mantenha as pessoas no controle: honre pedidos dentro do escopo, trate conteúdo sensível com cuidado, permita descartar conteúdo indesejado, reverter ou refazer transformações; identifique claramente quando e onde IA é usada.
- Garanta experiência inclusiva: peça às pessoas que forneçam a informação necessária em vez de inferir características pessoais ou culturais; busque clareza antes de assumir algo que possa levar a estereótipos comuns (identidade de gênero, tipos de relacionamento); teste com conjunto diverso de pessoas.
- Ofereça recursos generativos apenas quando trouxerem valor claro e específico (economia de tempo, comunicação melhor, criatividade aprimorada), não em toda situação.
- Garanta boa experiência mesmo quando o recurso generativo não estiver disponível ou a pessoa optar por não usá-lo; considere oferecer um fallback não baseado em IA.

Transparência
- Comunique onde o app usa IA, para que a pessoa escolha conscientemente usar o recurso; nunca engane alguém fazendo-o pensar que interage com ou vê conteúdo de autoria humana quando na verdade é IA; alinhe a divulgação a regulamentações locais.
- Defina expectativas claras sobre o que o recurso pode e não pode fazer, por exemplo com um breve tutorial ou sugestões curadas em recursos abertos como busca ou geração por prompt; se houver limitações conhecidas, avise antecipadamente e explique por que resultados inferiores ocorrem.

Privacidade
- Escolha o tipo de modelo adequado: modelos on-device mantêm a informação no dispositivo, respondem rápido e funcionam offline; modelos baseados em servidor valem a pena quando o recurso exige mais poder de processamento ou contexto maior; sempre pese privacidade junto com capacidade e desempenho.
- Em processamento baseado em servidor, processe o máximo possível localmente, minimize o que é compartilhado, seja transparente sobre o que é enviado e como pode ser armazenado ou usado para treinamento.
- Peça permissão antes de usar informação pessoal e dados de uso; use o mínimo necessário; ofereça forma clara de optar por não usar; peça permissão explícita se dados sensíveis forem usados para melhoria de modelo ou armazenamento; apps para crianças têm regras e leis mais rígidas.
- Divulgue claramente como o app e seu modelo usam e armazenam informação pessoal; explique benefícios de forma concisa, específica e fácil de entender; esclareça se o modelo usa informação pessoal para treinamento.

Modelos e datasets
- Avalie cuidadosamente as capacidades do modelo, já que alguns têm conhecimento geral e outros são treinados para tarefas específicas; tenha contato prático com modelos e dados o mais cedo possível; considere que alguns tipos de modelo podem estar indisponíveis conforme compatibilidade de dispositivo, acesso a rede e nível de bateria.
- Seja intencional ao escolher ou criar um dataset: escolha dados que incluam representação diversa; entenda a origem e a forma de coleta dos dados; garanta licenças relevantes para dados que não são de propriedade própria; ofereça escolhas apropriadas ao usar dados de pessoas; reserve tempo para teste e avaliação, já que datasets do mundo real costumam ser imperfeitos e podem propagar viés e desinformação.

Inputs
- Guie as pessoas sobre como usar o recurso generativo, por exemplo oferecendo exemplos de input predefinidos e diversos.
- Aumente a consciência sobre alucinações e minimize sua chance: alucinações ocorrem quando o modelo produz conteúdo plausível mas inventado; comunique claramente que conteúdo gerado por IA pode conter erros; evite pedir informação factual a menos que haja confiança de que o modelo tem acesso a dados verificados e atualizados; evite usar conteúdo gerado por IA em situações em que uma possível alucinação possa desinformar e causar dano.
- Considere consequências e peça permissão antes de executar tarefas irreversíveis ou potencialmente problemáticas; evite automatizar ações destrutivas (como deletar fotos) ou de difícil reversão (como fazer uma compra em nome da pessoa); geralmente peça confirmação antes de ações significativas; revise e siga políticas de uso específicas do modelo e políticas regulatórias de cada localidade.

Outputs
- Facilite refinar ou reverter resultados gerados, reconhecendo quando correções surtem efeito, por exemplo com controles como Edit, Undo, Retry ou Adjust próximos ao conteúdo gerado.
- Ajude as pessoas a melhorar pedidos quando bloqueados ou com resultados indesejados, minimizando saída bloqueada ou limitada ensinando como ter mais sucesso na próxima tentativa (exemplo citado: Image Playground responde "Unable to use that description" para conteúdo nocivo).
- Reduza resultados inesperados e nocivos com design cuidadoso e testes minuciosos, considerando cenários de uso indevido acidental e proposital, pedidos mal formulados, vagos ou ambíguos, tópicos pessoais, sensíveis ou controversos.
- Evite replicar conteúdo protegido por direitos autorais; reduza a chance construindo sobre modelos que já protegem contra isso e curando cuidadosamente os inputs; considere deixar a pessoa escolher entre prompts pré-aprovados ou instruir explicitamente o modelo a evitar imitar certo conteúdo ou estilo.
- Considere o tempo de processamento (latência) no design; modelos generativos costumam levar mais tempo que modelos não generativos (como rastreamento de posição corporal no ARKit e no framework Vision); projete uma experiência de carregamento ou gere em segundo plano enquanto a pessoa usa outra parte do app.
- Considere dar feedback específico e tranquilizador durante a geração, descrevendo o que está de fato acontecendo (por exemplo, "Finding substitutions for ingredients" em vez de "Processing…"); se algo der errado, descreva em linguagem simples e ofereça um próximo passo claro.
- Considere oferecer versões alternativas de resultados, dando à pessoa maior sensação de controle (exemplo citado: Image Playground gera múltiplas imagens representando uma pessoa, permitindo escolher a preferida).

Melhoria contínua
- Considere formas de melhorar o modelo ao longo do tempo, adaptando-o ao comportamento das pessoas, respondendo a feedback e incorporando novos dados; algumas melhorias (como atualizar lista de palavras bloqueadas) podem ser feitas com frequência e independentemente do ciclo de desenvolvimento do app; planeje fine-tuning, reteste e engenharia de prompt ao atualizar para modelo base mais capaz; se treinar modelo próprio, retreine com dados adicionais.
- Permita que as pessoas compartilhem feedback sobre os resultados, o que ajuda a identificar problemas inesperados; sempre torne o feedback voluntário; posicione o mecanismo de feedback em local claro que não interrompa a experiência; considere um jeito rápido de dar feedback positivo/negativo (como polegar para cima/baixo) e também uma forma de compartilhar feedback detalhado.
- Projete recursos flexíveis e adaptáveis, já que IA generativa é tecnologia em rápida evolução; considere separar o modelo da experiência do usuário para poder trocar de modelo ao longo do tempo mantendo a mesma experiência.

### Especificações exatas
Nenhum número, medida, duração ou valor padrão presente no texto (o artigo é inteiramente qualitativo/estratégico, sem especificações de dimensão, contraste ou duração).

### Diferenças por plataforma
Sem considerações adicionais para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

### Ligações com outros artigos
Cita Inclusion and Accessibility, Requesting permission, Loading, Multiple options, Explicit feedback, Implicit feedback, e a documentação de desenvolvedor Apple Intelligence and machine learning, Foundation Models, Core AI, além da referência "Acceptable Use Requirements for the Foundation Models Framework".

---

<!-- visual:generative-ai -->
### O que as ilustrações mostram
Base: 1 folha de ilustração vista (img 0527), código conferido; sem vídeo.
- O símbolo de abertura é um lápis na diagonal em azul escuro sólido, cercado por três estrelas de quatro pontas de tamanhos diferentes, distribuídas de forma assimétrica ao redor da ponta e do corpo (img 0527).
- O cartão tem degradê de azul violeta à esquerda para azul céu à direita, com grade retangular e circular de construção sobreposta, o mesmo padrão das ilustrações de abertura de páginas como Feedback, File management e Focus and selection (img 0527).
- O brilho ligado à IA generativa aparece repetido em três escalas, e não como um único ícone fixo; fora esse esboço, a página não ilustra tela, controle, estado de carregamento ou fluxo de geração (img 0527).
<!-- /visual:generative-ai -->

## O que este grupo revela sobre o jeito Apple

1. Reconhecimento de marca é tratado como ativo protegido em nível de pixel: AirPlay, Apple Pay e App Clip Codes compartilham a mesma estrutura de regra ("nunca altere a arte fornecida", "não gire, não dê glow, não mude proporção", "mantenha espaço livre mínimo") porque qualquer variação de terceiros dilui a confiança que o usuário deposita no símbolo (slugs: airplay, apple-pay, app-clips).

2. A Apple prefere sistematicamente fornecer o componente pronto (media player, botão de pagamento, coaching view, achievement card) e trata a customização como exceção a ser justificada, nunca como ponto de partida (slugs: airplay, apple-pay, augmented-reality, game-center).

3. Terminologia é normatizada com rigor quase legal: cada tecnologia tem uma lista explícita de termos corretos e incorretos (AirPlay como substantivo nunca verbo, "Game Center" nunca "GameKit", "Achievements" nunca "Trophies"), revelando que a Apple entende linguagem inconsistente como risco à experiência unificada entre apps (slugs: airplay, apple-pay, game-center).

4. Privacidade funciona como restrição de arquitetura, não como aviso legal adicional: App Clips apagam dados entre lançamentos, CareKit centraliza tudo nas configurações do sistema, Generative AI exige processamento local quando possível e permissão explícita antes de usar dados sensíveis (slugs: app-clips, carekit, generative-ai).

5. Contextos de atenção dividida (dirigir, realidade aumentada) geram as regras mais protetoras de segurança física e cognitiva do grupo: CarPlay proíbe qualquer dependência do iPhone destravado ou acessível, e Augmented Reality pede introdução gradual de movimento e atenção ao conforto e segurança da pessoa (slugs: carplay, augmented-reality).

6. A ilusão ou a credibilidade de uma experiência tem parâmetros técnicos exatos quando a Apple os define: 60 atualizações de cena por segundo em AR, ratio de leitura de 20:1 (ideal 10:1) em App Clip Codes, delta de cor CIELab de 2,5 na impressão. Quando a régua existe, ela é dada em número, não em adjetivo (slugs: augmented-reality, app-clips).

7. Onde a tecnologia lida com dinheiro ou saúde (Apple Pay, CareKit), a documentação é a mais longa e prescritiva do grupo, com tabelas de mensagens de erro, estados obrigatórios e fluxos de exceção detalhados, refletindo que o custo de um erro de design nesses domínios é mais alto do que em, por exemplo, AirPlay ou CarPlay (slugs: apple-pay, carekit).

8. A Apple repetidamente pede um "fallback" ou plano B quando a tecnologia em questão pode falhar ou estar indisponível: App Clip com app completo, Generative AI com caminho não-IA, AR com posicionamento reajustado sutilmente, Game Center com o jogo funcionando mesmo sem conta conectada (slugs: app-clips, generative-ai, augmented-reality, game-center).

9. Todas as sete tecnologias específicas de plataforma (airplay, always-on, app-clips, apple-pay, carplay, carekit, game-center) têm uma seção "Platform considerations" padronizada que declara explicitamente onde o recurso não é suportado, revelando uma disciplina editorial da HIG de nunca deixar implícita a abrangência de uma tecnologia entre iOS, iPadOS, macOS, tvOS, visionOS e watchOS.

10. Em domínios recentes e ainda instáveis do ecossistema (generative-ai é o mais novo do grupo, com "New page" datada de junho de 2025), a Apple escreve princípios e posturas éticas em vez de especificações numéricas, ao contrário de tecnologias maduras como Game Center e Apple Pay, que já acumulam tabelas de dimensões exatas (slugs: generative-ai, game-center, apple-pay).

## Evidência de leitura

| Arquivo | Linhas lidas | Lido até o fim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/airplay.md | 77 (arquivo com 77 linhas nominais, última linha de conteúdo é 78 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/always-on.md | 35 (última linha de conteúdo é 36 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/app-clips.md | 202 (última linha de conteúdo é 203 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/apple-pay.md | 242 (última linha de conteúdo é 243 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/augmented-reality.md | 134 (arquivo termina na linha 135 do Read, sem seção de change log) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/carekit.md | 127 (última linha de conteúdo é 128 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/carplay.md | 73 (última linha de conteúdo é 74 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/game-center.md | 177 (última linha de conteúdo é 178 no Read) | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/generative-ai.md | 71 (última linha de conteúdo é 72 no Read) | sim |

Todos os 9 arquivos do grupo foram lidos integralmente em uma única chamada Read cada, sem truncamento reportado pela ferramenta (nenhum aviso de limite atingido apareceu em nenhum dos retornos). Nenhum artigo do grupo é apenas índice de coleção; todos têm texto próprio completo.
