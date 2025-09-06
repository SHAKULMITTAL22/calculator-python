Feature: API Testing for Lorem Ipsum Text Verification

Background:
  Given the API base URL is set to 'http://localhost:3000'
  And the authorization header is set to 'Bearer <token>'
  And the content type is 'application/json'

Scenario: Verify the presence and correctness of Lorem Ipsum text in the user story
  Given the user story is loaded
  When I send a GET request to '/user-story'
  Then the response status should be 200
  And the response body should contain 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac faucibus odio.'

Scenario: Verify the formatting of the text in the user story
  Given the user story is loaded
  When I send a GET request to '/user-story'
  Then the response status should be 200
  And the response body should contain headings, paragraphs, and lists
  And the formatting should be consistent and correct

Scenario: Verify the content of the text in the user story
  Given the user story is loaded
  When I send a GET request to '/user-story'
  Then the response status should be 200
  And the response body should match the provided user story content

Scenario: Verify the load time of the user story page
  Given the user story page is accessible
  When I send a GET request to '/user-story'
  Then the response status should be 200
  And the response time should be within 2 seconds

Scenario: Verify the responsiveness of the user story page on different devices
  Given the user story page is accessible
  When I send a GET request to '/user-story' with device type 'desktop'
  Then the response status should be 200
  And the layout and functionality should be correct
  When I send a GET request to '/user-story' with device type 'tablet'
  Then the response status should be 200
  And the layout and functionality should be correct
  When I send a GET request to '/user-story' with device type 'mobile'
  Then the response status should be 200
  And the layout and functionality should be correct

Scenario: Verify the compatibility of the user story page with different browsers
  Given the user story page is accessible
  When I send a GET request to '/user-story' with browser 'Chrome'
  Then the response status should be 200
  And the functionality and layout should be correct
  When I send a GET request to '/user-story' with browser 'Firefox'
  Then the response status should be 200
  And the functionality and layout should be correct
  When I send a GET request to '/user-story' with browser 'Safari'
  Then the response status should be 200
  And the functionality and layout should be correct
  When I send a GET request to '/user-story' with browser 'Edge'
  Then the response status should be 200
  And the functionality and layout should be correct

Scenario: Handle incorrect input for user story page
  Given the user story page is accessible
  When I send a GET request to '/user-story' with incorrect input
  Then the response status should be 400
  And the response body should contain an error message

Scenario: Handle unauthorized access for user story page
  Given the user story page is accessible
  When I send a GET request to '/user-story' without authorization header
  Then the response status should be 401
  And the response body should contain an error message

Scenario: Handle non-existent user story page
  Given the user story page is accessible
  When I send a GET request to '/user-story/non-existent'
  Then the response status should be 404
  And the response body should contain an error message
