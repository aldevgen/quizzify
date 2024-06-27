----------------------------------------------------------------------------------------
---------------------------------------- USERS -----------------------------------------
----------------------------------------------------------------------------------------
INSERT INTO users_spotify (
  spotify_id, spotify_username, spotify_email, spotify_image_url, spotify_uri
)
VALUES (
  'abc123def456',
  'Jane',
  'jane@doe.ie',
  'https://fakeurl.ie',
  'spotify:user:abc123def456'
);

INSERT INTO users_quizzify (user_id, username, email, hashed_pwd, created_at)
VALUES (
  'abc123def456',
  'janedoe',
  'jane@doe.ie',
  '\x6861736865645f70617373776f7264',
  '2024-05-31 16:01:32.03385'
);

----------------------------------------------------------------------------------------
---------------------------------------- ALBUMS ----------------------------------------
----------------------------------------------------------------------------------------
INSERT INTO albums (
  id, name, popularity, release_year, release_decade, total_tracks, image_url
) VALUES (
  '2kcJ3TxBhSwmki0QWFXUz8',
  'RUSH! (ARE U COMING?)',
  73,
  '2023',
  '2020',
  22,
  'https://i.scdn.co/image/ab67616d0000b27393fcc2231abeb51d7e41ec5d'
),
(
  '3wLMnrlPtVSADxalu9kIxK',
  'RUSH!',
  63,
  '2023',
  '2020',
  18,
  'https://i.scdn.co/image/ab67616d0000b273aad7b695784a8dc4342fea8c'
),
(
  '7KF1Ain9mYYlg5M46g0i4A',
  'Teatro d''ira - Vol. I',
  77,
  '2021',
  '2020',
  8,
  'https://i.scdn.co/image/ab67616d0000b2735aa05015cfa7bd2943c29b21'
),
(
  '44a7Wk3Jh2JGVhjcFYWozj',
  'Il ballo della vita',
  70,
  '2018',
  '2010',
  12,
  'https://i.scdn.co/image/ab67616d0000b273dbc892b8194e35ca3524e767'
),
(
  '2qJw6w5XwQO0PQlSWPu7Tw',
  'Chosen',
  75,
  '2017',
  '2010',
  7,
  'https://i.scdn.co/image/ab67616d0000b273fa0ab3a28b5c52d8a5f97045'
);

----------------------------------------------------------------------------------------
--------------------------------------- ARTISTS ----------------------------------------
----------------------------------------------------------------------------------------

INSERT INTO artists (
  id, name, popularity, genres, followers, image_url
) VALUES (
  '0lAWpj5szCSwM4rUMHYmrr',
  'Måneskin',
  79,
  '{"indie rock italiano","italian pop"}',
  9225653,
  'https://i.scdn.co/image/ab6761610000e5eb46d0db8a86fda630ec12401f'
),
(
  '0C0XlULifJtAgn6ZNCW2eu',
  'The Killers',
  76,
  '{"alternative rock","dance rock","modern rock","permanent wave",rock}',
  7314419,
  'https://i.scdn.co/image/ab6761610000e5eb207b21f3ed0ee96adce3166a'
);

----------------------------------------------------------------------------------------
----------------------------------- ARTIST'S ALBUMS ------------------------------------
----------------------------------------------------------------------------------------

INSERT INTO albums_artists (artist_id, album_id) VALUES (
  '0lAWpj5szCSwM4rUMHYmrr', '2kcJ3TxBhSwmki0QWFXUz8'
),
(
  '0lAWpj5szCSwM4rUMHYmrr', '3wLMnrlPtVSADxalu9kIxK'
),
(
  '0lAWpj5szCSwM4rUMHYmrr', '7KF1Ain9mYYlg5M46g0i4A'
),
(
  '0lAWpj5szCSwM4rUMHYmrr', '44a7Wk3Jh2JGVhjcFYWozj'
),
(
  '0lAWpj5szCSwM4rUMHYmrr', '2qJw6w5XwQO0PQlSWPu7Tw'
);

INSERT INTO top_albums (album_id, user_id) VALUES (
  '44a7Wk3Jh2JGVhjcFYWozj', 'abc123def456'
);
INSERT INTO public.top_artists (artist_id, user_id) VALUES (
  '0lAWpj5szCSwM4rUMHYmrr', 'abc123def456'
);
