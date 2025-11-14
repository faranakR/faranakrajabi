---
permalink: /research/
title: "Research"
---

I'm interested in **Computational Science and Engineering (CSE)** for applications in complex biological systems. My work focuses on developing **high-performance numerical methods** including level-set methods, scientific computing on adaptive meshes, and solvers for nonlinear ODEs and PDEs. I'm passionate about bridging scales from molecular dynamics to continuum models using modern computational techniques.

---

## 1. Multi-Scale High-Performance Computational Methods for Free Boundary Problems

### Multiscale Continuum Framework for Protein Aggregation

I'm developing a computational framework to predict long-term stability of high-concentration biotherapeutic formulations. This work addresses a critical challenge in pharmaceutical development: protein aggregation can limit drug shelf-life and cause adverse immune responses, but current models cannot bridge molecular-scale physics with shelf-life timescales.

**Key contributions:**
- **Level-set representation** of evolving protein aggregate boundaries on adaptive octree grids
- **Continuum transport equations** coupled with stochastic nucleation events
- **Robin boundary conditions** derived from Wertheim Thermodynamic Perturbation Theory to capture surface binding affinities
- **Parallel implementation** using the CASL library with demonstrated scaling to 1000+ cores
- Integration of long-range interactions (electrostatics via Poisson-Boltzmann, hydrodynamics via Stokes flow)

**Impact:** This framework enables pharmaceutical companies to predict stability from short-term measurements, accelerating drug development and reducing costs.

**Technologies:** C++, PETSc, MPI, p4est adaptive mesh refinement, level-set methods

**Status:** Ongoing dissertation research (2024-2026)

---

## 2. Advanced Computational Techniques for Optimal Control

### Stochastic Optimal Control for Neural Oscillators

Developed computational methods for solving stochastic Hamilton-Jacobi-Bellman (HJB) equations to design energy-efficient control strategies for noisy dynamical systems, with applications to deep brain stimulation for Parkinson's disease.

**Key contributions:**
- First-ever numerical framework for computing **globally optimal feedback control** in stochastic neural oscillator systems
- High-order WENO/ENO schemes with operator splitting for HJB equations
- Implicit parabolic solvers achieving **50× speedup** through adaptive mesh refinement
- Event-driven optimal controllers for desynchronizing pathological neural rhythms

**Publications:**
- F. Rajabi, F. Gibou, J. Moehlis, "Optimal Control for Stochastic Neural Oscillators," *Biological Cybernetics* (2025)
- M. Zimet, F. Rajabi, J. Moehlis, "Nearly Optimal Chaotic Desynchronization," *IEEE CDC* (2025)
- J. Moehlis, M. Zimet, F. Rajabi, "Magnitude-Constrained Optimal Desynchronization," *Frontiers in Network Physiology* (2025)

**Technologies:** C++, PETSc, adaptive mesh refinement, numerical optimal control

---

## 3. Machine Learning & AI for Science

### Neural Signal Processing & Data-Driven Control

Integrating physics-informed machine learning with traditional numerical methods for time-series prediction and control optimization in biological systems.

**Research directions:**
- **Neural signal processing** for extracting features from noisy neurophysiological data
- **Data-driven control** methods combining ML with optimal control theory
- **Neural operators for free boundary problems**: Investigating neural operator architectures (DeepONet, FNO) for accelerating level-set simulations of protein aggregation
- **Physics-informed neural networks (PINNs)** for learning closure models in multiscale simulations

**Technologies:** PyTorch, JAX, TensorFlow, hybrid ML-physics approaches

**Status:** Active exploration (2024-2025)

---

## 4. Open-Source Scientific Solver Development

### CASL-HJX: Hamilton-Jacobi Equation Solver

Developed and released **CASL-HJX**, the first comprehensive open-source framework for solving deterministic and stochastic Hamilton-Jacobi equations with guaranteed convergence to globally optimal solutions.

**Features:**
- High-order accurate schemes (WENO3, WENO5, ENO) on adaptive Cartesian grids
- Implicit time integration for parabolic Hamilton-Jacobi equations
- Ghost fluid methods for irregular boundary conditions
- Parallel implementation with MPI scaling to 1000+ cores
- Comprehensive documentation and example problems

**Publication:** F. Rajabi, J. Fingerman, A. Wang, J. Moehlis, F. Gibou, "CASL-HJX: A Comprehensive Guide to Solving Deterministic and Stochastic Hamilton-Jacobi Equations," *Computer Physics Communications* (2025)

**GitHub:** [UCSB-CASL/CASL-HJX](https://github.com/UCSB-CASL/CASL-HJX)

### GPU-Accelerated 4D HJB Solver (Work in Progress)

Currently developing a GPU-accelerated solver for 4D Hamilton-Jacobi-Bellman equations using CUDA and Kokkos for performance portability. This will enable real-time optimal control for high-dimensional dynamical systems.

**Technologies:** CUDA, Kokkos, C++, GPU computing

**Target applications:** High-dimensional stochastic control, robotics, real-time decision systems

---

## Research Philosophy

I believe in **open science** and making advanced computational methods accessible. All my research code is open-source with comprehensive documentation. I'm committed to:
- Developing **production-quality scientific software** that others can build upon
- **Bridging theory and practice** in numerical methods
- **Reproducible research** with version-controlled code and data
- **Interdisciplinary collaboration** across mathematics, engineering, and biology

---

## Collaborations & Funding

- **Industry:** Merck Research Labs (protein aggregation modeling)
- **Academic:** Prof. Frédéric Gibou (UCSB ME), Prof. Jeff Moehlis (UCSB ME)
- **Fellowships:** UCSB Graduate Research Fellowship, multiple departmental awards

---

*Want to collaborate?* I'm always excited to discuss research projects, open-source contributions, or consulting opportunities in computational science. [Reach out!](mailto:faranakrajabi@ucsb.edu)
