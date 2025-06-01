import subprocess
import whisper
import os

VIDEO_DIR = "./video"

# Load Whisper model once
print("🧠 Loading Whisper model...")
model = whisper.load_model("medium")

# Loop through all video files
for filename in os.listdir(VIDEO_DIR):
  if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
    video_path = os.path.join(VIDEO_DIR, filename)
    base_name = os.path.splitext(filename)[0]
    audio_path = os.path.join(VIDEO_DIR, f"{base_name}.wav")
    output_path = os.path.join(VIDEO_DIR, f"{base_name}.txt")

    print(f"\n🔊 Extracting audio from: {filename}")
    subprocess.run([
        "ffmpeg", "-y", "-i", video_path,
        "-vn", "-acodec", "pcm_s16le",
        "-ar", "16000", "-ac", "1",
        audio_path
    ], check=True)

    print("🧠 Transcribing with Whisper...")
    result = model.transcribe(audio_path, word_timestamps=True)

    print("💾 Saving transcript...")
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            line = f"[{segment['start']:.2f} - {segment['end']:.2f}]: {segment['text']}"
            print(line)
            f.write(line + "\n")

    print(f"✅ Audio saved to: {audio_path}")
    print(f"✅ Transcript saved to: {output_path}")

print("\n🎉 All videos processed!")