from database import get_items, add_item, update_item, delete_item

def load_items():
    return get_items()

def add_item_logic(name, quantity):
    add_item(name, quantity)

def update_item_db(item_id, name, quantity):
    update_item(item_id, name, quantity)

def delete_item_logic(item_id):
    delete_item(item_id)
