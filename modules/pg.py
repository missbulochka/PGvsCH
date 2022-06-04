import time
import random
import datetime

dictionary = {
     1 : 31, 
     3 : 31, 
     5: 31,
     7 : 31,
     10 : 31,
     12 : 31,
     2 : 28,
     4 : 30,
     6 : 30,
     8 : 30,
     9 : 30,
     11 : 30
};


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
    'Omsk': 'Russia',
    'Novgorod': 'Russia',
    'Rastov-na-Donu': 'Russia',
    'Kaluga': 'Russia',
    'Severny': 'Russia',
    'Vladikavkaz': 'Russia' ,
    'New York': 'USA',
    'California': 'USA',
    'Boston': 'USA',
    'Chicago': 'USA',
    'Wshington' : 'USA',
    'Ottawa' : 'Canada',
    'Oslo' : 'Norway',
    'Beijing' : 'China',
    'Minsk' : 'Belorus',
    'Madrid': 'Italy',
    'Rome': 'Italy',
    'Milan' : 'Italy',
    'Mumbai' : 'India'
};

colors1 = ['yellow', 'red', 'blue', 'orange', 'green', 'purple', 'pink', 'brown', 'white', 'black', 'violet', 'wine'];
animals1 = ['cat', 'dog', 'elephant', 'horse', 'beetle', 'dolphin', 'capybara', 'parrot', 'hamster', 'fox', 'wolf', 'ostrich', 'kangaroo',
             'rat', 'rabbit'];
religions1 = ['christianity' , 'islam' , 'buddhism' , 'catholicism' , 'agnocism' , 'hinduism' , 'protestantism'];
forms1 = ['polygamy' , 'monogamy'];
orientations1 = ['heterosexual' , 'homosexual' , 'bisexual'];
singers1 = ['Alla Pugacheva' , 'Konstantin Kinchev' , 'Nothing but Thieves' , 'Two feet' , 'Imagine Dragons' , 'Nicki Minaj' , 'Scriptonite' ,
             'Artik & Asti' , 'Twenty one pilots' , 'Stray kids' , 'TXT' , 'PSY' ,  'Sevdaliza' , 'Thirty Seconds to Mars' , 'Rammstein' ,
             'SQWOZ BAB' , 'Eldar Dzharakhov' , 'Allj' , 'Egor Kreed' , 'feduc' , 'Valery Meladze' , 'Grigory Leps' , 'Nikolay Baskov' ,
               'Basta' , 'Iosif Kobzon'];
seasons1 = ['winter' , 'spring' , 'summer' , 'autumn'];
music_genres1 = ['blues' , 'classical' , 'country' , 'dance' , 'easy listening' , 'electronic' , 'folk' , 'heavy metal' , 'hip hop' , 'jazz' ,
                 'Latin' , 'opera' , 'pop' ,'rap' , 'reggae' , 'rock' , 'techno'];
writers1 = ['Alexander Pushkin' , 'Sergei Yesenin' , 'Leo Tolstoy' , 'Alexei Tolstoy' ,  'Anton Chekhov' , 'Mikhail Lermontov' , 'Agatha Christie',
             'John Boyne' , 'Alexander Kuprin' , 'Thomas Keneally' , 'Ray Bradbury' , 'Theoder Dreiser' ,  'Mikhail Bulgakov'];
artists1 = ['Vasily Perov', 'Ivan Aivazovsky', 'Hieronymus Bosch', 'Vasily Surikov', 'Wassily Kandinsky', 'Pablo Picasso', 'Henri Matisse',
             'Viktor Vasnetsov', 'Claude Monet', 'Ilya Repin', 'Vincent van Gogh', 'Edgar Degas', 'Arkhip Kuindzhi', 'Ivan Shishkin'];
temperaments1 = ['sanguine', 'choleric', 'melancholic', 'phlegmatic'];
bool1 = [0,1];
city_name = ['California','Boston','Chicago','Wshington','Beijing','New York', 'Ottawa','Oslo','Moscow','St Petersburg','Milan','Minsk','Mumbai',
			'Madrid','Rome','Saratov','Rzhev','Nalchik','Dagestan','Grozny','Chelyabinsk','Omsk','Novgorod','Rastov-na-Donu','Kaluga','Severny','Vladikavkaz'];

Bool = [True,False];

now_year = datetime.datetime.now().year; 

woman_name = ['Veronika', 'Lydmila', 'Yliya', 'Karina', 'Nataliya', 'Alena', 'Svetlana', 'Lybov', 'Klara', 'Sofiya', 'Nataliya',
             'Yliya', 'Karina', 'Kristina', 'Marina', 'Evgeniya', 'Viktoriya', 'Mariya', 'Elizaveta', 'Veronika', 'Eva', 'Inna',
             'Irina', 'Polina', 'Veronika', 'Larisa', 'Tamara', 'Kristina', 'Raisa', 'Polina'];
man_name = ['Ruslan', 'Maksim', 'Yriy', 'Vitaliy', 'Gennadiy', 'Vyacheslav', 'Artem', 'Igor', 'Gerasim', 'Gerasim', 'Aleksandr',
             'Fedor', 'Vadim', 'Oleg', 'Denis', 'Albert', 'Oleg', 'Roman', 'Stepan', 'Aleksey', 'Kirill', 'Gerasim', 'Oleg', 'Fedor', 
             'Fedor', 'Nikolay', 'Grigoriy', 'Aleksey', 'Taras', 'Aleksey'];
woman_surname = ['Antamanova', 'Tyrynkova', 'Zaglazeeva', 'Paroykova', 'Makisova', 'Voytovskaya', 'Karsalova', 'Gemogenova', 'Sanochkina',
                 'Bryatkova', 'Prilskaya', 'Lymoshina', 'Barontseva', 'Ukrayntseva', 'Chenikova', 'Zabegalova', 'Ionicheva', 'Hrimina', 
                 'Sputnitskaya', 'Kultysheva', 'Sadetskaya', 'Shmondina', 'Podtsiorina', 'Hamchunova', 'Krukovskaya', 'Matschina', 'Tymenbaeva',
                  'Menshutina', 'Galkova', 'Bychihina'];
man_surname = ['Kersov', 'Kulbyakin', 'Burlimov', 'Podkladkin', 'Klyagin', 'Kravtsunov', 'Rogonkov', 'Pyshkov', 'Abulhanov', 'Kulichev',
                 'Formenov', 'Techiev', 'Gapasov', 'Tromin', 'Svichkanev', 'Ischukov', 'Shanchenkov', 'Tarygin', 'Slizov', 'Madulov', 'Svirelin',
                  'Pridorogin', 'Fominkov', 'Zhukolin', 'Vysotskiy', 'Ukraintsev', 'Babolin', 'Sizov', 'Golobokih', 'Begtin'];
woman_patronamic = ['Egorovna', 'Viktorovna', 'Andreevna', 'Alekseevna', 'Dmitrievna', 'Kirillovna', 'Sergeevna', 'Igorevna', 'Viktorovna',
                 'Vadimovna', 'Andreevna', 'Yakovlevna', 'Maksimovna', 'Nikolaevna', 'Leonidovna', 'Valerevna', 'Arkadevna', 'Egorovna',
                  'Romanovna', 'Sergeevna', 'Sergeevna', 'Valerevna', 'Dmitrievna', 'Arkadevna', 'Petrovna',
                   'Yakovlevna', 'Ivanovna', 'Maksimovna'];
man_patronamic = ['Aleksievich', 'Danilovich', 'Alekseevich', 'Evgenevich', 'Vitalievich', 'Borisovich', 'Antonovich', 'Adamovich', 'Andreevich',
                 'Leonidovich', 'Leonidovich', 'Igorevich', 'Maksimovich', 'Yakovlevich', 'Danilovich', 'Adamovich', 'Vasilievich', 'Timofeevich',
                  'Adamovich', 'Vasilievich', 'Andreevich', 'Vasilievich', 'Danilovich', 'Petrovich', 'Evgenevich', 'Valerievich', 'Evgenevich',
                   'Vadimovich', 'Viktorovich', 'Pavlovich'];


def migrate(conn):
    cursor = conn.cursor()

    cursor.execute("""CREATE TYPE colors AS ENUM ('yellow', 'red', 'blue', 'orange', 'green', 'purple', 'pink', 'brown', 'white', 'black', 'violet', 'wine');
			CREATE TYPE animals AS ENUM ('cat', 'dog', 'elephant', 'horse', 'beetle', 'dolphin', 'capybara', 'parrot', 'hamster', 'fox', 'wolf', 'ostrich', 'kangaroo', 'rat', 'rabbit');
			CREATE TYPE religions AS ENUM ('christianity' , 'islam' , 'buddhism' , 'catholicism' , 'agnocism' , 'hinduism' , 'protestantism');
			CREATE TYPE forms AS ENUM ('polygamy' , 'monogamy');
			CREATE TYPE orientations AS ENUM ('heterosexual' , 'homosexual' , 'bisexual');
			CREATE TYPE singers AS ENUM ('Alla Pugacheva' , 'Konstantin Kinchev' , 'Nothing but Thieves' , 'Two feet' , 'Imagine Dragons' , 'Nicki Minaj' , 'Scriptonite' , 'Artik & Asti' , 'Twenty one pilots' , 'Stray kids' , 'TXT' , 'PSY' ,  'Sevdaliza' , 'Thirty Seconds to Mars' , 'Rammstein' ,  'SQWOZ BAB' , 'Eldar Dzharakhov' , 'Allj' , 'Egor Kreed' , 'feduc' , 'Valery Meladze' , 'Grigory Leps' , 'Nikolay Baskov' ,  'Basta' , 'Iosif Kobzon');
			CREATE TYPE seasons AS ENUM ('winter' , 'spring' , 'summer' , 'autumn');
			CREATE TYPE music_genres AS ENUM ('blues' , 'classical' , 'country' , 'dance' , 'easy listening' , 'electronic' , 'folk' , 'heavy metal' , 'hip hop' , 'jazz' , 'Latin' , 'opera' , 'pop' ,'rap' , 'reggae' , 'rock' , 'techno' );
			CREATE TYPE writers AS ENUM ('Alexander Pushkin' , 'Sergei Yesenin' , 'Leo Tolstoy' , 'Alexei Tolstoy' ,  'Anton Chekhov' , 'Mikhail Lermontov' , 'Agatha Christie' , 'John Boyne' , 'Alexander Kuprin' , 'Thomas Keneally' , 'Ray Bradbury' , 'Theoder Dreiser' ,  'Mikhail Bulgakov');
			CREATE TYPE artists AS ENUM ('Vasily Perov', 'Ivan Aivazovsky', 'Hieronymus Bosch', 'Vasily Surikov', 'Wassily Kandinsky', 'Pablo Picasso', 'Henri Matisse', 'Viktor Vasnetsov', 'Claude Monet', 'Ilya Repin', 'Vincent van Gogh', 'Edgar Degas', 'Arkhip Kuindzhi', 'Ivan Shishkin');
			CREATE TYPE temperaments AS ENUM ('sanguine', 'choleric', 'melancholic', 'phlegmatic');

			CREATE TABLE perf (
				id SERIAL PRIMARY KEY,
				name VARCHAR(20),
				surname VARCHAR(20),
				patronymic VARCHAR(20),
				age INT,
				birthday_date DATE,
				kindergarten_admission DATE,
				kindergarten_graduation DATE,
				school_admission DATE,
				school_graduation DATE,
				university_admission DATE,
				university_graduation DATE,
				work_starting DATE,
				work_ending DATE,
				sexual_partners INT,
				children INT,
				convictions INT,
				religion religions,
				marrige_form forms,
				sexual_orientation orientations,
				average_school_mark REAL,
				average_high_school_mark REAL,
				smoking BOOL,
				drinking BOOL,
				favorite_season seasons,
				favorite_music music_genres,
				favorite_artist artists,
				favorite_writer writers,
				favorite_singer singers,
				favorite_number INT,
				favorite_color colors,
				favorite_animal animals,
				marriages_amount INT,
				hometown VARCHAR(30),
				home_country VARCHAR(30),
				current_town VARCHAR(30),
				current_country VARCHAR(30),
				pet_owner BOOL,
				healthy_lifestyle BOOL,
				temperament temperaments
			);

			""")

    cursor.close()


def fio():
    if(random.choice(Bool) == True):
        return [random.choice(woman_name),random.choice(woman_surname),random.choice(woman_patronamic)];
    else:
        return [random.choice(man_name),random.choice(man_surname),random.choice(man_patronamic)]



def insert(conn):
	cursor = conn.cursor();
	with conn.cursor() as cursor:
		str1 ='';
		str2 = ';'
		for i in range(100000):
			age = random.randint(26,80);
			FIO = fio();
			city1 = random.choice(city_name);
			city2 = random.choice(city_name);
			month_ = random.randint(1,12);
			str = """INSERT INTO perf (
									name ,surname ,patronymic ,age,birthday_date,
									kindergarten_admission ,kindergarten_graduation,
									school_admission ,school_graduation , university_admission, university_graduation,work_starting ,
									work_ending ,sexual_partners ,children ,convictions ,religion
									,marrige_form , sexual_orientation ,average_school_mark ,average_high_school_mark ,smoking ,
									drinking ,favorite_season ,favorite_music ,favorite_artist ,favorite_writer ,
									favorite_singer ,favorite_number ,favorite_color ,favorite_animal ,
									marriages_amount ,hometown ,home_country ,current_town ,current_country ,
									pet_owner ,healthy_lifestyle ,temperament) 
									VALUES ( '{}','{}','{}', {},TIMESTAMP '{}',TIMESTAMP '{}',
									TIMESTAMP '{}',TIMESTAMP '{}',TIMESTAMP '{}',TIMESTAMP '{}',
									TIMESTAMP '{}',TIMESTAMP '{}',TIMESTAMP '{}',{},{},{},'{}',
									'{}','{}',{},{},{},{},'{}','{}','{}','{}','{}',{},'{}','{}',{},'{}','{}','{}','{}',{},{},'{}'
										)
									""".format( FIO[0],FIO[1],FIO[2],age,
										datetime.date(now_year-age,month_,dictionary.get(month_)),
										datetime.date(now_year-age+3,9,1),
										datetime.date(now_year-age+7,5,30),
										datetime.date(now_year-age+7,9,1),
										datetime.date(now_year-age+18,5,30),
										datetime.date(now_year-age+18,9,1),
										datetime.date(now_year-age+24,5,30),
										datetime.date(now_year-age+24+random.randint(4,10),month_,dictionary.get(month_)),
										datetime.date(now_year-age+24+random.randint(15,20),month_,dictionary.get(month_)),
										random.randint(0,4),random.randint(0,4),
										random.choice(bool1),random.choice(religions1),random.choice(forms1),random.choice(orientations1),
										random.randint(3,5),random.randint(3,5),random.choice(Bool),random.choice(Bool),
										random.choice(seasons1),random.choice(music_genres1),random.choice(artists1),random.choice(writers1),
										random.choice(singers1),random.randint(0, 100),random.choice(colors1),random.choice(animals1),
										random.randint(0,4),city1,dictionary_town_in_country.get(city1),city2,
										dictionary_town_in_country.get(city2),random.choice(Bool),random.choice(Bool),random.choice(temperaments1)
											);
			str1 = str1 + str2 + str;
			if(i%10==9):
				with conn.cursor() as cursor:
					cursor.execute("{}".format(str1));
				str1='';
	conn.commit();
