def community_required(func):

    def wrapped(*args, **kwargs):

        print('called with ', *args)
        print('and ', **kwargs)

        func(*args, **kwargs)

        return func
