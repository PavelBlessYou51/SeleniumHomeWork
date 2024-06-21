from pages.card_of_product_page import CardProductPage
from pages.cart_page import CartPage
from pages.list_of_notepades_page import NotepadesPage
from pages.main_page import MainPage
from pages.ragistration_page import RegPage
from pages.user_page import UserPage


def test_smoke(start_testing_info, get_driver):
    mp = MainPage(get_driver)
    mp.go_to_auth_page()
    user_page_url = "https://www.citilink.ru/?_action=login&_success_login=1"
    assert mp.get_current_url() == user_page_url
    print('Success! You are on auth_page!')

    up = UserPage(get_driver)
    up.go_to_list_of_notepades()
    list_of_notepades = "https://www.citilink.ru/catalog/igrovye-noutbuki/"
    assert up.get_current_url() == list_of_notepades
    print('Success! You are on list_of_notepades page!')

    lnp = NotepadesPage(get_driver)
    lnp.go_to_card_of_product()
    card_of_product = 'https://www.citilink.ru/product/noutbuk-igrovoi-msi-gf63-thin-12ucx-1037xru-9s7-16r821-1037-15-6-ips-i-1979696/'
    assert lnp.get_current_url() == card_of_product
    print('Success! You are on card of product page!')

    cpp = CardProductPage(get_driver)
    cpp.go_to_cart()
    cart = "https://www.citilink.ru/order/"
    assert cpp.get_current_url() == cart
    print('Success! You are on cart page!')

    cp = CartPage(get_driver)
    cp.go_to_registration()
    assert cpp.code == cp.code
    print('Code product is correct!')
    print('Success! You are on registration page!')

    rp = RegPage(get_driver)
    rp.end_registration()
    assert rp.get_approve() == 'Заказ ожидает оплаты!' or 'Заказ резервируется!'
    rp.get_screen()
    print('Success! Smoke testing is ended!')
