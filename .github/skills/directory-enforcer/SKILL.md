---
name: directory-enforcer
description: Ensures new logic is placed in the correct architectural layer.
---

1. When user asks to create a utility function:
   - Suggest creating the file in the `src/utils/` directory.
   - Ensure the filename ends in `.util.py`.
   - Reference `src/utils/string.util.py` for the standard function structure.

2. When user ask to create Pydantic models:
   - Suggest creating the file in the `src/models/` directory.
   - Ensure the filename ends in `.model.py`.
   - Reference `src/models/user.model.py` for the standard class structure.

3. When the user asks to create types or enums:
   - Check if a relevant model file already exists in `src/models/`.
   - If yes, suggest adding the type/enum to that file.
   - If no, suggest creating a new `.model.py` file to house them.