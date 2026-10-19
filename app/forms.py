from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# cada opcion es (valor que se envia, texto que ve el usuario)
# el valor vacio sirve para la opcion "Cualquiera"
ENTORNOS = [("", "Cualquiera"), ("playa", "Playa"), ("montaña", "Montaña"), ("ciudad", "Ciudad")]
TIPOS = [("", "Cualquiera"), ("hotel", "Hotel"), ("hostal", "Hostal"), ("cabaña", "Cabaña")]


class ExploradorForm(FlaskForm):
    class Meta:
        csrf = False

    entorno = SelectField("Entorno", choices=ENTORNOS)
    sin_visado = BooleanField("Solo destinos sin visado")
    submit = SubmitField("Buscar destinos")


class ComparadorForm(FlaskForm):
    class Meta:
        csrf = False

    # DataRequired obliga a escribir algo y NumberRange evita precios negativos o absurdos
    precio_max = IntegerField(
        "Presupuesto máximo por noche (€)",
        validators=[
            DataRequired(message="Indica un presupuesto máximo"),
            NumberRange(min=1, max=10000, message="El precio debe estar entre 1 y 10000"),
        ],
    )
    tipo = SelectField("Tipo de alojamiento", choices=TIPOS)
    desayuno = BooleanField("Desayuno incluido")
    mascotas = BooleanField("Admite mascotas")
    submit = SubmitField("Buscar alojamientos")


class AsistenteForm(FlaskForm):
    class Meta:
        csrf = False

    entorno = SelectField("Entorno", choices=ENTORNOS)
    sin_visado = BooleanField("Solo destinos sin visado")
    tipo = SelectField("Tipo de alojamiento", choices=TIPOS)
    precio_max = IntegerField(
        "Gasto máximo por noche (€)",
        validators=[
            DataRequired(message="Indica un gasto máximo"),
            NumberRange(min=1, max=10000, message="El precio debe estar entre 1 y 10000"),
        ],
    )
    desayuno = BooleanField("Desayuno incluido")
    submit = SubmitField("Buscar mi viaje")