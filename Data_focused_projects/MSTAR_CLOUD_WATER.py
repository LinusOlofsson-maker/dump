import cartopy.crs as ccrs  # <-- To install: conda install -c conda-forge cartopy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import netCDF4 as nc
from matplotlib.cm import ScalarMappable
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

file_for_earth = []
filename_list = []
namelist = ["Qflux 50m deep ocean, 50 year average", "Qflux 50m deep ocean, no sea ice allowed, 100 year average"]

# Earth "Earth (qflux/slab ocean)",
# Earth = ('ANN0190-0199.aijP211eoZoht100_X001_O30.nc')  # 0

file_for_earth.append('ANN0190-0199.aijP211eoZoht100_X001_O30.nc')  # -1

filename_list.append('ANN0450-0500.aijMSTAR3400_TL_01.nc')  #Qflux 50m deep ocean, 50 year average

filename_list.append('ANN1900-1999.aijMSTAR3400_TL_01I.nc') #Qflux 50m deep ocean, no sea ice allowed, 100 year average


Col_map = []

p = 0
vmin = 0
vmax = 1.6
levels = 9
bounds = np.linspace(vmin, vmax, 6)

print("All filenames")
print(filename_list, len(filename_list))
'''
    Calculations for EAERTH-FILES ONLY ! 
'''


def earth_calc(file):
    yaxis_tsurf_mean = []
    row_AIJ = []

    data_AIJ = data_set['cldw'][:]  # From aij we load cldw (CLOUD CONDENSED WATER)
    lat_AIJ = data_set['lat'][:]  # Latitude, aij
    lon_AIJ = data_set['lon'][:]  # Latitude, aij

    row, collumn = np.array(data_AIJ), np.array(data_AIJ.T)  # Trans pose of data to reach columns

    for i in range(0, len(row)):
        # Y-AXIS
        var = np.mean(data_AIJ[i] + 273.15)  # Change to Kelvin
        yaxis_tsurf_mean.append(var)
        row_AIJ.append(row[0][i])

    lat_AIJ = np.array(lat_AIJ)
    row_AIJ = np.array(row_AIJ)
    lon_AIJ = np.array(lon_AIJ)
    return lat_AIJ, row_AIJ, data_AIJ, lon_AIJ


for file in file_for_earth:
    data_set = nc.Dataset(file)
    lat_aij, row_aij, data_aij, lon_aij = earth_calc(data_set)

    ############################################ Ellipse-plots################################################
    fig = plt.figure()
    ax3 = fig.add_subplot(projection=ccrs.Mollweide(central_longitude=0))
    ax3.set_title("Cloud Water (kg/m^2)\nEarth (qflux/slab ocean)", fontname='Franklin Gothic Medium', fontsize=15)
    ax3.grid(True)

    p += 1

    ax3.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=.7, color='black',
                  alpha=.5, linestyle='-')

    labels = f"Max data = {np.amax(data_aij):.3f} Min data = {np.amin(data_aij):.3f} Mean data = {np.mean(data_aij):.3f}"
    #cp = plt.get_cmap('seismic')
    cp = "Blues_r"
    #my_colors = cp(np.linspace(.1, .9, 10))
    x, y = np.meshgrid(lon_aij, lat_aij)
    # Plot data
    cf = plt.contourf(x, y, data_aij, cmap=cp, levels=levels, transform=ccrs.PlateCarree(), vmin=0, vmax=1.6)
    fig.colorbar(ScalarMappable(norm=cf.norm, cmap=cf.cmap), orientation='horizontal', ticks=bounds, label=labels)
    ax3.coastlines()

'''
    Calculations for all the remaining files! 
'''


def tsurf_vs_lat_AIJ(file):
    # AIJ
    yaxis_tsurf_mean = []
    row_AIJ = []

    data_AIJ = file_dataset['cldw'][:]  # From aij we load cldw (CLOUD CONDENSED WATER)
    lat_AIJ = file_dataset['lat'][:]  # Latitude, aij
    lon_AIJ = file_dataset['lon'][:]  # Latitude, aij


    row, collumn = np.array(data_AIJ), np.array(data_AIJ.T)  # Trans pose of data to reach columns


    for i in range(0, len(row)):
        # Y-AXIS
        var = np.mean(data_AIJ[i] + 273.15)  # Change to Kelvin
        yaxis_tsurf_mean.append(var)
        row_AIJ.append(row[0][i])

    lat_AIJ = np.array(lat_AIJ)
    row_AIJ = np.array(row_AIJ)
    lon_AIJ = np.array(lon_AIJ)
    return lat_AIJ, row_AIJ, data_AIJ, lon_AIJ


k = 0
p = 0

for file in filename_list:
    file_dataset = nc.Dataset(file)
    lat_aij, row_aij, data_aij, lon_aij = tsurf_vs_lat_AIJ(
        file_dataset)  # Returns latitude, all rows for cldw, all data cldw (CLOUD CONDENSED WATER)
    ############################################ Ellipse-plots################################################
    fig = plt.figure()
    ax3 = fig.add_subplot(projection=ccrs.Mollweide(central_longitude=0))
    ax3.set_title("Cloud Water (kg/m^2)\n" + namelist[p], fontname='Franklin Gothic Medium', fontsize=15)
    ax3.grid(True)

    p += 1

    ax3.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=.7, color='black',
                  alpha=.5, linestyle='-')

    labels = f"Max data = {np.amax(data_aij):.3f} Min data = {np.amin(data_aij):.3f} Mean data = {np.mean(data_aij):.3f}"
    #cp = plt.get_cmap('seismic')
    cp = "Blues_r"
    print('CP:',cp)
    #my_colors = cp(np.linspace(0, 0.5,levels))
   # print('My Colors',my_colors)
    x, y = np.meshgrid(lon_aij, lat_aij)
    # Plot data
    cf = plt.contourf(x, y, data_aij, cmap=cp, levels=levels, transform=ccrs.PlateCarree(), vmin=0, vmax=1.6)
    fig.colorbar(ScalarMappable(norm=cf.norm, cmap=cf.cmap), orientation='horizontal', ticks=bounds, label=labels)

plt.show()

