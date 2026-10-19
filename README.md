# watermark-cli

Add a text watermark to an image from the command line.

```bash
pip install -r requirements.txt
python watermark.py foto.jpg "© Gery Super Shop"
python watermark.py foto.jpg "© Gery Super Shop" -o hasil.jpg --opacity 160
```

Watermark is drawn centered, white text with a black outline so it stays
readable on any background color (default opacity 128).
