""" clean up tool

The reST files are automatically generated using sphinx_tools.

However, there are known issus which require cleaning.

This code is intended at cleaning these issues until a neat 
solution is found.

:known problem:

- in ./deploy/openalea_deploy_binary_deps_ref.rst, the automodule 
includes the module binary_deps.py but there is only one
function inside this module. The automodule fails. To prevent this failure
switch the automodule to autofunction and remove all the fields below 
'.. autofunction::' that are not required anymore.
"""
import os
import sys
sys.path.append(os.path.abspath('../../misc'))
import sphinx_tools



filenames = ['deploy/openalea_deploy_binary_deps_ref.rst']
print 'Fixing the binary_deps_ref.rst case.'

for file in filenames:
    process = sphinx_tools.PostProcess(file)
    process.switch_automodule_to_autofunction()


print 'Try python setup.py build_sphinx now.'

