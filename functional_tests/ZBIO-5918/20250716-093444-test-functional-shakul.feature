Feature: API Testing for Integration Test Execution

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Successful Integration Test Execution
  Given the integration test scripts are correctly set up and all dependencies are installed
  When I send a POST request to '/run-integration-test' with the payload:
  """
  {
    "testId": "TC-001"
  }
  """
  Then the response status should be 200
  And the response body should contain:
  """
  {
    "status": "success",
    "message": "Test executed successfully"
  }
  """

Scenario: Error Handling in Integration Test
  Given the integration test scripts are set up with error handling mechanisms
  When I send a POST request to '/run-integration-test' with the payload:
  """
  {
    "testId": "TC-002"
  }
  """
  Then the response status should be 400
  And the response body should contain:
  """
  {
    "status": "error",
    "message": "Clear error message indicating the nature of the failure"
  }
  """

Scenario: Iterable Object Handling
  Given the integration test scripts are correctly set up to handle iterable objects
  When I send a POST request to '/run-integration-test' with the payload:
  """
  {
    "testId": "TC-003"
  }
  """
  Then the response status should be 200
  And the response body should contain:
  """
  {
    "status": "success",
    "message": "Test executed successfully and handled iterable objects without errors"
  }
  """

Scenario: Performance of Integration Test
  Given the integration test scripts are optimized for performance
  When I send a POST request to '/run-integration-test' with the payload:
  """
  {
    "testId": "TC-004"
  }
  """
  Then the response status should be 200
  And the response body should contain:
  """
  {
    "status": "success",
    "message": "Test completed within the performance baseline time frame"
  }
  """

Scenario: Resource Utilization of Integration Test
  Given the integration test scripts are optimized for resource utilization
  When I send a POST request to '/run-integration-test' with the payload:
  """
  {
    "testId": "TC-005"
  }
  """
  Then the response status should be 200
  And the response body should contain:
  """
  {
    "status": "success",
    "message": "Test utilized resources within the baseline limits"
  }
  """
