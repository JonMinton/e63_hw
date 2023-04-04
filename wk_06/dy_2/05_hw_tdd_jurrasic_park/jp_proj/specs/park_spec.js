const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {

  beforeEach(function () {
    park = new Park("Jurassic Dinosharkpark", 24.99);
    d1 = new Dinosaur('t-rex', 'carnivore', 50);
    d2 = new Dinosaur('tricert', 'herbivore', 30);
    d3 = new Dinosaur('raptor', 'omnivore', 20);

  })

  it('should have a name', 
    function() {
      assert.equal(park.name, "Jurassic Dinosharkpark")

    }
  );

  it('should have a ticket price',
    function() {
      assert.strictEqual(park.ticketPrice, 24.99)
    }
  );

  it('should be able to add a dinosaur to its collection',
  function() {
    assert.strictEqual(park.dinosaurs.length, 0)
    park.addDinosaur(d1)
    assert.strictEqual(park.dinosaurs.length, 1)
  }
  );

  it('should have a collection of dinosaurs',
  function() {
    park.addDinosaur(d1)
    park.addDinosaur(d2)
    park.addDinosaur(d3)
    assert.strictEqual(park.dinosaurs.length, 3)

  }
  );


  it('should be able to remove a dinosaur from its collection',
  function() {
    park.addDinosaur(d1)
    park.addDinosaur(d2)
    park.addDinosaur(d3)
    assert.strictEqual(park.dinosaurs.length, 3)
    park.removeDinosaur()
    assert.strictEqual(park.dinosaurs.length, 2)
  }
  );

  it('should be able to find the dinosaur that attracts the most visitors',
    function() {
      park.addDinosaur(d1)
      park.addDinosaur(d2)
      park.addDinosaur(d3)
      let mostPopDino = park.findMostPopularDinosaur()        
      assert.equal(mostPopDino.species, "t-rex")
    }
  );

  it('should be able to find all dinosaurs of a particular species',
  function() {
    park.addDinosaur(d1)
    park.addDinosaur(d2)
    park.addDinosaur(d2)
    park.addDinosaur(d3)
    let allTricerts = park.findDinosaursBySpecies("tricert")
    assert.strictEqual(allTricerts.length, 2)

  }
  );

  it('should be able to calculate the total number of visitors per day',
  function() {
    park.addDinosaur(d1)
    park.addDinosaur(d2)
    park.addDinosaur(d3)
    let totalVisitorsPerDay = park.getTotalVisitors()
    assert.strictEqual(totalVisitorsPerDay, 100)
  }
  );

  it('should be able to calculate the total number of visitors per year',
  function() {
    park.addDinosaur(d1)
    park.addDinosaur(d2)
    park.addDinosaur(d3)
    let totalVisitorsPerYear = park.getTotalAnnualVisitors()
    assert.strictEqual(totalVisitorsPerYear, 36525)
  
  }

  );

  it('should be able to calculate total revenue for one year',
  function() {
    park.addDinosaur(d1)
    park.addDinosaur(d2)
    let totalAnnualRevenue = park.getTotalAnnualRevenue()
    assert.strictEqual(totalAnnualRevenue, 730207.7999999999)

  }
  );

});
