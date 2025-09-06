Feature: Testing API that interacts with Integration Tests

Background:
  Given the API base URL 'http://localhost:3000'
  And the authorization header is set
  And the content type is 'application/json'

Scenario: Verify Gherkin Parsing for Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a GET request to '/parse-gherkin'
  Then the response status should be 200
  And the response should contain '6 scenarios were parsed successfully'

Scenario: Handle Non-Iterable Objects in Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/handle-non-iterable' with payload:
    """
    {
      "object": "non-iterable"
    }
    """
  Then the response status should be 200
  And the response should contain 'non-iterable object handled'

Scenario: Implement Additional Error Handling
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/error-handling' with payload:
    """
    {
      "triggerError": true
    }
    """
  Then the response status should be 200
  And the response should contain 'error logged successfully'

Scenario: Verify Integration Test Execution in DEV Environment
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/execute-in-dev' with payload:
    """
    {
      "environment": "DEV"
    }
    """
  Then the response status should be 200
  And the response should contain 'integration test executed successfully'

Scenario: Performance of Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a GET request to '/performance'
  Then the response status should be 200
  And the response should contain 'performance threshold met'

Scenario: Resource Utilization During Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a GET request to '/resource-utilization'
  Then the response status should be 200
  And the response should contain 'resource utilization within limits'
