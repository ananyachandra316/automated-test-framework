# Python Automated Test Framework

A hardware/system validation simulator written in Python, built to demonstrate
test engineering fundamentals for embedded, firmware, and systems integration roles.

## What it does
- Simulates 7 hardware sensor readings (voltage, temperature, signal strength, etc.)
- Evaluates each reading against engineering pass/fail specifications
- Prints a colour-coded results table to the terminal
- Saves a timestamped structured report to results/report.txt

## How to run
```bash
python3 main.py
```

## Project structure
automated_test_framework/
├── main.py               # Entry point
├── test_cases.py         # Hardware simulators + test definitions
├── report_generator.py   # Terminal output + file report writer
└── results/
└── report.txt        # Auto-generated on every run

## Test cases
| Parameter | Spec | Units |
|-----------|------|-------|
| Battery Voltage | 11.5 – 13.2 | V |
| Board Temperature | 0 – 85 | °C |
| Sensor Response Time | ≤ 10 | ms |
| Signal Strength | ≥ −80 | dBm |
| Firmware Version | Approved list | — |
| CPU Load | ≤ 80 | % |
| Current Draw | 0.5 – 4.0 | A |

## Skills demonstrated
- Python module design
- Hardware specification interpretation
- Automated pass/fail test logic
- Structured report generation
- Clean, documented, GitHub-ready code
