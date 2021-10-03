import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/Chaitra/PycharmProjects/nopCommerce/Configurations/config.ini")
#config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getBaseUrl():
        url = config.get('common values', 'base_url')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common values', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common values', 'password')
        return password

    @staticmethod
    def getFilePath():
        filePath = config.get('excel values', 'excelPath')
        return filePath

    @staticmethod
    def getSheetName():
        sheetName = config.get('excel values', 'sheetName')
        return sheetName

    @staticmethod
    def getDashboardTitle():
        dashTitle = config.get('title values', 'dashTitle')
        return dashTitle

    @staticmethod
    def getCustPassword():
        custPassword = config.get('add customer', 'custPassword')
        return custPassword

    @staticmethod
    def getFirstName():
        firstName = config.get('add customer', 'firstName')
        return firstName

    @staticmethod
    def getLastName():
        lastName = config.get('add customer', 'lastName')
        return lastName

    @staticmethod
    def getGender():
        gender = config.get('add customer', 'gender')
        return gender

    @staticmethod
    def getMonthInDOB():
        month = config.get('add customer', 'monthDOB')
        return month

    @staticmethod
    def getYearInDOB():
        year = config.get('add customer', 'yearDOB')
        return year

    @staticmethod
    def getDayInDOB():
        day = config.get('add customer', 'dayDOB')
        return day

    @staticmethod
    def getCompanyName():
        companyName = config.get('add customer', 'companyName')
        return companyName

    @staticmethod
    def getCustRoles():
        role = config.get('add customer', 'custRoles')
        return role

    @staticmethod
    def getVendor():
        vendor = config.get('add customer', 'vendor')
        return vendor

    @staticmethod
    def getValidationMessage():
        message = config.get('add customer', 'validationMessage')
        return message

    @staticmethod
    def getDOB():
        dob = config.get('add customer', 'dob')
        return dob





