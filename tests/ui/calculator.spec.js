const { test, expect } = require('@playwright/test');

test('operation radios use wrapped roving keyboard focus', {
  annotation: { type: 'requirement', description: 'operation-radio-keyboard-navigation' },
}, async ({ page }) => {
  await page.goto('/');
  const radios = page.getByRole('radio');
  await expect(radios).toHaveCount(11);
  await expect(radios.first()).toBeChecked();
  await expect(radios.first()).toHaveAttribute('tabindex', '0');
  await expect(radios.nth(1)).toHaveAttribute('tabindex', '-1');

  await radios.first().focus();
  await page.keyboard.press('ArrowLeft');
  await expect(radios.last()).toBeChecked();
  await expect(radios.last()).toBeFocused();
  await expect(radios.last()).toHaveAttribute('tabindex', '0');
  await expect(radios.first()).toHaveAttribute('tabindex', '-1');

  await page.keyboard.press('ArrowRight');
  await expect(radios.first()).toBeChecked();
  await expect(radios.first()).toBeFocused();
  await page.keyboard.press('ArrowDown');
  await expect(radios.nth(1)).toBeFocused();
  await page.keyboard.press('ArrowUp');
  await expect(radios.first()).toBeFocused();
});

test('pointer selection focuses the first required operand', {
  annotation: { type: 'requirement', description: 'pointer-operation-operand-focus' },
}, async ({ page }) => {
  await page.goto('/');
  await page.getByRole('radio', { name: 'Square', exact: true }).click();

  await expect(page.getByRole('radio', { name: 'Square', exact: true })).toBeChecked();
  await expect(page.getByRole('spinbutton', { name: 'number' })).toBeFocused();
});

test('all controls remain contained without document overflow at 320px', {
  annotation: { type: 'requirement', description: 'calculator-layout-320px' },
}, async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 844 });
  await page.goto('/');

  const metrics = await page.locator('html').evaluate(element => ({
    clientWidth: element.clientWidth,
    scrollWidth: element.scrollWidth,
  }));
  expect(metrics.scrollWidth).toBe(metrics.clientWidth);

  const viewport = page.viewportSize();
  for (const control of await page.locator('button, input').all()) {
    const box = await control.boundingBox();
    expect(box).not.toBeNull();
    expect(box.x).toBeGreaterThanOrEqual(0);
    expect(box.x + box.width).toBeLessThanOrEqual(viewport.width);
  }
});
