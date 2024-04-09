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

@app.route('/indexA')
def iniciA():
    return render_template("indexA.html")

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

@app.route('/signC')
def sC():
    return render_template("signupC.html")

@app.route('/sign')
def s():
    return render_template("sign.html")

#Navegador Cliente
@app.route('/comentarios')
def comentC():
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

@app.route('/pedidosA')
def pA():
    return render_template("pedidosA.html")

@app.route('/comentA')
def comentA():
    return render_template("comentA.html")

@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

@app.route('/comentarios')
def comentarios():
    return render_template('comentarios.html')

@app.route('/carrito')
def carrito():
    return render_template('tablas.html')
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
            -- Table `db_OAGR`.`adminis`
            -- -----------------------------------------------------
            CREATE TABLE IF NOT EXISTS `db_OAGR`.`adminis` (
            `id` INT PRIMARY KEY AUTO_INCREMENT,
            `nombre` VARCHAR(100) NOT NULL,
            `correo` VARCHAR(100) NOT NULL,
            `contra` VARCHAR(50) NOT NULL);
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
            insert into adminis(nombre, correo, contra) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');

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

            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Maki', 'Sushi', 'maki.png', '345', '80');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Nigiri', 'Sushi', 'nigiri.png', '564', '75');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Temaki', 'Sushi', 'temaki.png', '546', '50');
            insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Uramaki', 'Sushi', 'uramaki.png', '265', '82');

            insert into cliente (nombre, correo, contra, direccion, telefono) values ('alid',	'probanding@gmail.com',	'sepa si quedo bien',	'9878989034 5345',	'4494359680');
            insert into cliente (nombre, correo, contra, direccion, telefono) values ('val', 'dkwoen@hotmail.com', 'ey eso', 'ttyfyjugb', '4495699410');
            insert into reservas (id_cliente, hora, dia, nperson, mesa) values ('1', '10:00', '2024-04-17', '3', '5');
            insert into comentarios (id_cliente, razon, mensaje) values ('1', 'prueba2', 'mensaje	');
            insert into comentarios (id_cliente, razon, mensaje) values ('1', 'prueba', 'solo estoy probando que guarde mis comentarios');
            insert into comentarios (id_cliente, razon, mensaje) values ('2', 'jala o no', 'me avente todo el disenio, falta la funcion');
            insert into pedidos (id_cliente, id_producto, cantidad, total) values ('1', '1', '3', '60');
        """
        statements = [stmt.strip() for stmt in sql_statements.split(';') if stmt.strip()]


        # Execute each SQL statement
        for statement in statements:
            cursor.execute(statement)
            conn.commit()


        print("Base de datos y tablas creadas exitosamente")
        conn.close()

@app.route('/inicioA', methods=['POST'])
def iniciar():
    if request.method == 'POST':
        aux_Nom = request.form['nombre']
        aux_Contra = request.form['contra']
        conex()
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR' )
        cursor = conn.cursor()
        cursor.execute('select nombre, correo, contra from adminis where nombre = %s and contra=%s', (aux_Nom, aux_Contra))
        resultado = cursor.fetchone()
        if resultado:
            print("Bien")
            return redirect(url_for('iniciA'))
        else:
            print("mal")
            datos =cursor.fetchall()
            return render_template("Alogin.html", Admin = datos)

@app.route('/inicioC', methods=['POST'])
def iniciaC():
    if request.method == 'POST':
        aux_Nom = request.form['nombre']
        aux_Contra = request.form['contra']
        conex()
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR' )
        cursor = conn.cursor()
        cursor.execute('select nombre, correo, contra from cliente where nombre = %s and contra=%s', (aux_Nom, aux_Contra))
        resultado = cursor.fetchone()
        if resultado:
            print("Bien")
            return redirect(url_for('inicio'))
        else:
            print("mal")
            datos =cursor.fetchall()
            return render_template("login.html", Client =datos)

@app.route('/agrega_admin', methods=['POST'])
def agrega_admin():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        conex()
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into adminis (nombre,correo,contra) values (%s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra))
        conn.commit()
        return redirect(url_for('oL'))

# Tabla registros adminis, editar y borrar
@app.route('/crudAdmin')
def crudAdmin():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from adminis')
    datos = cursor.fetchall()
    return render_template("crudAdmin.html", Admin = datos)

@app.route('/editAdmin/<string:id>')
def editAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, nombre, correo, contra from adminis where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editAdmin.html", Ad=dato[0])

@app.route('/editar_admin/<string:id>',methods=['POST'])
def editar_admin(id):
    if request.method == 'POST':
        nom=request.form['nombre']
        corr=request.form['correo']
        contra=request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update adminis set nombre=%s, correo=%s, contra=%s where id=%s', (nom,corr,contra,id))
        conn.commit()
    return redirect(url_for('crudAdmin'))

@app.route('/borrarAd/<string:id>')
def borrarAdmin(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from adminis where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudAdmin'))


# Tabla registros cliente, editar y borrar
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
        conex()
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into cliente (nombre,correo,contra,direccion,telefono) values (%s, %s, %s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra, aux_Direccion, aux_Telefono))
        conn.commit()
    return redirect(url_for('crudClient'))

@app.route('/reg_cliente', methods=['POST'])
def registro_cliente():
    if request.method == 'POST':
        aux_Nombre = request.form['nombre']
        aux_Correo = request.form['correo']
        aux_Contra = request.form['contra']
        aux_Direccion = request.form['direccion']
        aux_Telefono = request.form['telefono']
        conex()
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('insert into cliente (nombre,correo,contra,direccion,telefono) values (%s, %s, %s, %s, %s)',(aux_Nombre, aux_Correo, aux_Contra, aux_Direccion, aux_Telefono))
        conn.commit()
    return redirect(url_for('oL'))

# Tabla registros almacen, editar y borrar
@app.route('/crudAlmacen')
def crudAlmacen():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select id, producto, descripcion, imagen, cantidad, precio from almacen order by id')
    datos = cursor.fetchall()
    return render_template("crudAlmacen.html", comentarios = datos)

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
        pro=request.form['product']
        des=request.form['descrip']
        img=request.form['img']
        cant=request.form['cant']
        pre=request.form['precio']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('update almacen set producto=%s, descripcion=%s, imagen=%s, cantidad=%s, precio=%s where id=%s', (pro,des,img,cant,pre,id))
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

# tabla registros pedidos, editar y borrar
@app.route('/crudPedidosA')
def crudPedidoA():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select p.id, c.nombre, a.producto, p.cantidad, p.total from pedidos p join cliente c on p.id_cliente = c.id join almacen a on a.id = p.id_producto')
    datos = cursor.fetchall()
    return render_template("crudPedidosA.html", comentarios = datos)

@app.route('/editPedidosA/<string:id>')
def editPedidosA(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select p.id, c.nombre, a.producto, p.cantidad, p.total from pedidos p join cliente c on p.id_cliente = c.id join almacen a on a.id = p.id_producto and p.id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editPedidosA.html", comentar=dato[0])

# Incolpeto
@app.route('/editar_pedidos/<string:id>',methods=['POST'])
def editar_pedidos(id):
    if request.method == 'POST':
        cli=request.form['nombre']
        pro=request.form['prod']
        cant=int(request.form['cant'])
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (cli,))
        id_c = cursor.fetchone()[0]
        cursor.execute('select id, precio, cantidad from almacen where producto = %s', (pro,))
        id_p, precio, a_c = cursor.fetchone()
        p = int(precio)
        tot = cant * p
        menos = a_c - cant
        cursor.execute('update almacen set cantidad=%s where id=%s', (menos, id_p))
        cursor.execute('update pedidos set id_cliente=%s, id_producto=%s, cantidad=%s, total=%s where id=%s', (id_c, id_p, cant, tot, id))
        conn.commit()
    return redirect(url_for('crudPedidoA'))

@app.route('/borrarPedA/<string:id>')
def borrarPedA(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from pedidos where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudPedidosA'))

@app.route('/agrega_pedidos', methods=['POST'])
def agrega_pedidos():
    if request.method == 'POST':
        n = request.form['nombre']
        p = request.form['prod']
        c = request.form['cant']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (n))
        id_c = cursor.fetchall()
        cursor.execute('select id, precio, cantidad from almacen where producto = %s', (p))
        id_p, precio, a_c = cursor.fetchone()
        p = int(precio)
        c= int(c)
        tot = c * p
        menos = a_c - c
        cursor.execute('update almacen set cantidad=%s where id=%s', (menos, id_p))
        cursor.execute('insert into pedidos (id_cliente,id_producto,cantidad,total) values (%s, %s, %s,%s)',(id_c,id_p,c,tot))
        conn.commit()
    return redirect(url_for('agrega_pedidos'))

@app.route('/reg_pedidos', methods=['POST'])
def reg_pedidos():
    if request.method == 'POST':
        n = request.form['nombre']
        p = request.form['prod']
        c = request.form['cant']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (n))
        id_c = cursor.fetchall()
        cursor.execute('select id, precio, cantidad from almacen where producto = %s', (p))
        id_p, precio, a_c = cursor.fetchone()
        p = int(precio)
        c= int(c)
        tot = c * p
        menos = a_c - c
        cursor.execute('update almacen set cantidad=%s where id=%s', (menos, id_p))
        cursor.execute('insert into pedidos (id_cliente,id_producto,cantidad,total) values (%s, %s, %s,%s)',(id_c,id_p,c,tot))
        conn.commit()
    return redirect(url_for('inicio'))

#tabla registros reservaciones, editar y borrar
@app.route('/crudReservaA')
def crudReservaA():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select r.id, c.nombre, r.hora, r.dia, r.nperson, r.mesa from reservas r join cliente c on r.id_cliente = c.id')
    datos = cursor.fetchall()
    return render_template("crudRes.html", reservaciones = datos)

@app.route('/editRes/<string:id>')
def editResA(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select r.id, c.nombre, r.hora, r.dia, r.nperson, r.mesa from reservas r join cliente c on c.id= r.id_cliente and r.id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editRes.html", reserva=dato[0])

@app.route('/editar_reservas/<string:id>',methods=['POST'])
def editar_reserva(id):
    if request.method == 'POST':
        cli=request.form['id_cliente']
        h=request.form['hora']
        d=request.form['dia']
        np=request.form['nperson']
        m=request.form['mesa']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (cli))
        id_c = cursor.fetchall()
        cursor.execute('update reservas set id_cliente=%s, hora=%s, dia=%s, nperson=%s, mesa=%s where id=%s', (id_c, h, d, np, m, id))
        conn.commit()
    return redirect(url_for('crudReservaA'))

@app.route('/borrarRes/<string:id>')
def borrarResA(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from reservas where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudRes'))

@app.route('/agrega_reservas', methods=['POST'])
def agrega_res():
    if request.method == 'POST':
        cli=request.form['id_cliente']
        h=request.form['hora']
        d=request.form['dia']
        np=request.form['nperson']
        m=request.form['mesa']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (cli))
        id = cursor.fetchall()
        cursor.execute('insert into reservas (id_cliente, hora, dia, nperson, mesa) values (%s, %s, %s,%s, %s)',(id, h, d, np, m))
        conn.commit()
        datos = cursor.fetchall()
    return redirect(url_for('crudReservaA'))

@app.route('/reg_reservas', methods=['POST'])
def reg_res():
    if request.method == 'POST':
        cli=request.form['id_cliente']
        h=request.form['hora']
        d=request.form['dia']
        np=request.form['nperson']
        m=request.form['mesa']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (cli))
        id = cursor.fetchall()
        cursor.execute('insert into reservas (id_cliente, hora, dia, nperson, mesa) values (%s, %s, %s,%s, %s)',(id, h, d, np, m))
        conn.commit()
        datos = cursor.fetchall()
    return redirect(url_for('inicio'))

# tabla de registros comentarios, editar y borrar
@app.route('/crudComent')
def crudComA():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select co.id, c.nombre, co.razon, co.mensaje from comentarios co join cliente c on c.id = co.id_cliente')
    datos = cursor.fetchall()
    return render_template("crudComent.html", comentarios = datos)

@app.route('/editComent/<string:id>')
def editcoment(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('select co.id, c.nombre, co.razon, co.mensaje from comentarios co join cliente c on c.id = co.id_cliente and co.id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editComent.html", comenta=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        n=request.form['nombre']
        r=request.form['razon']
        m=request.form['mensaje']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (n))
        id_c = cursor.fetchall()
        cursor.execute('update comentarios set id_cliente=%s, razon=%s, mensaje=%s where id=%s', (id_c, r, m, id))
        conn.commit()
    return redirect(url_for('crudComA'))

@app.route('/borrarComent/<string:id>')
def borraComa(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
    cursor = conn.cursor()
    cursor.execute('delete from comentarios where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crudComent'))

@app.route('/agrega_comenta', methods=['POST'])
def agrega_com():
    if request.method == 'POST':
        n=request.form['nombre']
        r=request.form['razon']
        m=request.form['mensaje']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (n))
        id = cursor.fetchall()
        cursor.execute('insert into comentarios (id_cliente, razon, mensaje) values (%s, %s, %s)',(id, r, m))
        conn.commit()
        datos = cursor.fetchall()
    return redirect(url_for('crudComA'))

@app.route('/reg_comenta', methods=['POST'])
def reg_com():
    if request.method == 'POST':
        n=request.form['nombre']
        r=request.form['razon']
        m=request.form['mensaje']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_OAGR')
        cursor = conn.cursor()
        cursor.execute('select id from cliente where nombre = %s', (n))
        id = cursor.fetchall()
        cursor.execute('insert into comentarios (id_cliente, razon, mensaje) values (%s, %s, %s)',(id, r, m))
        conn.commit()
        datos = cursor.fetchall()
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)
