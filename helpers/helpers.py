

def find_item_by_name(item_name, item_list):
    return next((i for i in item_list if item_name in i.name), None)

