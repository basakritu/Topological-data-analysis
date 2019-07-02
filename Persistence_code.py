import numpy as np
import math

savepath='G:/Research/'  #path for saving output
openpath='G:\\Research\\B0_persistence_diagrams\\'  #path for taking the files

numfiles=5  #number of files
for i in range(0,numfiles):
    if(i<10):
        Out_="Out_" #defining string
        n_ = "n_" #defining string for saving outout file name
        filename=openpath+Out_+str(i+1)+'_0.txt'
        #writefile= open(savepath + n_+str(i+1)+'.txt', 'w')
    #elif(i==10):
     #   Out_ = "Out_"
      #  n_ = "n_"
       # filename = openpath + Out_ + str(i) + '_0.txt'
        #writefile = open(savepath + n_ + str(i) + '.txt', 'w')
    elif(i>=10 and i<100):
        Out_ = "Out_"
        n_ = "n_"
        filename = openpath + Out_ + str(i+1) + '_0.txt'
        writefile = open(savepath + n_ + str(i+1) + '.txt', 'w')
    #elif(i==100):
     #   Out_ = "Out_"
      #  n_ = "n_"
       # filename = openpath + Out_ + str(i) + '_0.txt'
        #writefile = open(savepath + n_ + str(i) + '.txt', 'w')
    elif(i>=100 and i<1000):
        Out_ = "Out_"
        n_ = "n_"
        filename = openpath + Out_ + str(i+1) + '_0.txt'
        writefile = open(savepath + n_ + str(i+1) + '.txt', 'w')
    #elif(i==1000):
     #   Out_ = "Out_"
      #  n_ = "n_"
       # filename = openpath + Out_ + str(i) + '_0.txt'
        #writefile = open(savepath + n_ + str(i) + '.txt', 'w')
    elif(i>=1000 and i<10000):
        Out_ = "Out_"
        n_ = "n_"
        filename = openpath + Out_ + str(i+1) + '_0.txt'
        writefile = open(savepath + n_ + str(i+1) + '.txt', 'w')
    #elif(i==10000):
     #   Out_ = "Out_"
      #  n_ = "n_"
       # filename = openpath + Out_ + str(i) + '_0.txt'
        #writefile = open(savepath + n_ + str(i) + '.txt', 'w')
    elif(i>=10000 and i<300000):
        Out_ = "Out_"
        n_ = "n_"
        filename = openpath + Out_ + str(i+1) + '_0.txt'
        writefile = open(savepath + n_ + str(i+1) + '.txt', 'w')
    elif(i==300000):
        Out_ = "Out_"
        n_ = "n_"
        filename = openpath + Out_ + str(i+1) + '_0.txt'
        writefile = open(savepath + n_ + str(i+1) + '.txt', 'w')
    #i=i+1

    data = np.loadtxt(filename) #loading the data with numpy
    p=len(data) #size of the data
    #print(p)
    N = 5 #number of grid points
    count=0 #initialization for calculating the number of having(0,-1) points
    for j in range(0,p):
        if (data[j,0]== 0 and data[j,1]== -1):
            count=count+1 #; %count the number of cells in which (0,-1)\\n\",\n",
    n_p = p-count #calculating the size excluding (0,-1) coordinates
    cells = range(0, N) #defining the number of cells
    cellsize = .05/ math.sqrt(2) #size of the each cell
    CellIds = np.zeros((n_p, 2)) #initialization cellids
    x_cell = [] #making an array for x cordinates for each cell
    y_cell = [] #making an array for y cordinates for each cell
    for i in range(0, n_p):
        d_i = (np.absolute((data[i,0] - data[i,-1])) / math.sqrt(2))  # ; %distances to y=x\n",
        e_i = (np.absolute((data[i,-1] + data[i,0])) / math.sqrt(2))  # ; %distances to y=-x\n",
        xcell = math.ceil(d_i/cellsize)  #; % cell # from y=x\n",
        ycell = math.ceil(e_i/cellsize) #; % cell # from y=-x\n",
        CellIds[i][0] = xcell
        CellIds[i][1] = ycell   #;%number of cells\n",
        Xcell = x_cell.append(xcell) #combining all the x cords
        Ycell = y_cell.append(ycell) #combining all the y cords
    x=np.array(x_cell)
    y=np.array(y_cell)
    cell=[] #defining array for cellids
    for i in range(0,n_p):
        cell.append([x[i],y[i]])
    CellIds=np.array(cell)
    #print(CellIds)
    re=[]

    """"
    for i in range(0,n_p):
        if(data[i,0]<=0.01 and data[i,1] >= 0.01 or data[i,0]>=0.01 and data[i,1]<=0.01):
            re.append(i)
    near_Diag=np.array(re)
    print(near_Diag)
    """
#%% finding the total number of points in each cell\\n\",\n",
    cmax = 5 #size of number of rows
    P = np.zeros((1,2)) #initialization
    Counter = np.zeros((cmax,2*cmax)) #dimension of the matrix
    for i in range(0,n_p):
        P = CellIds[i,:]
        for j in range(0, 2*cmax):
            for k in range(j,cmax):

                if (P[0] == j+1 and P[1] == k+1):
                    Counter[j][k]= Counter[j][k] + 1  # ; %storing the number of points\\n\",\n",


    print(Counter)
    for i in range(0,9):
        C=Counter[1,i]
        #print(C)
