# fibermodes

This is an updated and debugged version of the infamous fibermodes 0.2.0 package by CBrunet (original repo cbrunet/fibermodes). It contains an optical step-index fiber mode solver suitable for multi-layer circular core structures. This version contains bug fixes in the mode listings (includes even and odd modes now) and vector field definitions.

Example notebooks available in the repository under [examples/](https://github.com/Smart-Photonics-IPHT/Fiber-Mode-Solver/tree/master/examples)

The original API documentation is still available on http://fibermodes.rtfd.org/

This code can be used freely for non-profit scientific work. When using this code for any publication we'd be pleased if you could acknowledge: github.com/cbrunet; Behnam Pishnamazi and Mario Chemnitz from the Smart Photonics group, Leibniz Institute of Photonic Technologies Jena, Germany.

Installation
============

Requirements:

- Python >= 3.12
- numpy
- scipy
- packaging

For GUI (legacy, Python ≤ 3.5 only, not installed by default):

– PyQt4 (system package)
– pyqtgraph (`pip install .[gui]`)

To run unit tests:

 - pytest
 - coverage (for coverage tests)

 Install both with `pip install .[test]`.

This software is still under development. Therefore, it is recommended to
install it in a development environment, to be able to quickly pull newest changes
from the GitHub repository, and to be able to propose pull requests. However,
we also describe a *simple* installation, in case you only want to run the 
software, without hacking it.

Legacy GUI (optional)  
----------------------

The graphical user interface is considered legacy and is only supported on Python ≤ 3.5 with system‑provided PyQt4 and pyqtgraph. On newer Python versions, please use the library from the command line or in scripts/Jupyter notebooks without the GUI.


Installing the required environment
-----------------------------------

### For Linux

On **Ubuntu** / **Debian**, install the following packages:
`python3`, `python3-numpy`, `python3-scipy`, `python3-pip`.
The legacy GUI additionally needs `python3-pyqt4`, `python3-pyqtgraph` (Python ≤ 3.5 only, see below).

On **Arch**, the required packages are:
`python`, `python-numpy`, `python-scipy`, `python-pip`.
The legacy GUI additionally needs `python-pyqt4` (Python ≤ 3.5 only, see below).


### For Windows / Mac

I recommend to use a distribution that includes scientific Python.
Choose a distribution that includes Python 3.12 or higher. I recommend
using either
[WinPython](http://winpython.github.io/) or
[Anaconda](https://www.continuum.io/downloads).
Follow the installation instructions, and everything should work out-of-the-box.


*Simple* installation
---------------------

This is not the recommended way. You should consider *development* installation
instead. However, this is the simplest installation, as it does not require `git`.

1. Download the [ZIP archive from GitHub](https://github.com/Smart-Photonics-IPHT/Fiber-Mode-Solver).
2. Unzip it!
3. Open a terminal and change into the `fibermodes` directory.
4. Install the package with `pip install .`

Or directly from GitHub: `pip install "git+https://github.com/Smart-Photonics-IPHT/Fiber-Mode-Solver.git"`

If you need the legacy GUI (Python ≤ 3.5 only, see below), use `pip install .[gui]` instead.


Development installation
------------------------

The first step is to install `git`. For Linux, the package should be called `git`.
For Windows, it is a little more complicated. I recommend using
[Git for Windows](https://git-for-windows.github.io/). Follow the installation
instructions from their page.
You could also install [GitHub Desktop](https://desktop.github.com/) instead.

The second step is to create a GitHub account, if you do not already have one.
Then you should configure you machine with ssh keys, and configure your name
and email for git.

The third step is to fork and clone the
[fibermodes repository](https://github.com/Smart-Photonics-IPHT/Fiber-Mode-Solver).
I recommend forking it first, as it will allow you to commit your changes
on GitHub, and to suggest pull requests.

After cloning the repository and changing into the `fibermodes` directory, install in editable (development) mode:
`pip install -e .`
This links the source tree into your environment, so you do not need to reinstall after pulling new changes.

(The older `python setup.py develop` / `python setup.py install` invocations are no longer recommended:
modern `pip` versions do not guarantee `setuptools` is preinstalled in a fresh virtual environment, and
`pip install -e .` / `pip install .` work reliably without it.)


Running tests
-------------

To ensure you have all the required dependencies to run tests, you can
do, from the `fibermodes` directory: `pip install .[test]`.

Then, run `pytest`.

After installing the package, you can test the solver and see typical usage in the example notebook:
– Open `examples/fibermodes, code, new version.ipynb` in Jupyter (e.g. on your JupyterHub or local JupyterLab).  
– Run the notebook cells to verify that the installation works and to see example mode‑solving workflows.


Building documentation
----------------------

You need sphinx (`pip install sphinx`) and probably a few dependencies to be documented.

``
sphinx-build doc doc/_build/html
``

Documentation is generated under `doc/_build/html`.
(The `python setup.py build_sphinx` command required a separate setuptools
plugin and is no longer supported by current setuptools versions.)


