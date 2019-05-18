# ubiquitous-octo-pancake

Based partly on a presentation from 
https://github.com/jcamier/dfw_google_vision_talk
though this is for experimentation with
AWS Rekognition instead of Google Cloud's
Vision.

* Requires Python 3 to be installed
* Also requires the Boto 3 library

Text Recognition Test:
```
./rekognition.py text --filename "<path to image file>"
```

Celebrity Recognition Test:
```
./rekognition.py celebrity --filename "<path to image file>"
```

Label Recognition Test:
```
./rekognition.py label --filename "<path to image file>"
```

Alternatively, omit the `--filename` parameter to use the
default images in this repository.
