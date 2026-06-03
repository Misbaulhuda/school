
import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
os.makedirs("../visuals", exist_ok=True)
zip_path = "../archive.zip"
extract_path = "../data"
os.makedirs(extract_path, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
print("\n========== ZIP FILE EXTRACTED ==========\n")
