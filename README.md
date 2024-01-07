# Object Detection and Text Extraction System

This repository contains code for object detection using OpenCV and a pre-trained model based on the COCO dataset. It also includes text extraction from images using Tesseract OCR. The system supports both image files and real-time object detection through the laptop's camera.

## Object Detection

### Setup
- The system uses OpenCV for object detection. Install the required library using:
  ```bash
  pip install opencv-python
  ```

### Usage
- For object detection from an image file, use `cv2.imread()` to read the image.
- To access the camera in real-time, use `cv2.VideoCapture(0)` with `0` as the parameter.
- Adjust video properties using `cap.set(propId, value)`, where `propId` identifies the video property, and `value` is the desired value.
- Bounding boxes are commonly used to define an object's position, specified by the coordinates of the upper-left and lower-right corners.

### Example
- Use `cv2.rectangle()` to draw a rectangle on an image.
- Use `cv2.putText()` to add text to an image.
- Display images using `cv2.imshow()` and wait for key input with `cv2.waitKey()`.

## Text Extraction

### Setup
- The text extraction system utilizes Tesseract OCR. Install the required library using:
  ```bash
  pip install pytesseract
  ```

### Usage
- Configure the Tesseract path using `pytesseract.tesseract_cmd`.
- Read an image using `cv2.imread()` and convert it to RGB using `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` since Tesseract works with RGB images.

### Text Recognition
- Use `pytesseract.image_to_string()` to extract text from the image.
- Detect and distinguish individual characters using the `image_to_boxes()` method.

### Bounding Boxes
- Create bounding boxes around characters using `cv2.rectangle()` and label each character with `cv2.putText()`.

### Real-Time Application
- Implement the code for real-time text extraction from the camera feed.

## How to Use
1. Clone this repository to your local machine.
2. Install the required dependencies for both object detection and text extraction using the respective commands mentioned above.
3. Customize the code as needed for your use case.
4. Run the code to perform object detection and text extraction.

Feel free to explore and adapt the code according to your specific requirements. If you encounter any issues or have questions, refer to the documentation or me.

Happy detecting and extracting!
