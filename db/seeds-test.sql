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
INTO users
(
  user_id,
  username,
  email,
  hashed_pwd,
  created_at
)
VALUES
(
  'abc123def456',
  'janedoe',
  'jane@doe.ie',
  '\x6861736865645f70617373776f7264',
  '2024-05-31 16:01:32.03385'
);

INSERT
INTO top_artists
(
  id,
  name,
  popularity,
  genres,
  followers,
  image_url,
  user_id
)
VALUES
(
  '0lAWpj5szCSwM4rUMHYmrr',
  'Måneskin',
  79,
  ARRAY['indie rock italiano', 'italian pop'],
  9133398,
  'https://i.scdn.co/image/ab6761610000e5eb46d0db8a86fda630ec12401f',
  'abc123def456'
),
(
  '6XyY86QOPPrYVGvF9ch6wz',
  'Linkin Park',
  83,
  ARRAY['alternative metal', 'nu metal', 'post-grunge', 'rap metal', 'rock'],
  25451916,
  'https://i.scdn.co/image/ab6761610000e5eb84a0dd74f21e8acce6a9fd49',
  'abc123def456'
),
(
  '3bmFPbLMiLxtR9tFrTcKcP',
  'Matthew Wilder',
  55,
  ARRAY['new wave pop'],
  47936,
  'https://i.scdn.co/image/ab6761610000e5eb5dcabf363571181dba3ecf66',
  'abc123def456'
);

INSERT
INTO top_albums
(
  id,
  name,
  popularity,
  release_year,
  total_tracks,
  image_url,
  artist_id,
  user_id
)
VALUES
(
  '2coqGqbnSCAy740mClWesA',
  'I Don''t Speak The Language',
  61,
  '1983',
  9,
  'https://i.scdn.co/image/ab67616d0000b2739824c6e084b02d24b2e22e94',
  '3bmFPbLMiLxtR9tFrTcKcP',
  'abc123def456'
);

INSERT
INTO top_songs
(
  id,
  name,
  artist_id,
  album_id,
  popularity,
  duration_ms,
  track_number
)
VALUES
(
  '1mCsF9Tw4AkIZOjvZbZZdT',
  'Break My Stride',
  '3bmFPbLMiLxtR9tFrTcKcP',
  '2coqGqbnSCAy740mClWesA',
  72,
  184480,
  1
);
