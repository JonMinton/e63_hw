### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# There is not intialisation method so references to self will not work

  def check_for_ace(self, card):
    if card.value = 1: # There should be two = to check for equality 
      return True
    else # There should be a colon after else
      return False
   

  dif highest_card(self, card1 card2): # This should be def not dif
  # There should be a comma after card1
  if card1.value > card2.value: # As a result of def being typed incorrectly this block is not indented as not recognised as part of a function or method
    return card # This should be card1
  else:
    return card2
  


def cards_total(self, cards):
  total # this is not assigned anything
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
