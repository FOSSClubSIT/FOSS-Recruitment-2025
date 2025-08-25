# src/overlay.py
import cv2
import numpy as np

# put this near the top of overlay.py
def proj(idx):
    return idx


def ref_corners_wh(w, h):
    """Return 4 reference corners in pixel units (Z=0 plane)."""
    return np.float32([[0, 0],
                       [w, 0],
                       [w, h],
                       [0, h]]).reshape(-1, 1, 2)

def warp_ref_corners_to_scene(H, w_ref, h_ref):
    """Project reference corners using homography H to scene image."""
    corners = ref_corners_wh(w_ref, h_ref)
    proj = cv2.perspectiveTransform(corners, H)  # shape (4,1,2)
    return proj

def draw_polygon(img_bgr, pts, color=(0, 255, 0), thickness=2):
    """Draw a closed 4-point polygon on image."""
    pts2 = pts.reshape(-1, 2).astype(int)
    for i in range(4):
        p1 = tuple(pts2[i])
        p2 = tuple(pts2[(i + 1) % 4])
        cv2.line(img_bgr, p1, p2, color, thickness, cv2.LINE_AA)
    return img_bgr

def project_points(P, pts_3d):
    """Project Nx3 3D points with P (3x4) to image (Nx2)."""
    pts_h = np.hstack([pts_3d, np.ones((pts_3d.shape[0], 1))])  # Nx4
    proj = (P @ pts_h.T).T  # Nx3
    proj = proj[:, :2] / proj[:, 2:3]
    return proj

def draw_cube(img_bgr, P, w_ref, h_ref, height_factor=0.5,
              color=(255, 0, 0), thickness=2):
    """
    Draw a cube extruded from the reference plane (Z negative).
    Base square = reference image rectangle (0,0)-(w_ref,h_ref).
    """
    base = np.array([[0, 0, 0],
                     [w_ref, 0, 0],
                     [w_ref, h_ref, 0],
                     [0, h_ref, 0]], dtype=np.float64)

    height = height_factor * min(w_ref, h_ref)
    top = base.copy()
    top[:, 2] = -height  # extend "out of" the plane

    pts3d = np.vstack([base, top])  # 8 points
    proj = project_points(P, pts3d).astype(int)

    # base square
    for i in range(4):
        cv2.line(img_bgr, tuple(proj[i]), tuple(proj[(i + 1) % 4]),
                 color, thickness, cv2.LINE_AA)
    # top square
    for i in range(4, 8):
        cv2.line(img_bgr, tuple(proj[i]), tuple(proj(((i - 4 + 1) % 4) + 4)),
                 color, thickness, cv2.LINE_AA)
    # vertical edges
    for i in range(4):
        cv2.line(img_bgr, tuple(proj[i]), tuple(proj[i + 4]),
                 color, thickness, cv2.LINE_AA)
    return img_bgr
