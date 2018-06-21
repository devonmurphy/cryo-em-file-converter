#!/usr/bin/python
import sqlite3
import os
from time import localtime, strftime

DATABASE_NAME = os.path.split(os.getcwd())[1] + ".db"
MAGNIFICATION = "36000.000000"
STAR_HEADER = '''
data_

loop_
_rlnMicrographName #1
_rlnDefocusU #2
_rlnDefocusV #3
_rlnDefocusAngle #4
_rlnVoltage #5
_rlnSphericalAberration #6
_rlnAmplitudeContrast #7
_rlnMagnification #8
_rlnDetectorPixelSize #9
'''

def get_sql_data():
    data = "" 
    filename = []
    pixel_size = []
    defocus1 = []
    defocus2 = []
    defocus_angle = []
    amplitude_contrast = []
    voltage = []
    spherical_aberration = []
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("select filename, pixel_size from image_assets")
    for row in cursor:
        filename.append(str(row[0]))
        pixel_size.append(str(row[1]))

    cursor.execute("select DEFOCUS1, DEFOCUS2, DEFOCUS_ANGLE, AMPLITUDE_CONTRAST from estimated_ctf_parameters")
    for row in cursor:
        defocus1.append(str(row[0]))
        defocus2.append(str(row[1]))
        defocus_angle.append(str(row[2]))
        amplitude_contrast.append(str(row[3]))

    cursor.execute("select VOLTAGE, SPHERICAL_ABERRATION from movie_assets")
    for row in cursor:
        voltage.append(str(row[0]))
        spherical_aberration.append(str(row[1]))

    for row in range(0,len(filename)):
        data += "  "+"   ".join([filename[row],defocus1[row],defocus2[row],defocus_angle[row],voltage[row],spherical_aberration[row],amplitude_contrast[row],str(MAGNIFICATION),pixel_size[row]])+"\n"
    return data

def write_star_file(data):
    writeFileName = "micrograph"+strftime("-%Y-%m-%d--%H-%M-%S", localtime())+".star"
    writeFile = open(writeFileName,'w')
    writeFile.write(STAR_HEADER)
    writeFile.write(data)
    writeFile.write("\n")
    writeFile.close()
    print "*********************************************************************************************"
    print "New Starfile created at "+ writeFileName
    print "*********************************************************************************************"
        
if __name__ == "__main__":
    data = get_sql_data()
    write_star_file(data)
