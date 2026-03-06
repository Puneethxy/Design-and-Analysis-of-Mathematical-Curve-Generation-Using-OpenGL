# Design-and-Analysis-of-Mathematical-Curve-Generation-Using-OpenGL

This project demonstrates the implementation and visualization of different parametric curves using Python, PyGame, and OpenGL.
The goal of this project is to study how various curve algorithms work, visualize them graphically, and analyze their time and space complexity.

The program generates curves based on control points and mathematical equations, then renders them in a graphical window using OpenGL.

Project Overview:

Curves play an important role in computer graphics, animation, CAD systems, and geometric modeling. Different mathematical formulations allow smooth curve generation from a set of control points.

This project focuses on implementing and visualizing multiple curve generation techniques to better understand their behavior, efficiency, and graphical representation.

Implemented Curves:

The repository contains implementations of different curve algorithms, including:

Bézier Curves

Cubic Bézier Curves

3D Bézier Curves

Bézier Surface (16 Control Points)

Other parametric curve implementations used for experimentation and visualization.

Each implementation renders:

Control Points

Control Polygon

Generated Curve

Features

Visualization of curves using OpenGL

Random or predefined control point generation

Rendering of control polygons

Computation of curve points using mathematical equations

Time complexity measurement (execution time)

Space complexity measurement (memory usage)

Modular code structure for experimenting with different curve algorithms

Technologies Used

Python

PyGame

PyOpenGL

NumPy

These libraries allow efficient mathematical computation and real-time graphical rendering.

Installation

Clone the repository:

git clone https://github.com/yourusername/curve-visualization.git
cd curve-visualization

Install the required dependencies:

pip install -r requirements.txt
Running the Project

Run the desired curve implementation:

python main.py

Depending on the script, a window will open showing:

Control points

Control polygon

Generated curve

The terminal will also display the execution time and memory usage for the curve computation.

Complexity Analysis

For n sampled points along a curve:

Time Complexity

O(n)

Each point on the curve is computed independently for a parameter value t.

Space Complexity

O(n)

Memory is required to store the generated curve points.

Applications

Curve generation techniques are widely used in:

Computer graphics

Animation and motion paths

CAD and industrial design

Font and vector graphics rendering

Game development

Surface modeling

Future Improvements

Possible extensions of this project include:

Interactive movement of control points

Real-time curve editing

Support for additional curve algorithms

Visualization of advanced 3D surfaces

Performance comparison between curve generation methods

Author:
Puneeth Satish Kumar - 2022BIFT07AED028
Jaisri V - 2022BIFT07AED043
Rehan Ahmed - 2022BIFT07AED044
Soma Ganeshwar Reddy - 2022BIFT07AED007

B.Tech Capstone Project
Curve Generation and Visualization in Computer Graphics
