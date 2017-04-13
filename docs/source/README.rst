ACTUALLY READ ME
====================================================

This is a skeleton for Python Projects. Read the ReadMe or be forever
lost. It contains all you need to know to get up and running. There is
documentation for each workspace folder for more detailed stuff.

Tools Summary
-------------

.. csv-table:: Tools Summary
    :header: "Need", "Solution"
    :widths: 40, 40

    "IDE", "Cloud9 (Ubuntu 14.04, ACE code editor)"
    "Language", "Python3.6.1"
    "Virtual Environment Manager", "python3.6 venv"
    "Virtual Environment Location", "<project root>/venv"
    "Version Control", "Git"
    "Central Repository", "GitHub"
    "Style", "PEP8 + <project root>/setup.cfg[style]"
    "Style Formatter", "YAPF"
    "Style Checker", "PyLint3"
    "Testing - Unit", "Pytest",
    "Testing - Compatibility", "tox"
    "Tests Folder", "<project root>/tests"
    "Test Naming", "test_<name>.py"
    "Type Checking", "mypy"
    "Scripts Folder", "<project root>/bin"
    "Instance Folder", "<project root>/instance"
    "Documentation", "Sphinx RST, sphinx-apidoc"
    "Docs Folder", "<project root>/docs"


Cloud9 Notes
------------

Here are the recommended project settings in the Cloud9 workspace (aka
ACE code editor):

- Soft Tabs = True; *This converts tab presses into spaces*
- Tab Size = 4; *Python standard is 4 spaces indent*
- On Save, Strip Whitespace = True; *This strips whitespace from the end of lines.*
- Python Version = Python3; *This sets the ACE code checking to Python3*
- Python Format on Save = True;
- Python formatter = ``yapf -i "$file"``; *This command is run on save to format the code in place.*

To get the latest version of Python3.6 (instead of 3.6.0), use:

.. code-block:: bash

    $ sudo add-apt-repository ppa:jonathonf/python-3.6
    $ sudo apt-get update
    $ sudo apt-get install python3.6


Then install yapf with sudo so that ACE can use it.

.. code-block:: bash

    $ sudo pip install yapf


To create a virtual environment, we're using the venv command packaged
with Python 3.6. Cloud9's Ubuntu 14.0 doesn't like this, so the process
is a bit convoluted. Here's some background: http://askubuntu.com/a/488530

.. code-block:: bash

    $ cd ~/workspace
    $ python3.6 -m venv --without-pip ./venv
    $ source venv/bin/activate
    $ curl https://bootstrap.pypa.io/get-pip.py | python
    $ deactivate


To verify the installation of Python in the virtual environment.

.. code-block:: bash

    $ source venv/bin/activate
    $ python --version
    $ pip --version


Language Notes
--------------

For new Python projects, Python3 is the version of choice. Some people are
upset about Python3 because of <reasons>. I empathize, but that's not
going to keep me tied to old versions.

Prepend your .py files with a version she-bang. ``#!/usr/bin/python3.6``

Style Notes
-----------

The style being used is PEP8 (https://www.python.org/dev/peps/pep-0008/)
because that's the usual Python standard. Styling by hand is inconsistent
and slow, so we use a Style Formatter to do it for us. YAPF
(https://github.com/google/yapf) is the formatter of choice. Options for
YAPF can be found in the the setup.cfg file in the project root, under the
[style] section. Make sure to install YAPF **outside of the virtual
environment** or else Cloud9 will yell at you when you try to format on save.

It is recommended to set up automatic format-code-on-save. See the Cloud9
notes on how to do this in the Cloud9 IDE. For other IDEs, you're on your own.

Pylint3 is used to check the code for compliance. This is because YAPF will
format what is there, but won't tell you what you're missing or where
you've made bad design choices. If pylint gives you a really bad score on
your code, don't just blame Pylint and move on. Correct the errors. If
they really aren't errors, use Pylint disable flags to disable the relevant
error code on the relevant lines, re-enabling the codes when appropriate.
Here are the error codes: http://pylint-messages.wikidot.com/all-codes

Testing Notes
-------------

There's a couple different testing frameworks for Python, each with their
own strengths and weaknesses. Pytest (https://docs.pytest.org/en/latest/)
is the current favored one for new Python projects, so that's what we're
going with. It is configured in setup.cfg, under the [tool:pytest]
section.

One of configuration options is to enable doctest, where docstrings can
be used for testing. This is my preferred option for simple~ish
functions, since it packages everything together and gives examples to
the reader.

Another testing package, tox, is used for checking compatibility with
different versions of python. The gist of tox is it creates virtual
environments for multiple versions of python and tries to install the
package in them and to run the unit testing package (ie. pytest). It
reports back whatever failures it had, so you know if there are any
compatibility issues in your project.

Documentation
-------------

The preferred way of documenting Python projects is a mix of .rst files
and docstrings embedded in python modules. The .rst files handle how
everything is organized and the expository writing (eg. how-to-guides),
while the docstrings handle the nitty-gritty of 'this function does X'.

There is a great package called sphinx that handles the task of
turning the rst files into a sensible and linked documentation.
Unfortunately, it's own documentation is terribly arcane and difficult
to understand. Here's my crack at a better explanation:

**What is rst?**

rst files are a type of 'markup' text file for human writing. What this
means is that you write the text pretty much normally, but with a few
extra symbols to add formatting.

**What does Sphinx do?**

Sphinx is a code documentation generator. It takes a bunch of rst files,
uses a few extra rst formatting symbols to link them together, then
converts them into a prettier format (eg. a pdf or a website).

**Where do the Python docstrings come in?**

Sphinx has an extension called sphinx-autodoc that lets it include
docstrings from your python module in the pretty documentation that it
makes.

**Great! What's the catch?**

Sphinx-autodoc does not magically include all the docstrings. To
generate the rst files that pull the docstrings, another tool is used:
sphinx-apidoc. This command looks through the projsect, then generates
rst files that contain the appropriate autodoc commands to pull the
docstrings.

**Anything more?**

Lots. Getting sphinx running is actually a very gory process that I
wouldn't wish on any new programmer. The instructions are too long to
include here, so see :doc:`docs` rst for the full rundown.

