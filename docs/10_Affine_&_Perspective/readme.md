# OpenCV - Affine and Perspective Transformations

Detailed notes based on `transcript.txt`.

---

## 1. What This Lecture Covers

This lecture introduces two important geometric image transformations:

- affine transformation,
- perspective transformation.

These are more advanced than simple flip or fixed-angle rotation operations.

They are used when we want finer control over how image points are mapped from the input image to the output image.

---

## 2. Why These Transformations Matter

The lecture explains that affine and perspective transformations are useful when basic image operations are no longer enough.

They are especially important for tasks such as:

- rotating an image by arbitrary angles like `45` degrees,
- scaling an image,
- shifting an image,
- shearing an image,
- correcting distortions,
- aligning images,
- changing the viewing perspective.

These transformations are also widely used in image augmentation and preprocessing.

---

## 3. Motivation: Why Basic Rotation Is Not Enough

The lecture compares simple rotation with affine-based rotation.

With a simple fixed rotation such as portrait-to-landscape rotation, the transformation is straightforward.

But when we rotate an image by an angle like `45` degrees:

- some points move to completely new locations,
- some parts of the image may go outside the visible frame,
- empty regions may appear in the output image,
- some original information may be lost near the boundaries.

This is why we need a more general transformation framework.

---

## 4. Core Idea: Mapping Old Coordinates to New Coordinates

Both transformations work by mapping original image coordinates to new coordinates.

If a pixel starts at:

- `(x, y)`

then after transformation it may move to:

- `(x', y')`

The main goal is to compute where each original point should appear in the transformed image.

---

## 5. Affine Transformation Matrix

The lecture introduces the affine transformation matrix as:

```text
[ x' ]   [ a  b  tx ] [ x ]
[ y' ] = [ c  d  ty ] [ y ]
                       [ 1 ]
```

This is a `2 x 3` matrix with six values:

- `a`
- `b`
- `c`
- `d`
- `tx`
- `ty`

This matrix determines how the point `(x, y)` is transformed into `(x', y')`.

---

## 6. Meaning of the Matrix Terms

The lecture describes the matrix values in terms of the transformations they control:

- `a` and `b` influence horizontal behavior,
- `c` and `d` influence vertical behavior,
- `tx` controls translation along the `x` axis,
- `ty` controls translation along the `y` axis.

Together, these values can represent:

- scaling,
- rotation,
- shearing,
- translation.

---

## 7. What Is Affine Transformation?

Affine transformation is a linear mapping that preserves important geometric structure.

The lecture highlights these properties:

- straight lines remain straight,
- parallel lines remain parallel,
- rotation, scaling, translation, and shearing can all be represented.

So affine transformation changes the image shape or orientation in controlled ways, but it does not change the image into a different viewing perspective.

---

## 8. Main Properties of Affine Transformation

The most important properties to remember are:

- straightness is preserved,
- parallelism is preserved,
- relative geometric structure is maintained better than in arbitrary warping.

For example, if two lines are parallel in the original image, they remain parallel after an affine transformation, even if the angle changes.

---

## 9. Affine Transformation Uses Three Point Pairs

The lecture explains affine transformation using point correspondences.

To define an affine transform, we specify:

- three points in the input image,
- and their three corresponding points in the output image.

These point pairs tell the transformation how the image should be repositioned and reshaped.

---

## 10. What Is Perspective Transformation?

Perspective transformation maps one quadrilateral in the input image to another quadrilateral in the output image.

Its main purpose is to simulate a change in viewing angle.

This is useful when an object looks distorted because of camera position.

For example:

- a parking space viewed from an angled CCTV camera may look like a trapezoid,
- but from a top-down view it should look closer to a rectangle.

Perspective transformation helps convert between such views.

---

## 11. Main Properties of Perspective Transformation

The lecture emphasizes an important difference from affine transformation:

- straight lines remain straight,
- but parallelism is **not** necessarily preserved.

This means:

- parallel lines may become non-parallel,
- non-parallel lines may appear parallel from another viewpoint.

That is exactly why perspective transformation is useful for viewpoint correction.

---

## 12. Affine vs Perspective

A simple way to compare them:

- **Affine transformation** changes shape, scale, rotation, shear, or position while preserving parallel lines.
- **Perspective transformation** changes the apparent viewpoint and does not guarantee parallel lines remain parallel.

So if the problem is about image geometry inside the same viewing plane, affine is often enough.

If the problem is about how the scene appears from another camera angle, perspective transformation is more appropriate.

---

## 13. Scaling in the Affine Matrix

Scaling means enlarging or shrinking the image.

The lecture explains that scaling is mainly controlled by:

- `a` for the `x` direction,
- `d` for the `y` direction.

For pure scaling, the matrix is typically:

```text
[ sx   0  0 ]
[ 0   sy  0 ]
```

where:

- `sx` is the horizontal scale factor,
- `sy` is the vertical scale factor.

---

## 14. Rotation in the Affine Matrix

For rotation by angle `theta`, the lecture gives the standard form:

```text
[ cos(theta)   -sin(theta)   0 ]
[ sin(theta)    cos(theta)   0 ]
```

This rotates the image around the chosen reference system.

Examples mentioned in the lecture include:

- `90` degree rotation,
- `45` degree rotation.

Arbitrary-angle rotation is one of the main reasons affine transformation is needed.

---

## 15. Shearing in the Affine Matrix

Shearing changes the shape of the image by slanting it.

The lecture explains this using the example of stretching a cloth diagonally.

In image terms:

- the image is pushed sideways while preserving straight lines,
- the shape becomes slanted.

Typical forms are:

```text
X-shear:
[ 1  shx  0 ]
[ 0   1   0 ]
```

```text
Y-shear:
[ 1   0   0 ]
[ shy 1   0 ]
```

where:

- `shx` controls shearing along the `x` direction,
- `shy` controls shearing along the `y` direction.

---

## 16. Translation in the Affine Matrix

Translation means moving the image without changing its shape.

This is controlled by:

- `tx`
- `ty`

The lecture explains that:

- positive `tx` moves the image to the right,
- positive `ty` moves the image downward in OpenCV image coordinates.

A pure translation matrix looks like:

```text
[ 1  0  tx ]
[ 0  1  ty ]
```

---

## 17. Why Empty Regions Appear After Transformation

When an image is rotated, sheared, or translated, some output pixels may not receive information from the original visible area.

As a result:

- black or empty areas can appear,
- parts of the original image can move outside the output frame.

This is a natural consequence of geometric transformation and one of the reasons these operations need careful handling.

---

## 18. Practical Intuition for Choosing the Right Transformation

Use affine transformation when you want:

- scaling,
- rotation,
- shearing,
- translation,
- structure-preserving geometric changes.

Use perspective transformation when you want:

- viewpoint correction,
- top-view conversion,
- quadrilateral-to-quadrilateral mapping,
- camera-angle simulation.

---

## 19. Key Takeaways

- Affine and perspective transformations are advanced geometric image transformations.
- Both work by mapping input coordinates to new output coordinates.
- Affine transformation uses a `2 x 3` matrix.
- Affine transformation preserves straight lines and parallel lines.
- Perspective transformation preserves straight lines but not parallelism.
- Affine transformation supports scaling, rotation, shearing, and translation.
- Rotation by arbitrary angles like `45` degrees is a major use case for affine transformation.
- Perspective transformation is useful for changing or correcting the apparent viewing angle.

---

## 20. Summary

This lecture extends basic image manipulation into more powerful geometric transformations.

Affine transformation helps us apply controlled changes such as scaling, rotation, shearing, and translation through a transformation matrix.

Perspective transformation goes a step further by simulating how the same scene would look from a different viewpoint.

Together, these transformations are essential for image augmentation, alignment, distortion correction, and many practical computer vision workflows.
