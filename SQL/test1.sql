select * from perf 
		where  ( patronymic in ('Leonidovich', 'Igorevich', 'Maksimovich','Valerevna', 'Dmitrievna', 'Arkadevna','Viktorovna', 'Andreevna')
				or favorite_writer in ('Sergei Yesenin' , 'Leo Tolstoy' , 'Alexei Tolstoy' ,  'Anton Chekhov' ) and (age < 30 and age > 20) or (sexual_partners>3 and children < 2 )
		and marrige_form = 'monogamy' and favorite_singer in ('Artik & Asti' , 'Twenty one pilots' ,'Egor Kreed' , 'feduc' , 'Valery Meladze')
		or average_school_mark >= 3 and (smoking = true and drinking = true) and favorite_music = 'country'
		and favorite_color in ('black', 'violet', 'wine') and (school_graduation between '1967/08/30' and '1980/03/31')
		and (university_admission between '1950/09/15' and '1967/03/31') and (kindergarten_admission between '1994/10/20' and '1995/03/31')
		and pet_owner = true and healthy_lifestyle = true or temperament in ('sanguine' ,'melancholic') and (marriages_amount > 2 and marriages_amount < 4) )


