# importing the necessory library
import numpy as np
import pandas as pd

# defining the function to read the box boundry

def dimension(file):
    f = open(file,'r')
    content = f.readlines()
#     stroring the each vertext point on the data list
    data = []
    v_info = []
    vertices_data =[]
#     cartesian_data =[]
#     vt_p = []
    for x in range(len(content)):
#         checking the file content cartesian points or not
        if "CARTESIAN_POINT" in content[x]:
            d=content[x].replace(",","").split(" ")
#             Storing the cartesian point (X,Y,Z)
            cartesian_data=d[0],d[7],d[8],d[9]
            data.append(cartesian_data)
            
#         checking for the unit used in step file.
        elif "LENGTH_UNIT" in content[x]:
            d=content[x].replace(",","").split(" ")
            length_unit = (d[11] +" "+ d[12]).replace(".","").title()
        elif "VERTEX_POINT " in content[x]:
            dt=content[x].replace(",","").split(" ")
            vt_p=dt[0],dt[5]
            v_info.append(vt_p)
                  
        else:
            pass 
        
    df = pd.DataFrame (data, columns = ['Line_no','x','y','z'])
    df = df.set_index("Line_no") 
    
    for value in range(len(v_info)):
        x_p = df.at[v_info[value][1],'x']
        y_p = df.at[v_info[value][1],'y']
        z_p = df.at[v_info[value][1],'z']
        Points = x_p,y_p,z_p
        vertices_data.append(Points)
        
 
        
#     storing all the vertices in np.array  
    vertices_data = np.array(vertices_data).astype(float)

#     storing the X, Y, Z minimum and Maximum values
    x_min=np.amin(vertices_data[:,0])
    y_min=np.amin(vertices_data[:,1])
    z_min=np.amin(vertices_data[:,2])
    x_max=np.amax(vertices_data[:,0])
    y_max=np.amax(vertices_data[:,1])
    z_max=np.amax(vertices_data[:,2])
    
#     Calculate the distance
    def measure(min_,max_):
        dist = max_ - min_
        return dist
    
#     Finding the Box Dimension:
    length = round(measure(x_min,x_max),2)
    width = round(measure(y_min,y_max),2)
    height = round(measure(z_min,z_max),2)
    return length, width, height ,length_unit