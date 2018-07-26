from PIL import Image
import tempfile
from django.test import TestCase
from .models import Image, Profile
from django.test import override_settings
# Create your tests here.


def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'jpeg')
    return temp_file

class ImageDummyTest(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    # gettempdir() gets images from the temp file created running tests
    # overrides the default media directory to avoid dumping test images in that directory
    def test_dummy_test(self):
            temp_file = tempfile.NamedTemporaryFile()
            # create a temp file to store temp test images
            test_image = get_temporary_image(temp_file)
            # create a small square  and save it in the temp file
            # test_image.seek(0) --> this test an image as an attached
            # file thats in http request
            # test_image.seek(0)
            # response = self.client.put(
            #     self.reverse('upload_user_picture'),
            #     {'profile_picture': test_image})
            image = Image.objects.create(image=test_image.name)
            # create an Image instance with test_image as its image field
            # test_image.name tells django where the image is located
            print( "It Worked!, ", image.image)
            # appears when the test is complete without errors
            self.assertEqual(len(Image.objects.all()), 1)


def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    profile_photo = Image.new("RGBA", size, color)
    profile_photo.save(temp_file, 'jpeg')
    return temp_file

class ProfileDummyTest(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    # gettempdir() gets images from the temp file created running tests
    # overrides the default media directory to avoid dumping test images in that directory
    def test_dummy_test(self):
            temp_file = tempfile.NamedTemporaryFile()
            # create a temp file to store temp test images
            test_image = get_temporary_image(temp_file)
            # create a small square  and save it in the temp file
            # test_image.seek(0) --> this test an image as an attached
            # file thats in http request
            # test_image.seek(0)
            # response = self.client.put(
            #     self.reverse('upload_user_picture'),
            #     {'profile_picture': test_image})
            profile_photo = Profile.objects.create(profile_photo=test_image.name)
            # create an Image instance with test_image as its image field
            # test_image.name tells django where the image is located
            print( "It Worked!, ", profile_photo.profile_photo)
            # appears when the test is complete without errors
            self.assertEqual(len(Profile.objects.all()), 1)