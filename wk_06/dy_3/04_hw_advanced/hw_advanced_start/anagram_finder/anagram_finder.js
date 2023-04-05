const AnagramFinder = function (word) {
    this.word = word.toLowerCase()

}

AnagramFinder.prototype.findAnagrams = function (otherWords) {
    console.log(`word: ${this.word}`)
    console.log(`initial candidates: ${otherWords}`)
    let candidateWords = []

    for (let word of otherWords){
        const lowerWord = word.toLowerCase()
        let candidateIsMatch = true
        if (lowerWord.length !== this.word.length) {
            candidateIsMatch = false
        }
        if (lowerWord === this.word) {
            candidateIsMatch = false
        }
        console.log(`this candidate word: ${word}`)
        for (let letter of this.word) {
            let outcome = lowerWord.match(letter)
            if (!outcome) {
                candidateIsMatch = false
            }
        }
        if (candidateIsMatch){
            candidateWords.push(word)
        }
    }
    console.log(`remaining candidates: ${candidateWords}`)

    return candidateWords
}

module.exports = AnagramFinder;
