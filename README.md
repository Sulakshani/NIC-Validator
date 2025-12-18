# Sri Lankan NIC Validator

A Deterministic Finite Automaton (DFA) based validator for Sri Lankan National Identity Card (NIC) numbers, developed for CM3230 - Automata Theory.

## Overview

This program validates Sri Lankan NIC numbers using the principles of automata theory. It implements a DFA that recognizes both old and new NIC formats used in Sri Lanka.

## NIC Format Specifications

Sri Lanka uses two NIC formats:

### Old Format (10 characters)
- **Structure**: `XXXXXXXXXV` or `XXXXXXXXXX`
- **Pattern**: 9 digits followed by either 'V' or 'X'
- **Example**: `951234567V`, `123456789X`
- **Used for**: Individuals registered before 2016

### New Format (12 digits)
- **Structure**: `XXXXXXXXXXXX`
- **Pattern**: 12 consecutive digits
- **Example**: `199512345678`
- **Used for**: Individuals registered from 2016 onwards

## How It Works

The validator uses a **Deterministic Finite Automaton (DFA)** with the following states:

- **q0 to q8**: Process the first 9 digits (mandatory for both formats)
- **q9**: Decision state - branches based on the 10th character:
  - If 'V' or 'X' → transitions to `q_old_accept` (old format)
  - If digit → transitions to `q10` (new format path)
- **q10 to q12**: Process digits 10-12 for the new format
- **q_old_accept**: Accepting state for old format (10 characters total)
- **q12**: Accepting state for new format (12 characters total)
- **q_reject**: Rejection state for invalid inputs

### State Transition Logic

1. The DFA starts at state `q0`
2. Each character in the input is processed sequentially
3. Valid digits advance the state forward
4. At position 9, the automaton branches:
   - **Old Format Branch**: Letter 'V' or 'X' leads to acceptance
   - **New Format Branch**: Continued digits lead to 12-digit validation
5. Invalid characters or incorrect lengths result in rejection

## Features

- ✅ Validates both old (10-character) and new (12-digit) NIC formats
- ✅ Case-insensitive for 'V' character (accepts both 'V' and 'v')
- ✅ Automatic test suite with predefined test cases
- ✅ Interactive mode for manual validation
- ✅ Clear acceptance/rejection messages with format identification

## Installation

No external dependencies required. The program uses only Python standard library.

### Requirements
- Python 3.x

## Usage

### Running the Program

```bash
python validate_nic.py
```

### Automatic Test Mode

When you run the program, it first executes automatic test cases:

```
=== AUTOMATIC TEST CASE RESULTS ===
Input: 951234567V -> Result: ACCEPT (Old NIC Format)
Input: 951234567v -> Result: ACCEPT (Old NIC Format)
Input: 199512345678 -> Result: ACCEPT (New NIC Format)
Input: 940123456 -> Result: REJECT
Input: 19940123456V -> Result: REJECT
Input: ABC123456V -> Result: REJECT
Input: 123456789X -> Result: ACCEPT (Old NIC Format)
```

### Interactive Mode

After the automatic tests, the program enters interactive mode:

```
=== INTERACTIVE NIC VALIDATION ===
Type 'exit' to stop.

Enter NIC: 951234567V
Result: ACCEPT (Old NIC Format)

Enter NIC: 199512345678
Result: ACCEPT (New NIC Format)

Enter NIC: invalid123
Result: REJECT

Enter NIC: exit
Program terminated.
```

## Test Cases

The program includes the following built-in test cases:

| Input          | Expected Result               | Description                           |
|----------------|-------------------------------|---------------------------------------|
| 951234567V     | ACCEPT (Old NIC Format)       | Valid old format with uppercase 'V'   |
| 951234567v     | ACCEPT (Old NIC Format)       | Valid old format with lowercase 'v'   |
| 199512345678   | ACCEPT (New NIC Format)       | Valid new format (12 digits)          |
| 940123456      | REJECT                        | Only 9 digits (incomplete)            |
| 19940123456V   | REJECT                        | Too many digits before 'V'            |
| ABC123456V     | REJECT                        | Contains letters in digit positions   |
| 123456789X     | ACCEPT (Old NIC Format)       | Valid old format with 'X'             |

## Implementation Details

### Algorithm

The validation follows these steps:

1. **Initialize**: Start at state `q0`
2. **Iterate**: Process each character in the input string
3. **Validate**: Check if the character is valid for the current state
4. **Transition**: Move to the next state based on the character
5. **Finalize**: Check if the final state is an accepting state and length is correct

### Time Complexity

- **Time**: O(n), where n is the length of the input string (max 12)
- **Space**: O(1), only a constant amount of memory is used

### Key Functions

#### `validate_nic(nic_input)`

**Parameters:**
- `nic_input` (str): The NIC string to validate

**Returns:**
- `"ACCEPT (Old NIC Format)"` - For valid old format NICs
- `"ACCEPT (New NIC Format)"` - For valid new format NICs
- `"REJECT"` - For invalid NICs

**Logic:**
- Strips whitespace from input
- Processes each character through the DFA
- Returns acceptance status with format identification

## Automata Theory Concepts

This project demonstrates several key concepts from Automata Theory:

1. **Deterministic Finite Automaton (DFA)**
   - Each state has exactly one transition for each input symbol
   - No ambiguity in state transitions

2. **State Machine Design**
   - Well-defined states representing validation progress
   - Clear acceptance and rejection states

3. **Regular Language Recognition**
   - NIC format can be expressed as a regular expression
   - DFA efficiently recognizes strings in this language

4. **Branching Paths**
   - The automaton handles multiple format possibilities
   - Elegant branching at state q9 for format differentiation

## Educational Context

This project was developed for **CM3230 - Automata Theory** to demonstrate:
- Practical application of DFA in real-world validation
- State machine design and implementation
- Regular language recognition
- Computational thinking in pattern matching

## Limitations

- Does not verify if the NIC number is actually issued or valid in the Sri Lankan database
- Does not validate the embedded information (birth year, days, etc.)
- Does not check for specific invalid date encodings within the NIC
- Purely syntactic validation based on format structure

## Future Enhancements

Potential improvements could include:
- Semantic validation (checking encoded birth dates)
- Gender determination from day-of-year encoding
- Age calculation from NIC number
- Checksum validation (if applicable)
- GUI interface for easier interaction
- Batch validation from file input

## License

This is an educational project developed for academic purposes.



## Contributing

This is a course project. For educational purposes, feel free to:
- Study the implementation
- Suggest improvements
- Adapt for learning purposes

---

**Note**: This validator checks only the format/syntax of NIC numbers. For official verification, consult the Department of Registration of Persons in Sri Lanka.
