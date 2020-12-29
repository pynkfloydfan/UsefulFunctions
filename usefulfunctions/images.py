from PIL import Image
import os


# set the default location of images to the Pictures directory (WINDOWS)
image_path = os.path.join(os.environ['USERPROFILE'], 'Pictures')


def cutimage(image, x_slices, y_slices, outpath=image_path):
    """
    Cuts an image into equal sized slices, x_slices long and y_slices high

    I wanted to expand an image over 2 pages in a pdf (via LaTeX) but 
    unfortunately it wouldn't automatically stretch over 2 pages, so instead I 
    decided to cut it in two and input each half to a separate page.
    
    Inspiration from here:
    https://tex.stackexchange.com/questions/22826/breaking-pictures-across-multiple-pages
    
    Parameters:
    -----------
    image: an image file
    x_slices: number of equal sized slices in the horizontal axis
    y_slices: number of equal sized slices in the vertical axis
    
    Returns:
    --------
    x_slices number of lists each with y_slices number of image items
    """

    # x, y image size
    xsize, ysize = image.size
    
    # size of each slice in each axis
    xstep = xsize // x_slices
    ystep = ysize // y_slices
    
    # all coordinates of each sub-image
    if x_slices > 1:
        xcoord = list(range(0, xsize + x_slices - 1, xstep))
    else:
        xcoord = [0, xsize]
    if xcoord[-1] < xsize: 
        xcoord[-1] = xsize
    
    if y_slices > 1:
        ycoord = list(range(0, ysize + y_slices - 1, ystep))
    else:
        ycoord = [0, ysize]
    if ycoord[-1] < ysize: 
        ycoord[-1] = ysize
    
    for y in range(y_slices):
        for x in range(x_slices):
            bbox = (xcoord[x], ycoord[y], xcoord[x+1], ycoord[y+1])
            image_slice = image.crop(bbox)
            image_slice.save(os.path.join(outpath, "slice_" + str(x) + "_" + str(y) + "_" + ".png"))
            # image_slice.show()
    
    return 'All images saved'
