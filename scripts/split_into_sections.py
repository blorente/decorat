import sys
from pathlib import Path
from markdown2 import Markdown

outline = Path(sys.argv[1]).read_text().split("\n")
files_to_create = {}
def store_scene(title, scene, content):
    title_str = title.replace(" ", "_")
    scene_str = scene.replace(" ", "_").replace(".", "")
    return {f"({title_str})_{scene_str}.md": content}

is_in_outline = False
current_title = ""
current_scene = ""
current_content = ""
for line in outline:
    if line.startswith("## Outline"):
        is_in_outline = True
        continue
    
    if not is_in_outline:
        continue
    print(line)

    if line.startswith("#"):
        if current_scene:
          files_to_create.update(store_scene(current_title, current_scene, current_content))
          current_title = line.split("#")[-1].strip()
          current_scene = ""
          current_content = ""
        else:
          current_title += "_" + line.split("#")[-1].strip()
    elif line.startswith("- **Scene:**"):
        files_to_create.update(store_scene(current_title, current_scene, current_content))
        current_scene = line.split("*")[-1].strip()
        current_content = line
    else:
        current_content += line


print(files_to_create.keys())
