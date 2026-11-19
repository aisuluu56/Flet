# Практика 14 — Поиск и фильтрация данных
# ЗАДАЧА: Каталог курсов с фильтром по названию
# Откройте соответствующий lessons/14_filter.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

COURSES = [
    {"name": "Python Start", "level": "Начальный"},
    {"name": "SQL Basics", "level": "Начальный"},
    {"name": "API Design", "level": "Продвинутый"},
    {"name": "Async Python", "level": "Продвинутый"},
    {"name": "Web Dev", "level": "Начальный"},
    {"name": "Django", "level": "Продвинутый"},
    {"name": "Data Science", "level": "Продвинутый"},
    {"name": "Алгоритмы", "level": "Начальный"},
]

def main(page: ft.Page):
    search = ft.TextField(label="Поиск")
    only_easy = ft.Checkbox(label="Только начальные")
    cards = ft.Column()

    def render(e=None):
        query = search.value.lower().strip() if search.value else ""
        cards.controls.clear()

        for c in COURSES:
            match_name = query in c["name"].lower()
            
            match_level = True
            if only_easy.value:
                match_level = (c["level"] == "Начальный")
                
            if match_name and match_level:
                cards.controls.append(ft.Text(c["name"]))

        if not cards.controls:
            cards.controls.append(ft.Text("Ничего не найдено", color=ft.Colors.RED))

        page.update()

    search.on_change = render
    only_easy.on_change = render
    render()
    page.add(search, only_easy, cards)
    # TODO: расширьте данные хотя бы до 8 курсов.

if __name__ == "__main__":
    ft.run(main)