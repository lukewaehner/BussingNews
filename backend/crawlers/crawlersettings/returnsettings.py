import json
import random
import os


def returnsettings():

    # Get a proxy

    # Load user agents
    script_dir = os.path.dirname(os.path.abspath(__file__))
    agentsdir = os.path.join(script_dir, 'headers_data.json')
    with open(agentsdir, 'rt') as agents_file:
        agents_list = json.load(agents_file)

    # Pick a random user agent
    user_agent = random.choice(list(agents_list))['user-agent']

    # Return both proxy and user agent
    return {"user_agent": user_agent}
