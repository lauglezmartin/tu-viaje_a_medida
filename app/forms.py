from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


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





