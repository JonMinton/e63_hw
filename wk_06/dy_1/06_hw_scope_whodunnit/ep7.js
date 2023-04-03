let murderer = 'Professor Plum';

const changeMurderer = function() {
  murderer = 'Mr. Green';
//   This is implicitly var murderer = 'Mr. Green'

  const plotTwist = function() {
    let murderer = 'Colonel Mustard';
    // This version of murderer disappears when the scope does

    const unexpectedOutcome = function() {
      murderer = 'Miss Scarlet';
    //   This will change but only to the locally scoped version
    // So Col Mustard becomes Miss Scarlet
    }

    unexpectedOutcome();
    // This will make some changes to a locally scoped version, but they won't persist beyond the scope
  }

  plotTwist();
//   Only the first line in this function will actually change the globally scoped variable
}

const declareMurderer = function() {
  return `The murderer is ${murderer}.`;
}

changeMurderer();
const verdict = declareMurderer();
console.log(verdict);
// The murderer is Mr Green