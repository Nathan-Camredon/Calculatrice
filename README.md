# Python Calculator

A command-line calculator implemented in Python, capable of handling arithmetic operations, trigonometric functions, and percentages, while respecting operator precedence and parentheses.

## Features

- **Basic Operations**: Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Advanced Operations**:
    - Trigonometry: `sin`, `cos`, `tan`
    - Angle conversion: `rad` (degrees to radians)
    - Percentage: `percent` (e.g., `10 percent 50` -> 5.0)
- **Order of Operations**: Correctly handles operator precedence.
- **Parentheses**: Supports nested parentheses `(...)` to group expressions.

## Project Structure

```
.
├── main.py              # Entry point of the application
├── modules/
│   ├── enter.py         # Handles user input and parsing
│   ├── comp_op.py       # Mathematical functions (sin, cos, tan, 
│   └── result.py        # Core calculation logic and expression 
├── .gitignore
└── README.md            # Project documentation
```

## Usage

Run the calculator from the project root:

```bash
python main.py
```

Enter your operation when prompted:

```
Entrez une operation :  3 + 3
Résultat final : 6
```

Examples:
- `3 + 3`
- `10 percent 50`
- `sin 90` (Note: Trigonometric inputs should be handled as per implementation, usually requires `rad` for degrees if logic dictates)

## Requirements

- Python 3.x
