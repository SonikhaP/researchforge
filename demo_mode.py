"""
Demo mode — returns realistic pre-built output so the UI can be shown
working without a live API key. Useful for recording the video and
testing the Streamlit UI while waiting for quota to activate.
"""

import time


DEMO_SOURCES = """
## Academic Papers (arXiv)

**1. Quantum Computing: An Overview**
*Nielsen, M., Chuang, I. — 2024-03-15*
Quantum computing exploits quantum mechanical phenomena such as superposition and entanglement to perform computation. Unlike classical bits which are either 0 or 1, qubits can exist in superposition of both states simultaneously, enabling quantum computers to process vast amounts of information in parallel.
[arXiv link](https://arxiv.org/abs/2403.00001)

---

**2. Recent Advances in Quantum Error Correction**
*Fowler, A., Martinis, J., Preskill, J. — 2024-01-20*
Quantum error correction is essential for practical quantum computing. Surface codes have emerged as the leading approach, offering high error thresholds and compatibility with 2D qubit architectures. Recent experiments demonstrate logical qubit lifetimes exceeding physical qubit coherence times.
[arXiv link](https://arxiv.org/abs/2401.00002)

---

**3. Quantum Advantage in Optimization Problems**
*Farhi, E., Goldstone, J. — 2023-11-10*
The Quantum Approximate Optimization Algorithm (QAOA) shows promise for combinatorial optimization. Benchmarking against classical algorithms reveals quantum advantage for certain problem classes when qubit counts exceed 1000.
[arXiv link](https://arxiv.org/abs/2311.00003)

## Web Results

**IBM Quantum Computing Overview**
IBM's quantum computers are now available through the cloud with up to 433 qubits. The IBM Quantum Network includes over 200 organizations worldwide working on quantum applications in finance, drug discovery, and logistics.
[link](https://www.ibm.com/quantum)

**Google Quantum AI**
Google achieved "quantum supremacy" in 2019 with its 53-qubit Sycamore processor. Current research focuses on error correction and scaling toward fault-tolerant quantum computation.
[link](https://quantumai.google)
"""

DEMO_FINDINGS = """
## Key Findings

1. **Qubits enable superposition** — Unlike classical bits, qubits can represent 0 and 1 simultaneously, enabling parallel computation across exponentially many states.

2. **Quantum entanglement is a core resource** — Entangled qubits allow correlations impossible classically, underpinning quantum speedups in algorithms like Shor's (factoring) and Grover's (search).

3. **Error correction is the critical bottleneck** — Current NISQ-era devices have error rates too high for large computations; surface codes offer the most practical path to fault tolerance.

4. **Quantum advantage is algorithm-specific** — Demonstrated speedups exist for factoring (exponential), unstructured search (quadratic), and simulation of quantum systems (exponential).

5. **Major platforms are cloud-accessible** — IBM, Google, and IonQ offer cloud quantum computing; IBM has reached 433 qubits as of 2024.

## Important Concepts & Definitions

- **Qubit**: Quantum bit; the basic unit of quantum information.
- **Superposition**: A qubit's ability to exist in a combination of 0 and 1 simultaneously.
- **Entanglement**: Quantum correlation between qubits where measurement of one instantly determines the other.
- **NISQ**: Noisy Intermediate-Scale Quantum — the current era of ~50–1000 noisy qubits.

## Conflicting Viewpoints

Some researchers argue quantum advantage claims are overstated and classical algorithms can match NISQ-era performance for practical problems. Google's 2019 "supremacy" claim was contested by IBM, who argued classical simulation was faster than reported.

## Gaps & Open Questions

- When will fault-tolerant quantum computers arrive at useful scale?
- Which industries will see real-world quantum advantage first?
"""

DEMO_CRITIQUE = """
## Reliability Assessment

**Overall reliability: Medium-High**

The field of quantum computing is well-established academically, with findings backed by peer-reviewed research from major institutions (MIT, Google, IBM). However, several caveats apply:

**Well-supported claims:**
- Qubits exploit superposition and entanglement — textbook physics, highly reliable.
- Surface codes as leading error correction approach — strong consensus across multiple research groups.
- IBM has 433-qubit systems — verified public information.

**Tentative claims (single/limited sources):**
- Specific quantum advantage thresholds (e.g., "1000 qubits for QAOA advantage") — evidence is limited and contested.
- Timeline claims for fault-tolerant computers — highly speculative.

**Flagged concerns:**
- "Quantum supremacy" (2019) is disputed — classical simulation improvements have since caught up for that specific benchmark.

**Suggested follow-up search:** "fault-tolerant quantum computing timeline 2024 2025 roadmap IBM Google"
"""

DEMO_SYNTHESIS = """
## Background

Quantum computing represents a paradigm shift in computation, leveraging the principles of quantum mechanics — superposition, entanglement, and interference — to process information in fundamentally different ways from classical computers. While a classical bit is either 0 or 1, a quantum bit (qubit) can exist in a superposition of both states simultaneously, and groups of qubits can be entangled to encode and manipulate exponentially more information.

## Current State of Knowledge

The field has made remarkable progress since the theoretical groundwork laid by physicists like Feynman and Deutsch in the 1980s. Today, quantum computers with hundreds of qubits are commercially available through cloud platforms from IBM, Google, and IonQ. Google's 2019 demonstration of "quantum supremacy" on a sampling task marked a milestone, though the claim remains contested as classical algorithms continue to improve.

The most well-established quantum algorithms offer provable speedups: Shor's algorithm for integer factorization (exponential speedup) and Grover's algorithm for database search (quadratic speedup). Quantum simulation of molecular systems is widely regarded as the most near-term practical application.

The central engineering challenge is **error correction**. Current devices operate in the "NISQ era" — Noisy Intermediate-Scale Quantum — where error rates limit circuit depth and useful computation. Surface codes, which encode one logical qubit across many physical qubits in a 2D grid, offer the most credible path to fault-tolerant quantum computing.

## Key Debates & Open Questions

The timeline to fault-tolerant, practically useful quantum computers remains deeply contested. Optimists point to exponential qubit scaling and improving error rates; skeptics note that the overhead of error correction means we may need millions of physical qubits per logical qubit. The question of which problems will first see *real-world* quantum advantage — beyond academic benchmarks — remains open.

## Practical Implications

Near-term applications likely include quantum chemistry (drug discovery, materials science), optimization (logistics, finance), and cryptography (both breaking and creating quantum-safe encryption). The cybersecurity implications are particularly urgent: RSA and elliptic-curve encryption could be broken by sufficiently powerful quantum computers, driving the development of post-quantum cryptography standards.
"""

DEMO_REPORT = """# Quantum Computing: From Qubits to Practical Applications

## Executive Summary

Quantum computing exploits quantum mechanical phenomena — superposition, entanglement, and interference — to solve certain problems exponentially faster than classical computers. While the field has achieved remarkable milestones (hundreds-of-qubit machines, first demonstrations of quantum advantage), practical fault-tolerant quantum computers remain years away. The most credible near-term impact will be in quantum chemistry, optimization, and cryptography.

## Research Overview

Quantum computing represents a paradigm shift in computation. Unlike classical bits (0 or 1), qubits can exist in superposition of both states simultaneously, and entangled groups of qubits encode exponentially more information. This enables algorithms like Shor's (exponential speedup for factoring) and Grover's (quadratic speedup for search).

**Current state:** IBM, Google, and IonQ offer cloud-accessible quantum computers with 50–433 qubits. Google's 2019 "quantum supremacy" demonstration was a milestone, though contested. The central bottleneck is error correction — current NISQ-era devices have error rates too high for deep computation. Surface codes are the leading path to fault tolerance, but require millions of physical qubits per logical qubit.

**Key debates:** The timeline to practically useful, fault-tolerant quantum computers is deeply contested — estimates range from 5 to 20+ years. Which applications will first show real-world advantage remains open.

**Practical implications:** Near-term impact likely in quantum chemistry (drug discovery), optimization (logistics, finance), and post-quantum cryptography. The cryptographic risk is urgent — RSA encryption could be vulnerable to future quantum attacks, driving adoption of quantum-safe standards.

## Evidence Reliability

**Medium-High.** Core physics (superposition, entanglement) is textbook and highly reliable. Hardware milestones (IBM 433 qubits, Google Sycamore) are verified. Timeline claims and specific quantum advantage thresholds are speculative and contested. The "quantum supremacy" claim (Google, 2019) remains disputed.

## Key Sources

1. Nielsen & Chuang — *Quantum Computing: An Overview* (arXiv, 2024) — [link](https://arxiv.org/abs/2403.00001)
2. Fowler, Martinis, Preskill — *Recent Advances in Quantum Error Correction* (arXiv, 2024) — [link](https://arxiv.org/abs/2401.00002)
3. IBM Quantum — [ibm.com/quantum](https://www.ibm.com/quantum)
4. Google Quantum AI — [quantumai.google](https://quantumai.google)

## Further Reading

- Search: "fault-tolerant quantum computing timeline 2025 roadmap"
- Search: "post-quantum cryptography NIST standards"
- Search: "quantum advantage drug discovery clinical trials"

---
*Generated by ResearchForge Multi-Agent System (Demo Mode)*
"""


def run_demo(query: str, progress_callback=None) -> dict:
    """Return realistic demo output without calling any API."""
    steps = [
        (1, "Searching arXiv and the web..."),
        (2, "Extracting key findings..."),
        (3, "Fact-checking and assessing reliability..."),
        (4, "Synthesizing into a coherent narrative..."),
        (5, "Writing the final report..."),
        (6, "Done!"),
    ]
    for step, label in steps:
        if progress_callback:
            progress_callback(step, label)
        time.sleep(1.2)

    return {
        "query": query,
        "sources": DEMO_SOURCES,
        "findings": DEMO_FINDINGS,
        "critique": DEMO_CRITIQUE,
        "synthesis": DEMO_SYNTHESIS,
        "report": DEMO_REPORT,
    }
