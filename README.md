# Loyalty System

## Layout

The code is organized into client, server, and proto directories.

The proto directory contains the message and service specifications for how the different parts of the system communicate. This is shared across the clients and server.

This is all stored as [Protocol Buffers](https://developers.google.com/protocol-buffers/).

The clients and server both use [GRPC](http://www.grpc.io/) to communicate using the specifications in the protobufs.


## Build
To avoid making everyone set up the build on their platform, the already generated
protocol buffers and GRPC bindings are included already committed in this repo.

If you would like to rebuild them, look at the instructions below:

To build and work with this system, you will require both GRPC and protocol buffers.

### Protobufs
Refer to the protocol buffer documentation for your platform. On OSX, 
```
brew install protobuf
```


### GRPC
For the python portions, run the commands:

```
pip install grpcio grpcio-tools
```
Coming soon.

## Test
Coming soon.

## Run

To run the server you need to have GRPC installed (see above).

Further instructions coming soon.
