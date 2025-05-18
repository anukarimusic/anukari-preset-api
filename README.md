# anukari-preset-api
APIs for programmatically editing preset files for the Anukari 3D Physics
Synthesizer (https://anukari.com). These APIs could be used, for example, to
create intricate presets with hundreds of entities that would be painstakingly
difficult to create manually.

# Background
Anukari's preset save files use the binary
[Google Protocol Buffer](https://protobuf.dev/) format. This is fast, efficient,
and type-safe, and offers API bindings in most languages. This repository has
a demo for parsing the protocol buffers in Python, but it would be very easy
to create the bindings for other languages as well.

# Setup and demo
A Python demo script to print the Anukari preset as JSON is included. Run the
following commands to install the required packages and run the demo:

```
$ cd anukari-preset-api
$ python3 -m venv .venv

[mac/linux]
$ source .venv/bin/activate

[win]
$ .venv\Scripts\activate

$ pip install "betterproto[compiler]" grpcio-tools
$ mkdir lib
$ python3 -m grpc_tools.protoc -I src --python_betterproto_out=lib src/model.proto
$ python3 -m src.print-preset .\src\example.ank
```

# Debugging preset files
While .proto files are type-safe, there are many other constraints that are not
expressed in the files directly. For example, some float fields have limited
ranges that are valid. Some ID fields need to correspond exactly between two
entities. There are limits on the number of entities, etc.

These things are not all going to get documented in the .proto files, as the
requirements are fairly complex. However, if you try to load a preset that
violates one of these constraints, Anukari should log a somewhat detailed error
message. The log files can be found in:

* **Windows**: C:\Users\\**YOURUSER**\AppData\Roaming\Anukari\logs\
* **MacOS**: /Users/**YOURUSER**/Library/Logs/Anukari/logs/

# Support
**NO OFFICIAL SUPPORT IS OFFERED FOR THIS REPOSITORY**. This is provided for
the convenience a very small number of advanced users. Anukari's software
development priority is improving the product itself. Feel free to ask questions
about this repository, but please understand that detailed help may not be
forthcoming. We will try to keep this repository up to date with the latest
Anukari release, but do not make any promises about that. Generally speaking,
presets created using the protos in this repository will work with all future
versions of Anukari, but not necessarily past versions of Anukari.

# Last updated
Anukari version 0.9.6

# License
See the LICENSE file.
