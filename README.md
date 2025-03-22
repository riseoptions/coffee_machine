# Coffee Machine Project (Python)

See Pythonis kirjutatud projekt simuleerib kohvimasinat, mis suudab valmistada erinevaid jooke nagu espresso ja latte, haldades koostisosi ja võimaldades kasutajal täita kohvimasina varusid.

## Projekti Struktuur

```plaintext
coffee_machine_project/
│
├── main.py                # Põhiprogramm, kus kõik kokku pannakse
├── coffee_machine.py       # CoffeeMachine klass ja selle loogika
├── beverage.py             # Erinevad kohvijookide klassid (nt Espresso ja Latte)
├── ingredient_manager.py   # Koostisosade haldur
├── tests/
│   ├── test_coffee_machine.py   # Unit testid kohvimasina jaoks
│   └── test_ingredient_manager.py # Unit testid koostisosade halduri jaoks



```
# Coffee Machine Project (Java)


```markdown


See Java projekt simuleerib kohvimasinat, mis suudab valmistada erinevaid jooke nagu espresso ja latte, haldades koostisosi ja võimaldades kasutajal täita kohvimasina varusid.

## Projekti Struktuur

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


```
---

### Kuidas kasutada:
- **Python projekti**
- **Java projekti**




```markdown
# Coffee Machine Project

See projekt simuleerib kohvimasinat, mis suudab valmistada erinevaid kohvijooke nagu espresso ja latte, haldades koostisosi ja võimaldades kasutajal täiendada kohvimasina varusid. Projekt on loodud kahes programmeerimiskeeles: **Python** ja **Java**. 

## Projekti Struktuur

### Python Projekt

```plaintext
coffee_machine_project/
│
├── main.py                # Põhiprogramm, kus kõik kokku pannakse
├── coffee_machine.py       # CoffeeMachine klass ja selle loogika
├── beverage.py             # Erinevad kohvijookide klassid (nt Espresso ja Latte)
├── ingredient_manager.py   # Koostisosade haldur
├── tests/
│   ├── test_coffee_machine.py   # Unit testid kohvimasina jaoks
│   └── test_ingredient_manager.py # Unit testid koostisosade halduri jaoks
```

### Java Projekt

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
```

---

## Python Projekti Kasutamine ja Käivitamine

### Nõuded

- **Python 3** peab olema installitud.
- Soovitame kasutada **virtuaalset keskkonda** sõltuvuste haldamiseks.

### Paigaldamine ja Käivitamine

1. **Projekti kloonimine**:
   ```bash
   git clone https://github.com/sinu_githubi_kasutajanimi/coffee_machine_project.git
   cd coffee_machine_project
   ```

2. **(Valikuline) Virtuaalse keskkonna loomine ja aktiveerimine**:
   - Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Sõltuvuste installimine**:
   - Kui projektil on väliseid sõltuvusi, võid lisada need `requirements.txt` faili ja installida need:
     ```bash
     pip install -r requirements.txt
     ```

4. **Testide käivitamine**:
   - Enne projekti käivitamist, veendu, et testid töötavad:
     ```bash
     python -m unittest discover tests
     ```

5. **Projekti käivitamine**:
   ```bash
   python main.py
   ```

### Kasutamine

Pärast projekti käivitamist avaneb menüü, kus saab valida erinevaid tegevusi:

1. **Make Espresso**: Valmista espresso.
2. **Make Latte**: Valmista latte.
3. **Refill Ingredients**: Täida koostisosade varusid (vesi, kohvioad, piim).
4. **Exit**: Sule programm.

Näide kasutajaga suhtlemisest:

```plaintext
--- Coffee Machine ---
1. Make Espresso
2. Make Latte
3. Refill Ingredients
4. Exit

Please enter your choice: 1
Espresso is ready!
```

### Testimine

Testid paiknevad `tests/` kaustas ja katavad põhifunktsionaalsust:
- **test_coffee_machine.py**: Testib kohvimasina põhitoiminguid.
- **test_ingredient_manager.py**: Testib koostisosade haldamist.

Testide käivitamiseks:
```bash
python -m unittest discover tests
```

---

## Java Projekti Kasutamine ja Käivitamine

### Nõuded

- **Java JDK** peab olema installitud (soovitatavalt JDK 8 või uuem).
- **JUnit** peab olema installitud testide jaoks (võib olla projektis juba lisatud).

### Paigaldamine ja Käivitamine

1. **Projekti kloonimine**:
   ```bash
   git clone https://github.com/sinu_githubi_kasutajanimi/coffee_machine_project.git
   cd coffee_machine_project
   ```

2. **Projekti kompileerimine**:
   - Kõik allikafailid tuleb kompileerida. Järgnev käsk kompileerib kõik `.java` failid:
     ```bash
     javac src/*.java
     ```

3. **Projekti käivitamine**:
   - Kui projekt on edukalt kompileeritud, käivita `Main.java`:
     ```bash
     java src.Main
     ```

4. **Testide käivitamine**:
   - Testide jaoks veendu, et `JUnit` on installitud ja olemas. Kasuta alljärgnevat käsku:
     ```bash
     javac -cp .:junit-4.12.jar tests/CoffeeMachineTest.java tests/IngredientManagerTest.java
     java -cp .:junit-4.12.jar org.junit.runner.JUnitCore tests.CoffeeMachineTest
     ```

### Kasutamine

Pärast projekti käivitamist avaneb menüü, kus saab valida erinevaid tegevusi:

1. **Make Espresso**: Valmista espresso.
2. **Make Latte**: Valmista latte.
3. **Refill Ingredients**: Täida koostisosade varusid (vesi, kohvioad, piim).
4. **Exit**: Sule programm.

Näide kasutajaga suhtlemisest:

```plaintext
--- Coffee Machine ---
1. Make Espresso
2. Make Latte
3. Refill Ingredients
4. Exit

Please enter your choice: 1
Espresso is ready!
```

### Testimine

Testid paiknevad `tests/` kaustas ja katavad põhifunktsionaalsust:
- **CoffeeMachineTest.java**: Testib kohvimasina põhitoiminguid.
- **IngredientManagerTest.java**: Testib koostisosade haldamist.

Testide käivitamiseks:
```bash
javac -cp .:junit-4.12.jar tests/CoffeeMachineTest.java tests/IngredientManagerTest.java
java -cp .:junit-4.12.jar org.junit.runner.JUnitCore tests.CoffeeMachineTest
```

---

## Autorid

- **Sinu nimi**
- **Sinu e-mail** (valikuline)
```

---

### Kuidas kasutada:
- Kopeerige see markdown kood ja paigutage see `README.md` failina oma projekti kausta. See sisaldab kasutamis- ja käivitamisjuhiseid nii Python kui ka Java projektide jaoks ühes kohas.

