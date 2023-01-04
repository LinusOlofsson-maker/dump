import cartopy.crs as ccrs
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import netCDF4 as nc


filename_list = []
file_for_lat = []


namelist = ["P211eoZoht100_X001_O30", "A211eoZoht100P10_X001",
            "A211eoZoht100P10_X001I",
            "Rotating with 16 x Earth's sidereal day length\n 10 year average",
            "Rotating with 64 x Earth's sidereal day length\n 10 year average",
            "Rotating with 128 x Earth's sidereal day length\n 50 year average"]

# cldw (CLOUD CONDENSED WATER) från aij
# totcld (TOTAL CLOUD COVER) från ajl

### Solar G-Type Star: Insolation=1365.3 W/m^2 ###
file_for_lat.append('ANN0090-0099.aijA211eoZoht100P10_X001.nc')  # -1
# Earth

filename_list.append('ANN0190-0199.ajlP211eoZoht100_X001_O30.nc')  # 0

# Qflux 100m deep ocean

filename_list.append('ANN0090-0099.ajlA211eoZoht100P10_X001.nc')  # 1

# Qflux 100m deep ocean, no sea ice allowed

filename_list.append('ANN0390-0399.ajlA211eoZoht100P10_X001I.nc')  # 2

# ________________________________________________________________
# Rotating with 16 x Earth's sidereal day length, 10 year average

#filename_list.append('ANN0090-0099.ajlA211eoZoht100P10_X016.nc')  # 3

# Rotating with 64 x Earth's sidereal day length, 10 year average

#filename_list.append('ANN0090-0099.ajlA211eoZoht100P10_X064.nc')  # 4

# Rotating with 128 x Earth's sidereal day length, 50 year average
#filename_list.append('ANN0150-0199.ajlA211eoZoht100P10_X128.nc')  # 5

#########################################################################################################


print("All filenames")
print(filename_list, len(filename_list))


def tsurf_vs_lat_AJL(file):
    yaxis_tsurf_mean = []
    row_AJL = []
    data_ajl = file_dataset['rh'][:]  # totcld (TOTAL CLOUD COVER) från ajl
    lat_AJL = file_dataset['plm'][:]  # 1 Millibar = 1 Hectopascal

    xaxis_lat = lat_AJL

    row, collumn = np.array(data_ajl), np.array(data_ajl.T)  # Transpose of data to reach columns

    for i in range(0, len(row)):
        # Y-AXIS
        var = np.mean(data_ajl[i] + 273.15)  # Change to Kelvin
        yaxis_tsurf_mean.append(var)
        row_AJL.append(row[0][i])

    lat_AJL = np.array(lat_AJL)
    row_AJL = np.array(row_AJL)
    print(lat_AJL.shape)
    print(row_AJL.shape)
    return lat_AJL, row_AJL, data_ajl


def lat_from_aij(file):
    lat_AIJ = data_set['lat'][:]  # lat
    lat_AIJ = np.array(lat_AIJ)
    return lat_AIJ


for file in file_for_lat:
    data_set = nc.Dataset(file)
    lat_aij = lat_from_aij(data_set)

k = 0
for file in filename_list:
    file_dataset = nc.Dataset(file)

    lat_ajl, row_ajl, data_ajl = tsurf_vs_lat_AJL(file_dataset)

    # ____________________________________________________________________________________________ #
    ##################################SQUAREPLOTS###################################################
    # ____________________________________________________________________________________________ #
    #  http://matplotlib.org/basemap/users/mapsetup.html

    fig, ax2 = plt.subplots()
    ax2.set_title("rh in " + namelist[k], fontname='Franklin Gothic Medium', fontsize=15)
    #ax2.grid(True)
    k += 1
    # Making the square plots
    label_x = ['90S', '60s', '30s', '0', '30N', '60N', '90N']  # Labels
    label_y = [ '200', '400', '600', '800'] # '10', '100',

    # Cosmetics
    colors_lower = plt.cm.gist_ncar(np.linspace(0.10, 0.75, 140))
    colors_middle = plt.cm.seismic(np.linspace(0.95, 1., 15))
    colors_upper = plt.cm.BuPu(np.linspace(0.85, 1., 20))
    colors = np.vstack((colors_lower, colors_middle, colors_upper))

    norm = mpl.colors.Normalize(vmin=0, vmax=100)
    #cmap = mcolors.LinearSegmentedColormap.from_list('mycmap', colors)
    cmap = "Blues_r"
    levels = np.arange(0, 105, 5)
    #levels = 9
    # Plot data
    cf = plt.contourf(lat_aij, lat_ajl, data_ajl, cmap=cmap, levels=levels)

    plt.gca().invert_yaxis()
    plt.xticks(np.arange(lat_aij.min(), lat_aij.max() + 30, 30), label_x)
    plt.yticks([200, 400, 600, 800], label_y) # 10, 100,
    #plt.colorbar(ticks=np.arange(0, 110, 10), orientation='horizontal')
    plt.ylabel('Pressure (hPa)', fontname='Franklin Gothic Medium', fontsize=15)
    plt.xlabel('Latitude (°N)', fontname='Franklin Gothic Medium', fontsize=15)
    #plt.xlabel(f"Max data = {np.amax(data_ajl):.3f} Min data = {np.amin(data_ajl):.3f} Mean data = {np.mean(data_ajl):.3f}")
print(namelist)
plt.show()
