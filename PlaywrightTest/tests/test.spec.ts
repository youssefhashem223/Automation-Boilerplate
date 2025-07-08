import { test, expect } from '@playwright/test';
import { login } from './utils';

test('Administrar Fale conosco', async ({ page }) => {
    await login(page);

    await page.getByRole('listitem').filter({ hasText: 'Chat' }).click();
    await page.waitForURL('**/chat');

    await page.getByRole('heading', { name: 'Flamingo' }).click();

    const chat = page.getByRole('textbox', { name: 'Mensagem...' });
    await expect(chat).toBeVisible();
    chat.fill('Playwright')
    chat.press('Enter');
});