class Surface(object):
    def __init__(self, size, flags=0, depth=0, mask=None):
        """
        :param size:(width, height)
        :type size:  tuple[int,int]
        :return:
        """

    def blit(self, source, dest, area=None, special_flags=0):
        """
        :rtype: pygame.Rect
        """
        pass

    def convert(self, surface=None, depth=0, flags=0, masks=None):
        """
        :rtype: Surface
        """
        pass

    def convert_alpha(self, surface=None):
        """
        :rtype: Surface
        """
        pass

    def copy(self):
        """
        :rtype: Surface
        """
        pass

    def fill(self, color, rect=None, spefial_flags=0):
        """
        :rtype: pygame.Rect
        """
        pass

    def scroll(self, dx=0, dy=0):
        """
        """
        pass

    def set_colorkey(self, color, flags=0):
        """set the transparent colorkey
        :rtype: 
        """
        pass

    def get_colorkey(self):
        """
        :rtype: RGB
        """
        pass

    def set_alpha(self, value, flags=0):
        """
        :type value:int
        :rtype: 
        """
        pass

    def get_alpha(self):
        """
        :rtype: int | None
        """
        pass

    def lock(self):
        """lock the Surface memory for pixel access
        """
        pass

    def unlock(self):
        """unlock the Surface memory from pixel access
        :rtype: 
        """
        pass

    def mustlock(self):
        """test if the Surface requires locking
        :rtype: bool
        """
        pass

    def get_locked(self):
        """test if the Surface is current locked
        :rtype: bool
        """
        pass

    def get_locks(self):
        """gets the locks for the Surface
        :rtype: tuple
        """
        pass

    def get_at(self, pos):
        """get the color value at a single pixel
        :argument pos: (x,y)
        :type pos: tuple[int,int]
        :rtype: Color
        """
        pass

    def set_at(self, pos, color):
        """
        :argument pos: (x,y)
        :type pos: tuple[int,int]
        :type color: Color
        :rtype: Color
        """
        pass

    def get_at_mapped(self, pos):
        """
        :rtype: Color
        """
        pass

    def get_palette(self):
        """
        :rtype: list[RGB]
        """
        pass

    def get_palette_at(self, index):
        """
        :rtype: RGB
        """
        pass

    def set_palette(self, palette_list):
        """
        :type palette_list: list[RGB]
        :rtype: 
        """
        pass

    def set_palette_at(self, index, rgb):
        """
        :type index: int
        :type rgb: RGB
        :rtype: 
        """
        pass

    def map_rgb(self, color):
        """
        :type color:Color
        :rtype: int
        """
        pass

    def unmap_rgb(self, mapped_int):
        """
        :rtype: Color
        """
        pass

    def set_clip(self, rect):
        """
        :type rect: pygame.Rect|None
        :rtype: 
        """
        pass

    def get_clip(self):
        """
        :rtype: pygame.Rect 
        """
        pass

    def subsurface(self, rect):
        """
        :rtype: Surface
        """
        pass

    def get_parent(self):
        """
        :rtype: Surface
        """
        pass

    def get_abs_parent(self):
        """
        :rtype: Surface
        """
        pass

    def get_offset(self):
        """
        :rtype: tuple[int, int]
        """
        pass

    def get_abs_offset(self):
        """
        :rtype: tuple[int, int]
        """

    def get_size(self):
        """
        :return: (width, height)
        :rtype: tuple[int,int]
        """
        pass

    def get_width(self):
        """
        :rtype: int
        """
        pass

    def get_height(self):
        """
        :rtype: int
        """
        pass

    def get_rect(self, **kwargs):
        """
        :rtype: Rect
        """
        pass

    def get_bitsize(self):
        """
        :rtype: int
        """
        pass

    def get_bytesize(self):
        """
        :rtype: int
        """
        pass

    def get_flags(self):
        """
        :rtype: int
        """
        pass

    def get_pitch(self):
        """
        :rtype: int
        """
        pass

    def get_masks(self):
        """
        :return: [R, G, B, A]
        :rtype: tuple[int, int, int, int]
        """
        pass

    def set_masks(self, rgba):
        """
        :type rgba: tuple[int, int, int, int]
        :rtype: 
        """
        pass

    def get_shifts(self):
        """
        :rtype: tuple[int, int, int, int]
        """
        pass

    def set_shifts(self, rgba):
        """
        :rtype: 
        """
        pass

    def get_losses(self):
        """
        :rtype: tuple[int, int, int, int]
        """
        pass

    def get_bounding_rect(self, min_alpha=2):
        """
        :rtype: Rect
        """
        pass

    def get_view(self, kind=2):
        """
        :rtype:BufferProxy 
        """
        pass

    def get_buffer(self):
        """
        :rtype: BufferProxy
        """
        pass
