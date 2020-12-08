from Project.Shaft_Singularity_ver3 import StaticsEqns,sngabsmax,integratesng,sngvals
from scipy.optimize import fsolve
import numpy as np
import math

class Beam:

    def __init__(self, ):
        self.title = None
        self.dist_unit = None
        self.force_unit = None
        self.sut = None
        self.sy = None
        self.se = None
        self.e = None
        self.fatiguefactor = None
        self.staticfactor = None
        self.reliability = None
        self.temp = None
        self.stressconcentration = None
        self.length = None
        self.loads_y = []
        self.loads_z = []
        self.torque = []
        self.thrust = []
        self.width = []
        self.delta = []
        self.slope = []
        self.TR = []
        self.RR = []
        self.bearings = []
        self.diameter = []
        self.max=[]
        self.TB_loc=None
        self.RB_loc=None
        self.tor_list=[]
        self.ten_list=[]
        self.Vz=[]
        self.Vy=[]
        self.Mz=[]
        self.My=[]
        self.M=[]
        self.bend_stress=[]
        self.ax_stress=[]
        self.shear_stress=[]

    def processshaft(self, data):


        for line in data:  # loop over all the lines
            cells = line.strip().split(',')
            keyword = cells[0].lower()

            if keyword == 'title': self.title = cells[1].replace("'", "")
            if keyword == 'distance_unit': self.dist_unit = cells[1].replace("'", "")
            if keyword == 'force_unit': self.force_unit = cells[1].replace("'", "")
            if keyword == 'material':
                self.sut = float(cells[1])
                self.sy = float(cells[2])
                self.se = float(cells[3])
                self.e = float(cells[4])
            if keyword == 'fatigue_factor': self.fatiguefactor = float(cells[1])
            if keyword == 'static_factor':self.staticfactor = float(cells[1])
            if keyword == 'reliability': self.reliability = float(cells[1])
            if keyword == 'temperature': self.temp = float(cells[1])
            if keyword == 'stress_concentrations':self.stressconcentration = float(cells[1])
            if keyword == 'shaft_length': self.length = float(cells[1])

            if keyword == 'thrust_bearing':
                self.bearings.append([float(cells[1]), float(cells[2]), float(cells[3]), float(cells[4])])
                self.TB_loc=float(cells[2])
            if keyword == 'radial_bearing':
                self.bearings.append([float(cells[1]), float(cells[2]), float(cells[3]), float(cells[4])])
                self.RB_loc=float(cells[2])
            if keyword == 'diameters':
                this_vals = []
                for cell in cells[1:]:
                    value = float(cell.replace("(", "").replace(")", ""))
                    this_vals.append(value)
                # self.diameter.append(this_vals)
                for g in range (0,len(this_vals),2):
                    pair=[]
                    pair.append(this_vals[g]);pair.append(this_vals[g+1])
                    self.diameter.append(pair)

            if keyword == 'load':
                # for cell in cells[1:]:
                self.thrust.append([float(cells[1]), float(cells[9]), -1])
                self.loads_y.append([float(cells[2]), float(cells[9]), -1])
                if float(cells[5])!=0.0:
                    self.loads_y.append([float(cells[5]), float(cells[9]), -2])
                self.loads_z.append([float(cells[3]), float(cells[9]), -1])
                if float(cells[5]) != 0.0:
                    self.loads_z.append([float(cells[6]), float(cells[9]), -2])
                self.torque.append([float(cells[4]), float(cells[9]), -1])
                self.slope.append([float(cells[8])])
                self.delta.append([float(cells[7])])
                self.width.append([float(cells[9])])
        #find Reactions at the bearings

        new_y = []
        new_y.append([0, self.bearings[0][1], -1])
        new_y.append([0, self.bearings[1][1], -1])
        for i in range(len(self.loads_y)):
            new_y.append(self.loads_y[i])

        new_z = []
        new_z.append([0, self.bearings[0][1], -1])
        new_z.append([0, self.bearings[1][1], -1])
        for i in range(len(self.loads_z)):
            new_z.append(self.loads_z[i])


        ly = r1r2(new_y)
        lz = r1r2(new_z)
        self.loads_y=ly
        self.loads_z=lz
        self.TR.append(ly[0][0])
        self.TR.append(lz[0][0])
        self.RR.append(ly[1][0])
        self.RR.append(lz[1][0])

        val=0.0
        n=len(self.thrust)
        #create a singularity list of all thrust forces
        thrustloads = []
        for i in range(n):
            val += self.thrust[i][0]
            thrustloads.append(self.thrust[i])
        self.TR.append(-1*val)
        thrustloads.append([self.TR[2],self.TB_loc,-1])
        #find the maximum axial tension
        TenLoads=integratesng(thrustloads)
        maxten=sngabsmax(TenLoads,0,self.length)
        self.max.append(maxten[0]);self.max.append(maxten[1])
        #check to see if the torques balance
        diff=0
        for j in range (len(self.torque)):
            diff+=self.torque[j][0]
        if diff!=0:#if the torques do not ballance say that any remaining torque is removed at the end of the shaf
            self.torque.append([diff*-1,self.length-10**(-6),-1])
        ShaftTorque=integratesng(self.torque)
        #find the maximum torque
        maxtor=sngabsmax(ShaftTorque,0,self.length)
        self.max.append(maxtor[0]);self.max.append(maxtor[1])
        #obtain shear and moment singularities in the y and z direction
        Vy=integratesng(self.loads_y)
        Vz=integratesng(self.loads_z)
        My=integratesng(Vy)
        Mz=integratesng(Vz)
        X = np.linspace(0, self.length, 10001)
        self.My=sngvals(My,X)
        self.Mz = sngvals(Mz, X)
        #find the vector magnitude of all moments and the Max
        MaxM = 0
        MaxM_Loc=0
        for j in range(len(self.Mz)):
            newval=math.sqrt(self.Mz[j]**2+self.My[j]**2)
            self.M.append(newval)
            if self.M[j]>MaxM:
                MaxM=self.M[j]
                MaxM_Loc=X[j]
        self.max.append(MaxM);self.max.append(MaxM_Loc)
        self.ten_list=sngvals(TenLoads,X)
        self.tor_list=sngvals(ShaftTorque,X)

def r1r2(loads):
    r1,r2=0,0

    for i in range(2,len(loads)):
        if loads[i][2]==-1:
            r2 += loads[i][0]*(loads[i][1]-loads[0][1])
        elif loads[i][2]==-2:
            r2-=loads[i][0]
    loads[1][0]=-r2/(loads[1][1]-loads[0][1])

    for i in range(1,len(loads)):
        if loads[i][2]== -1:
            r1 += loads[i][0]

    loads[0][0]=-r1

    return loads
