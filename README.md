## Parsing json

You need to find the course named "Scripting languages" in JSON file and return its code.
Information about JSON file structure is available
```
- university
- courses
  - name
  - code
```
use ```text``` method for ```requests.get``` to obtain file content before parsing.

The number of courses may vary (theoretically), so **do not use numerical indexes** for them, but cycles instead.
```['courses'][1]['code']``` will return the correct answer, but is not considered a correct solution.
