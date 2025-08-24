# 🔡 NATO Phonetic Alphabet Converter

A simple Python project that converts any word into its NATO phonetic alphabet equivalent (e.g., `PYTHON` → `Papa Yankee Tango Hotel Oscar November `).

## 🧠 How It Works
- Loads the **NATO phonetic alphabet** from a CSV file (`nato_phonetic_alphabet.csv`).
- Prompts the user to enter a word.
- Converts each letter into its corresponding NATO code word.
- Prints the result as a list of code words.

## 🛠️ Requirements
- Python 3.x
- pandas (`pip install pandas`)

## 📦 Files
- `main.py` → main script
- `nato_phonetic_alphabet.csv` → dataset of letters and their NATO equivalents
- `README.md` → this file

### Example of `nato_phonetic_alphabet.csv`
```csv
letter,code
A,Alpha
B,Bravo
C,Charlie
D,Delta
...
