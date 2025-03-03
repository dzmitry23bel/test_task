import logging
from playwright.sync_api import Page, Locator

logger = logging.getLogger(__name__)

class WebHelpers:

    @staticmethod
    def go_to_webapp(page: Page, test_url):
        page.goto(test_url)

    @staticmethod
    def accept_cookies(page: Page):
        try:
            cookie_window = page.get_by_text("We value your privacy")
            cookie_window.wait_for(state="visible")
            if cookie_window.is_visible():
                accept_cookie_button = page.locator("button:has-text('AGREE')")
                accept_cookie_button.click()
                logger.info('Cookies have been accepted')
        except:
            logger.info('No window with cookies has been found')

    @staticmethod
    def search_using_main_search(page: Page, text_to_search: str):
        search_box = page.locator("input[name='search']").first
        search_box.fill(text_to_search)
        page.wait_for_timeout(2000)
        page.locator("button[type='submit'][title='Search']").first.click()
        page.wait_for_timeout(2000)
        page.wait_for_load_state()

    @staticmethod
    def move_to_search_section(page: Page):
        page.locator("a[href='/ringtones-and-wallpapers']").first.click()
        page.locator("text='Personalise Your Device with'").wait_for(state="visible")
        page.wait_for_timeout(1000)

    @staticmethod
    def get_first_free_card(page: Page) -> Locator:
        all_wallpapers = page.locator("a[href*='/wallpapers/']").all()
        first_free_wallpaper = next(el for el in all_wallpapers if not
                                    el.locator("span[data-icon='true']").count())
        return first_free_wallpaper

