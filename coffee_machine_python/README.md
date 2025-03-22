# Coffee Machine Project

See projekt simuleerib kohvimasinat, mis suudab valmistada erinevaid kohvijooke nagu espresso ja latte. Projekti on tehtud kahes erinevas programmeerimiskeeles: **Python** ja **Java**. Mõlemal projektil on sama loogika ja arhitektuur.

## Projekti Ülesehitus

Allpool on näidatud kaustade ja failide struktuur mõlema projekti jaoks.

### 1. Python Projekt

```plaintext
coffee_machine_project/
│
├── main.py                # Põhiprogramm, kus kõik kokku pannakse
├── coffee_machine.py       # CoffeeMachine klass ja selle loogika
├── beverage.py             # Erinevad kohvijookide klassid (nt Espresso ja Latte)
├── ingredient_manager.py    # Koostisosade haldur
├── tests/
│   ├── test_coffee_machine.py   # Unit testid kohvimasina jaoks
│   └── test_ingredient_manager.py # Unit testid koostisosade halduri jaoks
