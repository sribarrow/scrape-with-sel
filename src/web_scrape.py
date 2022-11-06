import time

from parsel import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


def set_options() -> list:
    options = Options()
    options.headless = True  # hide GUI
    # options.page_load_strategy = 'none'
    options.add_argument(
        "--window-size=1920,1080"
    )  # set window size to native GUI size
    options.add_argument("start-maximized")  # ensure window is full-screen
    # configure chrome browser to not load images and javascript
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )

    return [options, chrome_options]


def main(t: int = 10) -> None:
    # import time
    # configure webdriver
    options, chrome_options = set_options()
    driver = webdriver.Chrome(options=options, chrome_options=chrome_options)
    driver.get("https://www.twitch.tv/directory/game/Art")
    time.sleep(t)
    # wait for page to load
    # element = WebDriverWait(driver=driver, timeout=5).until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, "div[data-target=directory-first-item]")
    #     )
    # )
    resp = Selector(text=driver.page_source)

    parsed = []
    for item in resp.xpath("//div[contains(@class,'tw-tower')]/div[@data-target]"):
        parsed.append(
            {
                "title": item.css("h3::text").get(),
                "url": item.css(".tw-link::attr(href)").get(),
                "username": item.css(".tw-link::text").get(),
                "tags": item.css(".tw-tag ::text").getall(),
                "viewers": "".join(item.css(".tw-media-card-stat::text").re(r"(\d+)")),
            }
        )
    print(parsed)
    driver.quit()


if __name__ == "__main__":
    main()
