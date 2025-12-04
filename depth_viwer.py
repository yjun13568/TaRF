import numpy as np
import matplotlib.pyplot as plt
import os

def show_depth_map(npy_path):
    if not os.path.exists(npy_path):
        return

    depth_raw = np.load(npy_path)
    
    depth_2d = np.squeeze(depth_raw)
    
    print(f"min: {depth_2d.min():.4f}m ~ max: {depth_2d.max():.4f}m")

    # Normalization
    d_min = depth_2d.min()
    d_max = depth_2d.max()
    
    if d_max - d_min == 0:
        depth_norm = np.zeros_like(depth_2d)
    else:
        depth_norm = (depth_2d - d_min) / (d_max - d_min)
    
    depth = (depth_norm * 255).astype(np.uint8)
    return depth
  

file_path1 = "nerfstudio_modules/outputs/touch_estimation_input_cache/depth/40_50.npy"
file_path2 = "nerfstudio_modules/outputs/touch_estimation_input_cache/depth/0_40.npy"
#file_path3 = "img/depth/40_50.npy"
#file_path4 = "img/depth/0_40.npy"

plt.subplot(1,2,1)
plt.title("Depth View")
plt.imshow(show_depth_map(file_path1), cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Depth View")
plt.imshow(show_depth_map(file_path2), cmap='gray')
plt.axis('off')

plt.show()
