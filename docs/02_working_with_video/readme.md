Here are your **structured notes** from the transcript:

---

# 📘 OpenCV – Working with Video (Structured Notes)

---

## 1. What is a Video?

* A **video = sequence of images (frames)**
* Each image = **frame**
* When frames are shown rapidly → creates **illusion of motion**
* Example: Flipbook concept 

---

## 2. Frames Per Second (FPS)

### Definition

* **FPS = number of frames displayed per second**

---

### Example 1: 1 FPS

* 1 frame per second
* 6 frames → 6-second video
* Output:

  * Looks **laggy**
  * Motion not smooth

---

### Example 2: 6 FPS

* 6 frames per second
* All frames shown within 1 second
* Output:

  * **Smoother motion**

---

### Key Insight

* Higher FPS → smoother video
* Lower FPS → choppy video

---

### Standard FPS Values

* **24 FPS** → Movies
* **30 FPS** → TV, YouTube, Netflix
* **60 FPS+** → Gaming, Sports
* **120+ FPS** → High-speed capture

---

### Slow Motion Concept

* Capture at very high FPS (e.g., 1200 FPS)
* Play at lower FPS → slow-motion effect

---

## 3. Codec (Very Important)

### Definition

* **Codec = algorithm for compressing & decompressing video**

---

### Why Codec?

* Videos have many frames → large size
* Codec helps:

  * Reduce size
  * Maintain quality

---

### File Format vs Codec

* File formats: `.mp4`, `.avi`, `.mkv`
* Codec determines **how data is stored inside these formats**

---

### Common Codecs

| Codec     | Use Case                    | Output Format |
| --------- | --------------------------- | ------------- |
| **mp4v**  | General purpose             | MP4, AVI      |
| **H.264** | Efficient, low quality loss | MP4, MKV      |
| **H.265** | Better compression, 4K/8K   | MP4, MKV      |

---

### FourCC

* **Four Character Code (FourCC)**
* Used to specify codec in OpenCV

---

## 4. Reading Video in OpenCV

### Step 1: Import

```python
import cv2
```

---

### Step 2: Load Video

```python
video = cv2.VideoCapture("mountain.mp4")
```

* Creates **VideoCapture object**
* Used to read frames

---

### Step 3: Read Frames

```python
ret, frame = video.read()
```

* `ret` → True/False (frame available or not)
* `frame` → image (NumPy array)

---

## 5. Display Video

```python
while True:
    ret, frame = video.read()
    
    if not ret:
        break
    
    cv2.imshow("Video Frame", frame)
```

---

## 6. Controlling Playback

```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```

### Explanation

* `waitKey(1)` → waits 1 ms between frames
* Returns key pressed
* `ord('q')` → ASCII of 'q'
* Press **q → exit loop**

---

## 7. Cleanup (VERY IMPORTANT)

```python
video.release()
cv2.destroyAllWindows()
```

⚠️ If not used:

* Memory issues
* Kernel crash possible

---

## 8. Writing Video (Saving Output)

---

### Step 1: Define Codec

```python
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
```

---

### Step 2: Get Frame Size

```python
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
```

---

### Step 3: Create Writer Object

```python
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))
```

⚠️ Must match:

* Width
* Height
* FPS

---

### Step 4: Write Frames

```python
while True:
    ret, frame = video.read()
    
    if not ret:
        break
    
    out.write(frame)
```

---

### Step 5: Release

```python
out.release()
video.release()
```

---

## 9. Important Notes

### ⚠️ Frame Processing Rule

* Always modify frame **after checking `ret`**

```python
if not ret:
    break

frame = frame + 20
```

---

### ⚠️ Common Errors

* Wrong FPS → video not saved properly
* Wrong frame size → corrupted video
* Not releasing objects → crash

---

## 10. Key Takeaways

* Video = sequence of frames
* FPS controls smoothness
* Codec controls compression
* `VideoCapture` → read video
* `VideoWriter` → save video
* Always release resources

---

If you want, I can:

* Convert next lecture
* Add diagrams (flow + pipeline)
* Or give you **interview-ready revision notes** 🚀
