import fetch from 'node-fetch';
import fs from 'fs';
import path from 'path';

async function fetchXkcds() {
  // Step 1: fetch the first URL and get the number of pages
  const res = await fetch('https://xkcd.com/info.0.json');
  const json = await res.json();
  const numPages = json.num;

  const directory = path.join(new URL('/Users/JonMinton/e63_hw/wk_07/dy_5/xkcd_app/src/data', import.meta.url).pathname, 'xkcds.json')

  // Step 2: create an array to store all xkcd objects
  const allXkcds = [];

  // Step 3: iterate through each page and fetch the data
  for (let i = 1; i <= numPages; i++) {
    if (i !== 404) {
        const url = `https://xkcd.com/${i}/info.0.json`;
        const res = await fetch(url);
        const json = await res.json();
        allXkcds.push(json);
        console.log(i)
    
    }
  }

    // Step 4: Save the resulting array as a JSON file
    if (!fs.existsSync(directory)) {
      fs.mkdirSync(directory, { recursive: true });
    }
    const filePath = path.join(directory, 'allXkcds.json');
    const jsonString = JSON.stringify(allXkcds, null, 2);
    fs.writeFileSync(filePath, jsonString);
  
    console.log(`All comics saved to ${filePath}`);
  

  // Step 5: log the results
  return allXkcds
}

fetchXkcds();