# python 3

from spacetrack import SpaceTrackClient
import spacetrack.operators as op
import datetime

#account info for space-track.org
#free account with minimal verification
st = SpaceTrackClient('username', 'password')

#list of the cubesats wanted
cubesats = [225544, 43546,43547,43548,43549,43550,43551,43552,43553,43554]

#printing off the list of values that will be pulled from the tle database

#lines for a file
lines = st.tle_latest(norad_cat_id=cubesats,ordinal=1,format='3le')
print(lines)


with open('tle.txt', 'w') as fp:
    for line in lines:
        fp.write(line)
