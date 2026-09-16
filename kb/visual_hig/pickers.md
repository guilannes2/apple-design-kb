# HIG, página pickers: o que as ilustrações e vídeos mostram

Status visual:
- hig-img_pickers: assistido: 3 de 3 folhas abertas, todos os códigos conferidos

### hig-img_pickers · folha 0001 · código 6E04A
- img 0841 (clara), seção Pickers: representação estilizada de um relógio Apple Watch visto de frente em fundo em degradê laranja/vermelho, com três faixas horizontais empilhadas simulando uma lista rolável: a faixa central, maior e com contorno branco destacado, contém o texto "Item" e representa o item selecionado; uma seta para a esquerda aparece à direita da faixa central. As faixas acima e abaixo estão parcialmente cobertas/reduzidas, sugerindo itens fora de foco na lista. Confere com a descrição oficial de "item selecionado em uma lista rolável".
- img 0842 (clara), seção iOS, iPadOS, legenda "In a compact layout, a picker opens as a popover over your content": linha compacta com rótulo "Date" à esquerda e valor "April 1, 2025" em azul à direita, dentro de um cartão cinza-claro; abaixo, um popover se abre mostrando um calendário mensal completo de "April 2025" com setas de navegação de mês, cabeçalho de dias da semana (SUN a SAT) e a grade de números do mês, com o dia 1 destacado em círculo azul e o dia 21 em azul (data atual do sistema, sublinhado). O popover se estende para baixo a partir da linha, coberto sobre o conteúdo abaixo.
- img 0843 (clara), seção iOS, iPadOS, legenda "In an inline layout, a picker opens inline with your content": cartão com título "Date" e um toggle verde ativado à direita na mesma linha; abaixo, incorporado no próprio cartão (sem popover), o mesmo calendário de abril de 2025 com dia 1 destacado.
- img 0844 (clara), seção iOS, iPadOS, legenda "Another example of an inline picker uses wheels to choose values for date and time": cartão com título "Time" e valor "8:00 PM" em azul na mesma linha; abaixo, três rodas verticais de rolagem (hora, minutos, AM/PM) com o valor central destacado em texto maior e preto ("8", "00", "PM") e os valores adjacentes acima/abaixo em cinza claro, sugerindo profundidade de rolagem tipo carretel.

### hig-img_pickers · folha 0002 · código 2C364
- img 0845 (clara), seção watchOS: tela do Apple Watch em fundo preto, hora "10:09" e "Title" em azul no topo, botão de voltar circular à esquerda; abaixo, rótulo verde "Label" e uma roda vertical de três posições com contorno verde destacando o valor central "Current" (os valores "After" acima e "Next" abaixo aparecem cortados/esmaecidos); botão verde "Done" na base.
- img 0846 (clara), seção watchOS: mesma estrutura de tela preta do Apple Watch, rótulo verde "Day" sobre três rodas lado a lado (dia, mês abreviado como número e ano), cada uma com contorno, sendo a roda central "09" destacada em verde; botão verde "Next" na base, indicando fluxo sequencial de seleção de data em várias etapas.
- img 0847 (clara), seção watchOS: mesma tela preta, rótulo verde "Minutes" sobre três rodas no formato de hora "05 : 09 : 09" separadas por dois pontos, com a roda central em destaque verde; botão verde "Done" na base.
- img 0848 (clara), seção watchOS: tela preta simples com um botão retangular cinza-escuro centralizado mostrando duas linhas de texto, "Item" em branco maior e "Second" em cinza menor abaixo, representando o botão de picker fechado que mostra a opção atualmente selecionada.

### hig-img_pickers · folha 0003 · código E0C98
- img 0849 (clara), seção watchOS: tela preta do Apple Watch com "Title" em azul no topo e botão de voltar; abaixo, uma lista vertical de três linhas visíveis, "First", "Second" (com checkmark verde à direita, indicando seleção) e "Third", separadas por linhas divisórias finas, mostrando o resultado de tocar no botão da imagem anterior (0848): o app abre a lista completa de opções para escolha.

## Síntese visual da página pickers
- No iOS, o mesmo componente de data muda de comportamento conforme o layout: compacto abre um calendário em popover flutuante sobre o conteúdo (img 0842), inline incorpora o calendário no próprio fluxo da página (img 0843), e uma terceira variação troca o calendário por rodas de rolagem estilo carretel para hora (img 0844).
- No watchOS, o picker de lista curta usa rodas com o item central sempre marcado por um contorno verde de foco e rótulo verde acima indicando o campo (img 0845, 0846, 0847), enquanto listas longas trocam a roda por um botão que abre uma tela de lista completa com checkmark verde no item selecionado (img 0848 leva a img 0849).
- Em todas as ilustrações de watchOS, a cor verde é reservada consistentemente para indicar foco/seleção (contorno da roda, rótulo do campo, botão de ação, checkmark), formando um código de cor único para "estado ativo" nesse contexto.
