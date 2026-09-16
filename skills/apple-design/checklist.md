# Checklist de revisão no padrão Apple

Cópia literal da seção 7 da essência (`kb/00_ESSENCIA_APPLE.md`). Toda tela produzida ou revisada com esta skill passa por estas 38 perguntas antes de ser entregue. Resposta "não" em qualquer uma é bloqueio, não observação.

## Checklist de revisão de uma interface no padrão Apple

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
