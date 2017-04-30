import urllib, json

class API(object):

    def __init__(self, params):
        self.url = 'https://getbible.net/json?%'
        self.params = params

    def result(self):
        params = urllib.urlencode(self.params)
        print params
        response = urllib.urlopen("https://getbible.net/json?{0}".format(params))
        data = response.read()
        data = data.replace(data[:1], '')
        data = data[:-2]
        result = json.loads(data)
        return result
