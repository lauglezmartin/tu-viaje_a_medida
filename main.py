from flask import Flask, render_template, request, url_for, redirect, abort

#NOTA PARA SELF, SI CARGA UNA NUEVA PAGINA O COSA CON F12, ES LADO SERVIDOR
#SI NO CARGA NADA NUEVO NI CAMBIA DE PAGINA ES LADO DE CLIENTE

#lo de arriba es cargando librerias, y, en el arriba, de producto, se especifica 
#la ruta del archivo, o sea, de donde se saca la info, y que info se saca

# Inicializamos la aplicación
app = Flask(__name__)
app.config["SECRET_KEY"] = "clave"



# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    # return """
    #     <h1>¡Hola desde Flask en Docker!!!!</h1>
    #     <p>Este es tu primer servidor Python funcionando.</p>
    # """
    return render_template ("index.html")





if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)

