from PIL import Image
import os


# set the default location of images to the Pictures directory (WINDOWS)
_image_path = os.path.join(os.environ['USERPROFILE'], 'Pictures')


def cutimage(image, columns, rows, 
             save_images=True, 
             save_path=_image_path,
             file_names=None):
    """
    Cuts an image into equal sized slices, columns long and rows high

    I wanted to expand an image over 2 pages in a pdf (via LaTeX) but 
    unfortunately it wouldn't automatically stretch over 2 pages, so instead I 
    decided to cut it in two and input each half to a separate page.
    
    Inspiration from here:
    https://tex.stackexchange.com/questions/22826/breaking-pictures-across-multiple-pages
    
    Parameters:
    -----------
    image: an image file
    columns: number of equal sized slices in the horizontal axis
    rows: number of equal sized slices in the vertical axis
    save_images: if True then save all images cut from the main image
    save_path: the place to save all cut images if save_images=True
               the default path is the "Pictures" folder
    file_names: a list of names for each image to be saved.
                file_names=None then the images are named "slice_"+row+"_"+column
    
    Returns:
    --------
    List of row number of sub-lists, each sub-list has column number of images
    Optionally, each image cut out can be saved
    """

    # x, y image size
    xsize, ysize = image.size
    
    # size of each slice in each axis
    xstep = xsize // columns
    ystep = ysize // rows
    
    # how many images will be created?
    # nbImages = rows * columns
    
    # all coordinates of each sub-image
    if columns > 1:
        xcoord = list(range(0, xsize + columns - 1, xstep))
    else:
        xcoord = [0, xsize]
    if xcoord[-1] < xsize: 
        xcoord[-1] = xsize
    
    if rows > 1:
        ycoord = list(range(0, ysize + rows - 1, ystep))
    else:
        ycoord = [0, ysize]
    if ycoord[-1] < ysize: 
        ycoord[-1] = ysize
    
    result = list()
    img = 0 # counter for images
    
    for y in range(rows):
        x_list = list()
        for x in range(columns):
            bbox = (xcoord[x], ycoord[y], xcoord[x+1], ycoord[y+1])
            image_slice = image.crop(bbox)
            x_list.append(image_slice)
            
            if save_images:
                if file_names == None:
                    image_name = "slice_" + str(x) + "_" + str(y) + ".png"
                else:
                    image_name = file_names[img] + '.png'
                    img += 1
                    
            image_slice.save(os.path.join(save_path, image_name))
            # image_slice.show()
        result.append(x_list)
    
    return result
