# cryo-em-file-converter

# About
cryoConverter.py -- Creates a star file from a cisTEM database

cryoConverter.py extracts these data elements
```
_rlnMicrographName #1
_rlnDefocusU #2
_rlnDefocusV #3
_rlnDefocusAngle #4
_rlnVoltage #5
_rlnSphericalAberration #6
_rlnAmplitudeContrast #7
_rlnMagnification #8
_rlnDetectorPixelSize #9
```

# Install
```
git clone https://github.com/Rick-Baker/cryo-em-file-converter
cd cryo-em-file-converter/
sudo cp cryoConverter.py /usr/local/bin
```

# Usage

To create a star file from a cisTEM database the user must provide the magnification of the microscope that captured the data with the -m or --magnification option.

```
cryoConverter.py -d path/to/cisTEM/database.db -m 36000
```

If the -d or --database arguement is not provided, cryoConverter.py assumes that the current working directory is the cisTEM database name.
