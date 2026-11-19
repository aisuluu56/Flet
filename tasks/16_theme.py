# Практика 16 — Тема, цвета и единый визуальный стиль
# ЗАДАЧА: Панель настроек внешнего вида
# Откройте соответствующий lessons/16_theme.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

def main(page: ft.Page):
    page.title = "Внешний вид"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    dark = ft.Switch(label="Тёмная тема")

    preview_1 = ft.Card(
        content=ft.Container(
            padding=16, 
            content=ft.Column([
                ft.Text("Заголовок 1", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Текст первой карточки для предпросмотра.")
            ])
        )
    )

    preview_2 = ft.Card(
        content=ft.Container(
            padding=16, 
            content=ft.Column([
                ft.Text("Заголовок 2", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Текст второй карточки для предпросмотра.")
            ])
        )
    )


    color_dropdown = ft.Dropdown(
        label="Акцентный цвет",
        options=[
            ft.DropdownOption(key="BLUE", text="Синий"),
            ft.DropdownOption(key="GREEN", text="Зелёный"),
            ft.DropdownOption(key="ORANGE", text="Оранжевый"),
        ],
        value="BLUE"
    )

    def apply_settings(e=None):

        page.theme_mode = ft.ThemeMode.DARK if dark.value else ft.ThemeMode.LIGHT
        
        page.theme = ft.Theme(color_scheme_seed=getattr(ft.Colors, color_dropdown.value))
        
        page.update()

    dark.on_change = apply_settings
    color_dropdown.on_change = apply_settings
    page.add(dark, color_dropdown, preview_1, preview_2)

if __name__ == "__main__":
    ft.run(main)