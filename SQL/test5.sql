SELECT name, surname, patronymic, religion
FROM perf
WHERE (
  home_country = 'Russia' AND
  favorite_season = 'winter' OR
  religion in (
      SELECT religion
      FROM perf
      WHERE (
        sexual_partners > 5 AND
        home_country = 'USA'
      )
    )
)

EXCEPT

SELECT name, surname, patronymic, religion
FROM perf
WHERE (
  hometown = 'Chelyabinsk' AND
  favorite_music IN ('rock', 'techno') OR
  age < 30 and 
	marrige_form in (
    SELECT marrige_form
      FROM perf
      WHERE (
        sexual_partners < 3 AND
        smoking = false AND
		drinking = false
      )
    )
)


