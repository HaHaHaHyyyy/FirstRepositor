import flet as  ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = 'Light' #Or Dark
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row(
            [
                ft.Text('Заргистрируйтесь'),
                ft.TextField(value = "0",width = 150, text_align=ft.TextAlign.CENTER),
                ft.IconButton(ft.Icons.CANCEL),
                ft.Icon(ft.Icons.BACK_HAND)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
