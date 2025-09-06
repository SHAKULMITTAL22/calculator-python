Feature: API Testing Scenarios

Background:
  Given the API base URL 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify Gherkin Parsing
  Given the API base URL 'http://localhost:3000'
  When I send a GET request to '/parse-gherkin'
  Then the response status should be 200
  And the response should contain 'parsed scenarios'
  And the response should not contain 'errors'

Scenario: Check Integration Test Execution
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/run-integration-tests'
  Then the response status should be 200
  And the response should contain 'tests executed'
  And the response should not contain 'runtime errors'

Scenario: Validate Error Handling in Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/run-integration-tests' with payload {"introduceError": true}
  Then the response status should be 200
  And the response should contain 'error caught'
  And the response should contain 'test execution continued'

Scenario: Performance Test for Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/run-performance-tests'
  Then the response status should be 200
  And the response should contain 'execution time'
  And the execution time should be within acceptable limits

Scenario: Resource Usage Test for Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/run-resource-tests'
  Then the response status should be 200
  And the response should contain 'resource usage'
  And the resource usage should be within acceptable limits

Scenario: Verify Object Iterability in Integration Tests
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/check-object-iterability'
  Then the response status should be 200
  And the response should contain 'objects iterable'
  And the response should contain 'non-iterable objects handled'

Scenario: Check Logs for Error Details
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/run-integration-tests' with payload {"introduceError": true}
  Then the response status should be 200
  And the response should contain 'error logs'
  And the error logs should contain 'stack trace'
  And the error logs should contain 'context'

Scenario: Validate Integration Test Method Changes
  Given the API base URL 'http://localhost:3000'
  When I send a POST request to '/apply-method-changes'
  Then the response status should be 200
  And the response should contain 'issues resolved'
  And the response should not contain 'remaining issues'
