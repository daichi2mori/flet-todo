import flet as ft


class Task(ft.UserControl):
    # 渡された値で初期化
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete

    def build(self):
        # valueをTrueにすると最初からチェックがついた状態になる
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=True)

        self.display_view = ft.Row(
            # SPACE_BETWEENでチェックボックスとボタンが端っこに配置される
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            # 垂直方向に対して中央に配置される
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            # tooltipを設定することでマウスをホバーしたときに説明文が表示される
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        # 編集用テキストフィールド
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    # チェックボックス(display_view)が非表示になり、編集用テキストフィールド(edit_view)が表示される
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    # 変更した内容をチェックボックスラベル(display_task)に格納し更新する
    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    # TodoAppクラスから渡されたtask_deleteを使い削除する
    def delete_clicked(self, e):
        self.task_delete(self)


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=self.add_clicked
        )
        self.tasks = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        self.add_button,
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        # インスタンス時にテキストフィールドの内容とtask_delete関数を渡している
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        # ft.Columnから要素を削除するときはremoveを使う
        self.tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()

    page.add(todo)


ft.app(target=main)
