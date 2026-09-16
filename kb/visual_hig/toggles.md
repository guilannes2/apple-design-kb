# HIG, página toggles: o que as ilustrações e vídeos mostram

Status visual:
- hig-img_toggles: assistido: 4 de 4 folhas abertas, todos os códigos conferidos

### hig-img_toggles · folha 0001 · código BB958
- img 1147 (clara), seção Toggles: ilustração conceitual em gradiente laranja/vermelho com dois switches rotulados "Label" (rótulo pontilhado), o de cima ligado em vermelho escuro com bolinha branca à direita e setas de régua medindo largura e altura, o de baixo desligado em branco com contorno vermelho fino e um pequeno círculo vazio à direita. Mostra o par ligado/desligado como abertura de seção, com anotação de medidas.
- img 1148 clara, seção iOS, iPadOS: cartão com duas linhas de lista, ambas com rótulo "Title" à esquerda; a primeira tem switch desligado (cinza claro, bolinha à esquerda), a segunda tem switch ligado em verde padrão (bolinha branca à direita), separadas por linha divisória fina. Mostra a cor verde padrão do switch ativo em contraste com o cinza do inativo.
- img 1149 clara, seção iOS, iPadOS: mesmo layout de cartão com duas linhas "Title", mas agora o switch ligado usa um roxo/violeta customizado em vez do verde padrão. Mostra a mesma estrutura da 1148 com cor de destaque personalizada, para comparação lado a lado (verde padrão versus cor customizada).
- img 1150 clara, seção iOS, iPadOS: screenshot real do app Phone (metade superior), barra de status "9:41", botão "Edit" à esquerda, controle segmentado "All / Missed" no centro com "Missed" selecionado, e à direita um botão circular azul com ícone de linhas (o toggle de filtro） destacado em azul sólido. Abaixo, título grande "Recents" e lista de chamadas perdidas em vermelho (Juan Chavez, Mei Chen, Tom Clark, Bill James). O botão de filtro azul preenchido confirma o texto sobre destaque azul quando o toggle está ativo.

### hig-img_toggles · folha 0002 · código E12F6
- img 1151 clara, seção iOS, iPadOS: mesma tela do Phone app, mas agora o controle segmentado mostra "All" selecionado e a lista de "Recents" mostra todas as chamadas (nomes em preto e vermelho misturados, ex. Juan Chavez em preto às 1:00 PM e em vermelho às 11:22 AM), e o botão de filtro à direita aparece sem preenchimento azul, apenas com contorno cinza claro, indicando toggle inativo. Confirma a diferença visual descrita: com destaque quando ativo (folha anterior) e sem nada atrás do símbolo quando inativo.
- img 1152 clara, seção Checkboxes: lista vertical de sete itens "Checkbox Label" dentro de um cartão cinza claro; o primeiro item tem um checkbox azul com traço horizontal branco (estado misto), seguido de checkboxes com estados variados (vazio, marcado com check azul, marcado, vazio, marcado, vazio), sem indentação hierárquica visível apesar do texto falar em hierarquia com indentação. Mostra a variedade de estados lado a lado numa lista plana.
- img 1153 clara, seção Checkboxes: um único checkbox isolado, quadrado com cantos arredondados, preenchido em azul com marca de check branca, legenda "On", exemplo isolado de estado ligado.
- img 1154 clara, seção Checkboxes: um único checkbox isolado, quadrado com cantos arredondados, sem preenchimento (apenas contorno cinza claro muito sutil), legenda "Off", exemplo isolado de estado desligado.

### hig-img_toggles · folha 0003 · código 91C8D
- img 1155 clara, seção Checkboxes: um único checkbox isolado, preenchido em azul com um traço horizontal branco no lugar do check, legenda "Mixed", exemplo isolado do terceiro estado possível do checkbox.
- img 1156 clara, seção Radio buttons: cartão cinza claro com cinco linhas "Radio Button Label", cada uma com um círculo à esquerda; apenas o terceiro item tem o círculo preenchido em azul com ponto branco central, os demais são círculos vazios cinza claro. Mostra grupo de opções mutuamente exclusivas com apenas uma selecionada.
- img 1157 clara, seção Radio buttons: um radio button isolado, círculo azul preenchido com ponto branco central, legenda "Selected".
- img 1158 clara, seção Radio buttons: um radio button isolado, círculo vazio com contorno cinza muito sutil, legenda "Deselected".

### hig-img_toggles · folha 0004 · código E2C6E
- img 1159 clara, seção Radio buttons: três itens dispostos horizontalmente lado a lado sobre uma faixa cinza clara, cada um com um radio button seguido de rótulo: "A long text label" (não selecionado), "Short label" (selecionado, círculo azul preenchido), "A long text label" (não selecionado); os três blocos ocupam a mesma largura apesar dos textos terem tamanhos diferentes, mostrando o espaçamento horizontal uniforme mencionado no texto.

## Síntese visual da página toggles
- O padrão de exibir um mesmo controle em três estados isolados sobre fundo neutro (On, Off e, quando existe, Mixed) se repete tanto para checkbox (img 1153, 1154, 1155) quanto para radio button (img 1157, 1158), sempre como imagem única de item pequeno centralizado, sem cartão ao redor.
- Comparações lado a lado dentro de um mesmo cartão cinza claro (duas linhas "Title" com switch) aparecem duas vezes com a mesma estrutura visual mudando só a cor de destaque, uma vez para mostrar verde padrão versus customizado (img 1148 e 1149) e não para comparação direta na mesma imagem, já que cada cor ocupa sua própria folha.
- Exemplos com app real (Phone, img 1150 e 1151) usam cor azul sólida cheia atrás do símbolo do botão de filtro para indicar estado ativo do toggle, e nenhuma cor de fundo quando inativo, mostrando que o padrão de "toggle como botão" difere do switch tradicional ao não ter trilho, mas ainda comunica estado por preenchimento de cor.
- O espaçamento consistente em radio buttons horizontais (img 1159) é mostrado com três blocos de largura igual mesmo com textos de tamanhos diferentes, evidenciando que a largura de cada opção é fixada pelo maior rótulo do grupo, não pelo conteúdo individual.
