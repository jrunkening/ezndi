# ezndi

A simple ndi wrapping in python

## Before started

As of January 2025, the latest version of NumPy that supports Python 3.8 is NumPy 1.24.4, released on June 26, 2023.
NumPy follows a support policy that maintains compatibility with Python versions released within the prior 42 months, with a minimum support for the two latest minor versions.
Since Python 3.8 was released in October 2019, support for it was maintained until April 2023.
Therefore, NumPy versions 1.25.0 and later, released after June 2023, no longer support Python 3.8.
If you're using Python 3.8, it's recommended to upgrade to a newer Python version to take advantage of the latest NumPy features and improvements.
Alternatively, you can continue using NumPy 1.24.4, which remains compatible with Python 3.8.

In this project, we still support Python 3.8 for our own reason and will soon narrow the range to Python >=3.10.
Therefore, one has to install numpy before this package.

For develop this package, since `distutils` is removed after Python >=3.12, use Python 3.11.

## Installation

```sh
pip install numpy
pip install git+https://github.com/jrunkening/ezndi.git
```

If you are using poetry, due to the reason that NumPy 1.24.4 does not support PEP 517 builds.
You have to install numpy manually before install this package

```sh
pip install numpy
poetry add git+https://github.com/jrunkening/ezndi.git
```

## Quick start

For running the example code:

```sh
python .\example\send_rand.py
```

For building your own broadcast loop:

```py
initialize_ndi()
sender = create_ndi_sender("sender name")
while True: # loop to broadcast random image
    try:
        image = numpy.random.rand(720, 1280, 3) # random image
        send_frame(sender, image) # send
    except KeyboardInterrupt: # if you want to stop broadcasting, press Ctrl+C
        break
destroy_ndi_sender(sender)
destroy_ndi()
```
