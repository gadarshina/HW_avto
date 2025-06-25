# lesson_3_task_3.py

from address import Address
from mailing import Mailing

# Создаем адрес получателя
to_addr = Address(
    index='123456',
    city='Москва',
    street='Ленина',
    house='10',
    apartment='15'
)

# Создаем адрес отправителя
from_addr = Address(
    index='654321',
    city='Санкт-Петербург',
    street='Невский проспект',
    house='20',
    apartment='30'
)

# Создаем экземпляр Mailing
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=250,
    track='AB123456789RU'
)

# Распечатываем информацию о отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")