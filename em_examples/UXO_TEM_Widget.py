import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
from SimPEG import mkvc
import scipy.optimize as op
from em_examples.Base import widgetify
from ipywidgets import interact,interactive, IntSlider, FloatSlider, FloatText, ToggleButtons, HBox
import matplotlib.pyplot as plt
from IPython.display import display
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



##############################################################################
#       DEFINE WIDGET CALL
##############################################################################

def ImageUXOWidget():

    Out = interactive(fcnImageUXOWidget,psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=400., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=300., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=1000., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            tn=IntSlider(min=1, max=11, value=1., step=1, continuous_update=False, description = "Time channel"))
    
    return Out









def ImageDataWidget(TxType):

    # TxType MUST be: "EM61", "TEMTADS" or "MPV"
    
    if TxType is "EM61":

        Out = interactive(fcnImageDataWidgetEM61,x0=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$x_{true}$"),\
            y0=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$y_{true}$"),\
            z0=FloatSlider(min=-2., max=-0.1, value=-0.5, step=0.05, continuous_update=False, description = "$z_{true}$"),\
            psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            tn=IntSlider(min=1, max=11, value=1., step=1, continuous_update=False, description = "Time channel"),\
            xTx=FloatSlider(min=-3., max=3., value=0., step=0.25, continuous_update=False, description = "X location"),\
            yTx=FloatSlider(min=-3., max=3., value=0., step=0.25, continuous_update=False, description = "Y location"))
    
    elif TxType is "TEMTADS":
        Out = interactive(fcnImageDataWidgetTEMTADS,x0=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$x_{true}$"),\
            y0=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$y_{true}$"),\
            z0=FloatSlider(min=-2., max=-0.1, value=-0.5, step=0.05, continuous_update=False, description = "$z_{true}$"),\
            psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            tn=IntSlider(min=1, max=11, value=1., step=1, continuous_update=False, description = "Time channel"),\
            xTx=FloatSlider(min=-3, max=3, value=0., step=0.25, continuous_update=False, description = "Tx x location"),\
            yTx=FloatSlider(min=-3, max=3, value=0., step=0.25, continuous_update=False, description = "Tx y location"))

    elif TxType is "MPV":
        Out = interactive(fcnImageDataWidgetMPV,x0=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$x_{true}$"),\
            y0=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$y_{true}$"),\
            z0=FloatSlider(min=-2., max=-0.1, value=-0.5, step=0.05, continuous_update=False, description = "$z_{true}$"),\
            psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            tn=IntSlider(min=1, max=11, value=1., step=1, continuous_update=False, description = "Time channel"),\
            xTx=FloatSlider(min=-3, max=3, value=0., step=0.25, continuous_update=False, description = "Tx x location"),\
            yTx=FloatSlider(min=-3, max=3, value=0., step=0.25, continuous_update=False, description = "Tx y location"),\
            dComp=ToggleButtons(options=['X','Y','Z'], description = "Data Component"))

    return Out





def InversionWidget(TxType):

    # TxType MUST be: "EM61", "TEMTADS" or "MPV"
    
    if TxType is "EM61":

        Out = interactive(fcnInversionWidgetEM61,xt=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$x_{true}$"),\
            yt=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$y_{true}$"),\
            zt=FloatSlider(min=-2., max=-0.1, value=-0.5, step=0.05, continuous_update=False, description = "$z_{true}$"),\
            psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=300., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=800., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            Dx=FloatSlider(min=1., max=6., value=4., step=0.1, continuous_update=False, description = "$D_x$"),\
            Dy=FloatSlider(min=1., max=6., value=4., step=0.1, continuous_update=False, description = "$D_y$"),\
            Nx=IntSlider(min=2, max=10, value=5, step=1, continuous_update=False, description = "$N_x$"),\
            Ny=IntSlider(min=2, max=10, value=10, step=1, continuous_update=False, description = "$N_y$"),\
            x0=FloatSlider(min=-3., max=3., value=0.2, step=0.1, continuous_update=False, description = "$x_0$"),\
            y0=FloatSlider(min=-3., max=3., value=-0.15, step=0.1, continuous_update=False, description = "$y_0$"),\
            z0=FloatSlider(min=-3., max=3., value=-0.8, step=0.1, continuous_update=False, description = "$z_0$"),\
            tn=IntSlider(min=1, max=11, value=1, step=1, continuous_update=False, description = "Time channel"))

    elif TxType is "TEMTADS":

        Out = interactive(fcnInversionWidgetTEMTADS,xt=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$x_{true}$"),\
            yt=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$y_{true}$"),\
            zt=FloatSlider(min=-2., max=-0.1, value=-0.5, step=0.05, continuous_update=False, description = "$z_{true}$"),\
            psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=300., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=800., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            Dx=FloatSlider(min=1., max=6., value=2., step=0.1, continuous_update=False, description = "$D_x$"),\
            Dy=FloatSlider(min=1., max=6., value=2., step=0.1, continuous_update=False, description = "$D_y$"),\
            Nx=IntSlider(min=2, max=10, value=3, step=1, continuous_update=False, description = "$N_x$"),\
            Ny=IntSlider(min=2, max=10, value=3, step=1, continuous_update=False, description = "$N_y$"),\
            x0=FloatSlider(min=-3., max=3., value=0.2, step=0.1, continuous_update=False, description = "$x_0$"),\
            y0=FloatSlider(min=-3., max=3., value=-0.15, step=0.1, continuous_update=False, description = "$y_0$"),\
            z0=FloatSlider(min=-3., max=3., value=-0.8, step=0.1, continuous_update=False, description = "$z_0$"),\
            tn=IntSlider(min=1, max=11, value=1, step=1, continuous_update=False, description = "Time channel"))

    elif TxType is "MPV":

        Out = interactive(fcnInversionWidgetMPV,xt=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$x_{true}$"),\
            yt=FloatSlider(min=-2., max=2., value=0., step=0.05, continuous_update=False, description = "$y_{true}$"),\
            zt=FloatSlider(min=-2., max=-0.1, value=-0.5, step=0.05, continuous_update=False, description = "$z_{true}$"),\
            psi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\psi$"),\
            theta=FloatSlider(min=0, max=180., value=-0., step=10., continuous_update=False, description = "$\\theta$"),\
            phi=FloatSlider(min=-180., max=180., value=-0., step=10., continuous_update=False, description = "$\phi$"),\
            k1=FloatSlider(min=100., max=1000., value=300., step=10., continuous_update=False, description = "$k_{x'}$"),\
            alpha1=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{x'}$"),\
            beta1=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{x'}$"),\
            gamma1=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{x'}$)"),\
            k2=FloatSlider(min=100., max=1000., value=500., step=10., continuous_update=False, description = "$k_{y'}$"),\
            alpha2=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{y'}$"),\
            beta2=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{y'}$"),\
            gamma2=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{y'}$)"),\
            k3=FloatSlider(min=100., max=1000., value=800., step=10., continuous_update=False, description = "$k_{z'}$"),\
            alpha3=FloatSlider(min=1., max=2., value=1.4, step=0.1, continuous_update=False, description = "$\\alpha_{z'}$"),\
            beta3=FloatSlider(min=1., max=1.5, value=1.3, step=0.1, continuous_update=False, description = "$\\beta_{z'}$"),\
            gamma3=FloatSlider(min=-4., max=-2., value=-3., step=0.1, continuous_update=False, description = "log($\gamma_{z'}$)"),\
            Dx=FloatSlider(min=1., max=6., value=4., step=0.1, continuous_update=False, description = "$D_x$"),\
            Dy=FloatSlider(min=1., max=6., value=4., step=0.1, continuous_update=False, description = "$D_y$"),\
            Nx=IntSlider(min=2, max=10, value=5, step=1, continuous_update=False, description = "$N_x$"),\
            Ny=IntSlider(min=2, max=10, value=5, step=1, continuous_update=False, description = "$N_y$"),\
            x0=FloatSlider(min=-3., max=3., value=0.2, step=0.1, continuous_update=False, description = "$x_0$"),\
            y0=FloatSlider(min=-3., max=3., value=-0.15, step=0.1, continuous_update=False, description = "$y_0$"),\
            z0=FloatSlider(min=-3., max=3., value=-0.8, step=0.1, continuous_update=False, description = "$z_0$"),\
            tn=IntSlider(min=1, max=11, value=1, step=1, continuous_update=False, description = "Time channel"),\
            dComp=ToggleButtons(options=['X','Y','Z'], description = "Data Component"))

    return Out










##############################################################################
#       DEFINE WIDGET
##############################################################################

##############################
#   IMAGE WIDGET

def fcnImageUXOWidget(psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,tn):

    r0 = np.r_[0.,0.,0.]
    phi = np.r_[psi,theta,phi]
    times = times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I= 1.

    uxoObj = EM61problem(r0,phi,L,times,I)
    A = uxoObj.computeRotMatrix()

    k = tn + np.r_[-1,10,21]
    Lmax = np.max(uxoObj.L[k])
    Lx = (uxoObj.L[k[0]]/Lmax)**1.5
    Ly = (uxoObj.L[k[1]]/Lmax)**1.5
    Lz = (uxoObj.L[k[2]]/Lmax)**1.5

    wsb = np.dot(A,np.r_[-Lx,-Ly,-Lz])
    esb = np.dot(A,np.r_[Lx,-Ly,-Lz])
    wnb = np.dot(A,np.r_[-Lx,Ly,-Lz])
    enb = np.dot(A,np.r_[Lx,Ly,-Lz])
    wst = np.dot(A,np.r_[-Lx,-Ly,Lz])
    est = np.dot(A,np.r_[Lx,-Ly,Lz])
    wnt = np.dot(A,np.r_[-Lx,Ly,Lz])
    ent = np.dot(A,np.r_[Lx,Ly,Lz])

    x1 = 2*np.dot(A,np.r_[1.,0.,0.])
    x2 = 2*np.dot(A,np.r_[1.,0.,0.])
    y1 = 2*np.dot(A,np.r_[0.,1.,0.])
    y2 = 2*np.dot(A,np.r_[0.,1.,0.])
    z1 = 2*np.dot(A,np.r_[0.,0.,1.])
    z2 = 2*np.dot(A,np.r_[0.,0.,1.])

    # UXO polygons
    v1 = [zip([wsb[0],esb[0],enb[0],wnb[0]],[wsb[1],esb[1],enb[1],wnb[1]],[wsb[2],esb[2],enb[2],wnb[2]])]
    v2 = [zip([wst[0],est[0],ent[0],wnt[0]],[wst[1],est[1],ent[1],wnt[1]],[wst[2],est[2],ent[2],wnt[2]])]
    v3 = [zip([wsb[0],esb[0],est[0],wst[0]],[wsb[1],esb[1],est[1],wst[1]],[wsb[2],esb[2],est[2],wst[2]])]
    v4 = [zip([wnb[0],enb[0],ent[0],wnt[0]],[wnb[1],enb[1],ent[1],wnt[1]],[wnb[2],enb[2],ent[2],wnt[2]])]
    v5 = [zip([wsb[0],wnb[0],wnt[0],wst[0]],[wsb[1],wnb[1],wnt[1],wst[1]],[wsb[2],wnb[2],wnt[2],wst[2]])]
    v6 = [zip([esb[0],enb[0],ent[0],est[0]],[esb[1],enb[1],ent[1],est[1]],[esb[2],enb[2],ent[2],est[2]])]

    # Shadow polygons
    v7 = [zip([wsb[0],esb[0],enb[0],wnb[0]],[wsb[1],esb[1],enb[1],wnb[1]],[-2.5,-2.5,-2.5,-2.5])]
    v8 = [zip([wst[0],est[0],ent[0],wnt[0]],[wst[1],est[1],ent[1],wnt[1]],[-2.5,-2.5,-2.5,-2.5])]
    v9 = [zip([wsb[0],esb[0],est[0],wst[0]],[wsb[1],esb[1],est[1],wst[1]],[-2.5,-2.5,-2.5,-2.5])]
    v10= [zip([wnb[0],enb[0],ent[0],wnt[0]],[wnb[1],enb[1],ent[1],wnt[1]],[-2.5,-2.5,-2.5,-2.5])]
    v11= [zip([wsb[0],wnb[0],wnt[0],wst[0]],[wsb[1],wnb[1],wnt[1],wst[1]],[-2.5,-2.5,-2.5,-2.5])]
    v12= [zip([esb[0],enb[0],ent[0],est[0]],[esb[1],enb[1],ent[1],est[1]],[-2.5,-2.5,-2.5,-2.5])]

    # PLOTTING

    Fig = plt.figure(figsize=(14,6))
    Ax1 = Fig.add_axes([0,0,0.47,1], projection='3d')
    Ax2 = Fig.add_axes([0.63,0.1,0.37,0.8])
    FS = 20

    # Orientation plot
    Ax1.add_collection3d(Poly3DCollection(v1,facecolors='k', linewidths=0.25, edgecolors='k'))
    Ax1.add_collection3d(Poly3DCollection(v2,facecolors='k', linewidths=0.25, edgecolors='k'))
    Ax1.add_collection3d(Poly3DCollection(v3,facecolors='r', linewidths=0.25, edgecolors='k'))
    Ax1.add_collection3d(Poly3DCollection(v4,facecolors='r', linewidths=0.25, edgecolors='k'))
    Ax1.add_collection3d(Poly3DCollection(v5,facecolors='b', linewidths=0.25, edgecolors='k'))
    Ax1.add_collection3d(Poly3DCollection(v6,facecolors='b', linewidths=0.25, edgecolors='k'))

    Ax1.add_collection3d(Poly3DCollection(v7,facecolors=(0.7,0.7,0.7), linewidths=0.25))
    Ax1.add_collection3d(Poly3DCollection(v8,facecolors=(0.7,0.7,0.7), linewidths=0.25))
    Ax1.add_collection3d(Poly3DCollection(v9,facecolors=(0.7,0.7,0.7), linewidths=0.25))
    Ax1.add_collection3d(Poly3DCollection(v10,facecolors=(0.7,0.7,0.7), linewidths=0.25))
    Ax1.add_collection3d(Poly3DCollection(v11,facecolors=(0.7,0.7,0.7), linewidths=0.25))
    Ax1.add_collection3d(Poly3DCollection(v12,facecolors=(0.7,0.7,0.7), linewidths=0.25))

    Ax1.set_xticks([-2,-1,0,1,2])
    Ax1.set_yticks([-2,-1,0,1,2])
    Ax1.set_zticks([-2,-1,0,1,2])

    Ax1.set_xbound(-2.5,2.5)
    Ax1.set_ybound(-2.5,2.5)
    Ax1.set_zbound(-2.5,2.5)

    Ax1.tick_params(labelsize=FS-2)
    Ax1.set_xlabel('Easting',fontsize=FS,labelpad=11)
    Ax1.set_ylabel('Northing',fontsize=FS,labelpad=11)
    Ax1.set_zlabel('Z',fontsize=FS)

    Ax1.view_init(30.,225.)

    # Decay plot
    Lxt = uxoObj.L[0:11]
    Lyt = uxoObj.L[11:22]
    Lzt = uxoObj.L[22:33]

    Ax2.loglog(uxoObj.times,Lxt,lw=2,color='b')
    Ax2.loglog(uxoObj.times,Lyt,lw=2,color='r')
    Ax2.loglog(uxoObj.times,Lzt,lw=2,color='k')

    Ax2.set_xlabel('t [s]',fontsize=FS)
    Ax2.set_ylabel('Polarization',fontsize=FS)
    Ax2.tick_params(labelsize=FS-2)

    Ax2.set_xbound(np.min(uxoObj.times),np.max(uxoObj.times))
    Ax2.set_ybound(1e-4*np.max(uxoObj.L),1.2*np.max(uxoObj.L))
    Ax2.text(1.2e-4,7e-4*np.max(uxoObj.L),"$\mathbf{L_{x'}}$",fontsize=FS,color='b')
    Ax2.text(1.2e-4,3e-4*np.max(uxoObj.L),"$\mathbf{L_{y'}}$",fontsize=FS,color='r')
    Ax2.text(1.2e-4,1.3e-4*np.max(uxoObj.L),"$\mathbf{L_{z'}}$",fontsize=FS,color='k')


    plt.show(Fig)










######################################
# PREDICT DATA WIDGET

def fcnImageDataWidgetEM61(x0,y0,z0,psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,tn,xTx,yTx):

    # SET PROPERTIES OF UXO INSTANCE
    r0 = np.r_[x0,y0,z0]
    phi = np.r_[psi,theta,phi]
    times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I = 100.

    uxoObj = EM61problem(r0,phi,L,times,I)
    N = 25
    X,Y = np.meshgrid(np.linspace(-3.,3.,N),np.linspace(-3.,3.,N))
    XYZ = np.c_[mkvc(X),mkvc(Y),0.1*np.ones(np.size(X))]

    # PREDICT DATA
    uxoObj.defineSensorLoc(XYZ)
    A = uxoObj.computeRotMatrix()
    Hp = uxoObj.computeHp()
    Brx = uxoObj.computeBrx()
    P = uxoObj.computeP(Hp,Brx)
    q = uxoObj.computePolarVecs()
    data = np.dot(P,q)

    # PLOTTING

    Fig = plt.figure(figsize=(13.5,5.3))
    Ax1 = Fig.add_axes([0,0,0.47,1])
    Ax2 = Fig.add_axes([0.63,0,0.37,1])
    FS = 18

    # Anomaly

    d_tn = 1e3*np.reshape(data[:,tn-1],(N,N))  # 1e3 for mV
    Cplot = Ax1.contourf(X,Y,d_tn.T,40,cmap='viridis')
    cbar = plt.colorbar(Cplot, ax=Ax1, pad=0.02, format='%.2e')
    cbar.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar.ax.tick_params(labelsize=FS-2)

    Ax1.set_xlabel('X [m]',fontsize=FS)
    Ax1.set_ylabel('Y [m]',fontsize=FS)
    Ax1.tick_params(labelsize=FS-2)

    titlestr1 = "Anomaly at t = " + '{:.3e}'.format(uxoObj.times[tn-1]) + " s"
    Ax1.set_title(titlestr1,fontsize=FS+2)
    Ax1.scatter(X,Y,color=(1,1,1),s=3)

    i = int(np.round((3+xTx)/0.25))
    j = int(np.round((3+yTx)/0.25))
    Ax1.scatter(X[j,i],Y[j,i],color=(1,0,0),s=15)

    Ax1.set_xbound(-3.,3.)
    Ax1.set_ybound(-3.,3.)
    

    # Decay

    d_ij = 1e3*np.abs(data[25*i+j,:]) # 1e3 for mV
    Ax2.loglog(uxoObj.times,d_ij,color='k')

    Ax2.set_xlabel('t [s]',fontsize=FS)
    Ax2.set_ylabel('|dB/dt| Field [mV]',fontsize=FS)
    Ax2.tick_params(labelsize=FS-2)

    Ax2.set_xbound(np.min(uxoObj.times),np.max(uxoObj.times))
    Ax2.set_ybound(1.2*np.max(d_ij),1e-4*np.max(d_ij))
    titlestr2 = "Decay at X = " + '{:.2f}'.format(xTx) + " m and Y = " + '{:.2f}'.format(yTx) + " m"
    Ax2.set_title(titlestr2,fontsize=FS+2)
    Ax2.text(1.2e-4,1.3e-4*np.max(d_ij),"$\mathbf{dBz/dt}$",fontsize=FS,color='k')

    plt.show(Fig)







def fcnImageDataWidgetTEMTADS(x0,y0,z0,psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,tn,xTx,yTx):

    # SET PROPERTIES OF UXO INSTANCE
    r0 = np.r_[x0,y0,z0]
    phi = np.r_[psi,theta,phi]
    times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I = 100.

    uxoObj = TEMTADSproblem(r0,phi,L,times,I)
    N = 25
    X,Y = np.meshgrid(np.linspace(-3.,3.,N),np.linspace(-3.,3.,N))
    XYZ = np.c_[mkvc(X),mkvc(Y),0.1*np.ones(np.size(X))]

    # PREDICT DATA
    uxoObj.defineSensorLoc(XYZ)
    A = uxoObj.computeRotMatrix()
    Hp = uxoObj.computeHp()
    Brx = uxoObj.computeBrx()
    P = uxoObj.computeP(Hp,Brx)
    q = uxoObj.computePolarVecs()
    data = np.dot(P,q)

    # PLOTTING

    Fig = plt.figure(figsize=(13.5,5.3))
    Ax1 = Fig.add_axes([0,0,0.47,1])
    Ax2 = Fig.add_axes([0.63,0,0.37,1])
    FS = 18

    # Anomaly
    di = np.reshape(data[12:25*N**2:25,tn-1],(N,N))
    Cplot = Ax1.contourf(X,Y,di.T,40,cmap='viridis')
    cbar = plt.colorbar(Cplot, ax=Ax1, pad=0.02)
    cbar.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar.ax.tick_params(labelsize=FS-2)

    Ax1.set_xlabel('X [m]',fontsize=FS)
    Ax1.set_ylabel('Y [m]',fontsize=FS)
    Ax1.tick_params(labelsize=FS-2)

    Ax1.scatter(X,Y,color=(1,1,1),s=2)

    titlestr1 = "Anomaly at t = " + '{:.3e}'.format(uxoObj.times[tn-1]) + " s"
    Ax1.set_title(titlestr1,fontsize=FS+2)

    i = int(np.round((3+xTx)/0.25))
    j = int(np.round((3+yTx)/0.25))
    Ax1.scatter(X[j,i],Y[j,i],color=(1,0,0),s=15)

    Ax1.set_xbound(-3.,3.)
    Ax1.set_ybound(-3.,3.)
    
    # Decay
    d_ij = 1e3*np.abs(data[i*25**2+j*25:i*25**2+(j+1)*25,:]) # 1e3 for mV
    Ax2.loglog(uxoObj.times,d_ij.T,color='k')

    Ax2.set_xlabel('t [s]',fontsize=FS)
    Ax2.set_ylabel('|dB/dt| Field [mV]',fontsize=FS)
    Ax2.tick_params(labelsize=FS-2)

    Ax2.set_xbound(np.min(uxoObj.times),np.max(uxoObj.times))
    Ax2.set_ybound(1.2*np.max(d_ij),1e-4*np.max(d_ij))
    titlestr2 = "Decays at X = " + '{:.2f}'.format(xTx) + " m and Y = " + '{:.2f}'.format(yTx) + " m"
    Ax2.set_title(titlestr2,fontsize=FS+2)
    Ax2.text(1.2e-4,1.3e-4*np.max(d_ij),"$\mathbf{dBz/dt}$",fontsize=FS,color='k')

    plt.show(Fig)








def fcnImageDataWidgetMPV(x0,y0,z0,psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,tn,xTx,yTx,dComp):

    # SET PROPERTIES OF UXO INSTANCE
    r0 = np.r_[x0,y0,z0]
    phi = np.r_[psi,theta,phi]
    times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I = 100.

    uxoObj = MPVproblem(r0,phi,L,times,I)
    N = 25
    X,Y = np.meshgrid(np.linspace(-3.,3.,N),np.linspace(-3.,3.,N))
    XYZ = np.c_[mkvc(X),mkvc(Y),0.1*np.ones(np.size(X))]

    # PREDICT DATA
    uxoObj.defineSensorLoc(XYZ)
    A = uxoObj.computeRotMatrix()
    Hp = uxoObj.computeHp()
    Brx = uxoObj.computeBrx()
    P = uxoObj.computeP(Hp,Brx)
    q = uxoObj.computePolarVecs()
    data = np.dot(P,q)

    # PLOTTING

    Fig = plt.figure(figsize=(13.5,5.3))
    Ax1 = Fig.add_axes([0,0,0.47,1])
    Ax2 = Fig.add_axes([0.63,0,0.37,1])
    FS = 18

    # Anomaly
    titlestr1 = "Anomaly at t = " + '{:.3e}'.format(uxoObj.times[tn-1]) + " s"

    if dComp is 'X':
        k=0
    elif dComp is 'Y':
        k=1
    elif dComp is 'Z':
        k=2

    di = np.reshape(data[6+k:15*N**2:15,tn-1],(N,N))
    Cplot = Ax1.contourf(X,Y,di.T,40,cmap='viridis')
    cbar = plt.colorbar(Cplot, ax=Ax1, pad=0.02)

    if dComp is 'X':
        cbar.set_label('dBx/dt [mV]', rotation=270, labelpad = 25, size=FS)
    elif dComp is 'Y':
        cbar.set_label('dBy/dt [mV]', rotation=270, labelpad = 25, size=FS)
    elif dComp is 'Z':
        cbar.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar.ax.tick_params(labelsize=FS-2)

    Ax1.set_xlabel('X [m]',fontsize=FS)
    Ax1.set_ylabel('Y [m]',fontsize=FS)
    Ax1.tick_params(labelsize=FS-2)

    Ax1.scatter(X,Y,color=(1,1,1),s=2)

    Ax1.set_title(titlestr1,fontsize=FS+2)

    i = int(np.round((3+xTx)/0.25))
    j = int(np.round((3+yTx)/0.25))
    Ax1.scatter(X[j,i],Y[j,i],color=(1,0,0),s=15)

    Ax1.set_xbound(-3.,3.)
    Ax1.set_ybound(-3.,3.)
    
    # Decay
    d_ijx = 1e3*np.abs(data[i*15*25+j*15:i*15*25+(j+1)*15:3,:]) # 1e3 for mV
    d_ijy = 1e3*np.abs(data[1+i*15*25+j*15:i*15*25+(j+1)*15:3,:]) # 1e3 for mV
    d_ijz = 1e3*np.abs(data[2+i*15*25+j*15:i*15*25+(j+1)*15:3,:]) # 1e3 for mV
    maxdij = np.max(np.r_[d_ijx,d_ijy,d_ijz])
    Ax2.loglog(uxoObj.times,d_ijx.T,color='b')
    Ax2.loglog(uxoObj.times,d_ijy.T,color='r')
    Ax2.loglog(uxoObj.times,d_ijz.T,color='k')

    Ax2.set_xlabel('t [s]',fontsize=FS)
    Ax2.set_ylabel('|dB/dt| Field [mV]',fontsize=FS)
    Ax2.tick_params(labelsize=FS-2)

    Ax2.set_xbound(np.min(uxoObj.times),np.max(uxoObj.times))
    Ax2.set_ybound(1.2*maxdij,1e-4*maxdij)
    titlestr2 = "Decays at X = " + '{:.2f}'.format(xTx) + " m and Y = " + '{:.2f}'.format(yTx) + " m"
    Ax2.set_title(titlestr2,fontsize=FS+2)
    Ax2.text(1.2e-4,7e-4*maxdij,"$\mathbf{dBx/dt}$",fontsize=FS,color='b')
    Ax2.text(1.2e-4,3e-4*maxdij,"$\mathbf{dBy/dt}$",fontsize=FS,color='r')
    Ax2.text(1.2e-4,1.3e-4*maxdij,"$\mathbf{dBz/dt}$",fontsize=FS,color='k')

    plt.show(Fig)


##################################
# INVERSION WIDGET

def fcnInversionWidgetEM61(xt,yt,zt,psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,Dx,Dy,Nx,Ny,x0,y0,z0,tn):

    # SET TRUE UXO PROPERTIES
    rt = np.r_[xt,yt,zt]
    phi = np.r_[psi,theta,phi]
    times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I = 100.

    # PREDICT TRUE ANOMALY
    uxoObj1 = EM61problem(rt,phi,L,times,I)
    N = 25
    X1,Y1 = np.meshgrid(np.linspace(-3.,3.,N),np.linspace(-3.,3.,N))
    XYZ1 = np.c_[mkvc(X1),mkvc(Y1),0.1*np.ones(np.size(X1))]
    uxoObj1.defineSensorLoc(XYZ1)
    A = uxoObj1.computeRotMatrix()
    Hp = uxoObj1.computeHp()
    Brx = uxoObj1.computeBrx()
    P1 = uxoObj1.computeP(Hp,Brx)
    q = uxoObj1.computePolarVecs()
    da_true = np.dot(P1,q)

    # PREDICT TRUE DATA
    uxoObj2 = EM61problem(rt,phi,L,times,I)
    X2,Y2 = np.meshgrid(np.linspace(-Dx/2,Dx/2,Nx),np.linspace(-Dy/2,Dy/2,Ny))
    XYZ2 = np.c_[mkvc(X2),mkvc(Y2),0.1*np.ones(np.size(X2))]
    uxoObj2.defineSensorLoc(XYZ2)
    A = uxoObj2.computeRotMatrix()
    Hp = uxoObj2.computeHp()
    Brx = uxoObj2.computeBrx()
    P2 = uxoObj2.computeP(Hp,Brx)
    q = uxoObj2.computePolarVecs()
    data = np.dot(P2,q)
    [dobs,dunc] = uxoObj2.get_dobs_dunc(data,1e-5,0.05)

    # SOLVE INVERSE PROBLEM
    Misfit = np.inf
    dMis = np.inf
    rn = np.r_[x0,y0,z0]
    
    uxoObj2.updatePolarizations(rn)
    Misfit = uxoObj2.computeMisfit(rn)
    
    COUNT = 0
    m_vec = []
    
    while Misfit > 1.001 and COUNT < 100 and dMis > 1e-5:
       
       MisPrev = Misfit
       
       rn,Sol = uxoObj2.updateLocation(rn)
       
       uxoObj2.updatePolarizations(rn)
       
       Misfit = uxoObj2.computeMisfit(rn)
       dMis = np.abs(MisPrev - Misfit)
       m_vec.append(Misfit)
       
       COUNT = COUNT + 1

    q = uxoObj2.q
    Ln = np.zeros((3,len(uxoObj2.times)))
    m_vec = np.array(m_vec)

    for pp in range(0,len(uxoObj2.times)):
        Q = np.r_[np.c_[q[0,pp],q[1,pp],q[2,pp]],np.c_[q[1,pp],q[3,pp],q[4,pp]],np.c_[q[2,pp],q[4,pp],q[5,pp]]]
        [qval,qvec] = np.linalg.eigh(Q)
        Ln[:,pp] = qval

    # PREDICT ANOMALY
    da_pre = np.dot(P1,q)


    # PLOTTING

    Fig = plt.figure(figsize=(13.5,8.5))
    Ax11 = Fig.add_axes([0,0.55,0.35,0.45])
    Ax12 = Fig.add_axes([0.5,0.55,0.35,0.45])
    Ax21 = Fig.add_axes([0.,0.,0.4,0.45])
    Ax22 = Fig.add_axes([0.5,0.,0.4,0.45])
    FS = 18

    # True Anomaly
    d11 = 1e3*np.reshape(da_true[:,tn-1],(N,N))  # 1e3 for mV
    Cplot1 = Ax11.contourf(X1,Y1,d11.T,40,cmap='viridis')
    cbar1 = plt.colorbar(Cplot1, ax=Ax11, pad=0.02, format='%.2e')
    cbar1.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar1.ax.tick_params(labelsize=FS-2)

    Ax11.set_xlabel('X [m]',fontsize=FS)
    Ax11.set_ylabel('Y [m]',fontsize=FS)
    Ax11.tick_params(labelsize=FS-2)

    titlestr1 = "Observed at t = " + '{:.3e}'.format(uxoObj1.times[tn-1]) + " s"
    Ax11.set_title(titlestr1,fontsize=FS+2)
    Xn,Yn = np.meshgrid(np.linspace(-Dx/2,Dx/2,Nx),np.linspace(-Dy/2,Dy/2,Ny))
    Ax11.scatter(Xn,Yn,color=(1,1,1),s=3)

    Ax11.set_xbound(-3.,3.)
    Ax11.set_ybound(-3.,3.)
    
    # Predicted Anomaly
    d12 = 1e3*np.reshape(da_pre[:,tn-1],(N,N))  # 1e3 for mV
    Cplot2 = Ax12.contourf(X1,Y1,d12.T,40,cmap='viridis')
    cbar2 = plt.colorbar(Cplot2, ax=Ax12, pad=0.02, format='%.2e')
    cbar2.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar2.ax.tick_params(labelsize=FS-2)

    Ax12.set_xlabel('X [m]',fontsize=FS)
    Ax12.set_ylabel('Y [m]',fontsize=FS)
    Ax12.tick_params(labelsize=FS-2)

    titlestr2 = "Predicted at t = " + '{:.3e}'.format(uxoObj1.times[tn-1]) + " s"
    Ax12.set_title(titlestr2,fontsize=FS+2)
    # Ax12.scatter(X,Y,color=(1,1,1),s=3)

    Ax12.set_xbound(-3.,3.)
    Ax12.set_ybound(-3.,3.)

    

    # CONVERGENCE AND PRINTOUT
    Ax21.plot(np.arange(1,len(m_vec)+1),np.ones(len(m_vec)),lw=3,color='k',ls=':')
    Ax21.plot(np.arange(1,len(m_vec)+1),m_vec,lw=2,color=(1,0,0))
    Ax21.set_xbound(1,len(m_vec))
    Ax21.set_ybound(0,np.max(m_vec))
    Ax21.set_xlabel('Count',fontsize=FS)
    Ax21.set_ylabel('$\chi^2$ Misfit',fontsize=FS)
    Ax21.tick_params(labelsize=FS-2)

    rt_str = "$r_{true}$ = (" + '{:.2f}'.format(rt[0]) + "," + '{:.2f}'.format(rt[1]) + "," + '{:.2f}'.format(rt[2]) + ")"
    rn_str = "$r_{rec}$  = (" + '{:.2f}'.format(rn[0]) + "," + '{:.2f}'.format(rn[1]) + "," + '{:.2f}'.format(rn[2]) + ")"
    fm_str = "Final Misfit = " + '{:.2f}'.format(m_vec[-1])
    Ax21.text(0.4*len(m_vec),0.92*m_vec[0],rt_str,fontsize=FS)
    Ax21.text(0.4*len(m_vec),0.83*m_vec[0],rn_str,fontsize=FS)
    Ax21.text(0.4*len(m_vec),0.74*m_vec[0],fm_str,fontsize=FS)

    # POLARIATIONS
    Lxt = uxoObj1.L[0:11]
    Lyt = uxoObj1.L[11:22]
    Lzt = uxoObj1.L[22:33]
    Lxn = Ln[0,:].T
    Lyn = Ln[1,:].T
    Lzn = Ln[2,:].T
    maxLtn = np.max([np.max(uxoObj1.L),np.max(Ln)])

    Ax22.loglog(uxoObj1.times,Lxt,lw=2,color='b')
    Ax22.loglog(uxoObj1.times,Lyt,lw=2,color='r')
    Ax22.loglog(uxoObj1.times,Lzt,lw=2,color='k')
    Ax22.loglog(uxoObj1.times,Lxn,lw=2,color='b',ls=':')
    Ax22.loglog(uxoObj1.times,Lyn,lw=2,color='r',ls=':')
    Ax22.loglog(uxoObj1.times,Lzn,lw=2,color='k',ls=':')

    Ax22.set_xlabel('t [s]',fontsize=FS)
    Ax22.set_ylabel('Polarization',fontsize=FS)
    Ax22.tick_params(labelsize=FS-2)

    Ax22.set_xbound(np.min(uxoObj1.times),np.max(uxoObj1.times))
    Ax22.set_ybound(1e-4*maxLtn,1.2*maxLtn)
    Ax22.text(1.2e-4,7e-4*maxLtn,"$\mathbf{L_{x'}}$",fontsize=FS,color='b')
    Ax22.text(1.2e-4,3e-4*maxLtn,"$\mathbf{L_{y'}}$",fontsize=FS,color='r')
    Ax22.text(1.2e-4,1.3e-4*maxLtn,"$\mathbf{L_{z'}}$",fontsize=FS,color='k')


    plt.show(Fig)


def fcnInversionWidgetTEMTADS(xt,yt,zt,psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,Dx,Dy,Nx,Ny,x0,y0,z0,tn):

    # SET TRUE UXO PROPERTIES
    rt = np.r_[xt,yt,zt]
    phi = np.r_[psi,theta,phi]
    times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I = 100.

    # PREDICT TRUE ANOMALY
    uxoObj1 = TEMTADSproblem(rt,phi,L,times,I)
    N = 25
    X1,Y1 = np.meshgrid(np.linspace(-3.,3.,N),np.linspace(-3.,3.,N))
    XYZ1 = np.c_[mkvc(X1),mkvc(Y1),0.1*np.ones(np.size(X1))]
    uxoObj1.defineSensorLoc(XYZ1)
    A = uxoObj1.computeRotMatrix()
    Hp = uxoObj1.computeHp()
    Brx = uxoObj1.computeBrx()
    P1 = uxoObj1.computeP(Hp,Brx)
    q = uxoObj1.computePolarVecs()
    da_true = np.dot(P1,q)

    # PREDICT TRUE DATA
    uxoObj2 = TEMTADSproblem(rt,phi,L,times,I)
    X2,Y2 = np.meshgrid(np.linspace(-Dx/2,Dx/2,Nx),np.linspace(-Dy/2,Dy/2,Ny))
    XYZ2 = np.c_[mkvc(X2),mkvc(Y2),0.1*np.ones(np.size(X2))]
    uxoObj2.defineSensorLoc(XYZ2)
    A = uxoObj2.computeRotMatrix()
    Hp = uxoObj2.computeHp()
    Brx = uxoObj2.computeBrx()
    P2 = uxoObj2.computeP(Hp,Brx)
    q = uxoObj2.computePolarVecs()
    data = np.dot(P2,q)
    [dobs,dunc] = uxoObj2.get_dobs_dunc(data,1e-5,0.05)

    # SOLVE INVERSE PROBLEM
    Misfit = np.inf
    dMis = np.inf
    rn = np.r_[x0,y0,z0]
    
    uxoObj2.updatePolarizations(rn)
    Misfit = uxoObj2.computeMisfit(rn)
    
    COUNT = 0
    m_vec = []
    
    while Misfit > 1.001 and COUNT < 100 and dMis > 1e-5:
       
       MisPrev = Misfit
       
       rn,Sol = uxoObj2.updateLocation(rn)
       
       uxoObj2.updatePolarizations(rn)
       
       Misfit = uxoObj2.computeMisfit(rn)
       dMis = np.abs(MisPrev - Misfit)
       m_vec.append(Misfit)
       
       COUNT = COUNT + 1

    q = uxoObj2.q
    Ln = np.zeros((3,len(uxoObj2.times)))
    m_vec = np.array(m_vec)

    for pp in range(0,len(uxoObj2.times)):
        Q = np.r_[np.c_[q[0,pp],q[1,pp],q[2,pp]],np.c_[q[1,pp],q[3,pp],q[4,pp]],np.c_[q[2,pp],q[4,pp],q[5,pp]]]
        [qval,qvec] = np.linalg.eigh(Q)
        Ln[:,pp] = qval

    # PREDICT ANOMALY
    da_pre = np.dot(P1,q)


    # PLOTTING

    Fig = plt.figure(figsize=(13.5,8.5))
    Ax11 = Fig.add_axes([0,0.55,0.35,0.45])
    Ax12 = Fig.add_axes([0.5,0.55,0.35,0.45])
    Ax21 = Fig.add_axes([0.,0.,0.4,0.45])
    Ax22 = Fig.add_axes([0.5,0.,0.4,0.45])
    FS = 18

    # True Anomaly
    d11 = 1e3*np.reshape(da_true[12:25*N**2:25,tn-1],(N,N))  # 1e3 for mV
    Cplot1 = Ax11.contourf(X1,Y1,d11.T,40,cmap='viridis')
    cbar1 = plt.colorbar(Cplot1, ax=Ax11, pad=0.02, format='%.2e')
    cbar1.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar1.ax.tick_params(labelsize=FS-2)

    Ax11.set_xlabel('X [m]',fontsize=FS)
    Ax11.set_ylabel('Y [m]',fontsize=FS)
    Ax11.tick_params(labelsize=FS-2)

    titlestr1 = "Observed at t = " + '{:.3e}'.format(uxoObj1.times[tn-1]) + " s"
    Ax11.set_title(titlestr1,fontsize=FS+2)
    Xn,Yn = np.meshgrid(np.linspace(-Dx/2,Dx/2,Nx),np.linspace(-Dy/2,Dy/2,Ny))
    Ax11.scatter(Xn,Yn,color=(1,1,1),s=3)

    Ax11.set_xbound(-3.,3.)
    Ax11.set_ybound(-3.,3.)
    
    # Predicted Anomaly
    d12 = 1e3*np.reshape(da_pre[12:25*N**2:25,tn-1],(N,N))  # 1e3 for mV
    Cplot2 = Ax12.contourf(X1,Y1,d12.T,40,cmap='viridis')
    cbar2 = plt.colorbar(Cplot2, ax=Ax12, pad=0.02, format='%.2e')
    cbar2.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar2.ax.tick_params(labelsize=FS-2)

    Ax12.set_xlabel('X [m]',fontsize=FS)
    Ax12.set_ylabel('Y [m]',fontsize=FS)
    Ax12.tick_params(labelsize=FS-2)

    titlestr2 = "Predicted at t = " + '{:.3e}'.format(uxoObj1.times[tn-1]) + " s"
    Ax12.set_title(titlestr2,fontsize=FS+2)
    # Ax12.scatter(X,Y,color=(1,1,1),s=3)

    Ax12.set_xbound(-3.,3.)
    Ax12.set_ybound(-3.,3.)

    

    # CONVERGENCE AND PRINTOUT
    Ax21.plot(np.arange(1,len(m_vec)+1),np.ones(len(m_vec)),lw=3,color='k',ls=':')
    Ax21.plot(np.arange(1,len(m_vec)+1),m_vec,lw=2,color=(1,0,0))
    Ax21.set_xbound(1,len(m_vec))
    Ax21.set_ybound(0,np.max(m_vec))
    Ax21.set_xlabel('Count',fontsize=FS)
    Ax21.set_ylabel('$\chi^2$ Misfit',fontsize=FS)
    Ax21.tick_params(labelsize=FS-2)

    rt_str = "$r_{true}$ = (" + '{:.2f}'.format(rt[0]) + "," + '{:.2f}'.format(rt[1]) + "," + '{:.2f}'.format(rt[2]) + ")"
    rn_str = "$r_{rec}$  = (" + '{:.2f}'.format(rn[0]) + "," + '{:.2f}'.format(rn[1]) + "," + '{:.2f}'.format(rn[2]) + ")"
    fm_str = "Final Misfit = " + '{:.2f}'.format(m_vec[-1])
    Ax21.text(0.4*len(m_vec),0.92*m_vec[0],rt_str,fontsize=FS)
    Ax21.text(0.4*len(m_vec),0.83*m_vec[0],rn_str,fontsize=FS)
    Ax21.text(0.4*len(m_vec),0.74*m_vec[0],fm_str,fontsize=FS)


    # POLARIATIONS
    Lxt = uxoObj1.L[0:11]
    Lyt = uxoObj1.L[11:22]
    Lzt = uxoObj1.L[22:33]
    Lxn = Ln[0,:].T
    Lyn = Ln[1,:].T
    Lzn = Ln[2,:].T
    maxLtn = np.max([np.max(uxoObj1.L),np.max(Ln)])

    Ax22.loglog(uxoObj1.times,Lxt,lw=2,color='b')
    Ax22.loglog(uxoObj1.times,Lyt,lw=2,color='r')
    Ax22.loglog(uxoObj1.times,Lzt,lw=2,color='k')
    Ax22.loglog(uxoObj1.times,Lxn,lw=2,color='b',ls=':')
    Ax22.loglog(uxoObj1.times,Lyn,lw=2,color='r',ls=':')
    Ax22.loglog(uxoObj1.times,Lzn,lw=2,color='k',ls=':')

    Ax22.set_xlabel('t [s]',fontsize=FS)
    Ax22.set_ylabel('Polarization',fontsize=FS)
    Ax22.tick_params(labelsize=FS-2)

    Ax22.set_xbound(np.min(uxoObj1.times),np.max(uxoObj1.times))
    Ax22.set_ybound(1e-4*maxLtn,1.2*maxLtn)
    Ax22.text(1.2e-4,7e-4*maxLtn,"$\mathbf{L_{x'}}$",fontsize=FS,color='b')
    Ax22.text(1.2e-4,3e-4*maxLtn,"$\mathbf{L_{y'}}$",fontsize=FS,color='r')
    Ax22.text(1.2e-4,1.3e-4*maxLtn,"$\mathbf{L_{z'}}$",fontsize=FS,color='k')


    plt.show(Fig)


def fcnInversionWidgetMPV(xt,yt,zt,psi,theta,phi,k1,alpha1,beta1,gamma1,k2,alpha2,beta2,gamma2,k3,alpha3,beta3,gamma3,Dx,Dy,Nx,Ny,x0,y0,z0,tn,dComp):

    # SET TRUE UXO PROPERTIES
    rt = np.r_[xt,yt,zt]
    phi = np.r_[psi,theta,phi]
    times = np.logspace(-4,-2,11)
    L = np.r_[k1,alpha1,beta1,10**gamma1,k2,alpha2,beta2,10**gamma2,k3,alpha3,beta3,10**gamma3]
    I = 100.

    # PREDICT TRUE ANOMALY
    uxoObj1 = MPVproblem(rt,phi,L,times,I)
    N = 25
    X1,Y1 = np.meshgrid(np.linspace(-3.,3.,N),np.linspace(-3.,3.,N))
    XYZ1 = np.c_[mkvc(X1),mkvc(Y1),0.1*np.ones(np.size(X1))]
    uxoObj1.defineSensorLoc(XYZ1)
    A = uxoObj1.computeRotMatrix()
    Hp = uxoObj1.computeHp()
    Brx = uxoObj1.computeBrx()
    P1 = uxoObj1.computeP(Hp,Brx)
    q = uxoObj1.computePolarVecs()
    da_true = np.dot(P1,q)

    # PREDICT TRUE DATA
    uxoObj2 = MPVproblem(rt,phi,L,times,I)
    X2,Y2 = np.meshgrid(np.linspace(-Dx/2,Dx/2,Nx),np.linspace(-Dy/2,Dy/2,Ny))
    XYZ2 = np.c_[mkvc(X2),mkvc(Y2),0.1*np.ones(np.size(X2))]
    uxoObj2.defineSensorLoc(XYZ2)
    A = uxoObj2.computeRotMatrix()
    Hp = uxoObj2.computeHp()
    Brx = uxoObj2.computeBrx()
    P2 = uxoObj2.computeP(Hp,Brx)
    q = uxoObj2.computePolarVecs()
    data = np.dot(P2,q)
    [dobs,dunc] = uxoObj2.get_dobs_dunc(data,1e-5,0.05)

    # SOLVE INVERSE PROBLEM
    Misfit = np.inf
    dMis = np.inf
    rn = np.r_[x0,y0,z0]
    
    uxoObj2.updatePolarizations(rn)
    Misfit = uxoObj2.computeMisfit(rn)
    
    COUNT = 0
    m_vec = []
    
    while Misfit > 1.001 and COUNT < 100 and dMis > 1e-5:
       
       MisPrev = Misfit
       
       rn,Sol = uxoObj2.updateLocation(rn)
       
       uxoObj2.updatePolarizations(rn)
       
       Misfit = uxoObj2.computeMisfit(rn)
       dMis = np.abs(MisPrev - Misfit)
       m_vec.append(Misfit)
       
       COUNT = COUNT + 1

    q = uxoObj2.q
    Ln = np.zeros((3,len(uxoObj2.times)))
    m_vec = np.array(m_vec)

    for pp in range(0,len(uxoObj2.times)):
        Q = np.r_[np.c_[q[0,pp],q[1,pp],q[2,pp]],np.c_[q[1,pp],q[3,pp],q[4,pp]],np.c_[q[2,pp],q[4,pp],q[5,pp]]]
        [qval,qvec] = np.linalg.eigh(Q)
        Ln[:,pp] = qval

    # PREDICT ANOMALY
    da_pre = np.dot(P1,q)


    # PLOTTING

    Fig = plt.figure(figsize=(13.5,8.5))
    Ax11 = Fig.add_axes([0,0.55,0.35,0.45])
    Ax12 = Fig.add_axes([0.5,0.55,0.35,0.45])
    Ax21 = Fig.add_axes([0.,0.,0.4,0.45])
    Ax22 = Fig.add_axes([0.5,0.,0.4,0.45])
    FS = 18

    if dComp is 'X':
        k=0
    elif dComp is 'Y':
        k=1
    elif dComp is 'Z':
        k=2

    # True Anomaly
    d11 = 1e3*np.reshape(da_true[6+k:15*N**2:15,tn-1],(N,N))  # 1e3 for mV
    Cplot1 = Ax11.contourf(X1,Y1,d11.T,40,cmap='viridis')
    cbar1 = plt.colorbar(Cplot1, ax=Ax11, pad=0.02, format='%.2e')
    if dComp is 'X':
        cbar1.set_label('dBx/dt [mV]', rotation=270, labelpad = 25, size=FS)
    elif dComp is 'Y':
        cbar1.set_label('dBy/dt [mV]', rotation=270, labelpad = 25, size=FS)
    elif dComp is 'Z':
        cbar1.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar1.ax.tick_params(labelsize=FS-2)

    Ax11.set_xlabel('X [m]',fontsize=FS)
    Ax11.set_ylabel('Y [m]',fontsize=FS)
    Ax11.tick_params(labelsize=FS-2)

    titlestr1 = "Observed at t = " + '{:.3e}'.format(uxoObj1.times[tn-1]) + " s"
    Ax11.set_title(titlestr1,fontsize=FS+2)
    Xn,Yn = np.meshgrid(np.linspace(-Dx/2,Dx/2,Nx),np.linspace(-Dy/2,Dy/2,Ny))
    Ax11.scatter(Xn,Yn,color=(1,1,1),s=3)

    Ax11.set_xbound(-3.,3.)
    Ax11.set_ybound(-3.,3.)
    
    # Predicted Anomaly
    d12 = 1e3*np.reshape(da_pre[6+k:15*N**2:15,tn-1],(N,N))  # 1e3 for mV
    Cplot2 = Ax12.contourf(X1,Y1,d12.T,40,cmap='viridis')
    cbar2 = plt.colorbar(Cplot2, ax=Ax12, pad=0.02, format='%.2e')
    if dComp is 'X':
        cbar2.set_label('dBx/dt [mV]', rotation=270, labelpad = 25, size=FS)
    elif dComp is 'Y':
        cbar2.set_label('dBy/dt [mV]', rotation=270, labelpad = 25, size=FS)
    elif dComp is 'Z':
        cbar2.set_label('dBz/dt [mV]', rotation=270, labelpad = 25, size=FS)
    cbar2.ax.tick_params(labelsize=FS-2)

    Ax12.set_xlabel('X [m]',fontsize=FS)
    Ax12.set_ylabel('Y [m]',fontsize=FS)
    Ax12.tick_params(labelsize=FS-2)

    titlestr2 = "Predicted at t = " + '{:.3e}'.format(uxoObj1.times[tn-1]) + " s"
    Ax12.set_title(titlestr2,fontsize=FS+2)
    # Ax12.scatter(X,Y,color=(1,1,1),s=3)

    Ax12.set_xbound(-3.,3.)
    Ax12.set_ybound(-3.,3.)

    

    # CONVERGENCE AND PRINTOUT
    Ax21.plot(np.arange(1,len(m_vec)+1),np.ones(len(m_vec)),lw=3,color='k',ls=':')
    Ax21.plot(np.arange(1,len(m_vec)+1),m_vec,lw=2,color=(1,0,0))
    Ax21.set_xbound(1,len(m_vec)+1)
    Ax21.set_ybound(0,np.max(m_vec))
    Ax21.set_xlabel('Count',fontsize=FS)
    Ax21.set_ylabel('$\chi^2$ Misfit',fontsize=FS)
    Ax21.tick_params(labelsize=FS-2)

    rt_str = "$r_{true}$ = (" + '{:.2f}'.format(rt[0]) + "," + '{:.2f}'.format(rt[1]) + "," + '{:.2f}'.format(rt[2]) + ")"
    rn_str = "$r_{rec}$  = (" + '{:.2f}'.format(rn[0]) + "," + '{:.2f}'.format(rn[1]) + "," + '{:.2f}'.format(rn[2]) + ")"
    fm_str = "Final Misfit = " + '{:.2f}'.format(m_vec[-1])
    Ax21.text(0.4*len(m_vec),0.92*m_vec[0],rt_str,fontsize=FS)
    Ax21.text(0.4*len(m_vec),0.83*m_vec[0],rn_str,fontsize=FS)
    Ax21.text(0.4*len(m_vec),0.74*m_vec[0],fm_str,fontsize=FS)

    # POLARIATIONS
    Lxt = uxoObj1.L[0:11]
    Lyt = uxoObj1.L[11:22]
    Lzt = uxoObj1.L[22:33]
    Lxn = Ln[0,:].T
    Lyn = Ln[1,:].T
    Lzn = Ln[2,:].T
    maxLtn = np.max([np.max(uxoObj1.L),np.max(Ln)])

    Ax22.loglog(uxoObj1.times,Lxt,lw=2,color='b')
    Ax22.loglog(uxoObj1.times,Lyt,lw=2,color='r')
    Ax22.loglog(uxoObj1.times,Lzt,lw=2,color='k')
    Ax22.loglog(uxoObj1.times,Lxn,lw=2,color='b',ls=':')
    Ax22.loglog(uxoObj1.times,Lyn,lw=2,color='r',ls=':')
    Ax22.loglog(uxoObj1.times,Lzn,lw=2,color='k',ls=':')

    Ax22.set_xlabel('t [s]',fontsize=FS)
    Ax22.set_ylabel('Polarization',fontsize=FS)
    Ax22.tick_params(labelsize=FS-2)

    Ax22.set_xbound(np.min(uxoObj1.times),np.max(uxoObj1.times))
    Ax22.set_ybound(1e-4*maxLtn,1.2*maxLtn)
    Ax22.text(1.2e-4,7e-4*maxLtn,"$\mathbf{L_{x'}}$",fontsize=FS,color='b')
    Ax22.text(1.2e-4,3e-4*maxLtn,"$\mathbf{L_{y'}}$",fontsize=FS,color='r')
    Ax22.text(1.2e-4,1.3e-4*maxLtn,"$\mathbf{L_{z'}}$",fontsize=FS,color='k')


    plt.show(Fig)








##############################################################################
#		DEFINE UXOTEM CLASS
##############################################################################

class UXOTEM():

    def __init__(self,r0,phi,L,times):

        self.r0 = r0
        self.phi = phi
        self.times = times
        self.TxLoc = None
        self.RxLoc = None
        self.RxComp = None
        self.TxID = None
        self.Hp = None
        self.Brx = None
        self.P = None
        self.q = None
        self.dunc = None
        self.dobs = None
        
        # For UXO, L3 is largest polarization!!!

        if len(L) == 8:
            L1 = L[0]*((1 + np.sqrt(times/L[1]))**(-L[2]))*np.exp(-times/L[3])
            L2 = L[4]*((1 + np.sqrt(times/L[5]))**(-L[6]))*np.exp(-times/L[7])
            L = np.r_[L1,L1,L2]
            self.L = L
        elif len(L) == 12 and len(times) != 4:
            L1 = L[0]*((1 + np.sqrt(times/L[1]))**(-L[2]))*np.exp(-times/L[3])
            L2 = L[4]*((1 + np.sqrt(times/L[5]))**(-L[6]))*np.exp(-times/L[7])
            L3 = L[8]*((1 + np.sqrt(times/L[9]))**(-L[10]))*np.exp(-times/L[11])
            L = np.r_[L1,L2,L3]
            self.L = L
        else:
            self.L = L

    def computeRotMatrix(self,Phi=False):
    
        #######################################
        # COMPUTE ROTATION MATRIX SUCH THAT m(t) = A*L(t)*A'*Hp
        # Default set such that phi1,phi2 = 0 is UXO pointed towards North
        
        if Phi is False:
            phi1 = np.radians(self.phi[0])
            phi2 = np.radians(self.phi[1])
            phi3 = np.radians(self.phi[2])
        else:
            phi1 = np.radians(Phi[0])           # Roll (CCW)
            phi2 = np.radians(Phi[1])           # Inclination (+ve is nose pointing down)
            phi3 = np.radians(Phi[2])           # Declination (degrees CW from North)
        
        # A1 = np.r_[np.c_[np.cos(phi1),-np.sin(phi1),0.],np.c_[np.sin(phi1),np.cos(phi1),0.],np.c_[0.,0.,1.]] # CCW Rotation about z-axis
        # A2 = np.r_[np.c_[1.,0.,0.],np.c_[0.,np.cos(phi2),np.sin(phi2)],np.c_[0.,-np.sin(phi2),np.cos(phi2)]] # CW Rotation about x-axis (rotates towards North)
        # A3 = np.r_[np.c_[np.cos(phi3),-np.sin(phi3),0.],np.c_[np.sin(phi3),np.cos(phi3),0.],np.c_[0.,0.,1.]] # CCW Rotation about z-axis (direction of head of object)

        A1 = np.r_[np.c_[np.cos(phi1),np.sin(phi1),0.],np.c_[-np.sin(phi1),np.cos(phi1),0.],np.c_[0.,0.,1.]] # CW Rotation about z-axis
        A2 = np.r_[np.c_[1.,0.,0.],np.c_[0.,np.cos(phi2),np.sin(phi2)],np.c_[0.,-np.sin(phi2),np.cos(phi2)]] # CW Rotation about x-axis (rotates towards North)
        A3 = np.r_[np.c_[np.cos(phi3),np.sin(phi3),0.],np.c_[-np.sin(phi3),np.cos(phi3),0.],np.c_[0.,0.,1.]] # CW Rotation about z-axis (direction of head of object)
        
        return np.dot(A3,np.dot(A2,A1))


    def computePolarVecs(self,karg=False):

        N = len(self.times)
        L = np.reshape(self.L,(3,N))

        if karg is False:
            A = self.computeRotMatrix()
        elif np.size(karg) is 3:
            A = self.computeRotMatrix(karg)
        elif np.size(karg) is 9:
            A = karg

        q = np.zeros((6,N))

        for pp in range(0,N):

            Lpp = np.diag(L[:,pp])
            p = np.dot(A,np.dot(Lpp,A.T))
            q[:,pp] = np.r_[p[:,0],p[[1,2],1],p[2,2]]

        return q

    def computeP(self,Hp,Brx):

        P = np.c_[Brx[:,0]*Hp[:,0], Brx[:,0]*Hp[:,1]+Brx[:,1]*Hp[:,0], Brx[:,0]*Hp[:,2]+Brx[:,2]*Hp[:,0], Brx[:,1]*Hp[:,1], Brx[:,1]*Hp[:,2]+Brx[:,2]*Hp[:,1], Brx[:,2]*Hp[:,2]]

        self.P = self.P

        return P


















##############################################################################
#       DEFINE EM61problem class
##############################################################################

class EM61problem(UXOTEM):

    def __init__(self,r0,phi,L,times,I):
        UXOTEM.__init__(self,r0,phi,L,times)
        self.I = I


    def defineSensorLoc(self,XYZ):
        #############################################
        # DEFINE TRANSMITTER AND RECEIVER LOCATIONS
        #
        # XYZ: N X 3 array containing transmitter center locations
        # **NOTE** for this sensor, we know where the receivers are relative to transmitters
        self.TxLoc = XYZ
        self.RxLoc = np.c_[XYZ[:,0],XYZ[:,1],XYZ[:,2]+0.4]
        self.TxID = np.arange(1,np.shape(XYZ)[0]+1)
        self.RxComp = 3*np.ones(np.shape(XYZ)[0])

    def computeHp(self,XYZ=False,r0=False,update=True):
        
        ################################
        # COMPUTE PRIMARY FIELDS FROM ALL TRANSMITTERS
        #
        # XYZ: N X 3 array containing transmitter center locations
        # No need for XYZ imput in sensors already defined
        # r0: UXO location (field point)
        # If r0 is False, we compute the primary field as the true UXO location
        
        if XYZ is False and r0 is False:
            assert self.TxLoc is not None, "TxLoc must be set already if XYZ = False"
            XYZ = self.TxLoc
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is not False and r0 is False:
            self.defineSensorLoc(XYZ)
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is False and r0 is not False:
            assert self.TxLoc is not None, "TxLoc must be set already if XYZ = False"
            XYZ = self.TxLoc
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        else:
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        
        I  = self.I
        
        dx1 = np.r_[1.,0.,-1.,0.]
        dx2 = np.r_[0.,0.5,0.,-0.5]
        x1p = np.r_[-0.5,0.5,0.5,-0.5,-0.5]
        x2p = np.r_[-0.25,-0.25,0.25,0.25,-0.25]
        
        Hx0 = np.zeros(np.shape(XYZ)[0])
        Hy0 = np.zeros(np.shape(XYZ)[0])
        Hz0 = np.zeros(np.shape(XYZ)[0])
        
        for pp in range(0,4):
            
            x1a = XYZ[:,0] + x1p[pp]
            x1b = XYZ[:,0] + x1p[pp+1]
            x2a = XYZ[:,1] + x2p[pp]
            x2b = XYZ[:,1] + x2p[pp+1]
            
            vab = np.sqrt(dx1[pp]**2 + dx2[pp]**2)
            vap = np.sqrt((x0 - x1a)**2 + (y0 - x2a)**2 + (z0 - XYZ[:,2])**2)
            vbp = np.sqrt((x0 - x1b)**2 + (y0 - x2b)**2 + (z0 - XYZ[:,2])**2)
            
            # Cosines from cos()=<v1,v2>/(|v1||v2|)
            CosAlpha = ((x0 - x1a)*( dx1[pp]) + (y0 - x2a)*( dx2[pp]))/(vap*vab)
            CosBeta  = ((x0 - x1b)*(-dx1[pp]) + (y0 - x2b)*(-dx2[pp]))/(vbp*vab)

            
            # Determining Radial Vector From Wire
            DotTemp = (x1a - x0)*(dx1[pp]) + (x2a - y0)*(dx2[pp])
            
            Rx1 = (x1a - x0) - DotTemp*(dx1[pp])/vab**2
            Rx2 = (x2a - y0) - DotTemp*(dx2[pp])/vab**2
            Rx3 = (XYZ[:,2] - z0)
            
            R = np.sqrt(Rx1**2 + Rx2**2 + Rx3**2)
            
            Phi = (CosAlpha + CosBeta)/R
            
            # I/4*pi in each direction
            Ix1 = I*(dx1[pp])/(4*np.pi*vab)
            Ix2 = I*(dx2[pp])/(4*np.pi*vab)
            
            # Add contribution from wire pp into array
            Hx0 = Hx0 + Phi*(-Ix2*Rx3)/R
            Hy0 = Hy0 + Phi*( Ix1*Rx3)/R
            Hz0 = Hz0 + Phi*(-Ix1*Rx2 + Ix2*Rx1)/R

        if update is True:
            self.Hp = np.c_[Hx0,Hy0,Hz0]
            
        return np.c_[Hx0,Hy0,Hz0]

    def computeBrx(self,XYZ=False,r0=False,update=True):
        
        ##############################################
        # COMPUTE SPARSE ROW-COMPRESSED DIPOLE GEOMETRY ARRAY
        #
        # XYZ: N X 3 array containing transmitter center locations
        # r0: 3L array containing a UXO object
        
        assert self.TxLoc is not None and self.RxLoc is not None, "Transmitter and receiver locations must be set"

        if XYZ is False and r0 is False:
            assert self.RxLoc is not None, "RxLoc must be set already if XYZ = False"
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is not False and r0 is False:
            self.defineSensorLoc(XYZ)
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is False and r0 is not False:
            assert self.RxLoc is not None, "RxLoc must be set already if XYZ = False"
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        elif XYZ is not False and r0 is not False:
            self.defineSensorLoc(XYZ)
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]

        #-------------------------------------------
        # DIPOLE RESPONSE AT CENTER OF RECEIVER LOOP
        # C = -(mu0/4*pi)*Area

        # a = 0.5 # Area of receiver loop
        # C = 1e-7*a

        # R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2)

        # Brx = np.c_[C*(3*(X-x0)*(Z-z0)/R**5),C*(3*(Y-y0)*(Z-z0)/R**5),C*(3*(Z-z0)*(Z-z0)/R**5-1/R**3)]

        #------------------------------------------------------
        # 4 POINT QUADRATURE OVER x[-0.5,0.5] and y[-0.25,0.25]

        M = len(X)

        hx = 0.5/np.sqrt(3)
        hy = 0.25/np.sqrt(3)

        X = np.kron(np.reshape(X,(M,1)),np.ones((1,4))) + np.kron(np.ones((M,1)),np.c_[-hx,hx,-hx,hx])
        Y = np.kron(np.reshape(Y,(M,1)),np.ones((1,4))) + np.kron(np.ones((M,1)),np.c_[-hy,-hy,hy,hy])
        Z = np.kron(np.reshape(Z,(M,1)),np.ones((1,4)))

        # C = -(mu0/4*pi)*((bx-ax)/2)*((by-bx)/2)
        C = 1e-7/8.

        R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2)

        Brx = np.c_[C*np.dot(3*(X-x0)*(Z-z0)/R**5,np.ones(4)),C*np.dot(3*(Y-y0)*(Z-z0)/R**5,np.ones(4)),C*np.dot(3*(Z-z0)*(Z-z0)/R**5-1/R**3,np.ones(4))]

        if update is True:
            self.Brx = Brx
        
        return Brx

    def get_dobs_dunc(self,dpre,Floor,Pct):

        # Floor is a fraction of the largest amplitude anomaly for the earliest time channel

        Floor = Floor*np.max(np.abs(dpre))

        dunc = Floor + Pct*np.abs(dpre)
        dobs = dpre + dunc*np.random.normal(size=np.shape(dpre))

        self.dunc = dunc
        self.dobs = dobs

        return dobs,dobs

    def computeMisfit(self,r0):

        assert self.q is not None, "Must have current estimate of polarizations"
        assert self.dunc is not None, "Must have set uncertainties"
        assert self.dobs is not None, "Must have observed data"

        dunc = self.dunc
        dobs = self.dobs
        q = self.q

        Hp = self.computeHp(r0=r0,update=False)
        Brx = self.computeBrx(r0=r0,update=False)
        P = self.computeP(Hp,Brx)

        N = np.size(dobs)

        dpre = np.dot(P,q)

        v = mkvc((dpre-dobs)/dunc)

        Phi = np.dot(v.T,v)

        return Phi/N

    def computeVecFcn(self,r0):

        assert self.q is not None, "Must have current estimate of polarizations"
        assert self.dunc is not None, "Must have set uncertainties"
        assert self.dobs is not None, "Must have observed data"

        dunc = self.dunc
        dobs = self.dobs
        q = self.q

        Hp = self.computeHp(r0=r0,update=False)
        Brx = self.computeBrx(r0=r0,update=False)
        P = self.computeP(Hp,Brx)

        N = np.size(dobs)

        dpre = np.dot(P,q)

        v = mkvc((dpre-dobs)/dunc)

        return v

    def updatePolarizations(self,r0):

        # Set operator and solution array
        Hp = self.computeHp(r0=r0)
        Brx = self.computeBrx(r0=r0)
        P = self.computeP(Hp,Brx)
        dunc = self.dunc
        dobs = self.dobs

        K = np.shape(dobs)[1]
        q = np.zeros((6,K))

        lb = np.zeros(6)
        ub = np.inf*np.ones(6)

        for kk in range(0,K):
            
            LHS = P/np.c_[dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk]]
            RHS = dobs[:,kk]/dunc[:,kk]
            Sol = op.lsq_linear(LHS,RHS,bounds=(lb,ub),tol=1e-5)
            q[:,kk] = Sol.x

        self.q = q

    def updateLocation(self,r0):

        # Sol = op.minimize(self.computeMisfit,r0,method='Powell',options={'xtol':1e-5})
        Sol = op.root(self.computeVecFcn,r0,method='lm',options={'xtol':1e-5})

        r0 = Sol.x

        return r0,Sol


























##############################################################################
#       DEFINE TEMTADSproblem class
##############################################################################

class TEMTADSproblem(UXOTEM):

    def __init__(self,r0,phi,L,times,I):
        UXOTEM.__init__(self,r0,phi,L,times)
        self.I = I


    def defineSensorLoc(self,XYZ):
        #############################################
        # DEFINE TRANSMITTER AND RECEIVER LOCATIONS
        #
        # XYZ: N X 3 array containing transmitter center locations
        # **NOTE** for this sensor, we know where the receivers are relative to transmitters
        self.TxLoc = XYZ

        dx,dy = np.meshgrid([-0.8,-0.4,0.,0.4,0.8],[-0.8,-0.4,0.,0.4,0.8])
        dx = mkvc(dx)
        dy = mkvc(dy)

        N = np.shape(XYZ)[0]

        X = np.kron(XYZ[:,0],np.ones((25))) + np.kron(np.ones((N)),dx)
        Y = np.kron(XYZ[:,1],np.ones((25))) + np.kron(np.ones((N)),dy)
        Z = np.kron(XYZ[:,2],np.ones((25)))

        self.RxLoc = np.c_[X,Y,Z]

        self.TxID = np.kron(np.arange(1,np.shape(XYZ)[0]+1),np.ones((25)))
        self.RxComp = np.kron(3*np.ones(np.shape(XYZ)[0]),np.ones((25)))

    def computeHp(self,XYZ=False,r0=False,update=True):
        
        ################################
        # COMPUTE PRIMARY FIELDS FROM ALL TRANSMITTERS
        #
        # XYZ: N X 3 array containing transmitter center locations
        # No need for XYZ imput in sensors already defined
        # r0: UXO location (field point)
        # If r0 is False, we compute the primary field as the true UXO location
        
        if XYZ is False and r0 is False:
            assert self.TxLoc is not None, "TxLoc must be set already if XYZ = False"
            XYZ = self.TxLoc
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is not False and r0 is False:
            self.defineSensorLoc(XYZ)
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is False and r0 is not False:
            assert self.TxLoc is not None, "TxLoc must be set already if XYZ = False"
            XYZ = self.TxLoc
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        else:
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        
        I  = self.I
        
        dx1 = np.r_[2.,0.,-2.,0.]
        dx2 = np.r_[0.,2.,0.,-2.]
        x1p = np.r_[-1.,1.,1.,-1.,-1.]
        x2p = np.r_[-1.,-1.,1.,1.,-1.]
        
        Hx0 = np.zeros(np.shape(XYZ)[0])
        Hy0 = np.zeros(np.shape(XYZ)[0])
        Hz0 = np.zeros(np.shape(XYZ)[0])
        
        for pp in range(0,4):
            
            x1a = XYZ[:,0] + x1p[pp]
            x1b = XYZ[:,0] + x1p[pp+1]
            x2a = XYZ[:,1] + x2p[pp]
            x2b = XYZ[:,1] + x2p[pp+1]
            
            vab = np.sqrt(dx1[pp]**2 + dx2[pp]**2)
            vap = np.sqrt((x0 - x1a)**2 + (y0 - x2a)**2 + (z0 - XYZ[:,2])**2)
            vbp = np.sqrt((x0 - x1b)**2 + (y0 - x2b)**2 + (z0 - XYZ[:,2])**2)
            
            # Cosines from cos()=<v1,v2>/(|v1||v2|)
            CosAlpha = ((x0 - x1a)*( dx1[pp]) + (y0 - x2a)*( dx2[pp]))/(vap*vab)
            CosBeta  = ((x0 - x1b)*(-dx1[pp]) + (y0 - x2b)*(-dx2[pp]))/(vbp*vab)

            
            # Determining Radial Vector From Wire
            DotTemp = (x1a - x0)*(dx1[pp]) + (x2a - y0)*(dx2[pp])
            
            Rx1 = (x1a - x0) - DotTemp*(dx1[pp])/vab**2
            Rx2 = (x2a - y0) - DotTemp*(dx2[pp])/vab**2
            Rx3 = (XYZ[:,2] - z0)
            
            R = np.sqrt(Rx1**2 + Rx2**2 + Rx3**2)
            
            Phi = (CosAlpha + CosBeta)/R
            
            # I/4*pi in each direction
            Ix1 = I*(dx1[pp])/(4*np.pi*vab)
            Ix2 = I*(dx2[pp])/(4*np.pi*vab)
            
            # Add contribution from wire pp into array
            Hx0 = Hx0 + Phi*(-Ix2*Rx3)/R
            Hy0 = Hy0 + Phi*( Ix1*Rx3)/R
            Hz0 = Hz0 + Phi*(-Ix1*Rx2 + Ix2*Rx1)/R

        if update is True:
            self.Hp = np.kron(np.c_[Hx0,Hy0,Hz0],np.ones((25,1)))
            
        return np.kron(np.c_[Hx0,Hy0,Hz0],np.ones((25,1)))

    def computeBrx(self,XYZ=False,r0=False,update=True):
        
        ##############################################
        # COMPUTE SPARSE ROW-COMPRESSED DIPOLE GEOMETRY ARRAY
        #
        # XYZ: N X 3 array containing transmitter center locations
        # r0: 3L array containing a UXO object
        
        assert self.TxLoc is not None and self.RxLoc is not None, "Transmitter and receiver locations must be set"

        if XYZ is False and r0 is False:
            assert self.RxLoc is not None, "RxLoc must be set already if XYZ = False"
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is not False and r0 is False:
            self.defineSensorLoc(XYZ)
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is False and r0 is not False:
            assert self.RxLoc is not None, "RxLoc must be set already if XYZ = False"
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        elif XYZ is not False and r0 is not False:
            self.defineSensorLoc(XYZ)
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]

        #-------------------------------------------
        # DIPOLE RESPONSE AT CENTER OF RECEIVER LOOP
        # C = -(mu0/4*pi)*Area

        # a = 0.5 # Area of receiver loop
        # C = 1e-7*a

        # R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2)

        # Brx = np.c_[C*(3*(X-x0)*(Z-z0)/R**5),C*(3*(Y-y0)*(Z-z0)/R**5),C*(3*(Z-z0)*(Z-z0)/R**5-1/R**3)]

        #------------------------------------------------------
        # 4 POINT QUADRATURE OVER x[-0.5,0.5] and y[-0.25,0.25]

        M = len(X)

        hx = 0.2/np.sqrt(3)
        hy = 0.2/np.sqrt(3)

        X = np.kron(np.reshape(X,(M,1)),np.ones((1,4))) + np.kron(np.ones((M,1)),np.c_[-hx,hx,-hx,hx])
        Y = np.kron(np.reshape(Y,(M,1)),np.ones((1,4))) + np.kron(np.ones((M,1)),np.c_[-hy,-hy,hy,hy])
        Z = np.kron(np.reshape(Z,(M,1)),np.ones((1,4)))

        # C = -(mu0/4*pi)*((bx-ax)/2)*((by-bx)/2)
        C = 1e-7*0.2**2

        R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2)

        Brx = np.c_[C*np.dot(3*(X-x0)*(Z-z0)/R**5,np.ones(4)),C*np.dot(3*(Y-y0)*(Z-z0)/R**5,np.ones(4)),C*np.dot(3*(Z-z0)*(Z-z0)/R**5-1/R**3,np.ones(4))]

        if update is True:
            self.Brx = Brx
        
        return Brx

    def get_dobs_dunc(self,dpre,Floor,Pct):

        # Floor is a fraction of the largest amplitude anomaly for the earliest time channel

        Floor = Floor*np.max(np.abs(dpre))

        dunc = Floor + Pct*np.abs(dpre)
        dobs = dpre + dunc*np.random.normal(size=np.shape(dpre))

        self.dunc = dunc
        self.dobs = dobs

        return dobs,dobs

    def computeMisfit(self,r0):

        assert self.q is not None, "Must have current estimate of polarizations"
        assert self.dunc is not None, "Must have set uncertainties"
        assert self.dobs is not None, "Must have observed data"

        dunc = self.dunc
        dobs = self.dobs
        q = self.q

        Hp = self.computeHp(r0=r0,update=False)
        Brx = self.computeBrx(r0=r0,update=False)
        P = self.computeP(Hp,Brx)

        N = np.size(dobs)

        dpre = np.dot(P,q)

        v = mkvc((dpre-dobs)/dunc)

        Phi = np.dot(v.T,v)

        return Phi/N

    def computeVecFcn(self,r0):

        assert self.q is not None, "Must have current estimate of polarizations"
        assert self.dunc is not None, "Must have set uncertainties"
        assert self.dobs is not None, "Must have observed data"

        dunc = self.dunc
        dobs = self.dobs
        q = self.q

        Hp = self.computeHp(r0=r0,update=False)
        Brx = self.computeBrx(r0=r0,update=False)
        P = self.computeP(Hp,Brx)

        N = np.size(dobs)

        dpre = np.dot(P,q)

        v = mkvc((dpre-dobs)/dunc)

        return v

    def updatePolarizations(self,r0):

        # Set operator and solution array
        Hp = self.computeHp(r0=r0)
        Brx = self.computeBrx(r0=r0)
        P = self.computeP(Hp,Brx)
        dunc = self.dunc
        dobs = self.dobs

        K = np.shape(dobs)[1]
        q = np.zeros((6,K))

        lb = np.zeros(6)
        ub = np.inf*np.ones(6)

        for kk in range(0,K):
            
            LHS = P/np.c_[dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk]]
            RHS = dobs[:,kk]/dunc[:,kk]
            Sol = op.lsq_linear(LHS,RHS,bounds=(lb,ub),tol=1e-5)
            q[:,kk] = Sol.x

        self.q = q

    def updateLocation(self,r0):

        # Sol = op.minimize(self.computeMisfit,r0,method='dogleg')
        Sol = op.root(self.computeVecFcn,r0,method='lm',options={'xtol':1e-5})

        r0 = Sol.x

        return r0,Sol



























##############################################################################
#       DEFINE MPVproblem class
##############################################################################

class MPVproblem(UXOTEM):

    def __init__(self,r0,phi,L,times,I):
        UXOTEM.__init__(self,r0,phi,L,times)
        self.I = I


    def defineSensorLoc(self,XYZ):
        #############################################
        # DEFINE TRANSMITTER AND RECEIVER LOCATIONS
        #
        # XYZ: N X 3 array containing transmitter center locations
        # **NOTE** for this sensor, we know where the receivers are relative to transmitters
        self.TxLoc = XYZ

        dx = np.kron([-0.18,0.,0.,0.,0.18],np.ones(3))
        dy = np.kron([0.,-0.18,0.,0.18,0.],np.ones(3))

        N = np.shape(XYZ)[0]

        X = np.kron(XYZ[:,0],np.ones((15))) + np.kron(np.ones((N)),dx)
        Y = np.kron(XYZ[:,1],np.ones((15))) + np.kron(np.ones((N)),dy)
        Z = np.kron(XYZ[:,2],np.ones((15)))

        self.RxLoc = np.c_[X,Y,Z]

        self.TxID = np.kron(np.arange(1,np.shape(XYZ)[0]+1),np.ones((15)))
        self.RxComp = np.kron(np.kron(np.ones(np.shape(XYZ)[0]),np.ones((5))),np.r_[1,2,3])

    def computeHp(self,XYZ=False,r0=False,update=True):
        
        ################################
        # COMPUTE PRIMARY FIELDS FROM ALL TRANSMITTERS
        #
        # XYZ: N X 3 array containing transmitter center locations
        # No need for XYZ imput in sensors already defined
        # r0: UXO location (field point)
        # If r0 is False, we compute the primary field as the true UXO location
        
        if XYZ is False and r0 is False:
            assert self.TxLoc is not None, "TxLoc must be set already if XYZ = False"
            XYZ = self.TxLoc
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is not False and r0 is False:
            self.defineSensorLoc(XYZ)
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is False and r0 is not False:
            assert self.TxLoc is not None, "TxLoc must be set already if XYZ = False"
            XYZ = self.TxLoc
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        else:
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        
        I  = self.I

        K = 8 # Number of lengths to approximate loop
        theta = np.linspace(0.,2*np.pi,num=K+1)
        x1p = 0.25*np.cos(theta)
        x2p = 0.25*np.sin(theta)
        dx1 = x1p[1:K+1] - x1p[0:K]
        dx2 = x2p[1:K+1] - x2p[0:K]
        
        Hx0 = np.zeros(np.shape(XYZ)[0])
        Hy0 = np.zeros(np.shape(XYZ)[0])
        Hz0 = np.zeros(np.shape(XYZ)[0])
        
        for pp in range(0,K):
            
            x1a = XYZ[:,0] + x1p[pp]
            x1b = XYZ[:,0] + x1p[pp+1]
            x2a = XYZ[:,1] + x2p[pp]
            x2b = XYZ[:,1] + x2p[pp+1]
            
            vab = np.sqrt(dx1[pp]**2 + dx2[pp]**2)
            vap = np.sqrt((x0 - x1a)**2 + (y0 - x2a)**2 + (z0 - XYZ[:,2])**2)
            vbp = np.sqrt((x0 - x1b)**2 + (y0 - x2b)**2 + (z0 - XYZ[:,2])**2)
            
            # Cosines from cos()=<v1,v2>/(|v1||v2|)
            CosAlpha = ((x0 - x1a)*( dx1[pp]) + (y0 - x2a)*( dx2[pp]))/(vap*vab)
            CosBeta  = ((x0 - x1b)*(-dx1[pp]) + (y0 - x2b)*(-dx2[pp]))/(vbp*vab)

            
            # Determining Radial Vector From Wire
            DotTemp = (x1a - x0)*(dx1[pp]) + (x2a - y0)*(dx2[pp])
            
            Rx1 = (x1a - x0) - DotTemp*(dx1[pp])/vab**2
            Rx2 = (x2a - y0) - DotTemp*(dx2[pp])/vab**2
            Rx3 = (XYZ[:,2] - z0)
            
            R = np.sqrt(Rx1**2 + Rx2**2 + Rx3**2)
            
            Phi = (CosAlpha + CosBeta)/R
            
            # I/4*pi in each direction
            Ix1 = I*(dx1[pp])/(4*np.pi*vab)
            Ix2 = I*(dx2[pp])/(4*np.pi*vab)
            
            # Add contribution from wire pp into array
            Hx0 = Hx0 + Phi*(-Ix2*Rx3)/R
            Hy0 = Hy0 + Phi*( Ix1*Rx3)/R
            Hz0 = Hz0 + Phi*(-Ix1*Rx2 + Ix2*Rx1)/R

        if update is True:
            self.Hp = np.kron(np.c_[Hx0,Hy0,Hz0],np.ones((15,1)))
            
        return np.kron(np.c_[Hx0,Hy0,Hz0],np.ones((15,1)))

    def computeBrx(self,XYZ=False,r0=False,update=True):
        
        ##############################################
        # COMPUTE SPARSE ROW-COMPRESSED DIPOLE GEOMETRY ARRAY
        #
        # XYZ: N X 3 array containing transmitter center locations
        # r0: 3L array containing a UXO object
        
        assert self.TxLoc is not None and self.RxLoc is not None, "Transmitter and receiver locations must be set"

        if XYZ is False and r0 is False:
            assert self.RxLoc is not None, "RxLoc must be set already if XYZ = False"
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is not False and r0 is False:
            self.defineSensorLoc(XYZ)
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]
        elif XYZ is False and r0 is not False:
            assert self.RxLoc is not None, "RxLoc must be set already if XYZ = False"
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = r0[0]
            y0 = r0[1]
            z0 = r0[2]
        elif XYZ is not False and r0 is not False:
            self.defineSensorLoc(XYZ)
            X = self.RxLoc[:,0]
            Y = self.RxLoc[:,1]
            Z = self.RxLoc[:,2]
            x0 = self.r0[0]
            y0 = self.r0[1]
            z0 = self.r0[2]

        M = len(X)/3

        X = X[0:3*M:3]
        Y = Y[0:3*M:3]
        Z = Z[0:3*M:3]

        # C = -(mu0/4*pi)*Area*Nturns
        a = 0.01
        C = 1e-7*a*100

        R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2)

        Brx = np.zeros((3*M,3))

        Brx[0:3*M:3,:] = np.c_[C*(3*(X-x0)*(X-x0)/R**5-1/R**3),C*(3*(Y-y0)*(X-x0)/R**5),C*(3*(Z-z0)*(X-x0)/R**5)]
        Brx[1:3*M:3,:] = np.c_[C*(3*(X-x0)*(Y-y0)/R**5),C*(3*(Y-y0)*(Y-y0)/R**5-1/R**3),C*(3*(Z-z0)*(Y-y0)/R**5)]
        Brx[2:3*M:3,:] = np.c_[C*(3*(X-x0)*(Z-z0)/R**5),C*(3*(Y-y0)*(Z-z0)/R**5),C*(3*(Z-z0)*(Z-z0)/R**5-1/R**3)]

        if update is True:
            self.Brx = Brx
        
        return Brx

    def get_dobs_dunc(self,dpre,FloorVal,Pct):

        # Floor is a fraction of the largest amplitude anomaly for the earliest time channel

        M = np.shape(dpre)[0]
        Floor = np.zeros(np.shape(dpre))
        Floor[0:M:3,:] = FloorVal*np.max(np.abs(dpre[0:M:3,:]))
        Floor[1:M:3,:] = FloorVal*np.max(np.abs(dpre[1:M:3,:]))
        Floor[2:M:3,:] = FloorVal*np.max(np.abs(dpre[2:M:3,:]))

        dunc = Floor + Pct*np.abs(dpre)
        dobs = dpre + dunc*np.random.normal(size=np.shape(dpre))

        self.dunc = dunc
        self.dobs = dobs

        return dobs,dobs

    def computeMisfit(self,r0):

        assert self.q is not None, "Must have current estimate of polarizations"
        assert self.dunc is not None, "Must have set uncertainties"
        assert self.dobs is not None, "Must have observed data"

        dunc = self.dunc
        dobs = self.dobs
        q = self.q

        Hp = self.computeHp(r0=r0,update=False)
        Brx = self.computeBrx(r0=r0,update=False)
        P = self.computeP(Hp,Brx)

        N = np.size(dobs)

        dpre = np.dot(P,q)

        v = mkvc((dpre-dobs)/dunc)

        Phi = np.dot(v.T,v)

        return Phi/N

    def computeVecFcn(self,r0):

        assert self.q is not None, "Must have current estimate of polarizations"
        assert self.dunc is not None, "Must have set uncertainties"
        assert self.dobs is not None, "Must have observed data"

        dunc = self.dunc
        dobs = self.dobs
        q = self.q

        Hp = self.computeHp(r0=r0,update=False)
        Brx = self.computeBrx(r0=r0,update=False)
        P = self.computeP(Hp,Brx)

        N = np.size(dobs)

        dpre = np.dot(P,q)

        v = mkvc((dpre-dobs)/dunc)

        return v

    def updatePolarizations(self,r0):

        # Set operator and solution array
        Hp = self.computeHp(r0=r0)
        Brx = self.computeBrx(r0=r0)
        P = self.computeP(Hp,Brx)
        dunc = self.dunc
        dobs = self.dobs

        K = np.shape(dobs)[1]
        q = np.zeros((6,K))

        lb = np.zeros(6)
        ub = np.inf*np.ones(6)

        for kk in range(0,K):
            
            LHS = P/np.c_[dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk],dunc[:,kk]]
            RHS = dobs[:,kk]/dunc[:,kk]
            Sol = op.lsq_linear(LHS,RHS,bounds=(lb,ub),tol=1e-5)
            q[:,kk] = Sol.x

        self.q = q

    def updateLocation(self,r0):

        # Sol = op.minimize(self.computeMisfit,r0,method='dogleg')
        Sol = op.root(self.computeVecFcn,r0,method='lm',options={'xtol':1e-5})

        r0 = Sol.x

        return r0,Sol































