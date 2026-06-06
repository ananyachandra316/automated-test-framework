"""
test_cases.py
-------------
Simulates hardware sensor readings and defines pass/fail test cases.
Each test function returns a dict with measured value, expected range,
and pass/fail status.
"""

import random
import time


# ---------------------------------------------------------------------------
# Hardware Simulators
# ---------------------------------------------------------------------------

def read_battery_voltage() -> float:
    return round(random.uniform(10.5, 13.8), 3)


def read_temperature() -> float:
    return round(random.uniform(18.0, 95.0), 2)


def read_sensor_response_time() -> float:
    return round(random.uniform(0.5, 25.0), 2)


def read_signal_strength() -> float:
    return round(random.uniform(-95.0, -30.0), 1)


def read_firmware_version() -> str:
    versions = ["1.4.2", "1.5.0", "2.0.1", "2.1.0", "0.9.8"]
    return random.choice(versions)


def read_cpu_load() -> float:
    return round(random.uniform(5.0, 98.0), 1)


def read_current_draw() -> float:
    return round(random.uniform(0.1, 5.5), 3)
#---------------------------------------------------------------------------
# Test Cases
# ---------------------------------------------------------------------------

def test_battery_voltage() -> dict:
    measured = read_battery_voltage()
    low, high = 11.5, 13.2
    passed = low <= measured <= high
    return {
        "name":     "Battery Voltage",
        "unit":     "V",
        "measured": measured,
        "expected": f"{low} – {high}",
        "passed":   passed,
        "note":     "Nominal 12 V system spec",
    }


def test_temperature() -> dict:
    measured = read_temperature()
    low, high = 0.0, 85.0
    passed = low <= measured <= high
    return {
        "name":     "Board Temperature",
        "unit":     "°C",
        "measured": measured,
        "expected": f"{low} – {high}",
        "passed":   passed,
        "note":     "Industrial operating temp range",
    }


def test_sensor_response_time() -> dict:
    measured = read_sensor_response_time()
    high = 10.0
    passed = measured <= high
    return {
        "name":     "Sensor Response Time",
        "unit":     "ms",
        "measured": measured,
        "expected": f"≤ {high}",
        "passed":   passed,
        "note":     "Real-time control loop requirement",
    }


def test_signal_strength() -> dict:
    measured = read_signal_strength()
    low = -80.0
    passed = measured >= low
    return {
        "name":     "Signal Strength",
        "unit":     "dBm",
        "measured": measured,
        "expected": f"≥ {low}",
        "passed":   passed,
        "note":     "Wireless link quality threshold",
    }


def test_firmware_version() -> dict:
    measured = read_firmware_version()
    approved = {"1.5.0", "2.0.1", "2.1.0"}
    passed = measured in approved
    return {
        "name":     "Firmware Version",
        "unit":     "",
        "measured": measured,
        "expected": ", ".join(sorted(approved)),
        "passed":   passed,
        "note":     "Approved production firmware list",
    }


def test_cpu_load() -> dict:
    measured = read_cpu_load()
    high = 80.0
    passed = measured <= high
    return {
        "name":     "CPU Load",
        "unit":     "%",
        "measured": measured,
        "expected": f"≤ {high}",
        "passed":   passed,
        "note":     "Real-time task headroom requirement",
    }


def test_current_draw() -> dict:
    measured = read_current_draw()
    low, high = 0.5, 4.0
    passed = low <= measured <= high
    return {
        "name":     "Current Draw",
        "unit":     "A",
        "measured": measured,
        "expected": f"{low} – {high}",
        "passed":   passed,
        "note":     "Power supply protection threshold",
    }


# ---------------------------------------------------------------------------
# Test Registry
# ---------------------------------------------------------------------------

ALL_TESTS = [
    test_battery_voltage,
    test_temperature,
    test_sensor_response_time,
    test_signal_strength,
    test_firmware_version,
    test_cpu_load,
    test_current_draw,
]


def run_all_tests(delay: float = 0.2) -> list[dict]:
    results = []
    for test_fn in ALL_TESTS:
        result = test_fn()
        time.sleep(delay)
        results.append(result)
    return results
