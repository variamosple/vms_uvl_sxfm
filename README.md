<h1 align="center">
  Variamos Project transformation UVL-SXFM Microservice
</h1>

## Description
```
Microservice that allows transforming projects from UVL and SXFM format to JSON in Variamos.
```

## Building of the project
```
docker build --no-cache --progress plain -t vms_uvl_sxfm .\ 
```

### Project deployment
```
docker run -p 10001:10001 --rm --name vms_uvl_sxfm -t vms_uvl_sxfm
```
# API Documentation

This document outlines the available endpoints and their usage for the project's API.

---