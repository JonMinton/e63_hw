const UpperCaser = function (words) {
    this.words = words
}

UpperCaser.prototype.toUpperCase = function () {
    return this.words.map(x => x.toUpperCase())
}

module.exports = UpperCaser;
