from utility import processCommand
import sharedData


def getCSRCommand(csrFile, keyStoreLocation, keystorePassword):
    """
    :type sslRequest: SSLRequest
    """
    commandString = "keytool -certreq -alias tomcat -file " + csrFile + "-keystore " + keyStoreLocation + " -noprompt -srcstorepass " + keystorePassword
    return commandString


def generateCSR(sslRequest):
    csr_command = getCSRCommand(sharedData.csrFile, sslRequest.keyStoreLocation, sslRequest.keystorePassword)
    processCommand(csr_command)
