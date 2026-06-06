"""
reporter_generator.py
----------------------
Handles 2 ouput channels:
1. Terminal - color coded table printed o stdout
2. File - text report (saved : results/report.txt)
----------------------------------------------------
"""
import os
from datetime import datetime

# ANSI colour codes for terminal output
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

COL_WIDTHS = {
    "name":     24,
    "measured": 14,
    "expected": 22,
    "status":    6,
    "note":     36,
}
DIVIDER = "-" * (sum(COL_WIDTHS.values()) + len(COL_WIDTHS) * 3 - 1)


def _status_str(passed: bool, colour: bool = True) -> str:
    if colour:
        return f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
    return "PASS" if passed else "FAIL"


def _fmt_measured(result: dict) -> str:
    unit = result.get("unit", "")
    val  = result["measured"]
    return f"{val} {unit}".strip()


# ---------------------------------------------------------------------------
# Terminal output
# ---------------------------------------------------------------------------

def print_results(results: list[dict], run_ts: datetime) -> None:

    total  = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = total - passed
    rate   = (passed / total * 100) if total else 0.0

    print()
    print(f"{BOLD}{CYAN}{'=' * len(DIVIDER)}{RESET}")
    print(f"{BOLD}{CYAN}  PYTHON AUTOMATED TEST FRAMEWORK — Hardware Validation Suite{RESET}")
    print(f"{BOLD}{CYAN}{'=' * len(DIVIDER)}{RESET}")
    print(f"  Run timestamp : {run_ts.strftime('%Y-%m-%d  %H:%M:%S')}")
    print(f"  Total tests   : {total}")
    print(f"  Passed        : {GREEN}{passed}{RESET}")
    print(f"  Failed        : {RED}{failed}{RESET}")
    print(f"  Pass rate     : {YELLOW}{rate:.1f}%{RESET}")
    print()

    header = (
        f"{'TEST NAME':<{COL_WIDTHS['name']}} "
        f"{'MEASURED':<{COL_WIDTHS['measured']}} "
        f"{'EXPECTED':<{COL_WIDTHS['expected']}} "
        f"{'STATUS':<{COL_WIDTHS['status']}} "
        f"{'NOTE':<{COL_WIDTHS['note']}}"
    )
    print(f"{BOLD}{header}{RESET}")
    print(DIVIDER)

    for r in results:
        status = _status_str(r["passed"], colour=True)
        raw_status = "PASS" if r["passed"] else "FAIL"
        pad = COL_WIDTHS["status"] - len(raw_status)

        row = (
            f"{r['name']:<{COL_WIDTHS['name']}} "
            f"{_fmt_measured(r):<{COL_WIDTHS['measured']}} "
            f"{r['expected']:<{COL_WIDTHS['expected']}} "
            f"{status}{' ' * pad} "
            f"{r.get('note', ''):<{COL_WIDTHS['note']}}"
        )
        print(row)

    print(DIVIDER)

    overall = f"{GREEN}ALL TESTS PASSED{RESET}" if failed == 0 else f"{RED}{failed} TEST(S) FAILED{RESET}"
    print(f"\n  Overall result : {overall}\n")


# ---------------------------------------------------------------------------
# File report
# ---------------------------------------------------------------------------

REPORT_DIR  = os.path.join(os.path.dirname(__file__), "results")
REPORT_PATH = os.path.join(REPORT_DIR, "report.txt")


def save_report(results: list[dict], run_ts: datetime) -> str:

    os.makedirs(REPORT_DIR, exist_ok=True)

    total  = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = total - passed
    rate   = (passed / total * 100) if total else 0.0

    divider = "=" * 80
    thin    = "-" * 80

    lines = [
        divider,
        "  PYTHON AUTOMATED TEST FRAMEWORK — Hardware Validation Suite",
        f"  Report generated : {run_ts.strftime('%Y-%m-%d %H:%M:%S')}",
        divider,
        "",
        "SUMMARY",
        thin,
        f"  Total tests  : {total}",
        f"  Passed       : {passed}",
        f"  Failed       : {failed}",
        f"  Pass rate    : {rate:.1f}%",
        "",
        "DETAILED RESULTS",
        thin,
    ]

    for idx, r in enumerate(results, start=1):
        status   = _status_str(r["passed"], colour=False)
        measured = _fmt_measured(r)
        lines += [
            f"[{idx:02d}] {r['name']}",
            f"     Measured : {measured}",
            f"     Expected : {r['expected']}",
            f"     Status   : {status}",
            f"     Note     : {r.get('note', 'N/A')}",
            "",
        ]

    lines += [
        thin,
        f"  Overall : {'ALL TESTS PASSED' if failed == 0 else f'{failed} TEST(S) FAILED'}",
        divider,
        "",
        "END OF REPORT",
    ]

    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    return os.path.abspath(REPORT_PATH)
