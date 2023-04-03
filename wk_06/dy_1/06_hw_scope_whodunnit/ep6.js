let murderer = 'Colonel Mustard';

const changeMurderer = function() {
  murderer = 'Mr. Green';
//   murderer is in scope, so changed accordingly

  const plotTwist = function() {
    murderer = 'Mrs. White';
  }

  plotTwist();
//   murderer is still in scope in plotTwist, so changed again to Mrs White
}

const declareMurderer = function () {
  return `The murderer is ${murderer}.`;
}

changeMurderer();
const verdict = declareMurderer();
console.log(verdict);
// The murderer is Mrs White