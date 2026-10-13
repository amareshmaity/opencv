# OpenCV - Coordinate System in OpenCV

Detailed notes based on `transcript.txt`.

---

## 1. What This Lecture Covers

This lecture explains one of the most foundational ideas in OpenCV:

- the coordinate system used inside an image.

This concept is essential because many image operations depend on knowing exactly where something is located in the image.

---

## 2. Why Coordinates Matter in Computer Vision

Coordinates are needed whenever we want to work with a specific location or region in an image.

The lecture highlights that coordinates are important for tasks such as:

- cropping an image,
- drawing shapes,
- placing text,
- marking objects,
- selecting regions of interest.

Without coordinates, OpenCV would not know where to perform these operations.

---

## 3. Cropping Requires Coordinates

Cropping means extracting only the part of the image we are interested in.

For example:

- if an image contains a larger scene,
- and we only want one small box or object,

then we must define the exact region to cut out.

To do that, we need coordinates.

Usually, a crop is defined using:

- a starting point,
- and an ending point.

Those points tell OpenCV which rectangular portion should become the new image.

---

## 4. Drawing Shapes Requires Coordinates

The lecture also explains that drawing shapes depends on coordinates.

For example, if we want to draw a rectangle:

- one coordinate pair defines one corner,
- another coordinate pair defines the opposite corner.

So even for simple annotation tasks, coordinates are necessary.

This is why coordinate understanding is a basic requirement in image processing.

---

## 5. Placing Text Requires Coordinates

Coordinates are also needed when we want to place text on an image.

Suppose we want to write a label such as:

- `person`

on top of a detected region.

OpenCV still needs:

- the starting point of the text.

The ending point may depend on the width of the text, but the initial placement always starts from a coordinate.

So text annotation is also coordinate-based.

---

## 6. OpenCV Uses a Cartesian-Style Coordinate System

The lecture describes the OpenCV image coordinate system as a Cartesian-style coordinate system.

This means positions are represented using:

- `x`
- `y`

However, the image layout is slightly different from the standard graph layout many students first learn in mathematics.

---

## 7. Where the Origin Starts

One of the most important ideas in the lecture is the location of the origin.

In OpenCV:

- the origin is `(0, 0)`,
- and it starts at the **top-left corner** of the image.

This is a very important rule to remember.

Unlike the usual mathematical graph where the origin is often drawn at the bottom-left or center, OpenCV starts from the top-left corner.

---

## 8. How the `x` Axis Works

In OpenCV:

- the `x` axis runs horizontally,
- and it increases from **left to right**.

So:

- smaller `x` values are closer to the left side,
- larger `x` values are closer to the right side.

If the image width increases across the row, the `x` coordinate increases along that direction.

---

## 9. How the `y` Axis Works

In OpenCV:

- the `y` axis runs vertically,
- and it increases from **top to bottom**.

So:

- smaller `y` values are closer to the top,
- larger `y` values are closer to the bottom.

This is one of the biggest differences from the standard plotting intuition many learners already have.

---

## 10. Key Difference from Standard Graphs

The lecture points out that OpenCV coordinates do not behave like the usual graph we may imagine first.

In many standard mathematical plots:

- upward movement increases `y`.

But in OpenCV:

- downward movement increases `y`.

So OpenCV image coordinates should be understood in terms of image rows and columns, not the usual classroom graph direction.

---

## 11. Understanding a Point in the Image

If we specify a point such as:

- `x = 90`
- `y = 90`

then OpenCV interprets that as:

- move `90` units to the right from the left edge,
- move `90` units downward from the top edge.

That point becomes the exact location where an operation begins.

For example:

- text can begin there,
- a shape corner can be placed there,
- or a crop boundary can start there.

---

## 12. Coordinates in Cropping

The lecture explains cropping using two coordinate pairs:

- `x1, y1`
- `x2, y2`

These coordinates define the boundaries of the region we want to extract.

So for cropping:

- one point marks the starting corner,
- the other point marks the ending corner.

Everything inside that rectangular area becomes the cropped output image.

---

## 13. Coordinates in Rectangles

To draw a rectangle in OpenCV, we again need two points.

These points are usually:

- one corner of the rectangle,
- and the opposite corner.

So the rectangle is not just a shape drawn freely.

It is mathematically defined using coordinates.

---

## 14. Coordinates in Text Placement

When placing text in an image:

- OpenCV needs the point from which the text should begin.

That starting coordinate tells the library where to place the first character.

So text placement is also tied directly to the coordinate system.

---

## 15. Region of Interest Thinking

A useful mental model from the lecture is that coordinates help us isolate meaningful parts of an image.

For example:

- if one object is important,
- if one part of the image needs annotation,
- or if one box must be extracted,

then coordinates give us the precise control needed to work only on that region.

This is why coordinates are at the heart of region-based operations in OpenCV.

---

## 16. Core Rule to Remember

The entire lecture can be summarized into three key rules:

- origin starts at the **top-left corner**,
- `x` increases from **left to right**,
- `y` increases from **top to bottom**.

If these three rules are clear, most OpenCV coordinate tasks become much easier to understand.

---

## 17. Why This Topic Is Foundational

The coordinate system may look simple, but it supports many important computer vision tasks.

It is foundational because it is needed before we can properly understand:

- cropping,
- drawing,
- annotation,
- bounding boxes,
- object labeling,
- many later geometric transformations.

So this lesson is one of the building blocks for practical OpenCV work.

---

## 18. Key Takeaways

- OpenCV uses a Cartesian-style coordinate system.
- The origin `(0, 0)` is at the top-left corner of the image.
- The `x` axis increases from left to right.
- The `y` axis increases from top to bottom.
- Coordinates are required for cropping, drawing shapes, and placing text.
- A rectangular region is usually defined using two coordinate pairs.

---

## 19. Summary

This lecture introduces the OpenCV coordinate system, which is essential for understanding how positions are represented inside an image.

The main idea is simple:

- start from the top-left corner,
- move right to increase `x`,
- move downward to increase `y`.

This coordinate system is used in practical tasks like cropping images, drawing rectangles, and placing text labels. Once this foundation is clear, many later OpenCV operations become much easier to understand.
