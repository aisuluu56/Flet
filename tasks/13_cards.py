# Практика 13 — Card, ListTile и изображения
# ЗАДАЧА: Каталог компьютерных комплектующих
# Откройте соответствующий lessons/13_cards.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

PRODUCTS = [
    {"name": "SSD 512 ГБ", "price": 4200, "stock": 7},
    {"name": "ОЗУ 16 ГБ", "price": 3100, "stock": 0},
    {"name": "Мышь", "price": 890, "stock": 18},
    {"name": "Клавиатура", "price": 2200, "stock": 3},
]


def main(page: ft.Page):
    page.title = "Комплектующие"
    cards = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)
    for product in PRODUCTS:
        if product["stock"] == 0:
            stock_text = ft.Text ("Нет в наличии", color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
        else:
            stock_text = ft.Text(f"Остаток: {product['stock']} шт")
        cards.controls.append(ft.Card(content=ft.Container(
            padding=12, content=ft.Row(controls=[
                ft.Icon(ft.Icons.COMPUTER, size=32, color=ft.Colors.BLUE),
                ft.Column(controls=[ft.Text(product["name"], weight=ft.FontWeight.BOLD, size=16),
                ft.Text(f"Цена: {product['price']} р"),
                stock_text],
                spacing=5)
            ]),
        )))
    page.add(cards)
    # TODO: иконка, цена, остаток и условное выделение.


if __name__ == "__main__":
    ft.run(main)
