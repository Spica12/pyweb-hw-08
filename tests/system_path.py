import sys
import os
from pprint import pprint

pprint(sys.path)
# [
#     "/media/spica/Storage/GoIT/PythonWEB-homework/pyweb-hw-08/tests",
#     "/usr/lib/python312.zip",
#     "/usr/lib/python3.12",
#     "/usr/lib/python3.12/lib-dynload",
#     "/home/spica/.cache/pypoetry/virtualenvs/pyweb-hw-08-0ebltS1P-py3.12/lib/python3.12/site-packages",
# ]

sys.path.append(os.path.join(os.getcwd(), "src"))
# sys.path.append('..')

pprint(sys.path)
# [
#     "/media/spica/Storage/GoIT/PythonWEB-homework/pyweb-hw-08/tests",
#     "/usr/lib/python312.zip",
#     "/usr/lib/python3.12",
#     "/usr/lib/python3.12/lib-dynload",
#     "/home/spica/.cache/pypoetry/virtualenvs/pyweb-hw-08-0ebltS1P-py3.12/lib/python3.12/site-packages",
#     "/media/spica/Storage/GoIT/PythonWEB-homework/pyweb-hw-08/src",
# ]
