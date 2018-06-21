# cryo-em-file-converter

# About
cryoConverter.py -- Creates a star file from a cisTEM database

cryoConverter.py extras these data elements
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
`cd` into the directory with the cisTEM database you want to convert then run `cryoConverter.py`

# Important
`_rlnMagnification` is hardcoded to be `36000.000000` until I figure out how to get this.

Currently cryoConverter.py assumes that the sql3lite datbase name matches the current cisTEM working directory. For example, if your cisTEM project is called `18apr23g` then your database name should be `18apr23g.db` or else it will fail.
