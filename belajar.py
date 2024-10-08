from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://saucedemo.com/")
    #print(page.title())

    #login
    page.locator('//input[@placeholder="Username"]').fill('standard_user')
    page.locator('[data-test="password"]').fill('secret_sauce')
    page.locator('[id="login-button"]').click()

    #masukin ke chart sampe checkout
    page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('//a[@class="shopping_cart_link"]').click()
    page.locator('[id="checkout"]').click()

    #masukin nama waktu checkout
    page.locator('//input[@placeholder="First Name"]').fill('Wisnu')
    page.locator('//input[@placeholder="Last Name"]').fill('Keren')
    page.locator('//input[@placeholder="Zip/Postal Code"]').fill('123456')

    #klik kontinu
    page.locator('[id="continue"]').click()

    #klik finish dan selesai
    page.locator('[id="finish"]').click()
    page.pause()

    #balik ke halaman produk
    #page.locator('[id="back-to-products"]').click()

    #tutup
    page.close()