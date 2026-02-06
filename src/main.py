import flet as ft

from router import Router
from components.nav_bar import NavBar

async def main(page: ft.Page):
    page.theme_mode = "dark"

    page.appbar = NavBar(page)
    my_router = Router(page)

    page.on_route_change = my_router.route_change

    page.add(
        my_router.body
    )
    await page.push_route('/')

ft.run(main, assets_dir="assets")