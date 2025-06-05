
# 🔐 Human-Like Password Strength Checker

This is an advanced Python-based password strength checker that goes beyond basic rules. It analyzes passwords the way a real attacker might — detecting patterns, estimating crack time, checking for breaches, and more.

## 🧠 Features

- Character variety checks (uppercase, digits, special chars, etc.)
- Pattern detection (e.g., `1234`, `qwerty`, repeated chars)
- Crack time estimation (based on entropy)
- Breach check via HaveIBeenPwned API
- Final human-likeness strength score (Weak / Medium / Strong)

## 🛠️ Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- Internet connection (for breach check)

## 🚀 How to Run

```bash
bash check.sh
=======
# password-strength-checker
>>>>>>> 7d984a4e6fef4727fef3a8dee5becb7876d0bc40
