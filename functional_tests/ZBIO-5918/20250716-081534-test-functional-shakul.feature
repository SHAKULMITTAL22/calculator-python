Feature: API Testing for Integration and Functional Scenarios

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify Gherkin Parsing
  Given the feature file with valid Gherkin syntax
  When I run the Gherkin parser
  Then the parser should identify all scenarios without errors

Scenario: Check Integration Test Execution
  Given the integration test methods are correctly implemented
  When I execute the integration test
  Then the test should complete without encountering errors

Scenario: Validate Error Handling
  Given the integration test methods are implemented with error handling
  When I introduce an error in the integration test
  And I execute the integration test
  Then the error should be caught and handled gracefully without crashing the test

Scenario: Verify Object Iterability
  Given the integration test methods expect objects to be iterable
  When I execute the integration test with objects that should be iterable
  Then the objects should be treated as iterable and the test should execute as expected

Scenario: Check for Correct Object Type
  Given the integration test methods expect specific object types
  When I pass objects of the correct type to the integration test
  And I execute the test
  Then the objects should be of the correct type and the test should execute without iteration errors

Scenario: Performance of Integration Test
  Given a stable environment for consistent performance measurement
  When I execute the integration test 10 times
  Then the average execution time should be within acceptable limits

Scenario: Resource Utilization
  Given tools to monitor system resources
  When I execute the integration test
  Then the CPU, memory, and disk usage should remain within acceptable limits

Scenario: Error Logging
  Given the error logging mechanism is implemented
  When I introduce an error in the integration test
  And I execute the test
  Then the error should be logged with relevant details, including timestamp and error message

Scenario: Test HTTP GET method
  Given the API base URL is set to 'http://localhost:3000'
  When I send a GET request to '/api/resource'
  Then the response status should be 200
  And the response should contain 'resource details'

Scenario: Test HTTP POST method
  Given the API base URL is set to 'http://localhost:3000'
  And the request payload is '{"key": "value"}'
  When I send a POST request to '/api/resource'
  Then the response status should be 201
  And the response should contain 'resource created'

Scenario: Test HTTP PUT method
  Given the API base URL is set to 'http://localhost:3000'
  And the request payload is '{"key": "newValue"}'
  When I send a PUT request to '/api/resource/1'
  Then the response status should be 200
  And the response should contain 'resource updated'

Scenario: Test HTTP DELETE method
  Given the API base URL is set to 'http://localhost:3000'
  When I send a DELETE request to '/api/resource/1'
  Then the response status should be 204
  And the response should be empty

Scenario: Test invalid input for HTTP POST method
  Given the API base URL is set to 'http://localhost:3000'
  And the request payload is '{"invalidKey": "value"}'
  When I send a POST request to '/api/resource'
  Then the response status should be 400
  And the response should contain 'Bad Request'

Scenario: Test unauthorized access
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer invalidToken'
  When I send a GET request to '/api/resource'
  Then the response status should be 401
  And the response should contain 'Unauthorized'

Scenario: Test resource not found
  Given the API base URL is set to 'http://localhost:3000'
  When I send a GET request to '/api/nonexistent'
  Then the response status should be 404
  And the response should contain 'Not Found'

Scenario: Test server error
  Given the API base URL is set to 'http://localhost:3000'
  When I send a GET request to '/api/error'
  Then the response status should be 500
  And the response should contain 'Internal Server Error'
