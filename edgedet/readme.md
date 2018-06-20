```py
    # Split out each channel
    blue, green, red = cv2.split(img)

    # sigma
    sigma = 0.60
    # median pixel intensities
    v_blue = np.median(blue)
    v_red = np.median(red)
    v_green = np.median(green)

    lower = int( max(0, (1.0-sigma) * v_blue) )
    upper = int( min(255, 1.0 + sigma) * v_blue)
    # Run canny edge detection on each channel
    blue_edges = cv2.Canny(blue, int( max(0, (1.0-sigma) * v_blue) ), int( min(255, 1.0 + sigma) * v_blue))
    green_edges = cv2.Canny(green, int( max(0, (1.0-sigma) * v_green) ), int( min(255, 1.0 + sigma) * v_green))
    red_edges = cv2.Canny(red, int( max(0, (1.0-sigma) * v_red) ), int( min(255, 1.0 + sigma) * v_red))

    # Join edges back into image
    edges = blue_edges | green_edges | red_edges
    cv2.imshow('canny edges', edges)
```
