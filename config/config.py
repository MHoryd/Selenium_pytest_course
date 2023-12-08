import yaml

with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)
    BASE_URL = config['base_url']
    MAX_WAIT = config['max_wait']
    HEADLESS = config['headless']
    FULLSCREEN = config['fullcreen']