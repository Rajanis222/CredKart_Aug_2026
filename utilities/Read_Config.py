import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        email=config.get("login data","email")
        return email

    @staticmethod
    def get_data_for_password():
        password=config.get("login data","password")
        return password

    @staticmethod
    def get_home_url():
        home_url=config.get("app urls","home_page_url")
        return home_url

    @staticmethod
    def get_login_url():
        login_url=config.get("app urls","login_url")
        return login_url

    @staticmethod
    def get_registeration_url():
        registration_url=config.get("app urls","registration_url")
        return registration_url

