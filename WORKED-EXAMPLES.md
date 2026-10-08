---
package_version: "1.0.0"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Worked examples across engineering contexts

## Key takeaway

The examples demonstrate reasoning and arithmetic under declared assumptions not measured engineering achievements.

## Summary

Three illustrative examples connect observation, competing explanations, model, test, scoped insight and application. All numerical data and file sets here are synthetic. The included Python tests check calculations and counterexamples, not physical validation or a reconstruction of a real incident.

## Software manifest counterexample

**Question:** Why can a newly generated checksum manifest fail its own coverage check?

**Illustrative setup:** The same directory contains `README.md`, `.github/workflows/validate.yml`, `.git/HEAD` and `__pycache__/validate.pyc`. The generator excludes only the cache; the verifier excludes Git internals and cache. Checksums can be correct while the sets still differ.

```text
generator = {README.md, .github/workflows/validate.yml, .git/HEAD}
verifier  = {README.md, .github/workflows/validate.yml}
difference = {.git/HEAD}
```

**Competing explanations:** A file disappeared; a file changed; the payload policies differ. The minimal set comparison discriminates policy mismatch without disabling checksum verification.

**Mechanism:** One side treats tool-state files as publication content; the other does not. The coverage comparison fails because the policies disagree, not because any checksum algorithm is necessarily wrong.

**Check performed here:** A deterministic unit test constructs those sets and checks their difference. A second test verifies that an aligned policy retains real content, including `.github`, while excluding `.git`, Python caches and test caches. Additional tests verify that unexpected publication files still differ.

**Scoped insight:** Independently specified inclusion policies can disagree even when both operate correctly according to their own definitions. A shared payload definition is one design response. It is not a rule to ignore every hidden file.

**Limits:** This toy fixture does not evaluate a real repository’s entire release process, symlink policy, threat model or provenance. It illustrates the distinction and a safe software-level discriminating test.

## Thermal transient and steady state

**Question:** Does a cooler early reading mean better heat removal?

**Scientific basis:** [OpenStax heat capacity and heat transfer](references/openstax-2016-university-physics-heat-transfer.md) distinguishes energy storage from heat transfer. The model below is an authored approximation, not a textbook-provided test of a device.

**Assumptions:** One spatially uniform temperature; constant input power P; constant thermal capacitance C; one linear heat-transfer resistance R; fixed ambient temperature; initial temperature equal to ambient; no phase change, extra heat sources, nonlinear losses or sensor lag.

```text
C d(deltaT)/dt = P - deltaT/R

deltaT(t) = P R (1 - exp(-t/(R C)))

time constant = R C
limiting temperature rise = P R
```

P has units W, R K/W, C J/K and t seconds. R times C therefore has units seconds. These unit checks and limiting cases verify aspects of the calculation, not applicability to hardware.

| Synthetic alternative | P in W | R in K per W | C in J per K | Rise at 100 s in K | Limiting rise in K |
|---|---:|---:|---:|---:|---:|
| Baseline | 4 | 5 | 20 | 12.6424 | 20 |
| More heat storage | 4 | 5 | 40 | 7.8694 | 20 |
| Lower heat-transfer resistance | 4 | 2.5 | 20 | 8.6466 | 10 |

**Calculated result:** Greater heat storage lowers the early rise from 12.6424 K to 7.8694 K in this model, but leaves the limiting rise at 20 K. Lower resistance also lowers the early rise, and changes the limiting rise. No physical measurements were performed.

**Competing accounts:** A lower early trace can result from more storage, lower resistance, lower input or slower sensing. A full model and sufficiently informative independent measurements might distinguish them; one early reading cannot.

**Next test plan:** Compare independent input/ambient measurements, transient shape and a suitably assessed later regime, with sensor response checked. Any physical setup needs competent design and safety approval. Do not run equipment toward unsafe steady conditions merely to resolve the explanation.

**Insight record:** Within the assumed lumped linear model, early and limiting temperature answer different design questions. Additional thermal storage can benefit a short-burst objective without improving the continuous-operation temperature limit. This is a conditional model-derived insight, not an empirically validated device claim.

**Application:** Compare burst benefit, mass, long-run behavior and safeguards. The preference depends on the operating goal; “more storage is better” is not a universal engineering Principle.

## Process interaction counterexample

**Question:** Does increasing setting A always improve a response?

**Synthetic data:** A and B are abstract binary settings, not real operating instructions. Y is an invented response in arbitrary units.

| A | B | Y |
|---:|---:|---:|
| 0 | 0 | 10 |
| 1 | 0 | 14 |
| 0 | 1 | 18 |
| 1 | 1 | 16 |

At B=0, increasing A changes Y by +4. At B=1, it changes Y by -2. The difference of these effects is -6. Under 0/1 coding the table is represented exactly by `Y=10+4A+8B-6AB`.

**Insight:** In this constructed table, the effect of A depends on B. The recommendation “increase A” omits the condition that determines its sign.

**Evidence status:** The numbers are synthetic, with one value per cell and no independent replicates. They establish a logical/numerical example, not measurement variability, statistical significance, causality in a real process or a safe operating policy. An exact saturated fit is not validation.

**Next test plan:** In an actual authorized investigation, choose factor levels and controls from domain knowledge, plan independent experimental units and relevant uncertainty, account for nuisance factors and carryover, and assess the joint combinations where safe. [NIST experimental design guidance](references/nist-undated-experimental-design-handbook.md) supports the design distinction; it does not supply these invented data.

## Executable checks and boundaries

Run `python3 test_examples.py`. The code checks the manifest sets, thermal formula and interaction arithmetic, including invalid input and limiting cases. Passing establishes the stated computations only. The broader Practices have not been field-tested by these examples.
