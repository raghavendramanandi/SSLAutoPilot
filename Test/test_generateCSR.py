import unittest
from unittest import TestCase

from generateCSR import getCSRCommand


class TestGenerateCSR(TestCase):

    def test_CSRGenerationCommand(self):
        csrFile = "./request.csr"
        keyStoreLocation = "./mycert"
        keystorePassword = "pass"
        command = getCSRCommand(csrFile, keyStoreLocation, keystorePassword)
        print(command)
        self.assertEqual(command, 'keytool -certreq -alias tomcat -file ./request.csr-keystore ./mycert -noprompt '
                                   '-srcstorepass pass')

    if __name__ == '__main__':
        unittest.main()
