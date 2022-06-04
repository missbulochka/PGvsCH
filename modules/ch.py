import random
import datetime
import time

dictionary_town_in_country = {
    'Omsk': 'Russia',
    'Moscow': 'Russia',
    'St Petersburg': 'Russia',
    'Saratov': 'Russia',
    'Rzhev': 'Russia',
    'Nalchik': 'Russia',
    'Dagestan': 'Russia',
    'Grozny': 'Russia',
    'Chelyabinsk': 'Russia',
    'Novgorod': 'Russia',
    'Rastov-na-Donu': 'Russia',
    'Kaluga': 'Russia',
    'Severny': 'Russia',
    'Vladikavkaz': 'Russia',
    'New York': 'USA',
    'California': 'USA',
    'Boston': 'USA',
    'Chicago': 'USA',
    'Wshington': 'USA',
    'Ottawa': 'Canada',
    'Oslo': 'Norway',
    'Beijing': 'China',
    'Minsk': 'Belorus',
    'Madrid': 'Italy',
    'Rome': 'Italy',
    'Milan': 'Italy',
    'Mumbai': 'India'
}

woman_name = ['Veronika', 'Lydmila', 'Yliya', 'Karina', 'Nataliya', 'Alena', 'Svetlana', 'Lybov', 'Klara', 'Sofiya',
              'Nataliya', 'Yliya', 'Karina', 'Kristina', 'Marina', 'Evgeniya', 'Viktoriya', 'Mariya', 'Elizaveta',
              'Veronika', 'Eva', 'Inna', 'Irina', 'Polina', 'Veronika', 'Larisa', 'Tamara', 'Kristina', 'Raisa',
              'Polina']
man_name = ['Ruslan', 'Maksim', 'Yriy', 'Vitaliy', 'Gennadiy', 'Vyacheslav', 'Artem', 'Igor', 'Gerasim', 'Gerasim',
            'Aleksandr', 'Fedor', 'Vadim', 'Oleg', 'Denis', 'Albert', 'Oleg', 'Roman', 'Stepan', 'Aleksey', 'Kirill',
            'Gerasim', 'Oleg', 'Fedor', 'Fedor', 'Nikolay', 'Grigoriy', 'Aleksey', 'Taras', 'Aleksey']
woman_surname = ['Antamanova', 'Tyrynkova', 'Zaglazeeva', 'Paroykova', 'Makisova', 'Voytovskaya', 'Karsalova',
                 'Gemogenova', 'Sanochkina', 'Bryatkova', 'Prilskaya', 'Lymoshina', 'Barontseva', 'Ukrayntseva',
                 'Chenikova', 'Zabegalova', 'Ionicheva', 'Hrimina', 'Sputnitskaya', 'Kultysheva', 'Sadetskaya',
                 'Shmondina', 'Podtsiorina', 'Hamchunova', 'Krukovskaya', 'Matschina', 'Tymenbaeva', 'Menshutina',
                 'Galkova', 'Bychihina']
man_surname = ['Kersov', 'Kulbyakin', 'Burlimov', 'Podkladkin', 'Klyagin', 'Kravtsunov', 'Rogonkov', 'Pyshkov',
               'Abulhanov', 'Kulichev', 'Formenov', 'Techiev', 'Gapasov', 'Tromin', 'Svichkanev', 'Ischukov',
               'Shanchenkov', 'Tarygin', 'Slizov', 'Madulov', 'Svirelin', 'Pridorogin', 'Fominkov', 'Zhukolin',
               'Vysotskiy', 'Ukraintsev', 'Babolin', 'Sizov', 'Golobokih', 'Begtin']
woman_patronamic = ['Egorovna', 'Viktorovna', 'Andreevna', 'Alekseevna', 'Dmitrievna', 'Kirillovna', 'Sergeevna',
                    'Igorevna', 'Viktorovna', 'Vadimovna', 'Andreevna', 'Yakovlevna', 'Maksimovna', 'Nikolaevna',
                    'Leonidovna', 'Valerevna', 'Arkadevna', 'Egorovna', 'Romanovna', 'Sergeevna', 'Sergeevna',
                    'Valerevna', 'Dmitrievna', 'Arkadevna', 'Petrovna', 'Yakovlevna', 'Ivanovna', 'Maksimovna']
man_patronamic = ['Aleksievich', 'Danilovich', 'Alekseevich', 'Evgenevich', 'Vitalievich', 'Borisovich', 'Antonovich',
                  'Adamovich', 'Andreevich', 'Leonidovich', 'Leonidovich', 'Igorevich', 'Maksimovich', 'Yakovlevich',
                  'Danilovich', 'Adamovich', 'Vasilievich', 'Timofeevich', 'Adamovich', 'Vasilievich', 'Andreevich',
                  'Vasilievich', 'Danilovich', 'Petrovich', 'Evgenevich', 'Valerievich', 'Evgenevich', 'Vadimovich',
                  'Viktorovich', 'Pavlovich']
city_name = ['California', 'Boston', 'Chicago', 'Wshington', 'Beijing', 'New York', 'Ottawa', 'Oslo', 'Moscow',
             'St Petersburg', 'Milan', 'Minsk', 'Mumbai', 'Madrid', 'Rome', 'Saratov', 'Rzhev', 'Nalchik', 'Dagestan',
             'Grozny', 'Chelyabinsk', 'Omsk', 'Novgorod', 'Rastov-na-Donu', 'Kaluga', 'Severny', 'Vladikavkaz']
    

def migrate(conn):
    conn.execute('CREATE DATABASE IF NOT EXISTS perfdb;')

    conn.execute("""
      CREATE TABLE IF NOT EXISTS perfdb.perf (
  	  `id` UUID,
	  `name` String,
	  `surname` String,
	  `patronymic` String,
	  `age` UInt8,
	  `birthday_date` Date,
	  `kindergarten_admission` Date,
	  `kindergarten_graduation` Date,
	  `school_admission` Date,
	  `school_graduation` Date,
	  `university_admission` Date,
	  `university_graduation` Date,
	  `work_starting` Date,
	  `work_ending` Date,
	  `sexual_partners` UInt8,
	  `children` UInt8,
	  `convictions` UInt8,
	  `religion` Enum8('christianity' = 1, 'islam' = 2, 'buddhism' = 3, 'catholicism' = 4, 'agnocism' = 5, 'hinduism' = 6, 'protestantism' = 7),
	  `marrige_form` Enum8('polygamy' = 1, 'monogamy' = 2),
	  `sexual_orientation` Enum8('heterosexual' = 1, 'homosexual' = 2, 'bisexual' = 3),
	  `average_school_mark` Float32,
	  `average_high_school_mark` Float32,
	  `smoking` Bool,
	  `drinking` Bool,
	  `favorite_season` Enum8('winter' = 1, 'spring' = 2, 'summer' = 3, 'autumn' = 4),
	  `favorite_music` Enum8('blues' = 1, 'classical' = 2, 'country' = 3, 'dance' = 4, 'easy listening' = 5, 'electronic' = 6, 'folk' = 7, 'heavy metal' = 8, 'hip hop' = 9, 'jazz' = 10, 'Latin' = 11, 'opera' = 12, 'pop' = 13,'rap' = 14, 'reggae' = 15, 'rock' = 16, 'techno' = 17),
	  `favorite_artist` Enum8('Vasily Perov' = 1, 'Ivan Aivazovsky' = 2, 'Hieronymus Bosch' = 3, 'Vasily Surikov' = 4, 'Wassily Kandinsky' = 5, 'Pablo Picasso' = 6, 'Henri Matisse' = 7, 'Viktor Vasnetsov' = 8, 'Claude Monet' = 9, 'Ilya Repin' = 10, 'Vincent van Gogh' = 11, 'Edgar Degas' = 12, 'Arkhip Kuindzhi' = 13, 'Ivan Shishkin' = 14),
	  `favorite_writer` Enum8('Alexander Pushkin' = 1, 'Sergei Yesenin' = 2, 'Leo Tolstoy' = 3, 'Alexei Tolstoy' = 4,  'Anton Chekhov' = 5, 'Mikhail Lermontov' = 6, 'Agatha Christie' = 7, 'John Boyne' = 8, 'Alexander Kuprin' = 9, 'Thomas Keneally' = 10, 'Ray Bradbury' = 11, 'Theoder Dreiser' = 12,  'Mikhail Bulgakov' = 13),
	  `favorite_singer` Enum8('Alla Pugacheva' = 1, 'Konstantin Kinchev' = 2, 'Nothing but Thieves' = 3, 'Two feet' = 4, 'Imagine Dragons' = 5, 'Nicki Minaj' = 6, 'Scriptonite' = 7, 'Artik & Asti' = 8, 'Twenty one pilots' = 9, 'Stray kids' = 10, 'TXT' = 11, 'PSY' = 12,  'Sevdaliza' = 13, 'Thirty Seconds to Mars' = 14, 'Rammstein' = 15,  'SQWOZ BAB' = 16, 'Eldar Dzharakhov' = 17, 'Allj' = 18, 'Egor Kreed' = 19, 'feduc' = 20, 'Valery Meladze' = 21, 'Grigory Leps' = 22, 'Nikolay Baskov' = 23,  'Basta' = 24, 'Iosif Kobzon' = 25),
	  `favorite_number` Int8,
	  `favorite_color` Enum8('yellow' = 1, 'red' = 2, 'blue' = 3, 'orange' = 4, 'green' = 5, 'purple' = 6, 'pink' = 7, 'brown' = 8, 'white' = 9, 'black' = 10, 'violet' = 11, 'wine' = 12),
	  `favorite_animal` Enum8('cat' = 1, 'dog' = 2, 'elephant' = 3, 'horse' = 4, 'beetle' = 5, 'dolphin' = 6, 'capybara' = 7, 'parrot' = 8, 'hamster' = 9, 'fox' = 10, 'wolf' = 11, 'ostrich' = 12, 'kangaroo' = 13, 'rat' = 14, 'rabbit' = 15),
	  `marriages_amount` UInt8,
	  `hometown` String, 
	  `home_country` String,
	  `current_town` String,
	  `current_country` String,
	  `pet_owner` Bool,
	  `healthy_lifestyle` Bool,
	  `temperament` Enum8('sanguine' = 1, 'choleric' = 2, 'melancholic' = 3, 'phlegmatic' = 4)
	  ) ENGINE = MergeTree()
          ORDER BY (birthday_date)
          PARTITION BY (current_country)
      """)


def insert(conn):
    for _ in range(500):
        r_str = "INSERT INTO perfdb.perf VALUES"
        str1 = ''
        now_date = datetime.datetime.today()

        for i in range(200):
            p_age = random.randint(26, 52)
            if (random.randint(0, 1) == 1):
                p_fio = [random.choice(woman_name), random.choice(woman_surname), random.choice(woman_patronamic)]
            else:
                p_fio = [random.choice(man_name), random.choice(man_surname), random.choice(man_patronamic)]
            city1 = random.choice(city_name)
            city2 = random.choice(city_name)

            str1 = f"""
                (
                generateUUIDv4(),
                '{p_fio[0]}',
                '{p_fio[1]}',
                '{p_fio[2]}',
                {p_age},
                '{now_date.year - p_age}-{random.randint(1, 12)}-{random.randint(1, 28)}',
                '{now_date.year - p_age + 3}-09-01',
                '{now_date.year - p_age + 7}-05-30',
                '{now_date.year - p_age + 7}-09-01',
                '{now_date.year - p_age + 18}-05-30',
                '{now_date.year - p_age + 18}-09-01',
                '{now_date.year - p_age + 24}-07-30',
                '{now_date.year - p_age + 24 + random.randint(4, 10)}-{random.randint(1, 12)}-{random.randint(1, 28)}',
                '{now_date.year - p_age + 24 + random.randint(15, 20)}-{random.randint(1, 12)}-{random.randint(1, 28)}',
                {random.randint(0, 100)},
                {random.randint(0, 7)},
                {random.randint(0, 2)},
                {random.randint(1, 7)},
                {random.randint(1, 2)},
                {random.randint(1, 3)},
                {round(random.uniform(3, 5), 2)},
                {round(random.uniform(3, 5), 2)},
                {random.randint(0, 1)},
                {random.randint(0, 1)},
                {random.randint(1, 4)},
                {random.randint(1, 17)},
                {random.randint(1, 14)},
                {random.randint(1, 13)},
                {random.randint(1, 25)},
                {random.randint(0, 100)},
                {random.randint(1, 12)},
                {random.randint(1, 15)},
                {random.randint(0, 4)},
                '{city1}',
                '{dictionary_town_in_country.get(city1)}',
                '{city2}',
                '{dictionary_town_in_country.get(city2)}',
                {random.randint(0, 1)},
                {random.randint(0, 1)},
                {random.randint(1, 4)}
                )
                """
            if i < 200-1:
                r_str = r_str + str1 + ", "
            else:
                r_str = r_str + str1 + ';'
        conn.execute(r_str)
