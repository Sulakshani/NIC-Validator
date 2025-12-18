# ---------------------------------------------
# Sri Lankan NIC Validator using DFA
# CM3230 - Automata Theory
# ---------------------------------------------

def validate_nic(nic_input):
    state = "q0"
    nic = nic_input.strip()

    for ch in nic:
        # First 9 digits
        if state == "q0":
            state = "q1" if ch.isdigit() else "q_reject"

        elif state == "q1":
            state = "q2" if ch.isdigit() else "q_reject"

        elif state == "q2":
            state = "q3" if ch.isdigit() else "q_reject"

        elif state == "q3":
            state = "q4" if ch.isdigit() else "q_reject"

        elif state == "q4":
            state = "q5" if ch.isdigit() else "q_reject"

        elif state == "q5":
            state = "q6" if ch.isdigit() else "q_reject"

        elif state == "q6":
            state = "q7" if ch.isdigit() else "q_reject"

        elif state == "q7":
            state = "q8" if ch.isdigit() else "q_reject"

        elif state == "q8":
            state = "q9" if ch.isdigit() else "q_reject"

        # Branching at 9th digit
        elif state == "q9":
            if ch.upper() in ['V', 'X']:
                state = "q_old_accept"
            elif ch.isdigit():
                state = "q10"
            else:
                state = "q_reject"

        # New NIC path (digits 10–12)
        elif state == "q10":
            state = "q11" if ch.isdigit() else "q_reject"

        elif state == "q11":
            state = "q12" if ch.isdigit() else "q_reject"

        elif state == "q12":
            state = "q_reject"  # No more characters allowed

        else:
            state = "q_reject"
            break

    # Final acceptance
    if state == "q_old_accept" and len(nic) == 10:
        return "ACCEPT (Old NIC Format)"

    elif state == "q12" and len(nic) == 12:
        return "ACCEPT (New NIC Format)"

    else:
        return "REJECT"


# ---------------------------------------------
# AUTOMATIC TEST CASES
# ---------------------------------------------

print("=== AUTOMATIC TEST CASE RESULTS ===")

test_cases = [
    "951234567V",
    "951234567v",
    "199512345678",
    "940123456",
    "19940123456V",
    "ABC123456V",
    "123456789X"
]

for nic in test_cases:
    print(f"Input: {nic} -> Result: {validate_nic(nic)}")


# ---------------------------------------------
# INTERACTIVE MODE
# ---------------------------------------------

print("\n=== INTERACTIVE NIC VALIDATION ===")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("Enter NIC: ")

    if user_input.lower() == "exit":
        print("Program terminated.")
        break

    print("Result:", validate_nic(user_input))
