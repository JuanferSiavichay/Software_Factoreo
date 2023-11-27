import sqlite3

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect('BaseContrasena.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    Cedula TEXT,
                    Contrasena TEXT,
                    Email TEXT
                )''')

# Insertar datos
cursor.execute("INSERT INTO usuarios (Cedula, Contrasena, Email) VALUES (?, ?, ?)", ('0103952487', 'PepeJuan', 'marypenafiel@hotmail.com'))
cursor.execute("INSERT INTO usuarios (Cedula, Contrasena, Email) VALUES (?, ?, ?)", ('0151052396', 'Lola', 'juanfersiavichay7@gmail.com'))
cursor.execute("INSERT INTO usuarios (Cedula, Contrasena, Email) VALUES (?, ?, ?)", ('0151052388', 'Perrito', 'jsiavichay663@gmail.com'))
cursor.execute("INSERT INTO usuarios (Cedula, Contrasena, Email) VALUES (?, ?, ?)", ('0102455995', 'Lolita', 'fsiavichay@hotmail.com'))

# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()
