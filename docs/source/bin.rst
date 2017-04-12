bin Folder
==========

This folder contains scripts that aren't integral to the workings of
the package. It's very useful for holding the scripts that actually do
something useful using your package. For example, if your package is
'python-polygons' a bin script might be 'generate-triangle'. If your
package is a web application, a bin script might be 'run-dev-server'.

In the package setup.py file, it is possible to create a list of
scripts that are installed alongside your package. This allows the
scripts to be run from the command line.

.. code-block:: python

   CONFIG = {
   ...
   'scripts' = ['bin/script1', 'bin/script2'],
   ...
   }

A quirk about making a bin script: do not add a file extension, and do
not forget the shebang (#!/usr/bin/python3.6) at the start of the file.