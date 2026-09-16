# Anti-padrões que a Apple condena com todas as letras

Cópia literal da seção 6 da essência (`kb/00_ESSENCIA_APPLE.md`). Cada item cita o cartão que o sustenta: `hig/NN slug` é um arquivo de `kb/hig/`, `vid/NN id` é um arquivo de `kb/videos/`. Nenhum destes padrões pode entrar numa interface feita com esta skill.

## Anti-padrões que a Apple condena explicitamente

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
