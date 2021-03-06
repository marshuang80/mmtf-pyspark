#!/user/bin/env python
'''
advancedQueryService.py

Authorship information:
    __author__ = "Mars (Shih-Cheng) Huang"
    __maintainer__ = "Mars (Shih-Cheng) Huang"
    __email__ = "marshuang80@gmail.com:
    __status__ = "Done"
'''

import urllib

SERVICELOCATION="http://www.rcsb.org/pdb/rest/search"

def postQuery(xml):
    '''
    Post an XML query (PDB XML query format) to the RESTful
    RCSB web service
    '''

    encodedXML = urllib.parse.quote(xml).encode('utf-8')

    url = urllib.request.Request(SERVICELOCATION)

    with urllib.request.urlopen(url, data = encodedXML) as f:

        pdbIds = [str(l)[2:-3] for l in f.readlines()]

    return pdbIds
