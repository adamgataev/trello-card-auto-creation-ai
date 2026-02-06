import asyncio
import flet as ft


def NavBar(page):
    def go_settings(_):
        asyncio.create_task(page.push_route("/settings"))

    NavBar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Trello Card Auto Creation AI"),
        center_title=False,
        actions=[
            ft.IconButton(icon=ft.CupertinoIcons.SETTINGS, on_click=go_settings),
        ]
    )
    return NavBar