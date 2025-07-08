export async function login(page) {
    await page.goto('https://');
    await page.getByPlaceholder('Insira o e-mail').fill('');
    await page.getByPlaceholder('Insira a senha').fill('');
    await page.getByRole('button', { name: 'Entrar' }).click();
    await page.waitForURL('**/dashboard');
}  