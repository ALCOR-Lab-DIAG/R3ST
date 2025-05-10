import numpy as np
import cv2 as cv
import os
import argparse

# This script processes a .npz file containing segmentation masks and depth maps.
# It generates and saves the segmentation mask and depth map as images in a specified output directory.
# The segmentation mask is color-mapped and the depth map is normalized and color-mapped.

def main(npz_path, out_dir):
    try:
        data = np.load(npz_path)
    except Exception as e:
        print(f"Error loading {npz_path} ===> {e}")
        return
    
    os.makedirs(out_dir, exist_ok=True)
    print(data.files, "\n")

    frame_number = npz_path.split('/')[-1].split('.')[0]
    print(f"Processing frame number: {frame_number}")

    # Process and save segmentation mask
    if 'segmentation_masks' in data.files:
        sg_msk = data['segmentation_masks']
        sg_msk_inds = data['segmentation_masks_indexes']

        inds = sg_msk_inds['pass_index']
        inds = inds[inds != 0]
        inds = np.unique(inds)
        n_inds = len(inds)
        cmap_vals = np.linspace(0.0, 1.0, n_inds) * 255.0

        height, width = sg_msk.shape
        sg_msk_img = np.zeros((height, width, 3), np.uint8)
        for counter, ind in enumerate(inds):
            sg_msk_img[sg_msk == ind] = cmap_vals[counter]

        sg_msk_img = cv.applyColorMap(sg_msk_img, cv.COLORMAP_RAINBOW)
        sg_msk_img[sg_msk == 0] = [0, 0, 0]


        cv.imwrite(os.path.join(out_dir, f'segmentation_mask_{frame_number}.png'), sg_msk_img)
        print(f"Saved segmentation mask to {out_dir}/segmentation_mask_{frame_number}.png")

    # Process and save depth map
    if 'depth_map' in data.files:
        depth = data['depth_map']
        INVALID_DEPTH = -1
        depth_min = np.amin(depth[depth != INVALID_DEPTH])
        depth_max = np.amax(depth)
        normalized_depth = (1.0 - (depth - depth_min) / (depth_max - depth_min)) * 255.0
        normalized_depth = normalized_depth.astype(np.uint8)
        depth_grayscale = cv.cvtColor(normalized_depth, cv.COLOR_GRAY2BGR)
        depth_colored = cv.applyColorMap(normalized_depth, cv.COLORMAP_JET)
        depth_colored[depth == INVALID_DEPTH] = [0, 0, 0]
        depth_grayscale[depth == INVALID_DEPTH] = [0, 0, 0]

        cv.imwrite(os.path.join(out_dir, f'depth_map_{frame_number}.png'), depth_grayscale)
        print(f"Saved depth map to {out_dir}/depth_map_{frame_number}.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="output", help="Output directory to save results")
    parser.add_argument("--npz", type=str, required=True, help="Path to .npz file")
    args = parser.parse_args()

    main(args.npz, args.out)