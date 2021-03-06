#!/usr/bin/env python

from setuptools import setup
import os, os.path, sys, distutils.util, glob

if distutils.util.get_platform() != "win32":
    print "Do not run this outside MSWindows."
    sys.exit(-1)

name="BisonFlex"
version="2.4.1-2.5.35"
description="Bison and Flex from the MSYS project"
author="The guys at www.mingw.org for the hard work, Daniel Barbeau Vasquez for the egg"
author_email="daniel.barbeau@sophia.inria.fr"
url="www.mingw.org"
license = "http://www.mingw.org/license"

#########
# UTILS #
#########
def unix_style_join(*args):
    l = len(args)
    if l == 1 : return args[0]
    
    ret = args[0]
    for i in range(1,l-1):
        ret += ("/" if args[i]!="" else "")+ args[i]
    
    if args[l-1] != "":
        ret += ("/" if args[l-2]!="" else "") + args[l-1]
        
    return ret
    
    
###############################################
# FINDING THE BISON and FLEX INSTALLATION DIR #
###############################################
BISFLEXDIR = os.getcwd()
if not os.path.exists(os.path.join(BISFLEXDIR, "bin", "flex.exe")):
    print "ERROR: could not find BISON-FLEX directory :", BISFLEXDIR 
    sys.exit(-1)
os.chdir(BISFLEXDIR)
BISFLEXDIR = BISFLEXDIR.replace("\\", "/") #because distutils expects / instead of \\

#####################################################################
# some voodoo to identify the files to copy and where to place them #
#####################################################################
raw_files = os.walk(BISFLEXDIR)
data_files = []
for i,j,k in raw_files:
    for f in k:
        #we want to reproduce the same hierarchy inside the egg.
        #as inside the BISFLEXDIR.
        rel_direc = os.path.relpath(i,BISFLEXDIR).replace("\\","/") 
        file_ = unix_style_join( rel_direc, f)        
        data_files.append( ("" if rel_direc == "." else rel_direc,[file_]) )

#############
# Let's go! #
#############
setup(name=name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      url=url,
      license=license,
      data_files = data_files,
      zip_safe = False,
      bin_dirs = { 'bin' : 'bin' },
      lib_dirs = { 'lib' : 'lib' },      
      inc_dirs = { 'include' : 'include' },
      setup_requires = ['openalea.deploy'],
      dependency_links = ['http://openalea.gforge.inria.fr/pi'],      
      )
      
egg = glob.glob("dist/*.egg")[0]
os.rename(egg, egg[:-4]+"-win32.egg")