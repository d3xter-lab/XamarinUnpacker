# XamarinUnpacker

XamarinUnpacker is a tool to unpack Android native library compiled using Xamarin.Android.

# Usage

To decompress a native library file run the script as follows:
```
python3 XamUnpack.py -i libmonodroid_bundle_app.so
```

If the output path is not specified, DLL files will be extract in `output` directory.

To specify a directory run the script as follows:
```
python3 XamUnpack.py -i libmonodroid_bundle_app.so -o files
```