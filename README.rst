====================================================
ACTUALLY READ ME
====================================================

This is a skeleton for Python Projects. Read it or be forever lost.

Tools Summary
*************
:IDE: Cloud9
:Language: Python3.6
:Style: PEP8 + <project root>/setup.cfg[style]
:Style Formatter: YAPF
:Style Checker: PyLint
:Testing: Pytest
:Tests Folder: <project root>/tests
:Test Naming: test_<name>.py
:Documentation: Sphinx RST, docutils
:Docs Folder: <project root>/docs
:Virtual Environment Manager: virtualenvwrapper
:Virtual Environment Name: venv
:Version Control: Git
:Central Repository: GitHub



IDE Notes
************
Here are the recommended project settings in the Cloud9 workspace (aka ACE code editor):
 - Soft Tabs = True; *This converts tab presses into spaces*
 - Tab Size = 4; *Python standard is 4 spaces indent*
 - On Save, Strip Whitespace = True; *This strips whitespace from the end of lines.*
 - Python Version = Python3; *This sets the ACE code checking to Python3*
 - Python Format on Save = True;
 - Python formatter = ``yapf -i "$file"``; *This command is run on save to format the code in place.*

Language Notes
**************
For new Python projects, Python3 is the version of choice. Some people are upset about this because of <reasons>. I empathize, but that's not going to keep me tied to old versions.

Setting Python3 as the default in your system can cause issues because it is not backwards compatible with Python2. The workaround is to append an alias to .bash_aliases using:
    ``echo 'alias python=python3.6' >> ~/.bash_aliases``

If there is no .bash_aliases file, append it to ``.bashrc`` instead.

Also, prepend your .py files with a version she-bang just to be double sure. This tells python which version is needed to run the code.
    ``#!/usr/bin/python3.6``

Style Notes
***********
The style being used is PEP8 (https://www.python.org/dev/peps/pep-0008/) because that's the usual Python standard. Styling by hand is inconsistent and slow, so we use a Style Formatter to do it for us. YAPF (https://github.com/google/yapf) is the formatter of choice. Options for YAPF can be found in the the setup.cfg file in the project root, under the [style] section. Make sure to install YAPF **outside of the virtual environment** or else Cloud9 will yell at you when you try to format on save.

It is recommended to set up automatic format-code-on-save. See the Cloud9 notes on how to do this in the Cloud9 IDE. For other IDEs, you're on your own.

Pylint is used to check the code for compliance. This is because YAPF will format what is there, but won't tell you what you're missing or where you've made bad design choices.

Testing Notes
*************
There's a couple different testing frameworks for Python, each with their own strengths and weaknesses. Pytest (https://docs.pytest.org/en/latest/) is the current favored one for new Python projects, so that's what we're going with.

