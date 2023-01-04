#   Suref.Pres  =   prsurf
#   Surft.Temp  =   tsurf
#   Incom.stell =   incsw_toa

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import netCDF4 as nc  # Find and install Python download

global c
c = 0
colors = ['k--', 'k-.', 'k', 'r', 'purple', 'brown', 'm']
filename_list = []
namelist = ["Aquaplanet with sea ice", "Aquaplanet without sea ice",
            "Earth-like planet",
            "Rotating with 16 x Earth's sidereal day length\n 10 year average",
            "Rotating with 64 x Earth's sidereal day length\n 10 year average",
            "Rotating with 128 x Earth's sidereal day length\n 50 year average",
            "Rotating with 256 x Earth's sidereal day length\n 100 year average", "Earth (qflux/slab ocean)"]

### Solar G-Type Star: Insolation=1365.3 W/m^2 ###

# Qflux 100m deep ocean
filename_list.append('ANN0450-0500.ajlMSTAR3400_TL_01.nc')  # 0   ANN0090-0099.ajlA211eoZoht100P10_X001.nc

# Qflux 100m deep ocean, no sea ice allowed
filename_list.append('ANN1900-1999.ajlMSTAR3400_TL_01I.nc')  # 1  ANN0390-0399.ajlA211eoZoht100P10_X001I.nc
filename_list.append('ANN0190-0199.ajlP211eoZoht100_X001_O30.nc')  # 6

"""
# ________________________________________________________________
# Rotating with 16 x Earth's sidereal day length, 10 year average
# #(It is the time taken by Earth to rotate on its own axis)
filename_list.append('ANN0090-0099.aijA211eoZoht100P10_X016.nc')  # 2

# Rotating with 64 x Earth's sidereal day length, 10 year average
filename_list.append('ANN0090-0099.aijA211eoZoht100P10_X064.nc')  # 3

# Rotating with 128 x Earth's sidereal day length, 50 year average
filename_list.append('ANN0150-0199.aijA211eoZoht100P10_X128.nc')  # 4

# Rotating with 256 x Earth's sidereal day length, 100 year average
filename_list.append('ANN0100-0199.aijA211eoZoht100P10_X256.nc')  # 5
# _________________________________________________________________

# Rotating with 256 x Earth's sidereal day length, 100 year average

# _________________________________________________________________
#########################################################################################################
"""
print("All filenames")
print(filename_list, len(filename_list))


def weighted_mean(x, y):  # x = tsurf, y = gridcell
    mean = np.nansum(x * y) / np.nansum(y)

    return mean


def plotter(lat, yaxis_tsurf_mean):
    fig1, ax1 = plt.subplots()
    ax1.plot(lat, yaxis_tsurf_mean, color="k")

    ax1.set_xlabel("Latitude (degrees)", fontname='Franklin Gothic Medium', fontsize=15)
    ax1.set_ylabel("Zonal-mean, $T_s$  (K)", fontname='Franklin Gothic Medium', fontsize=15)
    #ax1.set_title("Surface Air Temperature\n" + namelist[c], fontname='Franklin Gothic Medium', fontsize=15)
    ax1.grid(True)
    ax1.invert_yaxis()
    #label_x = ['90S', '60s', '30s', '0', '30N', '60N', '90N']  # Labels
    #plt.xticks(np.arange(lat.min(), lat.max() + 30, 30), label_x)
    #ax1.set_xlim((-90, 90))
    #ax1.legend(fontsize=12)


    return


def tsurf_vs_lat(file):
    yaxis_tsurf_mean = []
    xaxis_toa_mean = []

    Y_axis_mean = []

    X_axis_mean = []
    X_axis_mean2 = []

  #  y = file_dataset['axyp'][:]  # Gridcell used for weighted mean
   # data = file_dataset['tsurf'][:]         # Xaxis
  #  lon = file_dataset['lon'][:]  # Longitude
  #  lat = file_dataset['incsw_toa'][:]  # Latitude      # Yaxis

    Y_axis = file_dataset['plm']
    X_axis = file_dataset['tx']
    X_axis2 = file_dataset['q']

    #print("data", len(data), "\nLon", len(lon), "\nlat", len(lat))
   # xaxis_weighted = lat  # []

   # row, collumn = np.array(data), np.array(data.T)  # Transpose of data to reach columns

    #toa_row, toa_coll = np.array(lat), np.array(lat.T)

    #Y_axis_row, Y_axis_collumn = np.array(Y_axis), np.array(Y_axis).T
    #X_axis_row, X_axis_collumn = np.array(X_axis2), np.array(X_axis2).T
    #print('plm row')
   # print(Y_axis_row)
    #print('plm coll')
    #print(Y_axis_collumn)
    #print('tx row')
   # print(X_axis_row)
    #print('tx coll')
    #print(X_axis_collumn)
    #print(' ')
    for i in range(0, len(Y_axis)):
        # Y-AXIS
        varY =  np.mean(Y_axis[i])  # Change to Kelvin
        Y_axis_mean.append(varY)
        #print('plm')
        #print(Y_axis_mean[i])

    for i in range(0, len(X_axis)):
        # X-axis 1
        varX = np.mean(X_axis[i] + 273.15)
        X_axis_mean.append(varX)
        #varX2 = np.mean(X_axis2[i])
        #X_axis_mean2.append(varX2)
    for i in range(0,len(X_axis2)):
        # X-axis 2
        varX2 = np.mean(X_axis2[i])/1000
        X_axis_mean2.append(varX2)
        # X-AXIS
        # multiply weights with values(lat)
        #xaxis_weighted = lat * (np.cos(np.deg2rad(xaxis_weighted)))  # WEIGHTS
    #plotter(X_axis_mean, Y_axis_mean)
    #plotter(X_axis_mean2, Y_axis_mean)# Plot each run!
    #print('q')
    #print(X_axis_mean2)
    #print(' ')
    '''
    for i in range(0, len(row)):
        # Y-AXIS
        var = np.mean(data[i] + 273.15)  # Change to Kelvin
        yaxis_tsurf_mean.append(var)

        # X-AXIS
        # multiply weights with values(lat)
        xaxis_weighted = lat * (np.cos(np.deg2rad(xaxis_weighted)))  # WEIGHTS
    print('Tsurf')
    print(yaxis_tsurf_mean)

    for j in range(0, len(toa_row)):
        # Y-AXIS
        var_toa = np.mean(lat[j])  # Change to Kelvin
        xaxis_toa_mean.append(var_toa)

        # X-AXIS
        # multiply weights with values(lat)
        xaxis_weighted = lat * (np.cos(np.deg2rad(xaxis_weighted)))  # WEIGHTS

    print('Toa')
    print(xaxis_toa_mean)
    print(' ')
    '''
    #print('xaxis not weigthed:\n', lat)
    #plotter(lat, yaxis_tsurf_mean)  # Plot each run!
    return  X_axis_mean,Y_axis_mean,X_axis_mean2 #xaxis_weighted, yaxis_tsurf_mean, xaxis_toa_mean,

    # ______________________________________________________________________________________________
    # PLOTS
    # ______________________________________________________________________________________________


k = 0
p = 0
fig, ax2 = plt.subplots()
fig1, ax3 = plt.subplots()
for file in filename_list:
    file_dataset = nc.Dataset(file)

    X_mean,Y_mean,X_mean2 = tsurf_vs_lat(file_dataset) #xaxis_weighted, yaxis_tsurf_mean, xaxis_toa_mean,
    #print('weighted axsis:\n', xaxis_weighted)

    c += 1
    ax2.plot(X_mean, Y_mean,colors[k] ,label=namelist[k])

    k += 1

    ax2.set_xlabel("Temperature (K)", fontname='Franklin Gothic Medium', fontsize=15)
    ax2.set_ylabel("Pressure (hPa)", fontname='Franklin Gothic Medium', fontsize=15)
    ax2.invert_yaxis()
    #ax2.set_title("Surface Air Temperature", fontname='Franklin Gothic Medium', fontsize=15)
    ax2.grid(True)

    #label_x = ['10^1', '10^2', '10^3', '10^4', '10^5', '10^6']  # Labels

    #ax2.set_xlim((-90, 90))
    print(np.array(X_mean2).T)
    ax3.plot(np.array(X_mean2).T, Y_mean, colors[p], label=namelist[p])
    p += 1
    ax3.set_xlabel("Specific humidity (kg/kg)", fontname='Franklin Gothic Medium', fontsize=15)
    ax3.set_ylabel("Pressure (hPa)", fontname='Franklin Gothic Medium', fontsize=15)
    ax3.invert_yaxis()
    ax3.xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #ax3.ticklabel_format(axis="x", style="sci", scilimits=(0, 10))
    #ax3.set_xticks(label_x)
    # ax2.set_title("Surface Air Temperature", fontname='Franklin Gothic Medium', fontsize=15)
    ax3.grid(True)

ax2.legend(fontsize=10, loc='lower left')
ax3.legend(fontsize=10, loc='upper right')
plt.show()
