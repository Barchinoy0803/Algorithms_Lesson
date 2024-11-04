import pymysql

class BookShop():
    def __init__(self):
        self.connectToDatabase()
        self.createDataBase()
        self.createTable()
        self.insertIntovalues()

    def connectToDatabase(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password='0803'
        )
        self.cursor = self.db.cursor()

    def createDataBase(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS bookshop')
        self.cursor.execute('USE bookshop')

    def createTable(self):
        self.cursor.execute('DROP TABLE IF EXISTS bookshop')
        self.cursor.execute('''CREATE TABLE  bookshop(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50),
                            author VARCHAR(50),
                            year_publish INT,
                            price REAL,
                            sale INT,
                            genre VARCHAR(50),
                            lenPage INT)''')
        
    def insertIntovalues(self):
        self.cursor.execute('''INSERT INTO bookshop(name, author, year_publish, price, sale, genre, lenPage) VALUES  
                        ('Vincent & Theo', 'Raymund Slatty', 2000, 500, 10, 'Western', 500),
                        ('Charlie Chans Courage', 'Nessy Gibby', 2001, 600, 15, 'Animation', 600),
                        ('Pin', 'Sheilah Halliwell', 2002, 700, 5, 'Drama', 700),
                        ('Same Old Song (On connait la chanson)', 'Cully Boc', 2003, 800, 25, 'Thriller', 800),
                        ('Santa Claus', 'Leslie Hasling', 2004, 900, 10, 'Drama', 900),
                        ('Action in the North Atlantic', 'Natassia Turford', 2005, 1000, 15, 'Drama', 1000),
                        ('Heist', 'Rick Andrews', 2006, 1100, 5, 'Documentary', 1100),
                        ('Schizopolis', 'Sibilla Stolte', 2007, 1200, 25, 'Drama', 1200),
                        ('Game of Chance (Onnenpel)', 'Aldin McConnal', 2008, 1300, 10, 'Thriller', 1300),
                        ( 'Anne Frank Remembered', 'Agnese Spornj', 2009, 1400, 15, 'Western', 1400)
                        ''')    
        self.db.commit()

    def selectByGenre(self):
        self.cursor.execute('''SELECT genre, count(*) AS book_count
                            FROM bookshop
                            GROUP BY genre
                            HAVING book_count = (
                            SELECT MAX(book_count)
                            FROM (SELECT COUNT(*) AS book_count FROM bookshop GROUP BY genre) AS genre_count)''')   
        genre_name = self.cursor.fetchone()[0]
        self.cursor.execute('SELECT name FROM bookshop WHERE genre = %s', (genre_name))
        for i in self.cursor.fetchall():
            print(i[0]) 
        

    def selectByPricePage(self):
        self.cursor.execute('SELECT name FROM bookshop WHERE 2024-year_publish >= 10 ORDER BY price DESC, lenPage DESC LIMIT 1')
        print(self.cursor.fetchone()[0])
b = BookShop() 
b.selectByGenre()       
b.selectByPricePage() 
