import allure
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Покупка товаров и оформление заказа")
def test_purchase_flow(driver):
    @allure.step("Авторизация пользователя")
    def login():
        """
        Открываем страницу входа и авторизуемся под стандартным пользователем.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        # Скриншот после входа
        allure.attach(driver.get_screenshot_as_png(), name="Login Screen", attachment_type=allure.attachment_type.PNG)

    @allure.step("Добавление товаров в корзину")
    def add_items():
        """
        Добавляем три товара по их идентификаторам.
        """
        inventory = InventoryPage(driver)
        inventory.add_item_by_id("sauce-labs-backpack")
        inventory.add_item_by_id("sauce-labs-bolt-t-shirt")
        inventory.add_item_by_id("sauce-labs-onesie")
        inventory.go_to_cart()

    @allure.step("Проверка товаров в корзине")
    def check_cart():
        """
        Проверяем, что все добавленные товары отображаются в корзине.
        """
        cart = CartPage(driver)
        assert cart.is_item_in_cart("Sauce Labs Backpack"), "Backpack не найден в корзине"
        assert cart.is_item_in_cart("Sauce Labs Bolt T-Shirt"), "Bolt T-Shirt не найден в корзине"
        assert cart.is_item_in_cart("Sauce Labs Onesie"), "Onesie не найден в корзине"
        # Скриншот корзины
        allure.attach(driver.get_screenshot_as_png(), name="Cart Items", attachment_type=allure.attachment_type.PNG)

    @allure.step("Оформление заказа и заполнение данных")
    def checkout():
        """
        Переходим к оформлению заказа, заполняем форму и проверяем сумму.
        """
        cart = CartPage(driver)
        cart.checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("Имя", "Фамилия", "12345")

        # Скриншот после заполнения формы
        allure.attach(driver.get_screenshot_as_png(), name="Checkout Info Filled",
                      attachment_type=allure.attachment_type.PNG)

        total = checkout_page.get_total_amount()

        # Проверка суммы заказа
        assert total == "$58.29"
