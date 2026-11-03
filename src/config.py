# src/config.py: one place for all data paths, works on Kaggle and on your PC
from pathlib import Path
import os

ON_KAGGLE = os.path.exists("/kaggle/input")       # True only inside a Kaggle notebook

if ON_KAGGLE:
    IMG_DIR      = Path("/kaggle/input/datasets/adityajn105/flickr8k/Images")
    CAPTIONS_TXT = Path("/kaggle/input/datasets/adityajn105/flickr8k/captions.txt")
    BANCAP_CSV   = Path("/kaggle/input/datasets/saifsust/bancap/BAN-Cap_captiondata.csv")
    OUT_DIR      = Path("/kaggle/working")        # Kaggle only lets you write here
else:
    ROOT         = Path(__file__).resolve().parent.parent   # the image_captioning folder
    IMG_DIR      = ROOT / "data" / "Images"
    CAPTIONS_TXT = ROOT / "data" / "captions.txt"
    BANCAP_CSV   = ROOT / "data" / "BAN-Cap_captiondata.csv"
    OUT_DIR      = ROOT / "data" / "processed"