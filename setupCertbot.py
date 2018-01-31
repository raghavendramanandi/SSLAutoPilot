from sharedData import certbotLocation
from utility import processCommand


def downloadCertbot():
    commandString = "wget https://dl.eff.org/certbot-auto -P " + certbotLocation
    processCommand(commandString)

def getChangePriveledgeOnCertbotCommand(certbotLocation):
    commandString = "chmod 777 " + certbotLocation + "/certbot-auto"
    return commandString

def changePriveledgesOncertbot():
    processCommand(getChangePriveledgeOnCertbotCommand(certbotLocation))


def setupCertbot():
    downloadCertbot()
    changePriveledgesOncertbot()
