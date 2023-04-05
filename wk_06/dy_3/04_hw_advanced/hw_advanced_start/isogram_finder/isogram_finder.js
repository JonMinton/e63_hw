const IsogramFinder = function (word) {
    this.word = word
}

IsogramFinder.prototype.isIsogram = function () {
    const lowerWordArray = this.word.toLowerCase().split("")
    const uniqueLetters = []   
    console.log(lowerWordArray)
    lowerWordArray.forEach(x => {
        let addLetter = 0
        uniqueLetters.forEach(y => {
            if (y === x) {
                addLetter++
            }
        })
        if (!addLetter) {
            uniqueLetters.push(x)
        }
    });
    console.log(uniqueLetters)
    if (lowerWordArray.length === uniqueLetters.length) {
        return true
    } else {
        return false
    }
}

module.exports = IsogramFinder;
