## [WIP]

In this project we are going to create a frontend in Vue and a backend with Python to process images and extract text.

## Install

### MacOs
```bash
brew install tesseract opencv node python3 poppler
```

### Linux

#### Manjaro / Arch Linux based
```bash
sudo pacman -S tesseract opencv nodejs python3 poppler
```

#### Debian / Ubuntu based
```bash
sudo apt install tesseract opencv nodejs python3 poppler-utils
```

#### Fedora / Red hat based
```bash
sudo dnf install tesseract opencv nodejs python3 poppler-utils
```

### Windows
For windows you'll have to download the binaries on each website, or you can use some package manager such as [Chocolatey](https://chocolatey.org/).
 - [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
 - [OpenCV](https://opencv.org/releases/)
 - [NodeJs](https://nodejs.org/en/download/)
 - [Python 3](https://www.python.org/downloads/)
 - [Poppler](https://poppler.freedesktop.org/)

## Run

### Backend
```bash
cd backend/
python main.py
```

You must use `python 3` to run, if you have `python 2` and `python 3` installed, you'll probably need to use the alias for it:
```bash
python3 main.py
```

You can test the backend separated from the frontend with [cURL](https://curl.se/) and [jq](https://stedolan.github.io/jq/) or any API Testing Tools.

With the project running, you can run this from the root of the project:
```bash
curl -X POST http://localhost:5000 -F "image=@images/SJ-BC-Hydro.pdf" | jq
```