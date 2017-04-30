import urllib, json

class API(object):

    def __init__(self, params):
        print params
        self.url = 'http://www.markerapi.com/api/v1/trademark/search/{0}/username/{1}/password/{2}'
        self.search = params['search']
        self.username = params['username']
        self.password = params['password']

    def result(self):
        response = urllib.urlopen(self.url.format(self.search,
                                                  self.username,
                                                  self.password))
        data = response.read()
        result = json.loads(data)
        return result
