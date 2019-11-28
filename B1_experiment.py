import numpy as np
import math
from math import sqrt
import matplotlib.pyplot as plt
import gudhi

def trivialTriangle(particle_ids, force):
# particle_ids: a list of particle ids in contact; dimension: N*2
# force: list of contact force;dimension: N*1
# trivial: list, n*4
    trivialLoops = []
    id_len = len(particle_ids)
    for idx,item in enumerate(particle_ids):
        id1 = item[0]
        id2 = item[1]
        force12 = force[idx]    
        id1_set = set()
        id2_set = set()   
        for i in range(idx+1,id_len):
            l2 = particle_ids[i]
            if id1 in l2:
                id3 = l2[l2!=id1]
                id1_set.add(id3)
                
            if id2 in l2:
                id3 = l2[l2!=id2]
                id2_set.add(id3)
                
        common_id3 = id1_set & id2_set
        len_common = len(common_id3)
        
        if len_common > 0:
            for id3 in common_id3:
                for j in range(idx+1,id_len):
                    if set([id1,id3]) == set(particle_ids[j]):
                        force13 = force[j]
                    if set([id2,id3]) == set(particle_ids[j]):
                        force23 = force[j]
                fmin = min(force12,force13,force23)
                trivialLoops.append([id1,id2,id3,fmin])
    return trivialLoops

for k in range(400,401):
    file=np.loadtxt('G2perprt/'+'pimage%05d_g2perprt.txt' %k)
    id_x=[]
    id_y=[]
    rad=[]
    for i in range(0,len(file)):
        id_x.append(file[i,0])  #x_pos
        id_y.append(file[i,1])  #y_pos
        rad.append(file[i,2])   #rad
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
                if (math.sqrt((x_id[i]-x_id[j])**2 + (y_id[i]-y_id[j])**2) <= radius[i] + radius[j]): #particles id's which are in contact
                    edge.append([i,j])
    edges=np.array(edge) 
    print((edges))
#print(edges[2])
#print(edges)
    vertex=[]
    for i in range(0,len(file)):
        vertex.append(file[i,3])
    vertices=np.array(vertex) ##avg_G2 values
    #print(vertices[[edges[2][0]]])
    n_e=[]
    for j in range(0,len(edges)):
        new=min(vertices[edges[j][0]], vertices[edges[j][1]])
        n_e.append(new)
    new_vertex=np.array(n_e)
    particle_ids=edges.tolist()
    contact_force=new_vertex.tolist()
    # find the trivial loops
    trivialLoops = trivialTriangle(particle_ids, contact_force)
    
    # construct simplex trees
    contact_length = len(contact_force)
    loops_length = len(trivialLoops)
    
    st = gudhi.SimplexTree()
    for i in range(contact_length):
        st.insert(particle_ids[i], filtration = - contact_force[i])
            
    for i in range(loops_length):
        st.insert(trivialLoops[i][0:3], filtration = -trivialLoops[i][3])

    st.initialize_filtration()
    diag = st.persistence(11, 0.0, persistence_dim_max = True)
    #B0 = st.persistence_intervals_in_dimension(0)
    B1 = st.persistence_intervals_in_dimension(1)
    print(B1)

    
    st = gudhi.SimplexTree()
    for i in range(len(new_vertex)):
        st.insert([edges[i][0],edges[i][1]],filtration= - new_vertex[i])

    for j in range(len(trivial)):
        st.insert(trivial[j][0:3],filtration = - trivial[j][3])
    diag = st.persistence(11, 0.0, persistence_dim_max = True)
    print(diag)
    



