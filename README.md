## substitute.py

The `substitute.py` script is a Python function that accepts a dictionary as input and returns a modified version of the input dictionary. For every key-value pair in the input, the function performs substitution on the values based on the specified depth.

### Usage

The script can be executed from the command line and accepts three parameters:

1. JSON file name: The path to the JSON file to load as the input dictionary.
2. Depth (optional): An integer specifying the depth of the substitution. Default is `None`.
3. Output file path: The path to save the output dictionary.

## substitute.py:
python substitute.py input.json 2 out.json


## Unit Tests
python test_substitute.py