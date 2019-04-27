import unittest
from app.models import User,Comment
from app import db


class CommentTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(comments = 'That is a great blog post', post_id = 4456 , posted = '04/12/2019',user_id = 4)

    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comments,'That is a great blog post')
        self.assertEquals(self.new_comment.post_id,4456)
        self.assertEquals(self.new_comment.posted,'04/12/2019')
        self.assertEquals(self.new_comment.user_id,4)

    def test_save_review(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(4456)
        self.assertTrue(len(got_comments) == 1)