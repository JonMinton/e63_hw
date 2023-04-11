const PangramFinder = function (phrase) {
  this.alphabet = 'qwertyuiopasdfghjklzxcvbnm'.split('');
  this.phrase = phrase.split('').
    map(x => x.toLowerCase()).
    map((x) => {
      if (x === "?") {
        return "\\?"
      } else {
        return x
      }
    }).
  filter(x => ("qwertyuiopasdfghjklzxcvbnm".match(x)))

}

PangramFinder.prototype.isPangram = function () {
  let numMatches = 0
  if (this.phrase.length === 0) {return false}
  this.alphabet.forEach((x) => {
    let matchFound = false;
    this.phrase.forEach((y) => {
        if (x === y) {
          matchFound = true
        }
      })
      if (matchFound) {
        numMatches++
      }
    }
  );

  if (numMatches === 26) {
    return true
  } else {
    return false
  }
}
module.exports = PangramFinder;
