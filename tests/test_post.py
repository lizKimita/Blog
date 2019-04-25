import unittest
from app.models import Post, User


class PostTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post('The best way to learn Python', 'Watch alot of Youtube videos', 'shiko kimita', '02/04/2019')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

