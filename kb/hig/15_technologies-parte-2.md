# Technologies (parte 2)

## HealthKit (slug: healthkit)

O que governa: como um app pede acesso, exibe e usa dados de saúde e fitness armazenados no HealthKit, incluindo o uso do elemento Activity ring e do ícone Apple Health.

Por que: a Apple trata dados de saúde como categoria sensível que exige confiança contínua. O raciocínio central é que a permissão não é um evento único (o app precisa pedir de novo a cada vez que precisa de acesso, porque a pessoa pode ter revogado), e que a experiência de privacidade deve ser previsível e centralizada nas Configurações do sistema, nunca duplicada dentro do app. Da mesma forma, Activity rings e o ícone Apple Health são elementos de confiança visual: como as pessoas já reconhecem seu significado exato pelo uso no app Activity e no Health, qualquer alteração visual (cor, forma, escala) quebra esse reconhecimento e pode até induzir a erro sobre o que está sendo medido.

Faça e evite:
- Só peça acesso a dados de saúde se o app realmente oferecer funcionalidade de saúde e fitness.
- Peça acesso somente quando o contexto tornar a necessidade óbvia (por exemplo, quando a pessoa loga o peso), não logo após o app abrir.
- Escreva frases curtas explicando por que precisa do dado na tela padrão de permissão; não replique essa tela com uma versão customizada.
- Gerencie o compartilhamento de dados de saúde só pelas configurações de privacidade do sistema; não crie telas adicionais no app que afetem esse fluxo.
- Forneça uma política de privacidade com URL clara no processo de submissão à App Store.
- Use Activity rings apenas para mostrar progresso de Move, Exercise e Stand; nunca para outro tipo de dado.
- Use Activity rings só para representar o progresso de uma pessoa por vez; nunca de várias pessoas ao mesmo tempo, e deixe claro de quem é o progresso (rótulo, foto ou avatar).
- Não use Activity rings como ornamento nem como parte de branding ou ícone do app.
- Mantenha cores e aparência do Activity ring e do fundo sempre iguais; nunca aplique filtros, mude cores ou altere a opacidade. Desenhe a interface ao redor para se encaixar, por exemplo envolvendo os anéis em um círculo.
- Mantenha uma margem externa mínima do Activity ring igual à distância entre os anéis; nada pode cortar, obstruir ou invadir essa margem.
- Para exibir o Activity ring dentro de um círculo, ajuste o raio da borda da view em vez de aplicar uma máscara circular.
- Diferencie visualmente outros elementos em forma de anel do Activity ring, usando padding, linhas, rótulos, cor ou escala.
- Forneça informação específica do app nas notificações de Activity, mas nunca repita a mesma informação do sistema nem mostre um Activity ring dentro de notificações.
- Use apenas o ícone Apple Health fornecido pela Apple, baixado dos Apple Design Resources; nunca crie versão própria.
- Exiba o nome "Apple Health" próximo ao ícone.
- Não use o ícone Apple Health menor que outros ícones de apps de saúde quando exibidos juntos.
- Não use o ícone Apple Health como botão; ele só indica compatibilidade.
- Não altere a aparência do ícone (sem máscara circular, bordas, overlays de cor, gradientes, sombras).
- Mantenha espaço livre mínimo ao redor do ícone Apple Health.
- Não use o ícone dentro de texto corrido nem como substituto das palavras Health, Apple Health ou HealthKit.
- Não exiba imagens ou capturas de tela do app Health, pois são protegidas por copyright.
- Chame o app de "Apple Health" ou "the Apple Health app" no texto; nunca use o termo "HealthKit" voltado ao usuário (é termo de desenvolvedor).
- Use a capitalização correta: "Apple Health" com A e H maiúsculos, resto minúsculo; versão toda em maiúsculas só se o layout exigir esse estilo tipográfico.
- Use a tradução fornecida pelo sistema para o termo "Health" para evitar confusão.

Especificações exatas: a margem livre mínima ao redor do ícone Apple Health é de 1/10 da altura do ícone. Não há outros valores numéricos no texto.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS ou watchOS. Não suportado em macOS, tvOS ou visionOS.

Ligações com outros artigos: "Works with Apple Health", "Activity rings", "Apple Design Resources", "Protecting user privacy" (documentação de desenvolvedor do HealthKit).

<!-- visual:healthkit -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações vistas (img 0538 a 0542), todos os códigos conferidos; sem vídeo.
- O símbolo de abertura é um losango facetado em azul escuro, com faixas paralelas empilhadas como camadas e um coração pequeno encaixado na quina superior, sobre degradê azul e grade de linhas retas e círculos concêntricos tracejados (img 0538).
- No resumo do app Saúde, os dados vêm em cartões brancos empilhados na vertical sob o cabeçalho de favoritos, todos com a mesma hierarquia: rótulo da métrica pequeno com ícone colorido em cima, valor numérico grande em negrito com a unidade pequena ao lado e o horário do registro ainda menor e mais claro no canto oposto (img 0539).
- O cartão de atividade traz as submétricas de mover, exercitar e ficar em pé com um anel colorido em miniatura à direita, e a tela fecha com barra de abas de três ícones, a selecionada em azul (img 0539).
- A folha modal de acesso ao Health tem barra de título com a recusa em texto à esquerda e a permissão em azul à direita, ícone de coração em cartão branco, título, parágrafo curto e um botão de texto para desligar todas as categorias (img 0540).
- Na mesma folha, escrita e leitura ficam em seções separadas com rótulo cinza em caixa alta; cada linha de categoria tem ícone colorido, nome e toggle verde à direita, e a explicação do app aparece logo abaixo em texto cinza pequeno, recuada sob o rótulo (img 0540).
- O histórico usa o Activity ring em miniatura como unidade de calendário: num modal de fundo preto, com cancelar à esquerda e o mês centralizado, cada dia é um conjunto de três anéis concêntricos vermelho, verde e azul, com anéis incompletos em alguns dias e dias sem dado em cinza apagado (img 0541).
- Na tela de onboarding que integra com o Apple Health, o ícone oficial (coração vermelho em quadrado branco arredondado) fica pequeno e isolado no topo à esquerda, separado das ações; seguem título branco grande em negrito, corpo menor e mais claro, pontos de página, um botão pílula branco preenchido para sincronizar e, abaixo, a opção de pular como texto simples sem fundo, sobre fundo verde ilustrado com traços de frutas e vegetais (img 0542).
<!-- /visual:healthkit -->

## HomeKit (slug: homekit)

O que governa: como um app iOS, tvOS ou watchOS pode integrar com o HomeKit (e por extensão com o app Home) para configurar, nomear, organizar e controlar acessórios domésticos conectados, incluindo o uso correto da terminologia, do fluxo de setup, das interações por Siri e dos ícones HomeKit.

Por que: o HomeKit define um modelo hierárquico de objetos (casa, cômodo, acessório, serviço, característica, cena, automação, zona) e um vocabulário específico para que Siri e o app Home possam entender comandos de voz em linguagem natural de forma confiável em qualquer app. O raciocínio da Apple é que, ao reforçar essa mesma terminologia e hierarquia em apps de terceiros, a experiência de automação residencial fica previsível e composicional: uma pessoa pode dizer "desligue as luzes de cima" e o sistema entende isso independentemente de qual app configurou o acessório. Também há uma preocupação explícita com não duplicar nem fragmentar as configurações do HomeKit: o banco de dados de nomes e organização deve ter uma única fonte de verdade (a que a pessoa definiu no app Home), evitando confusão e retrabalho.

Faça e evite:
- Reconheça o modelo hierárquico do HomeKit mesmo que o app não organize acessórios por cômodos e zonas na própria UI; isso ajuda pessoas a usar comandos de Siri corretamente.
- Facilite encontrar detalhes de HomeKit relacionados a um acessório (como zona ou cômodo); não esconda essas informações em telas de configuração difíceis de achar.
- Reconheça que uma pessoa pode ter mais de uma casa (home), mesmo que o app não suporte esse conceito visualmente.
- Não apresente configurações duplicadas de casa; sempre reflita as escolhas feitas no app Home, nunca peça para configurar tudo de novo.
- Use o fluxo de setup fornecido pelo sistema, que já cobre nomear, entrar em redes, parear com HomeKit, atribuir categorias e marcar favoritos em poucas etapas.
- Forneça uma "purpose string" explicando por que o app precisa acessar os dados da Home.
- Não exija criação de conta ou dados pessoais para o setup; deixe isso opcional e posterior ao setup do HomeKit.
- Honre as escolhas de setup da pessoa; não force a configuração de outras plataformas durante o fluxo HomeKit.
- Sempre comece pelo fluxo de setup do sistema antes de oferecer uma experiência de setup customizada, e só ofereça o customizado depois que a funcionalidade básica já estiver disponível.
- Sugira nomes de serviço adequados para comandos de Siri; nunca sugira nomes de empresa ou números de modelo como nome de serviço.
- Verifique se os nomes escolhidos pelas pessoas seguem as regras de nomenclatura do HomeKit: apenas caracteres alfanuméricos, espaço e apóstrofo; começar e terminar com caractere alfabético ou numérico; sem emojis.
- Ajude a evitar nomes de serviço que dupliquem informação de localização (como "kitchen light" para uma luz na cozinha), pois isso pode gerar resultados imprevisíveis em comandos de voz.
- Apresente exemplos de comandos de voz durante o setup, usando o nome de serviço escolhido.
- Depois do setup, ensine comandos mais complexos de Siri em pontos úteis do app.
- Ofereça atalhos (shortcuts) apenas para funcionalidade específica do acessório que o HomeKit não suporta; nunca duplique funcionalidade que o HomeKit já oferece por linguagem natural.
- Se o app suporta HomeKit e shortcuts, deixe claro a diferença entre os dois tipos de controle por voz.
- Recomende a criação de zonas e grupos de serviço (service groups) quando fizer sentido para o acessório.
- Seja claro sobre o que é possível fazer no app versus no app Home; ajude a pessoa a entender quando abrir o Home para completar uma cena.
- Defira ao HomeKit quando o banco de dados do app divergir do banco HomeKit; reflita automaticamente mudanças feitas no app Home ou em outros apps HomeKit de terceiros.
- Peça permissão antes de atualizar o banco de dados HomeKit quando a pessoa fizer mudanças no app; nunca sobrescreva configurações do HomeKit sem direção explícita.
- Não bloqueie imagens de câmera com outro conteúdo; é aceitável complementar com recursos úteis, mas evite cobrir partes da imagem.
- Mostre um botão de microfone apenas se a câmera suportar áudio bidirecional.
- Use apenas os ícones HomeKit e Apple Home fornecidos pela Apple; nunca crie versão própria.
- Escolha a variante do ícone HomeKit (preto, branco ou de cor customizada) de acordo com o fundo e o estilo dos demais ícones de tecnologia usados.
- Posicione o ícone HomeKit de forma consistente com outros ícones de tecnologia (mesmo tratamento de forma, como círculos).
- Use o ícone HomeKit de forma não interativa; não o use dentro de botões customizados nem combine com a palavra "HomeKit" em elementos interativos.
- Não use o ícone HomeKit dentro de texto corrido nem como substituto da palavra "HomeKit".
- Combine corretamente o ícone com o nome HomeKit (abaixo ou ao lado), usando a mesma fonte do restante do layout.
- Torne referências ao HomeKit ou Apple Home menos proeminentes que o nome ou identidade principal do próprio app.
- Siga as diretrizes de marcas registradas da Apple: use nomes de produto Apple apenas no singular, sem forma possessiva; não traduza "Apple", "Apple Home", "HomeKit" ou outras marcas; não use descritores de categoria (diga "iPad", não "tablet"); não indique patrocínio, parceria ou endosso da Apple; atribua créditos legais corretos onde aplicável; refira-se a dispositivos e sistemas operacionais Apple só em especificações técnicas ou de compatibilidade.
- Use capitalização correta: "HomeKit" é uma palavra, H e K maiúsculos; "Apple Home" são duas palavras, A e H maiúsculos.
- Não use "HomeKit" como adjetivo descritor (evite "HomeKit lightbulbs"); prefira termos como "works with", "use", "supports" ou "compatible".
- Não sugira que o HomeKit está executando uma ação por conta própria (evite "HomeKit unlocked the back door"; prefira "Back door is unlocked with HomeKit").
- Pode usar "Apple" junto com "HomeKit" (por exemplo "Compatible with Apple HomeKit").
- Use o nome do app "Apple Home" completo na primeira menção em um texto corrido; menções seguintes podem usar só "the Home app".

Especificações exatas: o texto não traz medidas numéricas de pixels, pontos, durações ou proporções para este artigo.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS (a integração é descrita como disponível em iOS, tvOS e watchOS, com o app Home residindo em iOS).

Ligações com outros artigos: "Resources" (recursos de design), "Guidelines for Using Apple Trademarks".

<!-- visual:homekit -->
### O que as ilustrações mostram
Base: 4 folhas de ilustrações vistas (img 0544 a 0559), todos os códigos conferidos; sem vídeo.
- O símbolo de abertura é uma casa em traço azul escuro grosso com três níveis aninhados (contorno externo, casa menor dentro e uma porta no centro) e chaminé à direita, sobre degradê azul com a grade de linhas e círculos tracejados de guia (img 0544).
- Certo e errado são marcados por dois selos mínimos e sem texto: círculo verde preenchido com check branco e círculo cinza preenchido com X branco (img 0545, 0546).
- O ícone HomeKit final aparece limpo, em traço preto fino sobre branco, sem cartão nem grade (img 0547); o ícone do app Apple Home usa a mesma casa de três níveis, porém preenchida, num quadrado arredondado em degradê de laranja para amarelo (img 0548).
- As variantes do ícone mudam só a cor conforme o fundo e mantêm o desenho: contorno preto grosso sobre branco (img 0549), contorno branco sobre quadrado preto sólido de cantos arredondados que ocupa toda a moldura (img 0550) e contorno azul de cor customizada sobre branco (img 0551).
- Ao lado de outras tecnologias, o ícone recebe o mesmo tratamento dos vizinhos: num cartão branco com título de integração, três círculos cinza claro iguais, cada um com um ícone dentro e rótulo embaixo com o mesmo espaçamento, o primeiro com a casa do HomeKit e os outros com quadrados tracejados genéricos (img 0552).
- Os exemplos errados de uso interativo usam acabamento pesado de propósito: o ícone plano e fino dentro de um botão circular cromado, com degradê metálico e brilho especular no topo (img 0553), e um botão retangular grande de degradê metálico escuro com a palavra HomeKit em branco negrito, sem ícone (img 0554).
- A posição do ícone em texto corrido é testada no mesmo cartão pílula branco, mantido constante: ícone no início da linha, antes da frase (img 0555), no meio da frase entre duas palavras (img 0556) e no fim da linha no lugar da palavra HomeKit, que deixa de aparecer escrita (img 0557); em img 0555 o desenho traz um cadeado dentro da casa.
- Numa lista de configuração em cartão cinza claro, com título e linha divisória, cada linha tem ícone à esquerda, título, duas barras cinza simulando texto secundário e chevron à direita; a linha do HomeKit usa o ícone preenchido em preto com o nome escrito ao lado, no mesmo estilo tipográfico das linhas vizinhas (img 0558).
- Numa grade de apps dois por dois, o ícone colorido do Apple Home fica num quadrado branco arredondado com sombra e o nome centralizado embaixo, com a mesma tipografia dos três ícones genéricos tracejados da grade (img 0559).
<!-- /visual:homekit -->

## iCloud (slug: icloud)

O que governa: como um app deve se integrar ao iCloud para sincronizar documentos, dados de estado e conteúdo entre dispositivos sem exigir sincronização manual da pessoa.

Por que: o princípio central declarado no texto é transparência: as pessoas não precisam saber onde o conteúdo reside fisicamente, e devem sempre presumir que estão acessando a versão mais recente. Isso leva a uma postura de "menos decisões manuais", já que a maioria das pessoas não quer gerenciar o armazenamento de documentos individualmente, e o app deve automatizar o máximo possível das tarefas de gerenciamento de arquivo.

Faça e evite:
- Facilite o uso do app com iCloud automaticamente, já que a pessoa liga o iCloud nas Configurações e espera que os apps funcionem com ele sem configuração extra; se quiser oferecer escolha, mostre uma opção simples na primeira abertura entre usar iCloud para todos os dados ou não usar.
- Evite perguntar quais documentos manter no iCloud; a maioria espera que todo o conteúdo esteja disponível.
- Mantenha o conteúdo atualizado quando possível, equilibrando isso com armazenamento e banda do dispositivo; para documentos muito grandes, considere deixar a pessoa controlar quando baixar conteúdo atualizado, e indique quando existe uma versão mais recente disponível, com feedback sutil se o download demorar mais que alguns segundos.
- Respeite o espaço de armazenamento do iCloud, que é um recurso finito e pago; use-o para conteúdo que a pessoa cria e entende, evitando usá-lo para recursos do app ou conteúdo regenerável (os backups do iCloud incluem o conteúdo da pasta Documents de cada app, então seja seletivo sobre o que colocar lá).
- Garanta comportamento apropriado quando o iCloud estiver indisponível (iCloud desligado manualmente ou Modo Avião); não é necessário exibir um alerta, mas é útil avisar discretamente que as mudanças não estarão disponíveis em outros dispositivos até restaurar o acesso.
- Use o iCloud para guardar também configurações e estado do app, como a última página lida em um app de revista, desde que sejam ajustes que a pessoa queira aplicados em todos os dispositivos (nem todo ajuste se encaixa, por exemplo configurações mais úteis no trabalho do que em casa).
- Avise sobre as consequências de apagar um documento, já que a exclusão remove o documento do iCloud e de todos os outros dispositivos também; mostre um aviso e peça confirmação antes de excluir.
- Torne a resolução de conflitos rápida e fácil, tentando detectar e resolver conflitos de versão automaticamente; quando isso não for possível, mostre uma notificação discreta que facilite diferenciar e escolher entre as versões conflitantes, idealmente o mais cedo possível.
- Inclua conteúdo do iCloud nos resultados de busca, já que as pessoas esperam que seu conteúdo esteja universalmente disponível.
- Em jogos, considere salvar o progresso do jogador no iCloud, usando o framework GameSave, que sincroniza dados entre dispositivos e oferece alertas nativos para lidar com sincronização offline ou conflitos.

Especificações exatas: o texto não traz números, medidas ou proporções.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: nenhuma referência cruzada a outro artigo das HIG citada no texto (apenas documentação de desenvolvedor CloudKit e GameSave).

<!-- visual:icloud -->
### O que as ilustrações mostram
Base: 1 folha de ilustração vista (img 0560), código conferido; sem vídeo.
- O símbolo de abertura é uma nuvem em contorno azul escuro grosso e vazado, sem preenchimento, sobre fundo em degradê azul (img 0560).
- A grade de construção sobreposta combina linhas horizontais, verticais e diagonais com um círculo tracejado centralizado, tangente à base da nuvem, que parece ditar a curvatura do lobo maior à direita (img 0560).
- A página não ilustra tela de sincronização, conflito de versão, estado offline ou busca; o único material visual confirma o esboço do ícone tingido de azul descrito oficialmente (img 0560).
<!-- /visual:icloud -->

## ID Verifier (slug: id-verifier)

O que governa: como um app iPhone pode usar o ID Verifier para ler carteiras de identidade móveis (mobile IDs) compatíveis com ISO 18013-5 presencialmente, sem hardware externo, para verificação de identidade ou idade.

Por que: a Apple estrutura o ID Verifier em torno de minimização de dados e confiança: a pessoa verificada só apresenta o mínimo de dado necessário para provar idade ou identidade, sem entregar o cartão físico ou mostrar o próprio dispositivo, e a Apple fornece os componentes-chave de emissão, gestão e validação de certificados para garantir consistência e confiabilidade em toda a experiência. Isso justifica a divisão entre dois tipos de requisição (Display Only e Data Transfer): quando o app só precisa confirmar visualmente algo, os dados nem chegam a ser transmitidos ao app, preservando privacidade; só quando há exigência legal de verificação é que se justifica pedir (e armazenar) dados como endereço ou data de nascimento.

Faça e evite:
- Peça apenas o dado necessário para completar a verificação atual; por exemplo, para checar idade mínima, use uma requisição de limiar de idade em vez de pedir a idade exata ou a data de nascimento da pessoa.
- Se o app se qualifica para o Apple Business Register, registre-se para o ID Verifier, para que o nome oficial e o logo da organização apareçam na UI de verificação exibida no dispositivo do cliente.
- Forneça um botão que inicie o processo de verificação com um rótulo claro como "Verify Age" (para checagem simples de idade) ou "Verify Identity" (para requisição de identidade mais detalhada); evite incluir símbolos que sugiram um tipo específico de comunicação como NFC ou QR code, e nunca inclua o logo da Apple no rótulo do botão.
- Em uma requisição Display Only, ajude a pessoa que está usando o app a dar feedback sobre a confirmação visual que realiza, por exemplo com botões "Matches Person" e "Doesn't Match Person" para que o app receba um valor de aprovado ou rejeitado como parte da resposta.

Especificações exatas: o texto não traz números de pontos, pixels, durações ou proporções; a única referência técnica formal citada é a conformidade com o padrão ISO 18013-5.

Diferenças por plataforma: sem considerações adicionais para iOS. Não suportado em iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: "Apple Business Register", "IDs in Wallet", "Identity verification".

<!-- visual:id-verifier -->
### O que as ilustrações mostram
Base: 1 folha vista com 3 ilustrações (img 0625 a 0627), todos os códigos conferidos; o quarto quadrante da folha estava vazio, sem imagem nem código; sem vídeo.
- A ilustração de abertura é um cartão de identidade estilizado, retângulo arredondado com retrato genérico à esquerda e linhas horizontais de texto à direita, do qual saem ondas curvas crescentes no canto inferior direito, sugerindo leitura sem contato (img 0625).
- O desenho de abertura é construído sobre grade dupla, linhas retas pontilhadas e círculos concêntricos, com degradê de azul mais escuro para mais claro (img 0625).
- O botão de iniciar a verificação de idade é um retângulo de cantos arredondados em preto sólido, com rótulo branco centralizado, isolado sobre branco e sem ícone ou elemento adicional (img 0626).
- A versão para verificar identidade repete cor, altura e raio de canto e fica apenas mais larga para acomodar o rótulo maior, ou seja, a largura do botão acompanha o texto e as demais medidas ficam fixas entre as variações (img 0626, 0627).
<!-- /visual:id-verifier -->

## iMessage apps and stickers (slug: imessage-apps-and-stickers)

O que governa: como criar um app do iMessage (para compartilhar conteúdo, colaborar ou jogar dentro de uma conversa) e pacotes de figurinhas (stickers), incluindo especificações exatas de tamanho de ícones e figurinhas.

Por que: o raciocínio da Apple é que as pessoas estão em um fluxo conversacional quando abrem um app do iMessage, então a funcionalidade precisa ser compreendida e utilizável imediatamente, sem exigir uma curva de aprendizado; por isso a recomendação de manter uma experiência primária por app, em vez de acumular múltiplas funções que competem por atenção num contexto já rápido e informal da mensagem.

Faça e evite:
- Prefira oferecer uma experiência primária por app do iMessage; para múltiplos tipos de funcionalidade ou coleções de conteúdo distintas, considere criar um app separado para cada uma.
- Considere trazer conteúdo do app iOS/iPadOS principal para o app do iMessage, como uma lista de compras ou um roteiro de viagem, ou apoiar uma tarefa colaborativa simples.
- Apresente as funcionalidades essenciais na visão compacta (compact view), que aparece abaixo da transcrição de mensagens; reserve conteúdo e recursos adicionais para a visão expandida.
- Em geral, permita edição de texto apenas na visão expandida, já que a visão compacta ocupa aproximadamente o mesmo espaço do teclado; exiba o teclado na visão expandida para manter o conteúdo do app visível durante a edição.
- Crie figurinhas expressivas, inclusivas e versáteis, legíveis contra uma ampla variedade de fundos e quando rotacionadas ou escaladas; use transparência para ajudar a integrar visualmente a figurinha com texto, fotos e outras figurinhas.
- Forneça uma descrição alternativa localizada para cada figurinha, para que o VoiceOver possa falá-la.

Especificações exatas:
- Tamanhos de ícone do app iMessage/pacote de figurinhas (fornecidos com cantos quadrados; o sistema aplica máscara de cantos arredondados automaticamente):
  - Messages, notifications: 148x110 px em @2x (equivalente citado de 143x100, 120x90 em @2x / 180x135 em @3x, 64x48 em @2x / 96x72 em @3x, 54x40 em @2x / 81x60 em @3x, a tabela lista múltiplas linhas de uso sem rótulo individual claro além da primeira).
  - Settings: 58x58 px em @2x, 87x87 px em @3x.
  - App Store: 1024x1024 px em @2x e em @3x.
- Messages suporta três tamanhos de figurinha: small, regular e large; não misturar tamanhos dentro de um mesmo pacote.
- Dimensões de figurinha em @3x (o sistema gera @2x e @1x por downscaling em runtime):
  - Small: 300x300 px
  - Regular: 408x408 px
  - Large: 618x618 px
- Um arquivo de figurinha deve ter no máximo 500 KB.
- Formatos suportados e suas capacidades: PNG (transparência de 8 bits, sem animação), APNG (transparência de 8 bits, com animação), GIF (transparência de cor única, com animação), JPEG (sem transparência, sem animação).

Diferenças por plataforma: sem considerações adicionais para iOS ou iPadOS. Não suportado em macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: "iMessage Apps and Stickers" (link de recursos relacionados).

<!-- visual:imessage-apps-and-stickers -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (img 0634 a 0637), todos os códigos conferidos; sem vídeo.
- A ilustração de abertura é uma forma oval em azul mais escuro com o logotipo da App Store, a letra A desenhada como compasso, no centro, sobre degradê azul com grade de linhas pontilhadas em X e círculos concêntricos (img 0634).
- A figurinha é mostrada dentro da conversa real: barra de digitação do iMessage com botão de mais e microfone no topo e, embaixo, o painel de figurinhas com uma fileira de ícones de categoria sobre a grade (img 0635 a 0637).
- No tamanho pequeno a grade tem quatro figurinhas por fileira, com duas fileiras completas e uma terceira cortada na borda inferior da tela (img 0635).
- No tamanho regular os mesmos personagens ficam visivelmente maiores e a grade cai para três por fileira, com duas fileiras completas visíveis (img 0636).
- No tamanho grande a grade tem só duas figurinhas por fileira, com uma fileira completa e o início da seguinte cortado na borda inferior (img 0637).
- As três capturas mantêm idênticos a barra do iMessage, o botão de mais, o microfone e o painel de categorias, e variam o número de colunas, de quatro para três e para duas, conforme a figurinha cresce, dentro da mesma largura fixa de painel na parte de baixo da tela do iPhone (img 0635, 0636, 0637).
<!-- /visual:imessage-apps-and-stickers -->

## In-app purchase (slug: in-app-purchase)

O que governa: como projetar a experiência de compra dentro do app (in-app purchase) para bens virtuais (consumíveis, não consumíveis, assinaturas auto-renováveis e assinaturas não renováveis), incluindo suporte a Family Sharing, fluxo de reembolso, cadastro de assinatura e gerenciamento de assinatura.

Por que: a lógica central é diferenciar claramente in-app purchase de Apple Pay pelo tipo de bem vendido (virtual versus físico/serviço), e depois garantir que toda a jornada de compra seja íntegra e integrada visualmente ao app, sem parecer que a pessoa "saiu" do app para comprar. Há também uma ênfase forte em transparência de preço e termos (mostrar sempre o valor total de cobrança, explicar claramente como funciona um período de teste grátis) e em nunca dificultar o cancelamento, refletindo a preocupação da Apple com prevenção de compras acidentais e confiança de longo prazo do assinante.

Faça e evite:
- Use in-app purchase para bens virtuais (conteúdo premium, bens digitais, assinaturas); use Apple Pay para bens físicos, serviços (associações de clube, reservas de hotel, ingressos) e doações.
- Deixe a pessoa experimentar o app antes de comprar; considere suportar acesso gratuito limitado se oferecer assinaturas auto-renováveis.
- Projete uma experiência de compra integrada visualmente ao estilo do restante do app.
- Use nomes e descrições de produto simples e sucintos, que não truncem nem quebrem linha.
- Exiba o preço total de cobrança para cada compra dentro do app, independente do tipo.
- Exiba a loja apenas quando a pessoa puder efetivamente pagar (por exemplo, oculte ou explique quando houver restrições parentais).
- Use a folha de confirmação padrão do sistema ao iniciar uma compra; não modifique nem replique essa folha.
- Mencione o Family Sharing de forma proeminente onde as pessoas conhecem o conteúdo oferecido, incluindo o termo "Family" ou "Shareable" no nome do item quando aplicável.
- Ajude as pessoas a entender os benefícios e como participar do Family Sharing.
- Personalize as mensagens do app para fazer sentido tanto para quem comprou quanto para membros da família que recebem acesso compartilhado.
- Ofereça uma tela de ajuda customizada que as pessoas possam consultar antes de pedir reembolso, com um link para o fluxo de reembolso do sistema, respostas a perguntas frequentes e formas de contato.
- Use um título simples para a ação de reembolso, como "Refund" ou "Request a Refund"; o fluxo do sistema já deixa claro que o pedido é feito à Apple.
- Ajude a pessoa a encontrar a compra com problema, mostrando imagem, nome, descrição e data de compra de cada item recente.
- Considere oferecer soluções alternativas ao reembolso (por exemplo cumprimento imediato do item ou item de compensação), deixando sempre claro que ainda é possível pedir reembolso.
- Facilite pedir reembolso; evite exigir rolagem ou abertura de outra tela antes de revelar o botão de solicitação de reembolso.
- Evite caracterizar ou dar orientação sobre as políticas de reembolso da Apple; não especule se o cliente receberá o reembolso solicitado.
- Chame atenção para os benefícios da assinatura durante o onboarding, com uma chamada para ação forte e um resumo claro dos termos da assinatura.
- Ofereça uma variedade de opções de conteúdo, níveis de serviço e durações.
- Considere permitir teste gratuito do conteúdo antes de assinar (app freemium, paywall dosado ou teste grátis).
- Solicite assinatura em momentos relevantes, como quando a pessoa se aproxima do limite mensal de conteúdo gratuito.
- Incentive uma nova assinatura apenas quando a pessoa ainda não for assinante; se o mesmo serviço estiver disponível em vários apps ou no site, ofereça opção de login para evitar cobrança duplicada.
- Ofereça opções de assinatura claras e distinguíveis, com nomes curtos e autoexplicativos, especificando preço e duração de cada opção; se houver preço introdutório, liste claramente a duração da oferta e o preço padrão após o fim dela.
- Simplifique o cadastro inicial pedindo apenas as informações necessárias; adie pedidos de informação adicional para depois do cadastro.
- No app tvOS, ajude as pessoas a se cadastrarem ou autenticarem usando outro dispositivo, em vez de pedir digitação de informação na Apple TV.
- Na tela de cadastro do app, inclua: nome, duração e conteúdo/serviços de cada período de assinatura; valor de cobrança corretamente localizado por território e moeda; e uma forma de assinantes existentes entrarem ou restaurarem compras.
- Descreva claramente como funciona o período de teste gratuito, deixando explícito que ao final um pagamento será automaticamente iniciado para o próximo período de assinatura.
- Inclua uma oportunidade de assinatura nas configurações do app.
- Para códigos de oferta customizados (custom code), use apenas caracteres alfanuméricos ASCII; não use caracteres especiais, incluindo caracteres chineses e árabes.
- Explique aos usuários como resgatar um código customizado, já que ele não pode ser resgatado diretamente nas configurações da conta da App Store.
- Considere suportar resgate de oferta dentro do app usando as telas de resgate fornecidas pelo sistema; a única UI customizada necessária é a que inicia o fluxo do sistema.
- Forneça uma imagem promocional envolvente e informativa para o código de resgate; se não fornecer, as telas usam o ícone do app por padrão.
- Ajude a pessoa a se beneficiar do conteúdo desbloqueado assim que completar o fluxo de resgate, incluindo quem assina antes mesmo de abrir o app pela primeira vez.
- Forneça resumos das assinaturas da pessoa, incluindo a data de renovação próxima, idealmente perto da opção de gerenciamento de assinatura.
- Considere usar a UI de gerenciamento de assinatura fornecida pelo sistema (StoreKit) para uma experiência consistente sem sair do app.
- Considere formas de incentivar a pessoa a manter a assinatura ou reassinar depois, como uma oferta personalizada alternativa ao cancelamento ou uma pesquisa de saída.
- Sempre facilite o cancelamento de uma assinatura auto-renovável; se a ação de gerenciar assinatura estiver escondida ou difícil de reconhecer, os assinantes podem sentir que estão sendo desencorajados ou impedidos de cancelar.
- Considere criar uma experiência de marca contextual que complemente a UI de gerenciamento do sistema, como oferecer um nível premium popular ou sugestões personalizadas.

Especificações exatas: o texto traz exemplos de preços em contexto ilustrativo, sem serem regras normativas (por exemplo um exemplo de plano anual de US$ 29,99/ano com teste grátis de 1 semana e economia de 50% sobre o plano mensal de US$ 4,99/mês; outro exemplo de US$ 14,99/mês para "Intrepid Pro"; outro de US$ 9,99/mês para "Intrepid Pro with Ads"). Family Sharing permite compartilhar com até cinco membros adicionais da família. O texto não define nenhum valor de medida de interface (pt, px, ms) como regra obrigatória.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, macOS, tvOS ou visionOS.
watchOS: a tela de cadastro no app watchOS precisa exibir o mesmo conjunto de informações obrigatórias sobre as opções de assinatura que as demais versões do app. Deixe claras as diferenças entre as versões do app em diferentes dispositivos, sem sugerir que a experiência é idêntica. Considere usar uma folha modal (modal sheet) para apresentar todas as informações obrigatórias em uma única view, já que ela inclui um botão padrão de fechar. Torne as opções de assinatura fáceis de comparar em uma tela pequena, por exemplo exibindo cada opção em um botão separado (para início de cadastro com um toque) ou uma lista de opções seguida por um único botão cujo título atualiza para refletir a opção escolhida.

Ligações com outros artigos: "In-app purchase" e "Auto-renewable subscriptions" (marketing e negócios), "App Review Guidelines", "Onboarding" (para chamada de atenção durante onboarding).

<!-- visual:in-app-purchase -->
### O que as ilustrações mostram
Base: 6 folhas de ilustrações vistas (img 0644 a 0666), todos os códigos conferidos; sem vídeo.
- O símbolo de abertura é um ícone de app quadrado de cantos arredondados, em azul, com um sinal de mais grosso no centro, sobre grade pontilhada horizontal, vertical e diagonal com círculo concêntrico que marca o centro e os eixos de simetria (img 0644).
- A loja dentro do jogo, no iPad, fica sobre fundo verde oliva com mapa desenhado: duas fileiras temáticas de itens circulares com ilustração colorida, nome embaixo e preço numa cápsula cinza, com valores bem diferentes convivendo na mesma grade (img 0645).
- A ajuda antes do reembolso usa paleta azul marinho translúcida: uma lista de cinco opções numa única cápsula com divisórias finas e chevrons (img 0646); a tela de pedido de reembolso tem o botão de voltar rotulado com o nome da tela anterior e lista cada compra com miniatura, nome e data em azul (img 0647).
- A folha do sistema de reembolso mostra ícone, nome, preço e data do item e a conta Apple, uma lista simples de motivos só com divisórias, o escolhido marcado com check azul, um aviso de perda de acesso e o botão azul no rodapé (img 0648); a confirmação traz check azul grande centralizado, título, prazo de resposta por e-mail e botão de concluir azul (img 0649).
- O onboarding de assinatura coloca um cartão de benefício na metade inferior sobre foto temática escurecida, com pontos de paginação, um botão com o preço detalhado dentro dele e o link de entrar abaixo (img 0650); a mesma composição reaparece só com o botão realçado por contorno azul claro e o resto apagado (img 0653), e a oferta de reassinatura repete o padrão sobre fundo turquesa ilustrado, com botão branco em dois níveis de texto (img 0662).
- Na escolha de plano, dois cartões empilhados funcionam como opções de rádio: o anual selecionado com círculo vermelho preenchido e selo de economia, o mensal com círculo vazio; termos repetidos em texto de rodapé, botão vermelho de teste grátis e fechar no canto superior direito (img 0651).
- O limite de conteúdo gratuito é aplicado por sobreposição: o artigo continua atrás com opacidade reduzida e por cima ficam a mensagem de limite, um botão roxo em pílula para ver opções e o link para quem já assina (img 0652).
- Na tela de cadastro com dois planos, as duas opções pagas são botões verdes em pílula com nome e preço mensal, e o resgate de código fica abaixo como link de texto simples, sem forma de botão (img 0654); na seção de códigos a mesma tela realça esse link com uma cápsula preta sólida e esmaece os botões verdes (img 0656).
- Nas configurações, o bloco da assinatura reúne ícone, nome, plano, preço e próxima cobrança, e as ações de gerenciar, restaurar e resgatar ficam fora do bloco como links azuis empilhados sem ícone (img 0657); a tela de gerenciamento repete o bloco, lista as opções de duração com check na atual, põe o cancelamento como link vermelho centralizado com aviso de renovação em cinza (img 0660) e confirma o cancelamento num alerta central com dois botões lado a lado, o de confirmar em azul (img 0661).
- A tela de resgate de código aparece como wireframe dentro de moldura de iPhone, em cinza de placeholder sem cor de marca: área de ícone tracejada, título em negrito, campo de código vazio e link de termos no rodapé (img 0658); a variante de oferta nomeada, também em moldura de iPhone, troca o ícone por uma foto placeholder maior com ícone tracejado pequeno no canto inferior esquerdo e acrescenta preço em texto pequeno e botão azul sólido de resgate (img 0659).
- No Apple Watch o cadastro é uma coluna única: link de fechar no topo, título azul, descrição, botão azul de largura total e termos abaixo (img 0655); o par de textos compara uma descrição sem botão de assinatura, com o título cortado fora do quadro, que não separa o que roda no relógio (img 0663), com a reescrita de título verde que distingue o recurso do Watch dos mapas usados no iPhone e em outros aparelhos (img 0664).
- O preço no Watch é resolvido de dois jeitos: cada opção como seu próprio botão vermelho em pílula de largura total, com a economia em texto pequeno fora dos botões (img 0665), ou uma lista em cartão único com título cinza em caixa alta, a opção escolhida com check verde e um botão vermelho de largura total abaixo que mostra o plano selecionado (img 0666).
Divergências registradas: a legenda oficial da img 0654 fala em três imagens no topo, mas a tela mostra uma foto de floresta por vez com indicador de três pontos, como carrossel.
<!-- /visual:in-app-purchase -->

## Live Photos (slug: live-photos)

O que governa: como um app deve lidar, exibir, editar e compartilhar Live Photos, que capturam conteúdo de áudio e quadros extras antes e depois da foto.

Por que: o princípio orientador é a consistência: as pessoas precisam experimentar Live Photos da mesma forma visual e de interação em todos os apps, então o texto proíbe explicitamente desmontar a Live Photo em seus componentes (quadros separados, áudio isolado) e exige que qualquer edição aplicada afete o conteúdo inteiro, não apenas o quadro estático, preservando a expectativa de que "Live Photo" é sempre uma experiência coesa de movimento e som.

Faça e evite:
- Aplique ajustes ou efeitos a todos os quadros da Live Photo; se isso não for suportado, ofereça a opção de converter para foto estática.
- Mantenha o conteúdo da Live Photo intacto; não desmonte a Live Photo nem apresente seus quadros ou áudio separadamente.
- Implemente uma boa experiência de compartilhamento de foto: deixe a pessoa pré-visualizar o conteúdo completo da Live Photo antes de decidir compartilhar, e sempre ofereça a opção de compartilhar como foto tradicional.
- Indique claramente quando uma Live Photo está sendo baixada e quando está pronta para reprodução, com indicador de progresso durante o download.
- Em ambientes que não suportam Live Photos, exiba a foto como uma foto tradicional estática; não tente replicar a experiência de Live Photos.
- Torne as Live Photos facilmente distinguíveis de fotos estáticas, idealmente por um sutil efeito de movimento; como não existe efeito de movimento embutido fora do navegador em tela cheia do app Photos, é preciso desenhar e implementar efeitos de movimento customizados.
- Quando o movimento não for possível, mostre o selo (badge) fornecido pelo sistema, com ou sem texto; nunca inclua um botão de reprodução que possa ser interpretado como botão de vídeo.
- Mantenha o posicionamento do selo consistente, tipicamente em um canto da foto, sempre no mesmo local em todas as fotos.

Especificações exatas: o texto não traz números de medida, tamanho, duração ou proporção.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, macOS ou tvOS. Não suportado em watchOS.
visionOS: em visionOS, as pessoas podem visualizar uma Live Photo, mas não podem capturá-la.

Ligações com outros artigos: nenhuma referência cruzada explícita a outro artigo das HIG (apenas documentação de desenvolvedor PHLivePhoto e LivePhotosKit JS).

<!-- visual:live-photos -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (img 0728 a 0730), todos os códigos conferidos; sem vídeo.
- O símbolo de abertura é um círculo concêntrico duplo, anel grosso azul escuro com miolo vazado, rodeado por uma coroa de pontos, sobre grade tracejada horizontal, vertical e diagonal que passa pelo centro, com retângulo guia; o desenho se apoia em eixos de simetria radial (img 0728).
- O selo com texto é aplicado sobre uma foto real noturna de lago e montanhas: um crachá branco arredondado no canto superior esquerdo, com o ícone azul do Live Photo e a palavra LIVE em azul ao lado, o fundo branco semitransparente contrastando com a cena escura (img 0729).
- O selo sem texto usa a mesma foto e o mesmo canto, agora como um círculo branco pequeno só com o ícone; a única diferença para a imagem anterior é a ausência do rótulo, com ícone, tamanho e posição mantidos (img 0729, 0730).
- A página não ilustra efeito de movimento, progresso de download ou tela de compartilhamento; o material visual se limita ao ícone e às duas variantes do selo (img 0728 a 0730).
<!-- /visual:live-photos -->

## Mac Catalyst (slug: mac-catalyst)

O que governa: como transformar um app de iPad em um app de Mac usando Mac Catalyst, incluindo a escolha entre o idioma (idiom) iPad e o idioma Mac, e como adaptar navegação, entradas, ícones, layout e menus para a plataforma macOS.

Por que: o princípio central é que um bom app de iPad é uma boa base, mas não é suficiente: transformar em um app de Mac exige ir além de simplesmente exibir o layout do iPadOS dentro de uma janela do macOS. iPadOS e macOS definem padrões e convenções diferentes, enraizados em formas diferentes de as pessoas usarem seus dispositivos (toque versus teclado e mouse), então o texto orienta a auditar cada dimensão da experiência (navegação, entrada, ícones, layout, menus) e adaptá-la às convenções nativas do Mac em vez de portar diretamente.

Faça e evite:
- Avalie se o app é um bom candidato ao Mac Catalyst verificando se já suporta bem recursos-chave do iPad: drag and drop, navegação e atalhos de teclado, multitasking (Split View, Slide Over, Picture in Picture) e múltiplas janelas (múltiplas scenes no iPad).
- Reconheça que apps que dependem de recursos inexistentes no Mac (giroscópio, acelerômetro, câmera traseira, frameworks como HealthKit ou ARKit) ou cuja função primária é algo como marcação, escrita à mão ou navegação podem não ser adequados para o Mac.
- Ao criar o app com o idioma iPad ("Scale Interface to Match iPad"), saiba que texto e gráficos podem parecer menos detalhados, pois views e texto do iPadOS são escalados para baixo em macOS.
- Considere mudar para o idioma Mac quando o app já estiver funcionando bem no Mac com o idioma iPad; isso renderiza texto e artwork com mais detalhe, dá aparência mais nativa a alguns elementos e views, e pode melhorar performance e reduzir consumo de energia em apps gráficos intensivos.
- Beneficia-se mais do idioma Mac o app que exibe muito texto, artwork detalhado ou animações; mas essa escolha exige mais tempo atualizando o layout, texto e imagens do app Mac.
- Ao adotar o idioma Mac, audite completamente o layout do app e planeje mudanças; considere usar um catálogo de assets separado para o app Mac em vez de reaproveitar o catálogo do app iPad.
- Ajuste tamanhos de fonte conforme necessário; use estilos de texto (text styles) em vez de tamanhos de fonte fixos quando possível, pois com o idioma Mac o texto renderiza a 100% do tamanho configurado.
- Garanta que views e imagens fiquem boas na versão Mac, já que com o idioma Mac as views do iPadOS renderizam a 100% do tamanho, aparecendo mais detalhadas.
- Limite customizações de aparência às customizações padrão do macOS que sejam iguais ou similares às disponíveis no iPadOS; nem toda customização de controle do iPadOS está disponível para controles do macOS.
- Se o app iPad usa uma tab bar, considere usar uma split view com sidebar ou um controle segmentado no Mac, que são mais próximos das convenções de navegação do macOS.
- Prefira uma split view com sidebar a uma tab bar em geral; um controle segmentado funciona bem se o app usa uma hierarquia de navegação plana.
- Garanta que as pessoas mantenham acesso a itens importantes da tab bar na versão Mac, listando-os no menu View do macOS.
- Ofereça múltiplas formas de navegar entre páginas: botões Next e Previous além de gestos de deslizar, já que usuários de Mac (especialmente com dispositivo apontador ou apenas teclado) apreciam essa opção.
- Saiba que a maioria dos gestos do iPadOS converte automaticamente para interações de mouse e trackpad ao criar o app Mac (tap vira clique esquerdo ou direito; touch and hold vira clique e segurar; pan vira clique e arrastar; pinch e rotate se mantêm em trackpad).
- Crie uma versão macOS do ícone do app, que mostre o estilo de renderização realista que as pessoas esperam no macOS mantendo harmonia entre plataformas.
- Para aproveitar a tela mais larga do Mac: divida uma única coluna de conteúdo e ações em múltiplas colunas; use as size classes regular-width e regular-height, reorganizando elementos lado a lado ao redimensionar a janela; apresente UI de inspetor ao lado do conteúdo principal em vez de usar um popover.
- Considere mover controles da UI principal do app iPad para a toolbar do app Mac, listando os comandos associados nos menus da barra de menu.
- Adote um fluxo de cima para baixo (top-down); apps de Mac colocam as ações e conteúdo mais importantes perto do topo da janela.
- Realoque botões das bordas laterais e inferior da tela, já que no Mac essa consideração ergonômica não se aplica como no iPad.
- Para atalhos de teclado de comandos de menu, use UIKeyCommand.
- Saiba que botões pop-up ou pull-down que revelam um menu no app iPad automaticamente assumem aparência macOS no app Mac Catalyst.
- Para adicionar e remover menus customizados, use UIMenuBuilder e UICommand.
- Saiba que o sistema converte automaticamente os menus de contexto do app iPad em menus de contexto no app macOS; considere procurar lugares adicionais para suportar menus de contexto, já que usuários de Mac tendem a esperar que todo objeto no app ofereça um menu de contexto de ações relevantes (no Mac, esse menu às vezes é chamado de "contextual menu").

Especificações exatas: texto do iPadOS que usa o tamanho de fonte base de 17pt é escalado para baixo para 13pt no macOS quando se usa o idioma iPad (fator de escala de 77%). No idioma Mac, texto e views renderizam a 100% do tamanho configurado.

Diferenças por plataforma: sem considerações adicionais para iPadOS ou macOS. Não suportado em iOS, tvOS, visionOS ou watchOS. (Este artigo é inteiramente sobre a relação iPadOS/macOS via Mac Catalyst.)

Ligações com outros artigos: "Designing for macOS" (para entender as características que distinguem a experiência Mac).

<!-- visual:mac-catalyst -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista (img 0739 a 0741), todos os códigos conferidos; sem vídeo.
- A abertura sobrepõe literalmente duas molduras de aparelho em vez de um símbolo único: atrás, o contorno de um laptop com base horizontal e coluna vertical grossa à esquerda; na frente, um retângulo arredondado de tablet com um traço curto na base, com círculo guia concêntrico ao tablet e grade tracejada horizontal, vertical e diagonal (img 0739).
- O idioma iPad é representado pelo ícone pixelizado de um edifício com três arcos e colunas, em bege e cinza, ocupando toda a largura do quadro sem margem, com blocos de pixel grandes e grosseiros que indicam menos detalhe (img 0740).
- O idioma Mac usa o mesmo ícone centralizado com margem branca visível acima e abaixo, ocupando área menor, com blocos de pixel proporcionalmente menores e mais numerosos e impressão de mais nitidez (img 0741).
- O par de comparação não traz grade, anotação numérica nem texto sobre as imagens; a diferença entre os idiomas é mostrada só pelo enquadramento do mesmo desenho, cheio de quadro ou com margem, e pelo tamanho relativo dos blocos de pixel (img 0740, 0741).
<!-- /visual:mac-catalyst -->

## Machine learning (slug: machine-learning)

O que governa: como planejar, desenhar e comunicar recursos de app ou jogo que usam machine learning, incluindo como classificar o papel do machine learning no produto, como coletar e usar feedback (explícito e implícito), como conduzir calibração, como lidar com erros, correções, múltiplas opções, confiança (confidence), atribuição (attribution) e limitações.

Por que: o raciocínio central é que um app de machine learning não pode ser desenhado como reações fixas a um conjunto estático de cenários, porque seu comportamento depende dos dados recebidos; por isso, o design consiste em ensinar o app a interpretar dados e reagir, e a experiência de UI precisa ser construída em torno de eixos que definem o quanto as pessoas toleram erro e falta de precisão: se o recurso é crítico ou complementar, se lida com dado privado ou público, se é proativo ou reativo, se é visível ou invisível, se melhora de forma dinâmica ou estática. Cada eixo muda a expectativa de confiabilidade e o nível de tolerância a erro que as pessoas terão, o que por sua vez determina o quanto investir em feedback, calibração, correções e comunicação de confiança.

Faça e evite (planejamento e papel do machine learning):
- Ao desenhar os modelos, tenha em mente a experiência pretendida do app; esteja preparado para mudar a forma como usa dados e métricas se a experiência do app precisar mudar, já que ajustar o comportamento de modelos pode levar muito tempo.
- Defina o papel do machine learning no app (crítico ou complementar) para descobrir onde ele pode afetar a experiência.
- Quanto mais central o recurso for ao propósito do app, maior a expectativa de resultados precisos e confiáveis; para recursos secundários, as pessoas tendem a ser mais tolerantes com imprecisões.
- Quanto mais sensível o dado usado, mais sérias as consequências de um resultado impreciso ou não confiável; recursos que lidam com dados sensíveis devem priorizar precisão e confiabilidade, e todos os apps devem proteger a privacidade do usuário o tempo todo.
- Recursos proativos (que entregam resultado sem que a pessoa peça) tendem a ter menos tolerância a resultados de baixa qualidade, porque a pessoa não pediu aquele resultado; pode ser necessário usar dados adicionais para reduzir a chance de parecer intrusivo ou irrelevante.
- Recursos visíveis permitem que as pessoas formem opinião sobre a confiabilidade ao escolher entre os resultados; recursos invisíveis têm mais dificuldade de comunicar confiabilidade e de receber feedback, porque a pessoa pode nem saber que o recurso existe.

Faça e evite (feedback explícito):
- Peça feedback explícito somente quando necessário, já que exige que a pessoa tome uma ação; prefira usar feedback implícito quando possível.
- Sempre torne o fornecimento de feedback explícito uma tarefa voluntária, comunicando que ele ajuda a melhorar a experiência sem parecer obrigatório.
- Use linguagem simples e direta para descrever cada opção de feedback explícito e suas consequências; evite termos imprecisos como "dislike", que não comunicam consequência e são difíceis de traduzir (prefira algo como "Suggest less pop music", "Suggest more thrillers", "Mute politics for a week").
- Adicione ícones à descrição de uma opção se ajudar a entendê-la; evite usar um ícone sozinho, pois pode não comunicar granularidade ou consequência com clareza.
- Considere oferecer múltiplas opções ao pedir feedback explícito, dando senso de controle e ajudando a identificar sugestões indesejadas, progredindo de opções mais gerais para mais específicas.
- Aja imediatamente ao receber feedback explícito e persista a mudança resultante, por exemplo ocultando conteúdo indesejado em todo o app; isso constrói confiança de que o feedback tem valor.
- Considere usar feedback explícito para ajudar a decidir quando e onde mostrar resultados, já que a pessoa pode gostar de um resultado mas não querer vê-lo em certos momentos ou contextos.

Faça e evite (feedback implícito):
- Sempre proteja as informações das pessoas, já que o feedback implícito pode coletar dados potencialmente sensíveis.
- Ajude a pessoa a controlar sua informação; explique como o app obtém e compartilha dados, e ofereça formas de restringir esse fluxo, já que as pessoas podem se assustar ao ver que ações em um app afetam experiências em outro app, ou até suspeitar de compartilhamento indevido.
- Não deixe que o feedback implícito reduza as oportunidades de exploração da pessoa; ele reforça comportamento existente, o que pode piorar a experiência no longo prazo mesmo melhorando-a no curto prazo.
- Quando possível, use múltiplos sinais de feedback para melhorar sugestões e mitigar erros, já que o feedback implícito é indireto e pode ser difícil discernir a intenção real da pessoa (por exemplo, ver, compartilhar e salvar uma foto não significa necessariamente sentimento positivo sobre ela).
- Considere reter sugestões privadas ou sensíveis quando o app recebe feedback implícito relacionado a tópicos privados, já que pessoas compartilham contas e dispositivos.
- Priorize feedback recente, já que gostos mudam com frequência; caia de volta para feedback histórico se o recente não estiver disponível.
- Use feedback para atualizar previsões em um ritmo que combine com o modelo mental da pessoa sobre o recurso (sugestões de digitação devem atualizar imediatamente; recomendações de música contínuas e frequentes podem parecer apressadas ou sobrecarregar).
- Esteja preparado para mudanças no feedback implícito quando mudar a UI do app, já que mesmo pequenas alterações (como mover um botão) podem alterar o volume e tipo de feedback recebido.
- Cuidado com viés de confirmação: o feedback implícito é limitado ao que a pessoa pode ver e fazer no app e em outros apps, raramente revelando coisas novas que ela poderia gostar; evite basear-se apenas nele.

Faça e evite (calibração):
- Use calibração apenas quando o recurso não puder funcionar sem essa informação inicial; se o recurso puder funcionar sem calibração, considere obter a informação de forma implícita ou explícita.
- Sempre proteja as informações fornecidas durante a calibração, que podem ser sensíveis.
- Seja claro sobre por que precisa da informação da pessoa, enfatizando o que o recurso faz em vez de como ele funciona.
- Colete apenas a informação mais essencial, tornando a experiência mais confortável e aumentando a confiança.
- Evite pedir para a pessoa participar da calibração mais de uma vez; idealmente a calibração ocorre cedo na experiência, e depois disso use feedback implícito ou explícito para evoluir a informação sem pedir calibração de novo (exceto quando a calibração precisa ser feita com um objeto novo em vez de uma pessoa).
- Torne a calibração rápida e fácil: priorize obter poucos dados importantes e infira o resto por outras fontes ou feedback; evite pedir informação que a maioria teria que procurar; evite pedir ações difíceis de executar.
- Deixe claro como realizar a calibração com sucesso, dando um objetivo explícito e mostrando o progresso em direção a ele.
- Forneça assistência imediatamente se o progresso estagnar, com recomendações acionáveis, sem implicar que algo está errado ou que a pessoa é culpada, e sem deixá-la sem um próximo passo claro.
- Confirme o sucesso da calibração assim que ela for concluída, dando um caminho claro para usar o recurso.
- Deixe a pessoa cancelar a calibração a qualquer momento, sem implicar julgamento sobre a escolha; não há necessidade de mencionar o cancelamento depois, já que na próxima tentativa a pessoa terá nova chance.
- Dê à pessoa uma forma de atualizar ou remover informações fornecidas durante a calibração, idealmente também fora da própria experiência de calibração.

Faça e evite (mistakes, corrections, multiple options, confidence, attribution, limitations):
- Antecipe erros, ajude as pessoas a lidar com eles, e aprenda com eles quando isso melhorar o app (em alguns casos, aprender com um erro pode ter efeitos indesejados, como causar imprevisibilidade na experiência).
- Entenda a gravidade da consequência de um erro (uma sugestão de teclado errada incomoda; sugerir uma rota que causa perda de voo é sério) e forneça ações corretivas ou ferramentas proporcionais à gravidade.
- Facilite corrigir erros frequentes ou previsíveis; sem isso, as pessoas podem perder confiança no app.
- Atualize continuamente o recurso para refletir interesses e preferências em evolução, e atualize com informação específica de domínio (como tendências atuais).
- Quando possível, resolva erros sem complicar a UI; equilibre o efeito de um padrão na UI com seu potencial de agravar o erro (uma atribuição errada, por exemplo, amplifica o efeito do erro original).
- Seja especialmente cuidadoso para evitar erros em recursos proativos, já que as pessoas têm menos paciência com erros de algo que não pediram, e podem sentir que têm menos controle.
- Ao reduzir erros em uma área, considere sempre o efeito em outras áreas e na precisão geral (otimizar reconhecimento de cães pode piorar o de gatos).
- Dê formas familiares e fáceis de fazer correções, mostrando os passos que o app tomou na tarefa automatizada, para que a pessoa use os mesmos controles para refinar ou desfazer o resultado.
- Forneça valor imediato quando a pessoa fizer uma correção, exibindo o conteúdo corrigido instantaneamente e persistindo a atualização.
- Deixe a pessoa corrigir suas próprias correções, respondendo imediatamente e persistindo a atualização.
- Equilibre sempre o benefício de um recurso com o esforço exigido para corrigi-lo; se corrigir parecer mais trabalhoso que fazer manualmente, as pessoas param de usar o recurso.
- Nunca dependa de correções para compensar resultados de baixa qualidade, pois isso pode corroer a confiança e reduzir o valor do recurso.
- Aprenda com correções quando fizer sentido, verificando antes que a correção levará de fato a resultados de maior qualidade.
- Quando possível, use correções guiadas (que sugerem alternativas específicas, exigindo menos esforço) em vez de correções livres (freeform); um app pode suportar uma combinação de ambas.
- Prefira opções diversas ao apresentar múltiplos resultados, equilibrando precisão com diversidade das opções.
- Em geral, evite oferecer muitas opções, já que mais opções aumentam a carga cognitiva; quando possível, liste opções em uma única tela sem exigir rolagem.
- Liste a opção mais provável primeiro quando os valores de confiança se correlacionarem com a qualidade dos resultados; considere usar informação contextual (hora do dia, localização) para determinar a opção mais provável, e selecione a primeira opção por padrão se fizer sentido.
- Torne as opções fáceis de distinguir e escolher, com descrições breves que destaquem as diferenças; agrupe opções em categorias quando houver muitas para exibir em uma única view.
- Aprenda com as seleções quando fizer sentido, usando o feedback implícito de escolha para refinar as opções oferecidas e aumentar a chance de apresentar a opção mais provável primeiro; continuar oferecendo resultados incorretos tende a reduzir a confiança das pessoas.
- Verifique que os valores de confiança correspondem de fato à qualidade dos resultados antes de decidir como apresentá-los (por exemplo, revisando múltiplos limiares de confiança ou comparando entre versões do app); se não tiver certeza da correlação, não é boa ideia transmitir confiança às pessoas.
- Traduza valores de confiança para conceitos que as pessoas já entendem, em vez de simplesmente exibir um número (por exemplo, uma atribuição como "Because you listen to pop music" é mais acionável que "97% match").
- Em situações onde atribuições não ajudam, considere ordenar os resultados de forma que implique nível de confiança; se precisar exibir confiança diretamente, considere categorias semânticas (como "high chance", "low chance") em vez de números crus.
- Em cenários onde as pessoas esperam informação estatística ou numérica (previsão do tempo, estatísticas esportivas, pesquisas eleitorais), exiba valores de confiança que ajudem a interpretar os resultados, como intervalo ou porcentagem.
- Sempre que possível, ajude as pessoas a decidir transmitindo confiança em termos de sugestões acionáveis (por exemplo "This is a good time to buy" em vez de exibir uma porcentagem).
- Considere mudar a forma de apresentar resultados conforme diferentes limiares de confiança, adaptando a apresentação quando o nível de confiança tem impacto significativo na experiência (por exemplo, Photos mostra diretamente as fotos de uma pessoa quando a confiança é alta, mas pede confirmação quando a confiança é mais baixa).
- Quando os valores de confiança corresponderem de fato à qualidade do resultado, geralmente evite mostrar resultados quando a confiança for baixa; para recursos proativos, defina um limiar de confiança abaixo do qual você não oferece resultados.
- Considere usar atribuições (attribution) para explicar a base ou o raciocínio por trás de um resultado, sem explicar exatamente como o modelo funciona; use para incentivar mudança de comportamento, minimizar o impacto de erros, ajudar a construir modelo mental do recurso, ou promover confiança ao longo do tempo.
- Evite ser específico demais ou genérico demais em uma atribuição; atribuições muito específicas fazem a pessoa sentir que está sendo observada de perto demais, e atribuições muito genéricas parecem não personalizadas.
- Mantenha as atribuições factuais e baseadas em análise objetiva; não implique compreensão ou julgamento de emoções, preferências ou crenças da pessoa (prefira "Because you've read nonfiction" a "Because you love nonfiction").
- Em geral, evite jargão técnico ou estatístico em atribuições, exceto quando o próprio resultado for de natureza estatística ou técnica (clima, esportes, eleições, dados científicos).
- Identifique os cenários em que limitações do recurso impactam a experiência e desenhe formas de lidar com elas: defina expectativas antes do uso, mostre como obter os melhores resultados durante o uso, e explique o motivo quando o resultado for inferior.
- Ajude a estabelecer expectativas realistas, descrevendo a limitação em material de marketing ou no próprio contexto do recurso quando o efeito puder ser sério mas raro.
- Demonstre como obter os melhores resultados, por exemplo com texto de placeholder que sugira o tipo de entrada, feedback em tempo real conforme a pessoa interage, ou sugestão de formas alternativas de alcançar o objetivo.
- Explique como limitações podem causar resultados insatisfatórios, para que a pessoa ajuste suas expectativas (por exemplo, Memoji avisa que não funciona bem no escuro).
- Considere avisar quando limitações forem resolvidas, para que a pessoa ajuste o modelo mental do recurso e volte a usar interações que antes evitava.

Especificações exatas: não há números de medida, tamanho ou duração no texto; o único valor numérico citado é o exemplo ilustrativo de "97% match" usado para explicar por que exibir a porcentagem crua não é comunicação eficaz.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: "Generative AI" (para orientação relacionada ao uso de modelos de machine learning em experiências inteligentes), "Privacy", "Create ML" e "Core ML" (documentação de desenvolvedor), "Onboarding" não citado aqui mas relevante ao contexto geral do grupo.

<!-- visual:machine-learning -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura usa três estrelas de quatro pontas (sparkles) em tamanhos diferentes sobre degradê azul, com grade tracejada horizontal, vertical e diagonal e um círculo guia central; as pontas atravessam o círculo, que funciona como referência de escala e não como contorno de cada forma (img 0742).
- O feedback explícito aparece dentro de um menu de contexto branco flutuante e padrão, sobre um iPhone cinza sem cor de app: quatro linhas genéricas em cinza no topo e, abaixo de um divisor, duas opções com texto e ícone ("Love" com coração, "Suggest Less Like This" com polegar para baixo), ou seja, junto das demais ações e não num controle à parte (img 0743).
- O feedback implícito vira notificação no Apple Watch sobre fundo preto, com a frase "It looks like you're working out." e dois botões grandes abaixo do texto: a opção mais provável em verde limão vivo e a alternativa em cinza escuro (img 0744).
- A calibração é um fluxo de tela cheia em fundo preto: rosto esquemático dentro de um círculo pontilhado, título com instrução de posicionar e girar a cabeça, e um único botão azul "Get Started" na base (img 0745).
- A correção é mostrada como ferramenta manual sobre um resultado automático: modo de recorte e endireitar com alças nas quatro bordas da foto, roda de inclinação na base com o indicador levemente fora do centro, ícones de girar, espelhar e grade acima dela, e "AUTO" destacado em amarelo na barra superior (img 0746).
- Múltiplas opções aparecem ao mesmo tempo em duas vistas: três rotas azuis no mapa, cada uma com etiqueta de tempo, e um painel lateral "Options" listando tempo e distância, com a primeira rota selecionada em azul como a mais rápida (img 0747).
- A confiança é comunicada em linguagem natural e não em número: um app de voos com cabeçalho roxo claro traz "Keep waiting." em roxo, o menor preço atual e a economia estimada, seguidos de hierarquia de botões com "Track" preenchido em roxo, "View Flights" contornado e "Find New Dates" abaixo (img 0748).
- A atribuição é uma linha de subtítulo logo abaixo do título da seção "For You" (com seta de navegação), acima de uma fileira de cartões com ícone de câmera de vídeo, em que o terceiro fica cortado na borda direita do quadro (img 0749).
- A limitação é sinalizada por uma pequena pílula cinza "Low light" sobreposta à base do contorno amarelo pontilhado de rastreamento facial, no próprio quadro de captura, sem alerta modal; abaixo fica a grade de Memoji e Animoji com o item atual contornado e a opção "+" para criar outro (img 0750).
Divergências registradas: na img 0745 o texto alternativo oficial fala de um rosto, mas o desenho é um rosto sorridente esquemático, não uma foto. Na img 0750 a etiqueta "Low light" é mais discreta do que a descrição sugere, uma pílula pequena e não um texto grande central.
<!-- /visual:machine-learning -->

## Maps (slug: maps)

O que governa: como incorporar um mapa interativo (outdoor ou indoor) no app ou site, incluindo estilo visual, informação customizada sobre o mapa (annotations, overlays), place cards e mapas de interiores (indoor maps).

Por que: o princípio central é a familiaridade funcional: um mapa em um app de terceiros deve suportar as mesmas interações básicas que as pessoas já esperam do app Maps do sistema (zoom, pan, rotação), para que elementos não interativos que obscurecem o mapa não frustrem essa expectativa. Há também uma preocupação legal e de marca com a visibilidade do logo Apple e do link legal, que devem permanecer visíveis e fixos em relação ao mapa, e uma preocupação de legibilidade em cenários de muita densidade de informação, resolvida por clustering de pontos de interesse e por níveis progressivos de detalhe conforme o zoom.

Faça e evite:
- Em geral, torne o mapa interativo; elementos não interativos que obscurecem o mapa podem interferir nas expectativas das pessoas.
- Escolha um estilo de ênfase adequado às necessidades do app: o estilo padrão (default), com cores totalmente saturadas, é bom para a maioria dos apps de mapa padrão sem muitos elementos customizados, e mantém alinhamento visual com o app Maps; o estilo muted (desaturado) é ótimo quando há muito conteúdo rico em informação que precisa se destacar contra o mapa.
- Ajude as pessoas a encontrar lugares no mapa, considerando um recurso de busca combinado com filtro de locais por categoria.
- Identifique claramente elementos selecionados, usando estilo distinto como contorno e variação de cor.
- Agrupe (cluster) pontos de interesse sobrepostos para melhorar a legibilidade do mapa; um cluster usa um único pino para representar múltiplos pontos de interesse próximos, que se expandem progressivamente ao dar zoom.
- Ajude a manter visível o logo da Apple e o link legal: não os cubra o tempo todo (cobrir temporariamente é aceitável); use padding adequado para separá-los das bordas do mapa e dos controles customizados; evite que o logo e o link se movam junto com a interface (o ideal é que pareçam fixos ao mapa); se a interface customizada puder se mover em relação ao mapa, use a posição mais baixa do elemento customizado para determinar o posicionamento do logo e do link.
- Use annotations que combinem com o estilo visual do app para identificar pontos de interesse customizados; é possível mudar a cor (tint) da marcação padrão (que tem tonalidade vermelha e ícone de pino branco) e trocar o ícone por uma string ou imagem, como um logo; uma string de ícone pode conter qualquer caractere, incluindo Unicode, mas deve ter de dois a três caracteres para legibilidade.
- Se quiser exibir informação customizada relacionada a feições padrão do mapa, considere torná-las selecionáveis de forma independente, já que o sistema trata feições fornecidas pela Apple (pontos de interesse, territórios, feições físicas) de forma independente de outras anotações adicionadas.
- Use overlays para definir áreas do mapa com uma relação específica ao conteúdo: o nível "above roads" (padrão) coloca o overlay acima das ruas mas abaixo de prédios, árvores e outras feições, útil quando se quer que as pessoas tenham noção do que está abaixo do overlay; o nível "above labels" coloca o overlay acima de ruas e rótulos, ocultando tudo abaixo, útil para conteúdo totalmente abstraído das feições do mapa ou para ocultar áreas irrelevantes.
- Garanta contraste suficiente entre controles customizados e o mapa, usando um traço fino ou sombra leve para destacar o controle, ou aplicando blend modes na área do mapa.
- Use place cards para exibir informação estruturada e atualizada sobre lugares, como horário de funcionamento, telefone e endereço.
- Ao exibir place cards diretamente no mapa, escolha entre os estilos disponíveis: automatic (o sistema decide com base no tamanho da view do mapa), callout (estilo popover ao lado do lugar selecionado, com variante full para versão grande e detalhada e compact para versão concisa que economiza espaço; se não especificar, o padrão é o automatic callout), caption (exibe apenas um link "Open in Apple Maps") e sheet (exibe o place card em uma folha).
- Saiba que o place card de estilo full callout aparece de forma diferente conforme o dispositivo: em popover no iPadOS e macOS, e como folha (sheet) no iOS.
- Considere a apresentação do mapa ao escolher um estilo de place card; escolha um estilo que se encaixe no contexto (por exemplo, um mapa pequeno com muitas anotações se beneficia do estilo compact callout).
- Garanta que o place card fique bom em diferentes dispositivos e tamanhos de janela; para o estilo full callout, é possível definir uma largura mínima para evitar que o texto transborde em dispositivos menores.
- Evite duplicar informação já exibida em outro lugar do app ou site ao escolher um estilo de place card.
- Mantenha o local no mapa visível ao exibir um place card, ajudando a manter a noção de onde o local está; é possível definir uma distância de offset para o place card apontando para o local selecionado.
- Ao exibir place cards fora de um mapa (por exemplo em uma lista de resultados de busca), se não exibir o place card diretamente dentro de uma map view, é obrigatório incluir um mapa dentro do próprio place card.
- Use pistas relacionadas a localização no conteúdo ao redor para comunicar que é possível abrir um place card, como exibir nome e endereço do lugar ao lado de um botão de mais detalhes, ou incluir um ícone de pino de mapa junto ao nome do lugar.
- Para mapas de interiores (indoor maps) ligados a locais específicos como shoppings e estádios, ajuste o nível de detalhe do mapa conforme o nível de zoom, mostrando áreas grandes como salas e prédios em todos os níveis de zoom e adicionando progressivamente mais detalhes e rótulos conforme se aproxima o zoom.
- Use estilo visual distinto (cor e ícones) para diferenciar as feições do mapa e ajudar as pessoas a encontrar rapidamente o que procuram.
- Ofereça um seletor de andar (floor picker) se o local tiver múltiplos níveis, mantendo os números de andar concisos (geralmente uma lista de números de andar em vez de nomes é suficiente).
- Inclua áreas ao redor para dar contexto, como ruas adjacentes, playgrounds e outros locais próximos; se essas áreas forem não interativas, use esmaecimento (dimming) e cor distinta para que pareçam suplementares.
- Considere suportar navegação entre o local e pontos de trânsito próximos (ônibus, trem, estacionamento), oferecendo também a opção de trocar rapidamente para o app Maps para mais opções de navegação.
- Limite a rolagem para fora do local, para ajudar as pessoas a não se perderem ao deslizar com força demais; quando possível, mantenha ao menos parte do mapa de interior visível na tela o tempo todo, ajustando a quantidade de rolagem permitida conforme o nível de zoom.
- Desenhe um mapa de interior que pareça uma extensão natural do app; não tente replicar a aparência do app Apple Maps, e sim combinar overlays de área, ícones e texto com o estilo visual do próprio app.

Especificações exatas:
- Padding recomendado ao redor do logo Apple e do link legal em relação às bordas do mapa e controles customizados: 7 pontos nas laterais e 10 pontos acima e abaixo dos elementos.
- Quando a interface customizada pode se mover em relação ao mapa (por exemplo um cartão que sobe da parte inferior), posicionar o logo e o link a 10 pontos acima da posição de repouso mais baixa do cartão.
- O logo da Apple e o link legal não são exibidos em mapas menores que 200x100 pixels.
- Strings de ícone de annotation devem ter de dois a três caracteres de comprimento para legibilidade.
- No watchOS, é possível adicionar até cinco anotações a um mapa.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS, macOS, tvOS ou visionOS.
watchOS: no Apple Watch, mapas são snapshots estáticos de localizações geográficas; posicione um mapa na interface em tempo de design e mostre a região apropriada em runtime. A região exibida não é interativa; tocar nela abre o app Maps no Apple Watch. É possível adicionar até cinco anotações para destacar pontos de interesse ou informação relevante. Ajuste o elemento de mapa ao tamanho da tela, para que o elemento inteiro seja visível sem exigir rolagem. Mostre a menor região que abranja os pontos de interesse, já que o conteúdo do elemento de mapa não rola, então todo conteúdo-chave precisa estar visível na região exibida.

Ligações com outros artigos: não há referência cruzada explícita a outro artigo das HIG citado no texto (apenas documentação de desenvolvedor MapKit, MapKit JS e Indoor Mapping Data Format).

<!-- visual:maps -->
### O que as ilustrações mostram
Base: 5 de 5 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura desenha o mapa dobrado em três painéis só em contorno grosso azul escuro, vazado, sobre degradê azul com a grade tracejada e o círculo guia de construção (img 0753).
- Estilo padrão e estilo muted são comparados no mesmo enquadramento 3D da Coit Tower, com os mesmos prédios, árvores, rotatória e selo com foto: só a saturação muda, do verde vivo e telhado avermelhado para cinza esverdeado e bege; nessa comparação, como nas demais de estilo e plataforma da página, não há grade nem anotação (img 0754, 0755).
- O clustering é um antes e depois de zoom: um único pino circular laranja com "3" em branco centralizado substitui os pontos próximos (img 0756) e, aproximando, vira três pinos em gota laranja, cada um com xícara branca e rótulo abaixo (img 0757).
- Os estilos de place card aparecem sobre o mesmo mapa e o mesmo pino, variando só a densidade: o full callout empilha imagem de cabeçalho, ícone circular marrom, nome, categoria e avaliação, bloco de horário, bloco de site, telefone e endereço, e termina no botão "Open in Apple Maps" (img 0758); o compact fica ancorado logo acima do pino com nome, categoria e endereço, avaliação e o link azul (img 0759); o caption reduz tudo ao rótulo sob o pino e ao link azul sozinho (img 0760).
- No iPad, o mesmo full callout também aparece como folha centralizada sobre o mapa, com botão X de fechar no canto superior direito do cartão (img 0761).
- No iPhone, o full callout é uma folha que sobe da borda inferior e ganha estrutura própria: fileira de botões de ação com ícone (tempo de carro, ligar, site, pedir, mais), fileira de métricas (horário, avaliação, custo, distância), seção de detalhes e o botão final para abrir no Maps; o endereço aparece abreviado e em azul, enquanto no iPad vinha completo em preto (img 0762).
- O mapa de interior começa na vista ampla da cidade com o aeroporto marcado por ícone quadrado azul de avião e um cartão inferior com ações e métricas (img 0763); ao aproximar, surgem o rótulo do terminal, o link azul "Look Inside" acima do ícone e os números de portão em cápsulas amarelas ao longo do corredor, com novos controles de mapa à direita (mapa, localização, 3D, bússola) (img 0764).
- No nível de sala, o terminal em forma de L é preenchido em rosa claro e rotula funções internas com marcadores laranja (cruz para primeiros socorros, círculo para segurança), enquanto escadas e elevadores ficam em lilás fora do contorno, com busca na base (img 0765); numa vista equivalente, com o mapa quase todo branco e menos elementos, um único ponto aparece selecionado, o elevador, com ícone quadrado azul no centro do prédio e um cartão de detalhe embaixo com o texto cortado (img 0766).
- A vista volta para fora do terminal: vias rotuladas, marcadores numerados em cápsulas amarelas ao longo da margem da via e estacionamento azul numa pequena área cinza, com as ruas levemente esmaecidas e em cor neutra, contrastando com o verde vivo da grama ao lado (img 0767).
- O mapa de interior de um app próprio adota a identidade do app: fundo verde claro, prédios em verde mais escuro, marcadores circulares vermelhos, marcadores numerados em cápsulas verdes, pino azul de localização atual, campo de busca, lista inferior com tempo até cada destino e barra de abas verde do próprio app, mantendo a lógica de pinos numerados e marcadores redondos do mapa padrão (img 0768).
- No Apple Watch, o mapa é um snapshot em tema escuro do Apple Park em 3D, com rótulo em maiúsculas brancas, pino azul de localização e só dois botões circulares flutuantes no canto inferior direito (azul com seta de navegação, preto com três pontos), sem busca nem lista (img 0769).
<!-- /visual:maps -->

## NFC (slug: nfc)

O que governa: como um app iOS pode ler tags NFC (near-field communication) de objetos físicos, tanto ativamente dentro do app (in-app tag reading) quanto em segundo plano (background tag reading), incluindo a linguagem correta a usar ao instruir a pessoa a escanear.

Por que: o princípio central é acessibilidade da linguagem: como NFC pode ser tecnicamente desconhecido para muitas pessoas, o texto orienta evitar termos técnicos voltados a desenvolvedor (NFC, Core NFC, tag) e usar linguagem conversacional amigável. Há também uma correção de expectativa física: como o escaneamento exige apenas proximidade e não contato físico real com a tag, o texto instrui a usar verbos como "scan" e "hold near" em vez de "tap" e "touch", para não induzir a pessoa a tentar tocar fisicamente o objeto.

Faça e evite:
- Não incentive as pessoas a fazer contato físico com objetos; o dispositivo só precisa estar próximo da tag, não tocá-la. Use termos como "scan" e "hold near" em vez de "tap" e "touch".
- Use terminologia acessível, evitando termos técnicos orientados a desenvolvedor como NFC, Core NFC, "near-field communication" e "tag"; use termos amigáveis e conversacionais que a maioria das pessoas entenda (por exemplo "Scan the [object name]" em vez de "Scan the NFC tag"; "Hold your iPhone near the [object name] to learn more about it" em vez de "To use NFC scanning, tap your phone to the [object]").
- Forneça texto instrucional sucinto para a folha de escaneamento (scanning sheet): uma frase completa, em sentence case, com pontuação final, identificando o objeto a ser escaneado, revisando o texto adequadamente para escaneamentos subsequentes, e mantendo o texto curto para evitar truncamento (por exemplo, primeiro escaneamento: "Hold your iPhone near the [object name] to learn more about it."; escaneamentos seguintes: "Now hold your iPhone near another [object name].").
- Suporte tanto leitura em segundo plano quanto leitura dentro do app; o app deve sempre fornecer uma forma de escanear tags dentro do app, para pessoas com dispositivos que não suportam leitura em segundo plano.

Especificações exatas: o texto não traz números de medida, tamanho, duração ou proporção. Nota factual: a leitura em segundo plano não está disponível quando uma folha de escaneamento NFC está visível, quando Wallet ou Apple Pay estão em uso, quando câmeras estão em uso, quando o dispositivo está em Modo Avião, e quando o dispositivo está bloqueado após uma reinicialização.

Diferenças por plataforma: sem considerações adicionais para iOS ou iPadOS. Não suportado em macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: não há referência cruzada explícita a outro artigo das HIG (apenas documentação de desenvolvedor Core NFC).

<!-- visual:nfc -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página não tem vídeo.
- A abertura, tingida de azul sobre a grade geométrica e o círculo guia, mostra três arcos concêntricos crescentes para a direita, simétricos e ocupando boa parte do quadro, o que confere com a descrição oficial de linhas curvas cada vez maiores; é o mesmo motivo de ondas da página nearby-interactions (img 0806), aqui sem o círculo de pessoa ou sensor (img 0807).
- A leitura dentro do app é uma folha com título "Ready to Scan", ícone circular azul com um smartphone estilizado (com leve reflexo na borda esquerda, sugerindo vidro), uma frase de instrução, "Hold your device near the NFC tag.", e um botão "Cancel" cinza claro ocupando toda a largura na base (img 0808).
- A leitura em segundo plano não mostra nenhuma tela do app: o primeiro contato é um banner padrão de notificação no topo da Tela de Início, com ícone preto de ondas à esquerda, título "Item Detected", ação de abrir no app e horário, sobreposto e cobrindo parte da primeira fileira de ícones (img 0809).
<!-- /visual:nfc -->

## Photo editing (slug: photo-editing)

O que governa: como criar extensões de edição de fotos (photo-editing extensions) que deixam as pessoas modificarem fotos e vídeos dentro do app Photos, aplicando filtros ou outras alterações.

Por que: o princípio orientador é preservação e clareza de contexto: as edições são sempre salvas como novos arquivos no app Photos, preservando a versão original com segurança, e a extensão carrega dentro de uma view modal que já inclui uma toolbar do próprio app Photos, então duplicar essa toolbar ou pedir confirmação de cancelamento sem necessidade apenas confunde e desperdiça espaço e tempo da pessoa.

Faça e evite:
- Confirme o cancelamento de edições, já que editar uma foto ou vídeo pode consumir tempo; peça confirmação de que a pessoa realmente quer cancelar e informe que as edições serão perdidas; não é necessário mostrar essa confirmação se nenhuma edição foi feita ainda.
- Não forneça uma toolbar superior customizada; a extensão carrega dentro de uma view modal que já inclui uma toolbar, e uma segunda toolbar é confusa e tira espaço do conteúdo sendo editado.
- Deixe a pessoa pré-visualizar as edições antes de aprovar; é difícil aprovar uma edição sem ver o resultado do trabalho antes de fechar a extensão e voltar ao app Photos.
- Use o ícone do próprio app como ícone da extensão de edição de foto, para transmitir confiança de que a extensão é de fato fornecida pelo app.

Especificações exatas: o texto não traz números de medida, tamanho, duração ou proporção.

Diferenças por plataforma: sem considerações adicionais para iOS, iPadOS ou macOS. Não suportado em tvOS, visionOS ou watchOS.

Ligações com outros artigos: não há referência cruzada explícita a outro artigo das HIG (apenas documentação de desenvolvedor "App extensions" e "PhotoKit").

<!-- visual:photo-editing -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta, todos os códigos conferidos; a página tem uma única ilustração e nenhum vídeo.
- O símbolo da página é formado por marcas de corte em azul escuro, dois cantos em L opostos (superior esquerdo e inferior direito), em traço grosso colorido (img 0840).
- Duas setas curvas cercam as marcas, uma no topo apontando para a esquerda e outra embaixo apontando para a direita, desenhando um movimento circular incompleto que soma a ideia de rotação à de corte; a imagem confere com a descrição oficial (img 0840).
- A construção segue o sistema das outras ilustrações de abertura, como as de onboarding e offering-help: retângulo de cantos arredondados com degradê na cor temática, aqui azul, atravessado por grade pontilhada retangular e um círculo guia central (img 0840).
<!-- /visual:photo-editing -->

## ResearchKit (slug: researchkit)

O que governa: como usar o framework ResearchKit para desenhar um app de pesquisa médica, incluindo a sequência correta de onboarding (introdução, elegibilidade, consentimento informado, permissão de acesso a dados), a condução de pesquisas via surveys e active tasks, e a gestão de informação pessoal e engajamento dos participantes.

Por que: o princípio central é clareza em telas que não serão revisitadas: como as telas de onboarding de um app de pesquisa normalmente só são vistas uma vez, a clareza é essencial, e a ordem fixa (Introduction, Eligibility, Informed consent, Permission to access data) existe para garantir que ninguém avance para consentimento sem antes saber se é elegível, e que o consentimento informado sempre preceda qualquer coleta real de dado sensível. Há também uma nota explícita de que as diretrizes têm caráter apenas informativo e não constituem aconselhamento jurídico, refletindo que consentimento em pesquisa médica envolve requisitos legais e éticos (institutional review board / ethics review board) que vão além do design de interface.

Faça e evite:
- Sempre exiba as telas de onboarding na ordem correta: Introduction, depois Eligibility, depois Informed consent, depois Permission to access data.
- Na introdução, descreva claramente o assunto e o propósito do estudo, e permita que participantes existentes façam login rapidamente para continuar um estudo em andamento.
- Determine a elegibilidade o quanto antes, apresentando apenas os requisitos de elegibilidade necessários ao estudo, com linguagem simples e direta, e facilitando a entrada de informação; pessoas não precisam avançar até a seção de consentimento se não forem elegíveis.
- Antes de obter o consentimento, garanta que os participantes entendam o estudo; quebre um formulário de consentimento longo em seções digestíveis (uma para cada aspecto, como coleta de dados, uso de dados, benefícios potenciais, riscos possíveis, tempo exigido, como desistir), usando linguagem simples para uma visão geral e, se necessário, um botão "Learn More" para uma explicação mais detalhada; os participantes precisam poder visualizar o formulário de consentimento inteiro antes de concordar em participar.
- Se fizer sentido, forneça um quiz que teste a compreensão do participante, para perguntas que de outra forma seriam feitas ao obter consentimento presencialmente.
- Obtenha o consentimento do participante e, se apropriado, algumas informações de contato; após concordar em participar, os participantes recebem um diálogo de confirmação, seguido de telas para assinatura e detalhes de contato; a maioria dos apps de pesquisa envia por e-mail uma versão em PDF do formulário de consentimento para os registros do participante.
- Obtenha permissão para acessar o dispositivo ou dados do participante e para enviar notificações; explique claramente por que o app de pesquisa precisa de acesso a localização, Health ou outros dados, e não peça acesso a dados que não sejam críticos ao estudo; se necessário, peça também permissão para enviar notificações.
- Crie surveys que mantenham os participantes engajados, usando as telas customizáveis do ResearchKit para apresentar perguntas de diferentes tipos de resposta (verdadeiro ou falso, múltipla escolha, data e hora, escala deslizante, texto livre), seguindo estas diretrizes: informe quantas perguntas há e a duração aproximada do survey; use uma tela por pergunta; mostre o progresso do participante no survey; mantenha o survey o mais curto possível (vários surveys curtos costumam funcionar melhor que um longo); use a fonte padrão para a pergunta e uma fonte um pouco menor para texto explicativo adicional; avise o participante quando o survey estiver completo.
- Torne as active tasks fáceis de entender; uma active task exige que o participante se engaje em uma atividade (falar no microfone, tocar os dedos na tela, caminhar, fazer um teste de memória); descreva como realizar a tarefa com linguagem clara e simples; explique quaisquer requisitos, como se a tarefa deve ser realizada em um horário específico ou sob circunstâncias específicas; garanta que os participantes saibam quando a tarefa está completa.
- Use um perfil (profile) para ajudar os participantes a gerenciar dados pessoais relacionados ao estudo, permitindo editar dados que podem mudar ao longo do estudo (como peso ou hábitos de sono), lembrar de atividades futuras, e fornecer forma fácil de sair do estudo e ver informação importante como o documento de consentimento e a política de privacidade.
- Use um dashboard para mostrar progresso e motivar os participantes a continuar, se apropriado ao estudo, fornecendo feedback encorajador como progresso diário, avaliações semanais, resultados de atividades específicas, e até comparações agregadas com outros participantes do estudo.
- Idealmente, tanto o perfil quanto o dashboard de progresso ficam acessíveis o tempo todo no app.

Especificações exatas: o texto não traz números de medida, tamanho, duração ou proporção.

Diferenças por plataforma: sem considerações adicionais para iOS ou iPadOS. Não suportado em macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: "Research & Care > ResearchKit" e "Research & Care > Developers" (documentação de desenvolvedor), "Protecting user privacy, HealthKit", "ResearchKit GitHub project".

<!-- visual:researchkit -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações abertas, todos os códigos conferidos; a página não tem vídeo.
- A abertura desenha em azul uma forma de losango em camadas, como páginas empilhadas vistas em perspectiva, com pequenos corações sobre a face superior, sobre grade retangular e círculo concêntrico de construção (img 0922).
- A ordem do onboarding é um diagrama plano de quatro caixas roxo claro de cor uniforme, em fileira, ligadas por setas da esquerda para a direita e rotuladas só com texto simples, sem ícones (img 0923).
- A introdução do app de exemplo usa fundo roxo escuro, uma ilustração central de pessoa idosa cercada de ícones, título de boas-vindas com subtítulo que nomeia o estudo e um botão "Next" branco na base (img 0924).
- A elegibilidade é um formulário escrito como frases corridas com campos embutidos (um campo de idade, país e tipo de telefone em menus), sob barra roxa com voltar, título e ajuda; na base, "Back" e "Submit" lado a lado e "Step 3 of 3" com barra de progresso quase cheia (img 0925).
- O quiz traz a primeira pergunta, sobre o propósito do estudo, em negrito, com três opções de rádio (a primeira marcada), botão "Next" dourado centralizado e "Step 1 of 5" com a barra de progresso no início (img 0926).
- A tela de assinatura é a mais densa: cada item de consentimento tem ícone colorido à esquerda e check verde à direita, seguido do parágrafo legal e do nome digitado; a decisão final é um par assimétrico, "Disagree" como texto simples e "Accept" como botão amarelo sólido (img 0927).
- Rolando a mesma tela, a opção de compartilhamento de dados vira dois botões de rádio (compartilhar com outros pesquisadores ou só com este estudo, este marcado) e sobra um único "Accept" amarelo (img 0928).
- O mesmo botão primário aparece em dois estados: amarelo sólido quando há ação possível (Next, Submit, Accept, Get started) e amarelo pálido quando nada foi selecionado, como na pesquisa de sintomas de múltipla seleção, que tem pergunta em negrito, subtítulo pedindo marcar todas as que se aplicam e lista branca agrupada sob um rótulo de categoria (img 0929).
- A tarefa ativa combina topo roxo escuro com ilustração de pessoa andando, título, texto explicativo e uma seção do que será preciso com três ícones circulares coloridos rotulados, fechando em "Get started" amarelo (img 0930).
- Pesquisa e tarefa ativa usam um "x" branco de fechar no canto superior esquerdo (img 0929, 0930), enquanto elegibilidade, quiz e assinatura trazem seta de voltar na barra roxa (img 0925, 0926, 0927).
- O perfil é uma lista de pares rótulo e valor com seta de navegação à direita, engrenagem na barra roxa e barra de abas com três itens, a ativa destacada em roxo (img 0931); o histórico agrupa registros por data com horário, ícone colorido por tipo de tarefa e nome, repetindo o vocabulário de ícones das tarefas e a mesma barra de abas (img 0932).
<!-- /visual:researchkit -->

## O que este grupo revela sobre o jeito Apple

1. A permissão nunca é um evento único e definitivo: em healthkit, homekit, id-verifier e researchkit, o texto trata pedir acesso como algo contextual e revogável, repetido sempre que necessário, nunca assumido como concedido para sempre.

2. Minimização de dado como regra estrutural, não apenas ética: healthkit ("request access to health data only when you need it"), id-verifier ("ask only for the data you need", com requisições Display Only que nem transmitem dado ao app) e machine-learning (calibração: "collect only the most essential information") mostram o mesmo princípio aplicado em domínios completamente diferentes.

3. Elementos visuais de confiança do sistema (ícones, badges, rings) são tratados como propriedade intelectual protegida e semanticamente fixa: healthkit (Activity ring, ícone Apple Health), homekit (ícone HomeKit), live-photos (badge de Live Photo) e maps (logo Apple) compartilham a mesma lógica de "nunca altere cor, forma, escala ou posição", porque o significado do elemento depende da consistência visual entre apps.

4. A terminologia voltada ao desenvolvedor nunca deve vazar para a interface voltada à pessoa: healthkit proíbe o termo "HealthKit" em texto de usuário, homekit distingue cuidadosamente "action set" (API) de "scene" (UI), e nfc proíbe termos como "NFC", "Core NFC" e "tag" em favor de linguagem conversacional.

5. Nunca duplicar ou fragmentar uma fonte única de verdade: icloud evita perguntar quais documentos manter (a nuvem é a fonte única), homekit exige deferir sempre ao banco de dados do HomeKit e nunca apresentar configurações duplicadas, e in-app-purchase usa a folha de confirmação e o fluxo de reembolso do sistema em vez de replicá-los.

6. O cancelamento, a saída e a reversão devem ser sempre fáceis e nunca escondidos: in-app-purchase insiste que cancelar uma assinatura nunca pode parecer difícil ou desencorajado, machine-learning exige que a calibração possa ser cancelada a qualquer momento sem julgamento, e photo-editing pede confirmação antes de descartar edições, mas nunca bloqueia a saída.

7. Feedback e correção de erro sempre disparam ação imediata e persistente: machine-learning é explícito em pelo menos três seções (explicit feedback, implicit feedback, corrections) que qualquer resposta da pessoa deve ser refletida instantaneamente e mantida, nunca perdida ou ignorada.

8. Onboarding sequencial e não revisitável exige clareza redobrada: researchkit define uma ordem fixa de quatro etapas de onboarding justamente porque essas telas normalmente são vistas uma única vez, e in-app-purchase recomenda mostrar o valor da assinatura logo no onboarding antes de pedir compromisso financeiro.

9. Adaptação entre plataformas nunca é apenas redimensionamento: mac-catalyst é o exemplo mais explícito, com uma seção inteira dedicada a por que simplesmente escalar a interface do iPad não basta, exigindo repensar navegação, entrada, menus e layout para as convenções nativas do Mac.

10. Sensibilidade do dado determina o rigor do tratamento de UI, não apenas de segurança backend: healthkit, id-verifier, homekit e a seção de dados privados/públicos de machine-learning tratam a interface (o texto de permissão, a UI de calibração, os prompts) como parte do mecanismo de proteção de privacidade, não como uma camada decorativa sobre uma política de backend.

11. Transparência sobre limitações e confiança é preferida a fingir precisão perfeita: machine-learning dedica seções inteiras a "Limitations", "Confidence" e "Attribution" instruindo a comunicar abertamente quando um recurso pode falhar ou quando a confiança é baixa, em vez de simplesmente ocultar a imperfeição.

12. Nomenclatura correta de marca e trademark é tratada com o mesmo rigor em contextos técnicos bem diferentes: homekit dedica uma seção inteira a capitalização e uso correto de "HomeKit" e "Apple Home", e healthkit faz o mesmo para "Apple Health", ambos proibindo tradução do nome da marca e exigindo créditos legais corretos.

## Evidência de leitura

- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/healthkit.md, 67 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/homekit.md, 209 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/icloud.md, 32 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/id-verifier.md, 42 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/imessage-apps-and-stickers.md, 66 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/in-app-purchase.md, 132 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/live-photos.md, 34 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/mac-catalyst.md, 111 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/machine-learning.md, 196 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/maps.md, 106 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/nfc.md, 32 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/photo-editing.md, 26 linhas lidas, até o fim: sim
- /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/researchkit.md, 76 linhas lidas, até o fim: sim

Todos os 13 artigos deste grupo têm texto próprio; nenhum é apenas índice de coleção.
