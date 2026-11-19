# Практика 17 — Адаптивная компоновка ResponsiveRow
# ЗАДАЧА: Дашборд учебной платформы
# Откройте соответствующий lessons/17_responsive.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

METRICS = [("Студенты", 128), ("Группы", 8), ("Курсы", 14), ("Тесты", 32)]

def main(page: ft.Page):
    page.title = "Показатели"
    cards = []
    
    icons = {
        "Студенты": ft.Icons.PEOPLE,
        "Группы": ft.Icons.GROUPS,
        "Курсы": ft.Icons.BOOK,
        "Тесты": ft.Icons.QUIZ
    }

    for name, count in METRICS:
        cards.append(ft.Container(
            # TODO: добавьте breakpoint MD и LG
            col={"xs": 12, "md": 6, "lg": 3},
            padding=18,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=10,
            content=ft.Column([
                ft.Row([
                    ft.Icon(icons[name], size=24, color=ft.Colors.BLUE),
                    ft.Text(name, size=16, weight=ft.FontWeight.BOLD)
                ]),
                ft.Text(str(count), size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
            ])
        ))
        
    page.add(ft.ResponsiveRow(controls=cards, spacing=12, run_spacing=12))
    # TODO: оформление и иконки (выполнено выше)

if __name__ == "__main__":
    ft.run(main)