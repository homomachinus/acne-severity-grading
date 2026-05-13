import flet as ft
from ultralytics import YOLO
import cv2
import os
from PIL import Image


# ===============================
# LOAD MODEL
# ===============================
MODEL_PATH = "runs/train/acne part 3/weights/best.pt"
model = YOLO(MODEL_PATH)


# ===============================
# FUNGSI INFERENCE
# ===============================
def run_inference(image_path):
    results = model.predict(
        source=image_path,
        imgsz=640,
        conf=0.15,
        save=False
    )

    result = results[0]

    # Ambil gambar asli dalam bentuk numpy
    img = result.orig_img.copy()

    # Gambar bounding box
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]

        label = f"{class_name} {conf:.2f}"

        # Bounding box
        cv2.rectangle(
            img,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Label background
        cv2.rectangle(
            img,
            (x1, y1 - 25),
            (x1 + 160, y1),
            (0, 255, 0),
            -1
        )

        # Label text
        cv2.putText(
            img,
            label,
            (x1, y1 - 7),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )

    # Simpan hasil
    output_path = "result_inference.jpg"
    cv2.imwrite(output_path, img)

    return output_path, len(result.boxes)


# ===============================
# UI FLET
# ===============================
def main(page: ft.Page):
    page.title = "YOLO Acne Detection"
    page.window_width = 900
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.LIGHT

    selected_image_path = {"path": None}

    title = ft.Text(
        "YOLO Acne Detection",
        size=28,
        weight=ft.FontWeight.BOLD
    )

    status_text = ft.Text(
        "Silakan import gambar terlebih dahulu.",
        size=14
    )

    image_preview = ft.Image(
        src="",
        width=500,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        visible=False
    )

    # ===============================
    # FILE PICKER CALLBACK
    # ===============================
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            selected_image_path["path"] = file_path

            image_preview.src = file_path
            image_preview.visible = True

            status_text.value = f"Gambar dipilih: {os.path.basename(file_path)}"
            page.update()

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    # ===============================
    # TOMBOL IMPORT
    # ===============================
    def import_image(e):
        file_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE
        )

    # ===============================
    # TOMBOL INFERENCE
    # ===============================
    def start_inference(e):
        if selected_image_path["path"] is None:
            status_text.value = "Belum ada gambar yang dipilih."
            page.update()
            return

        status_text.value = "Sedang melakukan inference..."
        page.update()

        output_path, total_detection = run_inference(selected_image_path["path"])

        image_preview.src = output_path
        image_preview.visible = True

        status_text.value = f"Inference selesai. Jumlah deteksi: {total_detection}"
        page.update()

    import_button = ft.ElevatedButton(
        text="Import Gambar",
        icon=ft.Icons.IMAGE,
        on_click=import_image
    )

    inference_button = ft.ElevatedButton(
        text="Start Inference",
        icon=ft.Icons.PLAY_ARROW,
        on_click=start_inference
    )

    page.add(
        ft.Column(
            controls=[
                title,
                status_text,
                ft.Row(
                    controls=[
                        import_button,
                        inference_button
                    ],
                    spacing=15
                ),
                ft.Container(
                    content=image_preview,
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    border_radius=10,
                    padding=10,
                    width=550,
                    height=450
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )


if __name__ == "__main__":
    ft.app(target=main)