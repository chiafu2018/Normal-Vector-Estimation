import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("pointcloud\over1.ply")
graph = np.asarray(pcd.points)
print(pcd)
o3d.visualization.draw_geometries([pcd])

# Delete downsampling if not needed.
print("Downsample the point cloud with a voxel of 0.05")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
graph = np.asarray(downpcd.points)
print(downpcd)
# o3d.visualization.draw_geometries([downpcd])

downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

point = 0
print("Print a normal vector of the desired point")
print(f"Point {point}: Normal: {downpcd.normals[point]}")


#Using knn to avg the normal vector, or can use weighted sum 
dis, total = [], []

for i in graph:
    dis.append(sum(x ** 2 for x in point-i))

sorted_indices = np.argsort(dis).tolist() # You need to turn it into a original array 
for candidate in range(10): # k = 10
    total.append(downpcd.normals[sorted_indices[candidate]])

print("Print the average of K closest points' normal vectors to lower the potential error")
print(f"Point {point}: Normal: {np.mean(total, axis=0)}")


# Reorient normals to be consistent with the outward direction of the surface
downpcd.orient_normals_consistent_tangent_plane(k=30)

o3d.visualization.draw_geometries([downpcd], point_show_normal=True)