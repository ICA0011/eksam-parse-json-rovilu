[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7942182&assignment_repo_type=AssignmentRepo)
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
