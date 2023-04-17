describe("Calculator", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000");
  })

  it('should have working number buttons', () => {
    cy.get('#number2').click();
    cy.get('.display').should('contain', '2')
    cy.get('#number1').click();
    cy.get('.display').should('contain', '21')
    cy.get('#number3').click();
    cy.get('.display').should('contain', '213')


  })

  it('should have working arithmetic operations', () => {
    cy.get('#number2').click()
    cy.get('#operator_add').click()
    cy.get('#number3').click()
    cy.get('#operator-equals').click()
    cy.get('.display').should('contain', '5')

  })

  it('should chain multiple operators together', () => {
    cy.get('#number1').click()
    cy.get('#operator_add').click()
    cy.get('#number1').click()
    cy.get('#operator_add').click()
    cy.get('#operator-equals').click()
    cy.get('.display').should('contain', '3')
  
  })

  it('should work for negative numbers', () => {
    cy.get('#number3').click()
    cy.get('#operator-subtract').click()
    cy.get('#number5').click()
    cy.get('#operator-equals').click()
    cy.get('.display').should('contain', '-2')
    
  })

  it('should work for decimal numbers', () => {
    cy.get('#number0').click()
    cy.get('#decimal').click()
    cy.get('#number1').click()
    cy.get('#operator-equals').click()
    cy.get('#operator_add').click()
    cy.get('#number1').click()
    cy.get('#operator-equals').click()
    cy.get('.display').should('contain', '1.1')
  })  

  it('should work for large numbers', () => {
    cy.get('#number1').click()
    cy.get('#number0').click()
    cy.get('#number0').click()
    cy.get('#number0').click()
    cy.get('#number0').click()
    cy.get('#operator_add').click()
    cy.get('#number2').click()
    cy.get('#number0').click()
    cy.get('#number0').click()
    cy.get('#number0').click()
    cy.get('#number0').click()
    cy.get('#operator-equals').click()
    cy.get('.display').should('contain', '30000')
  })  

  it('should not divide by zero', () => {
    cy.get('#number1').click()
    cy.get('#operator-divide').click()
    cy.get('#number0').click()
    cy.get('#operator-equals').click()
    cy.get('.display').should('contain', 'Not a number')
  })  


})

// You should write tests to ensure the following requirements are met:

// 1. Do the number buttons update the display of the running total?
// 2. Do the arithmetical operations update the display with the result of the operation?

// - E.g. does `2 + 2 -` update the display to 4
// 3. Can multiple operations be chained together?
// - E.g. does `3 + 1 - 2` == 2
// 4. Is the output as expected for positive numbers
// 5. Is the output as expected for negative numbers
// 6. Is the output as expected for decimal numbers
// 7. Is the output as expected for very large numbers
// 8. What does the code do in exceptional circumstances? Specifically, if you divide by zero, what is the effect? Write a test to describe what you'd prefer to happen, and then correct the code to make that test pass (you will need to modify the Calculator model to meet this requirement).
