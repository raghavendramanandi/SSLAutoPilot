import getpass


class SSLRequest:
    domains = []
    organizationUnit = ""
    organization = ""
    city = ""
    stateORProvince = ""
    countryCode = ""
    keyStoreLocation = ""
    keystorePassword = ""
    keypass = ""

    def readSLLRequest(self):
        count = 0
        numberOfDomains = raw_input("Enter the number of domains: ")
        while count != numberOfDomains:
            self.domains[count] = raw_input("Enter your domain name: ")
            count = count + 1

        self.organizationUnit = raw_input("Enter your organization unit: ")
        self.organization = raw_input("Enter your organization: ")
        self.city = raw_input("Enter your city: ")
        self.stateORProvince = raw_input("Enter your state: ")
        self.countryCode = raw_input("Enter tour country code: ")
        self.keyStoreLocation = raw_input("Enter KeyStore location ")
        self.keystorePassword = getpass.getpass("Please enter keystor password", "")
        self.keypass = getpass.getpass("Please enter key password", "")






