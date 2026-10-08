#!/usr/bin/env python3
"""Tests of synthetic examples, not empirical validation of a technical system."""
import math
import unittest
from example_calculations import thermal_rise, factorial_effects, illustrative_payload


class SyntheticExamples(unittest.TestCase):
    def test_thermal_initial_condition(self):
        self.assertEqual(thermal_rise(4, 5, 20, 0), 0)

    def test_thermal_values(self):
        self.assertAlmostEqual(thermal_rise(4, 5, 20, 100), 12.642411176571153)
        self.assertAlmostEqual(thermal_rise(4, 5, 40, 100), 7.8693868057473315)
        self.assertAlmostEqual(thermal_rise(4, 2.5, 20, 100), 8.646647167633873)

    def test_storage_changes_transient_not_limit(self):
        self.assertLess(thermal_rise(4, 5, 40, 100), thermal_rise(4, 5, 20, 100))
        self.assertAlmostEqual(thermal_rise(4, 5, 20, 20000), 20)
        self.assertAlmostEqual(thermal_rise(4, 5, 40, 20000), 20)

    def test_thermal_derivative_matches_energy_balance(self):
        p, r, c, t, h = 4.0, 5.0, 20.0, 100.0, 0.001
        derivative = (thermal_rise(p, r, c, t+h) - thermal_rise(p, r, c, t-h))/(2*h)
        self.assertAlmostEqual(c*derivative, p-thermal_rise(p, r, c, t)/r, places=7)

    def test_invalid_thermal_parameters(self):
        for values in [(4, 0, 20, 1), (4, 5, 0, 1), (-1, 5, 20, 1),
                       (4, 5, 20, -1), (4, 5, math.nan, 1),
                       (4, 1e300, 1e300, 1), (4, 1e-300, 1e-300, 1)]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                thermal_rise(*values)

    def test_factorial_interaction(self):
        result = factorial_effects({(0, 0): 10, (1, 0): 14, (0, 1): 18, (1, 1): 16})
        self.assertEqual(result, {"a_effect_at_b0": 4, "a_effect_at_b1": -2,
                                  "difference_of_effects": -6})

    def test_factorial_saturated_formula(self):
        values = {(0, 0): 10, (1, 0): 14, (0, 1): 18, (1, 1): 16}
        for (a, b), y in values.items():
            self.assertEqual(10 + 4*a + 8*b - 6*a*b, y)
        with self.assertRaises(ValueError):
            factorial_effects({(0, 0): 10})

    def test_manifest_mismatch_and_alignment(self):
        files = {"README.md", ".github/workflows/validate.yml", ".git/HEAD",
                 "__pycache__/validate.pyc", ".pytest_cache/state"}
        generator = illustrative_payload(files, exclude_git=False)
        verifier = illustrative_payload(files, exclude_git=True)
        self.assertEqual(generator-verifier, {".git/HEAD"})
        self.assertEqual(verifier, {"README.md", ".github/workflows/validate.yml"})
        self.assertEqual(illustrative_payload(files, exclude_git=True), verifier)

    def test_ordinary_new_files_remain_detectable(self):
        base = {"README.md", ".github/workflows/validate.yml"}
        changed = illustrative_payload(base | {"unexpected.txt", ".git/HEAD"}, exclude_git=True)
        self.assertEqual(changed-base, {"unexpected.txt"})


if __name__ == '__main__':
    unittest.main(verbosity=2)
