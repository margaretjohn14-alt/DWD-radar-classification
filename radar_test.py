import wradlib as wrl
import numpy as np

data, metadata = wrl.io.read_radolan_composite('C:\\Users\\marga\\projects\\DWD-radar\\HG_LATEST_000')
print(f"Data shape: {data.shape}")
print(f"Data min: {data.min()}")
print(f"Data max: {data.max()}")
print(f"Metadata keys: {list(metadata.keys())}")