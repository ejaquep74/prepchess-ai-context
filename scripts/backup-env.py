#!/usr/bin/env python3
import os
import shutil

# Define core paths
HOME = os.path.expanduser("~")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKUP_DIR = os.path.join(REPO_ROOT, "4-disaster-recovery", "dotfiles")

# The definitive list of critical environment files (relative to home directory)
FILES_TO_BACKUP = [
    ".bashrc",
    ".gitconfig",
    ".gemini/config/AGENTS.md"
]

def run_backup():
    print(f"Starting environment backup to: {BACKUP_DIR} ...")
    
    success_count = 0
    for file_path in FILES_TO_BACKUP:
        src = os.path.join(HOME, file_path)
        dest = os.path.join(BACKUP_DIR, file_path)
        
        if os.path.exists(src):
            # Create the necessary subdirectories in the backup folder
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            # Copy file, preserving metadata
            shutil.copy2(src, dest)
            print(f"✅ Backed up: ~/{file_path}")
            success_count += 1
        else:
            print(f"⚠️  Warning: ~/{file_path} not found. Skipping.")

    print(f"\nBackup complete! Successfully mirrored {success_count}/{len(FILES_TO_BACKUP)} files.")

if __name__ == "__main__":
    run_backup()
