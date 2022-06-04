select name, favorite_season, temperament from perf
where ( name in ('Roman','Karina','Aleksey') or favorite_season = 'autumn') and (age < 60 and age > 50) or (sexual_partners>1 and children > 1 )
and marrige_form = 'monogamy' and religion in ('christianity' , 'islam' , 'buddhism' , 'catholicism' , 'agnocism' )
or average_school_mark >= 3 and (smoking = false and drinking = true) and ( favorite_animal in ('horse', 'beetle', 'dolphin','hamster', 'fox')
and favorite_color in ('red','blue','purple')) and (birthday_date between '1967/08/30' and '1980/03/31')
and (university_admission between '1950/09/15' and '1967/03/31') and (kindergarten_admission between '1994/10/20' and '1995/03/31')
and pet_owner = true and healthy_lifestyle = true or temperament in ('sanguine' ,'melancholic') and (marriages_amount > 2 and marriages_amount < 4)
