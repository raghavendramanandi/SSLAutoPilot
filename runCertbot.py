from utility import processCommand
from sharedData import certbotLocation
from sharedData import webrootLocation
from sharedData import csrFile


def FormCertbotCommand(sslRequest):
    domainString = ""
    for item in sslRequest.domains:
        domainString = domainString + "-d " + item

    commandString = "sudo " + certbotLocation + "/certbot-auto certonly --webroot -w " + webrootLocation + " " + domainString + " —csr " + csrFile + " —no-bootstrap"
    return commandString


def runCertbot(sslRequest):
    processCommand(FormCertbotCommand(sslRequest))
