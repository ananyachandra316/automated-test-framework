"""
main.py
-------
Entry point for the Python Automated Test Framework.

Usage:
    python3 main.py
"""

from datetime import datetime

from test_cases import run_all_tests
from report_generator import print_results, save_report


def main() -> None:
    run_ts = datetime.now()

    print("\n  Initialising hardware validation suite …")
    print("  Acquiring sensor readings (simulated I/O delay) …")

    results = run_all_tests(delay=0.15)
    print_results(results, run_ts)
    path = save_report(results, run_ts)

    print(f"  Report saved → {path}\n")


if __name__ == "__main__":
    main()
