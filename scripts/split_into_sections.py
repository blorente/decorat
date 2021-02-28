import sys
import json
import click
from pathlib import Path
from markdown2 import Markdown

def store_scene(title, scene, content):
    title_str = title.replace(" ", "_")
    scene_str = scene.replace(" ", "_").replace(".", "")
    return {f"({title_str})_{scene_str}.md": content}

@click.command()
@click.option('--outline', type=click.Path(exists=True))
@click.option('--outdir', type=click.Path(exists=True))
@click.option('--verbose', type=bool, default=False)
def main(outline, outdir, verbose):
  def vprint(msg):
      if verbose:
          print(msg, file=sys.stderr)

  outline = Path(outline).read_text().split("\n")
  files_to_create = {}
  is_in_outline = False
  current_title = ""
  scene_number = 0
  current_scene = ""
  current_content = ""
  for line in outline:
      if line.startswith("## Outline"):
          is_in_outline = True
          continue
      
      if not is_in_outline:
          continue
      vprint(line)

      if not line.strip():
          continue
      elif line.startswith("#"):
          if current_scene:
            files_to_create.update(store_scene(current_title, current_scene, scene_number, current_content))
            current_title = line.split("#")[-1].strip()
            current_scene = ""
            scene_number = 0
            current_content = ""
          else:
            current_title += "_" + line.split("#")[-1].strip()
      elif line.startswith("- **Scene:**"):
          scene_number += 1
          if current_scene:
              files_to_create.update(store_scene(current_title, current_scene, scene_number, current_content))
          current_scene = line.split("*")[-1].strip()
          current_content = line
      else:
          current_content += f"{line}\n"
  
  print(json.dumps(files_to_create))

if __name__ == "__main__":
  main()
