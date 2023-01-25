# sprite-generator

Sprite generator from a directory of images, similar to [GlueIT](https://github.com/Kavex/GlueIT).
Run on OSX but can be build into other platforms. You can find a build in the dist directory.

Made in python 


## Requirements

```
python 3.7
Pillow 9.4
tkinterdnd2 0.3
pyinstaller 5.7 if you want to build
```

## Build command

With pyinstaller installed in your python environnement, you can build with:

```
pyinstaller -F -w main.py --additional-hooks-dir=. --icon=logo/logo.png
```



