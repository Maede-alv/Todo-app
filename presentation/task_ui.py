import flet as ft
from domain.task import TaskStatus
from application.task_service import TaskService
from infrastructure.task_repository import TaskRepository


class TodoApp(ft.Column):
    def __init__(self, repo: TaskRepository, service: TaskService):
        super().__init__()
        self.repo = repo
        self.service = service
        self.new_task_input = ft.TextField(
            hint_text="What needs to be done?", on_submit=self.create_task, expand=True
        )
        self.task_list = ft.Column()
        self.filter_tabs = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.refresh_task_list,
            tabs=[
                ft.Tab(text="All"),
                ft.Tab(text="To-Do"),
                ft.Tab(text="In Progress"),
                ft.Tab(text="Done"),
            ],
        )

    def build(self):
        return ft.Column(
            controls=[
                ft.Row(
                    [
                        ft.Text(
                            value="Todos", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        self.new_task_input,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.create_task
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter_tabs,
                        self.task_list,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                ),
            ]
        )

    def refresh_task_list(self, _=None):
        status_map = {
            "All": None,
            "To-Do": TaskStatus.TODO,
            "In Progress": TaskStatus.IN_PROGRESS,
            "Done": TaskStatus.DONE,
        }
        selected_status = self.filter_tabs.tabs[self.filter_tabs.selected_index].text
        tasks = self.service.list_tasks(status_map[selected_status])

        self.task_list.controls.clear()
        for task in tasks:
            self.task_list.controls.append(self.create_task_row(task))
        self.update()

    def create_task(self, _=None):
        if self.new_task_input.value.strip():
            self.service.add_task(self.new_task_input.value.strip())
            self.new_task_input.value = ""
            self.refresh_task_list()

    def delete_task(self, task_name):
        self.service.delete_task(task_name)
        self.refresh_task_list()

    def change_task_status(self, task_name):
        self.service.change_task_status(task_name)
        self.refresh_task_list()

    def clear_completed_tasks(self, _):
        self.service.clear_completed()
        self.refresh_task_list()

    def create_task_row(self, task):
        return ft.Row(
            controls=[
                ft.Text(task.name),
                ft.Text(task.status.value),
                (
                    ft.ElevatedButton(
                        "Next", on_click=lambda _: self.change_task_status(task.name)
                    )
                    if task.status != TaskStatus.DONE
                    else ft.Text("✅")
                ),
                ft.IconButton(
                    ft.icons.DELETE, on_click=lambda _: self.delete_task(task.name)
                ),
            ]
        )


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    repo = TaskRepository()
    service = TaskService(repo)

    page.add(TodoApp(repo, service))
