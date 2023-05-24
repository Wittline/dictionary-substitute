import sys
import json

def substitute(dict_data, depth=None):
    """
    Substitutes values.
    
    Args:
        dict_data (dict): Input dictionary.
        depth (int): Depth of substitution.
    
    Returns:
        dict: Modified dictionary.
    """

    if depth is None:
        # substitution on all levels.
        depth = float('inf')

    if depth == 0:        
        return
    
    
    for k, v in dict_data.items():
        if isinstance(v, dict):            
            substitute(v, depth - 1)
        else:            
            dict_data[k] = {
                '_content': v,
                '_type': str(type(v))
            }
        

def save_dict(outputf, outputd):
    """
    Saves output.
    
    Args:
        outputf (str): Path output.
        outputd (dict): Output dictionary.
    """
    with open(outputf, 'w') as file:
        json.dump(outputd, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 4:        
        sys.exit(1)
    
    # read dict from json file
    with open(sys.argv[1], 'r') as file:
        dict_data = json.load(file)
        
    substitute(dict_data, int(sys.argv[2]))
    
    # Save modified
    save_dict(sys.argv[3], dict_data)
    
    print('Substitution ready!')