import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in os.listdir('.'):
    if fname.endswith('.py') and fname != 'find_colors.py':
        filepath = os.path.abspath(fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                lines = f.readlines()
            except Exception as e:
                print(f"Skipping {fname}: {e}")
                continue
        for i, line in enumerate(lines):
            line_num = i + 1
            if 'bg=' in line or 'fg=' in line or 'background=' in line or 'foreground=' in line or 'activebackground=' in line:
                if not line.strip().startswith('#'):
                    print(f"{fname}:{line_num}: {line.strip()}")
