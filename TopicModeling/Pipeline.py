class Pipeline(object):

    def __init__(self, pipeline = [], *args, **kwargs):
        super(Pipeline, self).__init__(*args, **kwargs)

    def __call__(self, x):
        data = x
        for transformation in self.pipeline:
            data = transformation(data)
        return data

    def iterOnStream(self, stream):
        for item in stream:
            yield self(item)