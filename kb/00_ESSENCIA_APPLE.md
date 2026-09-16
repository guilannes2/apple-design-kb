# Essência Apple: como a Apple pensa, desenha e constrói interfaces

Documento de síntese da base `apple-design-kb/kb`. Consolida os 18 arquivos destilados das Human Interface Guidelines (pasta `kb/hig/`) e os 18 arquivos destilados das transcrições das sessões de design da Apple de 2014 a 2026 (pasta `kb/videos/`). Tudo aqui vem desses 36 arquivos; nada foi acrescentado de memória ou de fonte externa. Citações literais são curtas e aparecem entre aspas; o resto é paráfrase.

Convenções de fonte usadas ao longo do texto:
- `hig/NN` indica o arquivo da pasta `kb/hig/` (por exemplo `hig/02` é `02_foundations-parte-2.md`), seguido do slug do artigo quando útil (por exemplo `hig/02 typography`).
- `vid/NN` indica o arquivo da pasta `kb/videos/`, seguido do id da sessão (por exemplo `vid/04 wwdc2018_803`).
- Quando um número vem de uma fala e não das diretrizes, isso fica dito.
- No capítulo 9 a citação muda de forma, porque a camada visual é indexada por imagem e por folha de quadros: as páginas aparecem pelo slug do artigo mais o número da imagem, e os vídeos pelo id da sessão mais a folha e os quadros.
## Sumário

1. A filosofia: princípios de primeira ordem
2. Como a Apple constrói uma interface, do problema à tela
3. O sistema: tipografia, cor, materiais, layout e espaçamento, ícones e símbolos, movimento, háptica e som, escrita, acessibilidade
4. Diferenças entre plataformas que mudam decisões de design
5. Evolução do pensamento de design da Apple por período
6. Anti-padrões que a Apple condena explicitamente
7. Checklist de revisão de uma interface no padrão Apple
8. Limites desta base
9. O que só as imagens mostram
---

## 1. A filosofia: princípios de primeira ordem

Os princípios abaixo aparecem ao mesmo tempo nas diretrizes escritas e nas falas das sessões. Para cada um: o que diz, por que a Apple defende, e onde está sustentado.

Um ponto de partida formal: a página "Design principles" das diretrizes lista oito princípios (Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight) e os trata como ferramentas para arbitrar prioridades concorrentes, não como regras fixas (`hig/00 design-principles`). A sessão "Principles of great design" de 2026 lista nove, acrescentando Forgiveness entre Agency e Responsibility, e abre com a definição de design como fazer algo com intenção, focando no que mais importa para as pessoas (`vid/17 wwdc2026_250`). Os treze princípios desta seção organizam essa gramática com o que as outras 34 fontes acrescentam.

### 1.1 Propósito antes de tudo: fazer poucas coisas que importam

O que diz: comece pela intenção, pelo que é genuinamente útil para quem usa; decidir o que construir é, na prática, decidir o que deixar de fora.

Por que: toda funcionalidade consome tempo, atenção e confiança das pessoas, recursos que não podem ser desperdiçados (`vid/17 wwdc2026_250`). Grandes apps fazem poucas coisas muito bem, em vez de tentar resolver tudo numa tela (`vid/11 wwdc2022_10001`). Configuração também é custo: cada opção extra é uma decisão a mais e interrompe a tarefa (`hig/04 settings`).

Sustentação: `hig/00 design-principles` (Purpose); `vid/17 wwdc2026_250`; `vid/04 wwdc2018_802` (simplificação radical, foco extremo, o caso da mala Rollaboard desenhada para 0,1% de 1% dos viajantes); `vid/02 wwdc2016_805` (cruzar funcionalidades com metas do cliente e do app); `vid/00 meet-with-apple_254` (LTK e a "brutal prioritization"); `vid/15 wwdc2025_359` (listar tudo, depois cortar, renomear e agrupar).

### 1.2 O conteúdo em primeiro lugar; a interface e a marca cedem

O que diz: a interface existe para servir o conteúdo. Controles formam uma camada funcional que aparece quando necessária e recua quando não; a identidade de marca vive na camada de conteúdo.

Por que: espaço de tela usado só para exibir marca é espaço tirado do que a pessoa veio buscar (`hig/01 branding`). A camada de interface vinha ocupando cada vez mais espaço à medida que as telas cresciam, e o Liquid Glass busca reduzir essa pegada (`vid/00 meet-with-apple_208`). Uma boa experiência de leitura é aquela que não se nota (`vid/03 wwdc2017_815`).

Sustentação: `hig/01 branding` (a marca sempre cede ao conteúdo; sem logo repetido; launch screen não é momento de marca); `hig/02 materials` (Liquid Glass como camada de controles acima do conteúdo, nunca na camada de conteúdo); `hig/03 launching`; `vid/00 meet-with-apple_208`, `_254`, `_255`, `_256`; `vid/05 wwdc2019_211` ("content first" no tvOS); `vid/03 wwdc2017_816` (liderar com conteúdo); `vid/05 wwdc2019_809` (no Mac a interface deve ser mais neutra e não competir com o conteúdo); `vid/16 wwdc2025_219`; `vid/17 wwdc2026_251` (UI layer para padrões familiares, content layer para a marca).

### 1.3 Familiaridade e consistência: o componente do sistema é o padrão, o customizado é exceção justificada

O que diz: construa sobre o que as pessoas já sabem, do mundo real e da plataforma. Um comportamento estabelecido deve valer em todo lugar. Use componentes e padrões do sistema; customize só onde há razão importante.

Por que: consistência de símbolos, posição e comportamento evita reaprender, como os controles de um carro que funcionam igual em carros diferentes (`vid/03 wwdc2017_802`). Componentes do sistema trazem de graça acessibilidade, adaptação de layout, Dynamic Type, localização e animação (`hig/00`, insight 10; `vid/00 meet-with-apple_208`). Recriar UI do sistema sem perfeição faz o app parecer quebrado (`hig/09 windows`). Mudar um modelo mental consolidado é arriscado e só vale com teste que prove uma vitória clara (`vid/03 wwdc2017_802`).

Sustentação: `hig/00 design-principles` (Familiarity); `hig/03` (insight 4: player de vídeo, navegador de arquivos, impressão e ajuda do sistema como padrão); `hig/09 windows`; `hig/13 gestures` (não usar gesto familiar para ação única, nem gesto único para ação padrão); `vid/03 wwdc2017_802` (o glifo "sharrow" do iOS preferido a um ícone de compartilhar genericamente bom); `vid/03 wwdc2017_809` (começar dos padrões do SDK); `vid/05 wwdc2019_808` (não recriar o que o UIKit entrega); `vid/00 meet-with-apple_255` (Slack: "don't make me think"); `vid/17 wwdc2026_251` (não recriar context menu); `vid/17 wwdc2026_250` (metáforas nem literais nem abstratas demais; consistência de comportamento e de posição).

### 1.4 Clareza e simplicidade, que não são minimalismo

O que diz: inclua só o necessário, com hierarquia clara, controles reconhecíveis e linguagem concisa. Simplicidade é ausência de fricção, não esconder tudo num único lugar; às vezes simplificar é acrescentar contexto.

Por que: um app claro responde em cada tela "onde estou", "o que posso fazer" e "para onde posso ir" (`vid/15 wwdc2025_359`), as mesmas perguntas de sinalização que a Apple já descrevia em 2017 como wayfinding (`vid/03 wwdc2017_802`). Um menu hambúrguer fechado não comunica o que contém (`vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`). O exemplo de 2026 é o controle de play que ganha o tempo restante ao retomar um vídeo: mais informação, mais simples de decidir (`vid/17 wwdc2026_250`).

Sustentação: `hig/00 design-principles` (Simplicity: "simplicidade não é minimalismo", foco no útil); `hig/02 writing` (menos palavras, cada palavra necessária); `hig/08 tab-bars` (abas sempre visíveis); `vid/03 wwdc2017_802` (visibility e wayfinding); `vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`; `vid/17 wwdc2026_250`; `vid/15 wwdc2025_404` (não existe cota mínima de palavras).

### 1.5 Agência, perdão e controle nas mãos da pessoa

O que diz: leve a pessoa direto à tarefa, deixe-a explorar sem prendê-la a fluxos fixos, torne ações reversíveis e confirme apenas o que é destrutivo e irreversível. Em sistemas inteligentes, a decisão final continua humana.

Por que: pessoas se engajam mais quando controlam a experiência no próprio ritmo; perdão sustenta agência porque dá confiança de que sempre é possível voltar (`vid/17 wwdc2026_250`). Gestos devem poder ser redirecionados e interrompidos a qualquer momento, porque pensamento e gesto acontecem em paralelo (`vid/04 wwdc2018_803`). Em IA generativa, as pessoas devem poder descartar, reverter e refazer, e ações destrutivas não devem ser automatizadas (`hig/14 generative-ai`).

Sustentação: `hig/00 design-principles` (Agency); `hig/04 undo-and-redo`; `hig/03 feedback` e `modality`; `hig/14 generative-ai`; `hig/15 machine-learning` (correções imediatas e persistentes; nunca depender de correções para compensar baixa qualidade); `vid/04 wwdc2018_803`; `vid/06 wwdc2019_803`; `vid/17 wwdc2026_250`; `vid/17 wwdc2026_227` (não delegar o pensamento crítico às ferramentas).

### 1.6 Feedback imediato e causal

O que diz: toda ação precisa de resposta, antes, durante e depois do toque. O feedback tem de deixar óbvio o que o causou e combinar visual, som e háptica em harmonia.

Por que: pessoas são muito sensíveis a latência; atraso quebra a sensação de que a interface é extensão do corpo (`vid/04 wwdc2018_803`). Um botão sem estado de pressão parece não responder (`hig/07 buttons`). Um indicador de progresso parado é lido como travamento (`hig/11 progress-indicators`). Para o feedback ser útil, precisa ser óbvio o que o causou (`vid/05 wwdc2019_810`).

Sustentação: `hig/03 feedback`, `playing-haptics` (relação causal consistente); `hig/11 progress-indicators`; `vid/03 wwdc2017_802` (feedback de status, conclusão, aviso e erro); `vid/04 wwdc2018_803`, `wwdc2018_804` (perceived affordance, feedforward, feedback); `vid/05 wwdc2019_810` (causalidade, harmonia, utilidade); `vid/10 wwdc2021_10278`.

### 1.7 Responsabilidade: privacidade, dados mínimos, momento certo e confiança

O que diz: seja transparente sobre o que o app faz, peça permissão no momento em que a funcionalidade precisa, colete só o necessário, antecipe usos indevidos e proteja as pessoas.

Por que: a Apple trata privacidade como direito humano fundamental; nenhum sistema inteligente vale esse sacrifício (`vid/07 wwdc2020_10086`). Pedir dados sem contexto é o locador que exige documentos antes de mostrar o apartamento (`vid/03 wwdc2017_816`). Urgência mal representada numa notificação quebra a confiança (`hig/03 managing-notifications`). No visionOS a privacidade vira arquitetura: o app não sabe para onde a pessoa olha até ela agir (`hig/13 eyes`; `vid/13 wwdc2023_10073`; `vid/16 wwdc2025_303`).

Sustentação: `hig/00 design-principles` (Responsibility); `hig/02 privacy`; `hig/03 managing-accounts`, `managing-notifications`; `hig/15 healthkit`, `id-verifier`; `hig/16 sign-in-with-apple`, `wallet` (pedir limiar de idade, não data de nascimento); `vid/03 wwdc2017_816`; `vid/07 wwdc2020_10162` (privacidade de localização); `vid/08 wwdc2020_10087` (o que acontece no dispositivo fica no dispositivo); `vid/17 wwdc2026_250` (salvaguardas para IA, até remover a funcionalidade).

### 1.8 Flexibilidade e inclusão desde o primeiro rascunho

O que diz: projete para todos, tratando acessibilidade e inclusão como fundamento, no mesmo nível de cor e tipografia, e não como camada posterior. Deficiência é um espectro e faz parte da experiência humana.

Por que: soluções desenhadas para uma necessidade específica viram recursos para todos, como o mostrador de tipo grande do Apple Watch (`vid/09 wwdc2021_10308`) ou as rampas de calçada (`vid/16 wwdc2025_316`). Inclusão tratada no fim é reativa e não sobra tempo para corrigir (`vid/10 wwdc2021_10304`). A lacuna de inclusão é a distância entre o que um corpo pode fazer e o que o design espera dele (`vid/16 wwdc2025_316`).

Sustentação: `hig/00 design-principles` (Flexibility); `hig/01 accessibility`, `inclusion`; `hig/17` (Foundations põe Accessibility e Inclusion ao lado de Color e Typography); `vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`; `vid/09 wwdc2021_10275`, `wwdc2021_10308`; `vid/10 wwdc2021_10304`; `vid/16 wwdc2025_316`.

### 1.9 O corpo, o contexto e o dispositivo como régua

O que diz: cada plataforma é desenhada a partir de como é segurada, vista e usada: distância, postura, tempo de atenção, método de entrada. Não se porta uma interface de uma plataforma para outra.

Por que: as práticas de cada plataforma derivam de observação de uso real, não de estética abstrata (`hig/00`, insight 1). O Apple Watch "não é um iPhone em miniatura" (`vid/02 wwdc2015_802`, `wwdc2015_805`). O ponteiro de seta do Mac não funcionou no iPad porque seria uma ferramenta de alta precisão para controles de baixa precisão (`vid/07 wwdc2020_10640`). No visionOS, conforto visual e vestibular é pré-requisito (`hig/02 motion`, `spatial-layout`; `vid/13 wwdc2023_10078`).

Sustentação: `hig/00` (Designing for iOS, iPadOS, macOS, tvOS, visionOS, watchOS, games, iPhone Duo); `hig/01 immersive-experiences`; `hig/02 spatial-layout`; `vid/01 tech-talks_801`, `_802`, `_10884` (princípios derivados da geometria do hardware); `vid/07 wwdc2020_10206` (um bom app de iPad não é meio-termo entre iPhone e Mac); `hig/15 mac-catalyst`; `vid/13 wwdc2023_10072`, `_10073`, `_10078`.

### 1.10 Craft: nada é aleatório

O que diz: cada decisão é deliberada, de um alinhamento óptico a um som de clique. Craft inclui manter e evoluir o design depois do lançamento.

Por que: qualidade implica que não há nada aleatório (`vid/04 wwdc2018_801`); detalhes são desenhados mesmo quando parecem óbvios (`vid/04 wwdc2018_804`). Para cada recurso lançado há dezenas de esboços e protótipos descartados (`vid/00 meet-with-apple_208`). Design é um compromisso contínuo que não termina no lançamento (`hig/00 design-principles`).

Sustentação: `hig/00 design-principles` (Craft); `hig/01 icons` (alinhamento óptico, não geométrico); `vid/03 wwdc2017_823` (peso óptico, espessura de linha e posicionamento óptico de glifos); `vid/03 wwdc2017_815`; `vid/04 wwdc2018_801`, `_804`; `vid/06 wwdc2019_239` (craft também no código); `vid/17 wwdc2026_250`.

### 1.11 Deleite é a soma, não decoração

O que diz: identifique a emoção que se quer provocar e deixe-a moldar o design. Deleite não é confete adicionado no fim.

Por que: o deleite emerge da soma de liberdade, segurança para explorar, familiaridade e flexibilidade (`hig/00 design-principles`); é a soma da consideração posta no produto (`vid/17 wwdc2026_250`). Efeitos visuais precisam continuar agradáveis muito depois da novidade passar (`vid/14 wwdc2024_10151`).

Sustentação: `hig/00 design-principles` (Delight); `vid/17 wwdc2026_250`; `vid/14 wwdc2024_10151`; `vid/03 wwdc2017_820`; `vid/09 wwdc2021_113` (a categoria "Delight and fun" do Apple Design Award); `hig/12 widgets` (surpreender em ocasiões especiais).

### 1.12 Moderação: interrupção, cor, efeito e som são créditos escassos

O que diz: alertas, notificações, cor de destaque, animação, háptica, som e efeitos de material devem ser usados com parcimônia e sempre com propósito.

Por que: interromper a pessoa é um crédito que se gasta (`hig/03`, insight 1); interromper é um privilégio (`vid/04 wwdc2018_806`). Alertas perdem impacto se usados em excesso (`hig/03 feedback`; `hig/09 alerts`). Cor de destaque usada amplamente dilui o impacto (`hig/01 branding`). Muitas vezes a decisão certa é não adicionar som nem háptica (`vid/05 wwdc2019_810`; `vid/03 wwdc2017_803`, "Silence is golden"). O Liquid Glass deve ser limitado aos elementos mais importantes (`vid/15 wwdc2025_284`).

Sustentação: `hig/01 branding`, `color`; `hig/02 motion`, `materials`; `hig/03 feedback`, `playing-haptics`; `hig/09 alerts`, `action-sheets`; `vid/03 wwdc2017_803`, `_813`; `vid/04 wwdc2018_806`; `vid/05 wwdc2019_810`; `vid/14 wwdc2024_10188` (usar animações com intenção e propósito); `vid/15 wwdc2025_284`; `vid/16 wwdc2025_219`.

### 1.13 Honestidade de estado e de linguagem

O que diz: a interface mostra o estado real e atual, sem enfeitar nem esconder. Componentes do sistema significam sempre a mesma coisa; limitações e confiança de um modelo são comunicadas com clareza.

Por que: badge só conta notificações não lidas, e imitar um badge engana (`hig/12 notifications`). Indicador determinado com ritmo irreal parece enganoso (`hig/11 progress-indicators`). Controles e complicações precisam refletir o estado real (`hig/12`, insight 1). Em ML, atribuição factual ("porque você baixou X") gera confiança onde uma porcentagem crua não gera (`vid/06 wwdc2019_803`; `hig/15 machine-learning`).

Sustentação: `hig/11 activity-rings`, `progress-indicators`; `hig/12 controls`, `complications`, `notifications`, `widgets`; `hig/14 generative-ai` (avisar que o conteúdo gerado pode conter erros); `hig/15 machine-learning`; `vid/06 wwdc2019_802` (Pixelmator Photo torna o ajuste do modelo visível e editável), `wwdc2019_803`; `vid/11 wwdc2022_110342` (descrição de gráfico autossuficiente).

---

## 2. Como a Apple constrói uma interface, do problema à tela

Nenhuma sessão isolada descreve o processo inteiro. As etapas abaixo consolidam o que as sessões e as diretrizes descrevem, na ordem em que aparecem com mais frequência. Várias sessões insistem que o processo é iterativo e que etapas voltam a ser percorridas (`vid/02 wwdc2016_805`; `vid/15 wwdc2025_359`: "Design is never really finished").

### Etapa 1. Perguntar por que a coisa deve existir

- Antes de esboçar qualquer tela, perguntar se o que está sendo construído tem propósito (`vid/17 wwdc2026_250`).
- Perguntar por que as pessoas usam o app (`vid/11 wwdc2022_10001`). Cada pessoa do time deveria saber responder que bem humano o produto serve (`vid/10 wwdc2021_10304`, fase de ideação).
- Cavar além da necessidade superficial até a necessidade real: o Streaks Workout não resolve "ficar saudável", resolve inércia e tédio (`vid/04 wwdc2018_802`).
- Em ambientes imersivos, a mesma pergunta aparece como "por que estamos construindo este ambiente, que qualidades ele deve transmitir e como será usado" (`vid/17 wwdc2026_234`); em ambientes customizados, a função emocional do espaço vem antes da geometria (`vid/14 wwdc2024_10087`).

### Etapa 2. Definir para quem, com especificidade

- A audiência não pode ser "todo mundo"; "você não é o usuário" (`vid/02 wwdc2016_805`).
- Transformar o que essa pessoa prefere, valoriza e faz em metas do cliente; definir metas do app (como deve parecer e se sentir); deixar metas de negócio de fora das decisões de design (`vid/02 wwdc2016_805`).
- Projetar para um caso extremo pode tornar o design mais coerente e alcançar mais gente (`vid/04 wwdc2018_802`).
- Pensar pelos eixos de diversidade e pelos extremos de uso, não pela pessoa média (`vid/10 wwdc2021_10304`); envolver pessoas com deficiência reais ("Nothing about us without us", `vid/16 wwdc2025_316`).
- Observar a plataforma e o contexto físico de uso: distância, postura, tempo de atenção, entradas (`hig/00` designing-for-*).

### Etapa 3. Listar tudo o que o app poderia fazer, sem julgar, e depois cortar

- Listar todas as funcionalidades imagináveis, sem ideia boa ou ruim nessa fase (`vid/02 wwdc2016_805`; `vid/15 wwdc2025_359`).
- Imaginar como e quando as pessoas usariam o app; então limpar: remover o não essencial, renomear o que não é claro, agrupar o que pertence junto. A Apple chama isso de arquitetura de informação (`vid/15 wwdc2025_359`).
- Classificar funcionalidades pela importância do ponto de vista de quem usa, não de quem desenvolve (`vid/09 wwdc2021_10126`).
- O mesmo filtro aparece para superfícies do sistema: nem toda ação vira shortcut; os critérios são valor de repetição, viabilidade por voz e utilidade em muitos contextos (`vid/06 wwdc2019_806`); um ou dois shortcuts habituais bastam (`vid/13 wwdc2023_10193`); para o Apple Watch, pergunta-se que informação mostrar se houvesse dez segundos de atenção (`vid/13 wwdc2023_10138`).

### Etapa 4. Estruturar navegação e conteúdo

- Decidir o que merece uma aba perguntando o que é realmente essencial; cada aba extra é mais uma decisão para a pessoa (`vid/15 wwdc2025_359`). Abas refletem a hierarquia de informação e são para navegação, não para ação (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`).
- Usar push para descer na hierarquia e modal para tarefa autocontida (`vid/11 wwdc2022_10001`; `hig/03 modality`).
- Usar a toolbar para responder "onde estou" (título da tela, não marca) e "o que posso fazer" (ações da tela) (`vid/15 wwdc2025_359`).
- Organizar conteúdo por comportamento e motivação reais, não por taxonomia técnica (`vid/09 wwdc2021_10126`); agrupar por tempo, sazonalidade, progresso ou padrões para reduzir sobrecarga de escolha (`vid/15 wwdc2025_359`).
- Aplicar divulgação progressiva: mostrar só o necessário e revelar mais sob demanda (`hig/01 layout`; `vid/03 wwdc2017_802`, a regra 80/20 e o diálogo de impressão).

### Etapa 5. Começar pelo que já se sabe

- Começar pela tela que certamente será necessária, usando como referência um app existente (layout, cor, tipografia), em vez de esperar o app inteiro estar mapeado (`vid/02 wwdc2016_805`; `vid/02 wwdc2014_223`).
- Partir dos padrões do SDK antes de customizar; escrever os casos de uso e os casos extremos e só então perguntar se vale customizar (`vid/03 wwdc2017_809`).
- Em redesenhos de plataforma, recompilar e ver o que migra de graça como linha de base (`vid/00 meet-with-apple_256`); adotar primeiro e redesenhar depois (`vid/00 meet-with-apple_257`).

### Etapa 6. Gerar muitas alternativas e só depois criticar

- Depois de uma primeira versão boa o suficiente, perguntar repetidamente "o que poderíamos fazer diferente?" variando densidade, tipografia, proporção de imagem, contêineres e navegação. No exemplo de 2016 foram onze variações antes da crítica (`vid/02 wwdc2016_805`).
- Começar com muitos esboços à mão e escolher direções realmente distintas (`vid/02 wwdc2014_223`).
- Nunca julgar durante a geração; não se contentar com a primeira ideia (`vid/02 wwdc2016_805`).
- Com agentes de código em 2026, o mesmo método: pedir múltiplas variações nomeadas com prompts específicos, remixar os elementos favoritos e repetir; prompts vagos ancoram num ponto de partida ruim (`vid/17 wwdc2026_227`).

### Etapa 7. Prototipar, subindo a fidelidade aos poucos

- Três perguntas antes de prototipar: o que precisa ser real, o que pode ser falso, onde a pessoa vai usar (`vid/02 wwdc2014_223`).
- Evoluir de imagens estáticas para animação e depois para interação real; código de protótipo é descartável (`vid/02 wwdc2014_223`).
- Qualquer ferramenta que mostre imagens e responda a interação serve, inclusive Keynote (`vid/03 wwdc2017_818`).
- Prototipar a interação junto com o visual, nunca depois; uma demo interativa vale mais que designs estáticos (`vid/04 wwdc2018_803`).
- Resolver a interação com protótipos de baixa fidelidade, até só com botões de texto, antes de investir no visual (`vid/06 wwdc2019_802`, Flow by Moleskine).
- Testar com dados reais cedo, porque dados reais raramente são tão limpos quanto os imaginados (`vid/11 wwdc2022_110340`); trazer conteúdo real e estados de borda para os protótipos (`vid/17 wwdc2026_227`).

### Etapa 8. Mostrar a pessoas reais, no dispositivo e no contexto

- Mostrar o protótipo ao público real sem defender o resultado; perguntar se a pessoa sabe fazer a tarefa, se é fácil, como melhorar; depois discutir o que funcionou, onde travaram e que ideias surgiram (`vid/02 wwdc2014_223`).
- Não argumentar, defender nem descartar o feedback; testar em contexto, no dispositivo real (`vid/03 wwdc2017_818`).
- Pedir a alguém que nunca usou o app para narrar em voz alta o que pensa enquanto usa (`vid/03 wwdc2017_802`).
- Testar no lugar onde será usado: o botão "make toast" foi testado num iPhone, no quarto, pela manhã (`vid/04 wwdc2018_804`).
- Iterar rótulos a partir da reação: coração e polegar foram mal interpretados até o texto "Suggest toast like this" resolver (`vid/09 wwdc2021_10126`).
- No visionOS e em hápticos o dispositivo é obrigatório: a percepção só é confiável no headset (`vid/14 wwdc2024_10096`, `wwdc2024_10152`; `vid/16 wwdc2025_303`); háptica não é reproduzida no simulador (`vid/10 wwdc2021_10278`).

### Etapa 9. Design visual: hierarquia, tipo, cor e forma trabalhando juntos

- Revisar como tipografia, cor e imagem trabalham juntas; o impacto vem do conjunto, não de peças isoladas (`vid/15 wwdc2025_359`).
- Tornar o elemento mais importante maior ou mais contrastado; usar estilos de texto do sistema; escolher uma paleta com regras simples; usar cores semânticas (`vid/15 wwdc2025_359`).
- Expressar hierarquia por layout e agrupamento, não por decoração; alinhar formas com concentricidade (`vid/16 wwdc2025_356`).
- Detalhes de sistema estão na Seção 3.

### Etapa 10. Escrever como parte do design

- Escrita não é preenchimento posterior. Para cada tela: Purpose, Anticipation, Context, Empathy (PACE) (`vid/11 wwdc2022_10037`).
- Definir a voz primeiro e depois variar o tom conforme a situação (`hig/02 writing`; `vid/14 wwdc2024_10140`).
- Remover palavras de preenchimento, evitar repetição, liderar com o porquê, manter uma lista de palavras (`vid/15 wwdc2025_404`).
- Nomear funcionalidades testando pertencimento, expectativa e funcionamento em qualquer idioma, e dizendo o nome em voz alta numa frase cotidiana (`vid/17 wwdc2026_290`).
- Ler o texto em voz alta (`vid/11 wwdc2022_10037`; `vid/15 wwdc2025_404`).

### Etapa 11. Som e háptica como camadas de design

- Pensar em som desde o início: o app manda notificações frequentes, o som pode ter papel de marca, como o app seria entendido sem interface gráfica (`vid/03 wwdc2017_803`).
- Perguntar o que o objeto seria no mundo físico e como soaria e se sentiria; aplicar causalidade, harmonia e utilidade; construir de forma aditiva, visual, depois áudio, depois háptica (`vid/05 wwdc2019_810`).
- Testar candidatos lado a lado e recombinar peças de assets diferentes quando nenhum par pronto combina (`vid/10 wwdc2021_10278`).

### Etapa 12. Acessibilidade e inclusão atravessando todas as etapas

- Planejar acessibilidade e internacionalização desde o início; testar com VoiceOver, tamanho de texto máximo e navegação por teclado; tratar lacunas com plano e data (`vid/10 wwdc2021_10304`).
- Apoiar múltiplos sentidos, oferecer customização, adotar as APIs de acessibilidade, rastrear a dívida de inclusão (`vid/16 wwdc2025_316`).
- Simular a limitação sobre o próprio produto: o jogo Ordia foi testado em monocromia e com filtros de daltonismo (`vid/06 wwdc2019_802`).

### Etapa 13. Comunicar o trabalho

- Terminologia compartilhada entre design e engenharia, uma única fonte de verdade, mostrar mais do que contar (`vid/03 wwdc2017_809`).
- Designers e engenheiros lado a lado olhando o build real, especialmente quando o material não é replicável nas ferramentas de design (`vid/00 meet-with-apple_208`).
- Ao apresentar: definir cada problema numa frase com acordo explícito, contar como história, falar da experiência na primeira pessoa, tratar todo feedback como dado (`vid/04 wwdc2018_811`).

### Etapa 14. Lançar, cortar com critério e continuar evoluindo

- Diante de prazo, cortar para fazer menos coisas bem para todos; lançar não é ponto final (`vid/10 wwdc2021_10304`).
- Priorizar o rollout por risco e frequência de uso (`vid/00 meet-with-apple_255`, Slack).
- Manter a interface atualizada com as capacidades da plataforma; mudanças de ícone devem ser deliberadas, porque a familiaridade acumulada é parte do valor (`hig/00 design-principles`; `vid/03 wwdc2017_822`, lineage).
- Tentar quebrar o próprio design para saber se ele funciona (`vid/17 wwdc2026_234`).

---

## 3. O sistema

Regras e números consolidados. Quando duas fontes divergem num número, as duas aparecem, com a indicação de qual é diretriz e qual é fala.

### 3.1 Tipografia

Famílias e regras gerais
- Duas famílias do sistema: San Francisco (SF Pro, SF Compact, SF Mono, variantes arredondadas e por script, como SF Arabic) e New York, serifada; ambas em formato variável com tamanhos ópticos dinâmicos (`hig/02 typography`). Em 2022 a SF ganhou o eixo de largura: Condensed, Compressed e Expanded, além de Regular; para a maioria dos casos, dois ou três estilos bastam (`vid/11 wwdc2022_110381`).
- Fonte do sistema por plataforma: SF Pro em iOS, iPadOS, macOS, tvOS e visionOS; SF Compact no watchOS, com SF Compact Rounded nas complicações (`hig/02 typography`).
- Prefira os pesos Regular, Medium, Semibold e Bold; evite Ultralight, Thin e Light, sobretudo em texto pequeno; fontes finas pedem tamanhos maiores que o recomendado (`hig/02 typography`; `hig/01 accessibility`).
- Minimize o número de tipografias; tipografias demais obscurecem a hierarquia (`hig/02 typography`). Em 2017 a recomendação falada era usar de dois a três text styles por tela (`vid/03 wwdc2017_812`).
- Use os text styles do sistema em vez de tamanhos "no olho": eles carregam hierarquia e suporte automático a Dynamic Type (`hig/02 typography`; `vid/15 wwdc2025_359`).
- Não embuta as fontes do sistema no app; em mockups fiéis, ajuste o tracking, porque em execução o sistema ajusta o tracking a cada tamanho (`hig/02 typography`).
- Fonte customizada: legível em todos os tamanhos, com Dynamic Type e Bold Text implementados manualmente; costuma funcionar bem para títulos com a fonte do sistema no corpo (`hig/01 branding`; `hig/02 typography`). Tipografia deve ser funcional antes de expressiva (`vid/17 wwdc2026_251`). Para escolher uma, parta do uso pretendido e da impressão desejada, entenda estrutura e contraste, compare candidatas no mesmo tamanho de ponto e não escolha pelo nome combinar com o tema (`vid/03 wwdc2017_815`).

Tamanhos padrão e mínimos (`hig/01 accessibility`; `hig/02 typography`; `hig/00 designing-for-games`)

| Plataforma | Padrão | Mínimo |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

A sessão de jogos de 2024 repete os mesmos números para iPhone, iPad (17 e 11) e Mac (13 e 10) e recomenda usar scroll views em vez de reduzir o tipo quando falta espaço (`vid/14 wwdc2024_10085`). Widgets: 11 pt ou mais (`hig/12 widgets`).

Dynamic Type no iOS e iPadOS, tamanho Large (padrão), em tamanho e leading, pontos (`hig/02 typography`)
- Large Title 34/41; Title 1 28/34; Title 2 22/28; Title 3 20/25; Headline 17/22; Body 17/22; Callout 16/21; Subhead 15/20; Footnote 13/18; Caption 1 12/16; Caption 2 11/13.
- No maior tamanho de acessibilidade (AX5): Body 53/62, Large Title 60/70.
- macOS (sem Dynamic Type): Body 13/16, Headline 13/16 em Bold, Large Title 26/32 (`hig/02 typography`; `vid/08 wwdc2020_10104`, text styles centrados no corpo de 13 pt, sem controle deslizante de tamanho no sistema).
- tvOS: Title 1 76/96, Body 29/36, Caption 2 23/30 (`hig/02 typography`).
- watchOS, tamanho Large (40, 41 e 42 mm): Body 16/18,5, Large Title 36/38,5 (`hig/02 typography`).

Regras de escala e leitura
- Suporte ampliação de texto de pelo menos 200%, ou 140% no watchOS (`hig/01 accessibility`).
- Se o texto pode crescer, deve crescer; use a largura disponível; não trunque; escale glifos junto com o texto (`vid/05 wwdc2019_244`). Em tamanhos grandes, troque layouts lado a lado por empilhados e reduza colunas; mantenha elementos primários no topo (`hig/02 typography`; `vid/08 wwdc2020_10020`).
- Não aumente títulos de abas junto com o conteúdo quando isso não for importante (`hig/02 typography`).
- Tight leading reduz a altura de linha em 2 pt e loose leading aumenta 2 pt no iOS e macOS; no watchOS o ajuste é de 1 pt (exemplo falado: Body com linha de 22 pt vai a 20 ou 24) (`vid/07 wwdc2020_10175`). Não use tight leading com três ou mais linhas (`hig/02 typography`).
- Tracking anda em par com o tamanho óptico: na SF Pro vai de +41 milésimos de em a 6 pt até 0 a partir de 80 pt (`hig/02 typography`). A troca entre desenho Text e Display acontece hoje entre 17 e 28 pt; antes o corte era 20 pt. Para strings truncadas, prefira o aperto automático de tracking ao kerning manual (`vid/07 wwdc2020_10175`).
- Readability margins limitam o comprimento de linha, porque linhas que vão até a margem padrão ficam longas demais para o olho (`vid/03 wwdc2017_812`).
- visionOS: pesos mais fortes (Body em Medium em vez de Regular; títulos em Bold em vez de Semibold) e tracking levemente maior; texto branco por padrão; texto sem fundo em negrito e sem sombra; texto 2D, não 3D; texto voltado para a pessoa (billboarding); Extra Large Title 1 e 2 para layouts editoriais (`hig/02 typography`; `vid/13 wwdc2023_10076`, `wwdc2023_10072`).
- Idiomas da direita para a esquerda: a diretriz fala em cerca de 2 pt a mais na fonte RTL ao lado de latim em maiúsculas (`hig/02 right-to-left`); a sessão sobre árabe fala em 10% a mais e em tracking zero quando a fonte não é otimizada, com opacidade aplicada à palavra inteira (`vid/12 wwdc2022_110441`).
- Mac Catalyst com idioma iPad: o texto de 17 pt vira 13 pt (escala de 77%) (`hig/15 mac-catalyst`; `vid/05 wwdc2019_809`).

### 3.2 Cor

- Use cor para comunicar, não para decorar; não use a mesma cor para significados diferentes (`hig/01 color`).
- Cores do sistema já trazem variantes clara, escura e de contraste aumentado; cor customizada precisa das quatro variantes; mesmo apps de um só modo precisam fornecer claro e escuro para a adaptatividade do Liquid Glass (`hig/01 color`).
- Cor semântica descreve o propósito, não o valor (`vid/05 wwdc2019_808`; `vid/15 wwdc2025_359`). Não fixe valores de cor do sistema no código e não redefina a semântica, como usar a cor de separador para texto (`hig/01 color`).
- Nunca use só cor para diferenciar, indicar interatividade ou transmitir informação essencial; acrescente forma ou texto; suporte Differentiate Without Color (`hig/01 color`, `accessibility`; `vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`).
- Contraste: texto até 17 pt, 4,5:1; texto de 18 pt ou em negrito, 3:1 (critério WCAG AA usado pelo Accessibility Inspector) (`hig/01 accessibility`). Dark Mode: mínimo 4,5:1 e, para cores customizadas em texto pequeno, buscar 7:1 (`hig/01 dark-mode`). Tint colors: 4,5:1 ou mais (`vid/05 wwdc2019_808`). A sessão de 2021 chama os 4,5:1 com Increase Contrast de "regra aproximada", porque combinações que passam ainda podem ser difíceis de ler (`vid/09 wwdc2021_10275`).
- Cor de destaque com critério: reserve para ações primárias e indicadores de status (badge de não lido, aba selecionada) (`hig/01 branding`). No Liquid Glass, aplique cor ao fundo da ação primária, não a símbolos e texto, e não a vários controles de uma vez (`hig/01 color`). Tint só para transmitir significado, como uma chamada para ação, nunca por efeito visual (`vid/15 wwdc2025_323`, `wwdc2025_284`). Tintar todos os elementos faz nada se destacar (`vid/16 wwdc2025_219`).
- Sobre conteúdo colorido, prefira toolbars e tab bars monocromáticas; evite cor de rótulo parecida com o fundo do conteúdo (`hig/01 color`; `hig/07 buttons`, `toolbars`; `hig/08 tab-bars`).
- Para expressar marca por cor, leve a cor para a camada de conteúdo, onde ela rola sob os controles de vidro (`hig/01 branding`; `vid/17 wwdc2026_251`, mover a cor das barras para o conteúdo).
- Dark Mode: não ofereça ajuste de aparência próprio do app; teste Auto, Increase Contrast e Reduce Transparency; iOS usa fundos base (recuam) e elevated (avançam) (`hig/01 dark-mode`). Pense em luzes diminuídas, não em cores invertidas (`vid/05 wwdc2019_808`). Em 2026, não suportar Dark Mode é descrito como experiência negativa num dispositivo tão pessoal (`vid/17 wwdc2026_251`). Dark Mode não é suportado em visionOS nem em watchOS (`hig/01 dark-mode`).
- Preenchimentos e a maioria dos separadores são semitransparentes; há seis cinzas opacos para quando a transparência cria ilusões ópticas (`vid/05 wwdc2019_808`).
- Cor tem significado cultural: vermelho é perigo em algumas culturas e positivo em outras; branco é luto em alguns lugares e pureza em outros; no Stocks com região China continental, ganho aparece em vermelho (`hig/01 color`, `inclusion`; `vid/09 wwdc2021_10275`).
- Cor ampla: Display P3 a 16 bits por canal, exportada em PNG, com perfil de cor em cada imagem (`hig/01 color`, `images`). Pergunte antes se o conteúdo pede P3; converta perfil, nunca atribua (`vid/03 wwdc2017_821`).
- Por plataforma: no macOS, a cor de destaque escolhida pela pessoa substitui a do app, e as interfaces devem ser mais neutras (`hig/01 color`; `vid/05 wwdc2019_809`); no tvOS, não indique foco só por cor (`hig/01 color`); no visionOS, cor com moderação sobre o vidro, preferindo texto e símbolos brancos e cor em fundos ou botões inteiros (`hig/01 color`; `vid/13 wwdc2023_10076`); no watchOS, cor de fundo com função, não adorno (`hig/01 color`; `vid/13 wwdc2023_10026`, `wwdc2023_10138`); no CarPlay, paleta limitada, mesma cor nunca para interativo e não interativo, e teste em carro real (`hig/14 carplay`).
- Elementos de cor fixa não se alteram: Activity rings (Move 250,17,79; Exercise 166,255,0; Stand 0,255,246), sempre sobre preto (`hig/11 activity-rings`); indicadores de page control não devem ser coloridos (`hig/09 page-controls`).

### 3.3 Materiais

- Liquid Glass forma uma camada funcional de controles e navegação que flutua acima do conteúdo; não se usa na camada de conteúdo (use materiais padrão ali), exceto em controles transitórios como sliders e toggles durante a interação (`hig/02 materials`). Aplicá-lo a uma table view de conteúdo compete com o resto e confunde a hierarquia (`vid/16 wwdc2025_219`).
- Use com moderação; é uma camada interativa sob a ponta dos dedos, então limite-a aos elementos mais importantes e prefira controles do sistema (`hig/02 materials`; `vid/15 wwdc2025_284`).
- Nunca vidro sobre vidro; elementos em cima do Liquid Glass usam preenchimento, transparência e vibrância (`vid/16 wwdc2025_219`). Vidros próximos em contêineres diferentes se comportam de modo inconsistente; agrupe-os num contêiner comum (`vid/15 wwdc2025_323`, `wwdc2025_284`).
- Duas variantes que nunca se misturam. Regular: a versátil, adaptativa, indicada quando o fundo pode prejudicar a legibilidade (alertas, sidebars, popovers com texto). Clear: só sobre conteúdo rico em mídia, com camada de escurecimento de 35% sobre conteúdo claro (`hig/02 materials`); a sessão de 2025 exige três condições juntas: conteúdo rico em mídia, o escurecimento não prejudicar o conteúdo, e conteúdo acima ousado e brilhante (`vid/16 wwdc2025_219`).
- O material se adapta: elementos pequenos alternam entre claro e escuro conforme o que passa atrás; elementos grandes, como menus e sidebars, não alternam, porque seria distrativo; ao crescer, o vidro simula maior espessura (`vid/16 wwdc2025_219`). No UIKit, vidro maior fica mais opaco (`vid/15 wwdc2025_284`).
- Materiais padrão no iOS: ultra thin, thin, regular (padrão) e thick. Escolha pelo significado semântico, nunca pela cor aparente; mais espesso dá contraste, mais fino preserva contexto; evite quaternary sobre thin e ultra thin (`hig/02 materials`; `vid/05 wwdc2019_808`). Use cores vibrantes do sistema sobre materiais (`hig/02 materials`).
- Scroll edge effect não é decorativo: só atrás de interface flutuante, um por view. Soft é o padrão no iOS e iPadOS; hard é mais comum no macOS e em interfaces densas, texto interativo e cabeçalhos fixos; os dois não se misturam (`hig/09 scroll-views`; `vid/16 wwdc2025_356`). Use-o no lugar de fundo sólido sob controles (`hig/01 layout`).
- Remova fundos e bordas customizados de barras; hierarquia vem de layout e agrupamento (`vid/16 wwdc2025_356`; `vid/15 wwdc2025_284`; `hig/07 toolbars`).
- Acessibilidade modifica o material automaticamente: Reduced Transparency deixa o vidro mais fosco, Increased Contrast o torna predominantemente preto ou branco com borda, Reduced Motion remove a elasticidade (`vid/16 wwdc2025_219`).
- visionOS: janelas usam glass, que se adapta à luz do ambiente e não tem modo escuro; evite janelas opacas; material mais escuro separa seções, mais claro chama atenção para elementos interativos; não empilhe materiais claros (`hig/02 materials`; `hig/09 windows`; `vid/13 wwdc2023_10076`).
- macOS: sidebar translúcida, nunca cor sólida, imagem ou padrão, porque a vibração sinaliza qual janela tem o foco (`vid/05 wwdc2019_809`).
- watchOS: materiais dão contexto em modais de tela cheia e não devem ser removidos (`hig/02 materials`); há quatro materiais de fundo, Ultra Thin a Thick (`vid/13 wwdc2023_10138`).

### 3.4 Layout e espaçamento

Princípios
- Ordene por importância: o que importa perto do topo e da borda inicial (`hig/01 layout`).
- Alinhamento comunica relação; indentação comunica subordinação; agrupe com espaço negativo, contêineres ou separadores (`hig/01 layout`). Proximidade, agrupamento e mapeamento seguem os princípios de 2017 (`vid/03 wwdc2017_802`).
- Decida layout por size class, não por dispositivo ou orientação; mantenha a mesma funcionalidade quando a size class muda (`hig/01 layout`; `vid/03 wwdc2017_812`).
- Respeite safe areas, margens e guias do sistema (`hig/01 layout`; `vid/01 tech-talks_801`).
- Estenda conteúdo de fundo sob sidebars e barras com background extension effect (`hig/01 layout`; `vid/16 wwdc2025_356`).
- Concentricidade: raio interno somado ao padding dá o raio externo (`vid/13 wwdc2023_10076`). Três formas: fixed (raio constante), capsule (raio igual a metade da altura) e concentric (raio do pai menos o padding) (`vid/16 wwdc2025_356`).
- Mudanças de layout por redimensionamento não devem ser destrutivas: volte ao estado inicial quando possível (`vid/15 wwdc2025_208`).
- macOS: nada crítico na parte inferior da janela, porque a pessoa costuma empurrar essa borda para fora da tela (`hig/01 layout`; `hig/08 sidebars`; `hig/09 windows`; `vid/05 wwdc2019_809`).

Alvos de toque e controles (`hig/01 accessibility`; `hig/00 designing-for-games`; `hig/07 buttons`)

| Plataforma | Padrão | Mínimo |
|---|---|---|
| iOS, iPadOS | 44 x 44 pt | 28 x 28 pt |
| macOS | 28 x 28 pt | 20 x 20 pt |
| tvOS | 66 x 66 pt | 56 x 56 pt |
| visionOS | 60 x 60 pt | 28 x 28 pt |
| watchOS | 44 x 44 pt | 28 x 28 pt |

- Padding ao redor de controles: cerca de 12 pt com bezel e cerca de 24 pt sem bezel (`hig/01 accessibility`; `hig/13 pointing-devices`; `vid/07 wwdc2020_10640`).
- A área de toque pode ser maior que a área visual, e deve ser em controles pequenos (`vid/04 wwdc2018_804`).
- visionOS: centros a pelo menos 60 pt de distância, com 16 pt ou mais entre elementos (`hig/01 layout`; `hig/02 spatial-layout`; `hig/13 eyes`). Um botão de 44 pt precisa de 8 pt ao redor; pilhas de botões, 16 pt; itens de lista e menu, 4 pt de padding; ornamentos sobrepõem a borda inferior da janela em 20 pt (`vid/13 wwdc2023_10076`). Botões com 60 pt ou mais ganham 4 pt de padding para o hover não se sobrepor; tamanhos padrão Mini 28, Small 32, Regular 44, Large 52, Extra large 64 pt (`hig/07 buttons`). Para objetos 3D a um metro, 60 pt correspondem a cerca de 2,5 graus, ou 4,4 cm (`vid/16 wwdc2025_303`).
- watchOS: no máximo três botões com glifo ou dois com texto lado a lado (`hig/01 layout`). A fala de 2015 dava 80 x 80 px para controles circulares no relógio de 42 mm e nunca mais de três botões lado a lado (`vid/02 wwdc2015_805`).

Medidas de estrutura
- tvOS: safe area com 60 pt no topo e na base e 80 pt nas laterais (`hig/01 layout`); a sessão de 2019 falou em 90 pt nas laterais e 60 pt em cima e embaixo (`vid/05 wwdc2019_211`). Grades de foco com 40 pt de espaço horizontal e 100 pt vertical mínimo, de 860 pt por coluna em duas colunas a 160 pt em nove (`hig/01 layout`). Tab bar com 68 pt de altura a 46 pt do topo (`hig/08 tab-bars`). Split view com um terço e dois terços (`hig/06 split-views`).
- macOS: menu bar com 24 pt; nome do app no item About com 16 caracteres ou menos (`hig/07 the-menu-bar`); divisor fino de split view com 1 pt (`hig/06 split-views`).
- Toolbar: título com menos de 15 caracteres; cerca de três grupos no máximo; zonas leading, center e trailing; uma única ação primária proeminente na trailing (`hig/07 toolbars`). Tab view do Mac: no máximo seis abas (`hig/06 tab-views`). Tab bar customizável do iPad: lista padrão de cinco ou menos (`hig/08 tab-bars`). Tab bar do visionOS: até seis itens (`vid/13 wwdc2023_10076`).
- Segmented control: até cinco a sete segmentos em interfaces largas, cerca de cinco no iPhone (`hig/10 segmented-controls`). Radio buttons em grupos de dois a cinco (`hig/10 toggles`). Page control: acima de cerca de dez pontos fica difícil de contar (`hig/09 page-controls`).
- Sheets: detents large e medium, este com cerca de metade da altura (`hig/09 sheets`).
- Widgets: margem padrão de 16 pt e 11 pt para agrupamentos internos (`hig/12 widgets`; `vid/07 wwdc2020_10103`); no widget pequeno, no máximo quatro peças de informação (`vid/07 wwdc2020_10103`). Live Activities: margem de 14 pt na Lock Screen, compartilhada com notificações; raio da Dynamic Island de 44 pt (`hig/12 live-activities`; `vid/13 wwdc2023_10194`).
- Snippets: a diretriz dá altura máxima de 400 pt para a view customizada (`hig/12 snippets`); a sessão de 2025 recomenda não passar de 340 pt (`vid/16 wwdc2025_281`).
- visionOS: janela padrão de 1280 x 720 pt, posicionada a cerca de dois metros, com largura aparente de cerca de três metros (`hig/09 windows`); leitura prolongada a pelo menos um metro (`hig/13 eyes`); limite de cerca de 1,5 m a partir da cabeça nos estilos progressive e full; progressive de 120 a 360 graus (`hig/01 immersive-experiences`); accessory view de alerta com até 154 pt de altura e raio de 16 pt (`hig/09 alerts`).
- iPhone X: 375 x 812 pt, 145 pt a mais de altura que a tela de 4,7 polegadas (`vid/01 tech-talks_801`). Apple Watch Series 7: 176 x 215 pt (41 mm) e 198 x 242 pt (45 mm) de área ativa (`vid/01 tech-talks_10884`).
- Arraste: imagem de arraste após cerca de 3 pt de movimento (`hig/03 drag-and-drop`); swipe reconhecido após histerese de cerca de 10 pt (`vid/04 wwdc2018_803`). Ponteiro do iPadOS (2020): círculo de 19 pt; botões de toolbar com 37 pt de altura (`vid/07 wwdc2020_10640`).

### 3.5 Ícones e símbolos

Ícone de app
- Tamanhos: 1024 x 1024 px para iOS, iPadOS e macOS (retângulo arredondado) e visionOS (círculo); 1088 x 1088 px no watchOS (círculo); 800 x 480 px no tvOS, com duas a cinco camadas e parallax (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`).
- Camadas sem máscara aplicada, conteúdo centralizado; o sistema aplica máscara, realces especulares, sombras e desfoque; não inclua chanfros, sombras ou brilhos "assados" (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`). No Icon Composer, até quatro grupos (`vid/15 wwdc2025_361`).
- Simplicidade: um conceito com poucas formas; texto só se essencial; prefira ilustração a foto; não replique a interface nem hardware Apple (`hig/01 app-icons`). Metáfora, simplicidade, conexão e linhagem; teste na Home Screen, dentro de pasta e em tamanho pequeno, apertando os olhos (`vid/03 wwdc2017_822`).
- Aparências consistentes entre padrão, escuro, claro translúcido e tintado, sem trocar elementos entre variantes (`hig/01 app-icons`); no modo mono, pelo menos um elemento branco (`vid/15 wwdc2025_361`).
- Com o novo material: evite objetos 3D realistas e perspectivas complexas, prefira vista frontal; translucidez com moderação ("Less is more"); evite bordas afiadas e linhas finas; prefira os gradientes System Light e System Dark a branco ou preto puros (`vid/16 wwdc2025_220`).

Ícones de interface e glifos
- Simplificados, com metáforas familiares; consistentes em tamanho, detalhe, peso e perspectiva; peso casado com o texto adjacente; alinhamento óptico com padding quando preciso; formato vetorial; rótulo de acessibilidade para ícones customizados (`hig/01 icons`).
- Desenhe glifos como conjunto: normalize peso óptico e espessura de linha; posicione pelo centro óptico, como o Play deslocado alguns pixels à direita; teste em contexto e no dispositivo (`vid/03 wwdc2017_823`).
- Prefira conceitos universais e figuras humanas neutras em gênero (`hig/01 icons`, `inclusion`; `vid/03 wwdc2017_819`, `wwdc2017_823`).
- Use o mesmo símbolo para a mesma ação em todos os dispositivos; quando não há atalho visual claro (Select, Edit), use texto; para ações muito relacionadas, o símbolo aparece uma vez para o grupo (`vid/16 wwdc2025_356`). Reserve reticências para overflow (`hig/00 designing-for-iphone-duo`).
- Respeite as convenções de cada plataforma mesmo com estilo próprio, como o ícone de compartilhar (`vid/17 wwdc2026_251`; `vid/03 wwdc2017_802`).

SF Symbols
- Nove pesos, de ultralight a black, casados com os pesos da SF; três escalas relativas à cap height (`hig/02 sf-symbols`); small cerca de 20% menor e large cerca de 30% maior que medium (`vid/07 wwdc2020_10207`).
- Especifique em pontos tipográficos, como texto; não force largura e altura; alinhe pela baseline ao lado de texto (`vid/05 wwdc2019_206`; `vid/07 wwdc2020_10207`).
- Modos de renderização: monochrome, hierarchical, palette e multicolor; escolha pela intenção e confirme no contexto, mesmo com o modo automático (`hig/02 sf-symbols`; `vid/09 wwdc2021_10349`; `vid/11 wwdc2022_10157`). Variable color representa mudança ao longo do tempo, não profundidade (`hig/02 sf-symbols`; `vid/11 wwdc2022_10157`).
- Outline combina com texto, toolbars, navigation bars e listas; fill dá ênfase em tab bars do iOS, swipe actions e seleção; símbolo em círculo ajuda em tamanho pequeno (`hig/02 sf-symbols`; `vid/09 wwdc2021_10097`). Forneça a versão outline; o sistema escolhe fill na tab bar (`vid/14 wwdc2024_10147`; `vid/09 wwdc2021_10349`).
- Proibido usar SF Symbols em ícones de app, logotipos ou marcas (`hig/02 sf-symbols`).
- Símbolos customizados partem de um símbolo existente e do template, com paths fechados, mesma quantidade e ordem de paths entre variantes; três desenhos geram as demais variantes por interpolação (`hig/02 sf-symbols`; `vid/09 wwdc2021_10250`; `vid/13 wwdc2023_10257`).
- A biblioteca foi descrita com mais de 1.000 símbolos em 2019, mais de 3.000 em 2021, mais de 4.000 em 2022, mais de 5.000 em 2023, mais de 6.000 em 2024 e mais de 7.000 em 2026 (`vid/05 wwdc2019_206`; `vid/09 wwdc2021_10097`; `vid/11 wwdc2022_10157`; `vid/13 wwdc2023_10197`; `vid/14 wwdc2024_10188`; `vid/17 wwdc2026_251`).

### 3.6 Movimento

- Movimento com propósito, nunca pela animação em si; opcional, complementado por háptica e som; feedback breve e preciso; evite animar interações frequentes, que o sistema já anima; deixe a pessoa cancelar em vez de esperar (`hig/02 motion`).
- Fluidez vem de comportamento, não de animação prescrita: resposta instantânea; gestos redirecionáveis e interrompíveis; entrada e saída pelo mesmo caminho; a interface cresce na direção do estado final; bordas elásticas, nunca parada seca; rastreamento um para um; conteúdo move com o dedo em posição relativa (`vid/04 wwdc2018_803`).
- Molas: dois parâmetros de design, damping e response; comece com 100% de damping; use quique (o exemplo cita 80%) só quando o gesto de origem tem momento; projete o ponto final pela velocidade (`vid/04 wwdc2018_803`). Em 2026 a sessão de agentes descreve ease e spring com stiffness, damping e mass (`vid/17 wwdc2026_227`).
- Confirmação de toque instantânea; animações lentas ou em fade fazem o controle parecer lento (`vid/04 wwdc2018_804`). Duplo toque atrasa o toque simples em cerca de meio segundo (`vid/04 wwdc2018_803`).
- Continuidade: a transição zoom mantém os mesmos elementos visíveis (`vid/14 wwdc2024_10145`); um botão pode se transformar no menu que abre (`vid/00 meet-with-apple_208`; `vid/15 wwdc2025_284`); elementos de vidro materializam modulando a luz em vez de simples fade (`vid/16 wwdc2025_219`); no watchOS, o mesmo objeto é animado entre páginas para dar permanência (`vid/13 wwdc2023_10026`).
- Limites de duração: animações de Live Activities e de atualização de widgets até 2 segundos (`hig/12 live-activities`, `widgets`); overlays interativos no tvOS com atraso mínimo de 0,5 s para pausar (`hig/03 playing-video`); jogos entre 30 e 60 fps (`hig/02 motion`); cena de AR atualizada 60 vezes por segundo (`hig/14 augmented-reality`).
- Reduce Motion: reduza animações automáticas e repetitivas; aperte as molas; acompanhe o gesto; evite animar profundidade no eixo z; troque transições em x, y e z por fades; evite animar blur (`hig/01 accessibility`); ofereça cross-fade (`vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`); em hover customizado, ofereça alternativa em cross-fade (`vid/14 wwdc2024_10152`).
- visionOS: evite movimento na periferia; objetos grandes em movimento ficam translúcidos; reposicione com fade; não gire o mundo; ofereça referencial estacionário; evite oscilação sustentada perto de 0,2 Hz (`hig/02 motion`). Evite conteúdo preso à cabeça, prefira lazy follow; alinhe o horizonte; mantenha o ponto de expansão lento e dentro do campo de visão; transições de escuro para claro mais lentas (`vid/13 wwdc2023_10078`).
- Hover no visionOS: efeitos instantâneos, com atraso ou em rampa; atraso evita cintilação; efeitos que revelam conteúdo pedem atrasos maiores; mantenha elementos de ancoragem; comece de um elemento visível; evite movimento inesperado e não aplique em views de uso intenso como botões de toolbar (`vid/14 wwdc2024_10152`; `vid/16 wwdc2025_303`).
- Indicadores de progresso sempre em movimento e com ritmo uniforme; não alterne entre spinner e barra (`hig/11 progress-indicators`).
- Animação de símbolos com intenção: Bounce para confirmação, Scale para foco persistente, Pulse para atividade contínua, Replace para mudança de estado; em excesso, distraem (`hig/02 sf-symbols`; `vid/13 wwdc2023_10197`; `vid/14 wwdc2024_10188`).

### 3.7 Háptica e som

Háptica
- Use os padrões do sistema pelo significado documentado; mantenha relação causal consistente; complemente visual e som, casando intensidade e nitidez com a animação; não exagere; prefira hápticos curtos; torne-os opcionais; não atrapalhe câmera, giroscópio ou microfone (`hig/03 playing-haptics`).
- Padrões: no iOS, notification, impact e selection; no Magic Trackpad, alignment, level change e generic; no watchOS, Notification, Up, Down, Success, Failure, Retry, Start, Stop e Click (`hig/03 playing-haptics`).
- Blocos customizados: eventos transient e continuous, com intensity e sharpness de 0 a 1 (`hig/03 playing-haptics`; `vid/05 wwdc2019_520`, `wwdc2019_810`).
- Causalidade, harmonia e utilidade; muitas vezes a decisão certa é não adicionar (`vid/05 wwdc2019_810`; `vid/10 wwdc2021_10278`, "Don't add feedback just because you can"). A densidade da háptica deve casar com a densidade visual (`vid/10 wwdc2021_10278`).
- Sincronia é percebida: deslocar o som em 10 ms em relação à háptica muda a experiência; a mesma vibração parece mais precisa com um som nítido (`vid/03 wwdc2017_803`).
- Sem tato real (toque direto no visionOS, controles virtuais de jogo), compense com feedback visual e sonoro em cada contato; controles de toque têm estado de pressão, som e háptica (`hig/13 game-controls`; `vid/13 wwdc2023_10073`; `vid/14 wwdc2024_10085`, `wwdc2024_10094`).

Som
- O volume do sistema governa a saída; o app só ajusta níveis relativos; escolha a categoria de áudio pelo uso real; não repropósito controles de áudio (`hig/03 playing-audio`).
- Nunca comunique informação importante só por som (`hig/03 playing-audio`; `hig/12 notifications`).
- Som de notificação: reconhecível como daquele app, alinhado à estética, discreto e repetível (a equipe convive com o som por uma semana), limpo. Som de interface: raro, mais baixo que o de notificação, sempre desligável. Teste no dispositivo final e com fones (`vid/03 wwdc2017_803`).
- Blocos do som: timbre, frequência (agudo sugere objeto pequeno), duração (sons repetidos, curtos) e volume (sons de interface, sutis); cliques de botão soam melhor em dois tempos, ao pressionar e ao soltar; estados intermediários podem não precisar de som (`vid/04 wwdc2018_804`).
- visionOS: prefira ter som, porque um app sem som pode parecer quebrado; use áudio espacial, fixo ou rastreado; varie sons repetitivos (`hig/03 playing-audio`); randomize tom e amplitude; cure a melhor versão da realidade, não a mais literal (`vid/13 wwdc2023_10271`).
- Números: áudio no watchOS a 64 kbps HE-AAC (`hig/03 playing-audio`); tvOS não toca sons para acompanhar alertas e notificações (`hig/03 playing-audio`).

### 3.8 Escrita

Voz, tom e clareza
- Defina a voz pelo público e pelo vocabulário familiar; ajuste o tom ao contexto, sério numa queda detectada e celebratório numa conquista (`hig/02 writing`). A voz da Apple é guiada por clareza, simplicidade, amigabilidade e ajuda; qualidades sobem ou descem conforme a situação, nunca zeram (`vid/14 wwdc2024_10140`).
- Seja claro, use menos palavras, leia em voz alta, escreva para todos, sem jargão; considere o propósito de cada tela (`hig/02 writing`; `vid/11 wwdc2022_10037`, PACE).
- Remova preenchimentos ("simply", "quickly"), interjeições e desculpas que não acrescentam sentido; evite repetição; lidere com o porquê ("To get reservation updates, enter your phone number."); mantenha uma lista de palavras com termo escolhido, termos evitados e definição (`vid/15 wwdc2025_404`).
- Refira-se à pessoa como "você"; evite "o usuário"; reserve "nós" para a empresa ou evite-o, sobretudo em erros (`hig/01 inclusion`; `hig/02 writing`).
- Linguagem neutra em gênero, sem expressões coloquiais de origem excludente, humor com cautela (`hig/01 inclusion`; `vid/11 wwdc2022_10037`).
- Termos de implementação não vazam para a interface: "HealthKit", "NFC", "tag", "scene", "popover" e "panel" são trocados por linguagem de quem usa (`hig/15 healthkit`, `nfc`; `hig/09 windows`, `popovers`, `panels`).

Padrões de rótulos e mensagens
- Botões orientados à ação, quase sempre com verbo ("Send" funciona melhor que "Let's do it!"); evite "Click here"; use "tap" em dispositivos de toque; capitalização consistente por tipo de elemento; em fluxos, "Get Started", depois "Continue" ou "Next" de forma consistente, e "Done" no fim (`hig/02 writing`).
- Erros: perto do problema, sem culpar, dizendo como corrigir ("Choose a password with at least 8 characters" em vez de "That password is too short"); sem "oops" (`hig/02 writing`). Estados vazios com próximo passo (`hig/02 writing`).
- Alertas: o que aconteceu, por que a pessoa está vendo, como seguir (`vid/03 wwdc2017_813`). Título que descreve a situação, nunca só "Error", em até duas linhas; frase completa em sentence case com pontuação, fragmento em title case sem ponto; botões de uma ou duas palavras com verbo; "OK" só em alerta informativo; nunca "Yes" e "No"; sempre "Cancel" para cancelar (`hig/09 alerts`). Nomeie a ação específica: "Cancel Subscription" e "Keep Subscription" (`vid/11 wwdc2022_10037`).
- Menus: verbo para ações, title case, sem artigos, reticências quando a ação pede mais informação; rótulos alternáveis como "Show Map" e "Hide Map" (`hig/07 menus`). Toolbar: título útil com menos de 15 caracteres, nunca o nome do app (`hig/07 toolbars`).
- Tooltips: 60 a 75 caracteres, começando por verbo, sentence case, sem ponto final (`hig/03 offering-help`). Tips: uma ou duas frases; título com frase de ação direta; se o recurso exige mais de três ações, é complexo demais para um tip (`hig/03 offering-help`; `vid/13 wwdc2023_10229`).
- Purpose strings de permissão: frase breve, completa, específica, na voz ativa, em sentence case, terminando em ponto (`hig/02 privacy`).
- Notificações: título curto em title case sem ponto; corpo em frases completas; sem nome ou ícone do app; texto genérico ("New comment") para quando prévias estão ocultas (`hig/12 notifications`).
- Voz e Siri: diálogo curto, na língua falada; perguntas específicas ("Which soup?" em vez de "Which one?"); sem nome do app, sem nome da pessoa, sem primeira pessoa; ouça o diálogo várias vezes (`hig/16 siri`; `vid/06 wwdc2019_806`; `vid/07 wwdc2020_10071`). Prompts como pergunta, não como rótulo ("When is the deadline?") (`vid/09 wwdc2021_10283`).
- Rótulos de Action button com até três palavras, verbo no presente (`hig/13 action-button`); títulos de App Clip Card até 30 caracteres e subtítulos até 56 (`hig/14 app-clips`); erros do Apple Pay até 128 caracteres (`hig/14 apple-pay`).
- Machine learning: linguagem de consequência ("Suggest less pop music" em vez de "dislike"); atribuições factuais ("Because you've read nonfiction", não "love") (`hig/15 machine-learning`). IA generativa: feedback específico durante a geração, não "Processing" genérico (`hig/14 generative-ai`).
- Nomes de funcionalidades: pertencem ao conjunto, cumprem a expectativa, funcionam em qualquer idioma; teste dizendo o nome numa frase cotidiana (`vid/17 wwdc2026_290`).
- Localização muda comprimento, direção e abreviações do texto; prefira termos que se traduzem de forma parecida ("photo" em vez de "picture") (`vid/11 wwdc2022_10037`; `vid/03 wwdc2017_819`).

### 3.9 Acessibilidade

- Uma interface acessível é intuitiva, perceptível e adaptável (`hig/01 accessibility`).
- Visão: Dynamic Type em todos os tamanhos, inclusive os de acessibilidade; contraste mínimo; variantes de contraste aumentado; nunca só cor; VoiceOver descrevendo interface e conteúdo (`hig/01 accessibility`). Rótulos de VoiceOver descritivos ("Account settings, button" em vez do nome do glifo) (`vid/09 wwdc2021_10275`); descreva imagens com significado, exclua as decorativas, agrupe imagem e legenda, avise mudanças de layout, suporte o rotor (`hig/16 voiceover`). Bold Text engrossa também elementos não textuais com função de legibilidade (`vid/09 wwdc2021_10275`).
- Audição: legendas, subtítulos, audiodescrição e transcrições; háptica e sinais visuais para quem não percebe o áudio (`hig/01 accessibility`).
- Mobilidade: controles grandes e espaçados; gestos simples; alternativa a todo gesto, como um botão além do swipe; rótulos para Voice Control; suporte a Switch Control, AssistiveTouch e Full Keyboard Access (`hig/01 accessibility`). Tolerância a erro, sem timeouts quando Switch Control está ativo, e dados privados expostos pelo menor tempo possível (`vid/07 wwdc2020_10019`).
- Cognição: ações simples e familiares; evite elementos com temporizador que se autodispensam; no Assistive Access, divida fluxos em telas de uma interação e confirme duas vezes ações difíceis de reverter (`hig/01 accessibility`).
- Movimento e luz: Reduce Motion, controle de reprodução automática, Dim Flashing Lights (`hig/01 accessibility`); Auto-play Video Previews e Prefer Cross-fade Transitions (`vid/05 wwdc2019_244`).
- Respeite as preferências de exibição da pessoa mesmo quando o efeito afetado faz parte da identidade visual do app (`vid/08 wwdc2020_10020`).
- Gráficos: rótulos de acessibilidade com contexto, Audio Graphs, navegação por teclado e Switch Control, nunca exigir interação para informação crítica (`hig/05 charts`); rótulos por extenso, data antes do valor ("June 1, 36 pancakes") (`vid/11 wwdc2022_110340`).
- Formulários: sem limite de caracteres e sem proibir hífens ou acentos em nomes; campo único de nome completo; gênero com espectro amplo e opção de privacidade (`vid/09 wwdc2021_10275`).
- visionOS: sempre mais de uma forma de interagir; gestos customizados não recebem entrada de mão com VoiceOver ativo (`hig/13 eyes`; `hig/16 voiceover`); modo de uma mão e sistemas de interação alternativos (`vid/14 wwdc2024_10094`, `wwdc2024_10096`).
- Números falados nas sessões, como contexto e não como diretriz: 285 milhões de pessoas cegas ou com baixa visão (`vid/03 wwdc2017_811`); mais de 300 milhões com alguma forma de daltonismo (`vid/06 wwdc2019_802`); daltonismo em quase 5% da população (`vid/09 wwdc2021_10275`); um terço das pessoas com algum grau de sensibilidade a movimento (`vid/05 wwdc2019_244`); pessoas com deficiência são 15% da população mundial (`vid/10 wwdc2021_10304`); cerca de uma em sete pessoas tem alguma deficiência (`vid/16 wwdc2025_316`).

---

## 4. Diferenças entre plataformas que mudam decisões de design

A regra de fundo é tratar cada plataforma com a mesma intenção e o mesmo cuidado, derivando as decisões de como o dispositivo é usado (`hig/00 design-principles`, Flexibility; `hig/00`, insight 1). Abaixo, só o que efetivamente muda uma decisão.

### iPhone (iOS)
- Uso na mão, em movimento, de minutos a mais de uma hora; controles mais fáceis de alcançar no meio e embaixo da tela; limitar controles visíveis; permitir swipe para voltar e para ações em linhas de lista (`hig/00 designing-for-ios`).
- Tab bar flutua sobre o conteúdo na base, em Liquid Glass, e pode minimizar ao rolar; busca pode ser aba dedicada na borda trailing ou campo na toolbar inferior, que sobe acima do teclado (`hig/08 tab-bars`, `search-fields`; `vid/15 wwdc2025_323`; `vid/17 wwdc2026_292`). A busca foi para a base por alcance do polegar (`vid/00 meet-with-apple_208`).
- Modal se dispensa por botão na toolbar superior ou swipe para baixo; sheets com detents e grabber; em compact, popovers dão lugar a sheets (`hig/03 modality`; `hig/09 sheets`, `popovers`).
- Switch só dentro de linha de lista; fora dela, botão que se comporta como toggle; não use slider para volume (`hig/10 toggles`, `sliders`).
- Ofereça context menu ou edit menu para um item, nunca os dois (`hig/07 context-menus`).
- Launch screen obrigatório e quase idêntico à primeira tela (`hig/03 launching`).
- Na geometria do iPhone X: preencher a tela inteira, respeitar safe areas, manter controles centralizados em paisagem, não enfeitar o Home indicator (`vid/01 tech-talks_801`).

### iPad (iPadOS)
- Tela grande e múltiplas entradas combinadas: minimize modais e transições de tela cheia, mostre mais conteúdo, mantenha contexto (renomear inline em vez de modal) (`hig/00 designing-for-ipados`; `vid/07 wwdc2020_10206`).
- Um bom app de iPad não é meio-termo entre iPhone e Mac (`vid/07 wwdc2020_10206`).
- Tab bar no topo, conversível em sidebar; na dúvida, comece pela tab bar; sidebar quando há conteúdo muito aninhado (`hig/08 tab-bars`; `vid/14 wwdc2024_10147`; `vid/15 wwdc2025_208`).
- Janelas redimensionáveis livremente; cada documento em sua janela, com nome descritivo; controles de janela na borda leading da toolbar (`hig/09 windows`; `vid/15 wwdc2025_208`).
- Menu bar escondida até ser revelada, centralizada; nunca esconder itens de menu, esmaecer (`hig/07 the-menu-bar`; `vid/15 wwdc2025_208`).
- Ponteiro: em 2020, precisão adaptativa, círculo de 19 pt e magnetismo (`vid/07 wwdc2020_10640`); no iPadOS 26, rastreamento um para um, sem magnetismo, com realce em vidro (`vid/15 wwdc2025_208`).
- Atalhos de teclado para todas as ações comuns; Full Keyboard Access cuida da navegação de controles (`vid/07 wwdc2020_10206`; `hig/13 keyboards`, `focus-and-selection`).
- Apple Pencil marca no instante do toque, sem modo; hover mostra prévia, nunca dispara ação (`hig/13 apple-pencil-and-scribble`).
- Navegação estilo navegador só para hierarquias complexas; tabelas voltam a ser listas em compact (`vid/11 wwdc2022_10009`).

### Mac (macOS)
- Uso estacionário, várias janelas e apps, entradas de alta precisão: mais densidade, menos níveis aninhados, janelas redimensionáveis, atalhos de teclado, personalização (`hig/00 designing-for-macos`).
- A menu bar é o inventário completo de comandos, em ordem fixa (App, File, Edit, Format, View, menus do app, Window, Help); todo item de toolbar também existe como comando de menu; itens indisponíveis são desabilitados, não escondidos (`hig/07 the-menu-bar`, `toolbars`).
- Controles nas bordas não trazem benefício ergonômico; fluxo de cima para baixo; nada crítico embaixo da janela (`vid/05 wwdc2019_809`; `hig/15 mac-catalyst`).
- Cor mais neutra; a cor de destaque escolhida pela pessoa prevalece; sidebar translúcida (`hig/01 color`; `vid/05 wwdc2019_809`; `vid/08 wwdc2020_10104`).
- Sem Dynamic Type; corpo de 13 pt (`hig/02 typography`).
- Controles Mini, Small e Medium seguem retângulo arredondado para alta densidade; Large e X-Large usam capsule (`vid/16 wwdc2025_356`).
- Usuários esperam context menu em todo objeto (`hig/15 mac-catalyst`); estados de janela Main, Key e Inactive com aparências distintas (`hig/09 windows`); settings em janela própria com Command-vírgula (`hig/04 settings`).

### Apple TV (tvOS)
- Visto a oito pés ou mais, com controle remoto: sistema de foco, arte de borda a borda, animações sutis, legível à distância (`hig/00 designing-for-tvos`).
- Foco não se indica só por cor; itens crescem ao ganhar foco, então o espaçamento precisa prever isso; até cinco estados visuais por item focável; evite ponteiro (`hig/01 color`, `layout`; `hig/06 lockups`; `hig/13 focus-and-selection`).
- Content first: algo já tocando ao abrir, menos passos, metadados só quando há interesse (`vid/05 wwdc2019_211`).
- Minimize entrada de texto; peça login e cadastro em outro dispositivo (`hig/03 managing-accounts`; `hig/10 text-fields`).
- Back abre a tela pai; em jogo ativo, abre menu de pausa; diferencie press de tap e ignore taps acidentais durante vídeo ao vivo (`hig/13 remotes`).
- Sem sons para alertas e notificações (`hig/03 playing-audio`).

### Apple Vision Pro (visionOS)
- O dispositivo leva o conteúdo até a pessoa; conforto visual e físico é prioridade; escolha o nível mínimo de imersão para cada momento e comece no Shared Space (`hig/00 designing-for-visionos`; `hig/01 immersive-experiences`; `vid/13 wwdc2023_10072`).
- Olhos miram, mãos selecionam; alvos de 60 pt; formas arredondadas; hover do sistema aplicado fora do processo do app, por privacidade (`hig/13 eyes`; `vid/13 wwdc2023_10073`; `vid/16 wwdc2025_303`).
- Conteúdo no campo de visão, em paisagem, ancorado no espaço e não na cabeça, além do alcance do braço; texto plano; profundidade sutil e com propósito; escala dinâmica (`hig/02 spatial-layout`; `vid/13 wwdc2023_10072`, `wwdc2023_10078`).
- Não há modo escuro; o glass se adapta à luz; tipografia mais pesada (`hig/02 materials`; `vid/13 wwdc2023_10076`).
- Tab bar vertical à esquerda da janela; toolbar na borda inferior como ornamento; não crie toolbar vertical; sheets centralizadas; botão de fechar no canto superior esquerdo (`hig/08 tab-bars`; `hig/07 toolbars`, `ornaments`; `vid/13 wwdc2023_10076`).
- Não existe modo de tela cheia; a expansão vem da janela ou da Digital Crown (`hig/03 going-full-screen`).
- Encontrar o "key moment" que só existe espacialmente, em vez de portar o app iOS numa janela (`vid/13 wwdc2023_10072`; `vid/14 wwdc2024_10086`).
- Som é esperado; um app sem som pode parecer quebrado (`hig/03 playing-audio`).

### Apple Watch (watchOS)
- Interações de relance, de menos de um minuto (`hig/00 designing-for-watchos`); em 2015 a meta falada era cerca de cinco segundos (`vid/02 wwdc2015_802`); em 2023, cerca de dez segundos no máximo com informação de relance (`vid/13 wwdc2023_10309`).
- "Apple Watch is not a miniature iPhone": subconjunto essencial, hierarquia rasa (`vid/02 wwdc2015_802`, `wwdc2015_805`); apps focados e altamente especializados (`vid/13 wwdc2023_10026`).
- Desde o watchOS 10, a Digital Crown é a navegação primária, sempre com equivalente por toque; paginação vertical preferida à horizontal; cada página com a altura de uma tela; layouts Dial, Infographic e List (`hig/13 digital-crown`; `vid/13 wwdc2023_10026`, `wwdc2023_10138`).
- No watchOS 7, menus por toque longo foram eliminados em favor de botões visíveis; ação primária nunca num menu More (`vid/07 wwdc2020_10171`).
- Evite indicadores de carregamento e de progresso indeterminado; prefira avisar por notificação ao terminar (`hig/03 feedback`, `loading`).
- Complicações, Smart Stack e notificações muitas vezes importam mais que o app; notificações foram descritas como a interação primária no relógio (`hig/00 designing-for-watchos`; `vid/04 wwdc2018_806`).
- O bezel preto funciona como padding; "bigger is better" (`vid/02 wwdc2015_805`); cor de fundo com função (`vid/13 wwdc2023_10026`).
- Apps não adicionam opções ao app Settings do sistema (`hig/04 settings`); vídeos de até 30 segundos (`hig/03 playing-video`).

### iPhone Duo
- Duas telas, várias poses e dobradiça: construa para redimensionar com size classes, margens e safe areas, sem larguras fixas; mantenha funcionalidade e posição relativa dos controles entre poses (`hig/00 designing-for-iphone-duo`).
- Toolbars, tab bars e controles de navegação vão para a lateral, no eixo vertical, exceto na tela interna em retrato; não sobrescreva esse posicionamento (`hig/00 designing-for-iphone-duo`).
- Regiões reservadas (câmeras e dobra); grades com número par de colunas; evite mudanças extremas de layout ao dobrar (`hig/00 designing-for-iphone-duo`).
- As quatro sessões técnicas sobre o iPhone Duo não têm transcrição nesta base (Seção 8).

### CarPlay
- Feito para quem dirige: nada deve exigir o iPhone, que pode estar no porta-malas; erros aparecem no CarPlay; sem reprodução automática e sem mudar o volume geral; conteúdo importante na metade superior (`hig/14 carplay`).
- A próxima geração do sistema de design do CarPlay é co-marcada com a montadora: não deve parecer só Apple nem cópia do sistema nativo (`vid/14 wwdc2024_10112`).

---

## 5. Evolução do pensamento de design da Apple por período

A leitura por período usa as sessões presentes na base. Onde um vídeo não tem data no arquivo, a data não é inferida além da versão de sistema citada na própria fala.

### 2014 a 2016: método, prototipagem e o nascimento do relógio
- O método aparece explícito: fazer apps falsos, mostrar a pessoas e aprender com o feedback, subindo a fidelidade de imagens para animação e interação (`vid/02 wwdc2014_223`); definir o app pela audiência e pelas metas, gerar onze alternativas antes de criticar (`vid/02 wwdc2016_805`). O Keynote é tratado como ferramenta real de design.
- O Apple Watch força uma mentalidade própria: comunicação pessoal, design holístico com o bezel, interação leve medida em segundos, e a lista de dez armadilhas (`vid/02 wwdc2015_802`, `wwdc2015_805`).
- Em jogos, "technology alone is not enough": fricção zero no primeiro contato, ensinar jogando, desenhar para toque em vez de portar controles (`vid/02 wwdc2014_602`).

### 2017: os fundamentos nomeados
- "Essential Design Principles" nomeia a base conceitual: "human interface" em vez de "user interface", wayfinding, feedback, visibility, consistency, mental models, proximity, grouping, mapping, affordance, progressive disclosure e symmetry, e lembra que as HIG remontam a 1978 (`vid/03 wwdc2017_802`).
- Uma série curta cobre cada ofício separadamente: alertas, glifos, ícones de app, fontes, cor P3, som, público global, primeira abertura, notificações ricas, prototipagem em 60 segundos, comunicação entre design e engenharia, size classes (`vid/03` inteiro).
- A geometria do iPhone X introduz Safe Area e o princípio de preencher a tela sem cortar controles (`vid/01 tech-talks_801`, pela versão iOS 11 citada).

### 2018: fluidez, intenção e qualidade
- A interface passa a ser descrita como extensão da mente e do corpo: resposta, redirecionamento, molas e projeção de momento, a partir do trabalho no gesto do iPhone X (`vid/04 wwdc2018_803`).
- Intenção e qualidade viram tema: simplificação radical, foco extremo, personalidade e comunicação direta (`vid/04 wwdc2018_802`); qualidade como tempo, esforço e cuidado (`vid/04 wwdc2018_801`); a vida inteira de um botão (`vid/04 wwdc2018_804`).
- Notificações ganham entrega silenciosa e agrupamento; interromper vira privilégio (`vid/04 wwdc2018_806`). Apresentar o trabalho de design passa a ser tratado como parte do ofício (`vid/04 wwdc2018_811`).

### 2019: sistema e sentidos
- iOS 13 redefine o sistema: Dark Mode com cores semânticas, materiais, fundos base e elevated, sheets em cartão, context menu no lugar do Peek and Pop, e o lançamento dos SF Symbols (`vid/05 wwdc2019_808`, `wwdc2019_206`).
- Som e háptica tornam-se design com princípios próprios (causalidade, harmonia, utilidade) e API própria (`vid/05 wwdc2019_810`, `wwdc2019_520`).
- Acessibilidade visual em primeira classe: Dynamic Type, Reduce Motion, Differentiate Without Color (`vid/05 wwdc2019_244`).
- Machine learning ganha linguagem de design: múltiplas opções, atribuição, confiança traduzida, limitações, calibração e correções (`vid/06 wwdc2019_803`). Apps de iPad chegam ao Mac com a regra de repensar, não portar (`vid/05 wwdc2019_809`).

### 2020: adaptação, inteligência e precisão
- iPadOS ganha identidade própria (sidebar, navegação achatada, ponteiro com precisão adaptativa) (`vid/07 wwdc2020_10206`, `wwdc2020_10640`).
- iOS 14 aproxima os menus do toque e do Mac; widgets e App Clips inauguram o app como camada contextual que aparece no lugar e na hora certa (`vid/07 wwdc2020_10205`, `wwdc2020_10103`, `wwdc2020_10172`).
- Inteligência é declarada prática de design e privacidade, direito humano (`vid/07 wwdc2020_10086`; `vid/08 wwdc2020_10087`, `wwdc2020_10088`, `wwdc2020_10200`).
- watchOS 7 troca menus ocultos por ações visíveis (`vid/07 wwdc2020_10171`); macOS Big Sur adota sidebars de altura total e toolbars unificadas (`vid/08 wwdc2020_10104`); privacidade de localização e tipografia de interface recebem sessões dedicadas (`vid/07 wwdc2020_10162`, `wwdc2020_10175`).

### 2021: inclusão e descobribilidade
- Inclusão vira processo com fases, eixos de diversidade e interseccionalidade (`vid/10 wwdc2021_10304`) e prática em conteúdo, linguagem, cor e formulários (`vid/09 wwdc2021_10275`); acessibilidade descrita como missão central do Apple Watch (`vid/09 wwdc2021_10308`).
- Descobribilidade substitui tutoriais: priorizar, dar pistas visuais, sugerir gestos com botão equivalente, organizar por comportamento, dar controle sobre personalização (`vid/09 wwdc2021_10126`).
- SF Symbols 3 traz os modos hierarchical e palette; ações de Shortcuts devem ser úteis, modulares, multimodais, claras e descobríveis (`vid/09 wwdc2021_10097`, `wwdc2021_10283`). Interação espacial entre dispositivos aparece com o chip U1 (`vid/09 wwdc2021_10245`).

### 2022: clareza de conteúdo e linguagem
- Gráficos ganham duas sessões sobre quando e como usar (`vid/11 wwdc2022_110342`, `wwdc2022_110340`); escrita para interfaces ganha o método PACE (`vid/11 wwdc2022_10037`); navegação no iOS é reorganizada em torno de abas que refletem hierarquia (`vid/11 wwdc2022_10001`).
- Localização estrutural para o árabe (`vid/12 wwdc2022_110441`; `vid/11 wwdc2022_10034`); SF ganha larguras e SF Symbols 4 ganha variable color (`vid/11 wwdc2022_110381`, `wwdc2022_10157`).
- iPad com janelas redimensionáveis pede toolbars reorganizadas e menus de documento (`vid/11 wwdc2022_10009`).

### 2023: computação espacial e o redesenho do relógio
- O visionOS chega com princípios de design espacial, entrada por olhos e mãos, ciência de visão e movimento, UI espacial e som imersivo; a familiaridade com o iOS é mantida de propósito (`vid/13 wwdc2023_10072`, `_10073`, `_10076`, `_10078`, `_10271`).
- watchOS 10 é descrito como a maior mudança desde o lançamento: Smart Stack, grid derivado da curvatura da tela, Digital Crown como navegação (`vid/13 wwdc2023_10026`, `_10138`, `_10309`).
- SF Symbols 5 dá movimento aos símbolos; Live Activities ganham layouts por contexto; TipKit formaliza a educação no app (`vid/13 wwdc2023_10197`, `_10194`, `_10229`).

### 2024: amadurecimento espacial e unificação
- visionOS domina as sessões de design do ano: key moment, ambientes, hover customizado, entrada em jogos, experiências narrativas; testar no dispositivo é repetido como regra (`vid/14` insights; `vid/14 wwdc2024_10086`, `_10096`, `_10152`).
- Tab bar e sidebar passam a ser a mesma estrutura no iPadOS 18; animações do SwiftUI passam a animar UIKit e AppKit (`vid/14 wwdc2024_10147`, `_10145`).
- "Anything your app does should be an app intent" amplia o papel das superfícies do sistema (`vid/14 wwdc2024_10176`); personalidade por voz e tom ganha exercícios práticos (`vid/14 wwdc2024_10140`).

### 2025: Liquid Glass
- Um novo material unifica a linguagem visual entre plataformas: camada funcional sobre o conteúdo, lensing, adaptação contínua, concentricidade, variantes Regular e Clear; a Apple o situa numa linhagem que passa pelo Aqua, pelos blurs do iOS 7, pelo iPhone X, pela Dynamic Island e pelo visionOS (`vid/16 wwdc2025_219`, `wwdc2025_356`).
- Ícones, controles, toolbars, sheets e busca são redesenhados; o recado recorrente é remover customizações antigas para o material trabalhar (`vid/15 wwdc2025_323`, `_284`, `_361`; `vid/16 wwdc2025_220`).
- Os fundamentos voltam em forma de processo (estrutura, navegação, conteúdo, design visual) e de escrita enxuta (`vid/15 wwdc2025_359`, `_404`); inclusão é redefinida pela lacuna de inclusão (`vid/16 wwdc2025_316`).
- Na série Meet with Apple, equipes externas relatam a adoção: marca na camada de conteúdo, busca na base, prototipagem no dispositivo, cautela com desempenho do vidro (`vid/00` inteiro).

### 2026: consolidação dos princípios e do método
- "Principles of great design" reescreve os princípios em nove, acrescentando Forgiveness, e trata IA como responsabilidade de quem projeta (`vid/17 wwdc2026_250`).
- Marca ganha modelo explícito de duas camadas (UI e conteúdo) (`vid/17 wwdc2026_251`); nomear funcionalidades vira método (`vid/17 wwdc2026_290`); busca volta a ser decisão de posição e escopo (`vid/17 wwdc2026_292`).
- Agentes de código entram no processo de exploração, sob supervisão humana (`vid/17 wwdc2026_227`); ambientes imersivos seguem pré-produção, produção e pós-produção (`vid/17 wwdc2026_234`).
- As diretrizes ganham a página do iPhone Duo, com change log de 9 de setembro de 2026 (`hig/00 designing-for-iphone-duo`).

Três linhas atravessam todos os períodos e mostram continuidade, não ruptura: prototipar e testar com pessoas reais (2014 a 2026), a camada de interface que cede ao conteúdo (de "content first" em 2019 ao modelo de duas camadas em 2026) e a acessibilidade que passa de tema de sessão a condição de todas as sessões.

---

## 6. Anti-padrões que a Apple condena explicitamente

Estrutura e navegação
1. Menu hambúrguer para esconder a navegação principal (`vid/03 wwdc2017_802`; `vid/09 wwdc2021_10126`; `vid/15 wwdc2025_359`).
2. Esconder, desabilitar ou trocar abas automaticamente; usar tab bar para ações; aba "Home" genérica que duplica outras abas (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`; `vid/04 wwdc2018_802`).
3. Modal usado porque a animação agrada, modal que vira "app dentro do app", modais empilhados, mais de um alerta ao mesmo tempo (`vid/05 wwdc2019_808`; `hig/03 modality`; `hig/09 sheets`, `popovers`; `vid/11 wwdc2022_10001`).
4. Colocar todas as ações de uma view atrás de um único botão ou esconder ação primária num menu "More" (`hig/07 pull-down-buttons`; `vid/07 wwdc2020_10205`, `wwdc2020_10171`).
5. Deixar a única forma de fazer algo num gesto, num context menu, num menu dinâmico com tecla modificadora ou numa interação de proximidade (`hig/07 context-menus`, `the-menu-bar`; `hig/13 gestures`, `nearby-interactions`; `vid/09 wwdc2021_10126`).
6. Esconder itens de menu indisponíveis na menu bar em vez de esmaecê-los (`hig/07 the-menu-bar`; `vid/15 wwdc2025_208`).
7. Aninhar scroll views na mesma orientação (`hig/09 scroll-views`).

Interface e sistema
8. Recriar componentes do sistema (janelas, context menus, player de vídeo, confirmação de compra) sem necessidade; a réplica imperfeita parece quebrada ou datada (`hig/09 windows`; `hig/03 playing-video`; `hig/15 in-app-purchase`; `vid/05 wwdc2019_808`; `vid/17 wwdc2026_251`).
9. Redefinir gestos e atalhos padrão para outras funções, ou inventar gesto novo para ação padrão (`hig/13 gestures`, `keyboards`, `pointing-devices`; `hig/04 undo-and-redo`).
10. Liquid Glass na camada de conteúdo, vidro sobre vidro, misturar variantes Regular e Clear, fundos customizados em barras (`hig/02 materials`; `vid/16 wwdc2025_219`, `wwdc2025_356`; `vid/15 wwdc2025_284`; `vid/00 meet-with-apple_256`, glass aninhado).
11. Scroll edge effect como decoração ou onde não há interface flutuante (`hig/09 scroll-views`; `vid/16 wwdc2025_356`).
12. Botão customizado sem estado de pressão; botões que não parecem botões; forma de botão em conteúdo não clicável (`hig/07 buttons`; `vid/02 wwdc2015_805`).
13. Primary role num botão destrutivo; Cancel como botão padrão num alerta destrutivo (`hig/07 buttons`; `hig/09 alerts`).
14. Ações destrutivas em menus rápidos sem confirmação em outro lugar (`vid/07 wwdc2020_10205`).
15. Ponteiro com magnetismo sem forma customizada; efeitos de ponteiro decorativos; texto instrucional junto ao ponteiro (`vid/07 wwdc2020_10640`; `hig/13 pointing-devices`).

Marca e cor
16. Launch screen como tela de marca; logo repetido pelo app; marca competindo com o conteúdo (`hig/01 branding`; `hig/03 launching`; `vid/17 wwdc2026_251`).
17. Cor como único meio de transmitir informação; cor fixa no código; redefinir semântica de cores do sistema; tintar tudo (`hig/01 color`, `accessibility`; `vid/16 wwdc2025_219`).
18. Ajuste de aparência próprio do app no lugar do Dark Mode do sistema (`hig/01 dark-mode`).
19. Usar Activity rings, ícone Apple Health, AirPlay ou Apple Pay mark como decoração, botão ou elemento alterado (`hig/11 activity-rings`; `hig/15 healthkit`; `hig/14 airplay`, `apple-pay`).
20. SF Symbols em ícones de app ou logotipos; réplicas de hardware Apple (`hig/02 sf-symbols`; `hig/01 app-icons`, `icons`).

Ícones
21. Texto, fotos ou screenshots da interface no ícone do app; sombras, chanfros e brilhos assados; exportar a camada já com a máscara (`hig/01 app-icons`; `vid/15 wwdc2025_361`; `vid/16 wwdc2025_220`).
22. Emoji no lugar de símbolo em quick actions (`hig/07 home-screen-quick-actions`).

Permissões, dados e confiança
23. Pedir permissões ao abrir o app sem necessidade; telas de pré-alerta com "Allow" ou que induzem no rastreamento (`hig/02 privacy`; `vid/03 wwdc2017_816`; `vid/17 wwdc2026_250`).
24. Exigir conta antes de mostrar valor; pedir senha a quem usa Sign in with Apple; enterrar a exclusão de conta (`hig/03 managing-accounts`; `hig/16 sign-in-with-apple`).
25. Notificações para marketing sem consentimento, Time Sensitive para promoção, várias notificações para o mesmo assunto, notificação só para abrir o app, badge para outra coisa que não mensagens não lidas (`hig/03 managing-notifications`; `hig/12 notifications`; `vid/04 wwdc2018_806`).
26. Dificultar o cancelamento de assinatura (`hig/15 in-app-purchase`).
27. IA que faz a pessoa pensar que fala com um humano, automatiza ações destrutivas ou apresenta fatos sem dados verificados (`hig/14 generative-ai`); porcentagens cruas de confiança e atribuições que supõem gostos ("love") (`hig/15 machine-learning`; `vid/06 wwdc2019_803`).

Feedback, onboarding e texto
28. Tutoriais longos obrigatórios, onboarding que ensina o sistema, seta ou mão flutuante indicando onde tocar (`hig/03 onboarding`; `vid/03 wwdc2017_811`; `vid/09 wwdc2021_10126`).
29. Alerta ao iniciar o app, alerta só informativo, alerta para ação comum e desfazível, alerta com código de erro, alerta como remendo de problema evitável (`hig/09 alerts`; `vid/03 wwdc2017_813`).
30. Pedir avaliação no primeiro lançamento ou no meio de uma tarefa (`hig/03 ratings-and-reviews`).
31. Indicador de progresso parado ou com ritmo irreal; descrições vagas como "carregando" (`hig/11 progress-indicators`).
32. "Yes" e "No" em botões, "OK" ambíguo, "Confirm" genérico, "oops", "Click here", jargão e preenchimento (`hig/09 alerts`; `hig/02 writing`; `vid/11 wwdc2022_10037`, `wwdc2022_10169`; `vid/15 wwdc2025_404`).
33. Escolher fonte pelo nome combinar com o tema, a "Lack of Typographic Imagination" (`vid/03 wwdc2017_815`).

Plataformas e corpo
34. Portar a interface de uma plataforma para outra: Watch como iPhone em miniatura, controles de console sobrepostos no toque, layout de iPad escalado no Mac (`vid/02 wwdc2015_802`, `wwdc2014_602`; `hig/15 mac-catalyst`).
35. No visionOS: conteúdo preso à cabeça, profundidade no texto, oscilação perto de 0,2 Hz, movimento na periferia, girar o mundo, janelas demais, exigir movimento físico, gestos customizados sem necessidade (`hig/02 spatial-layout`, `motion`; `vid/13 wwdc2023_10078`; `vid/14 wwdc2024_10094`).
36. No CarPlay, exigir o iPhone ou mostrar erros nele (`hig/14 carplay`).
37. Truncar texto quando o tamanho aumenta, ignorar preferências de acessibilidade porque o efeito faz parte da identidade (`vid/05 wwdc2019_244`; `vid/08 wwdc2020_10020`).

---

## 7. Checklist de revisão de uma interface no padrão Apple

Responder sim ou não. Cada pergunta indica a fonte que a sustenta.

Propósito e estrutura
1. Cada tela responde com clareza "onde estou", "o que posso fazer" e "para onde posso ir"? (`vid/15 wwdc2025_359`; `vid/03 wwdc2017_802`)
2. Cada funcionalidade presente tem propósito claro para quem usa, e o que não é essencial foi cortado ou movido para divulgação progressiva? (`hig/00 design-principles`; `vid/17 wwdc2026_250`; `hig/01 layout`)
3. As abas representam a hierarquia real, com rótulos curtos e específicos, sem ações na tab bar e sem aba genérica que duplica outras? (`hig/08 tab-bars`; `vid/11 wwdc2022_10001`)
4. Push é usado para descer na hierarquia e modal só para tarefa autocontida, com título que nomeia a tarefa e saída óbvia? (`vid/11 wwdc2022_10001`; `hig/03 modality`)
5. O conteúdo está ordenado por importância, do topo e da borda inicial, e agrupado por comportamento real? (`hig/01 layout`; `vid/09 wwdc2021_10126`)
6. Toda ação disponível em gesto, context menu ou menu escondido também existe num lugar visível? (`hig/07 context-menus`; `hig/13 gestures`; `vid/09 wwdc2021_10126`)

Sistema e plataforma
7. Componentes, símbolos e comportamentos do sistema foram usados onde existem, e cada customização tem razão explícita? (`hig/03`, insight 4; `vid/03 wwdc2017_809`; `vid/17 wwdc2026_251`)
8. O layout usa size classes, safe areas e margens, e mantém a mesma funcionalidade quando o tamanho muda, sem mudanças destrutivas? (`hig/01 layout`; `vid/15 wwdc2025_208`)
9. A interface foi desenhada para esta plataforma, e não portada de outra? (`vid/07 wwdc2020_10206`; `vid/02 wwdc2015_802`; `hig/15 mac-catalyst`)
10. No Mac, todo comando está na menu bar, com atalhos padrão, e itens indisponíveis aparecem esmaecidos? (`hig/07 the-menu-bar`, `toolbars`)

Conteúdo e marca
11. O conteúdo é o elemento dominante, e a marca vive na camada de conteúdo, sem logo repetido e sem launch screen de marca? (`hig/01 branding`; `hig/03 launching`; `vid/17 wwdc2026_251`)
12. O Liquid Glass está só na camada de controles e navegação, sem vidro sobre vidro, sem fundos customizados nas barras e com a variante certa? (`hig/02 materials`; `vid/16 wwdc2025_219`, `wwdc2025_356`)

Tipografia e cor
13. O texto usa text styles do sistema ou fonte customizada com Dynamic Type, respeitando tamanho padrão e mínimo da plataforma? (`hig/02 typography`; `hig/01 accessibility`)
14. A interface continua legível, sem truncar informação útil, no maior tamanho de acessibilidade? (`hig/02 typography`; `vid/05 wwdc2019_244`)
15. O contraste atinge 4,5:1 para texto até 17 pt e 3:1 para texto de 18 pt ou em negrito, nos modos claro, escuro e de contraste aumentado? (`hig/01 accessibility`, `dark-mode`)
16. Nenhuma informação depende só de cor? (`hig/01 color`; `vid/05 wwdc2019_244`)
17. As cores são semânticas, com variantes clara, escura e de contraste aumentado, e a cor de destaque aparece só em ações primárias e estados? (`hig/01 color`, `branding`; `vid/15 wwdc2025_323`)

Interação e feedback
18. Todo alvo interativo atende ao mínimo da plataforma (44 x 44 pt no iOS, 60 pt no visionOS, 28 x 28 pt no Mac) com espaçamento adequado? (`hig/01 accessibility`; `hig/07 buttons`)
19. Todo controle customizado tem estados normal, pressionado e desabilitado, e responde de imediato? (`hig/07 buttons`; `vid/03 wwdc2017_811`; `vid/04 wwdc2018_804`)
20. Gestos seguem o padrão da plataforma, podem ser interrompidos e têm alternativa por botão? (`hig/13 gestures`; `vid/04 wwdc2018_803`; `hig/01 accessibility`)
21. Ações destrutivas usam estilo destrutivo, ficam fora de menus rápidos, podem ser desfeitas ou pedem confirmação quando a perda é inesperada e irreversível? (`hig/03 feedback`; `hig/04 undo-and-redo`; `vid/07 wwdc2020_10205`)
22. Progresso é determinado sempre que possível, sempre em movimento e com opção de cancelar? (`hig/11 progress-indicators`)
23. O carregamento mostra algo o quanto antes e nunca deixa tela vazia? (`hig/03 loading`)
24. Animações têm propósito, são breves, respeitam Reduce Motion e não bloqueiam a próxima ação? (`hig/02 motion`; `hig/01 accessibility`)
25. Háptica e som seguem significados documentados, estão sincronizados com o visual, são raros e desligáveis? (`hig/03 playing-haptics`; `vid/05 wwdc2019_810`; `vid/03 wwdc2017_803`)

Escrita
26. Botões usam verbos específicos, sem "Yes" e "No" e sem "OK" ambíguo? (`hig/02 writing`; `hig/09 alerts`; `vid/11 wwdc2022_10037`)
27. Mensagens de erro ficam perto do problema, não culpam e dizem como corrigir? (`hig/02 writing`; `vid/03 wwdc2017_813`)
28. O texto foi lido em voz alta e está sem preenchimento, repetição, jargão ou termos de implementação? (`vid/15 wwdc2025_404`; `vid/11 wwdc2022_10037`; `hig/15 healthkit`, `nfc`)
29. Capitalização e terminologia são consistentes, com uma lista de palavras do app? (`hig/02 writing`; `vid/15 wwdc2025_404`)
30. Estados vazios dizem o próximo passo, e a busca vazia mostra o termo pesquisado? (`hig/02 writing`; `vid/17 wwdc2026_292`)

Responsabilidade
31. Permissões são pedidas no momento em que a funcionalidade precisa, com purpose string específica, e só para o necessário? (`hig/02 privacy`; `vid/03 wwdc2017_816`; `vid/07 wwdc2020_10162`)
32. A pessoa consegue usar o app sem conta até que a conta seja essencial, e consegue excluir a conta dentro do app? (`hig/03 managing-accounts`)
33. Alertas e notificações têm urgência honesta, são raros e acionáveis, e o badge conta só não lidas? (`hig/03 managing-notifications`; `hig/09 alerts`; `hig/12 notifications`)
34. Recursos de IA indicam onde há IA, permitem desfazer e refazer, avisam sobre erros e têm salvaguardas para danos? (`hig/14 generative-ai`; `vid/17 wwdc2026_250`)

Acessibilidade e inclusão
35. Todos os elementos têm rótulos de VoiceOver descritivos, imagens decorativas estão excluídas e a ordem de leitura é lógica? (`hig/16 voiceover`; `vid/09 wwdc2021_10275`)
36. Linguagem, imagens, nomes e opções de gênero incluem as pessoas, sem estereótipos? (`hig/01 inclusion`; `vid/09 wwdc2021_10275`)
37. O app funciona com Switch Control, Voice Control, Full Keyboard Access e sem depender de um único sentido? (`hig/01 accessibility`; `vid/16 wwdc2025_316`)

Processo
38. A interface foi testada no dispositivo real, no contexto real e com pessoas do público, sem defender o design durante o teste? (`vid/02 wwdc2014_223`; `vid/03 wwdc2017_818`; `vid/16 wwdc2025_303`)

---

## 8. Limites desta base

- A camada de texto veio de texto e a camada visual veio de imagens efetivamente vistas. Os 18 arquivos de `kb/hig/` e os 18 de `kb/videos/` foram destilados do texto das diretrizes e das transcrições. O capítulo 9, as seções "O que as ilustrações mostram" nos artigos e as seções "O que as imagens mostram" nos cartões vieram das folhas de quadros e de ilustrações, cada uma com código conferido.
- As ilustrações das diretrizes foram vistas: 552 folhas cobrindo 1.342 imagens e os 61 vídeos de demonstração das próprias páginas. Cada artigo com ilustração traz a seção "O que as ilustrações mostram". O texto alternativo continua citado quando a imagem não deixa ler algo, e as divergências entre imagem e descrição oficial estão registradas.
- Os quadros dos vídeos foram vistos: 3.072 folhas de 175 vídeos, com um quadro a cada mudança de cena e pelo menos um a cada 12 segundos, o que dá 26.869 quadros de 63,3 horas. Cada cartão em `kb/videos/` diz quantas folhas foram vistas. Movimento contínuo aparece como diferença entre quadros parados, e efeito rápido demais para o intervalo pode não aparecer.
- As sessões sem transcrição oficial ganharam transcrição automática local, feita com Whisper e marcada como não oficial no próprio cartão: `meet-with-apple_270`, `meet-with-apple_274`, `tech-talks_111461`, `tech-talks_111462`, `tech-talks_111463`, `tech-talks_111466`, `wwdc2020_20022` e `wwdc2026_8012`. Treze vídeos não têm arquivo nem transcrição na origem e seguem sem cartão.
- A sessão `wwdc2023_10115` ganhou cartão próprio, escrito a partir da transcrição oficial inteira e conferido frase a frase contra ela.
- Tabelas extensas não foram reproduzidas nos arquivos destilados: as tabelas completas de tracking por tamanho de ponto, as tabelas de valores RGB das cores do sistema e partes das tabelas de dimensões de complicações e widgets ficaram resumidas (`hig/02 typography`; `hig/01 color`; `hig/12`). Os números da Seção 3 são os que os arquivos trazem.
- Divergências entre fontes foram mantidas à vista em vez de resolvidas: oito princípios nas diretrizes e nove na sessão de 2026; safe area lateral do tvOS de 80 pt nas diretrizes e 90 pt na sessão de 2019; altura máxima de snippet de 400 pt nas diretrizes e 340 pt na sessão de 2025; ajuste de fonte RTL de cerca de 2 pt nas diretrizes e 10% na sessão sobre árabe; ponteiro do iPadOS com magnetismo em 2020 e sem magnetismo em 2025. Diretrizes e sessões são de momentos diferentes; a mais recente não foi presumida como correta sem que a fonte diga.
- Números falados nas sessões (estatísticas de população, métricas de apps parceiros, taxas de conversão) são contexto das falas, não diretrizes, e não foram verificados em outra fonte.
- Há sobreposição de conteúdo entre sessões registradas com ids diferentes (`wwdc2019_223` reúne `wwdc2019_520` e `wwdc2019_810`; `wwdc2022_10034` e `wwdc2022_110441`; versões em ASL de 2021 e 2022), e sessões que não tratam de design de interface (`wwdc2019_239`, `wwdc2021_10317`, boa parte de `wwdc2025_247`). Um cartão de `vid/14` (`wwdc2024_10086`) contém uma observação alheia ao vídeo, sinalizada no próprio arquivo, que foi ignorada.
- As durações registradas na primeira coleta estavam associadas ao vídeo errado por erro de coleta; foram corrigidas em 15/09/2026 pela medição dos arquivos, que confere com o servidor da Apple.
- Esta síntese não afirma que as sessões presentes esgotam o catálogo de design da Apple nem que as diretrizes estão completas; ela cobre exatamente os 36 arquivos indicados.

---

## O que só as imagens mostram

Este capítulo vem de uma camada de leitura que não existia quando as seções anteriores foram escritas. As 3.072 folhas de quadros extraídos dos vídeos e as 552 folhas de ilustrações das diretrizes foram vistas uma a uma, destiladas em 333 sínteses visuais com o código de cada folha conferido, e consolidadas nos 14 arquivos de `kb/essencia_visual/`. O que segue é paráfrase dessas sínteses. Cada item traz entre parênteses onde foi visto: a página das diretrizes pelo slug do artigo e o número da imagem, a sessão pelo id e a folha de quadros. Itens sustentados por uma fonte só estão marcados como fonte única. Isso preenche em parte o limite declarado na seção 8, que registrava que os quadros dos vídeos ainda não tinham sido vistos e que as imagens das diretrizes só haviam entrado pelo texto alternativo.

### Grade, medida e espaçamento

1. Medida de componente é ensinada como relação, não como número: setas duplas cotam largura, altura e respiro sem nenhum valor impresso. A notação, porém, não é rígida. Em `hig image-views` (img 0628) e `hig ornaments` (img 0825) a seta horizontal fica acima para a largura e a vertical à direita para a altura, mas em `hig panels` (img 0835) a horizontal desce para baixo do componente, e em `hig boxes` (img 0183) e `hig collections` (img 0252) as quatro setas cotam padding, margem e espaçamento entre células, não largura e altura.
2. O número só aparece onde existe contrato: arquivo a exportar, marca de terceiro, área reservada pelo sistema (`hig apple-pay` img 0144 e 0145, altura mínima de 30, larguras mínimas de 100 e 140 e margem de um décimo da altura; `hig game-center` img 0496, 0497, 0500, 0501, 0505 e 0511, máscaras e cortes cotados em pt; `hig icons` img 0623, margem de 10 por cento como única medida numérica de uma página de 29 folhas).
3. A área segura do tvOS é desenhada como faixa rosa com os valores escritos em vermelho, e as imagens confirmam a divergência entre as duas fontes: 60 no topo e na base com 80 nas laterais na prancha das diretrizes, contra 60 e 90 no slide da sessão de 2019, que ainda cota o Carousel em 125, 365 e 90 (`hig layout` img 0686; `vid wwdc2019_211` folha 0019).
4. O alvo de toque é maior que o desenho pintado, e a folga dobra quando o botão não tem moldura própria: 12 de cada lado para o botão com bezel, 24 para o símbolo pequeno e para o botão só de texto (`hig pointing-devices` img 0861 a 0863; `vid wwdc2020_10640` folha 0018; `vid wwdc2023_10076` folha 0009, retângulo de 60pt em volta do coração com 8pt de margem interna nos quatro lados).
5. Os pisos do sistema aparecem escritos na tela, e em vários vídeos o número não é dito na fala: um slide inteiro traz só "44 x 44" e "Points" (`vid wwdc2017_811` folha 0005). A tabela que emparelha cada valor com o componente no tamanho real, 17 pontos de corpo padrão com 11 de mínimo e 28 pontos de alvo padrão no Mac, tem fonte única (`vid wwdc2024_10085` folhas 0010 e 0011), e ali a relação se inverte: as notas registram valores ditos na fala que a tela nunca chega a mostrar.
6. A camada de anotação tem cor própria e nunca se confunde com a interface: rosa e vermelho marcam espaço reservado e cota nas diretrizes, amarelo faz o mesmo papel nas sessões, e o verde água e o laranja pontilhado entram quando três grandezas precisam conviver no mesmo quadro (`hig layout` img 0686 e 0687; `hig app-clips` img 0069 e 0070; `vid wwdc2023_10076` folhas 0009 a 0015; `vid wwdc2020_10207` folha 0016).
7. O raio de canto de um elemento colado à borda é derivado do raio da tela e do afastamento, não escolhido à mão (`vid meet-with-apple_257` folha 0007, os cantos dos cartões internos acompanhando a curvatura do próprio aparelho; `vid wwdc2023_10076` folha 0011, o rótulo somando raio interno e padding sobre a mesma célula de álbum). Só uma das fontes isola a geometria com cor chapada e nenhum conteúdo dentro, o verde preenchendo a tela inteira até coincidir com o contorno do aparelho (`vid tech-talks_111461` folha 0005).
8. Mais espaço vira mais informação, nunca informação maior: o que se multiplica é coluna, linha ou seção, e a escala tipográfica fica onde está (`hig widgets` img 1287 a 1290, o widget de Calendário ganha colunas e régua de horas até estender a quatro dias; `hig designing-for-iphone-duo` img 0437 e 0438, quatro colunas por quatro linhas na tela externa e seis por quatro na interna; `vid tech-talks_111461` folha 0001).
9. Centragem óptica é ensinada como deslocamento medido, com o glifo subindo alguns pixels e o padding absorvendo a diferença, e a guia chegando a entrar por dentro do desenho (`hig icons` img 0564 a 0566; `vid wwdc2020_10207` folhas 0010 e 0011; `vid wwdc2019_206` folha 0019, deslocamentos de linha de base anotados em menos 3,5 e mais 4,5).

### Hierarquia e tipografia

10. A escala tipográfica é entregue como tabela com o tamanho em pontos declarado, em duas formas que não se repetem entre si: cada linha renderizada no próprio estilo que nomeia, do título grande em 34 até as legendas em 12 e 11 (fonte única: `vid wwdc2025_359` folha 0012), e matriz cruzando categoria de tamanho de conteúdo com estilo de texto, com o valor em pontos em cada célula (fonte única: `vid tech-talks_802` folha 0005).
11. A diferença de escala tipográfica entre macOS e iOS é resolvida por um fator único: a coluna do Mac traz 13, 11 e 9 pontos, e a do iOS só ganha valores quando o rótulo vira escala de 77 por cento, chegando a 26,2 no título grande e 7,7 na legenda menor (fonte única: `vid wwdc2019_809` folha 0012).
12. A hierarquia de texto é uma escala de contraste decrescente, sempre na mesma ordem e sem caixa, borda ou cor nova. Em quatro níveis aparece como rótulo, secundário, terciário e quaternário (`hig dark-mode` img 0422 a 0424, a mesma escala repetida sobre preto, sobre cinza escuro elevado e sobre branco) e como título, subtítulo, placeholder e desabilitado (`vid wwdc2019_808` folhas 0005 e 0006). A mesma lógica aparece reduzida a três níveis, primário, secundário e terciário, em pílulas de opacidade decrescente (`vid wwdc2023_10138` folha 0013).
13. Ícone ao lado de texto é problema tipográfico, não gráfico: o alinhamento é provado com as guias de altura de caixa alta e linha de base desenhadas, e o símbolo fica ligeiramente acima da linha de base (`hig sf-symbols` img 1015 a 1017, o mesmo símbolo de mais ao lado da palavra em small, medium e large; `vid wwdc2020_10207` folha 0002; `vid wwdc2021_10097` folha 0003).
14. Igualar o valor numérico de corpo entre escritas diferentes produz desequilíbrio e não consistência: no mesmo corpo só o latim toca as duas guias, e o árabe e o hebraico ficam equilibrados com corpo um pouco maior (fonte única: `hig right-to-left` img 0953 e 0954).
15. A caixa precisa ser projetada para crescer: a mesma caixa de confirmação fica visivelmente mais alta em tailandês, e o cabeçalho de dia por extenso em árabe ocupa muito mais espaço que a letra única do inglês, com a estrutura de componentes idêntica (`vid wwdc2022_10037` folhas 0014 e 0015; `vid wwdc2022_110381` folha 0010, a mesma tela em espanhol, inglês e chinês com só o texto mudando).
16. A degradação entra como assunto de projeto: as pranchas mostram o que some primeiro quando o espaço falta, e mostram o estrago quando nada foi decidido (`hig toolbars` img 1164 e 1165, o menu de overflow recolhe inclusive o próprio botão More; `hig typography` img 1199 e 1200, no maior tamanho de acessibilidade o nome quebra em duas linhas e os ícones do rodapé se sobrepõem ao texto; `hig text-fields` img 1140 a 1142, corte na borda, quebra em duas linhas e truncamento com reticências; `vid wwdc2022_10009` folha 0005, os ícones da seção central da barra somem antes dos grupos das pontas).
17. A leitura começa pela conclusão em linguagem comum e desce para a evidência: título, frase curta, e só então o gráfico ou a pilha de ações (`hig charts` img 0242; `hig column-views` img 0342; `hig action-sheets` img 0025).
18. Quando existe um valor que importa, ele ocupa a tela sozinho em corpo enorme com legenda mínima (`vid meet-with-apple_274` folha 0007; `vid wwdc2017_803` folha 0012; `vid wwdc2019_803` folha 0011). O quadro vazio que antecede o dado, parte do mesmo recurso, aparece numa fonte só (`vid wwdc2025_247` folha 0001).
19. Símbolo tem métrica própria e é auditado em matriz de peso por escala, a mesma que a ferramenta entrega pronta em vez de calcular em tempo real (`hig sf-symbols` img 1014, 27 amostras do mesmo símbolo em nove colunas de Ultralight a Black por três linhas de escala; `vid wwdc2020_10207` folha 0010, template de exportação de três linhas por nove colunas; `vid wwdc2019_206` folhas 0008 e 0009).

### Cor, material e profundidade

20. Cor é publicada como valor verificável, não como impressão: cartão mínimo com os três valores RGB ao lado, repetido sobre fundo branco e sobre fundo preto com o valor idêntico nos dois (`hig color` img 0270 a 0341; `hig activity-rings` img 0031 a 0033, rosa avermelhado 250, 17, 79, verde limão 166, 255, 0 e ciano 0, 255, 246; `hig color-wells` img 0253, o valor RGB ligado por linha ao centro do botão).
21. A escala de cinzas do iOS vai de 28, 28, 30 a 242, 242, 247, e as pranchas mostram que nos extremos o contraste com o fundo praticamente desaparece, o mais claro sobre branco e o mais escuro sobre preto (fonte única: `hig color` img 0318 a 0341).
22. Nenhum estado vive só na matiz: ele é dobrado por forma, preenchimento, tamanho ou texto, e o custo de não fazer isso é demonstrado com rodas de cor simuladas para três tipos de daltonismo (`hig accessibility` img 0010 e 0011, dois círculos que só diferiam no tom ganham check branco no verde e octógono com X branco no vermelho; `hig charts` img 0243, sistólica em bolinhas e diastólica em losangos; `vid wwdc2019_244` folha 0005; `hig widgets` img 1296 a 1298, o verde semântico de alta desaparece quando a aparência tintada aplica um roxo único).
23. Modo escuro é troca de valores dentro de uma estrutura fixa: posição, réguas, cotas e cor de destaque não se movem, só fundo e luminosidade mudam (`hig color-wells` img 0253; `hig app-icons` img 0080 a 0082; `hig icons` img 0561 a 0567, o azul do item selecionado é idêntico nos dois modos e só as reticências trocam de preto para branco; `hig dark-mode` img 0413 e 0414).
24. Ilustração complexa no modo escuro não se resolve com borda: os valores internos são refeitos, com roupas, cadeiras e cabelos clareando, enquanto um ícone de forma única só precisa de contorno fino (fonte única: `hig dark-mode` img 0415 a 0419).
25. Material translúcido não tem cor própria, assume o tom do que está atrás, e por isso só pode ser julgado sobre conteúdo colorido de verdade (`hig materials` img 0771 a 0773, o mesmo círculo fica cinza escuro sobre céu estrelado e esbranquiçado sobre foto de praia; `hig color` img 0263; `vid wwdc2019_808` folha 0011, quatro níveis de material sobre um degradê laranja; `vid wwdc2026_8012` folha 0007, o canvas troca de cinza sólido para um gradiente e só então a refração aparece, voltando ao cinza em seguida).
26. Translucidez é testada contra o pior fundo possível, e não contra o fundo escolhido para o mockup (`vid wwdc2023_10076` folhas 0006 e 0007, o painel fica parado enquanto o vídeo de fundo troca por mar, elefante, campo verde e dinossauros; `vid wwdc2025_361` folha 0015, o mesmo ícone contra sete fundos em sequência; `vid wwdc2023_10072` folha 0003, a janela de vidro quase some contra a parede clara).
27. A gestão de gamut é mostrada como geometria e como consequência numérica: o triângulo do sRGB inteiramente contido no do Display P3, e o seletor de cor caindo de 255, 0, 0 para 236, 0, 0 e depois 234, 51, 35 na conversão (`hig color` img 0268; `vid wwdc2017_821` folha 0008).
28. Contraste é medido com o número na tela, e o valor reprovado aparece riscado ao lado do aprovado (`vid wwdc2019_808` folha 0008, razão anotada em cada painel com X vermelho e check verde; `vid wwdc2020_10020` folha 0009, calculadora com amostras, valores RGB e o resultado de 4,5 para 1 mais um selo informando quais tamanhos e pesos aquela razão atende; `vid wwdc2021_10275` folha 0023, a mesma caixa de diálogo de jogo em duas versões com a razão anotada ao lado de cada uma).
29. Em espaço tridimensional a hierarquia passa a vir de nitidez, transparência e distância, não de escala e sombra, e os painéis flutuam à frente da cena sem coincidir com o contorno do que está atrás (`hig app-icons` vídeo 004; `hig alerts` vídeos 002 e 003; `hig eyes` vídeo 009; `vid wwdc2023_10075` folha 0004; `vid wwdc2023_10072` folha 0012).
30. O vidro é reservado à moldura e ao chrome, com um único elemento opaco por composição, e o dado permanece sólido (`vid wwdc2024_10086` folha 0012; `vid wwdc2024_10116` folha 0002, barra de reprodução em vidro flutuando abaixo da tela e não acoplada a ela; `vid wwdc2023_10271` folha 0003).
31. A cápsula translúcida de cantos totalmente arredondados é a forma padrão do controle flutuante: a geometria fica constante e a adaptação acontece no tom herdado do fundo (`vid wwdc2025_219` folhas 0002, 0004 e 0006, a mesma cápsula de três ícones muda de tonalidade sobre flores amarelas e sobre duna sem mudar de forma; `hig tab-bars` img 1108; `hig typography` img 1194, nomes de plantas em cápsula translúcida para ficarem legíveis sobre o cenário).

### Estados, transição e movimento

32. Mudança de estado preserva a caixa: nada se desloca, cresce ou recompõe ao redor, e o espaço do estado final é reservado desde o inicial (`hig buttons` img 0191 e 0192, "Checkout" vira "Checking out" com spinner na borda inicial sem mudança perceptível de tamanho; `hig controls` img 0409 e 0410; `hig eyes` vídeo 009 folha 0002, o hover altera só o realce de fundo da linha mirada).
33. O quadro do meio é mostrado de propósito, porque é ele que ensina o mecanismo, e a especificação escrita costuma omiti-lo (`hig drag-and-drop` vídeo 008, o arquivo pousa primeiro como cartão plano rotulado e só então o objeto 3D nasce pequeno e cresce ganhando crateras; `hig buttons` vídeo 007, a tooltip surge com atraso e menor antes de atingir tamanho e opacidade finais; `vid wwdc2018_803` folha 0011, um terceiro quadrado rotulado "Hinting" aparece entre o estado inicial e o final; `vid wwdc2024_10116` folha 0002).
34. A propriedade animada é a que carrega significado, opacidade, tom ou preenchimento, enquanto posição e tamanho ficam parados (`hig gestures` vídeo 010 folha 0001, o fundo do botão de coração clareia de cinza translúcido até branco sólido sem nada mudar de lugar; `vid wwdc2018_804` folha 0010, estado pressionado feito só por escurecimento da mesma cor; `vid wwdc2021_10126` folha 0010, o obturador passa de translúcido a sólido conforme o reconhecimento avança).
35. Elementos irmãos animam fora de fase, porque animação simultânea em tudo lê como falha de renderização (fonte única: `hig sf-symbols` vídeos 045, 046 e 051, cada símbolo reduz e volta fora de fase dos outros e só uma camada pulsa por vez). A defasagem por camadas de velocidade diferente é o que monta a paralaxe do ícone de tvOS, com cartão e anel quase parados e o rosto varrendo a cena (`hig images` vídeo 012).
36. Foco e seleção são coisas distintas e precisam de duas linguagens visuais, sob pena de a pessoa achar que já escolheu quando só está navegando (`hig menus` img 0790 com preenchimento sólido para o momentâneo contra img 0796 com checkmark discreto na margem para o persistente; `hig pickers` img 0845 e 0846 contra img 0849; `vid wwdc2020_10205` folha 0004, marca de verificação no item ativo e realce de cor na linha em foco, dois tratamentos no mesmo menu).
37. O estado ativo se anuncia por área preenchida, quase nunca por sublinhado ou cor de texto sozinha, porque o preenchimento sobrevive a tela pequena, a daltonismo e a fundo com imagem (`hig segmented-controls` img 0996 a 0999; `hig tab-bars` img 1108; `hig outline-views` img 0826, linha selecionada em vermelho sólido com texto branco; `hig page-controls` img 0832 a 0834, o ponto da página atual é o único preenchido). O contorno não está proibido: na grade de símbolos a célula selecionada é marcada por contorno azul (`vid wwdc2022_10158` folhas 0002 e 0003).
38. O botão indisponível é o mesmo botão desbotado, não um botão cinza diferente: mantém a matiz e troca a saturação para continuar reconhecível (`hig researchkit` img 0927 e 0929, o mesmo amarelo em versão pálida enquanto nada foi selecionado; `hig buttons` img 0193 a 0196, o botão indisponível do visionOS aparece esmaecido ao lado do selecionado que inverte o contraste).
39. Espera sem previsão ganha forma própria e legenda, em vez de reaproveitar a barra determinada e prometer um fim que o sistema não pode cumprir (`hig progress-indicators` img 0911 e 0912, barra indeterminada como onda e spinner cinza sempre acompanhado de texto de estado; `hig tap-to-pay-on-iphone` img 1126, 1127 e 1132; `hig wallet` img 1265 e 1266, a barra verde parcial vira check quando entrega).
40. O vazio nunca é vazio: é a mesma caixa com preenchimento neutro, o que mantém ritmo e altura de linha estáveis entre carregando, sem dado e carregado (`hig widgets` img 1312 e 1313, três barras amarelas mais claras viram as três linhas de texto real; `hig workouts` img 1335, métrica sem dado preenchida com traços e o rótulo intacto; `vid wwdc2015_805` folha 0005, retângulo reservado rotulado "PHOTO" que vira spinner e por fim foto).
41. Animação é documentada em material estático de três modos, sempre congelando os extremos e o meio lado a lado: justaposição de poses (`vid wwdc2021_110142` folha 0007, o mesmo mostrador com duas e depois três posições do pé; `vid wwdc2021_10308` folha 0007, fileira de cinco miniaturas com o dedo em posição ligeiramente diferente), dupla exposição (`vid wwdc2022_10131` folha 0008, a mesma pessoa em duas poses semitransparentes sobrepostas no mesmo quadro) e borrão seletivo (`vid wwdc2021_10308` folha 0011, a mão borrada enquanto a tela reage). Numa imagem parada, oito traços em cápsula a 45 graus com opacidade decrescente bastam para sugerir rotação (fonte única: `hig loading` img 0732).
42. Todo componente efêmero nasce ancorado na origem, ligado por ponta, linha ou forma contínua, e perde a âncora só quando deixa de ser resposta a um toque e vira estrutura (`hig dock-menus` img 0469; `hig edit-menus` img 0471, linha fina ligando a ponta da barra à alça da seleção; `hig color-wells` img 0253, forma contínua em gota conectando botão fechado e popover; `vid wwdc2020_10206` folha 0007, a mesma lista vira coluna fixa e a seta some junto com a sobreposição).
43. No tvOS o foco eleva o elemento, que cresce, clareia para branco, ganha sombra e sobe de camada, e o layout precisa reservar a folga do estado maior em vez do de repouso (`hig lockups` img 0734 a 0738; `hig focus-and-selection` img 0485 e 0486; `hig layout` img 0687, faixas rosa preenchendo o padding em volta do cartão em foco; `hig game-center` img 0501, o mesmo asset exportado em 659 por 371, 618 por 348 e 548 por 309 pt).

### Comparação de certo e errado

44. O veredito mora numa camada separada do artefato, em selo padronizado, muitas vezes numa imagem própria isolada em vez de sobreposto ao exemplo, para que o exemplo continue servindo de referência de pixel (`hig branding` img 0186 e 0188, selos centralizados em fundo branco sem nenhum elemento de interface junto; `hig airplay` img 0044 e 0045, selos em células próprias; `hig toolbars` img 1166 a 1169, selos ao lado e nunca em cima; `vid wwdc2021_10283` folha 0004, em que o par de selos é padronizado mas fica colado ao canto superior da tela avaliada).
45. Existe um terceiro grau entre aprovado e reprovado, o alerta em laranja ou amarelo, e ele significa risco e não erro (`vid wwdc2023_10078` folha 0006, olhar para baixo e para os lados recebe check verde e olhar para cima e na diagonal recebe alerta laranja; `vid wwdc2026_321`, laranja para a prática problemática e verde para a corrigida em oito folhas entre a 0005 e a 0014; `vid wwdc2021_10250` folha 0014, trio de selos com o amarelo de exclamação ao lado dos dois verdes).
46. O par comparativo reusa literalmente a mesma tela, a mesma foto e o mesmo texto fictício, porque duas diferenças ao mesmo tempo destroem a atribuição (`hig apple-pay` img 0135 a 0143, os mesmos dois botões trocando uma variável por vez: tamanho, ordem, alinhamento, raio de canto; `hig focus-and-selection` img 0485 a 0489, o mesmo botão no mesmo ponto da mesma foto de praia; `vid wwdc2020_10103` folha 0012, dois cartões de nota que diferem só por trazer ou não a palavra antes do horário).
47. O errado é desenhado com o mesmo capricho do certo e recebe o nome do defeito, e em alguns casos aparece sem contraparte correta ao lado (`vid wwdc2018_803` folha 0015 com o rótulo "Too much visual change" e folha 0010 com "Not spatially consistent"; `hig camera-control` img 0209 a 0212, a régua com "1 EV" passa e a mesma régua com apenas "1" é marcada como erro; `vid wwdc2020_10104` folhas 0008 e 0020, X vermelho no canto sem versão aprovada ao lado, inclusive num bloco de código cujo próprio comentário avisa do resultado borrado).
48. A regra de sempre expor a saída do modal se inverte de propósito na antessala de um pedido de permissão (`hig sheets` img 1032 a 1036, em que reunir voltar, fechar e confirmar ao mesmo tempo é o padrão a evitar; `hig privacy` img 0898 e 0899, em que a tela de pré-permissão é reprovada justamente por ganhar saída). Na mesma página, e só nela, também são reprovados incentivo financeiro, gráfico de benefício crescente e reprodução do alerta real com o botão desejado circulado (fonte única: `hig privacy` img 0900 a 0903).

### Anatomia de componente

49. As zonas do componente são nomeadas na própria arte, por linha fina que sai do elemento e termina num rótulo fora do desenho, o que cria vocabulário compartilhado sem recortar a captura (`hig charts` img 0235, chamadas para grid line, plot area, mark, axis, tick e axis value label; `hig complications` img 0344, mostrador com rótulos ligados a Top Left, Date, Middle, Bottom Left, Bottom Middle e Bottom Right; `hig status-bars` img 1104; `vid wwdc2020_10172` folha 0011).
50. A abertura de um componente é ficha técnica cotada, não captura de app: a peça aparece isolada, com setas de régua de largura e altura, antes de qualquer discussão de comportamento (`hig pop-up-buttons` img 0883; `hig steppers` img 1107; `hig text-views` img 1143; `hig toggles` img 1147; `hig web-views` img 1285).
51. A hierarquia de ação é peso de preenchimento, e o destrutivo é marcado pela cor do texto e pela posição, nunca pelo fundo inteiro, que o tornaria o elemento mais pesado da tela (`hig buttons` img 0190, primário azul sólido, destrutivo em fundo cinza claro com texto vermelho; `hig action-sheets` img 0027; `hig machine-learning` img 0748, preenchido, contornado e texto puro na mesma coluna; `vid wwdc2018_806` folha 0013, destrutivo em vermelho separado numa segunda camada de confirmação dentro do mesmo cartão; `vid wwdc2020_10205` folhas 0008 e 0009, destrutivo acima do neutro e nunca ao lado).
52. O teto de altura da área customizável de um snippet é cotado em 400 pt entre o bloco de diálogo no topo e o par de botões na base, e vale notar que esse é o valor das diretrizes, enquanto a sessão de 2025 fala em 340 pt, divergência já registrada na seção 8 (fonte única: `hig snippets` img 1091).

### Processo e ferramentas

53. Exploração se mostra em volume e em redução, com os estágios contáveis na imagem e sem que a fala dê as contagens (`vid meet-with-apple_270` folha 0002, 14 notas soltas no brainstorm, 8 depois de simplificar, três aglomerados e por fim cinco, duas e uma; `vid wwdc2014_223` folhas 0007 a 0009, uma folha coberta de dezenas de wireframes a caneta com pontos azuis marcando quatro deles e uma lupa ampliando o de lista; `vid wwdc2024_10140` folha 0006, de nenhuma nota a cerca de dezesseis, depois reagrupadas em colunas com dois post-its de cabeçalho em azul).
54. A ferramenta real entra em quadro com os painéis abertos e os valores legíveis, quase sempre no mesmo esqueleto de três zonas, navegação à esquerda, palco ao centro, inspetor à direita, e os parâmetros de animação são tratados como controles de produto (`hig app-icons` img 0079, Icon Composer com opacidade 100 por cento, blend mode normal, "Liquid Glass Effects" ligado, imagem em SVG, posição x e y em 0 pt e escala 100 por cento; `vid wwdc2021_10250` folha 0005; `vid wwdc2026_8012` folhas 0002 a 0007; `vid wwdc2014_223` folha 0019, duração de 0,60 s e atraso de 0,50 s com casamento por objeto, palavra ou caractere; `vid wwdc2018_803` folha 0024, rigidez subindo de 40 para 100 e amortecimento de 10 para 40 com a bola mudando junto).
55. O placeholder prova que a estrutura funciona sozinha, mas só o conteúdo verdadeiro e o pior caso revelam truncamento, ausência e ambiguidade de rótulo, e os dois estágios aparecem como etapas distintas do trabalho (`hig live-activities` img 0701 a 0703, formas pretas nomeadas por linhas de chamada no lugar de conteúdo real; `vid wwdc2026_227` folhas 0007 a 0009, a capa em cor sólida dá lugar a capas reais e comentários com tempo relativo, e os casos de borda são nomeados na própria lista de prévias, entre eles conteúdo longo, clube vazio e clube lotado; `vid wwdc2026_290` folha 0003, o valor do cartão é zerado mantendo o rótulo para testar o tom no pior caso; `vid wwdc2026_292` folha 0014, o estado vazio traz o termo entre aspas com um erro de digitação proposital).

### Como a Apple apresenta e demonstra

56. O indicador de progresso de uma sessão inteira é a própria lista de tópicos, resolvida só por peso e opacidade do mesmo texto na mesma posição, sem barra, numeração, ícone ou moldura de seleção, e as notas registram repetidamente que a fala nunca comenta o recurso (`vid wwdc2017_802` folhas 0010, 0012 e 0013; `vid wwdc2019_802`, a mesma fileira de seis palavras em onze folhas entre a 0002 e a 0039; `vid tech-talks_111462` folhas 0003, 0008 e 0015; `vid wwdc2022_10139` folha 0006; `vid wwdc2025_317` folha 0002; `vid wwdc2026_250` folhas 0004, 0006, 0008, 0010, 0012 e 0014).
57. Nada aparece pronto: lista, tabela, grade e diagrama crescem um item por quadro, o que já entrou não se move, e o item seguinte costuma ficar pré-visível em cinza antes de acender (`vid wwdc2017_819` folha 0002; `vid wwdc2020_10206` folha 0024; `vid wwdc2022_10131` folhas 0002 a 0005, de um item a quatro, e folha 0010, chegando a sete; `vid meet-with-apple_255` folhas 0003 e 0004, a fileira de princípios cresce de um para cinco com uma ilustração nova ao lado de cada item).
58. Código e resultado dividem o quadro e o realce translúcido caminha de trecho em trecho enquanto a tela fica parada, com um limite honesto anotado no próprio material: em várias sequências o resultado renderizado não muda enquanto o código cresce, e ali a imagem não prova nada (`vid wwdc2018_803` folha 0032, o retângulo percorre de decelerationRate até a linha do canto mais próximo; `vid tech-talks_111462` folha 0007; `vid wwdc2024_10151` folhas 0002 a 0019, convenção rígida de código à esquerda e aparelho à direita; `vid wwdc2020_10175`, onde o limite é registrado).
59. A cor dos diagramas carrega taxonomia fixa que a fala não declara, e o significado vale do começo ao fim da peça (`vid wwdc2019_223` folha 0009, azul claro para eventos transientes e laranja para contínuo; `vid tech-talks_111463` folha 0009, azul para contêiner de navegação, vermelho para conteúdo e verde para layout; `vid wwdc2019_520` folhas 0001 e 0002, verde para o assunto da palestra, azul para as APIs já existentes e vermelho para o hardware; `vid wwdc2025_273`, vermelho para o frame da view, amarelo para o do contêiner composto e azul tracejado para o que o sistema de layout enxerga).
60. O fecho é componente, não improviso: o fundo chapado dá lugar à fotografia de um objeto físico, quase sempre sobre mesa de madeira, as recomendações entram uma linha por quadro, e a referência cruzada vive num rodapé fino com título à esquerda e ano à direita, entrando por último (`vid wwdc2024_10145` folha 0009; `vid wwdc2026_321` folha 0015; `vid wwdc2025_316` folha 0017; `vid wwdc2023_10026` folha 0008; `vid wwdc2025_247` folhas 0020 e 0027; `vid wwdc2023_10258` folha 0002).
