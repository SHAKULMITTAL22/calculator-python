Feature: Testing API that interacts with React JS application

Background:
  Given the API base URL 'http://localhost:3000'
  And the authorization header is set
  And the content type is 'application/json'

Scenario: Verify Gherkin Parsing
  When I send a GET request to '/parse-gherkin'
  Then the response status should be 200
  And the response should contain '6 scenarios parsed successfully'

Scenario: Check Error Handling for Non-Iterable Object
  When I send a POST request to '/integration-test' with the payload:
    """
    {
      "object": "non-iterable"
    }
    """
  Then the response status should be 400
  And the response should contain 'object is not iterable'

Scenario: Validate Integration Test Method Changes
  When I send a POST request to '/integration-test' with the payload:
    """
    {
      "object": "iterable"
    }
    """
  Then the response status should be 200
  And the response should contain 'integration tests ran successfully'

Scenario: Test Additional Error Handling
  When I send a POST request to '/integration-test' with the payload:
    """
    {
      "object": "error-scenario"
    }
    """
  Then the response status should be 400
  And the response should contain 'detailed error message'

Scenario: Performance of Integration Tests
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "tests": ["test1", "test2", "test3"]
    }
    """
  Then the response status should be 200
  And the response should contain 'execution time within threshold'

Scenario: Scalability of Integration Tests
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "tests": ["test1", "test2", "test3", "test4", "test5"]
    }
    """
  Then the response status should be 200
  And the response should contain 'performance maintained'

Scenario: Reliability of Integration Tests
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "tests": ["test1", "test2", "test3"]
    }
    """
  Then the response status should be 200
  And the response should contain 'consistent results'
