SELECT DISTINCT ON ( marrige_form) name, surname, patronymic
FROM perf
WHERE (
  smoking = false AND
  drinking = false AND
  children > 1 AND
  marrige_form in (
    SELECT marrige_form
    FROM perf
    WHERE birthday_date BETWEEN 
      TO_DATE('1980-01-01', 'yyyy-mm-dd') AND
      TO_DATE('1990-01-01', 'yyyy-mm-dd')
  )
) OR (
  average_school_mark > 4 AND
  healthy_lifestyle = true AND
  (
    sexual_orientation = 'bisexual' OR
    religion in (
      SELECT religion
      FROM perf
      WHERE (
        sexual_partners > 5 AND
        home_country = 'USA'
      )
    )
  )
)
ORDER BY marrige_form
