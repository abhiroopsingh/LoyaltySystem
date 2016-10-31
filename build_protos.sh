python -m grpc.tools.protoc -Iproto --python_out=server/genproto --grpc_python_out=server/genproto ./proto/*

# Copy the proto files to the right location for the android build.
cp -r proto ./client/pointofsale/app/src/main
cp -r proto ./client/customer/app/src/main
