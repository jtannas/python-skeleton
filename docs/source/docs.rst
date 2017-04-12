Documentation Folder
====================

Folder structure
----------------

.. code-block:: none

    <docs>
    |-- _build\         Where the pretty documentation resides (once it is built)
    |-- _static\        Folder for if you want to use jinja templates
    |-- _templates\     Folder for if you want to use jinja templates
    |-- source\         Where the rst files (aka the actual documentation) are stored
    |-- conf.py         The configuration file for sphinx
    |-- index.rst       The root file of the actual documentation
    `-- Makefile        Tells sphinx what to do when the make command is issued

Sphinx Quickstart
-----------------

You can *start* a sphinx documentation folder using the sphinx-quickstart
command. It won't be useful yet, but it's a start.

.. code-block:: none

    $ cd <project-root>
    $ sphinx-quickstart
    Welcome to the Sphinx quickstart utility...

    > Root path for the documentation [.]: docs
    > Separate source and build directories (y/N) [n]:
    > Name prefix for templates and static dir [_]:
    > Project name: <project name>
    > Author name(s): <author name(s)>
    > Project version: 1.0
    > Project release [1.0]:
    > Project language [en]:
    > Source file suffix [.rst]: .rst
    > Name of your master document (without suffix) [index]: index
    > Do you want to use the epub builder (y/N) [n]: n
    > autodoc: automatically insert docstrings ... (y/N) [n]: y
    > doctest: automatically test code snippets ... (y/N) [n]: y
    > intersphinx: ... (y/N) [n]:
    > todo: ... (y/N) [n]:
    > coverage: ... (y/N) [n]:
    > pngmath: ... (y/N) [n]:
    > mathjax: ... (y/N) [n]: y
    > ifconfig: ... (y/N) [n]:
    > viewcode: include links to the source code ... (y/N) [n]: y
    > githubpages: ... (y/n) [n]:
    > Create Makefile? (Y/n) [y]: y
    > Create Windows command file? (Y/n) [y]: y

From there, I'd recommend going and adding a folder to keep the rst
files in, to keep them from blowing up the documentation root dir.

.. code-block:: bash

    $ cd <project-root>/docs
    $ mkdir source

Next, you have to edit the conf.py file so that sphinx-autodoc can
actually find your files. Go into conf.py and change this:

.. code-block:: python

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    #
    # import os
    # import sys
    # sys.path.insert(0, os.path.abspath('.'))

to this:

.. code-block:: python

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    #
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__name__), '..'))

This lets sphinx-autodoc know to look in the parent folder of conf.py
for the project. The ``os.path.dirname(__name__)`` piece ensures that
it always searches relative to conf.py, instead of the current working
directory.

While you're mucking around in conf.py, add
::

    'sphinx.ext.napoleon'

to the list of extensions. This extension lets sphinx parse different
styles of docstring (ie Google and NumPy) without rst formatting.
Google 'sphinx napoleon' to get a better example.



Sphinx-Autodoc
--------------

Part of the sphinx-quickstart was to include the sphinx-autodoc extension.
This extension allows sphinx to pull docstrings and other info from
python module docstrings via the rst command ``automodule``. For the
example module in the app package (<project root>/app/example.py):

::

    .. automodule:: app.example
        :members:
        :undoc-members:
        :show-inheritance:

Sphinx-Apidoc
-------------

Sphinx-autodoc does not magically include all the docstrings. To
generate the rst files that pull the docstrings (via the
``.. automodule:: <Module>`` directive), another tool is used:
sphinx-apidoc. This command looks through the project, then generates
rst files that contain the appropriate autodoc commands to pull the
docstrings. The general usage is: ``sphinx-apidoc <source dir>``, however
I use it a little differently so that I keep all the rst files in a single
folder - ``sphinx-apidoc -o <output dir> <source dir>``. My chosen output
directory is ``<project-root>/docs/source``, so that translates into:

.. code-block:: bash

   $ cd <project-root>/docs
   $ sphinx-apidoc -o ./source ..

Even after that, you still have to add the files to the index table of
contents (toctree).

::

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       source/<rst filename1, no extension>
       source/<rst filename2, no extension>