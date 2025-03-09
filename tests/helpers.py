import logging
from playwright.sync_api import Page, Locator

logger = logging.getLogger(__name__)

class WebHelpers:

    @staticmethod
    def go_to_webapp(page: Page, test_url):
        page.goto(test_url)

    @staticmethod
    def agree_on_personal_data(page: Page):
        try:
            consent_button = page.get_by_role("button", name="Consent").first
            consent_button.wait_for(state="visible")
            consent_button.click()
            logger.info('Personal data has been accepted')
        except:
            logger.info('No window with personal data has been found')

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

    @staticmethod
    def get_first_premium_card(page: Page) -> Locator:
        all_wallpapers = page.locator("a[href*='/wallpapers/']").all()
        first_premium_wallpaper = next(el for el in all_wallpapers if el.locator("span[data-icon='true']").count())
        return first_premium_wallpaper
