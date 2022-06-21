# SVG2PNG

![cover.png](./dst/Cover.png)

# Introduction
If you want to convert SVG files repeatedly, it is bothering to open and save files each time.
Then CairoSVG is a good python library for converting SVG to PNG.
But building a python environment is also bothering me, so this repository manages the following things.

- Dockerfile for environment to use python and CairoSVG
- python code for batch file conversion
- Memorandum for docker commands

# Installation
1. Install docker.
2. Build Dockerfile with following command.
```
docker build -t python-cairosvg:latest .
```


# Usage
## Single file conversion on macOS
1. Run docker image with mounting current directory as working directory.
```bash
docker run --rm -it -v $(pwd):/var/python python-dl bash
```

2. Put SVG file (ex. image.svg) to src directory.

3. Run cairosvg command.
```bash
cairosvg src/image.svg -o dst/image.png
```

## Multiple file conversion on macOS
1. Run docker image with mounting current directory as working directory.
```bash
docker run --rm -it -v $(pwd):/var/python python-cairosvg bash
```

2. Put SVG files (ex. image.svg) to src directory.

3. Run python script.
```bash
python convert.py
```

4. All SVG files inside ./src will be converted and saved to ./dst

## Cleanup old build after updating Dockerfile
If you build Dockerfile after updating it, the previous build may remain like following log.

```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
python-dl           latest              c6d6f509ae5b        3 seconds ago        1.21GB
<none>              <none>              6e119ff05b9e        About a minute ago   1.21GB  <- Previous build
python              latest              a4cc999cf2aa        2 days ago           929MB
```

Then you can cleanup these images by following command.

```bash
docker rmi $(docker images -qa -f 'dangling=true')
```
