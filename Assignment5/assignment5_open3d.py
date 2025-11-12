import open3d as o3d
import numpy as np

# === STEP 1: Load and visualize original model ===
model_path = r"C:\Users\musta\mercadoinsights-olist-ecommerce\Assignment5\my_model_mustafa.ply"

mesh = o3d.io.read_triangle_mesh(model_path)
if not mesh.has_vertex_normals():
    mesh.compute_vertex_normals()

print("\n--- Step 1: Original Mesh ---")
print("Vertices:", np.asarray(mesh.vertices).shape[0])
print("Triangles:", np.asarray(mesh.triangles).shape[0])
print("Has color:", mesh.has_vertex_colors())
print("Has normals:", mesh.has_vertex_normals())
o3d.visualization.draw_geometries([mesh], window_name="Original Mesh")

# === STEP 2: Convert to point cloud ===
pcd = mesh.sample_points_uniformly(number_of_points=5000)
print("\n--- Step 2: Point Cloud ---")
print("Vertices:", np.asarray(pcd.points).shape[0])
print("Has color:", pcd.has_colors())
o3d.visualization.draw_geometries([pcd], window_name="Sampled Point Cloud")

# === STEP 3: Surface reconstruction (Poisson) ===
mesh_poisson, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)
bbox = mesh.get_axis_aligned_bounding_box()
mesh_poisson = mesh_poisson.crop(bbox)
print("\n--- Step 3: Reconstructed Mesh (Poisson) ---")
print("Vertices:", np.asarray(mesh_poisson.vertices).shape[0])
print("Triangles:", np.asarray(mesh_poisson.triangles).shape[0])
o3d.visualization.draw_geometries([mesh_poisson], window_name="Reconstructed Mesh (Poisson)")

# === STEP 4: Voxelization ===
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.05)
print("\n--- Step 4: Voxel Grid ---")
print("Voxels:", len(voxel_grid.get_voxels()))
o3d.visualization.draw_geometries([voxel_grid], window_name="Voxel Grid")

# === STEP 5: Add a plane ===
plane = o3d.geometry.TriangleMesh.create_box(width=3, height=0.01, depth=3)
plane.paint_uniform_color([0.8, 0.8, 0.8])
plane.translate([0, -0.1, 0])
print("\n--- Step 5: Plane Added ---")
o3d.visualization.draw_geometries([mesh_poisson, plane], window_name="Mesh + Plane")

# === STEP 6: Surface clipping (remove points above plane) ===
points = np.asarray(pcd.points)
mask = points[:, 1] < 0.0  # y-axis clipping
pcd_clipped = o3d.geometry.PointCloud()
pcd_clipped.points = o3d.utility.Vector3dVector(points[mask])
print("\n--- Step 6: After Clipping ---")
print("Remaining vertices:", np.asarray(pcd_clipped.points).shape[0])
o3d.visualization.draw_geometries([pcd_clipped], window_name="Clipped Point Cloud")

# === STEP 7: Recolor and mark extrema ===
pts = np.asarray(pcd.points)
z_vals = pts[:, 2]
z_min, z_max = z_vals.min(), z_vals.max()
colors = (z_vals - z_min) / (z_max - z_min)
colors = np.stack([colors, 1 - colors, np.zeros_like(colors)], axis=1)
pcd.colors = o3d.utility.Vector3dVector(colors)

min_point = pts[np.argmin(z_vals)]
max_point = pts[np.argmax(z_vals)]
sphere_min = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
sphere_min.translate(min_point)
sphere_min.paint_uniform_color([1, 0, 0])

sphere_max = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
sphere_max.translate(max_point)
sphere_max.paint_uniform_color([0, 1, 0])

print("\n--- Step 7: Color Gradient & Extremes ---")
print("Z-min coordinates:", min_point)
print("Z-max coordinates:", max_point)
o3d.visualization.draw_geometries([pcd, sphere_min, sphere_max], window_name="Color Gradient + Extremes")
