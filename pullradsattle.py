# python 3

from spacetrack import SpaceTrackClient
import spacetrack.operators as op
import datetime


def pullTLEs(stuser, stpass, cubesats):
    #account info for space-track.org
    #free account with minimal verification
    st = SpaceTrackClient(stuser, stpass)


    #list of the cubesats wanted
    # cubesats = [43377, 43378, 43553]
    #printing off the list of values that will be pulled from the tle database

    #lines for a file
    lines = st.tle_latest(norad_cat_id=cubesats,ordinal=1,format='3le')
    print(lines)


    with open('tle.txt', 'w') as fp:
        for line in lines:
            fp.write(line)




if __name__ == "__main__":

    stuser = "exampleEmail@sample.org"
    stpass = "examplePassword"

    #These are your NoradIDs you're looking for.
    cubesats = [40377, 40378, 43553]

    pullTLEs(stuser, stpass, cubesats)
