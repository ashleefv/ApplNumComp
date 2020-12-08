import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
from scipy.optimize import fsolve

def sng(x,a,power):

    if x<a:
        return 0
    if power==0:
        return 1
    if power>=1:
        return (x-a)**power
    else:
        return 0

def integratesng(snglist):

    Int=deepcopy(snglist)
    for i in range(len(snglist)):
        val,start,power=snglist[i]
        power+=1
        if power > 1:

            val=val/power
        Int[i]=[val,start,power]
    return Int

def sngval(snglist,x):
    sum=0
    for i in range(len(snglist)):
        sum +=snglist[i][0]*sng(x,snglist[i][1],snglist[i][2])
    return sum

def sngvals(snglist,x):
    y=np.zeros(len(x))

    for i in range(len(x)):
        y[i]=sngval(snglist,x[i])
    return y

def sngabsmax(snglist,x1,x2,npoints=10001):
    x=np.linspace(x1,x2,npoints)
    max=0
    max_x=0
    for xval in x:
        y=sngval(snglist,xval)
        if np.abs(y)>max:
            max=np.abs(y)
            max_x=xval

    return max,max_x

def scalesng(snglist,scale):
    for s in snglist:
        s[0]*=scale
    return snglist

def StaticsEqns(vals,loads,thrust_bearing,radial_bearing):#create the eqn's for fsolve to use to find R1 and R2
    R1,R2=vals
    vlist=integratesng(loads)
    mlist=integratesng(vlist)

    vlist[0][0]=R1; vlist[1][0]=R2
    mlist[0][0]=R1; mlist[1][0]=R2
    val2=sngval(vlist,thrust_bearing)#moment must be 0 @ x=support1
    val3=sngval(mlist,radial_bearing)#moment must be 0 @ x=support2
    return [val2,val3]


def HandyDandyBeamPlotter(Vs,Ms,Slopes,Deltas,x1,x2,C1,C2,
                          npoints=1000,show=True, save=False,
                          title="Beam1 Characteristics",
                          vtitle="Shear",mtitle="Moment",
                          slopetitle="EISlope", deltatitle="EIDelta"):

    X=np.linspace(x1+x2/10000.0,x2+x2/10000,1000)

    plt.rcParams["figure.figsize"] = [16,16]
    plt.rcParams.update({'font.size': 18})
    fig, axarr = plt.subplots(4, sharex=True)
    plt.suptitle(title,fontsize=36)
    fig.patch.set_facecolor('WhiteSmoke')

    Y=sngvals(Vs,X)
    axarr[0].plot(X,Y,linewidth=3)
    axarr[0].set_title(vtitle)
    axarr[0].locator_params(axis='y',nbins=2)

    Y=sngvals(Ms,X)
    axarr[1].plot(X,Y,linewidth=3)
    axarr[1].set_title(mtitle)
    axarr[1].locator_params(axis='y',nbins=2)

    Y=sngvals(Slopes,X,0,C1)
    axarr[2].plot(X,Y,linewidth=3)
    axarr[2].set_title(slopetitle)
    axarr[2].locator_params(axis='y',nbins=2)

    Y=sngvals(Deltas,X,C1,C2)
    axarr[3].plot(X,Y,linewidth=3)
    axarr[3].set_title(deltatitle)
    axarr[3].locator_params(axis='y',nbins=2)

    if show:
        plt.show()
    if save:
        fig.savefig(title+".pdf")

    return fig,plt

