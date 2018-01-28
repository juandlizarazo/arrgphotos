# Import google_streetview for the api module
# helpful links
# https://developers.google.com/maps/documentation/streetview/
# https://pypi.python.org/pypi/google-streetview
# https://rrwen.github.io/google_streetview/

import google_streetview.api

# Define parameters for street view api
SaylesLat=41.8266
SaylesLon=-71.4029823
IndiaPtLat=41.817603
IndiaPtLon=-71.3925556
SoutheastcampusLat=41.8262113
SoutheastcampusLon=-71.3975559
DowntownLat=41.827702
DowntownLon=-71.414918
RISDLat= 41.8258538
RISDLon=-71.40773680000001
Lats=[SaylesLat,IndiaPtLat,SoutheastcampusLat,DowntownLat,RISDLat]
Lons=[SaylesLon,IndiaPtLon,SoutheastcampusLon,DowntownLon,RISDLon]
colors=['blue','red','green','black','yellow']

urlbase='https://maps.googleapis.com/maps/api/staticmap?center=' # https://developers.google.com/maps/documentation/static-maps/intro
settings='&zoom=14&size=500x500&maptype=satellite'
staticKey='&key=AIzaSyA1vVaV_-sOQyCt9UWPxiX1hGmlRJMlRFw'
url=urlbase
for x in range(0,5):
	centralLat=Lats[x]
	centralLon=Lons[x]
	color=colors[x]
	color='&markers=color:'+color
	for m in range(1,8):
		for n in range(1,8):
			lat=centralLat+0.0005*(-4+m)
			lon=centralLon+0.0005*(-4+n)
			location=str(lat)+','+str(lon)
			params = [{
			  'size': '500x500', # max 640x640 pixels
			  'location': location,
			  'heading': '150',
			  'pitch': '10',
			  'key': 'AIzaSyDU900xzLG2Th6lr1HSDA2GmeHu8QM8Xf8'
			}]
	# Create a results object
			results = google_streetview.api.results(params)

	# Download images to directory 'downloads'
			results.download_links(location)
			results.save_links('links.txt')
			results.save_metadata('metadata.json')

	# range to test latitude: 41.83+- 0.03, longitude
	# 5 locations, 40 images per location
			if n==1 & m==1:
				url=url+str(lat)+','+str(lon)+settings+color
			else: 
				url=url+'%7C'+str(lat)+','+str(lon)
url=url+staticKey
print(url)

	# 20m 30m, 000 just below organ 



# https://maps.googleapis.com/maps/api/staticmap?center=63.259591,-144.667969&zoom=6&size=400x400
# &markers=color:blue%7Clabel:S%7C62.107733,-145.541936&markers=size:tiny%7Ccolor:green%7CDelta+Junction,AK
# &markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK"&key=YOUR_API_KEY