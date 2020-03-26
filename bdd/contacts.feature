Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>, <home>, <mobile>, <work> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  |firstname  |lastname   |address  |home  |mobile  |work  |email  |
  |firstname1 |lastname1  |address1 |home1 |mobile1 |work1 |email1 |
  |firstname2 |lastname2  |address2 |home2 |mobile2 |work2 |email2 |



Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact

Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list
