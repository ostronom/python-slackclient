import json

import requests
import six


class SlackRequest(object):
    def __init__(self, url):
        self.url = url

    def do(self, token, request="?", post_data=None):
        '''
        Perform a POST request to the Slack Web API

        Args:
            token (str): your authentication token
            request (str): the method to call from the Slack API. For example: 'channels.list'
            post_data (dict): key/value arguments to pass for the request. For example:
                {'channel': 'CABC12345'}
            domain (str): if for some reason you want to send your request to something other
                than slack.com
        '''
        post_data = post_data or {}

        for k, v in six.iteritems(post_data):
            if not isinstance(v, six.string_types):
                post_data[k] = json.dumps(v)

        url = '{0}/{1}/api/{2}'.format(self.url, token, request)
        files = {'file': post_data.pop('file')} if 'file' in post_data else None

        return requests.post(url, data=post_data, files=files)
