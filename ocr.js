const Tesseract = require('tesseract.js');

process.stdin.on('data', async (data) => {
        const result = await Tesseract.recognize(
            data,
            'eng'
        );

        // Filter out only the recognized text
        const recognizedText = result.data.text;

        // Output the recognized text
        process.stdout.write(recognizedText);
});