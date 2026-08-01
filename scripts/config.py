from pathlib import Path
import yaml

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ==========================================================
# Load configuration
# ==========================================================

with open(PROJECT_ROOT / "environment.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# ==========================================================
# Main folders
# ==========================================================

RAW_DATA = PROJECT_ROOT / config["paths"]["raw_data"]
PROCESSED_DATA = PROJECT_ROOT / config["paths"]["processed_data"]
INTERIM_DATA = PROJECT_ROOT / config["paths"]["interim_data"]
OUTPUT_DATA = PROJECT_ROOT / config["paths"]["output_data"]

# ==========================================================
# Input datasets
# ==========================================================

BMD = PROJECT_ROOT / config["paths"]["bmd"]
CCS = PROJECT_ROOT / config["paths"]["ccs"]
CDR = PROJECT_ROOT / config["paths"]["cdr"]
CHIRPS = PROJECT_ROOT / config["paths"]["chirps"]
DISTANCE_SEA = PROJECT_ROOT / config["paths"]["distance_sea"]
ERA5 = PROJECT_ROOT / config["paths"]["era5"]
GSMAP = PROJECT_ROOT / config["paths"]["gsmap"]
GSMAP_MVK = PROJECT_ROOT / config["paths"]["gsmap_mvk"]
IMERG = PROJECT_ROOT / config["paths"]["imerg"]
BOUNDARY = PROJECT_ROOT / config["paths"]["boundary"]
LAND_VARIABLE = PROJECT_ROOT / config["paths"]["land_variable"]
LST = PROJECT_ROOT / config["paths"]["lst"]
NDVI = PROJECT_ROOT / config["paths"]["ndvi"]
PDIR = PROJECT_ROOT / config["paths"]["pdir"]
PERSIANN = PROJECT_ROOT / config["paths"]["persiann"]

# ==========================================================
# Results
# ==========================================================

FIGURES = PROJECT_ROOT / config["results"]["figures"]
TABLES = PROJECT_ROOT / config["results"]["tables"]
MAPS = PROJECT_ROOT / config["results"]["maps"]