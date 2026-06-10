import csv
import random
import os
import sys

NUM_ROWS = 67

COLUMNS = ["Brawl_stars", "Standoff", "Roblox", "Clash_royale"]

def generate_row():
    return {
        "Brawl_stars": random.choice(["шелли", "ворон", "60"]),
        "Standoff": random.choice(["FBI", "SIG4", "FOG"]),
        "Roblox": random.choice(["tower of hell", "dress to impress", "adopt me"]),
        "Clash_royale": random.choice(["мерарыцарь", "вышибала", "темный принц"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
