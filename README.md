Psi4NWX (i.e. Psi for NWChemEx)
===============================

This repo provides a series of wrappers which allow Psi4 methods to be used as
plugins with NWChemEx. This repo does not provide either NWChemEx or Psi4.

Installation
============

This repo depends on:

- Psi4 ([obtain psi4](https://psicode.org/installs/latest))
- NWChemEx ([obtain NWX](https://github.com/NWChemEx-Project/NWChemEx))

It is assumed that you have installed both of these dependencies prior to
attempting to use this repo.

Installation Tips
-----------------

- Installing Psi4 requires the use of Anaconda. Anaconda has a propensity to 
  mess with system paths so it is strongly recommended that you:

  - Install Miniconda yourself (don't use the Psi4 installer option)
    - Miniconda can be obtained [here](https://docs.conda.io/en/latest/miniconda.html)
    - Miniconda is a stripped down version of Anaconda. I've had limited success
      installing Psi4 with full Anaconda on account of package conflicts
  - During the Miniconda install do not let the installer initialize conda (when
    prompted just say "no")
  - If you follow these tips you will need to run a command like:
    `eval "$(/path/2/where/you/installed/miniconda/bin/conda shell.bash hook)"` 
    in order to use conda (substituting bash for your Linux shell of choice)

Usage
-----

The most straigtforward usage of these plugins is to simply make sure NWX, Psi4,
and the psi4nwx Python module are all in your Python's path. If this is the
case you should simply be able to run any of the tests like: 
`cd tests && python3 test_scf.py`