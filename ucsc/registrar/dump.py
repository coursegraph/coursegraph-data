from courses import *
import json

output = { "departments": depts, "courses": courses }
with open('dump.json', 'w') as f:
    json.dump(output, f)
    # f.write(repr(output))
