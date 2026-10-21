from flask import Flask, render_template, abort
from data.destinations_data import obtain_destinations, search_destination_by_id, filter_destinations
from data.accomodations_data import (
    obtain_accomodations,
    search_accomodation_by_id,
    accomodations_of_destination,
    filter_accomodations,
)
from data.activities_data import (
    obtain_activities,
    search_activity_by_id,
    activities_of_destination,
)
from app.search import custom_trip
from app.forms import SearchForm, ComparatorForm, AsistantForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave"


# paginas estaticas
@app.route("/")
def home():
    # len() cuenta cuantos elementos hay, asi el resumen se actualiza solo si cambian los datos
    return render_template(
        "index.html",
        total_destinations=len(obtain_destinations()),
        total_accomodations=len(obtain_accomodations()),
        total_activities=len(obtain_activities()),
    )


@app.route("/acerca")
def about():
    return render_template("about.html")


# directorios generales
@app.route("/destinos")
def destinations():
    return render_template("destinations.html", destinations_list=obtain_destinations())


@app.route("/alojamientos")
def accomodations():
    return render_template("accomodations.html", accomodations_list=obtain_accomodations())


@app.route("/actividades")
def activities():
    # la actividad solo guarda el id del destino, pero el listado debe mostrar su nombre
    # por eso construimos una lista nueva con el nombre del destino ya buscado
    activities_list = []
    for activity in obtain_activities():
        destination = search_destination_by_id(activity["destination_id"])
        activities_list.append({
            "id": activity["id"],
            "name": activity["name"],
            "destination_name": destination["name"],
        })
    return render_template("activities.html", activities_list=activities_list)


# buscadores
@app.route("/explorador", methods=["GET", "POST"])
def search():
    form = SearchForm()
    results = None
    if form.validate_on_submit():
        results = filter_destinations(form.environment.data, form.wo_visa.data)
    return render_template("search.html", form=form, results=results)


@app.route("/comparador", methods=["GET", "POST"])
def comparator():
    form = ComparatorForm()
    results = None
    if form.validate_on_submit():
        results = filter_accomodations(
            form.max_price.data,
            form.accomodation_type.data,
            form.breakfast.data,
            form.pets.data,
        )
    return render_template("comparator.html", form=form, results=results)


@app.route("/viaje-a-medida", methods=["GET", "POST"])
def asistant():
    form = AsistantForm()
    results = None
    if form.validate_on_submit():
        results = custom_trip(
            form.environment.data,
            form.wo_visa.data,
            form.accomodation_type.data,
            form.max_price.data,
            form.breakfast.data,
        )
    return render_template("asistant.html", form=form, results=results)


# fichas de detalle
# <int:destination_id> hace que Flask solo acepte numeros, si ponen letras ya da 404 solo
@app.route("/destino/<int:destination_id>")
def destination_detail(destination_id):
    destination = search_destination_by_id(destination_id)
    if destination is None:
        abort(404)
    return render_template(
        "destiny.html",
        destination=destination,
        accomodations_list=accomodations_of_destination(destination_id),
        activities_list=activities_of_destination(destination_id),
    )


@app.route("/alojamiento/<int:accomodation_id>")
def accomodation_detail(accomodation_id):
    accomodation = search_accomodation_by_id(accomodation_id)
    if accomodation is None:
        abort(404)
    destination = search_destination_by_id(accomodation["destination_id"])
    return render_template("accomodation.html", accomodation=accomodation, destination=destination)


@app.route("/actividad/<int:activity_id>")
def activity_detail(activity_id):
    activity = search_activity_by_id(activity_id)
    if activity is None:
        abort(404)
    destination = search_destination_by_id(activity["destination_id"])
    return render_template("activity.html", activity=activity, destination=destination)


# error 404 personalizado
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # host 0.0.0.0 es necesario en Docker para que el servidor sea accesible desde fuera del contenedor
    app.run(host="0.0.0.0", port=5000, debug=True)


