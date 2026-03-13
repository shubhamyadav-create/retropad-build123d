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
