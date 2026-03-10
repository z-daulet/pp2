from pathlib import Path
import shutil

# copying file to another directory

root  =Path(__file__).parent / "workspace"
source =  root/"raw_dir"/"1.txt"
destination = root/"processed"/"1.txt"

shutil.copy2(source,destination)

# file migration to different dir

source =  root/"raw_dir"/"2.txt"
destination = root/"processed"
shutil.move(source,destination)
print("File moved!")