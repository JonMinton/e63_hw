const Traveller = function(journeys) {
  this.journeys = journeys;
};

Traveller.prototype.getJourneyStartLocations = function() {
  return this.journeys.map(x => x.startLocation)
};

Traveller.prototype.getJourneyEndLocations = function () {
  return this.journeys.map(x => x.endLocation)
};

Traveller.prototype.getJourneysByTransport = function (transport) {
  return this.journeys.filter(x => x.transport === transport)
};

Traveller.prototype.getJourneysByMinDistance = function (minDistance) {
  return this.journeys.filter(x => x.distance >= minDistance)
};

Traveller.prototype.calculateTotalDistanceTravelled = function () {
  return this.journeys.reduce((total, x) => total + x.distance, 0)

};

Traveller.prototype.getUniqueModesOfTransport = function () {
  const uniqueModes = []
  this.journeys.forEach((x) => {
      if (!uniqueModes.includes(x.transport)) {
        uniqueModes.push(x.transport)
      }
    }
  )
  return uniqueModes
};


module.exports = Traveller;
