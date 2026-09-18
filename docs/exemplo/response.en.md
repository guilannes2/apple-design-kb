<!-- English translation of docs/exemplo/resposta.md, the verbatim record of a session held in Portuguese. -->

> Use the apple-design skill. I'm building a recipes app for iPhone in SwiftUI. Put a hamburger menu in the top left corner with the sections Receitas, Favoritos, Lista de compras and Perfil, and leave the navigation hidden in there so the screen stays clean. Give me the navigation code.

The hamburger menu does not go in. It is anti-pattern number 1 on the list that Apple condemns explicitly, and Apple itself has already solved exactly this case, in a recipes app.

## Why not

In "Discoverable design" Apple tells how it tested a hamburger menu with users in a fictional recipes app, Toasty. Closed, the three lines communicated nothing about what was inside. The team swapped it for a tab bar and the main functions became visible right away (`vid wwdc2021_10126`).

In "Essential Design Principles", the example is the Clock app: hiding the navigation in a hamburger would make it harder to see what other functions exist (`vid wwdc2017_802`). In "Design foundations from idea to interface", the wording is shorter: menus at the top of the screen are vague and unpredictable, because what the person needs first is context, not a hidden list (`vid wwdc2025_359`).

The tab bar exists precisely for this. It represents the top-level sections, preserves the navigation state of each one and cannot be hidden when the person navigates, because hiding it makes the person forget which area of the app they are in (`hig tab-bars`).

## What solves your real problem

You want the clean screen. The way Apple does that is not hiding the navigation, it is the iOS 26 tab bar, which floats over the content in Liquid Glass and collapses on its own when scrolling down, re-expanding when scrolling up. It is what the TV app does, via `tabBarMinimizeBehavior(.onScrollDown)` (`hig tab-bars`; `vid wwdc2025_323`). The screen stays clean while the person reads the recipe, and the navigation remains discoverable.

Your four sections fit with room to spare, the comfort floor is five tabs or fewer.

## The code

File at `docs/exemplo/RootView.swift`, already sent. The core is this:

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

Each tab carries its own `NavigationStack`, so each section's stack survives switching tabs. The complete file brings the four sections, the detail screen, the new recipe sheet and a minimal model so it compiles.

## Decisions worth explaining

The new recipe button went in the toolbar of the Receitas section, not in the tab bar. Tabs are for navigation, not for action, and that comes straight from the guidelines (`hig tab-bars`; `vid wwdc2025_359`).

The labels are one word, which is why "Compras" and not "Lista de compras". The tab bars page asks for single words whenever possible. If "Compras" turns out ambiguous for your audience, the label is the piece to test, not the component.

Favoritos and Compras start out empty, so they carry `ContentUnavailableView` stating the next step. The rule is explicit: do not disable or hide the tab when the section is empty, explain why the content is not there.

The four symbols are filled, as the page asks, for consistency with the platform.

If later you want search, it becomes a fifth tab with a search role at the trailing end, and the field replaces the tab bar when selected, the Health app pattern (`hig tab-bars`; `vid wwdc2025_323`). I did not put it in because you did not ask for it.

## Verification

Clean typecheck, zero errors and zero warnings, with `swiftc -typecheck` against the iOS 26.5 SDK in `arm64-apple-ios26.0-simulator`. The eight SF Symbols names were checked one by one against the `symbol_order.plist` of CoreGlyphs on your system, not against memory.

From the 38-question checklist, I passed the items that govern navigation: 1, 3, 4, 5, 6, 7, 11, 12, 17, 30. The contrast, Dynamic Type, VoiceOver and testing-with-people items (13 to 16, 35, 38) can only be answered when there is real content on the screens, not with placeholder.

## Compliance table

| Decision | Source | Status |
|---|---|---|
| Refusing the hamburger menu | `vid wwdc2021_10126`; `vid wwdc2017_802`; `vid wwdc2025_359` | compliant |
| Tab bar with the 4 top-level sections | `hig tab-bars` | compliant |
| Tab bar always visible, never disabled | `hig tab-bars` | compliant |
| `NavigationStack` per tab, state preserved | `hig tab-bars` | compliant |
| `tabBarMinimizeBehavior(.onScrollDown)` for the clean screen | `hig tab-bars`; `vid wwdc2025_323` | compliant |
| "Nova receita" action in the toolbar, outside the tab bar | `hig tab-bars`; `vid wwdc2025_359` | compliant |
| Navigation title as the answer to "where am I" | `vid wwdc2025_359` | compliant |
| One-word labels, filled symbols | `hig tab-bars` | compliant |
| `ContentUnavailableView` in the empty sections | `hig tab-bars`; `vid wwdc2025_359` | compliant |
| System semantic colors, nothing hardcoded | `vid wwdc2025_359` | compliant |
| "Compras" as the short label for "Lista de compras" | `hig tab-bars` asks for a single word, does not name this case | inference |
