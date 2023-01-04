import cartopy.crs as ccrs  # <-- To install: conda install -c conda-forge cartopy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import netCDF4 as nc
from matplotlib.cm import ScalarMappable
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

data_list_x = []
data_list_y = []
data_list_data = []
file_for_earth = []
filename_list = []
namelist = ["Qflux 100m deep ocean", "Qflux 100m deep ocean, no sea ice allowed",
            "Rotating with 16 x Earth's sidereal day length\n 10 year average",
            "Rotating with 64 x Earth's sidereal day length\n 10 year average",
            "Rotating with 128 x Earth's sidereal day length\n 50 year average",
            "Rotating with 256 x Earth's sidereal day length\n 100 year average"]

# Earth "Earth (qflux/slab ocean)",
# Earth = ('ANN0190-0199.aijP211eoZoht100_X001_O30.nc')  # 0

file_for_earth.append('ANN0190-0199.aijP211eoZoht100_X001_O30.nc')  # -1

# Qflux 100m deep ocean
filename_list.append('ANN0090-0099.aijA211eoZoht100P10_X001.nc')  # 1

# Qflux 100m deep ocean, no sea ice allowed
filename_list.append('ANN0390-0399.aijA211eoZoht100P10_X001I.nc')  # 2

# Rotating with 16 x Earth's sidereal day length, 10 year average
# filename_list.append('ANN0090-0099.aijA211eoZoht100P10_X016.nc')   # 3

# Rotating with 64 x Earth's sidereal day length, 10 year average
# filename_list.append('ANN0090-0099.aijA211eoZoht100P10_X064.nc')   # 4

# Rotating with 128 x Earth's sidereal day length, 50 year average
# filename_list.append('ANN0150-0199.aijA211eoZoht100P10_X128.nc')   # 5

# Rotating with 256 x Earth's sidereal day length, 100 year average
# filename_list.append('ANN0100-0199.aijA211eoZoht100P10_X256.nc')   # 6
Col_map = []

p = 0
vmin = 0
vmax = 1.6
levels = 9 # Gå igenom med Moa <3

#colors_lower = plt.cm.binary(np.linspace(0.35, 0.75, 140))
#colors_middle = plt.cm.binary(np.linspace(0.55, 1., 15))
#colors_upper = plt.cm.binary(np.linspace(0.95, 1., 20))
#colors = np.vstack((colors_lower, colors_middle, colors_upper))
#cmap_col = mcolors.LinearSegmentedColormap.from_list('mycmap', colors)

cmap_col = "Blues_r"
#cmap_col = plt.get_cmap(cmap_col)
xmap = np.linspace(0.0, 1.0, 100)
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
    ax3 = fig.add_subplot(projection=ccrs.Mollweide(central_longitude=0),facecolor='white')
    #ax3.set_title("Cloud Water (kg/m^2)\nEarth (qflux/slab ocean)", fontname='Franklin Gothic Medium', fontsize=15)
    ax3.grid(True)

    p += 1

    ax3.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=.7, color='black',
                  alpha=.5, linestyle='-')
    #ax3.add_feature(cfeature.BORDERS)
   # labels = f"Max data = {np.amax(data_aij):.3f} Min data = {np.amin(data_aij):.3f} Mean data = {np.mean(data_aij):.3f}"
    cp = plt.get_cmap(cmap_col)
    x, y = np.meshgrid(lon_aij, lat_aij)
    # Plot data
    #ax3.contour(x, y, data_aij, 10, colors='white')
    cf = plt.contourf(x, y, data_aij, cmap=cp, levels=levels, transform=ccrs.PlateCarree(), vmin=0, vmax=1.6)

    Cb = fig.colorbar(ScalarMappable(norm=cf.norm, cmap=cf.cmap), orientation='horizontal', ticks=bounds) #, label=labels
    # Cb.set_clim(0,1.6)
    ax3.coastlines(color='black', linewidth=0.7)
    #data_list_x.append(x)
    #data_list_y.append(y)
    #data_list_data.append(data_aij)
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
T = 3

for file in filename_list:
    file_dataset = nc.Dataset(file)
    lat_aij, row_aij, data_aij, lon_aij = tsurf_vs_lat_AIJ(
        file_dataset)  # Returns latitude, all rows for cldw, all data cldw (CLOUD CONDENSED WATER)
    ############################################ Ellipse-plots################################################
    fig = plt.figure()
    ax3 = fig.add_subplot(projection=ccrs.Mollweide(central_longitude=0))
    #ax3.set_title("Cloud Water (kg/m^2)\n" + namelist[p], fontname='Franklin Gothic Medium', fontsize=15)
    ax3.grid(True,color='white')

    p += 1

    ax3.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=.7, color='black',
                  alpha=.5, linestyle='-')

    #labels = f"Max data = {np.amax(data_aij):.3f} Min data = {np.amin(data_aij):.3f} Mean data = {np.mean(data_aij):.3f}"
    cp = plt.get_cmap(cmap_col)
    x, y = np.meshgrid(lon_aij, lat_aij)
    # Plot data
    cf = plt.contourf(x, y, data_aij, cmap=cp, levels=levels, transform=ccrs.PlateCarree(), vmin=0, vmax=1.6)
    fig.colorbar(ScalarMappable(norm=cf.norm, cmap=cf.cmap), orientation='horizontal', ticks=bounds) #, label=labels
    data_list_x.append(x)
    data_list_y.append(y)
    data_list_data.append(data_aij)


fig2 = plt.figure()
"""
The 1,2,1+1 returns 1 row 2 collums and 1+i returns index of subplots
"""
for i in range(0, len(data_list_x)):
    cp = plt.get_cmap(cmap_col)
    axs = fig2.add_subplot(1, 2, 1 + i, projection=ccrs.Mollweide(central_longitude=0))
    cff = axs.contourf(data_list_x[i], data_list_y[i], data_list_data[i], cmap=cp, levels=levels,
                       transform=ccrs.PlateCarree(), vmin=0, vmax=1.6)
fig2.subplots_adjust(right=0.8)
cb_ax = fig2.add_axes([0.85, 0.15, 0.05, 0.7])
cbar = fig2.colorbar(ScalarMappable(norm=cff.norm, cmap=cff.cmap),cax=cb_ax)



plt.show()
