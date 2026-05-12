from ultralytics import YOLO
import cv2
import os

def main():
    # Load model
    model = YOLO("runs/train/helmet30-yolo11n/weights/best.pt")

    # URL video / stream
    video_url = r"d:\modelhelm\fr.mp4"

    # Folder output
    output_folder = "results_video"
    os.makedirs(output_folder, exist_ok=True)

    # Buka video stream
    cap = cv2.VideoCapture(video_url)

    if not cap.isOpened():
        print("Gagal membuka video/stream")
        return

    # Ambil properti video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Kalau FPS gagal kebaca, kasih default
    if fps == 0 or fps != fps:
        fps = 25

    output_path = os.path.join(output_folder, "hasil_deteksi.mp4")

    # Simpan hasil video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Selesai atau gagal ambil frame")
            break

        # Inferensi
        results = model(frame, conf=0.2)

        # Ambil hasil annotated
        annotated = results[0].plot()

        # Simpan ke video output
        out.write(annotated)

        # Tampilkan realtime
        cv2.imshow("Helmet Detection Video", annotated)

        frame_count += 1
        print(f"Processed frame: {frame_count}")

        # Keluar dengan q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Selesai! Hasil video disimpan di: {output_path}")

if __name__ == "__main__":
    main()