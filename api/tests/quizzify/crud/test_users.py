import unittest
from quizzify.crud import users as crud_users
from quizzify.utils.schemas import User
from quizzify.utils.helpers import encode_str_to_base64


class TestCrudUsers(unittest.TestCase):
    def test_create_spotify_user(self):
        # Given
        spotify_id = '9876543210adgjl'
        spotify_username = 'Abigail'
        spotify_email = 'abigail@domain.ie'
        spotify_image_url = 'https://image.com/abigail.jpg'
        spotify_uri = 'spotify:user:9876543210adgjl'

        # When
        crud_users.create_spotify_user(
            spotify_id=spotify_id,
            spotify_username=spotify_username,
            spotify_email=spotify_email,
            spotify_image_url=spotify_image_url,
            spotify_uri=spotify_uri,
        )

        # Then
        result = crud_users.get_user_by_spotify_id(
            spotify_id=spotify_id
        )
        self.assertEqual(result[0]['spotify_id'], spotify_id)
        self.assertEqual(len(result), 1)

    def test_create_user(self):
        # Given
        spotify_id = '9876543210adgjl'
        spotify_username = 'Abigail'
        spotify_email = 'abigail@domain.ie'

        # When
        crud_users.create_user(
            user_id=spotify_id,
            username=spotify_username,
            email=spotify_email,
            hashed_pwd='hashed_password',
        )

        # Then
        result = crud_users.get_user_by_spotify_id(
            spotify_id=spotify_id
        )
        self.assertEqual(result[0]['spotify_id'], spotify_id)
        self.assertEqual(len(result), 1)

    def test_get_user_by_email(self):
        # Given
        email = 'jane@doe.ie'
        hashed_pwd = "hashed_password"
        encoded_hashed_pwd = encode_str_to_base64(hashed_pwd)

        # When
        result = crud_users.get_user_by_email(
            email=email
        )

        # Then
        self.assertEqual(result[0]['username'], 'janedoe')
        self.assertEqual(result[0]['email'], email)
        self.assertEqual(len(result), 1)

    def test_get_user_by_spotify_id(self):
        # Given
        spotify_id = '9876543210adgjl'

        # When
        result = crud_users.get_user_by_spotify_id(
            spotify_id=spotify_id
        )

        # Then
        self.assertEqual(result[0]['spotify_id'], spotify_id)
        self.assertEqual(len(result), 1)

    def test_get_user_by_username(self):
        # Given
        username = 'janedoe'

        # When
        result = crud_users.get_user_by_username(
            username=username
        )

        # Then
        self.assertEqual(result[0]['username'], username)
        self.assertEqual(len(result), 1)
