import api
import unittest


class api_tests(unittest.TestCase):

    def setUp(self):
        self.api_checker = api

    def tearDown(self):
        pass

    ## Check if the function get_search_by_name in api returns a list
    def testGetSearchByNameType(self):
        self.assertIsInstance(self.api_checker.get_search_by_name("Wii Sports"), list)


    ## Check if the function get_search_by_name returns the correct information related to "WiiSports"
    ## This test is expected to fail.
    def testGetSearchByName(self):
        gameInfoDict = self.api_checker.get_search_by_name("Wii Sports")
        self.assertEqual([{'name': 'Wii Sports', 'platform': 'Wii', 'yearofrelease': '2006', 'genre': 'Sports',
                               'publisher': 'Nintendo', 'nasales': 41.36, 'eusales': 28.96, 'jpsales': 3.77,
                               'othersales': 8.45, 'globalsales': 82.53, 'criticscore': 76.0, 'criticcount': 51.0,
                               'userscore': '8', 'usercount': 322.0, 'developer': 'Nintendo', 'rating': 'E'}], gameInfoDict)


    ## Check if the function get_search_by_publisher in api returns a list
    def testGetSearchByPublisherType(self):
        self.assertIsInstance(self.api_checker.get_search_by_publisher("Nintendo"), list)


    ## Check if the function get_search_by_publisher returns a list that lists the right number of games
    ## by the same publisher Nitendo.
    ## This test is expected to fail.
    def testGetSearchByPublisherNumber(self):
        ## according to the data base, 706 games in the database are developed by Nitendo.
        numGameSamePublisher = 692
        self.assertEqual(len(self.api_checker.get_search_by_publisher("Nintendo")), numGameSamePublisher)


    ## Check if the function get_display_by_publisher in api returns a list
    def testGetDisplayByPublisherType(self):
        self.assertIsInstance(self.api_checker.get_display_by_publisher("Nintendo"), list)


    ## Check if the function get_display_by_publisher returns a list that lists the right number of games
    ## by the same publisher , in this case Nitendo.
    ## This test is expected to fail.
    def testGetDisplayByPublisherNumber(self):
        ## according to the data base, 706 games in the database are developed by Nitendo.
        numGameSamePublisher = 692
        self.assertEqual(len(self.api_checker.get_display_by_publisher("Nintendo")), numGameSamePublisher)


    ## Check if the function get_name_platform_display_by_genre in api returns a list
    def testGetNamePlatformDisplayByGenreType(self):
        self.assertIsInstance(self.api_checker.get_name_platform_display_by_genre("Sports"), list)


    ## Check if the function get_display_by_publisher returns a list that lists the right number of games
    ## by the same genre , in this case Sports.
    ## This test is expected to fail.
    def testGetNamePlatformDisplayByGenreNum(self):
        ## according to the data base, 2348 games in the database are Sports games
        numGameSameGenre = 2347
        self.assertEqual(len(self.api_checker.get_name_platform_display_by_genre("Sports")), numGameSameGenre)


    ## Check if the function get_display_by_platform in api returns a list
    def testGetDisplayByPlatformType(self):
        self.assertIsInstance(self.api_checker.get_display_by_platform("GC"), list)


    ## Check if the function get_display_by_platform returns a list that lists the right number of games
    ## supportive of the same paltform , in this case GC.
    ## This test is expected to fail.
    def testGetDisplayByPlatformNum(self):
        ## according to the data base, 556 games in the database are developed by GC.
        numGameSamePlatform = 555
        self.assertEqual(len(self.api_checker.get_display_by_platform("GC")), numGameSamePlatform)


    ## Check if the function get_name_display_by_genre in api returns a list
    def testGetNameDisplayByGenreType(self):
        self.assertIsInstance(self.api_checker.get_name_display_by_genre("Action"), list)

    ## Check if the function get_name_display_by_genre returns a list that lists the right number of games
    ## supportive of the same genre , in this case Action.
    ## This test is expected to fail.
    def testGetNameDisplayByGenreNum(self):
        ## according to the data base, 3370 games in the database are action games
        numGameSameGenre = 3368
        self.assertEqual((len(self.api_checker.get_name_display_by_genre("Action"))), numGameSameGenre)
    
    ## Check if the function get_name_display_by_developer in api returns a list
    def testGetNameByDeveloperType(self):
        self.assertIsInstance(self.api_checker.get_name_display_by_developer("Acclaim"), list)


    ## Check if the function get_name_display_by_developer a list that lists the right number of games
    ## supportive of the same developer , in this case Acclaim.
    ## This test is expected to fail.
    def testGetNameByDeveloperNum(self):
        ## according to the data base, 32 games in the database are developed by the developer "Acclaim"
        numGameSameDeveloper = 32
        self.assertEqual(len(self.api_checker.get_name_display_by_developer("Acclaim")), numGameSameDeveloper)


    ## Check if the function get_password_with_account_name in api returns a string
    def testGetPasswordWithAccountName(self):
        self.assertIsInstance(api.get_password_with_account_name("cheny2"), str)


    ## Check if the function get_password_with_account_name returns the password
    ## that the user given, in this case "vic31415@@"
    ## This test is expected to fail.
    def testGetPasswordWithAccountNameInfo(self):
        password = "vic31415@@"
        self.assertEqual(api.get_password_with_account_name("cheny2"), password)


    ## Check if the function get_user_info in api returns a dictionary
    def testGetUserInfoType(self):
        self.assertIsInstance(self.api_checker.get_user_info("cheny2"), dict)


    ## Check if the function get_user_info returns the correct information
    ## about the user.
    ## This test is expected to fail.
    def testGetUserInfo(self):
        # user information as give api.py
        userInfoDict = {'email_address':'cheny2@carleton.edu', 'favorite_games':['Halo 3', 'Super Mario Land','Call of Duty: Black Ops 3']}
        self.assertEqual(self.api_checker.get_user_info("cheny2"), userInfoDict)


    ## Check if the function get_password_with_email returns a list
    def testGetPasswordWithEmailType(self):
        self.assertIsInstance(self.api_checker.get_password_with_email("cheny2@carleton.edu"), str)


    ## Check if the function get_password_with_email returns the correct information about the user.
    ## This test is expected to fail.
    def testGetPaswordWithEmail(self):
        # password as given in api.py
        password = "vic31415@@"
        self.assertEqual(self.api_checker.get_password_with_email("cheny2@carleton.edu"), password)

if __name__ == '__main__':
    unittest.main()