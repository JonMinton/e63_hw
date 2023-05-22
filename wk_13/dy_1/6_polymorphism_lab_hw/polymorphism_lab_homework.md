### Polymorphism Lab / HW

An smartphone manufacturer wants you to model a virtual `Wallet` allowing customers to pay with different methods and keep track of transactions. 

## Properties

- `GiftCard` has
  - balance

- `DebitCard` and `CreditCard` have
  - card number
  - expiry date
  - security number

- `DebitCard` also has
  - account number
  - sort code

- `CreditCard` also has
  - available credit

- `Wallet` has
  - a collection of `IChargeable`s -
  - a selected `IChargeable`
  
## Behaviours

Different cards work in subtley different ways when `charge`d -


- `CreditCard`
  - adds a percentage to the transaction cost
  - logs transactions
  - reduces available credit 
  
- `DebitCard` 
  - does not add a percentage to the transaction cost
  - log transactions
  
- `GiftCard` 
  - has a balance that reduces
  - does not log transactions
  
- `Wallet`
  - the ability to choose the selected `IChargeable`
  - the ability to `pay` with a selected `IChargeable`
  - the ability to add new `IChargeable`s to the collection
  
```java
public interface IChargeable {
    void charge(double purchaseAmount);
}
```


<hr>

- **BIG HINT**: Perhaps *some* of the cards could inherit from a `PaymentCard` where similar enough.
- TDD a solution. Making a class diagram would be a useful planning exercise.



