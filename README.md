# ASL_ASCII_Translator

Translate American Sign Language (ASL) inputs into clear ASCII art. This repository provides a simple pipeline that maps recognized hand poses to ASCII representations for education, accessibility, and demos.

## Features

- ASL to ASCII mapping with a human editable lookup file
- Command line scripts and a minimal web demo
- Modular design, easy to extend with new recognizers or mappings
- Optional hand detection with common CV stacks, MediaPipe or Google APIs

## Project Structure

```
ASL_ASCII_translator/
├─ main.py                     # Core translator runner
├─ counting_WORKING.py         # Example for counting gestures
├─ handrecognitionGOOGLE.py    # Example integration with a Google based recognizer
├─ hand.txt                    # Mapping file, ASL tokens to ASCII blocks
├─ index.html                  # Minimal web page to visualize ASCII output
├─ style.css                   # Styles for the web demo
└─ requirements.txt            # Optional dependencies
```

## Quick Start

### 1) Clone the repository
```bash
git clone https://github.com/szwedk/ASL_ASCII_translator.git
cd ASL_ASCII_translator
```

### 2) Install dependencies
If a requirements file is present:
```bash
pip install -r requirements.txt
```
If not, install what you need for your path:
- Core usage: Python 3.7 or newer
- CV options: opencv-python, mediapipe, numpy
- Google recognition: relevant Google SDKs and credentials

### 3) Run the translator
```bash
python main.py
```

### 4) Try the counting demo
```bash
python counting_WORKING.py
```

### 5) Google hand recognition example
Configure credentials inside `handrecognitionGOOGLE.py`, then run:
```bash
python handrecognitionGOOGLE.py
```

### 6) Web demo
Open `index.html` in your browser to render ASCII output. Adjust `style.css` as needed.

## Configuration

### Mapping file, `hand.txt`
Define gesture tokens and their ASCII blocks. Example:
```
A:
  ###
  # #
  ###
  # #
  # #

B:
  ####
  #  #
  ####
  #  #
  ####
```
Guidelines:
- One gesture token per block, followed by its ASCII lines
- Keep a consistent width and height for alignment
- Use a monospace font in terminals and the web demo

## Extending

- Add new gestures in `hand.txt`, update parsing in `main.py` if you change the format
- Add a new recognizer module that outputs the same tokens
- Wrap the translator in a Flask or FastAPI service for a richer UI
- Build a real time mode that reads webcam frames and streams ASCII to console or web

## Troubleshooting

- Misaligned ASCII: normalize widths in `hand.txt`, use a monospace font
- No recognizer output: test with static tokens first, then verify CV libraries
- Credential issues: confirm environment variables and API keys for any external SDKs

## Roadmap

- Unified recognizer interface for easy swapping
- Real time webcam demo with MediaPipe
- Export utilities for text, PNG, or GIF
- Basic unit tests for mapping integrity

## Contributing

Issues and pull requests are welcome. Open an issue to discuss significant changes before submitting a PR. Keep commits focused, include clear descriptions, and add tests when practical.

## License

Choose a license that fits your goals, for example MIT or Apache 2.0. Add a `LICENSE` file and update this section accordingly.

## Acknowledgements

- Community tools for hand detection, for example MediaPipe and OpenCV
- Open source contributors who maintain ASCII art utilities and monospace fonts

Created by [Kamil Szwed](https://github.com/szwedk)
