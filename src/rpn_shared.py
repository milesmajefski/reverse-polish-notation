"""
This module contains code that could be used by future python front-ends.
"""
from rpn_operators import _operators


def parse_float(data_string):
    """
    This function takes a string of user input like "1 2 +" and returns parsed
    data like (1.0, 2.0, "+") in a list inside a dict.  It always uses float
    because "/" operator will often return a float automatically.
    """
    parsed = []
    for d in data_string.split():
        if d in _operators:
            parsed.append(d)
            continue

        try:
            as_float = float(d)
        except ValueError:
            return {'parsed': parsed,
                    'error_msg':
                    f'Cannot convert {d} to float and {d} is not a supported operator'}
        else:
            parsed.append(as_float)

    return {'parsed': parsed, 'error_msg': None}
