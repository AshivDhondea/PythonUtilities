"""
Gets the name of the script.

Useful when you want to name output files according
to the script which created them.
"""
import os
import sys

# --------------------------------------------------------------------------- #
file_name =  os.path.basename(sys.argv[0]);

if file_name[-3:] == '.py':
    script_name = file_name[:-3];
elif file_name[-3:] == '.ipynb':
    script_name = file_name[:-6];
else:
    script_name = 'main_xx';
# --------------------------------------------------------------------------- #
"""
Then the output file's name can be script_name+'some_string.png'
"""
