import json

from src.category import Category
from src.product import Product


def open_file_json(path: str) -> list[dict]:
    """Открывает файл Json формата"""
    with open(path,'r', encoding='utf=8') as file:
        data = json.load(file)
    return data



def eject_in_file(path:str) -> list:
    """Принимает путь до файла, распределяет всю информацию с файла по классам"""
    categories = []
    data = open_file_json(path)
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


path = r'..\data\products.json'
# if __name__ == '__main__':
