import os
import shutil
from datetime import datetime


source_dir = '/mnt/d/session-16'
backup_dir = '/mnt/d/session-16/backup'

# create if backup dir not exist
os.makedirs(backup_dir,exist_ok=True)

timestamp=datetime.now().strftime("%d-%m-%y_%H-%M-%S")

backup_file=f"backup-{timestamp}"
back_path=os.path.join(backup_dir,backup_file_name)

shutil.make_archive(backup_path,'zip',source_dir)
print("Backup completed successfully")





