import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        # page.add()が起動したタイミングで画面にチェックボックスが追加される
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        # new_task.value = "" だけだと画面の再描写はされないため、page.update()が必要
        page.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?")
    add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)

    page.add(new_task, add_button)

ft.app(target=main)
