const { test, expect } = require('@playwright/test');

test('arrow selection retains focus and calculation remains announced', {
  annotation: { type: 'requirement', description: 'keyboard-navigation' },
}, async ({ page }) => {
  await page.goto('/');
  const addition = page.getByRole('radio', { name: 'Addition' });
  const subtraction = page.getByRole('radio', { name: 'Subtraction' });

  await addition.focus();
  await addition.press('ArrowRight');

  await expect(subtraction).toBeChecked();
  await expect(subtraction).toBeFocused();
  await expect(addition).toHaveAttribute('tabindex', '-1');
  await expect(subtraction).toHaveAttribute('tabindex', '0');

  await page.getByRole('spinbutton', { name: 'num1' }).fill('8');
  await page.getByRole('spinbutton', { name: 'num2' }).fill('3');
  await page.getByRole('button', { name: 'Calculate' }).click();
  await expect(page.getByRole('status')).toHaveText('Subtraction: 5');
});

test('all controls fit and remain operable at exactly 320px', {
  annotation: { type: 'requirement', description: 'responsive-layout' },
}, async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 844 });
  await page.goto('/');

  const controls = page.getByRole('radio').or(page.getByRole('spinbutton')).or(page.getByRole('button', { name: 'Calculate' }));
  await expect(controls).toHaveCount(14);
  for (const control of await controls.all()) {
    await expect(control).toBeVisible();
    const box = await control.boundingBox();
    expect(box).not.toBeNull();
    expect(box.x).toBeGreaterThanOrEqual(0);
    expect(box.x + box.width).toBeLessThanOrEqual(320);
  }
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(320);

  const operationNames = [
    'Addition', 'Subtraction', 'Multiplication', 'Percentage', 'Modulus',
    'Division', 'Exponentiation', 'Square', 'Cube', 'Integer division',
    'Absolute difference',
  ];
  for (const name of operationNames) {
    const operation = page.getByRole('radio', { name, exact: true });
    await operation.click();
    await expect(operation).toBeChecked();
  }

  await page.getByRole('radio', { name: 'Addition', exact: true }).click();
  await page.getByRole('spinbutton', { name: 'num1' }).fill('2');
  await page.getByRole('spinbutton', { name: 'num2' }).fill('3');
  await page.getByRole('button', { name: 'Calculate' }).click();
  await expect(page.getByRole('status')).toHaveText('Addition: 5');
});

test('desktop layout remains contained and keeps operands side by side', {
  annotation: { type: 'requirement', description: 'responsive-layout' },
}, async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto('/');

  const calculator = page.locator('.calculator');
  const firstOperand = page.getByRole('spinbutton', { name: 'num1' });
  const secondOperand = page.getByRole('spinbutton', { name: 'num2' });
  const [calculatorBox, firstBox, secondBox] = await Promise.all([
    calculator.boundingBox(), firstOperand.boundingBox(), secondOperand.boundingBox(),
  ]);

  expect(calculatorBox).not.toBeNull();
  expect(firstBox).not.toBeNull();
  expect(secondBox).not.toBeNull();
  expect(calculatorBox.x).toBeGreaterThanOrEqual(0);
  expect(calculatorBox.x + calculatorBox.width).toBeLessThanOrEqual(1440);
  expect(firstBox.y).toBe(secondBox.y);
  expect(firstBox.x + firstBox.width).toBeLessThan(secondBox.x);
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(1440);
});

test('reduced motion disables control transitions', {
  annotation: { type: 'requirement', description: 'reduced-motion' },
}, async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto('/');

  const operation = page.getByRole('radio', { name: 'Addition', exact: true });
  await expect(operation).toHaveCSS('transition-duration', '0s');
  await operation.hover();
  await expect(operation).toHaveCSS('transition-duration', '0s');
});
