## OCR Warzone Loadouts

The goal of this project is to create a microsservice that receives a image (print screen from loadout screen in cod warzone) and return the loadout in a text format, separated by `;`

## Install

### MacOs
```bash
brew install tesseract opencv node python3
```

### Linux

#### Manjaro / Arch Linux based
```bash
sudo pacman -S tesseract opencv nodejs python3
```

#### Debian / Ubuntu based
```bash
sudo apt install tesseract opencv nodejs python3
```

#### Fedora / Red hat based
```bash
sudo dnf install tesseract opencv nodejs python3
```

### Windows
For windows you'll have to download the binaries on each website, or you can use some package manager such as [Chocolatey](https://chocolatey.org/).
 - [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
 - [OpenCV](https://opencv.org/releases/)
 - [NodeJs](https://nodejs.org/en/download/)
 - [Python 3](https://www.python.org/downloads/)

### Python dependencies
```bash
pip install pytesseract opencv-python flask flask-cors pdf2image
```

## Run
```bash
python main.py
```

You must use `python 3` to run, if you have `python 2` and `python 3` installed, you'll probably need to use the alias for it:
```bash
python3 main.py
```

You can test the backend separated from the frontend with [cURL](https://curl.se/) and [jq](https://stedolan.github.io/jq/) or any API Testing Tools.

With the project running, you can run this from the root of the project:
```bash
curl -X POST http://localhost:5000 -F lang=eng -F "image=@images/en/grau.png" | jq
```
