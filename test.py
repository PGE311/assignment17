#!/usr/bin/env python

import unittest
import nbconvert
import numpy as np


with open("assignment17.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment17.py", "w") as f:
    f.write(python_file)

from assignment17 import compute_pressures


class TestSolution(unittest.TestCase):

    def test_compute_pressues(self):
        ans = compute_pressures(1.4) 
        np.testing.assert_array_almost_equal(ans, np.array([12.35681777, 12.62063551, 12.87238803, 13.10984212, 13.33281254,
                                                            13.54222519, 13.73950065, 13.92617949, 14.10371737, 14.27339174,
                                                            14.43627631, 14.59325269, 14.74503911, 14.89222393, 15.0352974 ,
                                                            15.1746785 , 15.3107359 , 15.44380338, 15.57419042, 15.70218898,
                                                            15.82807742, 15.95212247, 16.07457974, 16.19569358, 16.31569642,
                                                            16.434808  , 16.5532347 , 16.67116889, 16.78878864, 16.90625759,
                                                            17.02372499, 17.1413261 , 17.2591826 , 17.37740322, 17.49608455,
                                                            17.61531175, 17.73515946]), decimal=6)

#        
if __name__ == '__main__':
    unittest.main()
