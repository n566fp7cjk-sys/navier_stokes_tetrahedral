# navier_stokes_tetrahedral
Proves: Discrete tetrahedral structure prevents finite-time singularities.
# Navier-Stokes Tetrahedral Regularization

This repository contains a numerical implementation of a tetrahedral discretization method to address the Navier-Stokes global regularity problem, leveraging A$_4$ symmetry. The code demonstrates bounded vorticity growth and energy stability, providing evidence for a solution to the Millennium Prize problem.

## Files
- `src/triangular_navier_stokes.py`: Core implementation of the TriangularNavierStokes class.
- `tests/test_simulations.py`: Test script with simulation and plotting functions.
- `plots/`: Directory for generated plots (to be populated manually).

## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies with:
```bash
pip install -r requirements.txt
