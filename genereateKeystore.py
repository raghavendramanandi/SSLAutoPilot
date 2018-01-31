from utility import processCommand


def formDname(domain, organizationUnit, organization, city, stateORProvince, countryCode):
    dname = "CN=" + domain + ", OU=" + organizationUnit + ", O=" + organization + ", L=" + city + ", S=" + stateORProvince + ", C=" + countryCode
    return dname


def getKeyStoreCommand(dname, keyStoreLocation, keystorePassword, keypass):
    commandString = "keytool -genkey -noprompt -alias tomcat -dname \"" + \
                    dname + \
                    "\" -keystore " + \
                    keyStoreLocation + \
                    " -storepass " + \
                    keystorePassword + \
                    " -keypass " + \
                    keypass
    return commandString


def getMigrateToPKCS12Command(keyStoreLocation, keystorePassword):
    commandString = "keytool -importkeystore -srckeystore " + keyStoreLocation + " -destkeystore " + keyStoreLocation + " deststoretype pkcs12 -noprompt -srcstorepass " + keystorePassword
    return commandString


def MigrateToPKCS12(keyStoreLocation, keystorePassword):
    processCommand(getMigrateToPKCS12Command(keyStoreLocation, keystorePassword))


def createKeyStore(sslRequest):
    processCommand(
        getKeyStoreCommand(
            formDname(sslRequest.domain
                      , sslRequest.organizationUnit
                      , sslRequest.organization
                      , sslRequest.city
                      , sslRequest.stateORProvince
                      , sslRequest.countryCode
                      )
            , sslRequest.keyStoreLocation
            , sslRequest.keystorePassword
            , sslRequest.keypass
        )
    )


def generateKeyStoreFor(sslRequest):
    createKeyStore(sslRequest)
    MigrateToPKCS12(sslRequest.keyStoreLocation, sslRequest.keystorePassword)
