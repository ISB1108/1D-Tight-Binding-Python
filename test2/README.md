# Basic 1D Tight-Binding Models

This folder contains basic implementations of the one-dimensional tight-binding model.
The purpose of these exercises is to build physical intuition and numerical skills
before moving to more complex systems.

## Model

We consider a one-dimensional lattice with nearest-neighbor hopping.
The tight-binding dispersion relation is given by

E(k) = E₀ − 2t cos(ka),

where t is the hopping parameter, a is the lattice constant,
and E₀ is the onsite energy.

## Implemented Topics

### 1. Band Structure of a 1D Tight-Binding Model
We calculate and plot the energy dispersion E(k) within the first Brillouin zone.
This demonstrates how the hopping parameter determines the band shape and bandwidth.

### 2. Effect of Onsite Energy Shift
We study the effect of changing the onsite energy E₀.
Varying E₀ shifts the entire energy band rigidly without changing its bandwidth.
This shows that the onsite energy controls the band center,
while the hopping parameter controls the dispersion and bandwidth.

## Purpose of This Section

These basic models serve as a foundation for later studies,
including disorder, localization, and more advanced tight-binding extensions.





