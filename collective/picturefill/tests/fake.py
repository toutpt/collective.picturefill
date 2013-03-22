

class FakeContext(object):

    def __init__(self):
        self.id = "myid"
        self.title = "a title"
        self.description = "a description"
        self.creators = ["myself"]
        self.date = "a date"
        self._modified = "modified date"
        self.remoteUrl = ''  # fake Link

    def getId(self):
        return self.id

    def Title(self):
        return self.title

    def Creators(self):
        return self.creators

    def Description(self):
        return self.description

    def Date(self):
        return self.date

    def modified(self):
        return self._modified

    def getPhysicalPath(self):
        return ('/', 'a', 'not', 'existing', 'path')

    def absolute_url(self):
        return "http://nohost.com/" + self.id


class FakeBrain(object):
    def __init__(self):
        self.Title = ""
        self.Description = ""
        self.getId = ""
        self.portal_type = ""

    def getURL(self):
        return "http://fakebrain.com"

    def getObject(self):
        ob = FakeContext()
        ob.title = self.Title

        return ob


class FakeProperty(object):
    def __init__(self):
        self.photo_max_size = 400
        self.thumb_max_size = 80

    def getProperty(self, name, default=None):
        return getattr(self, name, default)


def fake_get_property(self):
    return FakeProperty()