from configparser import ConfigParser

config = ConfigParser()

config.read('./Utility/config.cfg')

print(config.get('Section 1', 'username'))