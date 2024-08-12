# Final Project of Clinical Applicaiton of Computational Medicine

This repository hosts the code for the final project of the "Clinic Applications of Computational Medicine" lecture at TUM.

Project Subject: "Semiautonomous Telerobotic Auscultation with Surface Normal Estimation"

This project is based on the [6G-life](https://www.ce.cit.tum.de/lkn/research/6g-life/) project initiative by the [MITI](https://web.med.tum.de/en/miti/home/) group and [LKN](https://www.ce.cit.tum.de/lkn/startseite/) chair.

Main Contributors: Jeff Lin, Zikang Liu, Yuya Yuan, Delun Zhang
 
Supervisor: [Sven Kolb, M.Sc](https://web.med.tum.de/miti/personen/sven-kolb/).

## Name
Semiautonomous Telerobotic Auscultation with Surface Normal Estimation

## Description
With the normal vector of the chest surface, the robotic arms can put the stethoscope with the correct angle. 

## Conda Environment
Packages: python, pclpy, open3d 

Commands      
```
python == 3.7       
conda install -c conda-forge -c davidcaron pclpy        
conda install -c open3d-admin open3d        
```

## File Explanation    
open3d_normal.py: algorithm estimating normal vectors    
pclpy_normal.py: algorithm estimating normal vectors    
pclpy_poly.py: algorithm estimating normal vectors             

## Video Link 
https://drive.google.com/file/d/1O_zOlRpkffZDXiX0jzWqyexz5RCrZJAL/view?usp=sharing  

## License
Due to the privacy policy, I can only provide the code for calculating the normal vector estimation.