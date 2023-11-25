aaa = {
    "switch": True,
    "type": "Action",
    "after": "software",
    "user": ["-all"],
    "uuid": "750b1e28684b4a61a41bb37d86814e46",
    "time": "2023-08-29 09:41:26",
    "comment": ""
}

import json
print(json.dumps(aaa))


ccc = aaa.get("bbb")
print(isinstance(ccc, int))