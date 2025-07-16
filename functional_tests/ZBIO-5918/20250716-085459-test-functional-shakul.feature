Feature: Testing API that interacts with Aetherix UI

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify that integration tests run successfully without errors
  Given the integration test directory is accessible
  When I run the integration test script
  Then the console output should not contain 'TypeError: object is not iterable'
  And the integration tests should complete execution

Scenario: Verify that integration tests handle errors gracefully
  Given the integration test directory is accessible
  When I run the integration test script
  And I introduce a known error in the test data
  Then the console output should contain error logs
  And the integration tests should not fail

Scenario: Verify that integration tests handle object iteration correctly
  Given the integration test directory is accessible
  When I run the integration test script
  And the test data includes objects that should be iterable
  Then the console output should not contain iteration-related errors
  And the integration tests should not fail

Scenario: Verify the performance of integration tests
  Given the integration test directory is accessible
  When I run the integration test script
  Then the execution time should be within the specified performance threshold

Scenario: Verify the resource usage of integration tests
  Given the integration test directory is accessible
  When I run the integration test script
  Then the system resource usage (CPU, memory) should not exceed the acceptable limits

Scenario: Verify that the 'Generate Test' button has improved design and contrast
  Given the UI page with the 'Generate Test' button is accessible
  When I inspect the button's color, padding, and hover/active states
  Then the button should have sufficient contrast against the background
  And the button should respond to user interactions

Scenario: Verify that slider labels are readable and clearly labeled
  Given the UI page with sliders is accessible
  When I inspect the font size, contrast, and labeling of slider labels
  Then the slider labels should have sufficient contrast
  And the slider labels should clearly indicate the max values

Scenario: Verify that the layout has improved spacing and visual separation
  Given the UI page is accessible
  When I inspect the vertical spacing between title, sliders, and button
  Then the layout should have increased spacing
  And the layout should have visual separation between different sections
