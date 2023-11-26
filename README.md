# Water/Vapor Interface Fluctuation Analysis

## Overview
This repository contains a Python script designed for analyzing fluctuations at the water/vapor interface. The script utilizes molecular dynamics data to compute and evaluate the surface height fluctuations over time, offering insights into the dynamic behavior of the interface.

## Key Features
- **Complex Surface Analysis**: Implements a sophisticated approach to process molecular dynamics simulation outputs, particularly focusing on the water/vapor interface.
- **Willard-Chandler Interface Detection**: Uses the Willard-Chandler method from the `pytim` library to identify and analyze the interface in molecular dynamics simulations of water.
- **Data Filtering and Processing**: Applies specific criteria to filter and process the vertex data, focusing on the absolute values to refine the interface height calculation.
- **Temporal Analysis**: The script runs through a specified time range, computing interface heights at each timestep, thus allowing for a temporal analysis of surface fluctuations.
- **Visualization**: Includes functionality to plot the computed surface height over time, providing a visual representation of the interface fluctuations.

## Usage
1. **Setting Parameters**: Define the time bounds (`time_b`, `time_e`) and the timestep increment (`delta_t`) for the analysis.
2. **Running the Script**: Execute the script to perform the interface height calculation over the specified time range.
3. **Result Output**: The script outputs the calculated surface heights and generates a plot showing the fluctuation over time.

## Dependencies
- `numpy`
- `matplotlib`
- `MDAnalysis`
- `pytim`
- `scipy`
- `pyvista`

## Note
This script is part of a research project aimed at understanding the dynamic properties of water interfaces. It is intended for use with molecular dynamics simulation data and requires specific input file formats.

