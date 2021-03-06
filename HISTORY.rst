.. :changelog:

OpenAlea.Deploy 2.0.0
---------------------

- add VirtualEnv and Conda compatibility and detection

OpenAlea.Deploy 0.9.0
---------------------

- add bdist_rpm  options

OpenAlea.Deploy 0.8.0
---------------------

**Revision 2194**

- add add_plat_name option in setuptools
- Add Sphinx documentation in ./doc and update the setup.cfg accordingly

OpenAlea.Deploy 0.7.0
---------------------

**Revision xxxx**

- add pylint option in setuptools
- add sphinx_upload option in setuptools
- add DYLD_LIBRARY_PATH to deploy config file
- update documentation
	- Fixes docstrings to make them compatible with sphinx, or have a nicer output
	- fixes indentation issues in binary_deps and gforge_utils
	- fixes coding conventions
	- a few typos
	- remove some warnings
	- Fixed bad indentation

OpenAlea.Deploy 0.6.2
---------------------

**Revision 1575**

- add clean command to incorporate scons into setup.py
- Port to Mac
- Fix documentation (docstrings) to remove warnings in epydoc:
	http://openalea.gforge.inria.fr/doc/deploy-0.6.0/
- Fix tests
- Upgrade setuptools to 0.6c9
- Fix PATH problem on Windows to take into account OpenAlea libraries.
- Version are now compared with pkg_resources

OpenAlea.Deploy 0.4.12
----------------------
- Fix PATH problem on Windows to take into account OpenAlea libraries.

OpenAlea.Deploy 0.4.11
----------------------
- Fix version comparison by using parse_version rather than lexical cmp.

OpenAlea.Deploy 0.4.9
---------------------
- add binary dependency declaration in binray_deps.py

OpenAlea.Deploy 0.4.8
---------------------
- Fix upload for big files

OpenAlea.Deploy 0.4.7
---------------------
- Add remove_package and remove_release in gforge.py

OpenAlea.Deploy 0.4.6
---------------------
- Add get_metainfo function

OpenAlea.Deploy 0.4.5
---------------------
- Fix alea_clean Bug (remove all site-package)

OpenAlea.Deploy 0.4.4
---------------------
- Fix bug with os.environ['PATH'] under windows

OpenAlea.Deploy 0.4.3
---------------------
- Fix bug with namespace creation and complex __init__.py

OpenAlea.Deploy 0.4.2
---------------------
- Add <alea_upload> command (GForge upload)
- Add gforge module (SOAP communication)
- Fix dyn-lib bug with virtual env and with relative path
- Add option to alea_config to print dyn-lib

OpenAlea.Deploy 0.4.1
---------------------
- Fix bug with <develop> command and namespaces

OpenAlea.Deploy 0.4.0
---------------------
- Improve <develop> command : manage namespace and environment variables
- Reinstall shared libraries if they are missing (but not egm)
- Add shell command : alea_clean, alea_config and alea_update
- Based on setuptools-0.6c8

OpenAlea.Deploy 0.3.8
---------------------
- Adapt develop command for lib_dir and bin_dir

OpenAlea.Deploy 0.3.7
---------------------
- Simplify the warning message for environment variable on Linux

OpenAlea.Deploy 0.3.6
---------------------
- add get_recommended_pkg functions

OpenAlea.Deploy 0.3.5
---------------------
- add alea_clean and alea_update_all scripts

OpenAlea.Deploy 0.3.4a
----------------------
- Fix platform detection for darwin

OpenAlea.Deploy 0.3.3
---------------------
- Execute build_ext before build_py

OpenAlea.Deploy 0.3.2
---------------------
- Manage a list of web repository

OpenAlea.Deploy 0.3
-------------------
- Manage a directory of shared lib

