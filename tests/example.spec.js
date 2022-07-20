const {playwright} = require('playwright');

async function main(){
    const browser = await playwright.chromium.launch({headless: false});
    const context = await browser.newContext();
    const page = await context.newPage();

    await page.goto('http://github.com/login');
    await page.click('text=Sign up');
    await page.fill('input[name="login"]','shreypat76@gmail.com');
    await page.fill('input[name="password"]','Patil@1234');
    await page.click('text=Sign in');
}
main();