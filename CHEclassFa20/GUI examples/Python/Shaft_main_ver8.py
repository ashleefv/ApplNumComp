#   The objective of this project is to create a GUI that can read a text file that contains loading and other information
#   about a round shaft and the use that info to: calculate stresses and safety factors for the shaft, plot those stresses and safety
#   factors, and display diaglog boxes if improper inputs are given or something goes wrong in the calculations.
#-------------------------------------------------------------------------------------------------------------------------------------
#   There are several files and packages that must accompany this file in order fr the GUI to work properly. Files needed are:
#       'shaft_class_ver9.py' ; 'shaft_ui.py' ; and 'shaft_singularity.py'
#   The package that is needed is PyQt5
#   The following files are intended to be files that the program reads to obtain input information:
#       'Shaft Design Input File 1.txt' ; 'Shaft Design Input FIle Ex 7-2.txt'


import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

#the classes imported below are imported from files in a directory on the author's PC in a directory called 'Project'
#therefore the word 'Project' below should be changed to the name of the directory that the files below are stored in
#when the code is run by another person on another PC
from Project.shaft_ui import Ui_Dialog
from Project.Shaft_Class_ver9 import Beam
from Project.Shaft_Singularity_ver3 import sngval

#this class takes the code from 'shaft_ui' and attaches various functions within the class to all of the buttons
#this  does not open the ui when the code is run. That is done by the function starting on line 293

class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.beam = None
        self.show()

    def assign_widgets(self):

        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_GetShaft.clicked.connect(self.GetShaft)
        self.ui.pushButton_PlotAxTor.clicked.connect(self.PlotAxialTorque)
        self.ui.pushButton_PlotStresses.clicked.connect(self.stresses)
        self.ui.pushButton_PlotFS.clicked.connect(self.Safety_Factors)
        #self.ui.pushButton_Moments.clicked.connect(self.PlotMoment)

    def GetShaft(self):

        # get the filename using the OPEN dialog
        filename = QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:
            no_file()
            return
        self.ui.textEdit_filename.setText(filename)
        app.processEvents()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        # Read the file
        f1 = open(filename, 'r')  # open the file for reading
        data = f1.readlines()  # read the entire file as a list of strings
        f1.close()  # close the file  ... very important

        self.beam = Beam()  # create a Beam instance (object)

        try:
            self.beam.processshaft(data)
            self.ui.lineEdit_TRy.setText('{:.2f}'.format(self.beam.TR[0]))
            self.ui.lineEdit_TRz.setText('{:.2f}'.format(self.beam.TR[1]))
            self.ui.lineEdit_Thrust.setText('{:.2f}'.format(self.beam.TR[2]))
            self.ui.lineEdit_RRy.setText('{:.2f}'.format(self.beam.RR[0]))
            self.ui.lineEdit_RRz.setText('{:.2f}'.format(self.beam.RR[1]))
            self.ui.lineEdit_maxTension.setText('{:.2f}'.format(self.beam.max[0]))
            self.ui.lineEdit_maxTorque.setText('{:.2f}'.format(self.beam.max[2]))
            self.ui.lineEdit_maxMoment.setText('{:.2f}'.format(self.beam.max[4]))
            self.ui.lineEdit_maxTension_loc.setText('{:.2f}'.format(self.beam.max[1]))
            self.ui.lineEdit_maxTorque_loc.setText('{:.2f}'.format(self.beam.max[3]))
            self.ui.lineEdit_maxMoment_loc.setText('{:.2f}'.format(self.beam.max[5]))
            QApplication.restoreOverrideCursor()
        except:
            QApplication.restoreOverrideCursor()
            bad_file()


    def PlotSomething(self,moment=False):
        x = np.linspace(self.length/1000,self.length, 1000)
        y_y = np.zeros(x)
        y_z = np.zeros(x)

        for i in range(300):
            y_y[i] = sngval(self.load_y, x, c1=0, c2=0)
            y_z[i] = sngval(self.load_z, x, c1=0, c2=0)



        plt.plot(x, y_y)
        plt.plot(x, y_z)
        plt.show()
        return

    def stresses(self):
        # initialize all necessary values for the method
        L = self.beam.length;
        Diameters = self.beam.diameter;
        loads = self.beam.ten_list;torques = self.beam.tor_list;moments = self.beam.M
        MaxAmp = 0 ;MaxMean = 0; MaxStat = 0;
        MaxStat_Loc = 0; MaxAmp_Loc = 0; MaxMean_Loc = 0
        X = np.linspace(0, L, 10001)
        d_list = np.zeros(10001);bending = np.zeros(10001);axial = np.zeros(10001);torsion = np.zeros(10001)
        static = np.zeros(10001);mean = np.zeros(10001); amplitude = np.zeros(10001)
        i = 0;n = len(Diameters)

        for j in range(len(X)):
            if i == n - 1:
                break
            elif Diameters[i + 1][0] <= X[j]:  # see if the location of the next diameter is less than or equal to the current location
                i += 1
            d_list[j] = Diameters[i][1]
        for k in range(j, len(X)):
            d_list[k] = Diameters[i][1]
        for h in range(len(d_list)):
            load = loads[h]  # insert value or list already found in previus part **if list, find the maximum load first**
            # Find Axial Stress
            Area = (math.pi * (d_list[h]) ** 2) / 4
            axial[h] = load / Area
            # Find Torsional stress
            tor = torques[h]
            radius = d_list[h] / 2
            J = (math.pi * (d_list[h]) ** 4) / 32
            torsion[h] = tor * radius / J
            # Find Bending Stress
            moment = moments[h]
            I = (math.pi * (d_list[h]) ** 4) / 64
            bending[h] = moment * radius / I
            #Stress equations
            static[h] = math.sqrt(((axial[h] + bending[h]) ** 2) + (3 * (torsion[h]) ** 2))
            mean[h] = (((axial[h]) ** 2 )+ (3 * (torsion[h]) ** 2))**0.5
            amplitude[h] = bending[h]
            # check to see if the most recently calculated stresses are greater than the current maximums
            if h == 0:
                MaxAmp = amplitude[h]
                MaxMean = mean[h]
                MaxStat = static[h]
                MaxAmp_Loc = X[h]
                MaxStat_Loc = X[h]
                MaxMean_Loc = X[h]
            if amplitude[h] > MaxAmp:
                MaxAmp = amplitude[h]
                MaxAmp_Loc = X[h]
            if static[h] > MaxStat:
                MaxStat = static[h]
                MaxStat_Loc = X[h]
            if mean[h] > MaxMean:
                MaxMean = mean[h]
                MaxMean_Loc = X[h]
        self.ui.lineEdit_maxSiga.setText('{:.2f}'.format(MaxAmp))
        self.ui.lineEdit_maxSiga_loc.setText('{:.2f}'.format(MaxAmp_Loc))
        self.ui.lineEdit_maxSigm.setText('{:.2f}'.format(MaxMean))
        self.ui.lineEdit_maxSigm_loc.setText('{:.2f}'.format(MaxMean_Loc))
        self.ui.lineEdit_maxStatic.setText('{:.2f}'.format(MaxStat))
        self.ui.lineEdit_maxStatic_loc.setText('{:.2f}'.format(MaxStat_Loc))
        self.beam.bend_stress = bending
        self.beam.ax_stress = axial
        self.beam.shear_stress = torsion

        plt.rcParams["figure.figsize"] = [16, 16]
        plt.rcParams.update({'font.size': 18})
        fig, axarr = plt.subplots(3, sharex=True)
        #plt.suptitle(, fontsize=36)
        fig.patch.set_facecolor('WhiteSmoke')

        axarr[0].plot(X, mean, linewidth=3)
        axarr[0].set_title("Mean")
        axarr[0].locator_params(axis='y', nbins=2)

        axarr[1].plot(X, static, linewidth=3)
        axarr[1].set_title("Static Von mises")
        axarr[1].locator_params(axis='y', nbins=2)

        axarr[2].plot(X, amplitude, linewidth=3)
        axarr[2].set_title("Amplitude")
        axarr[2].locator_params(axis='y', nbins=2)

        plt.show()
        # set these equal to ui text boxes i.e. MaxMean, MaxStat, MaxAmp

    def Safety_Factors(self, title="Shaft Safety Factors",
                       ntitle="Static Safety Factor", nftitle="Fatigue Safety Factor", show=True, save=False):
        # intialize minimum values for static and fatigue factors of safety and their locations
        BendList = self.beam.bend_stress
        AxList = self.beam.ax_stress
        ShearList = self.beam.shear_stress
        kf=self.beam.stressconcentration
        Sut = self.beam.sut * 10 ** 3
        Sy = self.beam.sy * 10 ** 3
        Se = self.beam.se * 10 ** 3
        L = self.beam.length
        min_n = 0;min_nf = 0;
        n_loc = 0;nf_loc = 0
        # initialize lists necessary for storage
        n = np.zeros(len(AxList));
        nf = np.zeros(len(AxList));
        mean = np.zeros(len(AxList));
        X = np.linspace(0, L, len(AxList))
        for i in range(len(AxList)):
            mean[i] = (AxList[i] ** 2 + 3 * ShearList[i] ** 2) ** 0.5
            n[i] = Sy / ((( BendList[i] + AxList[i]) ** 2 + 3 * ShearList[i] ** 2) ** 0.5)
            nf[i] = ((kf*BendList[i] / Se) + (mean[i] / Sut)) ** -1
            if n[i] > 20:
                n[i] = 20
            if nf[i] > 20:
                nf[i] = 20
            # check to see if newly calculated safety fatcors are less than the current minimums
            if i == 0:
                min_n = n[i]
                min_nf = nf[i]
                n_loc = X[i]
                nf_loc = X[i]
            if n[i] < min_n:
                min_n = n[i]
                n_loc = X[i]
            if nf[i] < min_nf:
                min_nf = nf[i]
                nf_loc = X[i]
        self.ui.lineEdit_minFSfatigue.setText('{:.2f}'.format(min_nf))
        self.ui.lineEdit_minFSstatic.setText('{:.2f}'.format(min_n))
        self.ui.lineEdit_minFSfatigue_loc.setText('{:.2f}'.format(n_loc))
        self.ui.lineEdit_minFSstatic_loc.setText('{:.2f}'.format(nf_loc))
        self.ui.lineEdit_FS_Fatigue_Reqd.setText('{:.2f}'.format(self.beam.fatiguefactor))
        self.ui.lineEdit_FS_Static_Reqd.setText('{:.2f}'.format(self.beam.staticfactor))
        #plot the safety factors
        X = np.linspace(0, L, len(n))
        plt.rcParams["figure.figsize"] = [16, 16]
        plt.rcParams.update({'font.size': 18})
        fig, axarr = plt.subplots(2, sharex=True)
        plt.suptitle(title, fontsize=36)
        fig.patch.set_facecolor('WhiteSmoke')

        axarr[0].plot(X, n, linewidth=3)
        axarr[0].set_title(ntitle)
        axarr[0].locator_params(axis='y', nbins=2)

        axarr[1].plot(X, nf, linewidth=3)
        axarr[1].set_title(nftitle)
        axarr[1].locator_params(axis='y', nbins=2)

        if show:
            plt.show()
        if save:
            fig.savefig(title + ".pdf")

    def PlotAxialTorque(self, title="Axial Force and Torque", tentitle='Axial force', tortitle='Torque'):
        x = np.linspace(self.beam.length / 10001, self.beam.length, 10001)
        ten = self.beam.ten_list
        tor = self.beam.tor_list

        plt.rcParams["figure.figsize"] = [16, 16]
        plt.rcParams.update({'font.size': 18})
        fig, axarr = plt.subplots(2, sharex=True)
        #plt.suptitle(title, fontsize=36)
        fig.patch.set_facecolor('WhiteSmoke')

        axarr[0].plot(x, ten, linewidth=3)
        axarr[0].set_title(tentitle)
        axarr[0].locator_params(axis='y', nbins=2)

        axarr[1].plot(x, tor, linewidth=3)
        axarr[1].set_title(tortitle)
        axarr[1].locator_params(axis='y', nbins=2)

        plt.show()

    def ExitApp(self):
        app.exit()


def no_file():
    msg = QMessageBox()
    msg.setText('There was no file selected')
    msg.setWindowTitle("No File")
    retval = msg.exec_()
    return None


def bad_file():
    msg = QMessageBox()
    msg.setText('Unable to process the selected file')
    msg.setWindowTitle("Bad File")
    retval = msg.exec_()
    return None

#
if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())







