Feature: Integration Test Script Validation

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify Gherkin Parsing
  When I send a GET request to '/parse-gherkin'
  Then the response status should be 200
  And the response body should contain '6 scenarios parsed successfully'

Scenario: Check for Iteration Errors
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "testData": [
        {"id": 1, "name": "Object1"},
        {"id": 2, "name": "Object2"}
      ]
    }
    """
  Then the response status should be 200
  And the response body should not contain 'iteration error'

Scenario: Validate Error Handling for Non-Iterable Objects
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "testData": [
        {"id": 1, "name": "Object1"},
        "Non-iterable string"
      ]
    }
    """
  Then the response status should be 200
  And the response body should contain 'error handling message'

Scenario: Test Object Handling as Arrays
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "testData": [
        {"id": 1, "name": "Object1"},
        [{"id": 2, "name": "ArrayObject"}]
      ]
    }
    """
  Then the response status should be 200
  And the response body should contain 'objects processed as arrays'

Scenario: Performance Testing with Large Datasets
  When I send a POST request to '/run-integration-tests' with a large payload:
    """
    {
      "testData": [
        {"id": 1, "name": "Object1"},
        {"id": 2, "name": "Object2"},
        ...
        {"id": 1000, "name": "Object1000"}
      ]
    }
    """
  Then the response status should be 200
  And the response time should be within an acceptable range

Scenario: Error Logging Clarity and Detail
  When I send a POST request to '/run-integration-tests' with the payload:
    """
    {
      "testData": [
        {"id": 1, "name": "Object1"},
        "Non-iterable string"
      ]
    }
    """
  Then the response status should be 200
  And the response body should contain clear and detailed error logs
