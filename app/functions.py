import json, requests, base64, time
import config

class prettyprint:
    def parse(self, input, language):
        # parse according to language
        if language == 'json' or language == 'auto':
            output = self.json(input);
        else:
            output = input

        # return output
        return output

    def json(self, input):
        # load and dump json with indention
        try:
            parsed = json.loads(input)
            output = json.dumps(parsed, indent=4, sort_keys=True)
        except:
            output = False

        # return output
        return output
