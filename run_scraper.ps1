# Can use this to make a desktop shortcut to run the scraper
# 1. Create a desktop shortcut
# 2. Set the target to "powershell.exe -file path\to\script.ps1"

# Activate the virtual environment
.\venv\Scripts\activate

# Run the scraper
python rivals_code_scraper.py

# Deactivate the virtual environment
deactivate

# Wait for user to press Enter before closing
Read-Host -Prompt "Press Enter to close"