# Patterns (parte 1)

Base de conhecimento sobre os artigos de padrões de interação das Apple Human Interface Guidelines: apresentação de dados, colaboração, drag and drop, entrada de dados, feedback, gestão de arquivos, tela cheia, lançamento de apps, exibição ao vivo, carregamento, contas, notificações, modalidade, multitarefa, ajuda, onboarding, áudio, haptics, vídeo, impressão, avaliações e busca.

## Charting data (slug: charting-data)

O que governa: como e quando usar gráficos (charts) para comunicar dados de forma clara, em vez de despejar texto ou tabelas.

Por que: um gráfico chama a atenção visual, então a Apple trata essa proeminência como algo a ser usado com responsabilidade, comunicando exatamente o que a pessoa precisa aprender sobre os dados que importam para ela. A ideia central é gradualidade: revelar complexidade aos poucos, e examinar os dados em múltiplos níveis (macro, subconjuntos, pontos individuais) para descobrir o que vale a pena destacar.

Faça e evite:
- Use um gráfico quando quiser destacar informação importante de um conjunto de dados; se só precisa oferecer os dados sem análise, prefira lista ou tabela pesquisável e ordenável.
- Mantenha o gráfico simples; deixe que a pessoa escolha quando quer mais detalhe, em vez de empacotar tudo de uma vez.
- Torne todo gráfico acessível, com labels de acessibilidade que descrevem valores e componentes, além de elementos de acessibilidade para interação.
- Prefira tipos de gráfico comuns (barras, linhas) porque as pessoas já sabem lê-los; se inventar um tipo novo, ensine como interpretá-lo (o exemplo citado é a animação individual dos Activity Rings ao parear o Watch com o iPhone).
- Examine os dados em nível macro (totais, médias), médio (subconjuntos úteis) e individual (pontos específicos) para enriquecer o gráfico.
- Adicione texto descritivo (títulos, subtítulos, anotações) para reforçar o que é acionável; o texto descritivo não substitui os labels de acessibilidade.
- Dimensione o gráfico conforme a funcionalidade, o tema e o nível de detalhe: grande o bastante para detalhes e interatividade, pequeno quando for só uma prévia glanceable.
- Mantenha consistência visual entre múltiplos gráficos do app, mudando o tipo ou estilo só para destacar diferenças reais.
- Mantenha continuidade (mesmo tipo, cores, anotações, layout, texto) entre gráficos que representam o mesmo conjunto de dados em diferentes níveis de detalhe.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Charts (componente relacionado).

<!-- visual:charting-data -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações (img 0231 a 0233) vista, código conferido; a página não tem vídeo.
- A abertura é um esboço de gráfico de barras: quatro barras verticais que sobem e depois descem, apoiadas numa linha de base, em contorno vermelho escuro sobre degradê laranja, com grade tracejada e círculo guia de construção (img 0231).
- No Stocks, a tela de detalhe da AAPL traz preço e variação, um seletor de período com "1M" marcado e um único gráfico de linha verde preenchido para esse período, com eixo horizontal de dias (23, 30, 7, 14, 21) e eixo vertical de preço de 277 a 312 (img 0232).
- No Health, a tela Activity abre com o anel colorido e três métricas numéricas (Move, Exercise, Stand) e depois empilha três gráficos de barras verticais, um por métrica, cada um com cor própria (vermelho, verde e ciano), escala vertical própria e o mesmo eixo de horas do dia; um bloco de texto "About Activity" fecha a tela (img 0233).
- As duas capturas mostram duas abordagens para apresentar dados: um único gráfico de linha detalhado, com período selecionável (img 0232), contra três gráficos de barra menores e paralelos, cada um com escala própria, que resumem métricas diferentes do mesmo dia na mesma tela (img 0233).
<!-- /visual:charting-data -->

## Collaboration and sharing (slug: collaboration-and-sharing)

O que governa: como oferecer compartilhamento e colaboração em tempo real usando as interfaces do sistema (share sheet, popover de compartilhamento, botão de colaboração) e a integração com Messages.

Por que: a Apple quer que colaborar pareça uma extensão natural do sistema, não um recurso isolado do app. O raciocínio é reduzir fricção na configuração (permissões simples, resumidas em frases) e manter as pessoas cientes, via o botão de colaboração e notificações no Messages, de que o conteúdo é compartilhado e de quem está envolvido.

Faça e evite:
- Coloque o botão Share num local conveniente, como uma toolbar, para facilitar o início do compartilhamento.
- Customize a share sheet ou o popover de compartilhamento só se necessário, para oferecer os tipos de compartilhamento de arquivo que o app suporta.
- Escreva frases sucintas que resumem as permissões de compartilhamento, como "Only invited people can edit" ou "Everyone can make changes".
- Ofereça um conjunto simples de opções de compartilhamento; mantenha o número de escolhas customizadas ao mínimo e agrupe-as de forma clara.
- Exiba o botão Collaboration com destaque assim que a colaboração começa, tipicamente ao lado do botão Share.
- Ofereça ações customizadas no popover de colaboração só se necessário; a seção do meio é para itens customizados, sem sobrecarregar de informação.
- Customize o título do botão de gerenciamento de colaboração da modal view se fizer sentido no app (padrão é "Manage Shared File").
- Considere postar notificações de eventos de colaboração no Messages, incluindo um universal link para a view relevante no app.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- iOS, iPadOS, macOS: sem considerações adicionais além das gerais. A partir do iOS 16, a share sheet do sistema inclui formas de escolher método de compartilhamento de arquivo e definir permissões; iPadOS 16 e macOS 13 trazem aparência e funcionalidade semelhantes no popover de compartilhamento.
- tvOS: recurso não disponível.
- visionOS: por padrão, o sistema suporta compartilhamento de tela para um app rodando no Shared Space, transmitindo a janela atual para outros colaboradores; se alguém transiciona o app para um Full Space durante o compartilhamento, o sistema pausa o stream para as outras pessoas até o app voltar ao Shared Space.
- watchOS: em app SwiftUI, use ShareLink para apresentar a share sheet do sistema.

Ligações com outros artigos: Activity views; SharePlay (para atividades em tempo real entre dispositivos); Managing accounts (relacionado a autenticação e permissões, mencionado indiretamente).

<!-- visual:collaboration-and-sharing -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações (img 0246 a 0251) vistas, códigos conferidos; a página não tem vídeo.
- A abertura mostra um círculo de traço grosso vermelho escuro, aberto de um lado, com um ícone de pessoa dentro e um círculo menor preenchido com check branco sobreposto na base, sobre degradê laranja com grade tracejada e círculo guia (img 0246).
- As cinco capturas reaproveitam o mesmo documento do app de notas no iOS, "Nature Walks", com o mesmo desenho de folha e anotações manuscritas, e mudam apenas os controles sobrepostos; o foco didático fica nos elementos de interface, não no conteúdo (img 0247 a img 0251).
- O botão Share fica no canto superior direito, ao lado do botão "...", numa barra superior que também traz a seta de voltar, com o título grande abaixo (img 0247).
- A share sheet abre abaixo do título com, na ordem, um seletor "Collaborate" acompanhado da frase de permissão e de uma seta de disclosure, quatro avatares de colaboradores com iniciais e ponto verde de status, e duas fileiras de quatro ações cada: AirDrop, Messages, Mail e Reminders; Copy, Export as Markdown, Markup e More (img 0248).
- A frase de permissão é ensinada por um par com layout idêntico, mesmos avatares e mesmas ações, trocando só o resumo no mesmo lugar acima dos avatares: "Only invited people can edit." e depois "Everyone can make changes." (img 0248 e img 0249).
- Com a colaboração ativa, surge na barra superior um botão circular laranja com ícone de duas pessoas, à esquerda do Share e do "...", com destaque proeminente como o do Share (img 0250).
- O popover desse botão se organiza em três blocos verticais: no topo, abas de mensagem, vídeo e áudio, com mensagem selecionada em laranja; no meio, "Latest Updates" e "Current Participants" com textos de estado vazio; embaixo, um toggle verde ligado para "Participant Cursors" e itens de lista com ícone à direita, "Show All Activity", "Show Highlights" e "Manage Shared Note" (img 0251).
<!-- /visual:collaboration-and-sharing -->

## Drag and drop (slug: drag-and-drop)

O que governa: como implementar arrastar e soltar (mover ou copiar seleções de fotos, texto e outro conteúdo) entre origem (source) e destino (destination), no mesmo container, em containers diferentes ou entre apps.

Por que: a lógica de mover versus copiar segue o que as pessoas já esperam do mundo físico e de outros sistemas: mesmo container tende a mover, containers diferentes tendem a copiar, e entre apps sempre copia. Feedback contínuo durante o arraste existe para que a pessoa se sinta no controle de um processo com múltiplos desfechos possíveis.

Faça e evite:
- Suporte drag and drop o máximo possível pelo app; componentes do sistema (campos e views de texto) já trazem suporte embutido.
- Ofereça formas alternativas de realizar a mesma ação (comandos de menu) quando o drag and drop for inconveniente ou impossível; em iOS/iPadOS use APIs de acessibilidade para permitir drag and drop via tecnologias assistivas.
- Decida mover vs. copiar de acordo com o que a maioria espera: mesmo container tende a mover, containers diferentes tendem a copiar; prefira o comportamento menos propenso a frustração ou perda de dados.
- Suporte arraste de múltiplos itens quando fizer sentido; em iPadOS a pessoa pode adicionar itens ao grupo sem parar o arraste.
- Prefira permitir desfazer uma operação de drag and drop; peça confirmação antes de completar operações que não podem ser desfeitas (exemplo: Finder pede confirmação ao arrastar arquivo para uma pasta somente-gravação).
- Considere oferecer múltiplas versões do conteúdo arrastado, da maior para a menor fidelidade, para que o destino escolha a melhor versão que aceita.
- Considere suportar spring loading, que permite ativar controles (botões, segmented controls) arrastando o conteúdo selecionado sobre eles.
- Mostre uma imagem de arraste translúcida assim que a pessoa arrasta a seleção por cerca de 3 pontos; mantenha até o drop.
- Modifique a imagem de arraste para prever o resultado, se ajudar a clareza; use drag flocking para agrupar visualmente múltiplos itens arrastados.
- Mostre se um destino pode aceitar o conteúdo arrastado (insertion point, destaque, ou símbolo "não permitido" como `circle.slash` do SF Symbols); remova o feedback quando o conteúdo se afasta do destino.
- Ao falhar o drop ou cair em destino inválido, dê feedback visual (voltar à origem, ou escala/fade sugerindo evaporação).
- Ao aceitar drops: role o conteúdo do destino automaticamente quando necessário; escolha a versão mais rica do conteúdo que o app aceita; extraia só a parte relevante do conteúdo (exemplo: Mail extrai só nome e email de um contato arrastado); verifique a tecla Option no momento do drop (força o comportamento de cópia dentro do mesmo container); dê feedback quando a transferência do conteúdo solto demorar; dê feedback quando o drop inicia uma tarefa (como impressão); aplique o estilo correto ao texto solto (mantendo fonte/estilo original quando ambos suportam, ou aplicando o estilo do destino); mantenha o estado de seleção do conteúdo no destino após o drop, atualizando a origem conforme necessário.

Especificações exatas: exibir a imagem de arraste assim que a pessoa arrasta a seleção por cerca de 3 points.

Diferenças por plataforma:
- Não suportado em tvOS nem watchOS.
- iOS, iPadOS: permita múltiplas atividades de arraste simultâneas; em iPadOS a pessoa pode selecionar um ícone de app, começar a arrastar e selecionar ícones adicionais antes de soltar todos numa Home Screen diferente ou numa pasta, exigindo suporte a adicionar itens durante o arraste (com flocking) e aceitar múltiplos drops simultâneos.
- macOS: considere permitir arrastar conteúdo do app para o Finder, num formato que o app possa reabrir depois (exemplo: Calendar arrasta evento como arquivo `.ics`); é possível usar um clipping (container temporário) para conteúdo arrastado, que não tem relação com o Clipboard; permita arrastar uma seleção em janela inativa (background selection) sem trazer a janela para frente; ao possível, permita arrastar itens individuais de janela inativa sem afetar a seleção em background existente; considere exibir um badge (oval preenchido com número) durante operações de arraste multi-item; considere mudar a aparência do ponteiro (cópia, drag link, item desaparecendo, operação não permitida) conforme a situação; ao máximo, permita selecionar e arrastar com um único movimento.
- visionOS: quando possível, lance o app para tratar conteúdo solto no espaço vazio, associando uma user activity ao conteúdo arrastável (exemplo: soltar uma URL no espaço vazio abre o Safari; conteúdo suportado por Quick Look abre o Quick Look).

Ligações com outros artigos: Universal Control (arrastar conteúdo entre Mac e iPad); Pointers (aparência do ponteiro no macOS).

<!-- visual:drag-and-drop -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações (img 0470) e 2 folhas de vídeo (vídeo 008) vistas, códigos conferidos.
- A abertura resume o gesto com duas formas e um cursor, sem texto: dois retângulos arredondados do mesmo tamanho parcialmente sobrepostos e uma seta de ponteiro grande na parte inferior direita da composição, apontando para cima e para a esquerda, para dentro do par, sobre degradê laranja com grade pontilhada e círculo guia (img 0470).
- No vídeo 008 (folha 0001, q001 a q003), o ponto de partida no visionOS é uma janela do Files com a lista Recents mostrando o arquivo "meteor.usdz", com tamanho e data, e um menu de contexto aberto ao lado, tudo sobre a sala real ao fundo.
- De q003 para q004 o menu some, a janela passa a mostrar uma grade de miniaturas com botões Select e Search, e o ícone quadrado branco do arquivo aparece cruzando a borda direita do painel.
- Em q005 o ícone já se soltou da janela e flutua sozinho sobre a sala, sem nenhuma moldura de app; ao mesmo tempo a grade de origem passa a exibir só três arquivos, sem o meteor.
- De q005 a q008 o ícone percorre o ar de forma contínua, vai para perto do braço do sofá, desce em direção ao centro da mesa e se estabiliza logo acima do tampo; em q009 ganha o rótulo "meteor" e um pequeno indicador azul, o que sugere que o sistema reconheceu o ponto de soltura.
- Na folha 0002, o arquivo pousa primeiro como cartão plano rotulado sobre a mesa (q010); em seguida um objeto 3D rochoso nasce pequeno acima dele (q011) e cresce ganhando crateras e textura (q012).
- De q013 a q015 o meteoro fica flutuando acima da mesa, sem se apoiar nela, e gira devagar mostrando outras faces, enquanto rótulo e indicador continuam visíveis no tampo abaixo.
Divergências registradas: o texto alternativo da img 0470 fala em uma seta apontando para o canto superior esquerdo, mas o traço mostra um cursor de mouse, não uma seta de direção separada. A descrição oficial do vídeo 008 confere no essencial, mas não menciona o menu de contexto antes do arraste (q001 a q003), a etapa do cartão plano rotulado antes do objeto 3D (q009 a q010) nem a rotação contínua do meteoro no final (q013 a q015).
<!-- /visual:drag-and-drop -->

## Entering data (slug: entering-data)

O que governa: como projetar a entrada de dados para reduzir tédio e erro, seja pré-preenchendo informação já disponível no sistema, seja suportando todos os métodos de input disponíveis.

Por que: entrar dados é tedioso independente do método; a Apple prioriza minimizar o volume de dados que a pessoa precisa fornecer manualmente e validar cedo para evitar a frustração de corrigir erros só no fim de um formulário longo.

Faça e evite:
- Obtenha informação do sistema sempre que possível (configurações, permissão de localização, calendário) em vez de pedir para a pessoa digitar.
- Seja claro sobre o dado necessário, usando um prompt no campo (como "username@company.com") ou um label introdutório ("Email"); pode pré-preencher com valores padrão razoáveis.
- Use um campo de texto seguro quando apropriado, para dados sensíveis, tipicamente exibindo um pequeno círculo preenchido por caractere digitado.
- Nunca pré-preencha um campo de senha; sempre peça para a pessoa digitar ou use autenticação biométrica ou do keychain.
- Quando possível, ofereça escolhas (picker, menu, componente de seleção) em vez de exigir digitação de texto.
- Deixe a pessoa fornecer dados arrastando/soltando ou colando, quando fizer sentido.
- Valide dinamicamente os valores dos campos assim que a pessoa os insere, dando feedback assim que detecta um problema; para dados numéricos, considere um number formatter que aceita só valores numéricos e pode formatar (casas decimais, porcentagem, moeda).
- Quando a entrada de dados é necessária, deixe claro que a pessoa deve preencher o obrigatório antes de prosseguir (por exemplo, desabilitando um botão Next ou Continue até os campos serem preenchidos).

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- iOS, iPadOS, tvOS, visionOS, watchOS: sem considerações adicionais.
- tvOS: pode configurar uma digit entry view para ocultar os numerais digitados (`isSecureDigitEntry`). Em visionOS, quando usa o campo de texto do sistema, o sistema mostra o dado digitado só para quem está usando o dispositivo, não para outros presentes; um campo de texto seguro embaça automaticamente ao usar AirPlay.
- macOS: considere usar uma expansion tooltip para mostrar a versão completa de texto cortado ou truncado num campo, quando o campo é pequeno demais para exibir o dado inteiro.

Ligações com outros artigos: Managing accounts (nunca pré-preencher senha); Text fields; Virtual keyboards; Keyboards; Offering help (expansion tooltip no macOS/visionOS).

<!-- visual:entering-data -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0472), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura representa a entrada de dados de forma abstrata: um campo de texto retangular de cantos arredondados com três pontos preenchidos dentro, em traço vermelho escuro sobre degradê laranja (img 0472).
- Um lápis inclinado se sobrepõe à quina superior direita do campo, com a ponta tocando o interior, indicando a ação de escrever ou editar (img 0472).
- A composição segue grade pontilhada e círculo guia central: o corpo do campo fica inscrito no círculo, e só o lápis ultrapassa esse limite no alto à direita, o que dá sensação de movimento entrando no campo (img 0472).
<!-- /visual:entering-data -->

## Feedback (slug: feedback)

O que governa: como comunicar status, sucesso/falha, avisos e oportunidades de correção conforme a pessoa interage com o app.

Por que: o princípio central é casar a importância da informação com o nível de interrupção da entrega. Status passivo pode ser passivo na apresentação; um risco de perda de dados precisa interromper, porque a pessoa só tem chance de evitar o problema se for avisada a tempo.

Faça e evite:
- Torne todo feedback acessível, usando múltiplos canais (cor, texto, som, haptics), para alcançar mais pessoas em diferentes contextos (silenciado, olhando para longe, usando VoiceOver).
- Considere integrar feedback de status diretamente na interface, perto dos itens que descreve, em vez de exigir ação ou saída do contexto atual (exemplo: Mail mostra a contagem de mensagens não lidas na toolbar).
- Use alerts para entregar informação crítica e, idealmente, acionável; alerts perdem impacto se usados em excesso ou para informação sem importância.
- Avise quando a pessoa inicia uma tarefa que pode causar perda de dados inesperada e irreversível; não avise quando a perda de dados é o resultado esperado da ação (exemplo: Finder não avisa toda vez que a pessoa joga um arquivo fora).
- Quando fizer sentido, confirme que uma tarefa ou ação significativa foi concluída (exemplo: confirmação de transação Apple Pay bem-sucedida); reserve esse tipo de confirmação para atividades suficientemente importantes, já que as pessoas normalmente esperam que a ação dê certo.
- Mostre quando um comando não pode ser executado e ajude a entender por quê (exemplo: Maps avisa que não pode dar direções entre o mesmo local de origem e destino).

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- iOS, iPadOS, macOS, tvOS, visionOS: sem considerações adicionais.
- watchOS: evite exibir um indicador de progresso indeterminado (como um loading indicator) num app watchOS; um indicador animado pode fazer a pessoa achar que precisa continuar prestando atenção à tela. Prefira garantir que ela receberá uma notificação quando o processo terminar.

Ligações com outros artigos: Playing audio; Playing haptics; Motion; Alerts.

<!-- visual:feedback -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0478), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura é um cartão de cantos arredondados com gradiente laranja, mais claro no alto à esquerda e mais escuro e avermelhado embaixo à direita, sem moldura de aparelho, sem texto e sem elementos de interface (img 0478).
- O conceito é desenhado como um ponteiro de seta vermelho escuro cercado por seis traços curtos em disposição radial, sugerindo a resposta a um clique (img 0478).
- A construção fica exposta: uma malha retangular tracejada ao fundo, aparentemente de três colunas por três linhas, e um círculo tracejado concêntrico ao ponteiro, com o anel de traços centrado exatamente no eixo da seta (img 0478).
<!-- /visual:feedback -->

## File management (slug: file-management)

O que governa: como apps que manipulam documentos e arquivos devem se integrar com a navegação de arquivos do sistema (Finder no Mac, Files em iPhone/iPad/Vision Pro), criar, abrir, salvar e apresentar previews de arquivos.

Por que: a Apple parte do princípio de que as pessoas já têm um modelo mental do sistema de arquivos da plataforma (via Finder ou Files), então um browser de arquivos customizado deve respeitar esse layout básico em vez de reinventá-lo. Para salvar, a filosofia é que o trabalho da pessoa deve estar sempre preservado por padrão, sem exigir uma ação explícita de "salvar".

Faça e evite:
- Use menus do app e atalhos de teclado para criar e abrir documentos; em iPadOS e macOS, ofereça comandos familiares como New e Open; inclua um botão Add (+) para criar novo documento (no macOS, a ação de adicionar vai no menu File).
- Se precisar de um navegador de arquivos customizado, respeite a compreensão da pessoa sobre o sistema de arquivos da plataforma; pode mostrar a parte mais relevante ao abrir (pasta Documents, iCloud, local mais recente), mas permita navegar pelo resto do sistema de arquivos.
- Ajude a pessoa a confiar que o trabalho está sempre preservado, a menos que cancele ou apague; em geral, evite exigir uma ação explícita de salvar, fazendo salvamentos periódicos automáticos enquanto edita e ao fechar o arquivo ou trocar de app.
- Oculte extensões de arquivo por padrão, mas permita que a pessoa opte por vê-las; reflita a escolha atual em todas as interfaces de salvar ou abrir.
- Use um Quick Look viewer para permitir preview de um arquivo mesmo quando o app não consegue abri-lo.
- Considere implementar um Quick Look generator se o app produz tipos de arquivo customizados, para que Finder, Files e Spotlight consigam mostrar previews dos documentos.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- tvOS, visionOS, watchOS: sem considerações adicionais (watchOS e tvOS normalmente não têm interface de navegação de documentos).
- iOS, iPadOS: a partir do iOS 18 e iPadOS 18, apps baseados em documentos podem usar o document launcher do sistema, uma experiência em tela cheia com três partes: um title card (nome do app e dois botões específicos do app), uma imagem de fundo com acessórios opcionais ao redor do title card, e uma sheet com o navegador de arquivos e controles opcionais do app. O botão primário do title card tipicamente cria um novo documento; o secundário pode oferecer opções adicionais (exemplo: Numbers usa "Start Writing" e "Choose a Template"). O fundo deve ser claramente distinto dos acessórios e do title card (cor sólida, gradiente ou padrão), evitando imagens complexas. Cuidado com o posicionamento dos acessórios para manter nome do app e botões visíveis. Use animação com moderação (animações suaves e repetitivas). Um app pode também criar uma file provider app extension para importar, exportar, abrir e mover documentos, mostrando só documentos apropriados ao contexto atual, permitindo escolher destino ao exportar/mover, e evitando toolbar customizada dentro da extensão (que já carrega uma toolbar própria na modal view).
- macOS: prefira o navegador de arquivos padrão (Finder) a um customizado, a menos que haja razão importante para um próprio; um customizado pode incluir "open recent", filtro por critério, seleção múltipla, e customização do título do botão Open (por exemplo, "Insert"). Forneça uma interface de salvar que permita mudar nome, formato e local do arquivo (título padrão "Untitled" até nomear); pode estender o diálogo Save com uma accessory view de opções específicas do app. Pode criar uma Finder Sync app extension para expressar status e controle de sincronização dentro do Finder (badges, itens de menu contextual, botões de toolbar para sincronização global). Ajude a evitar perda de trabalho se a pessoa desligar o autosave (opção "Ask to keep changes when closing documents" em Desktop & Dock settings): mostre que o documento tem mudanças não salvas e apresente um diálogo de salvar ao fechar, sair do app, deslogar ou reiniciar; use um ponto no botão de fechar da janela do documento e ao lado do nome no menu Window quando autosave está desligado (não mostrar quando autosave está ligado); pode adicionar "Edited" ao título na title bar, removendo assim que o autosave ocorrer ou a pessoa salvar explicitamente.

Ligações com outros artigos: Toolbars; File menu; Printing; Documents, SwiftUI (documentação de desenvolvedor).

<!-- visual:file-management -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações (img 0479 e img 0480) vista, código conferido; a página não tem vídeo.
- A abertura é um documento com o canto superior direito dobrado para dentro, em contorno vermelho escuro grosso e sem preenchimento, centrado no cruzamento das guias e inscrito no círculo tracejado, sobre o cartão laranja com grade retangular e circular (img 0479).
- O document launcher no iPad em paisagem ocupa a tela em duas partes: em cima, um cartão de título com fundo próprio em gradiente lilás e formas orgânicas; embaixo, uma sheet com o navegador de arquivos (img 0480).
- Os acessórios ficam nas laterais do título: um mascote robô à esquerda e um ramo de flores estilizadas à direita, com o nome do app em tipografia grande preta ao centro (img 0480).
- A ação primária é um botão azul sólido, "Start Writing", logo abaixo do nome do app, destacado contra o fundo ilustrado (img 0480).
- A sheet usa fundo branco neutro e controles padrão: abas de texto Recents, Shared e Browse, com Browse selecionada em azul, ícones de visualização, pasta, grade e busca no canto superior direito, o nome do app repetido no cabeçalho com um chevron e "+ Create Document" como único item da lista (img 0480).
- A tela separa em camadas o que é marca do app (fundo ilustrado, mascote, título e botão primário) do que é controle padrão do sistema (navegador de arquivos neutro na parte de baixo) (img 0480).
<!-- /visual:file-management -->

## Going full screen (slug: going-full-screen)

O que governa: como e quando oferecer modo de tela cheia em iPhone, iPad e Mac, expandindo uma janela para ocupar toda a tela e oferecer um ambiente sem distrações.

Por que: o modo de tela cheia serve concentração e imersão (jogos, mídia, tarefas complexas). O princípio de fundo é preservar acesso essencial: mesmo em tela cheia, a pessoa não deve perder acesso a controles necessários nem sentir que perdeu o controle sobre quando sair do modo.

Faça e evite:
- Suporte modo de tela cheia quando fizer sentido: jogos, visualização de mídia (vídeos, slideshows de fotos), ou tarefas aprofundadas que se beneficiam de ambiente sem distrações.
- Se necessário, ajuste o layout no modo de tela cheia, mas não redimensione a janela programaticamente; mantenha conteúdo essencial em destaque e ajustes sutis o bastante para não causar transições visualmente bruscas.
- Continue dando acesso a recursos e controles essenciais para que a tarefa possa ser concluída sem sair da tela cheia (exemplo: uma experiência de mídia em tela cheia precisa manter controles de playback persistentemente disponíveis ou fáceis de revelar).
- Exceto em jogos, permita revelar o Dock enquanto o app iPadOS ou macOS está em tela cheia; para prevenir revelação acidental durante um jogo, pode pedir ao iPadOS para ignorar um swipe inicial da borda inferior, ou ocultar o Dock inteiramente no macOS.
- Depois que a pessoa troca de app e volta, ajude a retomar de onde parou (por exemplo, um jogo ou slideshow deve pausar automaticamente ao sair).
- Deixe a pessoa escolher quando sair do modo de tela cheia; não espere que ele termine automaticamente ao trocar de app ou terminar uma atividade absorvente.
- Priorize o conteúdo ocultando temporariamente toolbars e controles de navegação; permita restaurar os elementos ocultos com um gesto familiar (tocar, deslizar para baixo, ou mover o cursor até o topo); mantenha controles visíveis quando forem essenciais para navegação ou tarefas.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- Não suportado em tvOS, visionOS ou watchOS (Apple TV e Apple Watch já preenchem a tela por padrão; Apple Vision Pro não tem modo de tela cheia porque a pessoa pode expandir a janela ou usar a Digital Crown para uma experiência mais imersiva).
- iOS, iPadOS: considere adiar (defer) gestos do sistema para evitar saídas acidentais; por padrão, o indicador da Home Screen esconde-se pouco depois de trocar para o app e reaparece ao interagir com a parte inferior da tela, permitindo um swipe para sair; se isso resultar em saídas inesperadas, é possível habilitar dois swipes em vez de um.
- macOS: use a experiência de tela cheia fornecida pelo sistema (garante compatibilidade com, por exemplo, a área do camera housing de alguns modelos de Mac). Num jogo, não mude o modo de exibição ao entrar em tela cheia (a pessoa espera controlar o modo de exibição). Sempre deixe a pessoa escolher quando entrar em tela cheia, preferindo o botão Enter Full Screen da janela, o item do menu View, ou o atalho Control-Command-F; evite um menu customizado de modos de janela; num jogo, pode oferecer um toggle customizado que liga e desliga a tela cheia.

Ligações com outros artigos: Layout; Multitasking; Windows; The menu bar; Immersive experiences (visionOS).

<!-- visual:going-full-screen -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0536), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura é um cartão em gradiente que vai do amarelo alaranjado, à esquerda, ao laranja avermelhado, à direita, com a grade retangular e circular de construção sobreposta (img 0536).
- A ideia de expansão é desenhada com duas setas vermelhas grossas apontando para fora em sentidos opostos: a de cima à esquerda aponta para cima e para a esquerda, a de baixo à direita aponta para baixo e para a direita (img 0536).
- As duas setas ficam na mesma diagonal, do canto superior esquerdo ao inferior direito, e essa linha cruza o centro do círculo guia (img 0536).
Divergências registradas: o texto alternativo oficial descreve as setas numa linha vertical, mas na imagem a linha que as une é claramente diagonal.
<!-- /visual:going-full-screen -->

## Launching (slug: launching)

O que governa: como projetar o início do app ou jogo, desde o toque de abertura até a primeira tela pronta, incluindo o launch screen quando exigido pela plataforma.

Por que: a filosofia central é que lançar precisa ser instantâneo e imperceptível. O launch screen não é um momento de expressão de marca; sua única função é reforçar a percepção de rapidez, então ele deve ser quase idêntico à primeira tela real, para não criar um flash desagradável na transição.

Faça e evite:
- Lance instantaneamente; as pessoas às vezes não querem esperar mais que poucos segundos.
- Se a plataforma exigir, forneça um launch screen (iOS, iPadOS, tvOS); macOS, visionOS e watchOS não exigem.
- Se precisar de um splash screen, considere exibi-lo no início do fluxo de onboarding, ou logo após o lançamento terminar se não houver onboarding.
- Restaure o estado anterior ao reiniciar o app, para a pessoa continuar de onde parou; restaure detalhes granulares o máximo possível (posição de scroll, estado e localização das janelas).
- Para o launch screen: não faça parte de um onboarding nem de um splash screen, e não é oportunidade de expressão artística; desenhe-o quase idêntico à primeira tela real (mesma cor sólida se aplicável, mesma orientação e modo de aparência atuais do dispositivo); evite incluir texto, já que o conteúdo do launch screen não muda e não é localizado; não faça propaganda, evitando parecer splash screen ou janela "Sobre", sem logos ou elementos de marca a menos que sejam parte fixa da primeira tela.

Especificações exatas: o texto não traz números, medidas ou proporções específicas (apenas "não mais do que poucos segundos", sem valor exato).

Diferenças por plataforma:
- macOS, watchOS: sem considerações adicionais (não exigem launch screen).
- iOS, iPadOS: lance na orientação apropriada; se o app suporta retrato e paisagem, lance na orientação atual do dispositivo; se a interface roda só numa orientação, lance nessa orientação e deixe a pessoa girar o dispositivo se necessário; interfaces landscape-only precisam responder corretamente independente de a pessoa girar para a esquerda ou direita.
- tvOS: ao contrário das layered images usadas em boa parte de um app tvOS, o launch screen é estático; em um app de exibição ao vivo, considere iniciar a reprodução automaticamente pouco depois de abrir o app, após alguns segundos de inatividade.
- visionOS: considere lançar no Shared Space mesmo que o app seja totalmente imersivo, dando mais contexto sobre o app enquanto carrega e permitindo apresentar um controle para abrir a experiência totalmente imersiva.

Ligações com outros artigos: Onboarding; Loading; Layout; Live-viewing apps.

<!-- visual:launching -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0679), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura mostra um quadrado de cantos arredondados com uma seta dentro apontando para o canto superior direito, sugerindo a passagem para um novo estado (img 0679).
- O desenho é feito em vermelho escuro sólido sobre o cartão em degradê laranja, o que dá contraste forte entre a forma e o fundo (img 0679).
- A composição se apoia na grade de linhas pontilhadas retangulares e num círculo de alinhamento central, o mesmo sistema de construção das aberturas de outras seções (img 0679).
Divergências registradas: a descrição oficial fala apenas do tingimento geral em laranja e não registra que o quadrado e a seta são vermelho escuro.
<!-- /visual:launching -->

## Live-viewing apps (slug: live-viewing-apps)

O que governa: como priorizar e apresentar conteúdo ao vivo em apps de TV/streaming, incluindo o guia eletrônico de programação (EPG) e a gravação em nuvem (cloud DVR).

Por que: a premissa é que quem abre um app de exibição ao vivo veio para assistir, então cada decisão de design mira reduzir o intervalo entre abrir o app e ver o conteúdo tocando, e deixar claro, a qualquer momento, que aquele conteúdo é ao vivo (diferente de VOD).

Faça e evite:
- Destaque o conteúdo ao vivo com proeminência e fácil acesso; se estiver na primeira aba, a pessoa não precisa tocar mais de uma vez para começar a assistir.
- Deixe a pessoa tocar uma vez, ou nenhuma, para iniciar o playback (exemplo: um botão Watch Now sobre o conteúdo em destaque, que desaparece e inicia o playback em tela cheia imediatamente).
- Faça o conteúdo ao vivo parecer ao vivo: tocar o conteúdo é a melhor forma, mas também ajuda marcar de alguma maneira (badge, símbolo, sash) numa coleção titulada "Live".
- Considere indicar o progresso do conteúdo ao vivo em reprodução, via barra de progresso ou outro indicador, para a pessoa saber onde vai "aterrissar".
- Dê ações e alternativas de visualização adicionais (gravar, reiniciar, baixar, favoritar), sempre na mesma ordem em todo o app (exemplo: Watch, Start Over, Record, Favorite); se o conteúdo reaparece em outros horários, mostre essa informação.
- Considere usar um content footer para navegar entre canais durante o playback, com tratamento sutil (escurecimento) para manter texto legível; identifique claramente a miniatura do conteúdo tocando agora (badge ou tint na barra de progresso); combine as categorias do footer com as do EPG; projete uma forma simples e previsível de invocar e dispensar o footer (exemplo: se deslizar para cima invoca, deslizar para baixo dispensa).
- Dê feedback visual instantâneo ao trocar de canal, tanto para confirmar o canal certo quanto para dar tempo ao carregamento.
- Combine o áudio com o contexto atual: ao começar a tocar conteúdo ao vivo, o áudio deve continuar mesmo ao navegar em segundo plano, mas parar quando a pessoa sai da aba live.
- No EPG: exiba com destaque a informação atual (programa, canal, horário) e facilite voltar ao playback; torne a navegação sem esforço (paginação, scroll, salto); considere um grupo "My Channels" ou "Favorites"; agrupe conteúdo em categorias familiares (Movies, TV Shows, Kids, Sports, Popular), usando as mesmas categorias no content footer; permita navegar o EPG sem sair do conteúdo atual (picture-in-picture ou reprodução em segundo plano).
- No cloud DVR: permita iniciar/parar gravação a partir do painel de informações; permita agendar gravação de programa futuro numa view com detalhes, com opção de gravar só esse episódio ou todos os futuros; ajude a especificar precisamente o que gravar (episódio atual, só novos episódios, só jogos de times específicos); permita reproduzir e deletar conteúdo, ajustar configurações de gravação; considere oferecer gerenciamento automático de armazenamento, sobrescrevendo o conteúdo mais antigo ou já assistido.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma: nenhuma consideração adicional específica citada além da natureza do artigo (voltado a tvOS/streaming); o texto declara "No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS."

Ligações com outros artigos: Remotes; Playing video.

<!-- visual:live-viewing-apps -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0731), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura desenha um televisor estilizado, um retângulo de cantos bem arredondados com um pequeno pé horizontal embaixo, em vermelho sobre gradiente laranja (img 0731).
- Dentro da tela há um triângulo de play vermelho centralizado, que junta num só ícone a ideia de TV e de reprodução (img 0731).
- A grade tracejada tem linhas horizontais, verticais e diagonais e um círculo guia; ela mostra que o retângulo da TV e o círculo do play compartilham o mesmo centro geométrico e que os cantos do retângulo se alinham aos raios diagonais (img 0731).
<!-- /visual:live-viewing-apps -->

## Loading (slug: loading)

O que governa: como projetar o carregamento de conteúdo (assets, níveis, dados) para que não atrapalhe a experiência, idealmente terminando antes que a pessoa perceba.

Por que: a Apple parte do princípio de que uma tela vazia é interpretada como problema no app; a resposta é sempre mostrar algo (placeholder), manter a pessoa ocupada com outras ações possíveis enquanto carrega em segundo plano, e usar indicadores de progresso apropriados (determinado quando o tempo é conhecido, indeterminado quando não é).

Faça e evite:
- Mostre algo o quanto antes; use texto, gráficos ou animações de placeholder enquanto o conteúdo carrega, substituindo-os conforme os elementos reais ficam disponíveis.
- Deixe a pessoa fazer outras coisas no app enquanto espera o carregamento; carregar em segundo plano dá acesso a outras ações (exemplo: um jogo pode carregar conteúdo enquanto o jogador aprende sobre o próximo nível ou vê um menu).
- Se o carregamento for inevitavelmente longo, dê algo interessante para ver enquanto espera (dicas de jogabilidade, tips, apresentação de novos recursos); calcule o tempo restante o mais precisamente possível.
- Melhore o tempo de instalação e lançamento baixando assets grandes em segundo plano; considere usar o Background Assets framework para agendar downloads (pacotes de nível, modelos 3D, texturas) para logo após a instalação, durante atualizações, ou outros momentos não disruptivos.
- Comunique claramente que o conteúdo está carregando e quanto tempo pode levar; use indicador determinado quando souber a duração, indeterminado quando não souber.
- Para jogos, considere criar uma tela de carregamento customizada com animações e elementos que combinem com o estilo do jogo, em vez dos indicadores padrão.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- iOS, iPadOS, macOS, tvOS, visionOS: sem considerações adicionais.
- watchOS: ao máximo, evite mostrar um indicador de carregamento na experiência watchOS, já que as pessoas esperam interações rápidas; em situações onde o conteúdo precisa de um segundo ou dois para carregar, é melhor mostrar um indicador de carregamento do que uma tela em branco.

Ligações com outros artigos: Launching; Progress indicators; Background Assets (documentação de desenvolvedor).

<!-- visual:loading -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0732), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura é o indicador de atividade giratório clássico: oito traços em forma de cápsula dispostos em raios ao redor de um centro comum, em vermelho sobre gradiente laranja (img 0732).
- Cada traço tem opacidade diferente, do mais escuro e opaco no topo até quase transparente nas posições intermediárias, recurso que sugere rotação numa imagem parada (img 0732).
- A grade de construção explica o posicionamento: o círculo guia passa pelas pontas externas dos oito traços, e as linhas horizontais, verticais e diagonais marcam intervalos angulares iguais de 45 graus (img 0732).
<!-- /visual:loading -->

## Managing accounts (slug: managing-accounts)

O que governa: quando e como pedir que a pessoa crie uma conta, como autenticar (Sign in with Apple, passkeys, biometria), e como suportar a exclusão de contas.

Por que: a regra de ouro é só pedir conta quando a funcionalidade essencial exige; o objetivo declarado é reduzir a barreira de entrada, adiar o compromisso ao máximo e dar confiança e conveniência via Sign in with Apple ou passkeys, evitando que a pessoa precise lembrar múltiplas credenciais.

Faça e evite:
- Peça conta só se a funcionalidade essencial exigir; caso contrário, deixe usar o app ou jogo sem conta.
- Explique os benefícios de criar conta e como se inscrever, com uma descrição breve e amigável na tela de login.
- Adie o login o máximo possível; deixe a pessoa sentir o valor do app antes de pedir compromisso (exemplo: um app de compras pode deixar navegar livremente, pedindo login só na hora da compra).
- Se não usar Sign in with Apple num app iOS, iPadOS, macOS ou visionOS, prefira usar passkey, que elimina a necessidade de criar ou digitar senhas; se ainda precisar de senhas, reforce a segurança com autenticação de dois fatores.
- Sempre identifique o método de autenticação oferecido (por exemplo, um botão "Sign In with Face ID" em vez de um genérico "Sign In").
- Refira-se só aos métodos de autenticação disponíveis no contexto atual (não mencione Face ID num dispositivo que não o oferece).
- Em geral, evite oferecer uma configuração específica do app para opt-in de autenticação biométrica, já que isso é ligado no nível do sistema.
- Evite usar o termo "passcode" para se referir a autenticação de conta, para não confundir com o passcode de desbloqueio do dispositivo.
- Sobre exclusão de contas: se ajuda a criar conta no app, também deve ajudar a deletá-la, não só desativá-la, respeitando os requisitos legais regionais sobre exclusão e direito ao esquecimento; se exigências legais obrigam a manter contas ou informações (como registros de saúde digitais) ou seguir um processo específico, descreva claramente a situação. Forneça uma forma clara de iniciar a exclusão dentro do app; se não for possível fazer a exclusão no app, forneça um link direto para a página web onde é possível fazê-lo, e torne o link fácil de encontrar (não enterrado em Privacy Policy ou Terms of Service). Se usou Sign in with Apple para criar a conta, revogue os tokens associados ao deletar. Ofereça uma experiência de exclusão consistente, seja no app ou no site, evitando um fluxo mais longo ou complicado que o outro. Considere permitir agendar a exclusão para o futuro, mas ofereça também opção de exclusão imediata. Diga quando a exclusão vai se completar e notifique quando terminar. Se suporta compras no app, ajude a entender como funcionam cobrança e cancelamento ao deletar a conta (a cobrança de uma assinatura auto-renovável continua pela Apple até a pessoa cancelá-la, independente de deletar a conta; após deletar, a pessoa precisa cancelar a assinatura ou pedir reembolso); mesmo que a pessoa não tenha comprado a assinatura pelo app, ainda é preciso suportar a exclusão de conta.
- Sobre contas de provedores de TV: muitos provedores populares permitem login no nível do sistema, eliminando autenticação app por app; use TV Provider Authentication para o onboarding mais eficiente; evite mostrar opção de logout quando a pessoa está logada no nível do sistema; se precisar incluir logout, deve direcionar para Settings > TV Provider; nunca instrua a fazer logout ajustando controles de privacidade (Settings > Privacy não é mecanismo de logout, apenas gerencia quais apps acessam a conta do provedor).

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- iOS, iPadOS, macOS, visionOS: sem considerações adicionais.
- tvOS: a maioria interage via controle remoto, não teclado, então peça o mínimo de informação necessário; prefira permitir que a pessoa use outro dispositivo para se inscrever ou autenticar (ao configurar associated domains, o Apple TV pode sugerir credenciais com segurança, incluindo Sign in with Apple); quando logada numa conta compartilhada, evite pedir para escolher o perfil toda vez que se torna o usuário atual (no tvOS 16+, o app pode compartilhar credenciais entre usuários mantendo perfil e dados individuais separados); minimize entrada de dados, pedindo para visitar um site de outro dispositivo se precisar reunir mais informação; se precisar de email, mostre a tela de teclado de email com lista de endereços recentemente digitados.
- watchOS: use sincronização iCloud para dar acesso ao Keychain, permitindo autofill de usuário e senha e preservação de configurações do app.

Ligações com outros artigos: Onboarding; Sign in with Apple; Helping people manage their subscriptions; Providing help with in-app purchases.

<!-- visual:managing-accounts -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0751), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura representa a conta com um ícone de pessoa, cabeça circular e ombros em meia lua, sobre gradiente laranja (img 0751).
- A pessoa fica dentro de um anel circular grosso em vermelho, vazado e não preenchido, que funciona como moldura de perfil (img 0751).
- A construção usa duas camadas concêntricas: além da grade tracejada horizontal, vertical e diagonal, um círculo guia menor logo dentro do anel marca o raio interno da moldura (img 0751).
<!-- /visual:managing-accounts -->

## Managing notifications (slug: managing-notifications)

O que governa: como pedir permissão, classificar por nível de interrupção e entregar notificações, incluindo integração com Focus e regras para notificações de marketing.

Por que: a lógica central é confiança: o app deve representar com precisão a urgência de cada notificação, porque a pessoa tem várias formas de ajustar como recebe (incluindo desligar tudo), e uma notificação que usa alta urgência para informação de baixa prioridade quebra essa confiança.

Faça e evite:
- É preciso obter permissão antes de enviar qualquer notificação; o sistema deixa a pessoa mudar essa decisão nas configurações, inclusive silenciando todas as notificações (exceto alertas governamentais em alguns locais).
- Identifique os tipos de notificação que o app pode enviar: comunicação direta (chamadas, mensagens) usa communication notifications (via SiriKit intents, permitindo customização por Siri); as demais usam noncommunication notifications, com um nível de interrupção definido pelo sistema para cada uma.
- Construa confiança representando com precisão a urgência de cada notificação.
- Use o nível Time Sensitive só para notificações relevantes no momento presente; ajude a pessoa a entender os benefícios de deixar notificações Time Sensitive atravessarem um Focus ou entrega agendada; a notificação precisa ser sobre um evento acontecendo agora ou dentro de uma hora.
- Não use notificações para conteúdo de marketing ou promocional a menos que a pessoa concorde explicitamente; nunca use o nível Time Sensitive para uma notificação de marketing.
- Peça permissão explícita se quiser enviar notificações promocionais ou de marketing, com uma interface (alerta, modal view) que descreve os tipos de informação e dá forma clara de optar por entrar ou sair.
- Garanta que a pessoa consiga gerenciar as configurações de notificação dentro do app, além do pedido inicial de permissão.

Especificações exatas:
- O sistema define quatro níveis de interrupção para notificações não comunicacionais: Passive (informação para ver com calma), Active (padrão; informação que a pessoa pode gostar de saber quando chega), Time Sensitive (informação que impacta diretamente e exige atenção imediata) e Critical (informação urgente de saúde e segurança, extremamente rara, tipicamente de agências governamentais ou apps de saúde/lar).
- Tabela de comportamento por nível: Passive não sobrepõe entrega agendada, não atravessa Focus, não sobrepõe o interruptor Ring/Silent; Active idem (todos "No"); Time Sensitive sobrepõe entrega agendada (Sim) e atravessa Focus (Sim), mas não sobrepõe Ring/Silent (Não); Critical sobrepõe entrega agendada (Sim), atravessa Focus (Sim) e sobrepõe o interruptor Ring/Silent (Sim).
- Uma notificação Time Sensitive precisa ser sobre um evento que está acontecendo agora ou vai acontecer dentro de uma hora.
- É necessário obter uma entitlement específica para enviar uma notificação Critical, já que ela pode sobrepor o interruptor Ring/Silent e atravessar entrega agendada e Focus.

Diferenças por plataforma:
- iOS, iPadOS, macOS, tvOS, visionOS: sem considerações adicionais.
- watchOS: por padrão, as configurações de notificação que a pessoa usa para apps no iPhone se aplicam aos mesmos apps no Apple Watch; é possível gerenciar essas configurações pelo app Apple Watch no iPhone, ou acessar opções por notificação (como Mute 1 Hour ou Turn off Time Sensitive) deslizando para a esquerda quando a notificação chega no relógio.

Ligações com outros artigos: Privacy; Settings; User Notifications (documentação de desenvolvedor).

<!-- visual:managing-notifications -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0752), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura desenha um sino de notificação só em contorno vermelho grosso, sem preenchimento, sobre gradiente laranja (img 0752).
- O único elemento preenchido é um círculo pequeno sobreposto ao canto superior direito do sino, que serve de ponto de contraste e sugere um indicador de alerta preso ao sino (img 0752).
- O conjunto se assenta sobre a grade de linhas tracejadas e o círculo guia usados nas demais aberturas (img 0752).
<!-- /visual:managing-notifications -->

## Modality (slug: modality)

O que governa: quando e como apresentar conteúdo em modo modal (alertas, sheets, popovers, janelas separadas, experiências em tela cheia) que impede interação com a view pai até uma ação explícita de dispensa.

Por que: a modalidade tira a pessoa do contexto atual e exige uma ação para sair, então ela só deve ser usada quando há um benefício claro: entregar informação crítica, confirmar ou modificar uma ação recente, ajudar numa tarefa distinta e bem delimitada sem perder o contexto anterior, ou oferecer imersão/concentração numa tarefa complexa.

Faça e evite:
- Apresente conteúdo modalmente só quando houver benefício claro para foco ou escolhas que afetam o conteúdo ou dispositivo.
- Mantenha tarefas modais simples, curtas e enxutas; uma tarefa modal complicada faz a pessoa perder a noção da tarefa que suspendeu ao entrar na view modal.
- Evite criar uma experiência modal que pareça "um app dentro do app"; apresentar uma hierarquia de views dentro de uma modal pode confundir sobre como retroceder os passos; se a tarefa modal precisa conter subviews, ofereça um único caminho pela hierarquia e evite botões que possam ser confundidos com o botão de dispensar a modal.
- Considere usar um estilo modal em tela cheia para conteúdo aprofundado ou uma tarefa complexa (vídeos, fotos, câmera, ou tarefas multi-etapa como marcar um documento ou editar uma foto); em visionOS, ao rodar junto de outros apps no Shared Space, essa apresentação preenche uma janela; se a pessoa transiciona o app para um Full Space, pode se tornar uma experiência mais imersiva.
- Sempre dê uma forma óbvia de dispensar uma view modal, seguindo as convenções da plataforma (em iOS, iPadOS e watchOS, tipicamente um botão na toolbar superior ou deslizar para baixo; em macOS e tvOS, um botão na view de conteúdo principal).
- Quando necessário, ajude a evitar perda de dados obtendo confirmação antes de fechar uma view modal que perderia conteúdo gerado pela pessoa; explique a situação e dê formas de resolver (exemplo: em iOS, um action sheet com opção de salvar).
- Facilite identificar a tarefa de uma view modal: dê um título que nomeie a tarefa, ou texto adicional que a descreva ou oriente.
- Deixe a pessoa dispensar uma view modal antes de apresentar outra; várias views modais visíveis ao mesmo tempo criam desordem visual; embora um alert possa aparecer sobre todo o resto (inclusive outras views modais), nunca mostre mais de um alert simultaneamente.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Sheets; Alerts; Popovers; Action sheets; Activity views; Going full screen; Immersive experiences (visionOS).

<!-- visual:modality -->
### O que as ilustrações mostram
Base: 1 folha de ilustrações vista, com uma única imagem (img 0799), código conferido; a página não tem vídeo nem captura de tela de interface.
- A abertura mostra duas janelas retangulares arredondadas sobrepostas: uma atrás e à esquerda, outra maior à frente e à direita, cobrindo parte da primeira (img 0799).
- Só a janela da frente tem barra de título com três pontos no topo, acima de um corpo retangular; a de trás não tem esse detalhe (img 0799).
- As duas janelas usam o mesmo vermelho translúcido sobre o fundo laranja, sem diferença de opacidade, cor ou escurecimento; a hierarquia vem apenas da sobreposição e da barra de título exclusiva da janela frontal (img 0799).
- Uma grade de linhas pontilhadas verticais, horizontais e diagonais radiais, com um círculo guia, cobre toda a composição e marca os eixos usados para desenhar e alinhar as duas janelas (img 0799).
Divergências registradas: a descrição oficial diz que a composição sugere foco na janela da frente, mas a imagem não marca a janela de trás como inativa por opacidade ou cor; o foco se lê só pela sobreposição e pela barra de três pontos.
<!-- /visual:modality -->

## Multitasking (slug: multitasking)

O que governa: como um app deve se comportar quando a pessoa troca para outro app (pausar, salvar contexto, responder a interrupções de áudio, terminar tarefas em segundo plano) e como a multitarefa se manifesta em cada plataforma.

Por que: a premissa é que a pessoa espera multitarefa e pode achar que há algo errado se o app não permitir; como o app nunca sabe quando a multitarefa vai ser iniciada, ele precisa estar sempre pronto para salvar e restaurar contexto, e tratar interrupções (de áudio, por exemplo) da forma que o sistema e outros apps esperam.

Faça e evite:
- Pause atividades que exigem atenção ou participação ativa quando a pessoa troca de app (jogos, apps de mídia), garantindo que nada seja perdido; ao voltar, permita continuar como se nunca tivesse saído.
- Responda suavemente a interrupções de áudio: pause o áudio indefinidamente para interrupções de áudio primário (música, podcasts, audiobooks); abaixe temporariamente o volume ou pause para interrupções curtas (notificações de direção do GPS), retomando volume ou playback original quando a interrupção terminar.
- Termine tarefas iniciadas pela pessoa em segundo plano (download de assets, processamento de vídeo) mesmo que ela troque de app, completando antes de suspender, se a tarefa não precisar de mais input.
- Use notificações com moderação: pode notificar quando uma tarefa importante ou sensível ao tempo termina enquanto o app está suspenso ou em segundo plano; evite notificar para tarefas rotineiras ou secundárias, deixando a pessoa checar ao voltar.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- Não suportado em watchOS.
- iOS: no iPhone, a multitarefa permite usar FaceTime ou assistir vídeo em Picture in Picture enquanto usa outro app.
- iPadOS: é possível ver e interagir com janelas de vários apps diferentes ao mesmo tempo; um único app também pode suportar múltiplas janelas abertas; apps podem ser usados em tela cheia ou em janelas (windowed); em janelas, o comportamento é redimensionável e similar ao macOS, com controles de sistema para configurações comuns de tiling, entrar em tela cheia, minimizar e fechar janelas; o sistema identifica a janela frontal colorindo seus controles de janela e projetando uma sombra sobre as janelas atrás; apps não controlam nem recebem indicação das configurações de multitarefa que a pessoa escolhe; vídeos e chamadas FaceTime também podem tocar em Picture in Picture sobre outro conteúdo, independente de os apps estarem em tela cheia ou em janela.
- macOS: multitarefa é a experiência padrão, já que as pessoas costumam rodar mais de um app por vez, trocando entre janelas e tarefas; o macOS aplica sombras para dar sensação de janelas em camadas na área de trabalho, e outros efeitos visuais para diferenciar estados de janela.
- tvOS: é possível tocar ou navegar conteúdo enquanto também reproduz filmes ou programas em Picture in Picture (onde suportado).
- visionOS: no Apple Vision Pro, é possível rodar múltiplos apps ao mesmo tempo no Shared Space, vendo e trocando entre janelas e volumes; só uma janela fica ativa por vez no Shared Space, tornando-se ativa quando a pessoa olha para ela, enquanto a anterior fica mais translúcida e parece recuar ao longo do eixo z; fechar uma janela de app no Shared Space transiciona o app para segundo plano sem encerrá-lo; quando o app é o Now Playing app, fechar sua janela pausa automaticamente a reprodução de áudio (é possível retomar no Control Center sem abrir a janela); evite interferir no comportamento de multitarefa fornecido pelo sistema (o visionOS aplica uma máscara "feathered" à janela de onde a pessoa desvia o olhar, e mudar a aparência das bordas da janela interfere nesse feedback); não pause a reprodução de vídeo de uma janela quando a pessoa olha para longe dela (como no macOS, a reprodução iniciada numa janela continua enquanto se vê ou realiza tarefa em outra); esteja preparado para situações em que o áudio pode fazer "duck" (abaixar), a menos que o app seja o Now Playing app atual.

Ligações com outros artigos: Layout; Windows; Playing video; Playing audio; Managing notifications.

<!-- visual:multitasking -->
### O que as ilustrações mostram
Base: 2 folhas de ilustrações (img 0801 a 0805) e 2 folhas de vídeo (vídeo 016) vistas, códigos conferidos.
- A abertura já é o próprio layout de split view: duas colunas retangulares idênticas lado a lado, separadas por um espaço fino, dentro de um contorno arredondado maior, sobre a grade geométrica e o círculo guia (img 0801).
- O app switcher do iPhone empilha os cartões dos apps em cascata, levemente sobrepostos, com cantos arredondados e sombra entre eles; o cartão da frente fica mais nítido, os cartões visíveis mostram trechos do conteúdo dos apps (Mail, biblioteca de música com barra "Not Playing", um terceiro cortado à direita) e há ícones de apps recentes na base, sobre fundo desfocado (img 0802).
- A chamada de FaceTime que continua em outro app aparece como uma foto pequena e arredondada da pessoa, flutuando no canto inferior esquerdo por cima do e-mail aberto, e não como painel separado (img 0803).
- O app switcher do iPad em paisagem organiza os apps abertos em grade de duas linhas, três miniaturas em cima e duas embaixo, cada uma com o conteúdo real renderizado, com o Dock abaixo e a hora no topo (img 0804). Comparado ao iPhone, o formato troca a cascata por uma grade (img 0802 e img 0804).
- Com janelas no iPad, a janela da frente, maior e sobreposta, projeta sombra visível sobre a janela do Maps atrás e exibe controles coloridos em bolinhas no canto superior esquerdo; a janela de trás não mostra esses controles coloridos. Ambas flutuam sobre o papel de parede, com o Dock embaixo (img 0805).
- No vídeo 016 (folha 0001, q001 a q009), duas janelas translúcidas convivem lado a lado no visionOS, Notes à esquerda e Settings à direita, cada uma com seu conteúdo e sua barra superior de botões redondos, com as bordas quase encostadas; de q004 a q006 o cenário ao fundo muda de uma estante com plantas para uma parede com violão, e a posição relativa das janelas não se altera.
- Na folha 0002 (q010 a q018), as janelas estão mais próximas; em q012, q016 e q018 surge uma faixa vertical clara e brilhante exatamente na borda esquerda do Settings, na fronteira com o Notes, enquanto nos outros quadros essa borda é uma linha reta comum. A alternância é compatível com o esmaecimento aplicado à borda da janela que perde o foco, um efeito localizado e sutil.
Divergências registradas: nos quadros parados do vídeo 016 não é possível ver qual janela está ativa em cada instante. A troca de cenário ao fundo, de plantas para violão, aparece nos quadros e não consta da descrição oficial.
<!-- /visual:multitasking -->

## Offering help (slug: offering-help)

O que governa: como oferecer ajuda contextual (tips, tooltips) quando a experiência não é totalmente autoexplicativa, incluindo as regras para criar tips com TipKit e tooltips (help tags) em macOS/visionOS.

Por que: a filosofia de base é que a experiência mais eficaz é aproximável e intuitiva por conta própria; ajuda contextual é o recurso de reserva, e deve estar diretamente ligada à ação ou tarefa que a pessoa está fazendo agora, fácil de dispensar ou evitar se não for necessária.

Faça e evite:
- Deixe as tarefas do app orientarem os tipos de ajuda necessários: para tarefas simples de um ou dois passos, uma view inline que descreve sucintamente a tarefa; para tarefas complexas ou multi-etapa, considere um tutorial.
- Use linguagem e imagens relevantes e consistentes no conteúdo de ajuda, apropriadas ao contexto atual (por exemplo, não mostrar dicas com controle de jogo num contexto de Siri Remote) e consistentes com os termos da plataforma (não dizer "clicar" num botão de iPhone, nem "tocar" num item de menu de Mac).
- Torne todo o conteúdo de ajuda inclusivo.
- Evite inflar o conteúdo de ajuda explicando como componentes ou padrões padrão funcionam; descreva a ação ou tarefa específica que um elemento padrão realiza no seu app; se o app introduz um controle único ou espera um uso não padrão de um dispositivo de entrada, oriente rapidamente, preferindo animação ou gráficos a uma descrição longa.
- Sobre tips (TipKit): use o tipo de tip mais apropriado à interface (popover tip para preservar o fluxo de conteúdo; inline tip para garantir que a informação ao redor permaneça visível; annotation-style para apontar a um elemento específico da UI; hint-style quando não relacionado a uma peça específica de UI); use tips para recursos simples, fáceis de descrever e completar em poucos passos (se um recurso exige mais de três ações, é provavelmente complicado demais para um tip); torne os tips curtos, acionáveis e envolventes, com linguagem direta e orientada à ação, limitados a uma ou duas frases, evitando conteúdo promocional ou relacionado a outro recurso; defina regras de elegibilidade (baseadas em parâmetro ou evento) para os tips alcançarem o público certo, exibindo só quando a pessoa pode se beneficiar; quando há mais de um tip, defina a frequência de exibição para uma cadência razoável (por exemplo, uma vez a cada 24 horas); se há imagem ou símbolo associado ao recurso, considere incluí-lo no tip, preferindo a variante preenchida (filled); se o recurso já é representado por uma imagem à qual o tip se conecta diretamente, evite repetir a mesma imagem no tip e na UI; use botões para direcionar a configurações ou mais informação relacionada ao recurso.

Especificações exatas:
- Se um recurso exige mais de três ações, é provavelmente complicado demais para um tip.
- Considere definir a frequência de exibição de tips, por exemplo, uma vez a cada 24 horas.
- Em macOS/visionOS, limite o conteúdo do tooltip a no máximo 60 a 75 caracteres (a localização costuma mudar o comprimento do texto).

Diferenças por plataforma:
- iOS, iPadOS, tvOS, watchOS: sem considerações adicionais.
- macOS, visionOS: um tooltip (chamado help tag na documentação do usuário) exibe uma view pequena e transitória que descreve brevemente como usar um componente; em apps rodando no Mac (incluindo apps de iPhone e iPad), tooltips aparecem quando a pessoa segura o ponteiro sobre um elemento; em apps visionOS, um tooltip pode aparecer quando a pessoa olha para um elemento ou segura o ponteiro sobre ele. Descreva só o controle pelo qual a pessoa demonstrou interesse; explique a ação ou tarefa que o controle inicia (frequentemente começando com um verbo, como "Restore default settings"); em geral, evite repetir o nome do controle no tooltip; seja breve, limitando a 60-75 caracteres (considerando fragmentos de frase e omissão de artigos); use sentence case (mais casual e aproximável), omitindo pontuação final a menos que exigida pelo estilo do app; considere oferecer tooltips sensíveis ao contexto, com texto diferente para diferentes estados do controle.

Ligações com outros artigos: Onboarding; Feedback; Writing; Help menu; TipKit (documentação de desenvolvedor).

<!-- visual:offering-help -->
### O que as ilustrações mostram
Base: 3 de 3 folhas de ilustrações abertas (img 0813 a 0823), todos os códigos conferidos; sem vídeo.
- A arte de abertura deixa visível a própria construção geométrica do símbolo: um ponto de interrogação dentro de dois círculos concêntricos, atravessado por guias pontilhadas retangulares e radiais que partem do centro, sobre degradê laranja (img 0813).
- O tip tem anatomia fixa em todas as variantes: cartão de cantos arredondados, título em negrito, descrição abaixo, X de fechar no canto superior direito e seta triangular apontando para o elemento relacionado, no exemplo uma estrela azul preenchida (img 0814, 0815, 0816, 0821, 0822).
- No popover, o cartão flutua sobre o conteúdo e o texto de corpo por trás aparece esmaecido, sem ser deslocado (img 0814).
- No annotation, o cartão entra no fluxo da página: há um bloco de texto acima e outro abaixo, e o conteúdo ao redor é empurrado em vez de coberto (img 0815).
- Par errado e certo para o símbolo dentro do tip: estrela azul só em contorno ao lado do título recebe o marcador de X cinza em círculo cinza; estrela azul sólida, na mesma estrutura, recebe o círculo verde com check branco. A folha é uma grade 2x2 com o marcador ao lado de cada variante (img 0817 a 0820).
- Contra a redundância, duas versões quase idênticas do mesmo tip annotation apontando para a estrela na tela: uma repete a estrela ao lado do título, a outra fica só com texto e evita repetir o símbolo (img 0821 e 0822).
- O tooltip do macOS é construído de outro jeito que o tip do iPhone: caixa retangular cinza clara, sem seta, sem título em negrito, uma única linha de texto logo abaixo do ponteiro, parado sobre o botão de voltar de uma janela do Finder com semáforos, título "Documents" e barra lateral de Favorites (img 0823).
Divergências registradas: nas notas, os quadros de Annotation e Hint (img 0815 e 0816) têm a mesma composição, sem diferença construída perceptível além da posição do cartão; a distinção que o texto oficial faz entre os dois tipos não é legível na imagem.
<!-- /visual:offering-help -->

## Onboarding (slug: onboarding)

O que governa: como projetar um fluxo de introdução ao app ou jogo (quando necessário), incluindo splash screens, tutoriais opcionais, tips contextuais e pedidos de permissão durante a introdução.

Por que: o ideal, segundo a Apple, é que a pessoa entenda o app simplesmente experimentando-o; onboarding é uma exceção necessária, não a regra, e quando existe deve ser rápido, divertido e opcional, porque ensinar demais sobrecarrega e reduz retenção. O onboarding só ocorre depois que o lançamento (launching) termina, nunca faz parte dele.

Faça e evite:
- Ensine por interatividade: as pessoas retêm melhor quando realizam a tarefa que estão aprendendo, em vez de só ver material instrucional; ofereça uma experiência interativa onde a pessoa pode testar uma ação, descobrir um recurso ou experimentar uma mecânica de jogo com segurança.
- Considere oferecer uma coleção de tips específicos por contexto, em vez de um único fluxo de onboarding; tips contextuais ajudam a aprender enquanto se progride no app, concentrando-se numa única ação por vez.
- Se precisar de um fluxo de onboarding pré-requisito, projete uma experiência breve e agradável que não exija memorizar muita informação; onboarding rápido e divertido tem mais chance de ser completado; ensinar demais sobrecarrega e reduz retenção.
- Se fizer sentido oferecer um tutorial separado, considere torná-lo opcional; se a pessoa pula no primeiro lançamento, não apresente de novo nos lançamentos seguintes, mas deixe fácil de encontrar depois (numa área de ajuda, conta ou configurações).
- Mantenha o conteúdo do onboarding focado na experiência que o app oferece; a pessoa não precisa aprender a usar o sistema ou o dispositivo ali.
- Exiba um splash screen brevemente se necessário, com um gráfico bonito e comunicação sucinta; exiba só o tempo suficiente para absorver a informação num relance, sem parecer que atrasa a experiência.
- Não deixe downloads grandes atrapalharem o onboarding; considere incluir mídia e conteúdo suficiente no pacote de software para evitar esperas.
- Evite exibir detalhes de licenciamento no fluxo de onboarding; deixe a App Store mostrar acordos e avisos legais; se precisar incluí-los no onboarding, integre de forma equilibrada, sem atrapalhar a experiência.
- Adie fluxos de configuração ou customização não essenciais, oferecendo padrões razoáveis para a maioria começar a interagir sem configuração adicional.
- Se o app precisa de acesso a dados ou recursos privados antes de funcionar, considere integrar o pedido de permissão ao fluxo de onboarding, para mostrar por que precisa e os benefícios de conceder; caso contrário, apresente o pedido quando a pessoa acessa a função específica que depende daquele dado ou recurso.
- Prefira deixar a pessoa experimentar o app antes de pedir avaliações ou compras, já que a resposta tende a ser mais positiva depois de algum engajamento.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Launching; Feedback; Offering help; TipKit; Requesting permission.

<!-- visual:onboarding -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0824), código conferido; sem vídeo e sem versão escura nesta folha.
- O motivo é uma mão de dedos abertos acenando, desenhada em traço contínuo vermelho escuro no estilo de esboço, o que confirma a leitura oficial de boas vindas (img 0824).
- A construção fica exposta: linhas de grade pontilhadas retangulares e um círculo guia centralizado na palma atravessam o desenho, o mesmo padrão de grade de referência visto na arte de offering-help (img 0824).
- O suporte é um retângulo de cantos arredondados com fundo em degradê laranja, no mesmo sistema das outras ilustrações de abertura do HIG: traço vermelho escuro grosso e contínuo e grade de construção retangular e circular visível (img 0824).
<!-- /visual:onboarding -->

## Playing audio (slug: playing-audio)

O que governa: como um app deve tocar áudio respeitando volume do sistema, modo silencioso, roteamento de fones e categorias de sessão de áudio (Solo ambient, Ambient, Playback, Record, Play and record), além do tratamento de interrupções.

Por que: a regra central é que o volume do sistema sempre governa a saída final, e o app só ajusta níveis relativos internos; a escolha da categoria de áudio deve refletir honestamente a natureza do som (essencial ou não, precisa mixar com outros áudios ou não) para atender à expectativa da pessoa sobre silêncio, volume e fones de ouvido.

Faça e evite:
- Ajuste níveis automaticamente quando necessário, mas não ajuste o volume geral; o app pode ajustar níveis relativos e independentes para um bom mix de áudio, mas o volume do sistema sempre governa a saída final.
- Permita reroteamento de áudio quando possível (por exemplo, para um estéreo, rádio do carro ou Apple TV), a menos que haja razão convincente para não permitir.
- Use a volume view fornecida pelo sistema (com slider de nível e controle de reroteamento) para ajustes de áudio; é possível customizar a aparência do slider.
- Escolha uma categoria de áudio que combine com o uso de som do app ou jogo, evitando interromper o áudio de outro app sem necessidade.
- Responda a controles de áudio (Control Center, controles de fone) só quando fizer sentido: é aceitável responder se o app está tocando áudio ativamente, num contexto claramente relacionado a áudio, ou conectado via Bluetooth/AirPlay; caso contrário, evite interromper áudio de outro app ao ativar um controle.
- Evite repropositar controles de áudio; se o app não suporta certos controles, não responda a eles.
- Considere criar controles de player de áudio customizados só se precisar de comandos que o sistema não suporta (incrementos customizados de avanço/retrocesso, ou conteúdo relacionado como placar esportivo).
- Avise outros apps quando o app termina de tocar áudio temporário, sinalizando a sessão de áudio de forma que outros apps saibam quando podem retomar.
- Sobre interrupções: determine como responder a interrupções de sessão de áudio (por exemplo, evitar interromper o áudio atual para uma chamada recebida, a menos que a pessoa escolha atender); ao final de uma interrupção, determine se retoma o playback automaticamente, considerando se a interrupção é retomável (como uma chamada) ou não retomável (como quando a pessoa inicia uma nova playlist).

Especificações exatas:
- Tabela de categorias de áudio (AVAudioSession.Category): Solo ambient (som não essencial mas silencia outros áudios; responde ao interruptor de silêncio; não mixa com outros sons; não toca em segundo plano); Ambient (som não essencial e não silencia outros áudios; responde ao interruptor de silêncio; mixa com outros sons; não toca em segundo plano); Playback (som essencial, pode mixar com outro áudio; não responde ao interruptor de silêncio; pode ou não mixar; pode tocar em segundo plano); Record (som gravado; não responde ao interruptor de silêncio; não mixa; pode gravar em segundo plano); Play and record (som gravado e tocado, possivelmente simultâneo; não responde ao interruptor de silêncio; pode ou não mixar; pode gravar e tocar em segundo plano).
- watchOS: use codificação de 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) para boa qualidade com menor exigência de dados.

Diferenças por plataforma:
- iOS, iPadOS: use os serviços de som do sistema para tocar sons curtos e vibrações (Audio Services).
- macOS: sons de notificação mixam com outro áudio por padrão.
- tvOS: o sistema toca áudio só quando a pessoa o inicia, através de interações em apps e jogos ou calibrações de dispositivo; o tvOS não toca sons para acompanhar componentes como alerts ou notificações.
- visionOS: sons sutis e expressivos estão por toda parte, reforçando experiências e dando feedback essencial ao olhar para um objeto virtual e usar gestos; o sistema combina algoritmos de áudio com informação sobre os arredores físicos da pessoa para produzir Spatial Audio, som percebido como vindo de locais específicos no espaço, não só de alto-falantes; evite comunicar informação importante usando só som; a reprodução de áudio do Now Playing app pausa automaticamente ao fechar a janela do app, e o áudio de um app que não é o Now Playing pode fazer "duck" ao olhar para outro app; prefira tocar som (um app sem som pode parecer sem vida ou até quebrado, especialmente num momento imersivo); projete sons customizados para elementos de UI customizados; use Spatial Audio para uma experiência intuitiva e envolvente, especialmente em contexto totalmente imersivo; considere definir uma variedade de locais de onde os sons do app podem se originar (quando a pessoa move uma janela tocando áudio, o som continua vindo diretamente da janela); considere variar sons que poderiam ser percebidos como repetitivos ao longo do tempo (exemplo: o sistema varia sutilmente o tom e volume dos sons do teclado virtual); decida entre som fixo (fixed, como se apontado para a pessoa, independente da direção que olha) ou rastreado (tracked, percebido como vindo de um objeto específico), exemplo citado: Mindfulness usa som fixo para envolver a pessoa num ambiente pacífico.
- watchOS: o sistema gerencia a reprodução de áudio; um app pode tocar clipes curtos enquanto ativo em primeiro plano, ou áudio mais longo que continua mesmo baixando o pulso ou trocando de app; use os valores de codificação recomendados (64 kbps HE-AAC); considere apresentar uma Now Playing view para controlar áudio atual ou recente sem sair do app, que também mostra informação da fonte atual (podendo ser outro app no Apple Watch ou iPhone) e seleciona automaticamente a fonte atual ou mais recente.

Ligações com outros artigos: Playing video; Feedback; Multitasking (resposta a interrupções de áudio); MusicKit, AVAudioSession (documentação de desenvolvedor).

<!-- visual:playing-audio -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0850), código conferido; sem vídeo.
- O ícone conceitual é um alto falante em traço grosso vermelho escuro, com três ondas sonoras curvas de tamanho crescente saindo para a direita, conforme a descrição oficial (img 0850).
- A grade de construção pontilhada fica visível por cima do desenho, com linhas retangulares e um círculo guia centralizado no corpo do alto falante (img 0850).
- O conjunto repete o sistema das ilustrações de abertura de seção: retângulo de cantos arredondados, grade de construção sobreposta e fundo em degradê tingido na cor temática, aqui laranja (img 0850).
<!-- /visual:playing-audio -->

## Playing haptics (slug: playing-haptics)

O que governa: quando e como usar feedback tátil (haptics) do sistema e customizado, incluindo os padrões definidos por plataforma (notification, impact, selection em iOS; alignment, level change, generic no Magic Trackpad; e o conjunto de haptics do watchOS).

Por que: a lógica de fundo é causalidade clara: cada haptic precisa reforçar uma relação de causa e efeito consistente com a ação que o gera, para que a pessoa aprenda a associar certos padrões a certas experiências; usar o mesmo padrão para desfechos opostos (positivo e negativo) gera confusão.

Faça e evite:
- Use os padrões de haptic do sistema de acordo com seus significados documentados; se o caso de uso documentado não fizer sentido no seu app, use um padrão genérico ou crie o próprio, onde suportado.
- Use haptics de forma consistente por todo o app, construindo uma relação causal clara entre cada haptic e a ação que o provoca.
- Prefira usar haptics para complementar outros feedbacks (visual, auditivo); quando estão em harmonia, a experiência parece mais natural; combine intensidade e nitidez do haptic com a intensidade e nitidez da animação que ele acompanha; é possível sincronizar som com haptics.
- Evite usar haptics em excesso; um haptic pode parecer perfeito ocasionalmente, mas cansativo se tocado com frequência; teste com usuários para achar o equilíbrio (a melhor experiência de haptic é aquela que a pessoa talvez nem perceba conscientemente, mas sente falta quando desligada).
- Na maioria dos apps, prefira haptics curtos que complementam eventos discretos; haptics longos podem melhorar a jogabilidade, mas num app podem diluir o significado do feedback e distrair da tarefa (no Apple Pencil Pro, haptics contínuos ou muito longos não costumam esclarecer a experiência de escrita/desenho e podem tornar segurar o lápis menos agradável).
- Torne os haptics opcionais: deixe a pessoa desligar ou silenciar, garantindo que ainda consiga aproveitar o app ou jogo sem eles.
- Esteja ciente de que tocar haptics pode impactar outras experiências: como produzem força física suficiente para serem sentidos, garanta que não atrapalhem recursos do dispositivo como câmera, giroscópio ou microfone.
- Sobre haptics customizados: use os dois blocos básicos, transient events (breves e compactos, como toques ou impulsos) e continuous events (vibrações sustentadas); é possível controlar nitidez (sharpness) e intensidade de qualquer evento; combine eventos transientes e contínuos, variando nitidez e intensidade, e incluindo áudio opcional, para criar uma ampla gama de experiências hápticas.

Especificações exatas: o texto não traz números, medidas de força ou duração exatas para haptics.

Diferenças por plataforma:
- iOS: em modelos de iPhone suportados, use componentes de UI padrão (toggles, sliders, pickers) que tocam haptics do sistema desenhados pela Apple por padrão; quando fizer sentido, use um feedback generator para tocar um de vários padrões predefinidos nas categorias notification (feedback sobre o desfecho de uma tarefa ou ação, como depositar um cheque ou destravar um veículo), impact (metáfora física para complementar uma experiência visual, como sentir um tap quando uma view se encaixa no lugar ou um thud quando dois objetos pesados colidem) e selection (feedback enquanto os valores de um elemento de UI estão mudando).
- macOS: quando um Magic Trackpad está disponível, o app pode fornecer um dos três padrões de haptic em resposta a uma operação de arraste ou force click: Alignment (indica alinhamento de um item arrastado, como alinhar formas num app de desenho, escalar um objeto, posicionar num local preferido, ou alcançar início/fim de um scrubber de vídeo); Level change (indica movimento entre níveis discretos de pressão, como ao pressionar um botão de avanço rápido num player de vídeo); Generic (feedback geral quando os outros padrões não se aplicam).
- watchOS: Apple Watch Series 4 e posteriores fornece feedback háptico para a Digital Crown, dando uma experiência mais tátil ao rolar conteúdo; por padrão, o sistema fornece detentes hápticos lineares sentidos ao girar a Digital Crown; alguns controles do sistema, como table views, fornecem detentes conforme novos itens entram na tela. O watchOS define um conjunto de haptics, cada um com significado específico: Notification (algo significativo ou fora do comum aconteceu e exige atenção; o sistema toca o mesmo haptic quando chega uma notificação local ou remota); Up (um valor importante aumentou acima de um limiar significativo); Down (um valor importante diminuiu abaixo de um limiar significativo); Success (uma ação completou com sucesso); Failure (uma ação falhou); Retry (uma ação falhou mas pode ser tentada de novo); Start (uma atividade começou, usado ao iniciar um timer ou atividade que a pessoa pode explicitamente iniciar e parar; normalmente seguido pelo haptic Stop); Stop (uma atividade parou, usado ao parar um timer ou outra atividade previamente iniciada); Click (sensação de um dial clicando, comunicando progresso em incrementos ou intervalos predefinidos; usar em excesso diminui a utilidade e pode confundir quando os cliques se sobrepõem).

Ligações com outros artigos: Feedback; Gestures; Core Haptics (documentação de desenvolvedor); Apple Pencil (para haptics no Apple Pencil Pro).

<!-- visual:playing-haptics -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0851) e 18 vídeos de demonstração (017 a 034), uma folha cada, todos abertos com códigos conferidos.
- A arte de abertura usa três círculos de contorno grosso vermelho escuro, ligeiramente sobrepostos numa fileira horizontal, com um núcleo mais denso onde os traços se cruzam; a grade pontilhada retangular e um losango ou círculo guia centralizado ficam visíveis sobre o degradê laranja (img 0851).
- Os vídeos 017 a 025 compartilham uma notação de linha do tempo: linha de base horizontal cinza clara, faixa verde clara com textura tracejada como referência fixa perto do início, pulsos desenhados como barras verticais verdes sólidas cuja altura acompanha a força, e uma guia vertical pontilhada com uma bolinha em cada ponta, que fica na margem esquerda em q001 (0,0 s) e na margem direita em q002 (0,5 s), o que sugere revelação progressiva do padrão; a exceção é o erro, em que a guia já aparece perto do centro esquerda em q001 (vídeos 017 a 025, quadros q001 e q002; vídeo 019).
- Nos padrões de notificação, sucesso termina com duas barras, uma um pouco mais alta que a outra (vídeo 017, q002); aviso também termina com duas barras, de alturas que parecem mais próximas, numa diferença sutil demais para ser afirmada (vídeo 018, q002); erro chega a quatro barras de perfil dentado, com uma barra no meio da sequência claramente mais alta que as vizinhas, irregularidade mais acentuada que em sucesso e aviso, e em q001 já mostra duas faixas hachuradas e duas barras sólidas de alturas bem diferentes (vídeo 019).
- Nos impactos há um único pulso, e a altura da barra cresce na ordem leve, médio e pesado; no pesado ela ocupa quase toda a distância entre a linha de base e o topo útil do quadro (vídeos 020, 021 e 022, q002).
- Rígido tem barra alta, próxima da de pesado, que aparenta estar levemente deslocada para a esquerda; suave tem barra baixa, parecida com a de leve, que parece um pouco mais larga; seleção tem altura moderada e a barra visivelmente mais estreita que todas as de impacto (vídeos 023, 024 e 025, q002).
- Os vídeos 026 a 034 trocam de notação: barras rosa finas e isoladas para pulsos discretos, um leque triangular de linhas verticais azuis e rosa que cresce e depois se estreita para a vibração contínua que decai, e uma cauda de pontos claros; um marcador branco de tempo, linha vertical com bolinhas nas pontas, sai do início, passa pelo pico do leque e chega ao fim da cauda, e em q004 e q005 o desenho completo reaparece com o marcador no fim, o que sugere repetição do ciclo (vídeo 026, quadros q001 a q005).
- A quantidade de pulsos isolados no início é o principal código de identidade entre esses haptics: dois em Notification, Up e Down, três em Success e um só em Start (vídeos 026, 027, 028, 029 e 032).
- Up tem o corpo de vibração azul visivelmente mais alto, longo e denso que o de Notification; Down repete a mesma forma de Up, sem inversão nem diferença visível de proporção (vídeos 026, 027 e 028, q001).
- Stop é construído como duas cópias idênticas do desenho de um pulso, leque e cauda, lado a lado no mesmo quadro, com o marcador entre as duas cópias em q002; em q004 o par reaparece sem marcador visível dentro da moldura recortada (vídeo 033, q001 a q004).
- Failure e Retry abandonam os pulsos separados: um bloco retangular rosa preenchido, com picos internos densos e irregulares, seguido de cauda pontilhada azul curta, sem os intervalos entre pulsos das outras formas (vídeos 030 e 031).
- Click é o desenho mais discreto do conjunto: dentro da barra rosa há só um traço ondulado curto e de baixa amplitude, sem leque de decaimento, seguido de uma linha pontilhada quase reta e longa até o fim do quadro (vídeo 034).
Divergências registradas: o áudio descrito na legenda oficial não é verificável pela imagem (vídeo 017); a diferença de altura entre sucesso e aviso é sutil demais para ser afirmada (vídeo 018); rígido e pesado não se distinguem além da altura semelhante (vídeo 023); Retry não tem marca visual que o separe de Failure, contra a expectativa de formas distintas para significados distintos (vídeo 031); as legendas alternativas de 026 a 034 são genéricas e não citam marcador de tempo, repetição do ciclo nem contagem de pulsos, que só as imagens mostram.
<!-- /visual:playing-haptics -->

## Playing video (slug: playing-video)

O que governa: como usar o player de vídeo do sistema (modos aspect-fill e aspect/fit-to-screen, Picture in Picture), integrar com o app TV, e como as recomendações mudam entre plataformas para telas de carregamento e saída de reprodução.

Por que: a diretriz central é usar o player do sistema para dar uma experiência familiar e consistente; quando um player customizado é realmente necessário, ele deve referenciar o comportamento e a interface do player do sistema, porque um desvio sutil causa frustração já que a pessoa não sabe quais interações habituais ainda funcionam.

Faça e evite:
- Use o player de vídeo do sistema para uma experiência familiar e conveniente; se o app realmente precisa de um player customizado, referencie o comportamento e interface do player do sistema.
- Sempre exiba o conteúdo de vídeo na proporção original; padding embutido (letterbox/pillarbox) no próprio frame do vídeo pode impedir a escala correta do sistema conforme o modo de reprodução, fazendo vídeos aparecerem menores tanto em tela cheia quanto em fit-to-screen, e prevenindo exibição correta em contextos de borda a borda, como Picture in Picture no iPad.
- Forneça informação adicional quando agregar valor (imagem, título, descrição) em iOS, iPadOS, tvOS e visionOS, restringindo para não obscurecer a reprodução da mídia.
- Suporte as interações que a pessoa espera, independente do dispositivo de entrada (por exemplo, pressionar Espaço num teclado conectado para tocar/pausar em Apple Vision Pro, Mac, iPhone, iPad e Apple TV; gestos familiares e intuitivos com o Siri Remote no Apple TV).
- Se a pessoa precisa acessar opções de reprodução ou informação específica do conteúdo no app tvOS, considere adicionar um transport control ou content tab customizado, oferecendo só as ações e informações mais úteis, ajudando a voltar rapidamente à experiência de visualização.
- Evite deixar áudio de fontes diferentes se misturarem ao trocar de modo (por exemplo, entre tela cheia e Picture in Picture); áudio misturado é uma experiência desagradável e frustrante.
- Sobre integração com o app TV: garanta uma transição suave (o app TV escurece para preto na transição e não mostra o launch screen do seu app; mantenha continuidade visual mostrando sua própria tela preta imediatamente antes de começar ou retomar o conteúdo); mostre o conteúdo esperado imediatamente, pulando direto da tela preta para o conteúdo, evitando splash screens, telas de detalhe, animações de introdução ou qualquer barreira; evite perguntar se a pessoa quer retomar a reprodução, retomando automaticamente sem pedir confirmação; toque ou pause a reprodução ao pressionar Espaço num teclado Bluetooth conectado; garanta que o conteúdo toque para o espectador correto (se o app suporta múltiplos perfis, mude automaticamente para o perfil especificado pelo app TV antes de iniciar a reprodução; se o pedido não especifica perfil, peça para escolher antes de começar); use o tempo final anterior ao retomar reprodução de um clipe longo.
- Sobre carregamento de conteúdo: evite exibir telas de carregamento quando possível; se o carregamento levar mais de dois segundos, considere mostrar uma tela de carregamento preta com um spinner de atividade centralizado, sem conteúdo ao redor; inicie a reprodução imediatamente, exibindo a tela de carregamento só até haver conteúdo suficiente carregado, continuando a carregar o resto em segundo plano; minimize o conteúdo da tela de carregamento (branding ou imagens com moderação), mantendo o fundo preto para transição suave.
- Sobre saída da reprodução: mostre uma tela contextualmente relevante, exibindo a detail view do conteúdo que estava sendo assistido, com opção de retomar a reprodução; se não houver detail view, mostre um menu com esse conteúdo ou o menu principal do app; esteja preparado para uma saída imediata, preparando a view de saída assim que possível após receber a notificação de reprodução.

Especificações exatas:
- Modo full-screen (aspect-fill) é o padrão para vídeo wide (2:1 até 2.40:1); o vídeo escala para preencher a tela, podendo ocorrer corte nas bordas.
- Modo fit-to-screen (aspect) é o padrão para vídeo standard (4:3, 16:9 e qualquer coisa até 2:1) e vídeo ultrawide (acima de 2.40:1); o vídeo inteiro fica visível, com letterboxing ou pillarboxing conforme necessário.
- Se o carregamento levar mais de dois segundos, considere mostrar uma tela de carregamento preta com spinner centralizado.
- tvOS: implemente um atraso mínimo de 0,5 segundos para pausar a mídia e exibir um overlay interativo (quizzes, enquetes, check-ins de progresso).
- visionOS: para suportar scrubbing, forneça um conjunto de thumbnails de 160 px de largura cada.
- watchOS: prefira clipes de vídeo curtos, de no máximo 30 segundos.
- watchOS, tabela de codificação recomendada para assets de mídia: codec de vídeo H.264 High Profile; taxa de bits de vídeo 160 kbps a até 30 fps; resolução em tela cheia 208x260 px (retrato); resolução 16:9 320x180 px (paisagem); áudio 64 kbps HE-AAC (os valores de codificação de áudio se aplicam tanto a filmes quanto a assets só de áudio).

Diferenças por plataforma:
- iOS, iPadOS, macOS: sem considerações adicionais.
- tvOS: prefira o conteúdo ao mostrar logos ou overlays não interativos sobre o vídeo; um logo pequeno e discreto ou um cronômetro de contagem regressiva pode ser apropriado, mas evite overlays grandes e distrativos; alguns dispositivos são propensos a retenção de imagem, então é melhor manter overlays curtos e preferir gráficos translúcidos em Standard Dynamic Range (SDR) a conteúdo opaco e brilhante; para overlays interativos (quizzes, enquetes), implemente um atraso mínimo de 0,5 segundos ao pausar a mídia, e dê uma forma clara de dispensar o overlay e retomar a reprodução.
- visionOS: ajude a pessoa a se manter confortável ao reproduzir vídeo, deixando-a escolher quando começar, usando uma janela pequena para reprodução (redimensionável se quiser) e garantindo que consiga ver os arredores durante a reprodução; numa experiência totalmente imersiva, evite deixar conteúdo virtual obscurecer a reprodução ou os transport controls (o sistema posiciona automaticamente o player numa localização previsível que oferece visualização ótima); evite iniciar automaticamente uma experiência de reprodução totalmente imersiva sem aviso; crie uma thumbnail track se quiser suportar scrubbing (thumbnails de 160 px de largura); evite expandir um player de vídeo inline para preencher uma janela (o vídeo inline precisa ser 2D, e o conteúdo da janela deve continuar visível ao redor do player); use um RealityKit video player se precisar tocar vídeo numa view como um splash screen ou view transicional, já que nesses casos a pessoa não precisa de controles de reprodução nem integração do sistema (dimming, view anchoring); o RealityKit video player usa automaticamente a proporção correta para vídeo 2D e 3D e suporta legendas ocultas, além de poder tocar vídeo como efeito especial na superfície de uma view ou objeto customizado.
- watchOS: o sistema gerencia a reprodução de vídeo; apps podem tocar clipes curtos enquanto ativos em primeiro plano; é possível usar um elemento de filme para incorporar clipes inline ou tocar um clipe numa interface separada; prefira clipes curtos de no máximo 30 segundos (clipes longos consomem mais espaço em disco e exigem manter o pulso levantado por mais tempo, causando fadiga); use os tamanhos e valores de codificação recomendados, evitando escalar clipes de vídeo (afeta performance e resulta em aparência inferior); evite criar uma poster image que pareça um controle do sistema; considere criar uma poster image que represente o conteúdo do clipe, ajudando a pessoa a decidir se quer assistir, evitando imagens sem relação com o conteúdo ou que possam ser confundidas com um controle.

Ligações com outros artigos: Playing audio; Feedback; Keyboards; Remotes; AVKit, HTTP Live Streaming (documentação de desenvolvedor).

<!-- visual:playing-video -->
### O que as ilustrações mostram
Base: 2 de 2 folhas de ilustrações abertas (img 0852 a 0859), códigos conferidos; sem vídeo.
- A capa é um botão de play, círculo vermelho escuro com triângulo branco, sobre degradê laranja, atravessado por uma grade tracejada horizontal, vertical e diagonal que forma um X e um círculo concêntrico ao ícone (img 0852).
- Os diagramas repetem a moldura de um iPhone deitado, de contorno cinza na img 0853, e um código de três cores que a legenda nomeia: azul claro para a área segura do AVKit, roxo lilás para o vídeo e rosa para o padding embutido (img 0853, 0855, 0857, 0858, 0859); o retângulo do vídeo traz um ícone de câmera centralizado (img 0853, 0858).
- A legenda que nomeia as três cores só aparece na segunda folha, depois de as cores já terem sido usadas sem explicação nas primeiras ilustrações (img 0857 em relação a 0853 e 0855).
- Vídeo 4:3 sem padding: o retângulo roxo é mais largo que a tela azul e ultrapassa por igual as bordas esquerda e direita do aparelho, sem nenhuma faixa rosa (img 0853).
- O mesmo vídeo 4:3 com padding embutido ganha duas faixas verticais rosa estreitas coladas nas laterais do retângulo roxo, estendidas até as bordas do aparelho (img 0855).
- Certo e errado não são mostrados variando a cena, e sim com selos separados ao lado da ilustração equivalente: círculo verde com check branco para a versão sem padding e círculo cinza com X branco para a versão com padding (img 0854 e 0856, pareados com 0853 e 0855); pelas notas, a legenda da página associa o selo de certo ao vídeo 4:3 em tela cheia (img 0854).
- Vídeo 21:9 sem padding: uma faixa azul clara fina atravessa a largura da tela no topo como área segura, e um retângulo de contorno azul escuro com a câmera no centro ocupa quase toda a tela, do topo à base, mais alto que a área segura (img 0858).
- Vídeo 21:9 com padding: duas faixas horizontais rosa de letterbox acima e abaixo do retângulo de vídeo, entre ele e as bordas do aparelho (img 0859).
- Regra comum às duas folhas: o vídeo extrapola a área segura por igual nas bordas relevantes, laterais no 4:3 e topo e base no 21:9, e o padding sempre surge como faixa fina rosa colada exatamente nessas bordas (img 0853, 0855, 0858, 0859).
<!-- /visual:playing-video -->

## Printing (slug: printing)

O que governa: como integrar a funcionalidade de impressão do sistema em apps iOS, iPadOS, macOS e visionOS, incluindo opções customizadas de impressora e documento no macOS.

Por que: a orientação é discoverability e transparência: colocar a ação de imprimir em locais padrão do sistema, e ocultar ou desabilitar a opção quando não há nada para imprimir ou nenhuma impressora disponível, para não frustrar com um comando que não pode ser executado.

Faça e evite:
- Torne a impressão descobrível, colocando a ação de imprimir em locais padrão do sistema (item Print no menu File de um app macOS; num app iOS ou iPadOS, um botão de toolbar que abre um action sheet); se o app macOS tem toolbar, considere colocar também um botão Print, mas como botão opcional que a pessoa adiciona ao customizar a toolbar.
- Apresente a opção de imprimir só quando for possível; se não há nada na tela para imprimir, ou nenhuma impressora disponível, esmaeça o item Print no menu File (macOS) ou remova a ação Print do action sheet (iOS/iPadOS); se implementar um botão de impressão customizado, esmaeça ou oculte-o quando a impressão não for possível.
- Apresente opções de impressão relevantes (seleção de intervalo de páginas, múltiplas cópias, impressão frente e verso) usando a view fornecida pelo sistema, se fizer sentido e a impressora suportar.
- No macOS, se o app oferece opções específicas que o sistema não oferece, considere criar uma categoria customizada no painel de impressão, com nome único (como o nome do app) e opções que melhorem a experiência de impressão no app (exemplo: Keynote oferece opções específicas de apresentação, como imprimir notas do apresentador, fundos de slide e slides pulados).
- Se o app suporta configurações de página específicas do documento, considere apresentar um diálogo de page setup com configurações raramente alteradas (tamanho de página, orientação, escala); evite implementar recursos que o sistema já oferece (como orientação da página ou impressão em ordem reversa).
- Garanta que interdependências entre opções fiquem claras (exemplo: se impressão frente e verso está disponível, a opção de imprimir em transparências fica indisponível).
- Separe recursos avançados dos recursos frequentemente usados, considerando um disclosure control para ocultar opções avançadas até serem necessárias, rotuladas como "Advanced Options".
- Considere deixar a pessoa pré-visualizar o efeito de uma configuração (exemplo: atualizar uma thumbnail para mostrar o efeito de mudar um controle de tom).
- Considere armazenar configurações modificadas junto com o documento, pelo menos até o documento ser fechado, caso a pessoa queira imprimir de novo.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma:
- Sem considerações adicionais para iOS, iPadOS ou visionOS. Não suportado em tvOS ou watchOS.
- macOS: ver os pontos detalhados acima (categoria customizada no painel de impressão, page setup dialog, interdependências entre opções, disclosure control para opções avançadas, preview de configurações, armazenamento de configurações com o documento).

Ligações com outros artigos: File management; File menu; UIPrintInteractionController, NSDocument (documentação de desenvolvedor).

<!-- visual:printing -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0889), código conferido; sem vídeo.
- O ícone reduz uma impressora vista de frente a formas simples: alça ou abertura superior arredondada, corpo retangular de cantos arredondados, folha saindo pela ranhura frontal com duas linhas horizontais no lugar do texto impresso e um pequeno círculo no canto superior direito como indicador luminoso (img 0889).
- A malha de construção fica visível por trás do desenho: linhas tracejadas retangulares e um círculo concêntrico centrado no corpo da impressora, evidenciando simetria e alinhamento geométrico deliberados (img 0889).
- A silhueta em vermelho escuro fica sobre um degradê de laranja para amarelo alaranjado; o laranja é a tonalidade que a legenda oficial liga às seis cores do logo original da Apple (img 0889).
- O esquema é o mesmo das ilustrações de capa estilizadas de outras páginas citadas nas notas, como pop-up buttons e popovers: silhueta numa cor temática sobre gradiente, com guias de proporção expostas (img 0889).
<!-- /visual:printing -->

## Ratings and reviews (slug: ratings-and-reviews)

O que governa: quando e como pedir avaliações (ratings) e reviews dentro do app, usando o prompt fornecido pelo sistema.

Por que: a premissa é que entregar uma ótima experiência geral é a melhor forma de estimular avaliações positivas, mas o momento do pedido é crucial: pedir cedo demais, antes de a pessoa formar uma opinião sobre o valor do app, pode até gerar feedback negativo.

Faça e evite:
- Peça avaliação só depois que a pessoa demonstrou engajamento com o app ou jogo (por exemplo, ao completar um nível ou uma tarefa significativa); evite pedir no primeiro lançamento ou durante o onboarding, porque a pessoa ainda não teve tempo de formar uma opinião clara, e pode até deixar feedback negativo se sentir que o pedido veio cedo demais.
- Evite interromper a pessoa enquanto realiza uma tarefa ou joga; procure pausas naturais ou pontos de parada onde o pedido de avaliação é menos incômodo.
- Evite insistir com pedidos repetidos, que podem irritar e até influenciar negativamente a opinião sobre o app; considere esperar pelo menos uma ou duas semanas entre pedidos, pedindo de novo depois que a pessoa demonstra engajamento adicional.
- Prefira o prompt fornecido pelo sistema, que verifica feedback anterior e, se não houver, mostra um prompt in-app pedindo avaliação e uma review escrita opcional; a pessoa pode fornecer feedback ou dispensar o prompt com um único toque ou clique, e pode optar por não receber mais esses prompts para todos os apps instalados.
- Avalie o custo-benefício de resetar o resumo de avaliação ao lançar uma nova versão: resetar faz as avaliações refletirem a versão atual, mas resulta em menos avaliações no total, o que pode desencorajar downloads.

Especificações exatas: o sistema limita automaticamente a exibição do prompt a três ocorrências por app dentro de um período de 365 dias.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Ratings, reviews, and responses; RequestReviewAction (StoreKit, documentação de desenvolvedor).

<!-- visual:ratings-and-reviews -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0919 e 0920), código conferido; sem vídeo.
- A capa é uma estrela de cinco pontas em vermelho escuro dividida na vertical: metade esquerda preenchida em tom sólido mais escuro e metade direita só em contorno, deixando ver o laranja do fundo, o que confirma a leitura oficial de uma avaliação parcial (img 0919).
- A estrela é desenhada sobre grade de guias retangulares e um círculo concêntrico, no mesmo sistema de construção das outras capas tingidas (img 0919).
- O pedido de avaliação no macOS é um cartão branco com sombra, organizado de cima para baixo: ícone de app genérico no canto superior esquerdo, feito de linhas concêntricas cinza claro; título em forma de pergunta, "Enjoying App Name?"; texto explicativo secundário; linha divisória; fileira horizontal de cinco estrelas; botão de dispensar na base (img 0920).
- As cinco estrelas aparecem em contorno azul e todas vazias, sem nota escolhida de antemão, ao contrário da nota parcial fixada na capa (img 0920 comparada a 0919).
- Há uma única ação de dispensar, o botão cinza claro "Not Now" em largura total na base, sem botão de confirmar separado, porque tocar numa estrela já é a própria ação (img 0920).
<!-- /visual:ratings-and-reviews -->

## Searching (slug: searching)

O que governa: como oferecer busca dentro de um app (campo de busca, escopo, sugestões, histórico) e como integrar o conteúdo do app à busca de todo o sistema via Spotlight.

Por que: a diretriz de fundo é dar à pessoa um único local claramente identificado para encontrar qualquer coisa que procura no app, personalizando a experiência com o que se sabe sobre como ela interage (buscas recentes, sugestões, completions, correções), sempre equilibrando conveniência com privacidade sobre o histórico de busca.

Faça e evite:
- Se a busca é importante, dê a ela uma posição primária no app ou na view (exemplo: no app Notes, um campo de busca fica na toolbar inferior junto a outras ações importantes; em apps que usam tab bars, como Photos e Apple TV, a busca é uma aba dedicada).
- Procure tornar o conteúdo do app pesquisável através de um único local; para apps com seções claramente distintas, ainda pode ser útil oferecer busca local (exemplo: no app Music do iOS, a busca funciona como filtro na view atual ao buscar entre músicas e álbuns).
- Exiba claramente o escopo atual de uma busca, usando placeholder text descritivo, scope bars e tokens, ou um título que reforce o que está sendo buscado (exemplo: no Mail sempre há referência clara à mailbox que está sendo buscada).
- Forneça sugestões para facilitar a busca, mostrando buscas recentes antes de digitar ou sugestões preditivas enquanto digita, ajudando a buscar mais rápido e digitar menos.
- Leve a privacidade em conta antes de exibir o histórico de busca; a pessoa pode não gostar que seu histórico apareça onde outros possam ver; se exibir, dê uma forma de limpá-lo.
- Sobre busca em todo o sistema (Spotlight): torne o conteúdo do app pesquisável no Spotlight, compartilhando conteúdo indexável com metadados descritivos; defina metadados para tipos de arquivo customizados via um plug-in Spotlight File Importer; use o Spotlight para oferecer capacidades avançadas de busca de arquivo dentro do contexto do app (por exemplo, um botão que inicia instantaneamente uma busca Spotlight baseada na seleção atual); prefira usar as views de abrir e salvar fornecidas pelo sistema, que geralmente incluem um campo de busca embutido para buscar e filtrar todo o sistema; implemente um Quick Look generator se o app produz tipos de arquivo customizados, ajudando Spotlight e outros apps a mostrar previews dos documentos.

Especificações exatas: o texto não traz números, medidas ou proporções específicas.

Diferenças por plataforma: nenhuma consideração adicional para iOS, iPadOS, macOS, tvOS, visionOS ou watchOS.

Ligações com outros artigos: Search fields; Scope bars and tokens; File management; Quick Look; Core Spotlight (documentação de desenvolvedor).

<!-- visual:searching -->
### O que as ilustrações mostram
Base: 1 de 1 folha de ilustrações aberta (img 0994), código conferido; sem vídeo.
- O ícone é uma lupa vermelha com o cabo apontando para a diagonal inferior direita, sobre gradiente laranja (img 0994).
- O aro da lupa é concêntrico ao círculo guia da grade, o que evidencia que foi desenhado sobre a malha circular de referência (img 0994).
- As diagonais da grade coincidem com a inclinação do cabo, e a malha inclui ainda linhas horizontais e verticais (img 0994).
- É a única imagem da página e segue o padrão das capas de outras páginas citadas nas notas, como right-to-left, scroll-views e search-fields: grade geométrica visível e tingimento numa das cores do logo de seis cores, aqui laranja, indicando malha modular comum em vez de desenho à mão livre (img 0994).
<!-- /visual:searching -->

## O que este grupo revela sobre o jeito Apple

1. Urgência é um recurso escasso e regulado por contrato: a Apple define formalmente níveis de interrupção (Passive, Active, Time Sensitive, Critical em `managing-notifications`) e exige entitlement para o nível mais alto, numa lógica que se repete em `feedback` (reservar alerts para o que é realmente crítico) e em `ratings-and-reviews` (nunca pedir avaliação num momento de interrupção da tarefa). O denominador comum é: interromper a pessoa é um crédito que se gasta, não um botão que se aperta.

2. Confiança do sistema é mais importante que a vontade pontual do app: em `managing-notifications`, uma notificação Time Sensitive de marketing é proibida mesmo com consentimento explícito da pessoa; em `managing-accounts`, o app é obrigado a suportar exclusão de conta mesmo quando a assinatura foi comprada fora dele. A plataforma protege a pessoa de decisões do próprio desenvolvedor.

3. "Downplay" e "não é oportunidade de marca" aparecem como princípio recorrente: o launch screen (`launching`) explicitamente não é branding; o loading screen do tvOS (`playing-video`) deve minimizar branding mantendo fundo preto; o splash screen do onboarding (`onboarding`) deve ser breve o bastante para não parecer atraso. A Apple trata os momentos de transição como neutros por design, reservando expressão de marca para o conteúdo real.

4. O componente do sistema é sempre a opção padrão, e o customizado é a exceção justificada: isso aparece quase palavra por palavra em `playing-video` ("use the system video player"), `file-management` ("use the default file browser unless you have an important reason"), `printing` ("evite implementar recursos que o sistema já oferece") e `offering-help` (tooltips do sistema via `help(_:)`). Construir do zero é tratado como risco de quebrar expectativa, não como oportunidade de diferenciação.

5. Perda de dados é a linha vermelha que sempre exige confirmação, mas só quando é inesperada: `drag-and-drop`, `modality` e `feedback` repetem a mesma regra com a mesma exceção, avisar quando a perda é surpreendente e irreversível, mas nunca avisar quando ela é o resultado óbvio e esperado da ação da pessoa (o exemplo do Finder não avisar ao jogar um arquivo fora aparece quase idêntico em `feedback` e é ecoado em `drag-and-drop`).

6. Todo padrão que envolve texto curto tem um teto de caracteres implícito ou explícito: tooltips em macOS/visionOS (`offering-help`) têm limite de 60 a 75 caracteres; tips do TipKit devem caber em uma ou duas frases; frases de permissão de compartilhamento (`collaboration-and-sharing`) são descritas como "succinct phrases". A Apple trata concisão como requisito funcional, não estilístico.

7. Adiar é tratado como boa prática em quase todo fluxo inicial: adiar login o máximo possível (`managing-accounts`), adiar configurações não essenciais no onboarding (`onboarding`), adiar pedidos de avaliação até haver engajamento real (`ratings-and-reviews`), e até usar o Background Assets framework para adiar downloads grandes para depois da instalação (`loading`, `onboarding`). O primeiro contato deve ser desobstruído.

8. Áudio, haptics e vídeo compartilham um mesmo vocabulário de "resposta ao contexto, não redefinição do controle": `playing-audio` diz para não repropositar controles de áudio; `playing-haptics` diz para não redefinir o significado de um padrão de haptic documentado; ambos convergem para a mesma ideia central de `feedback`, que é preservar a relação causal aprendida pela pessoa entre uma ação e sua resposta sensorial.

9. A plataforma trata "ao vivo" (visionOS Shared Space, tvOS live-viewing, chamadas) com regras próprias de continuidade de mídia: em `multitasking`, `playing-video` e `live-viewing-apps`, o comportamento esperado é que áudio e vídeo continuem tocando quando a pessoa olha para outra janela ou navega em paralelo, e só parem quando ela sai deliberadamente do contexto (ver também o "duck" de áudio no visionOS e o Now Playing app).

10. Documentação de desenvolvedor e texto de design andam lado a lado com frequência incomum: quase todo artigo do grupo referencia uma API específica (`SecureField`, `RequestReviewAction`, `AVAudioSession.Category`, `UIFeedbackGenerator`, `NSHapticFeedbackPerformer`, `DocumentGroupLaunchScene`), mostrando que as HIG desse grupo de "Patterns" são escritas para serem implementadas letra por letra, não apenas inspiradas.

11. visionOS é tratado como uma plataforma de exceções recorrentes ao padrão das demais, não como mais uma linha na tabela: em quase todo artigo do grupo (`going-full-screen`, `modality`, `multitasking`, `playing-audio`, `playing-video`, `drag-and-drop`) o visionOS ganha uma seção própria que redefine conceitos centrais (tela cheia, áudio, ativação de janela) em termos espaciais (Shared Space, Full Space, Spatial Audio, tracked vs. fixed sound).

12. watchOS é tratado como a plataforma da economia extrema de atenção e recursos: evita indicadores de carregamento (`loading`, `feedback`), limita clipes de vídeo a 30 segundos (`playing-video`), usa 64 kbps HE-AAC para reduzir dados (`playing-audio`, `playing-video`), e prefere não mostrar rating requests ou processos assíncronos visíveis, sempre em nome de reduzir o tempo que a pessoa precisa manter o pulso levantado ou a atenção no relógio.

## Evidência de leitura

| Arquivo | Linhas lidas | Lido até o fim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/charting-data.md | 45 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/collaboration-and-sharing.md | 51 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/drag-and-drop.md | 73 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/entering-data.md | 41 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/feedback.md | 38 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/file-management.md | 80 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/going-full-screen.md | 49 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/launching.md | 50 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/live-viewing-apps.md | 44 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/loading.md | 39 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/managing-accounts.md | 58 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/managing-notifications.md | 54 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/modality.md | 47 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/multitasking.md | 69 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/offering-help.md | 65 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/onboarding.md | 41 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/playing-audio.md | 75 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/playing-haptics.md | 81 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/playing-video.md | 98 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/printing.md | 31 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/ratings-and-reviews.md | 30 | sim |
| /Users/guilhermelannes/Downloads/apple-design-kb/text/hig/searching.md | 41 | sim |

Todos os 22 arquivos do grupo foram lidos por inteiro com a ferramenta Read, sem truncamento (nenhum arquivo se aproximou do limite da ferramenta) e sem necessidade de leitura em partes. Nenhum artigo do grupo é apenas índice de coleção; todos têm texto próprio completo.
