"""Synthetic educational calculations, not measured engineering results.

The thermal model is lumped, linear, constant-parameter, starts at ambient,
and excludes sensor dynamics. These functions do not authorize experiments.
"""
from __future__ import annotations

import math
from pathlib import PurePosixPath
from typing import Iterable, Mapping


def thermal_rise(power_w: float, resistance_k_per_w: float,
                 capacitance_j_per_k: float, time_s: float) -> float:
    """Return synthetic temperature rise in K for C*dT/dt = P - T/R.

    Parameters must be finite; power/time nonnegative; R/C positive.
    Initial temperature equals a constant ambient temperature.
    """
    values = (power_w, resistance_k_per_w, capacitance_j_per_k, time_s)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Parameters must be finite")
    if power_w < 0 or time_s < 0:
        raise ValueError("Power and time must be nonnegative")
    if resistance_k_per_w <= 0 or capacitance_j_per_k <= 0:
        raise ValueError("Resistance and capacitance must be positive")
    tau = resistance_k_per_w * capacitance_j_per_k
    limiting_rise = power_w * resistance_k_per_w
    if not math.isfinite(tau) or tau <= 0 or not math.isfinite(limiting_rise):
        raise ValueError("Parameters exceed the supported floating point range")
    return limiting_rise * (-math.expm1(-time_s / tau))


def factorial_effects(responses: Mapping[tuple[int, int], float]) -> dict[str, float]:
    """Arithmetic contrasts for one synthetic 2x2 table; no uncertainty inference."""
    expected = {(0, 0), (1, 0), (0, 1), (1, 1)}
    if set(responses) != expected:
        raise ValueError("Exactly one response is required for each binary combination")
    if not all(math.isfinite(x) for x in responses.values()):
        raise ValueError("Responses must be finite")
    low = responses[(1, 0)] - responses[(0, 0)]
    high = responses[(1, 1)] - responses[(0, 1)]
    return {"a_effect_at_b0": low, "a_effect_at_b1": high,
            "difference_of_effects": high - low}


def illustrative_payload(paths: Iterable[str], *, exclude_git: bool) -> set[str]:
    """Filter a synthetic list, not a secure filesystem traversal implementation."""
    ignored = {"__pycache__", ".pytest_cache"}
    if exclude_git:
        ignored.add(".git")
    return {name for name in paths if not ignored.intersection(PurePosixPath(name).parts)}
