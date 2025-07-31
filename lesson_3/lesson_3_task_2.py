from smartphone import Smartphone

# Создаем список с пятью разными смартфонами
catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S22", "+79261234567"),
    Smartphone("Google", "Pixel 6", "+79361234567"),
    Smartphone("Xiaomi", "Mi 11", "+79461234567"),
    Smartphone("Huawei", "P50 Pro", "+79561234567")
]

# Выводим каталог в указанном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")