import PIL.Image
import PIL.ExifTags
from gmplot import gmplot
img = PIL.Image.open("rembacka.jpg")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k,v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

#print(exif)
north = exif['GPSInfo'][2]
east = exif['GPSInfo'][4]
print(f'North: {north}\nEast: {east}\n')

lat = ((((north[0]*60)+north[1])*60)+north[2])/60/60
long = ((((east[0]*60)+east[1])*60)+east[2])/60/60
lat, long = float(lat), float(long)
print(f'Lat: {lat}\nLong: {long}\n')

gmap = gmplot.GoogleMapPlotter(lat, long, 12)

gmap.marker(lat, long, "cornflowerblue")
gmap.draw("location.html")