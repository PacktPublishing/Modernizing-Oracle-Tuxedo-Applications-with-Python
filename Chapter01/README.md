# Docker image for development

Contains:

- Python3
- Tuxedo
- Python `tuxedo` module
- Exposes "WSL port" 5020 (FIXME)

Based on:

- https://github.com/oracle/docker-images/tree/master/OracleInstantClient
- https://github.com/oracle/docker-images/tree/master/Archive/OracleTuxedo

Go to http://www.oracle.com/technetwork/middleware/tuxedo/downloads/index.html and download Oracle Tuxedo 12cR2 (12.2.2) (Including Tuxedo, SALT and Jolt) for Linux x86-64 (64-bit) and place `tuxedo122200_64_Linux_01_x86.zip` in the same folder as `Dockerfile`


## Building 

`docker build -t tuxpy .`


## Running

Windows:

`winpty docker run -ti tuxpy bash`

Linux:

`docker run -ti tuxpy bash`
