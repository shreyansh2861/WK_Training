const { test } = require('@playwright/test');

test.beforeEach(async ({ page }) => {
  // Runs before each test and signs in each page.
  await page.goto('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Dwm&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Ftab%3Dwm&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin');
  await page.click('text=Login');
  await page.fill('input[name="www.shreyanshpatil2001@gmail.com"]', 'username');
  await page.fill('input[name="Patil@1234"]', 'password');
  await page.click('text=Submit');
});

test('first', async ({ page }) => {
  // page is signed in.
});

test('second', async ({ page }) => {
  // page is signed in.
});