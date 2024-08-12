import pclpy
from pclpy import pcl


cloud = pcl.PointCloud.PointXYZ()
pcl.io.loadPLYFile("pointcloud/over1.ply", cloud)

# k-d tree is used to find nearest neighbors
tree = pcl.search.KdTree.PointXYZ()
# Initial instances. 
normals = pcl.PointCloud.PointNormal()
mls = pcl.surface.MovingLeastSquares.PointXYZ_PointNormal()

mls.setInputCloud(cloud)
mls.setPolynomialOrder(2)
mls.setSearchMethod(tree)
mls.setSearchRadius(0.03)

mls.setComputeNormals(True)
mls.process(normals)

for i in range(cloud.size()):
    normal = normals.points[i]
    print(f"Point {i}: Normal ({normal.normal_x}, {normal.normal_y}, {normal.normal_z})")

