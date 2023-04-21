// Create an array of values 

const myArray = [1, 5, 3, 6, 7, 20, 4]

console.log("Initial array:")
console.log(myArray)

function getFivePlus(arr) {
    return arr.filter(x => x >= 5)
}

console.log("Array after function applied:")
console.log(getFivePlus(myArray))