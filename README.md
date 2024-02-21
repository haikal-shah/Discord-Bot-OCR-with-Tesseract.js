## Installation

1. Clone the repository

2. Install Node.js, including Tesseract.js:

```bash
npm install tesseract.js
```

3. (Optional) If you plan to use a different language for OCR, you may need to download additional language data files for Tesseract.js. You can find these files on the [Tesseract-OCR GitHub page](https://github.com/tesseract-ocr/tessdata).

## Usage

1. Insert your Discord bot token in `ocr_bot.py`:

```python
TOKEN = "{insert your token here}"
```

2. Run the bot:

```bash
python ocr_bot.py
```

3. In your Discord server, use the bot by uploading an image and using the `!ocr` command:

```
!ocr
```

## How it works

- When a user uploads an image and uses the `!ocr` command, the bot extracts the image data and sends it to a Node.js script (`ocr.js`).
- The Node.js script utilizes Tesseract.js to perform OCR on the image data.
- The recognized text is then sent back to the Python bot, which sends it as a message in the Discord channel.

## Customize language

You can customize the language for OCR by changing the language code in `ocr.js`:

```javascript
const result = await Tesseract.recognize(
    data,
    'eng' //Change language here
);
```

Replace `'eng'` with the appropriate [language code](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html).


## License

This project is licensed under the MIT License.

---
