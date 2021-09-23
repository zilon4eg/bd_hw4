import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://bd_hw4:pass@localhost:5432/bd_hw4')
connection = engine.connect()

connection.execute('''
    INSERT INTO genre(title) VALUES('rock');
    INSERT INTO genre(title) VALUES('power metal');
    INSERT INTO genre(title) VALUES('horror punk');
    INSERT INTO genre(title) VALUES('christian rock');
    INSERT INTO genre(title) VALUES('punk rock');
    INSERT INTO genre(title) VALUES('alternative metal');
    INSERT INTO genre(title) VALUES('art rock');
    INSERT INTO genre(title) VALUES('folk rock');
    ''')

connection.execute('''
    INSERT INTO executor(name, nickname) VALUES('би-2', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('эпидемия', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('король и шут', 'киш');
    INSERT INTO executor(name, nickname) VALUES('ария', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('алиса', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('powerwolf', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('the offspring', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('rammstein', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('egypt central', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('sabaton', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('nightwish', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('мельница', 'nickname');
    INSERT INTO executor(name, nickname) VALUES('starset', 'nickname');
    ''')

connection.execute('''
    INSERT INTO album(title, year) VALUES('горизонт событий', 2017);
    INSERT INTO album(title, year) VALUES('жизнь в сумерках', 2005);
    INSERT INTO album(title, year) VALUES('будь как дома, путник', 2000);
    INSERT INTO album(title, year) VALUES('крещение огнем', 2003);
    INSERT INTO album(title, year) VALUES('сейчас позднее, чем ты думаешь', 2003);
    INSERT INTO album(title, year) VALUES('best of the blessed', 2020);
    INSERT INTO album(title, year) VALUES('americana', 1989);
    INSERT INTO album(title, year) VALUES('conspiracy of one', 2000);
    INSERT INTO album(title, year) VALUES('reise, reise', 2004);
    INSERT INTO album(title, year) VALUES('white rabbit', 2011);
    INSERT INTO album(title, year) VALUES('the last stand', 2016);
    INSERT INTO album(title, year) VALUES('wishmaster', 2000);
    INSERT INTO album(title, year) VALUES('дорога сна', 2003);
    INSERT INTO album(title, year) VALUES('дикие травы', 2009);
    INSERT INTO album(title, year) VALUES('всадник из льда', 2011);
    INSERT INTO album(title, year) VALUES('transmissions', 2018);
    ''')

connection.execute('''
    INSERT INTO track(title, duration, album_id) VALUES('лайки', 211, 1);
    INSERT INTO track(title, duration, album_id) VALUES('феанор', 499, 2);
    INSERT INTO track(title, duration, album_id) VALUES('лесник', 193, 3);
    INSERT INTO track(title, duration, album_id) VALUES('твой новый мир', 244, 4);
    INSERT INTO track(title, duration, album_id) VALUES('битва', 301, 4);
    INSERT INTO track(title, duration, album_id) VALUES('небо славян', 275, 5);
    INSERT INTO track(title, duration, album_id) VALUES('army of the night', 201, 6);
    INSERT INTO track(title, duration, album_id) VALUES('the kids arent alright', 179, 7);
    INSERT INTO track(title, duration, album_id) VALUES('want you bad', 202, 8);
    INSERT INTO track(title, duration, album_id) VALUES('amerika', 226, 9);
    INSERT INTO track(title, duration, album_id) VALUES('white rabbit', 217, 10);
    INSERT INTO track(title, duration, album_id) VALUES('the last battle', 192, 11);
    INSERT INTO track(title, duration, album_id) VALUES('wishmaster', 264, 12);
    INSERT INTO track(title, duration, album_id) VALUES('дорога сна', 190, 13);
    INSERT INTO track(title, duration, album_id) VALUES('волкодав', 301, 14);
    INSERT INTO track(title, duration, album_id) VALUES('прощай, мой дом', 260, 15);
    INSERT INTO track(title, duration, album_id) VALUES('my demons', 288, 16);
    ''')

connection.execute('''
    INSERT INTO collection(title, year) VALUES('greatest hits', 2005);
    INSERT INTO collection(title, year) VALUES('sleeping songs', 2019);
    INSERT INTO collection(title, year) VALUES('energy', 2020);
    INSERT INTO collection(title, year) VALUES('туц-туц', 2001);
    INSERT INTO collection(title, year) VALUES('road music', 2010);
    INSERT INTO collection(title, year) VALUES('open space', 2014);
    ''')

connection.execute('''
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(1, 1);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(2, 2);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(3, 3);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(4, 1);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(5, 4);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(6, 2);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(7, 5);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(8, 6);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(9, 1);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(10, 1);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(11, 2);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(12, 8);
    INSERT INTO executor_genre(executor_id, genre_id) VALUES(13, 1);    
    ''')

connection.execute('''
    INSERT INTO executor_album(executor_id, album_id) VALUES(1, 1);
    INSERT INTO executor_album(executor_id, album_id) VALUES(2, 2);
    INSERT INTO executor_album(executor_id, album_id) VALUES(3, 3);
    INSERT INTO executor_album(executor_id, album_id) VALUES(4, 4);
    INSERT INTO executor_album(executor_id, album_id) VALUES(5, 5);
    INSERT INTO executor_album(executor_id, album_id) VALUES(6, 6);
    INSERT INTO executor_album(executor_id, album_id) VALUES(7, 7);
    INSERT INTO executor_album(executor_id, album_id) VALUES(7, 8);
    INSERT INTO executor_album(executor_id, album_id) VALUES(8, 9);
    INSERT INTO executor_album(executor_id, album_id) VALUES(9, 10);
    INSERT INTO executor_album(executor_id, album_id) VALUES(10, 11);
    INSERT INTO executor_album(executor_id, album_id) VALUES(11, 12);
    INSERT INTO executor_album(executor_id, album_id) VALUES(12, 13);
    INSERT INTO executor_album(executor_id, album_id) VALUES(12, 14);
    INSERT INTO executor_album(executor_id, album_id) VALUES(13, 16);
    INSERT INTO executor_album(executor_id, album_id) VALUES(2, 15);
    ''')

connection.execute('''
    INSERT INTO track_collection(track_id, collection_id) VALUES(8, 1);
    INSERT INTO track_collection(track_id, collection_id) VALUES(9, 1);
    INSERT INTO track_collection(track_id, collection_id) VALUES(16, 2);
    INSERT INTO track_collection(track_id, collection_id) VALUES(17, 2);
    INSERT INTO track_collection(track_id, collection_id) VALUES(6, 2);
    INSERT INTO track_collection(track_id, collection_id) VALUES(7, 3);
    INSERT INTO track_collection(track_id, collection_id) VALUES(9, 3);
    INSERT INTO track_collection(track_id, collection_id) VALUES(12, 3);
    INSERT INTO track_collection(track_id, collection_id) VALUES(13, 3);
    INSERT INTO track_collection(track_id, collection_id) VALUES(15, 5);
    INSERT INTO track_collection(track_id, collection_id) VALUES(14, 5);
    INSERT INTO track_collection(track_id, collection_id) VALUES(17, 4);
    INSERT INTO track_collection(track_id, collection_id) VALUES(2, 6);
    INSERT INTO track_collection(track_id, collection_id) VALUES(10, 6);
    INSERT INTO track_collection(track_id, collection_id) VALUES(12, 6);
    ''')