# 🎬 M3U8 to MKV Downloader

A simple Python Flask-based tool to download and convert `.m3u8` streams into `.mkv` files.  
It parses the playlist, fixes relative URLs, and uses `ffmpeg` to handle the actual download and conversion.

---

## 🚀 Features
- Parse and fix `.m3u8` playlists with relative paths.
- Download video segments and merge them into a single `.mkv` file.
- Web interface built with Flask for easy usage.
- Temporary file handling for clean execution.

---

## 📦 Requirements
- Python 3.8+
- Flask
- ffmpeg (must be installed and available in PATH)

Install dependencies:
```bash
pip install flask

Make sure ffmpeg is installed:

Linux/macOS: sudo apt install ffmpeg or brew install ffmpeg

Windows: Download from ffmpeg.org (ffmpeg.org in Bing) and add to PATH.
```
## 🛠️ Usage
Clone this repository:
```
bash
git clone https://github.com/yourusername/m3u8-to-mkv.git
cd m3u8-to-mkv
```
Run the Flask app:
```
bash
python app.py
```

Open your browser at:
```
http://127.0.0.1:5000
```
or
use ipconfig on win to find your ip then port 
```
ip:5000
```
Enter the .m3u8 URL and click Download.
The tool will:

Fix the playlist URLs.

Call ffmpeg to download and merge segments.

Provide the .mkv file for download.

## 📂 Project Structure
```
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Web UI
└── README.md           # Documentation
```
Example
```
def fix_m3u8(content, base_url):
    lines = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            lines.append("")
            continue
        if line.startswith("#"):
            lines.append(line)
            continue
        lines.append(urljoin(base_url, line))
    return "\n".join(lines)
```
##📜 License
MIT License – feel free to use and modify.

Would you like me to also draft a **sample `index.html` template** for the Flask UI so the README feels complete with frontend instructions?
