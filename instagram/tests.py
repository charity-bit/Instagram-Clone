from django.test import TestCase

from django.contrib.auth.models import User

from .models import Profile,Follow



# Create your tests here.

class UserTestClass(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(
            username = 'charity',
            password = 'pass1',
            email = 'charitynyanchera@gmail.com'
        )

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        users = User.objects.all()
        self.assertEquals(len(users),1)

    def test_delete_method(self):
        self.new_user.save()
        test_user = User(username = 'testuser',password='12345678',email='example@gmail.com')
        test_user.save()
        self.new_user.delete()
        users = User.objects.all()
        self.assertEquals(len(users),1)


        


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(
            username = 'charity',
            password = 'pass1',
            email = 'charitynyanchera@gmail.com'
        )

        # saving user to create profile for
        self.new_user.save()

        # profile instance
        self.new_profile = Profile(user = self.new_user, name = 'charity Nyanchera',bio = "Don't blame meLove made me Crazy, if it doesn,t you aint doing right")


    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))



    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)

    def test_delete_profile(self):
        ''''

        method to test deleteing a profile
        create and save a test profile
        then delete new_profile instance
        '''
        self.test_user = User.objects.create(
            username = 'testuser',
            password = '123456789',
            email = 'example@gmail.com'
        )

        self.test_user.save()

        self.test_profile = Profile(user = self.test_user, name = 'Test User',bio = "Hurts so good")
        self.test_profile.save_profile()
        self.new_profile.save_profile()

        self.new_profile.delete()

        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)


        

def FollowTestClass(TestCase):
    def setUp(self):
        self.charity = User.objects.create(
            username = 'charity',
            password = 'pass1',
            email = 'charitynyanchera@gmail.com'
        )


        self.test = User.objects.create(
            username = 'test',
            password = 'test1234',
            email = 'example@gmail.com'
        )


        self.test2 = User.objects.create(
            username = 'test_user2',
            password = 'test1234',
            email = 'example@gmail.com'
        )


        self.charity.save()
        self.test.save()
        self.test2.save()

    def test_instance(self):
        self.follow = Follow(account = self.charity,follower = self.test)
        self.assertTrue(isinstance(self.follow,Follow))

    
    def test_follow(self):
        self.follow = Follow(account = self.charity,follower = self.test)
        self.follow.follow()

        follow_objects = Follow.objects.all()

        self.assertEquals(follow_objects,1)

