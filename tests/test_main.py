import subprocess
import sys
import math
import pytest

# Helper to run CLI

def run_cli(args):
    cmd = [sys.executable, "main.py"] + args
    return subprocess.run(cmd, capture_output=True, text=True)


def parse_output(stdout):
    # Expected format: r=0.5, n=30, t=3.0091, p=0.0053658
    vals = {}
    for part in stdout.strip().split(','):
        k, v = part.strip().split('=')
        vals[k] = float(v)
    return vals


# ---- 正常系 ----

def test_cli_value_correctness():
    r = 0.5
    n = 30

    # Expected values
    df = n - 2
    t_expected = r * math.sqrt(df / (1 - r*r))
    # two‑tailed
    from scipy import stats
    p_expected = stats.t.sf(abs(t_expected), df) * 2

    result = run_cli(["--r", str(r), "--n", str(n)])
    assert result.returncode == 0

    vals = parse_output(result.stdout)

    assert abs(vals["t"] - t_expected) < 1e-4
    assert abs(vals["p"] - p_expected) < 1e-6


def test_cli_negative_r_value():
    r = -0.3
    n = 50
    df = n - 2

    t_expected = r * math.sqrt(df / (1 - r*r))
    from scipy import stats
    p_expected = stats.t.sf(abs(t_expected), df) * 2

    result = run_cli(["--r", str(r), "--n", str(n)])
    assert result.returncode == 0

    vals = parse_output(result.stdout)
    assert abs(vals["t"] - t_expected) < 1e-4
    assert abs(vals["p"] - p_expected) < 1e-6


# ---- 異常系 ----

def test_cli_invalid_r():
    # r > 1
    result = run_cli(["--r", "1.5", "--n", "30"])
    assert result.returncode != 0


def test_cli_invalid_n():
    # n too small
    result = run_cli(["--r", "0.1", "--n", "1"])
    assert result.returncode != 0
