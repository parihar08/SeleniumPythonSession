import configparser

config = configparser.RawConfigParser()
config.read("../../../Configurations/config.ini")

class ReadConfig():

    @staticmethod
    def baseUrl():
        url = config.get('common info','baseUrl')
        return url