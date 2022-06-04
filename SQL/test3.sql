SELECT name, surname, patronymic
FROM perf
WHERE (
  home_country = 'Russia' AND
  favorite_season = 'winter'
)

EXCEPT

SELECT name, surname, patronymic
FROM perf
WHERE (
  hometown = 'Chelyabinsk' AND
  favorite_music IN ('rock', 'techno') OR
  age < 30
)
