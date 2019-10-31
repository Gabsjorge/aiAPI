"""This module will encode and parse the query string params."""

import urllib.parse as urlparse
import sys
sys.modules['urlparse'] = urlparse
sys.modules['urllib'] = urlparse
from urlparse import parse_qs

# # AI methods
# prepare = imp.load_source('*', './facial_recognition/app/core/preparing.py')
# train = imp.load_source('*', './facial_recognition/app/core/traning.py')
# recognize = imp.load_source('*', './facial_recognition/app/core/recognizing.py')


def parse_query_params(query_string):
    """
        Function to parse the query parameter string.
        """
    # Parse the query param string
    query_params = dict(parse_qs(query_string))
    # Get the value from the list
    query_params = {k.decode('ascii'): v[0].decode('ascii') for k, v in query_params.items()}
    return query_params
