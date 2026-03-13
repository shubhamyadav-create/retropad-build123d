# RetroPad Assembly using build123d

This project demonstrates how to assemble the RetroPad controller case using the **build123d** Python CAD library.

## Files

- RetroPad - Top Shell.stl
- RetroPad - Bottom Shell.stl
- RetroPad - Button.stl
- RetroPad - D-Pad.stl
- assembly.py
- retropad_assembly.stl

## Requirements

Python 3.9+

Install build123d:

pip install build123d

## Workflow

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/retropad-build123d.git

2. Navigate to the folder

cd retropad-build123d

3. Run the assembly script

python assembly.py

4. The script imports the STL parts and combines them into one assembly.

5. The final assembled model will be exported as:

retropad_assembly.stl

## Result

The output STL contains the assembled RetroPad case including:

- Top Shell
- Bottom Shell
- Button
- D-Pad
  
Note: Open the .stl file created by the script in CAD based Software i.e Fusion 360,etc 

## Tools Used

- Python
- build123d
- STL geometry

volume symmetric difference explanation:

The symmetric volume check is performed by reflecting each triangle's centroid across the part's principal symmetry plane — specifically the midplane of the bounding box along the X axis, defined as `axis = (xmin + xmax) / 2`. For every triangle in the mesh, the centroid is computed as the average of its three vertices, rounded to one decimal place for floating-point tolerance. The mirror of that centroid is then calculated as `(2·axis − cx, cy, cz)`, flipping only the X coordinate while keeping Y and Z unchanged. This mirrored point is looked up in a pre-built set of all triangle centroids in the mesh. If a match is found, the triangle has a corresponding mirror triangle on the opposite side of the symmetry plane — meaning the geometry is locally symmetric at that location. The ratio of matched triangles to total triangles gives a symmetry score as a percentage. A score of 100% means every triangle has an exact mirror counterpart, confirming that `Vol(A Δ Mirror(A)) = 0` — the formal set-theory condition for perfect geometric symmetry. For scores below 100%, the approximate symmetric volume difference is estimated as `Vol(A) × (1 − symmetry_fraction) × 2`, which quantifies how much volume exists on one side of the plane without a corresponding counterpart on the other side.
