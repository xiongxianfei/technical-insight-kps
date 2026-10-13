#!/usr/bin/env python3
"""Method source declarations and synthetic arithmetic; not domain-effectiveness tests."""
from pathlib import Path
import importlib.util
import math
import re
import sys
import unittest
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('transition_validator', ROOT/'validate.py')
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)

def normalize(value,lower,upper,higher=True):
    if value is None:return None
    if not all(math.isfinite(x) for x in (value,lower,upper)) or upper<=lower:
        raise ValueError('Finite values and increasing bounds required')
    return (value-lower)/(upper-lower) if higher else (upper-value)/(upper-lower)
def area(values):
    if len(values)<3 or any(x<0 or not math.isfinite(x) for x in values):raise ValueError('Positive radial domain required')
    return .5*math.sin(2*math.pi/len(values))*sum(x*values[(i+1)%len(values)] for i,x in enumerate(values))
class MethodTests(unittest.TestCase):
    def test_03_named_basis_and_local_content(self):
        for p in (ROOT/'methods').glob('*.md'):
            d=v.parse(p);self.assertEqual(d.meta.get('method_origin'),'established')
            self.assertTrue(d.meta.get('references'))
            for h in ('Established basis','Inputs and prerequisites','Rationale','Procedure','Worked example','Working template','Output and validation','Limits and optional tools'):
                self.assertTrue(v.meaningful(v.section(d,re.escape(h))),str(p)+': '+h)
    def test_08_radar_normalization(self):
        self.assertAlmostEqual(normalize(20,10,50,False),.75)
        self.assertAlmostEqual(normalize(35,10,50,False),.375)
        self.assertAlmostEqual(normalize(.92,.8,1),.6)
    def test_09_missing_is_not_zero(self):self.assertIsNone(normalize(None,0,100))
    def test_10_bad_bounds_rejected(self):
        with self.assertRaises(ValueError):normalize(1,2,2)
    def test_11_out_of_range_not_silently_clipped(self):self.assertEqual(normalize(120,0,100),1.2)
    def test_12_radar_area_depends_on_order(self):
        self.assertAlmostEqual(area([1,1,.2,.2]),.72)
        self.assertAlmostEqual(area([1,.2,1,.2]),.4)
    def test_13_weighted_ranking_reversal(self):
        a=[.8,.4];b=[.5,.8]
        dot=lambda x,w:sum(t*s for t,s in zip(x,w))
        self.assertAlmostEqual(dot(a,[.6,.4]),.64)
        self.assertGreater(dot(a,[.6,.4]),dot(b,[.6,.4]))
        self.assertLess(dot(a,[.4,.6]),dot(b,[.4,.6]))
    def test_14_factorial_difference_of_effects(self):self.assertEqual((13-15)-(14-10),-6)
    def test_15_uncertainty_and_pareto_arithmetic(self):
        self.assertAlmostEqual(math.hypot(.3,.4),.5)
        self.assertAlmostEqual((40+25)/sum([40,25,20,15]),.65)
if __name__=='__main__':unittest.main(verbosity=2)
