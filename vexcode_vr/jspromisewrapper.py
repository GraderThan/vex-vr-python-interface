class WrappedPromise:
    def __init__(self, promise):
        self.promise = promise
    def __await__(self):
        x = yield self.promise
        return x

def wrap_promise(promise):
    return WrappedPromise(promise)