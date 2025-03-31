import flet as ft
from logic import load_items, add_item_logic, update_item_db, delete_item_logic

def main(page: ft.Page):
    page.title = 'Shopping List'
    page.theme_mode = ft.ThemeMode.DARK
    page.window_maximized = True

    item_list = ft.Column(spacing=10)
    
    def refresh_items():
        item_list.controls.clear()
        for item_id, item_name, bought, quantity in load_items():
            item_list.controls.append(create_item_row(item_id, item_name, bought, quantity))
        page.update()

    def create_item_row(item_id, item_name, bought, quantity):
        item_field = ft.TextField(value=item_name, expand=True, dense=True, read_only=True)
        quantity_field = ft.TextField(value=str(quantity), expand=False, dense=True, read_only=True)
        item_checkbox = ft.Checkbox(value=bought == 1, on_change=lambda e: toggle_item(item_id, e.control.value))

        def toggle_item(item_id, is_bought):
            bought = 1 if is_bought else 0
            update_item(item_id, bought)
            refresh_items()

        def edit_item(e):
            item_field.read_only = False
            quantity_field.read_only = False
            page.update()

        def save_item(e):
            update_item_db(item_id, item_field.value, int(quantity_field.value))
            item_field.read_only = True
            quantity_field.read_only = True
            refresh_items()

        return ft.Row([
            item_checkbox,
            item_field,
            quantity_field,
            ft.IconButton(ft.Icons.EDIT, icon_color=ft.colors.YELLOW_400, on_click=edit_item),
            ft.IconButton(ft.Icons.SAVE, icon_color=ft.colors.GREEN_400, on_click=save_item),
            ft.IconButton(ft.Icons.DELETE, icon_color=ft.colors.RED_400, on_click=lambda e: delete_item(item_id))
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def add_item_func(e):
        item_name = item_input.value.strip()
        quantity = int(quantity_input.value)
        if item_name:
            add_item_logic(item_name, quantity)
            refresh_items()

    def delete_item(item_id):
        delete_item_logic(item_id)
        refresh_items()

    item_input = ft.TextField(hint_text='Item Name', expand=True, dense=True)
    quantity_input = ft.TextField(hint_text='Quantity', expand=True, dense=True, value="1")
    add_button = ft.ElevatedButton("Add", on_click=add_item_func, icon=ft.Icons.ADD)

    content = ft.Container(
        content=ft.Column([
            ft.Row([item_input, quantity_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            item_list
        ], alignment=ft.MainAxisAlignment.CENTER), 
        padding=20,
        alignment=ft.alignment.center
    )

    page.add(content)
    refresh_items()

if __name__ == '__main__':
    ft.app(target=main)


