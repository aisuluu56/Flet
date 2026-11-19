# Практика 15 — Сортировка, выбор и работа с коллекциями
# ЗАДАЧА: Рейтинг видеоигр
# Откройте соответствующий lessons/15_sort.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

GAMES = [
    {"id": 101, "name": "Portal", "rating": 9.6},
    {"id": 102, "name": "Celeste", "rating": 9.1},
    {"id": 103, "name": "Hades", "rating": 9.4},
    {"id": 104, "name": "Hollow Knight", "rating": 9.5},
    {"id": 105, "name": "The Witcher 3", "rating": 9.8},
    {"id": 106, "name": "Minecraft", "rating": 8.9},
]

def main(page: ft.Page):
    order = ft.Dropdown(label="Сортировать", options=[
        ft.DropdownOption(key="name", text="По названию"),
        ft.DropdownOption(key="rating", text="По оценке"),
    ], value="name")
    
    reverse = ft.Switch(label="Обратный порядок")
    result = ft.Text("Ничего не выбрано")
    cards = ft.Column()

    def render(e=None):
        sorted_games = sorted(GAMES, key=lambda g: g[order.value], reverse=reverse.value)
        
        cards.controls.clear()
        for game in sorted_games:
            cards.controls.append(
                ft.Row([
                    ft.Text(f"{game['name']} (Рейтинг: {game['rating']})"),
                    # Здесь исправлено на ft.Button
                    ft.Button("Выбрать", on_click=lambda e, id=game['id']: select_game(id))
                ])
            )
        page.update()

    def select_game(game_id):
        result.value = f"Выбрана игра с ID: {game_id}"
        page.update()

    order.on_select = render
    reverse.on_change = render
    render()
    page.add(order, reverse, cards, result)

if __name__ == "__main__":
    ft.run(main)