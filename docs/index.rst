.. ibd_dendrogram documentation master file, created by
   sphinx-quickstart on Tue Apr 18 20:46:28 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ibd_dendrogram's documentation!
==========================================

ibd_dendrogram is a python package designed to provide a consistent framework for generating dendrograms based on pairwise IBD sharing between individuals. This tool is designed to be used in conjunction with the output from DRIVE. This package works directly with the networks.txt and the allpairs.txt file produced by DRIVE.

Installation:
=============
This tool can be installed from `PYPI <https://pypi.org/project/ibd-dendrogram/>`_ using the following command

.. code:: bash
   
   pip install ibd-dendrogram

.. attention:: 

   This package currently only supports python>=3.10. It currently has type annotations that will not work in python<=3.9. 

.. toctree::
   :maxdepth: 1
   :caption: Package API:
   :Hidden:

   source/modules


