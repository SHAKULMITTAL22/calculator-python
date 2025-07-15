Feature: API Testing Scenarios

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify Integration Test Execution
  When I send a POST request to '/run-integration-test'
  Then the response status should be 200
  And the response should contain 'Test completed successfully'

Scenario: Check Gherkin Parsing
  When I send a POST request to '/parse-gherkin'
  Then the response status should be 200
  And the response should contain 'Parsed X Scenarios using gherkin'

Scenario: Handle Non-Iterable Objects
  When I send a POST request to '/handle-non-iterable'
  Then the response status should be 200
  And the response should contain 'Non-iterable object handled successfully'

Scenario: Validate Error Handling
  When I send a POST request to '/introduce-error'
  Then the response status should be 500
  And the response should contain 'Clear and informative error message'

Scenario: Performance Test
  When I send a POST request to '/performance-test'
  Then the response status should be 200
  And the response should contain 'Average execution time: <time>'

Scenario: Stress Test
  When I send a POST request to '/stress-test'
  Then the response status should be 200
  And the response should contain 'Stress test passed'

Scenario: Scalability Test
  When I send a POST request to '/scalability-test'
  Then the response status should be 200
  And the response should contain 'Scalability test passed'

Scenario: Recovery Test
  When I send a POST request to '/recovery-test'
  Then the response status should be 200
  And the response should contain 'Recovery test passed'
