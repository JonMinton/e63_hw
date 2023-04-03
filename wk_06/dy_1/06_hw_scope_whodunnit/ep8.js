const scenario = {
    murderer: 'Mrs. Peacock',
    room: 'Conservatory',
    weapon: 'Lead Pipe'
  };
  
  const changeScenario = function() {
    scenario.murderer = 'Mrs. Peacock';
    scenario.room = 'Dining Room';
    // These changes will be made when the function is run
    // And they will persist beyond the scope of the function
  
    const plotTwist = function(room) {
      if (scenario.room === room) {
        scenario.murderer = 'Colonel Mustard';
        // This change WILL be made
      }
  
      const unexpectedOutcome = function(murderer) {
        if (scenario.murderer === murderer) {
            // Because the change of murderer will have been made, this condition will be true
          scenario.weapon = 'Candle Stick';
        //   So this change will be made too
        }
      }
  
      unexpectedOutcome('Colonel Mustard');
    }
  
    plotTwist('Dining Room');
  }
  
  const declareWeapon = function() {
    return `The weapon is ${scenario.weapon}.`
  }
  
  changeScenario();
  const verdict = declareWeapon();
  console.log(verdict);
//   Should be the weapon is candle stick
  