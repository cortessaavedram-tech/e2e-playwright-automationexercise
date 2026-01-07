from playwright.sync_api import Page, expect
import re


def test_visit_menu_links(page: Page):
    print("Given the user is on the homepage")
    page.goto("https://es.nttdata.com/")

    print("When the user clicks on the 'Industries' menu link")
    #Localize the element by role (cutton, link, heading...) and by text
    page.get_by_role("button", name="Industries", exact=True).click()
    print("And clicks on the 'Industries' link")
    page.get_by_role("link", name="Industries").first.click()
    #Assertion
    print("Then the user should be redirected to the 'Industries' page")
    expect(page).to_have_url("https://es.nttdata.com/industries")
    print("And the user should see the 'Industries' heading")
    expect(page.get_by_role("heading", name="Industries")).to_be_visible()
    


    print("And the user clicks on the 'Services' menu link")
    page.get_by_role("button", name="Services", exact=True).click()
    print("And clicks on the 'Services' link")
    page.get_by_role("link", name="Services").first.click()
    #Assertion
    print("Then the user should be redirected to the 'Services' page")
    expect(page).to_have_url("https://es.nttdata.com/services")




    print("And the user clicks on the 'Products' menu link")
    page.locator("#navbarLevel0Collapse").get_by_role("link", name="Products").first.click()
    print("And the user clicks on the 'Products' menu link")

    print("And the user clicks on the 'Insights' menu link")
    page.get_by_role("button", name="Insights", exact=True).click()

    print("And the user clicks on the 'About us' menu link")
    page.get_by_role("button", name="About us", exact=True).click()

    print("And the user clicks on the 'Careers' menu link")
    page.get_by_role("button", name="Careers", exact=True).click()
    
