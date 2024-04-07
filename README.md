## Table of Contents
- [Introduction](#LittleScyllaOCR)
- [Installation](#Installation)
- [Notes](#Notes)
- [Contributing](#contributing)
<a id="introduction"></a>
# LittleScyllaOCR
LittleScyllaOCR is a Python application used to parse smite post-match stats screenshots for statistical analysis. 
It is built using [PyTesseract](https://pypi.org/project/pytesseract/) which is a wrapper for Google's [Tesseract](https://en.wikipedia.org/wiki/Tesseract_(software)).
It can parse images with a success rate of 95% (imperfections indicated [here](#imperfections))


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.


<a id="installation"></a>
## Required dependencies
**_numpy_**
```bash
pip install numpy
```
**_Opencv_**
```bash
pip install opencv-python
```
**_pytesseract_**
```bash
pip install pytesseract
```
**_Prompt-toolkit_** (if you want to run Interface package.)
```bash
pip install prompt-toolkit
```


## Notes:
1. Create a new folder to store processed images.
2. Navigate to  `LittleScyllaOCR/EngineOCR` and create a `/temp` folder.
3. Navigate to `LittleScyllaOCR/EngineOCR` and create a `debug` folder. (Required when enabling the debug flag.)

### Supported Enums.
- Current supported output formats (Enums `OUTPUT.type`:
  - Console: `OUTPUT.CONSOLE` (default)
  - Txt file: `OUTPUT.TXT`
  - XML file: `OUTPUT.XML` (coming soon)
  - xlsx file: `OUTPUT.XLSX` (coming soon)
  - CSV file: `OUTPUT.CSV`
  - JSON file: `OUTPUT.JSON`

### Shortcomings:
  - This OCR engine tends to struggle in the second line of some images (The KDA line), as sometimes `/` next to a 1 is recognized as a `7`.
  - Somtimes if a line contain many zeros (usually player healing, wards, Structure_dmg), this engine fails to recognize them as zeros (This should be patched, however, watch out for them)
  - Rarely the 5th player on the Order team, but mostly the 1st player on the Chaos team tend to include a `7` in the middle of their stats (some stats), this is due to the golden border that separates both teams.

## Usage
### Interface Usage:
Navigate to the root `LittleScyllaOCR/Interface`
```bash
python3 main.py
```

### Custom Usage:
Driver function is located in `LittleScyllaOCR/EngineOCR/OCRDriver.py`
#### `startOCR(imagePath, outputFormat)`
Description of the `startOCR`:
- `imagePath`: Path to an image that will be processed.
- `outputFormat`: Choose one of the supported enums.
- Returns: Description of the return value.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.