# Python Calculator

A simple command-line calculator implemented in Python, capable of handling basic arithmetic operations properly respecting operator precedence and parentheses.

## Features

- **Basic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Order of Operations**: Correctly handles operator precedence (Multiplication/Division before Addition/Subtraction).
- **Parentheses**: Supports nested parentheses to group expressions.

## Project Structure

```
.
├── main.py              # Entry point (currently empty/placeholder)
├── modules/
│   ├── affichage.py     # Display module (placeholder)
│   ├── op_base.py       # Basic operations (placeholder)
│   └── result.py        # Core logic: parsing and calculation
└── README.md            # Project documentation
```

## Usage

Currently, the core logic is contained within `modules/result.py`. To run the calculator with the default example expression:

```bash
python modules/result.py
```

### Example

The default example in `result.py` processes the following expression list:
`[12 , "+", 12, "/", 12, "*", 12, "-", 12, "*", "(", 12, "+", 12, ")"]`

Which corresponds to: $12 + 12 / 12 * 12 - 12 * (12 + 12)$

## Requirements

- Python 3.x
