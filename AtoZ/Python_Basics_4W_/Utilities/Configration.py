def getconfig():
    import configparser
    config = configparser.ConfigParser()
    config.read("Utilities/project.ini")
    return config
