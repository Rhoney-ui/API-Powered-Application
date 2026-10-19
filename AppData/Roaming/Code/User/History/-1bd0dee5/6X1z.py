# Stage a single file
git add tracker.py 

# Stage multiple specific files
git add tracker.py config.py README.md

# Stage all changes in the current directory
git add .

# Check what is staged
git status

# COMMITTING WITH GIT COMMIT
# MAKING COMMITS

# Committ with an inline message
git committ -m "Add SMP tracker script with daily check-in logic"
[main (root-commit) a1b2c3d] Add SMP tracker script with daily check-in logic
3 files changed, 84 insertions (+)
create mode 100644 .gitignore
create mode 100644 README.md
create mode 100644 tracker.py

# Stage and commit all tracked files in one step
git commit -am "Fix step count calculation off-by-one error"
# Note: -a only stages already-tracked files, not new files 
