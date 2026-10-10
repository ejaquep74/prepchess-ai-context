# Solopreneur Disaster Recovery

This directory acts as a safe mirror for critical Linux environment dotfiles. It ensures that custom AI rules, Git configurations, and WSL shell aliases are tracked securely within the project repository rather than being lost if the machine is wiped.

### How to trigger a backup
The AI is instructed to automatically run the backup script whenever it modifies a system file. 
To run it manually, simply execute:
```bash
./scripts/backup-env.py
```

### How to Restore your Environment
If you set up a fresh Linux machine, simply copy the contents of the `dotfiles` directory directly into your home (`~`) directory:
```bash
cp -r 4-disaster-recovery/dotfiles/* ~/
```
