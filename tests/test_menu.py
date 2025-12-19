from playwright.sync_api import Page, expect

def test_visit_menu_links(page: Page):
    print("Given the user is on the homepage")
    page.goto("https://es.nttdata.com/")

    print("When the user clicks on the 'Industries' menu link")
    #Localize the element by role (cutton, link, heading...) and by text
    page.get_by_role("button", name="Industries", exact=True).click()

    print("And the user clicks on the 'Services' menu link")
    page.get_by_role("button", name="Services", exact=True).click()

    print("And the user clicks on the 'Products' menu link")
    page.locator("#navbarLevel0Collapse").get_by_role("link", name="Products").first.click()
    print("And the user clicks on the 'Products' menu link")

    print("And the user clicks on the 'Insights' menu link")
    page.get_by_role("button", name="Insights", exact=True).click()

    print("And the user clicks on the 'About us' menu link")
    page.get_by_role("button", name="About us", exact=True).click()

    print("And the user clicks on the 'Careers' menu link")
    page.get_by_role("button", name="Careers", exact=True).click()
    
