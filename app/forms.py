from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# cada opcion es (valor que se envia, texto que ve el usuario)
# el valor vacio sirve para la opcion "Cualquiera"
ENVIRONMENTS = [("", "Cualquiera"), ("playa", "Playa"), ("montaña", "Montaña"), ("ciudad", "Ciudad")]
ACCOMODATION_TYPES = [("", "Cualquiera"), ("hotel", "Hotel"), ("hostal", "Hostal"), ("cabaña", "Cabaña")]


class SearchForm(FlaskForm):
    class Meta:
        csrf = False

    environment = SelectField("Entorno", choices=ENVIRONMENTS)
    wo_visa = BooleanField("Solo destinos sin visado")
    submit = SubmitField("Buscar destinos")


class ComparatorForm(FlaskForm):
    class Meta:
        csrf = False

    # DataRequired obliga a escribir algo y NumberRange evita precios negativos o absurdos
    max_price = IntegerField(
        "Presupuesto máximo por noche (€)",
        validators=[
            DataRequired(message="Indica un presupuesto máximo mayor que 0"),
            NumberRange(min=1, max=10000, message="El precio debe estar entre 1 y 10000"),
        ],
    )
    accomodation_type = SelectField("Tipo de alojamiento", choices=ACCOMODATION_TYPES)
    breakfast = BooleanField("Desayuno incluido")
    pets = BooleanField("Admite mascotas")
    submit = SubmitField("Buscar alojamientos")


class AsistantForm(FlaskForm):
    class Meta:
        csrf = False

    environment = SelectField("Entorno", choices=ENVIRONMENTS)
    wo_visa = BooleanField("Solo destinos sin visado")
    accomodation_type = SelectField("Tipo de alojamiento", choices=ACCOMODATION_TYPES)
    max_price = IntegerField(
        "Gasto máximo por noche (€)",
        validators=[
            DataRequired(message="Indica un gasto máximo mayor que 0"),
            NumberRange(min=1, max=10000, message="El precio debe estar entre 1 y 10000"),
        ],
    )
    breakfast = BooleanField("Desayuno incluido")
    submit = SubmitField("Buscar mi viaje")