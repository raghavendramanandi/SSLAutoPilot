from utility import processCommand
from sharedData import certbotLocation


def getCommandForImport(certbotLocation, keyStoreLocation, keystorePassword):
    return "keytool -import -trustcacerts -alias tomcat -file " + certbotLocation + "/0001_cert.perm -keystore " + keyStoreLocation + " -noprompt -storepass " + keystorePassword


def importCertbotCertificate(sslRequest):
    processCommand(getCommandForImport(certbotLocation, sslRequest.keyStoreLocation, sslRequest.keystorePassword))
