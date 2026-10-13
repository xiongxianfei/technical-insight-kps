"""Verify the pinned checker; shared failure-case regressions live in Core."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_validator_matches_pin(self):
        pin = json.loads((ROOT / 'upstream-lock.json').read_text())['validator']
        self.assertEqual(pin['sha256'], hashlib.sha256((ROOT / pin['path']).read_bytes()).hexdigest())


if __name__ == '__main__':
    unittest.main(verbosity=2)
