from build123d import *

top_shell = import_stl("RetroPad - Top Shell.stl")
bottom_shell = import_stl("RetroPad - Bottom Shell.stl")
button = import_stl("RetroPad - Button.stl")
dpad = import_stl("RetroPad - D-Pad.stl")

assembly = Compound([top_shell, bottom_shell, button, dpad])

export_stl(assembly, "retropad_assembly.stl")

print("Assembly exported successfully")