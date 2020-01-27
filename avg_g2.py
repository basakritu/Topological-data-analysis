import numpy as np
import math
from math import sqrt
import matplotlib.pyplot as plt
import gudhi

for k in range(2,2873):
    file=np.loadtxt('G2perprt/'+'pimage%05d_g2perprt.txt' %k)
    id_x=[]
    id_y=[]
    rad=[]
    for i in range(0,len(file)):
        id_x.append(file[i,0])
        id_y.append(file[i,1])
        rad.append(file[i,2])
        #print(idx)
    x_id=np.array(id_x)
    y_id=np.array(id_y)
    #print(len(x_id))
    radius=np.array(rad)
    edge=[]
#print(x_id)
    for i in range(0,len(id_x)):
        for j in range(0,len(id_y)):
            if(j!=i):
                if (math.sqrt((x_id[i]-x_id[j])**2 + (y_id[i]-y_id[j])**2) <= radius[i] + radius[j]):
                    edge.append([i,j])
    edges=np.array(edge)
    #print(len(edges))
#print(edges[2])
#print(edges)
    vertex=[]
    for i in range(0,len(file)):
        vertex.append(file[i,3])
    vertices=np.array(vertex)

#print(vertices[[edges[2][0]]])
    n_e=[]
    for j in range(0,len(edges)):
        new=max(vertices[edges[j][0]], vertices[edges[j][1]])
        n_e.append(new)
    new_vertex=np.array(n_e)
    #print((new_vertex))
    st = gudhi.SimplexTree()
    for i in range(1,len(new_vertex)):
        st.insert([edges[i][0],edges[i][1]],filtration= - new_vertex[i]) #st.insert( new_vertex[i-1] ,new_vertex[i], filtration = -new_vertex[i])
    st.initialize_filtration()
    diagram = st.persistence()
    #dim=st.persistence_intervals_in_dimension(1)
    #pair=st.persistence_pairs()
    #print(diagram)
    g='B0_max/'
    f=open(g+ str(k)+'.txt',"w")
    f.write(str(diagram))
    f.close()
    
    
