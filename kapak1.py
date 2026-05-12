import cv2
import os

# Path video
video_path = "fr.mp4"

# Folder output
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# Buka video
cap = cv2.VideoCapture(video_path)

# Ambil FPS (frame per second)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS Video: {fps}")

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Simpan 1 frame setiap 1 detik
    if frame_count % int(fps) == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print("Selesai!")