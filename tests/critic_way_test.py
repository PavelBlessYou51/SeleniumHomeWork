from pages.list_of_notepades_page import NotepadesPage
from pages.main_page import MainPage
from pages.user_page import UserPage


def test_critic_way(start_testing_info, get_driver):
    mp = MainPage(get_driver)
    mp.go_to_auth_page()

    up = UserPage(get_driver)
    up.go_to_list_of_notepades()

    np = NotepadesPage(get_driver)
    res = np.checking_filters()
    print(f'Count products: {res}')
    np.get_screen()
    print('Critical way testing was ended!')
