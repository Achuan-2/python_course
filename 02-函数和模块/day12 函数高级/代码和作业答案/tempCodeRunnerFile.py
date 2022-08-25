def check_dir(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        # dirname = path.rsplit('/', 1)[0]
        dirname=os.path.dirname(args[0])
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        res = func(*args, **kwargs)
      
        return res
    return inner