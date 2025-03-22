# Coffee Machine Project

See projekt simuleerib kohvimasinat, mis suudab valmistada erinevaid kohvijooke nagu espresso ja latte. Projekti on tehtud kahes erinevas programmeerimiskeeles: **Python** ja **Java**. Mõlemal projektil on sama loogika ja arhitektuur.

## Projekti Ülesehitus

```plaintext
coffee_machine_project/
│
├── src/
│   ├── CoffeeMachine.java       # CoffeeMachine klass ja selle loogika
│   ├── Beverage.java            # Erinevad kohvijookide klassid (nt Espresso ja Latte)
│   ├── Espresso.java            # Espresso klass
│   ├── Latte.java               # Latte klass
│   ├── IngredientManager.java   # Koostisosade haldur
│   └── Main.java                # Põhiprogramm, kus kõik kokku pannakse
│
├── tests/
│   ├── CoffeeMachineTest.java   # Unit testid kohvimasina jaoks
│   └── IngredientManagerTest.java # Unit testid koostisosade halduri jaoks

