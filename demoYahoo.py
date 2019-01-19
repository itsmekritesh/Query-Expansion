import simplejson, urllib
APP_ID = '5A1rZg48' # Change this to your API key
SEARCH_BASE = 'http://search.yahooapis.com/ WebSearchService/V1/webSearch'

class YahooSearchError(Exception):
    pass

def search(query, results=20, start=1, **kwargs):
    kwargs.update({
        'appid': APP_ID,
        'query': query,
        'results': results,
        'start': start,
        'output': 'json'
    })
    url = SEARCH_BASE + '?' + urllib.parse.urlencode(kwargs)
    print(url)
    result = simplejson.load(urllib.request.urlopen(url))
    '''if 'Error' in result:
        # An error occurred; raise an exception
        raise YahooSearchError, result['Error']'''
    return result['ResultSet']

info = search('swine flu vaccine')
results = info['Result']
for result in results:
    print(result['Url'])
