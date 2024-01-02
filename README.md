# 📐 GeoPyLib

GeoPyLib is a Python library designed to tackle problems related to 2D and 3D Coordinate Geometry. Whether you're calculating distances, finding midpoints, or working with equations of lines and shapes, GeoPyLib provides a set of functions to simplify these tasks.

## Installation 🚀

To install GeoPyLib and its dependencies, use the following commands:

```bash
pip install -r requirements.txt
pip install GeoPyLib
```

## Features 🌟

GeoPyLib includes a plethora of features for both 2D and 3D Coordinate Geometry:

- Distance calculation
- Midpoint calculation
- Slope calculation
- Equations of lines (various forms)
- Triangle area calculation
- Circle, parabola, ellipse, and hyperbola equations
- 3D-specific functions like plane equations, angle between lines, and more.

## Usage 💡

Here's a simple example demonstrating how to use GeoPyLib in a Python script:

```python
from GeoPyLib import CoordinateGeometry2D, CoordinateGeometry3D

# Example 2D Coordinate Geometry
geo_2d = CoordinateGeometry2D()

x1, y1 = 1, 2
x2, y2 = 4, 6

distance = geo_2d.distance_formula(x1, y1, x2, y2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {distance}")

# Example 3D Coordinate Geometry
geo_3d = CoordinateGeometry3D()

x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 6, 8

distance_3d = geo_3d.distance_formula(x1, y1, z1, x2, y2, z2)
print(f"3D Distance between ({x1},{y1},{z1}) and ({x2},{y2},{z2}): {distance_3d}")
```

## Requirements 📋

- numpy==1.21.0
- matplotlib==3.4.3
