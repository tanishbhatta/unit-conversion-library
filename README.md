# unit-conversion-library
A simple library for common unit conversions.

Supports:

* Distance conversions
* Weight conversions
* Temperature conversions

Built as part of my Python learning journey to practice writing reusable, modular code instead of duplicating calculations across projects

---

# Features
**Distance**
* Kilometer ↔ Meter
* Kilometer ↔ Mile
* Meter ↔ Kilometer
* Meter ↔ Foot
* Foot ↔ Meter
* Mile ↔ Kilometer
* Centimeter ↔ Inch
* Inch ↔ Centimeter

**Weight**
* Kilogram ↔ Gram
* Gram ↔ Kilogram
* Kilogram ↔ Pound
* Pound ↔ Kilogram
* Gram ↔ Ounce
* Ounce ↔ Gram
* Ton ↔ Kilogram
* Kilogram ↔ Ton

**Temperature**
* Celsius ↔ Fahrenheit
* Fahrenheit ↔ Celsius
* Celsius ↔ Kelvin
* Kelvin ↔ Celsius
* Fahrenheit ↔ Kelvin
* Kelvin ↔ Fahrenheit
---
# Installation
Clone the repository:
```bash
git clone https://github.com/TanishBhatta/unit-conversion-library.git
cd unit-conversion-library
```
No external dependencies.
---
# Usage
**Distance Conversion**
```python
from distance import km_to_miles

result = km_to_miles(10)

print(result)
```
Output:
```text
6.21
```
---
**Weight Conversion**
```python
from weight import kg_to_pounds

result = kg_to_pounds(5)

print(result)
```
Output:
```text
11.02
```
---
**Temperature Conversion**
```python
from temperature import celsius_to_fahrenheit

result = celsius_to_fahrenheit(25)

print(result)
```
Output:
```text
77
```
---
# Project Structure
```text
unit-conversion-library/
|
|-- distance.py
|-- weight.py
|-- temperature.py
|-- README.md
```
---
# Why I Built This
While learning Python, I noticed I was rewriting the same conversion functions repeatedly across different projects.
Instead of duplicating the logic every time, I decided to create a reusable module.

The project helped me practice:
* Modular programming
* Function design
* Code reusability
* Project organization
---
# Future Improvements
* Additional conversion categories
* Unit tests
* Better error handling
---
# Author
**Tanish Bhatta**

Building in public from Kathmandu, Nepal.

Github: https://github.com/TanishBhatta

---
