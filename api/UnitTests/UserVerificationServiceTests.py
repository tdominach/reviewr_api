import unittest
from reviewr_api.api.VerificationServices import UserVerificationService


class UserVerificationServiceTests(unittest.TestCase):
    def test_GivenUsernameIsLessThanFiveCharacters_WhenVerifyUsernameCalled_ThenReturnFalse(self):
        self.assertEqual(UserVerificationService.verifyUsername("User"), False)

    def test_GivenUsernameIsMoreThanFiveCharacters_WhenVerifyUsernameCalled_ThenReturnTrue(self):
        self.assertEqual(UserVerificationService.verifyUsername("Username"), True)


if __name__ == '__main__':
    unittest.main()
