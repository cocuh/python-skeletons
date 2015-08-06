def init():
    """
    """
    pass


def quit():
    """
    """
    pass


def get_init():
    """
    :rtype: bool
    """
    pass


def set_mode(resolution=(0, 0), flags=0, depth=0):
    """
    :rtype: pygame.Surface
    """
    pass


def get_surface():
    """
    :rtype: pygame.Surface
    """
    pass


def flip():
    """
    
    """
    pass


def update(rectangle_list=[]):
    """
    :type rectangle_list: pygame.rect.Rectangle
    """
    pass


def get_driver():
    """
    
    """
    pass


def info():
    """
    :rtype:VideoInfo
    """
    pass


def get_wm_info():
    """
    :rtype:dict
    """
    pass


def list_modes(depth=0, flags=pygame.FULLSCREEN):
    """
    :rtype:list
    """
    pass


def mode_ok(size, flags=0, depth=0):
    """
    :rtype:int
    :return:depth
    """
    pass


def gl_get_attribute(flag):
    """
    :return:value
    """
    pass


def gl_set_attribute(flag, value):
    """
    :rtype:
    """
    pass


def get_active():
    """
    :rtype:bool
    """
    pass


def iconify():
    """
    
    :rtype: bool
    """
    pass


def toggle_fullscreen():
    """
    
    :rtype: bool
    """
    pass


def set_gamma(red, green=None, blue=None):
    """change the hardware gamma ramps
    :rtype: 
    """
    pass


def set_gamma_ramp(red, gree, blue):
    """
    :rtype: bool
    """
    pass


def set_icon(surface):
    """
    :rtype: 
    """
    pass


def set_caption(title, icontitle=None):
    """
    :rtype: 
    """
    pass


def get_caption():
    """
    :return: (title, icontitle)
    """
    pass


def set_palette(palette=None):
    """
    """
    pass
