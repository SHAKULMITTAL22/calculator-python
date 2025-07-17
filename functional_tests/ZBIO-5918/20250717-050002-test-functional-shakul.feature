Feature: API Testing for Integration and Gherkin Parsing

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify that integration tests are executed without errors
