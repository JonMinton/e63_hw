document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript loaded');

  const form = document.querySelector("#new-item-form");
  form.addEventListener("submit", handleFormSubmit);
});

const handleFormSubmit = function (event) {
  event.preventDefault();
  // console.table(event);
  // console.log(event)
  // console.log(event.target)
  const collection = document.getElementsByClassName("form-item");
  // console.log(collection)

  const newTitle = collection[0].children[1].value
  const newAuthor = collection[1].children[1].value
  const newType = collection[2].children[1].value

  this.reset()

  console.log(`heard title ${newTitle} and author ${newAuthor} and type ${newType}`)

  const readingList = document.querySelector("#reading-list")

  const newEntry = document.createElement("li")
  const innerList = newEntry.appendChild(document.createElement("ul"))
  innerList.className = "to-read-entry"    
  const li1 = innerList.appendChild(document.createElement("li"));
  li1.className = "to-read-item"
  li1.textContent = `${newTitle}`;

  const li2 = innerList.appendChild(document.createElement("li"));
  li2.className = "to-read-item"
  li2.textContent = `${newAuthor}`;

  const li3 = innerList.appendChild(document.createElement("li"));
  li3.className = "to-read-item"
  li3.textContent = `${newType}`;

  readingList.appendChild(newEntry)
  console.log(readingList)


}