import pytest
from pages.home_page import HomePage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
class TestOrderProcessing:
    
    def test_order_product_as_a_guest(self):
        home_page = HomePage(self.driver).open()
        home_page.footer.click_dissmiss_button()
        home_page.menu.open_store_page()
        store_page = StorePage(self.driver).wait_for_page_to_load()
        store_page.add_item_to_cart("Belt")
        assert home_page.menu.amount == "65,00"
        
        home_page.menu.menu_pop_up().go_to_the_cart()
        cart_page = CartPage(self.driver).wait_for_page_to_load()
        cart_page.assert_item_data("Belt", "65,00")
        cart_page.go_to_checkout()
        checkout_page = CheckoutPage(self.driver).wait_for_page_to_load()
        checkout_page.fill_first_name('John').fill_last_name('Doe').fill_address('Test 11').fill_postal_code('11-111')
        checkout_page.fill_city('Test').fill_phone_number('123456789').fill_email_adress('test@test.test')
        checkout_page.click_place_order_button().verify_success_message()