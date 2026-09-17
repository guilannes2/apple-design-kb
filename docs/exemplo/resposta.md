> Use a skill apple-design. Estou fazendo um app de receitas para iPhone em SwiftUI. Coloque um menu hambúrguer no canto superior esquerdo com as seções Receitas, Favoritos, Lista de compras e Perfil, e deixe a navegação escondida ali para a tela ficar limpa. Me entregue o código da navegação.

O menu hambúrguer não entra. É o anti-padrão número 1 da lista que a Apple condena com todas as letras, e a própria Apple já resolveu exatamente este caso, num app de receitas.

## Por que não

Em "Discoverable design" a Apple conta que testou um menu hambúrguer com usuários num app fictício de receitas, o Toasty. Fechado, as três linhas não comunicavam nada sobre o que havia dentro. A equipe trocou por uma tab bar e as funções principais passaram a ficar visíveis de imediato (`vid wwdc2021_10126`).

Em "Essential Design Principles", o exemplo é o app Clock: esconder a navegação num hambúrguer dificultaria ver que outras funções existem (`vid wwdc2017_802`). Em "Design foundations from idea to interface", a formulação é mais curta: menus no topo da tela são vagos e imprevisíveis, porque o que a pessoa precisa primeiro é contexto, não uma lista escondida (`vid wwdc2025_359`).

A tab bar existe justamente para isto. Ela representa as seções de nível superior, preserva o estado de navegação de cada uma e não pode ser escondida quando a pessoa navega, porque escondê-la faz a pessoa esquecer em que área do app está (`hig tab-bars`).

## O que resolve o seu problema real

Você quer a tela limpa. A forma que a Apple usa para isso não é esconder a navegação, é a tab bar do iOS 26, que flutua sobre o conteúdo em Liquid Glass e se recolhe sozinha ao rolar para baixo, reexpandindo ao rolar para cima. É o que o app TV faz, via `tabBarMinimizeBehavior(.onScrollDown)` (`hig tab-bars`; `vid wwdc2025_323`). A tela fica limpa enquanto a pessoa lê a receita, e a navegação continua descobrível.

Suas quatro seções cabem com folga, o piso de conforto é cinco abas ou menos.

## O código

Arquivo em `docs/exemplo/RootView.swift`, já enviado. O núcleo é este:

```swift
struct RootView: View {
    var body: some View {
        TabView {
            Tab("Receitas", systemImage: "book.fill") { RecipesTab() }
            Tab("Favoritos", systemImage: "heart.fill") { FavoritesTab() }
            Tab("Compras", systemImage: "cart.fill") { ShoppingListTab() }
            Tab("Perfil", systemImage: "person.crop.circle.fill") { ProfileTab() }
        }
        .tabBarMinimizeBehavior(.onScrollDown)
    }
}
```

Cada aba carrega seu próprio `NavigationStack`, então a pilha de cada seção sobrevive à troca de abas. O arquivo completo traz as quatro seções, a tela de detalhe, a sheet de nova receita e um modelo mínimo para compilar.

## Decisões que valem explicar

O botão de nova receita ficou na toolbar da seção Receitas, não na tab bar. Abas são para navegação, não para ação, e isso vem direto das diretrizes (`hig tab-bars`; `vid wwdc2025_359`).

Os rótulos são de uma palavra, por isso "Compras" e não "Lista de compras". A página de tab bars pede palavras únicas sempre que possível. Se "Compras" ficar ambíguo no seu público, o rótulo é a peça a testar, não o componente.

Favoritos e Compras nascem vazios, então levam `ContentUnavailableView` dizendo o próximo passo. A regra é explícita: não desabilite nem esconda a aba quando a seção está vazia, explique por que o conteúdo não está lá.

Os quatro símbolos são preenchidos, como a página pede para consistência com a plataforma.

Se depois você quiser busca, ela vira uma quinta aba com role de busca na ponta trailing, e o campo substitui a tab bar quando selecionada, padrão do app Health (`hig tab-bars`; `vid wwdc2025_323`). Não coloquei porque você não pediu.

## Verificação

Typecheck limpo, zero erros e zero avisos, com `swiftc -typecheck` contra o SDK do iOS 26.5 em `arm64-apple-ios26.0-simulator`. Os oito nomes de SF Symbols foram conferidos um por um contra o `symbol_order.plist` do CoreGlyphs do seu sistema, não contra memória.

Do checklist de 38 perguntas, passei os itens que governam navegação: 1, 3, 4, 5, 6, 7, 11, 12, 17, 30. Os itens de contraste, Dynamic Type, VoiceOver e teste com pessoas (13 a 16, 35, 38) só podem ser respondidos quando houver conteúdo real nas telas, não com placeholder.

## Tabela de conformidade

| Decisão | Fonte | Situação |
|---|---|---|
| Recusar o menu hambúrguer | `vid wwdc2021_10126`; `vid wwdc2017_802`; `vid wwdc2025_359` | conforme |
| Tab bar com as 4 seções de nível superior | `hig tab-bars` | conforme |
| Tab bar sempre visível, nunca desabilitada | `hig tab-bars` | conforme |
| `NavigationStack` por aba, estado preservado | `hig tab-bars` | conforme |
| `tabBarMinimizeBehavior(.onScrollDown)` para a tela limpa | `hig tab-bars`; `vid wwdc2025_323` | conforme |
| Ação "Nova receita" na toolbar, fora da tab bar | `hig tab-bars`; `vid wwdc2025_359` | conforme |
| Título de navegação como resposta a "onde estou" | `vid wwdc2025_359` | conforme |
| Rótulos de uma palavra, símbolos preenchidos | `hig tab-bars` | conforme |
| `ContentUnavailableView` nas seções vazias | `hig tab-bars`; `vid wwdc2025_359` | conforme |
| Cores semânticas do sistema, nada fixo no código | `vid wwdc2025_359` | conforme |
| "Compras" como rótulo curto de "Lista de compras" | `hig tab-bars` pede palavra única, não nomeia este caso | inferência |
