# Importar liberia Flask
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

# Inicializar
app = Flask(__name__)

# Navegacion Principal
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def inicio():
    return render_template("index.html")

@app.route('/optionl')
def oL():
    return render_template("optionLogin.html")

@app.route('/login')
def iC():
    return render_template("login.html")

@app.route('/Alogin')
def iA():
    return render_template("Alogin.html")

@app.route('/Asign')
def sA():
    return render_template("Asign.html")

@app.route('/sign')
def sC():
    return render_template("signup.html")

@app.route('/close')
def c():
    return render_template("close.html")

#Navegador Cliente
@app.route('/comentarios')
def coment():
    return render_template("comentarios.html")

@app.route('/carro')
def carro():
    return render_template("carrito.html")

@app.route('/sushi')
def sushi():
    return render_template("sushi.html")

@app.route('/ramen')
def ramen():
    return render_template("ramen.html")

@app.route('/postres')
def postres():
    return render_template("postres.html")

@app.route('/bebidas')
def bebidas():
    return render_template("bebidas.html")

@app.route('/coffee')
def coffee():
    return render_template("coffee.html")

@app.route('/pedidosC')
def pC():
    return render_template("pedidosC.html")

@app.route('/reservaC')
def rC():
    return render_template("reservaC.html")

# Navegador Administradores
@app.route('/almacen')
def a():
    return render_template("almacen.html")

@app.route('/table')
def t():
    return render_template("table.html")

@app.route('/crudAdmin')
def cA():
    return render_template("crudAdmin.html")

@app.route('/crudClient')
def cC():
    return render_template("crudClient.html")

@app.route('/editAdmin')
def eA():
    return render_template("editAdmin.html")

@app.route('/editClient')
def eC():
    return render_template("editClient.html")

# Comprobacion de base de datos
def conex():
    conn = pymysql.connect(host='localhost', user='root', passwd='')
    cursor = conn.cursor()
    # Consulta SQL para verificar la existencia de una base de datos específica (en este caso, 'db_OAGR')
    cursor.execute("SHOW DATABASES LIKE 'db_OAGR'")
    resultado = cursor.fetchone()

    # Comprueba si la base de datos existe
    if resultado:
        print("La base de datos existe.")
    else:
        print("La base de datos no existe.")
        cursor.execute("CREATE SCHEMA IF NOT EXISTS `db_OAGR` DEFAULT CHARACTER SET utf8mb4 ")
        cursor.execute("USE `db_OAGR`")

        # Define the SQL statements for table creation
        sql_statements = """
            CREATE SCHEMA IF NOT EXISTS `db_OAGR` DEFAULT CHARACTER SET utf8mb4 ;
            USE `db_OAGR` ;
            -- -----------------------------------------------------
            -- Table `db_OAGR`.`admin`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`admin` (
            `id` INT PRIMARY KEY AUTO_INCREMENT,
            `nombre` VARCHAR(100) NOT NULL,
            `correo` VARCHAR(100) NOT NULL,
            `contra` VARCHAR(10) NOT NULL);
            -- -----------------------------------------------------
            -- Table `db_OAGR`.`almacen`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`almacen` (
            `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            `producto` VARCHAR(100) NOT NULL,
            `descripcion` VARCHAR(200) DEFAULT NULL,
            `imagen` VARCHAR(100) DEFAULT NULL,
            `cantidad` INT NOT NULL,
            `precio` INT NOT NULL);
            -- -----------------------------------------------------
            -- Table `db_OAGR`.`cliente`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`cliente` (
            `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
            `nombre` VARCHAR(50) NOT NULL,
            `correo` VARCHAR(100) NOT NULL,
            `contra` VARCHAR(50) NOT NULL,
            `direccion` VARCHAR(100) DEFAULT NULL,
            `telefono` VARCHAR(10) DEFAULT NULL);

            -- -----------------------------------------------------
            -- Table `db_OAGR`.`pedidos`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`pedidos` (
            `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
            `id_cliente` INT NOT NULL,
            `id_producto` INT NOT NULL,
            `cantidad` VARCHAR(100) NOT NULL,
            `total` VARCHAR(50) NOT NULL,
            FOREIGN KEY (`id_cliente`) REFERENCES cliente(id),
            FOREIGN KEY (`id_producto`) REFERENCES almacen(id));


            -- -----------------------------------------------------
            -- Table `db_OAGR`.`reservas`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`reservas` (
            `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
            `id_cliente` INT NOT NULL,
            `hora` time NOT NULL,
            `dia` date NOT NULL,
            `nperson` int NOT NULL,
            `mesa` int NOT NULL,
            FOREIGN KEY (`id_cliente`) REFERENCES cliente(id));

            -- -----------------------------------------------------
            -- Table `db_OAGR`.`comentarios`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`comentarios` (
            `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
            `id_cliente` INT NOT NULL,
            `razon` VARCHAR(50) NOT NULL,
            `mensaje` VARCHAR(200) NOT NULL,
            FOREIGN KEY (`id_cliente`) REFERENCES cliente(id));

            -- admin predeterminado  
            insert into admin(nombre, correo, contra) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');

            -- Productos
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Agua', 'Bebidas', 'agua.png', '409', '20');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Boba', 'Bebidas', 'boba.png', '209', '30');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Coca', 'Bebidas', 'coca.png', '312', '20');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Frappe', 'Bebidas', 'frappe.png', '123', '30');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Jugo de Limon', 'Bebidas', 'jugo_limon.png', '123', '25');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Jugo de Naranja', 'Bebidas', 'jugo_naranja.png', '42', '25');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Jugo de Toronja', 'Bebidas', 'jugo_toronja.png', '34', '25');

            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Bombon', 'Cafe', 'bombon.png', '893', '40');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Capuchino', 'Cafe', 'capuchino.png', '213', '35');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Carajillo', 'Cafe', 'carajillo.png', '423', '30');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Cafe con Leche', 'Cafe', 'con_leche.png', '123', '30');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Espresso', 'Cafe', 'espresso.png', '124', '40');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Irlandes', 'Cafe', 'irlandes.png', '121', '45');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Latte Macchiato', 'Cafe', 'latte_macchiato.png', '321', '50');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Lungo', 'Cafe', 'lungo.png', '324', '45');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Macchiato', 'Cafe', 'macchiato.png', '145', '34');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mocca', 'Cafe', 'mocca.png', '221', '40');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Ristretto', 'Cafe', 'ristretto.png', '342', '55');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Vienes', 'Cafe', 'vienes.png', '532', '50');

            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Dorayaki', 'Postres', 'dorayaki.png', '234', '70');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Hanami Dango', 'Postres', 'hanami_dango.png', '564', '95');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mitarashi Dango', 'Postres', 'mitarashi_dango.png', '453', '85');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mochis', 'Postres', 'mochis.png', '533', '60');

            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Hakata', 'Ramen', 'hakata.png', '676', '80');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Kyoto', 'Ramen', 'kyoto.png', '567', '70');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Sapporo', 'Ramen', 'sapporo.png', '645', '75');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Shio', 'Ramen', 'shio.png', '876', '90');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Tokyo', 'Ramen', 'tokyo.png', '545', '90');

            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Maki', 'Comida', 'maki.png', '345', '80');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Nigiri', 'Comida', 'nigiri.png', '564', '75');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Temaki', 'Comida', 'temaki.png', '546', '50');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Uramaki', 'Comida', 'uramaki.png', '265', '82');
        """
        statements = [stmt.strip() for stmt in sql_statements.split(';') if stmt.strip()]


        # Execute each SQL statement
        for statement in statements:
            cursor.execute(statement)
            conn.commit()


        print("Base de datos y tablas creadas exitosamente")
        conn.close()


@app.route('/inicio', methods=['POST'])
def iniciar():
    if request.method == 'POST':
        aux_Nom = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        conex()
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR' )
        cursor = conn.cursor()
        cursor.execute('insert into admin (nombre, correo, contra) values (%s, %s, %s)',(aux_Nom, aux_Correo, aux_Contra))
        conn.commit()
    return redirect(url_for('home'))


@app.route('/crudAdmin')
def crudAdmin():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from admin order by id')
    datos = cursor.fetchall()
    return render_template("crudAdmin.html", comentarios = datos)

@app.route('/editAdmin/<string:id>')
def editAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from admin where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editAdmin.html", comentar=dato[0])

@app.route('/editar_admin/<string:id>',methods=['POST'])
def editar_admin(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update admin set nombre=%s, correo=%s, contra=%s where id=%s', (nom,corr,contra,id))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/borrarAd/<string:id>')
def borrarAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from admin where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/agrega_admin', methods=['POST'])
def agrega_admin():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into admin (nombre,correo,contra) values (%s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/crudClient')
def crudClient():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra, direccion, telefono from cliente order by id')
    datos = cursor.fetchall()
    return render_template("crudClient.html", comenta = datos)

@app.route('/editClient/<string:id>')
def editClient(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra, direccion, telefono from cliente where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editClient.html", comentar=dato[0])

@app.route('/editar_cliente/<string:id>',methods=['POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        direc=request.form['direccion']
        tel=request.form['telefono']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update cliente set nombre=%s, correo=%s, contra=%s, direccion=%s, telefono=%s where id=%s', (nom,corr,contra,direc,tel,id))
        conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/borrarC/<string:id>')
def borrarClient(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from cliente where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/agrega_cliente', methods=['POST'])
def agrega_cliente():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        aux_Direccion = request.form['direccion']
        aux_Telefono = request.form['telefono']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into cliente (nombre,correo,contra,direccion,telefono) values (%s, %s, %s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra, aux_Direccion, aux_Telefono))
        conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/crudAlmacen')
def crudAlmacen():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, producto, descripcion, imagen, cantidad, precio from almacen order by id')
    datos = cursor.fetchall()
    return render_template("crudAdmin.html", comentarios = datos)

@app.route('/editAlmacen/<string:id>')
def editAlmacen(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, producto, descripcion, imagen, cantidad, precio from almacen where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editAlmacen.html", comentar=dato[0])

@app.route('/editar_almacen/<string:id>',methods=['POST'])
def editar_almacen(id):
    if request.method == 'POST':
        pro=request.form['producto']
        des=request.form['descripcion']
        img=request.form['imagen']
        cant=request.form['cantidad']
        pre=request.form['precio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update almacen set producto=%s, descripcion=%s, imagen=%s, cantidad=%s, precio=%s, where id=%s', (pro,des,img,cant,pre,id))
        conn.commit()
    return redirect(url_for('crudAlmacen'))

@app.route('/borrarAl/<string:id>')
def borrarAlmacen(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from almacen where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudAlmacen'))

@app.route('/agrega_almacen', methods=['POST'])
def agrega_almacen():
    if request.method == 'POST':
        aux_Produc = request.form['producto']
        aux_Descri = request.form['descripcion']
        aux_Imagen = request.form['imagen']
        aux_Cant = request.form['cantidad']
        aux_Precio = request.form['precio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into almacen (producto,descripcion,imagen,cantidad,precio) values (%s, %s, %s,%s,%s)',(aux_Produc,aux_Descri,aux_Imagen,aux_Cant,aux_Precio))
    return redirect(url_for('crudAlmacen'))

if __name__ == "__main__":
    app.run(debug=True)
