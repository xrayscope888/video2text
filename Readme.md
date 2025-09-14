
# 🎧 Video Transcriber with Whisper

This tool extracts audio from video files and transcribes the speech using [OpenAI's Whisper](https://github.com/openai/whisper). It processes all video files in a folder and saves both `.wav` audio and `.txt` transcripts using the same filenames.

---

## Requirement


## 🚀 Features

- Extracts mono audio from videos using `ffmpeg`
- Transcribes audio with timestamps via Whisper
- Saves `.wav` and `.txt` files alongside the original video
- Batch processes all videos in the `./video` folder
- Supports `.mp4`, `.mov`, `.avi`, `.mkv`

---

## 📁 Folder Structure

```

project-root/
├── video/
│   ├── example.mp4
│   ├── example.wav
│   ├── example.txt
├── transcribe.py
└── README.md

````

---

## 🛠️ Requirements

- Python 3.8+
- `ffmpeg` (must be installed and accessible in your system PATH)
- Python packages:
  - `openai-whisper`
  - `torch`

### ✅ Install dependencies

```bash
pip install -U openai-whisper
pip install torch
````

Check if `ffmpeg` is installed:

```bash
ffmpeg -version
```

If not installed:

* **macOS**: `brew install ffmpeg`
* **Ubuntu**: `sudo apt install ffmpeg`
* **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

---

## 📦 Usage

1. Put your video files in the `./video/` folder.
2. Run the script:

```bash
python transcribe.py
```

3. You’ll get:

   * Extracted audio as `.wav`
   * Transcript as `.txt`

---

## 🧠 Output Example

For `demo.mp4`, you'll get:

```
demo.wav   # extracted audio
demo.txt   # transcript with timestamps
```

Example contents of `demo.txt`:

```
[0.00 - 4.50]: Welcome to the demo video.
[4.50 - 8.20]: This tool transcribes videos automatically.
```

---

## 📌 Customization

Change the Whisper model:

```python
model = whisper.load_model("medium")  # Options: tiny, base, small, medium, large
```

---

## 🧾 License

MIT License

---

## ✨ Credits

* [OpenAI Whisper](https://github.com/openai/whisper)
* `ffmpeg` for audio extraction

```
```
