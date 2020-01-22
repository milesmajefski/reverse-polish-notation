from collections import deque
import json
from rpn_operators import _operators


def parse_float(data_string):
    """
    Take a string of user input like "1 2 +" and return parsed data
    like (1.0, 2.0, "+") in a list inside a dict.  Always using float 
    because / operator will often return a float automatically.
    """

    parsed = []
    for d in data_string.split():
        if d in _operators:
            parsed.append(d)
            continue

        try:
            as_float = float(d)
        except ValueError as e:
            return {'parsed': parsed, 'error_msg': f'Cannot convert {d} to float and {d} is not a supported operator'}
        else:
            parsed.append(as_float)

    return {'parsed': parsed, 'error_msg': None}
