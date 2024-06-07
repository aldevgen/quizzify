INSERT
INTO users_spotify (
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
INTO users_quizzify
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
INTO artists
(
  id,
  name,
  popularity,
  genres,
  followers,
  image_url
)
VALUES
(
  '0lAWpj5szCSwM4rUMHYmrr',
  'Måneskin',
  79,
  ARRAY['indie rock italiano', 'italian pop'],
  9133398,
  'https://i.scdn.co/image/ab6761610000e5eb46d0db8a86fda630ec12401f'
),
(
  '6XyY86QOPPrYVGvF9ch6wz',
  'Linkin Park',
  83,
  ARRAY['alternative metal', 'nu metal', 'post-grunge', 'rap metal', 'rock'],
  25451916,
  'https://i.scdn.co/image/ab6761610000e5eb84a0dd74f21e8acce6a9fd49'
),
(
  '3bmFPbLMiLxtR9tFrTcKcP',
  'Matthew Wilder',
  55,
  ARRAY['new wave pop'],
  47936,
  'https://i.scdn.co/image/ab6761610000e5eb5dcabf363571181dba3ecf66'
);

INSERT
INTO top_artists
(
  artist_id,
  user_id
)
VALUES
(
  '0lAWpj5szCSwM4rUMHYmrr',
  'abc123def456'
),
(
  '6XyY86QOPPrYVGvF9ch6wz',
  'abc123def456'
),
(
  '3bmFPbLMiLxtR9tFrTcKcP',
  'abc123def456'
);

INSERT
INTO albums
(
  id,
  name,
  popularity,
  release_year,
  release_decade,
  total_tracks,
  image_url,
  artist_id
)
VALUES
(
  '2coqGqbnSCAy740mClWesA',
  'I Don''t Speak The Language',
  61,
  '1983',
  '1980',
  9,
  'https://i.scdn.co/image/ab67616d0000b2739824c6e084b02d24b2e22e94',
  '3bmFPbLMiLxtR9tFrTcKcP'
),
(
  '0sNOF9WDwhWunNAHPD3Baj',
  'Hybrid Theory',
  82,
  '2000',
  '2000',
  12,
  'https://i.scdn.co/image/ab67616d0000b273f4e0f8b3b8f1f3f3b3f3b3f3',
  '6XyY86QOPPrYVGvF9ch6wz'
),
(
  '2ZUwFxlDV6dP8y2fMs59fN',
  'Teatro d''ira: Vol. I',
  79,
  '2021',
  '2020',
  10,
  'https://i.scdn.co/image/ab67616d0000b273f4e0f8b3b8f1f3f3b3f3b3f3',
  '0lAWpj5szCSwM4rUMHYmrr'
);

INSERT
INTO top_songs
(
  song_id,
  user_id
)
VALUES
(
  '1mCsF9Tw4AkIZOjvZbZZdT',
  'abc123def456'
),
(
  '6hQ5vU4jWvz1bXjXj3t7yT',
  'abc123def456'
),
(
  '2gMXnyrvIjhVBUZwvLZDMP',
  'abc123def456'
);

INSERT
INTO songs
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
),
(
  '6hQ5vU4jWvz1bXjXj3t7yT',
  'In the End',
  '6XyY86QOPPrYVGvF9ch6wz',
  '0sNOF9WDwhWunNAHPD3Baj',
  85,
  216933,
  1
),
(
  '2gMXnyrvIjhVBUZwvLZDMP',
  'Beggin''',
  '0lAWpj5szCSwM4rUMHYmrr',
  '2ZUwFxlDV6dP8y2fMs59fN',
  89,
  211560,
  1
);

INSERT
INTO top_albums
(
  album_id,
  user_id
)
VALUES
(
  '2coqGqbnSCAy740mClWesA',
  'abc123def456'
),
(
  '0sNOF9WDwhWunNAHPD3Baj',
  'abc123def456'
),
(
  '2ZUwFxlDV6dP8y2fMs59fN',
  'abc123def456'
);
