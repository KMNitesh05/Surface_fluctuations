import os, numpy as np, MDAnalysis as mda, pytim, matplotlib.pyplot as plt
from scipy import spatial
from pytim.datafiles import *
import pyvista as pv
import random, functools


class CompSurfaceAnalysis:
    def __init__(self, start_time, end_time, step):
        self.start_time = start_time
        self.end_time = end_time
        self.step = step
        self._internal_state = {}

    def _convoluted_calculation(self, universe, core_selection):
        core = universe.select_atoms(core_selection)
        willard_chandler = pytim.WillardChandler(universe, group=core, alpha=2.5, mesh=2.0, fast=False)
        return willard_chandler.triangulated_surface[0][:, 2]

    def _process_vertices(self, vertices):
        filtered_left = [v for v in vertices if v < 70.0]
        filtered_left = np.array(filtered_left) - np.mean(filtered_left)
        filtered_left = [v for v in filtered_left if abs(v) < 3.0]

        filtered_right = [v for v in vertices if v > 70.0]
        filtered_right = np.array(filtered_right) - np.mean(filtered_right)
        filtered_right = [v for v in filtered_right if abs(v) < 3.0]

        return filtered_left, filtered_right

    def perform_analysis(self):
        self._internal_state['time'], self._internal_state['surface_height'] = [], []
        t = self.start_time
        while t <= self.end_time:
            universe = mda.Universe("water_pure" + str(t) + ".gro")
            z_coords = self._convoluted_calculation(universe, 'name OW')
            left_z, right_z = self._process_vertices(z_coords)
            height = (np.mean(left_z) + np.mean(right_z)) / 2
            self._internal_state['time'].append(t)
            self._internal_state['surface_height'].append(height)
            t += self.step

    def save_results(self, filename):
        np.savetxt(filename, self._internal_state['surface_height'])


comp_analyzer = CompSurfaceAnalysis(1, 3500, 10)
comp_analyzer.perform_analysis()
comp_analyzer.save_results("comp_surface_height_pure.csv")


plot_lambda = lambda height: plt.plot(height)
plot_lambda(list(map(lambda x: x + random.uniform(-0.5, 0.5), comp_analyzer._internal_state['surface_height'])))
plt.show()
