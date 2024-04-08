import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        # ft.Column内に描写するにはcontrols.appendが必要
        # tasks_viewに追加することでview変数内に追加されていく
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        # page.update()でも画面は更新されるが、
        # view.update()にすることで再描写の範囲を小さくしている
        view.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
    add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)

    tasks_view = ft.Column()

    # ft.Column内の要素は縦に並べられる
    view = ft.Column(
        width=600,
        controls=[
            # ft.Rowは横
            ft.Row(
                controls=[new_task, add_button],
            ),
            tasks_view,
        ],
    )

    # ページ全体を中央揃えに設定
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(target=main)
