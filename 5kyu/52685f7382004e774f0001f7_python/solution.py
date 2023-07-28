def make_readable(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:>02}:{:>02}:{:>02}".format(hours, minutes, seconds)