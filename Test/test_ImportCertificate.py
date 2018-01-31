import unittest
from unittest import TestCase

from importCertificate import getCommandForImport


class TestImportCertificate(TestCase):
    def test_getKeyStoreCommand(self):
        command = getCommandForImport("certbotlocation", "location", "password")
        self.assertEqual(command, "keytool -import -trustcacerts -alias tomcat -file certbotlocation/0001_cert.perm -keystore location -noprompt -storepass password")

    if __name__ == '__main__':
        unittest.main()
