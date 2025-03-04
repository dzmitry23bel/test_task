import logging
import os
import pytest
from PIL import Image

from helpers import WebHelpers

logger = logging.getLogger(__name__)
DOWNLOAD_PATH = "downloads"

@pytest.fixture
def test_setup(page, test_url):
    WebHelpers.go_to_webapp(page, test_url)
    WebHelpers.accept_cookies(page)


def test_search_wallpaper(test_setup, page):
    keyword_for_test = 'forrest'
    WebHelpers.move_to_search_section(page)
    WebHelpers.search_using_main_search(page, text_to_search=keyword_for_test)
    wallpapers_titles = [wallpaper.get_attribute('title') for wallpaper in
                         page.locator("a[href*='/wallpapers/']").all()]
    # Check that results correspond to keyword
    titles_count = sum(1 for title in wallpapers_titles if keyword_for_test in title.lower())
    total_links = len(wallpapers_titles)
    assert titles_count >= total_links * 0.6, (f"{titles_count} results of {total_links} has a "
                                               f"searched word in the title")

def test_download_free_wallpaper(test_setup, page):
    keyword_for_test = 'sun'
    WebHelpers.move_to_search_section(page)
    WebHelpers.search_using_main_search(page, text_to_search=keyword_for_test)
    free_wallpaper_el = WebHelpers.get_first_free_card(page)
    free_wallpaper_el.click()
    # Click the button to trigger download
    with page.expect_download() as download_info:
        page.locator("button:has-text('Download Free')").last.click()
    # Get the downloaded file
    download = download_info.value
    file_path = os.path.join(DOWNLOAD_PATH, download.suggested_filename)
    download.save_as(file_path)
    # Open the image to verify it's not corrupted
    try:
        with Image.open(file_path) as img:
            img.verify()  # Raises an error if the image is corrupted
        logger.info("Image verification passed!")
    except Exception as e:
        logger.info(f"Image verification failed:{str(e)}")

def test_download_premium_wallpaper(test_setup, page):
    keyword_for_test = 'sun'
    WebHelpers.move_to_search_section(page)
    WebHelpers.search_using_main_search(page, text_to_search=keyword_for_test)
    premium_wallpaper_el = WebHelpers.get_first_premium_card(page)
    premium_wallpaper_el.click()
    page.get_by_text('Premium').wait_for(timeout=5000, state="visible")
    page.wait_for_timeout(2000)
    page.locator("button[data-event='ATTEMPT_PURCHASE_CONTENT']").last.click()
    page.wait_for_timeout(2000)
    assert page.locator("button:has-text('Buy Credits')").count(), "Window with buying proposal didn't show up"
