# cryo-em-file-converter

# About
cryoConverter.py -- Creates a star file from a cisTEM database.

# Install
```
git clone https://github.com/Rick-Baker/cryo-em-file-converter
cd cryo-em-file-converter/
cp cryoConverter.py /usr/local/bin
```

# Usage
`cd` into the directory with the cisTEM database you want to convert then run: `cryoConverter.py`

# Important
Currently cryoConverter.py assumes that the sql3lite datbase name matches the current cisTEM working directory. For example, if your cisTEM project is called `18apr23g` then your database name should be `18apr23g.db` or else it will fail.
