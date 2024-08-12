import pclpy
from pclpy import pcl

cloud = pcl.PointCloud.PointXYZ()
pcl.io.loadPLYFile("pointcloud/over1.ply", cloud)

# Create instances
ne = pcl.features.NormalEstimation.PointXYZ_Normal()
# k-d tree is used to find nearest neighbors
tree = pcl.search.KdTree.PointXYZ()
normals = pcl.PointCloud.Normal()

ne.setInputCloud(cloud)
ne.setSearchMethod(tree)
ne.setRadiusSearch(0.03)

ne.compute(normals)

for i in range(cloud.size()):
    normal = normals.points[i]
    print(f"Point {i}: Normal ({normal.normal_x}, {normal.normal_y}, {normal.normal_z})")
