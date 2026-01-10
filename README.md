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

For GUI (legacy, Python ≤ 3.5 only):  

– PyQt4 (system package)  
– pyqtgraph

To run unit tests:

 - nose
 - coverage (for coverage tests)

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
`python3`, `python3-numpy`, `python3-scipy`, `python3-pyqt4`, `python3-pyqtgraph`,
`python3-nose`, `python3-coverage`.

On **Arch**, the required packages are:
`python`, `python-numpy`, `python-scipy`, `python-pyqt4`, `python-nose`,
`python-coverage`, `python-pip`.


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
4. Run `python setup.py install`
   or install the package with `pip install .`

Or directly from GitHub: `pip install "git+https://github.com/Smart-Photonics-IPHT/Fiber-Mode-Solver.git"`

The command on line 4 may vary.
For instance, it should be `sudo python3 setup.py install` on Ubuntu / Debian.


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


Then you should install the software in `develop` mode. This is similar
to `install`, but it uses links instead of moving the files. Therefore, you
do not need to reinstall each time you pull changes from GitHub.
The command is: `python setup.py develop`. You may need to use `python3`
instead of `python` if you are on Ubuntu / Debian, and you may need to use
`sudo` to run this command.


Running tests
-------------

To ensure you have all the required dependencies to run tests, you can
do, from the `fibermodes` directory: `pip install .[test]`.

Then, you can either run `nosetests` or `python setup.py nosetests`.

After installing the package, you can test the solver and see typical usage in the example notebook:
– Open `examples/fibermodes, code, new version.ipynb` in Jupyter (e.g. on your JupyterHub or local JupyterLab).  
– Run the notebook cells to verify that the installation works and to see example mode‑solving workflows.


Building documentation
----------------------

You need sphinx (and probably a few dependencies to be documented).

``
python setup.py build_sphinx
``

Documentation is generated under `doc/_build/html`.


