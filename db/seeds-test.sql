INSERT
  INTO spotify_users (
    spotify_id,
    spotify_username,
    spotify_email,
    spotify_image_url,
    spotify_uri
  )
  VALUES (
    'abc123def456',
    'Jane',
    'jane@doe.ie',
    'https://fakeurl.ie',
    'spotify:user:abc123def456'
  );

INSERT
  INTO users (
    user_id,
    username,
    email,
    hashed_pwd,
    created_at
  )
  VALUES (
    'abc123def456',
    'janedoe',
    'jane@doe.ie',
    '\x12345678901234567890',
    '2024-05-31 16:01:32.03385'
  );