const Park = function(name, ticketPrice){
    this.name = name
    this.ticketPrice = ticketPrice
    this.dinosaurs = []
}

Park.prototype.addDinosaur = function(dino){
    this.dinosaurs.push(dino)
}

Park.prototype.removeDinosaur = function(){
    this.dinosaurs.pop()
}

Park.prototype.findMostPopularDinosaur = function() {
    let most_popular = 0 
    for (dino of this.dinosaurs) {
        if (dino.guestsAttractedPerDay > most_popular) {
            most_popular = dino.guestsAttractedPerDay
        }
    }
    for (dino of this.dinosaurs) {
        if (dino.guestsAttractedPerDay === most_popular) {
            return (dino)
        }
    }
}

Park.prototype.findDinosaursBySpecies = function(species){
   const selectedDinos = [] 
   for (dino of this.dinosaurs){
    if (dino.species === species) {
        selectedDinos.push(dino)
    }
   }
   return selectedDinos 
}

Park.prototype.getTotalVisitors = function() {
    let totalVisitors = 0
    for (dino of this.dinosaurs) {
        totalVisitors += dino.guestsAttractedPerDay
    }
    return totalVisitors
}

Park.prototype.getTotalAnnualVisitors = function() {
    const totalAnnualVisitors = this.getTotalVisitors() * 365.25    
    return totalAnnualVisitors
}

Park.prototype.getTotalAnnualRevenue = function(){
    const totalAnnualRevenue = this.getTotalAnnualVisitors() * this.ticketPrice
    return totalAnnualRevenue
}

module.exports = Park;