#!/usr/bin/env python3
"""Release-specific structure and synthetic arithmetic; not domain-effectiveness tests."""
from pathlib import Path
import importlib.util
import json
import math
import re
import sys
import unittest
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('transition_validator', ROOT/'validate.py')
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)
POLICY=json.loads((ROOT/'transition.json').read_text())

def normalize(value,lower,upper,higher=True):
    if value is None:return None
    if not all(math.isfinite(x) for x in (value,lower,upper)) or upper<=lower:
        raise ValueError('Finite values and increasing bounds required')
    return (value-lower)/(upper-lower) if higher else (upper-value)/(upper-lower)
def area(values):
    if len(values)<3 or any(x<0 or not math.isfinite(x) for x in values):raise ValueError('Positive radial domain required')
    return .5*math.sin(2*math.pi/len(values))*sum(x*values[(i+1)%len(values)] for i,x in enumerate(values))
class TransitionTests(unittest.TestCase):
    def test_01_all_generic_methods_retired(self):
        self.assertEqual(len(POLICY['retired_methods']),20)
        for rec in POLICY['retired_methods'].values():self.assertFalse((ROOT/rec['path']).exists(),rec['path'])
    def test_02_exact_established_library(self):
        self.assertEqual({p.stem for p in (ROOT/'methods').glob('*.md')},set(POLICY['established_methods']))
        self.assertEqual(len(POLICY['established_methods']),22)
    def test_03_named_basis_and_local_content(self):
        for p in (ROOT/'methods').glob('*.md'):
            d=v.parse(p);self.assertEqual(d.meta.get('method_origin'),'established')
            self.assertTrue(d.meta.get('references'))
            for h in ('Established basis','Inputs and prerequisites','Rationale','Procedure','Worked example','Working template','Output and validation','Limits and optional tools'):
                self.assertTrue(v.meaningful(v.section(d,re.escape(h))),str(p)+': '+h)
    def test_04_every_retired_operation_has_a_real_home(self):
        for r in POLICY['retired_methods'].values():
            d=v.parse(ROOT/r['practice']);self.assertIn(r['stage'],[x[1] for x in d.headings])
            self.assertGreater(len(r['responsibility']),15)
    def test_05_no_retired_method_id_in_live_metadata(self):
        old={'ti:me:'+k for k in POLICY['retired_methods']}
        for p in ROOT.rglob('*.md'):
            if '.github' in p.parts:continue
            d=v.parse(p)
            for k in v.RELATIONS:self.assertFalse(old.intersection(d.meta.get(k,[])),str(p))
    def test_06_all_new_methods_are_used_by_practices(self):
        used=set()
        for p in (ROOT/'practices').glob('*.md'):used.update(v.parse(p).meta.get('uses_methods',[]))
        self.assertTrue({'ti:me:'+s for s in POLICY['established_methods']}<=used)
    def test_07_five_whys_and_5w2h_distinguished(self):
        a=(ROOT/'methods/5w2h.md').read_text();b=(ROOT/'methods/five-whys.md').read_text()
        self.assertIn('How much',a);self.assertIn('Who',a);self.assertIn('unknown',a)
        self.assertIn('fewer or more than five',b);self.assertIn('causal',b)
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
    def test_16_intelligence_scope_retained(self):
        for rel in ('concepts/technology-intelligence.md','concepts/technology-readiness.md','models/readiness-evidence-model.md','principles/readiness-evidence-is-context-dependent.md','INTEGRATED-EXAMPLE.md'):
            self.assertTrue((ROOT/rel).is_file(),rel)
if __name__=='__main__':unittest.main(verbosity=2)
