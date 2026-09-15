const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests/ui',
  use: {
    // The protected runner requires an explicitly approved hosted target.
    baseURL: process.env.UI_TEST_BASE_URL || 'http://6a4f6400-0e68-43c7-b2be-6f7dc17536e4.preview.localhost:3088',
    trace: 'retain-on-failure',
    video: 'retain-on-failure',
  },
});
