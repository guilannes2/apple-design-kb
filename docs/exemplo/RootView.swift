import SwiftUI

// MARK: - Raiz da navegação
// Quatro seções de nível superior numa tab bar. Sempre visível, nunca
// desabilitada, cada aba com sua própria pilha de navegação.

struct RootView: View {
    var body: some View {
        TabView {
            Tab("Receitas", systemImage: "book.fill") {
                RecipesTab()
            }

            Tab("Favoritos", systemImage: "heart.fill") {
                FavoritesTab()
            }

            Tab("Compras", systemImage: "cart.fill") {
                ShoppingListTab()
            }

            Tab("Perfil", systemImage: "person.crop.circle.fill") {
                ProfileTab()
            }
        }
        // A barra flutua sobre o conteúdo e se recolhe ao rolar para baixo,
        // reexpandindo ao rolar para cima. É assim que a tela fica limpa
        // sem esconder a navegação.
        .tabBarMinimizeBehavior(.onScrollDown)
    }
}

// MARK: - Receitas

struct RecipesTab: View {
    @State private var path: [Recipe] = []
    @State private var isAddingRecipe = false

    var body: some View {
        NavigationStack(path: $path) {
            List(Recipe.samples) { recipe in
                NavigationLink(recipe.name, value: recipe)
            }
            // O título responde "onde estou". Não é marca, não é menu.
            .navigationTitle("Receitas")
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetail(recipe: recipe)
            }
            .toolbar {
                // Ação primária na toolbar da seção, nunca na tab bar.
                ToolbarItem(placement: .primaryAction) {
                    Button {
                        isAddingRecipe = true
                    } label: {
                        Label("Nova receita", systemImage: "plus")
                    }
                }
            }
            .sheet(isPresented: $isAddingRecipe) {
                NewRecipeSheet()
            }
        }
    }
}

struct RecipeDetail: View {
    let recipe: Recipe

    var body: some View {
        List {
            Section("Ingredientes") {
                ForEach(recipe.ingredients, id: \.self, content: Text.init)
            }
        }
        .navigationTitle(recipe.name)
        .navigationBarTitleDisplayMode(.inline)
    }
}

struct NewRecipeSheet: View {
    @Environment(\.dismiss) private var dismiss
    @State private var name = ""

    var body: some View {
        NavigationStack {
            Form {
                TextField("Nome da receita", text: $name)
            }
            // O modal nomeia a tarefa e tem saída óbvia.
            .navigationTitle("Nova receita")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancelar") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Salvar") { dismiss() }
                        .disabled(name.isEmpty)
                }
            }
        }
    }
}

// MARK: - Favoritos

struct FavoritesTab: View {
    @State private var favorites: [Recipe] = []

    var body: some View {
        NavigationStack {
            Group {
                if favorites.isEmpty {
                    // Aba vazia explica o próximo passo. Não se esconde a aba.
                    ContentUnavailableView(
                        "Nenhum favorito",
                        systemImage: "heart",
                        description: Text("Toque no coração de uma receita para guardá-la aqui.")
                    )
                } else {
                    List(favorites) { recipe in
                        NavigationLink(recipe.name, value: recipe)
                    }
                }
            }
            .navigationTitle("Favoritos")
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetail(recipe: recipe)
            }
        }
    }
}

// MARK: - Lista de compras

struct ShoppingListTab: View {
    @State private var items: [String] = []

    var body: some View {
        NavigationStack {
            Group {
                if items.isEmpty {
                    ContentUnavailableView(
                        "Lista vazia",
                        systemImage: "cart",
                        description: Text("Adicione os ingredientes de uma receita para montar sua lista.")
                    )
                } else {
                    List(items, id: \.self, rowContent: Text.init)
                }
            }
            .navigationTitle("Compras")
        }
    }
}

// MARK: - Perfil

struct ProfileTab: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Preferências alimentares") {
                    Text("Preferências")
                        .navigationTitle("Preferências alimentares")
                }
                NavigationLink("Notificações") {
                    Text("Notificações")
                        .navigationTitle("Notificações")
                }
            }
            .navigationTitle("Perfil")
        }
    }
}

// MARK: - Modelo mínimo para o exemplo compilar

struct Recipe: Identifiable, Hashable {
    let id = UUID()
    let name: String
    let ingredients: [String]

    static let samples = [
        Recipe(name: "Pão de queijo", ingredients: ["Polvilho", "Queijo", "Ovo"]),
        Recipe(name: "Risoto de limão", ingredients: ["Arroz arbóreo", "Limão", "Parmesão"])
    ]
}

#Preview {
    RootView()
}
