import unittest
from app.models import Comment, User

class CommentTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment('That is a great tip', 'Kijo Kimita', '28/06/2019')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

