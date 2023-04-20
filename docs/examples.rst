Example Usage example
=====================
ibd-dendrogramm was designed to be an to use package that has a simplistic interface. There are three main functions that the user can call to use the package. These steps listed below:

1. make_distance_matrix

.. code-block:: python

    grids, distance_matrix = make_distance_matrix(pairs_df, cM_threshold, distance_function)