class CVHelper(object):

    """Utilities for image processing and computer vision apps"""

    def __init__(self, verbose=False):
        """Constructor. Set verbose, if verbose = True print image paths"""
        self.verbose = verbose

    def read_images_filename(self,  folder_path, recursive=False):
        """Reads images filename in a folder

        :folder_path: Folder path that contains the images
        :recursive: Look inside subfolders
        :returns: List of image paths, e.g.,
        ['/path/to/im1.jpg', '/path/to/im2.png', '/path/to/img3.tiff']
        """

        from os import listdir
        from os.path import isfile, join, isdir

        extensions = [".jpg",".png",".tiff",".bmp"]

        cvhelper = CVHelper()
        dirname = listdir(folder_path)
        filelist = [join(folder_path, file) for file in dirname if isfile(join(folder_path, file))]

        for file in filelist:
            if (any(file) for ext in extensions) and (file.endswith(".DS_store")):
                filelist.remove(file)

        if recursive:
            for file in dirname:
                if isdir(join(folder_path, file)):
                    path = join(folder_path, file)
                    filelist.extend(cvhelper.read_images_filename(path,True))

        return filelist

        pass
        #
        # End code
        #
