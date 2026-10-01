from flask import Flask, render_template, request, send_file
from urllib.parse import urljoin, urlparse
import tempfile
import subprocess
import os

app = Flask(__name__)


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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():

    m3u8_url = request.form.get("m3u8_url", "").strip()

    uploaded = request.files.get("m3u8_file")

    base_url = request.form.get("base_url", "").strip()

    temp_dir = tempfile.mkdtemp()

    final_m3u8 = os.path.join(temp_dir, "final.m3u8")

    output_file = os.path.join(temp_dir, "video.mkv")

    try:

        if uploaded and uploaded.filename:

            content = uploaded.read().decode("utf-8")

            fixed = fix_m3u8(content, base_url)

            with open(final_m3u8, "w", encoding="utf8") as f:
                f.write(fixed)

            input_source = final_m3u8

        else:

            input_source = m3u8_url

        cmd = [
            "ffmpeg",
            "-y",
            "-protocol_whitelist",
            "file,http,https,tcp,tls",
            "-i",
            input_source,
            "-c",
            "copy",
            output_file
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:

            return f"""
            <h2>FFmpeg Error</h2>
            <pre>{result.stderr}</pre>
            """

        return send_file(
            output_file,
            as_attachment=True,
            download_name="video.mkv"
        )

    except Exception as e:

        return str(e)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )