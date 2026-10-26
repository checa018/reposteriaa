from flask_appbuilder import ModelView, BaseView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import Categoria, Ingrediente

# --- 1. Vista personalizada para el Dashboard de Inventario ---
class DashboardView(BaseView):
    route_base = "/dashboard"

    @expose("/")
    def index(self):
        # Consultamos todos los ingredientes de la base de datos MySQL
        ingredientes = db.session.query(Ingrediente).all()
        # Renderizamos tu archivo dashboard.html con los datos reales
        return self.render_template("dashboard.html", ingredientes=ingredientes)

# Registrar el Dashboard para que aparezca primero en el menú
appbuilder.add_view_no_menu(DashboardView)
appbuilder.add_link(
    "Dashboard General",
    href="/dashboard/",
    icon="fa-gauge",
    category="Inventario",
    category_icon="fa-boxes-stacked"
)


# --- 2. Vistas de Administración (CRUD) para Categorías ---
class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)

    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripcion",
        "activo": "Activo",
        "ingredientes": "Ingredientes"
    }
    
    list_columns = ["nombre", "descripcion", "activo"]
    show_columns = ["id", "nombre", "descripcion", "activo", "ingredientes"]
    add_columns = ["nombre", "descripcion", "activo"]
    edit_columns = ["nombre", "descripcion", "activo"]
    order_columns = ["nombre"]


# --- 3. Vistas de Administración (CRUD) para Ingredientes ---
class IngredienteView(ModelView):
    datamodel = SQLAInterface(Ingrediente)

    label_columns = {
        "nombre": "Nombre",
        "categoria": "Categoria",
        "cantidad": "Cantidad",
        "unidad_medida": "Unidad de Medida",
        "costo_unitario": "Costo Unitario",
        "stock_minimo": "Stock Minimo",
        "fecha_vencimiento": "Fecha de Vencimiento",
        "activo": "Activo"
    }
    
    list_columns = [
        "nombre", "categoria", "cantidad", "unidad_medida",
        "costo_unitario", "stock_minimo", "fecha_vencimiento", "activo"
    ]

    show_columns = list_columns + ["id"]
    add_columns = list_columns
    edit_columns = add_columns
    search_columns = ["nombre"]
    order_columns = ["nombre"]


# --- Registro de Vistas en el Menú de Flask-AppBuilder ---
appbuilder.add_view(
    CategoriaView,
    "Módulo Categorías",
    icon="fa-tags",
    category="Inventario"
)
    
appbuilder.add_view(
    IngredienteView,
    "Módulo Ingredientes",
    icon="fa-cubes",
    category="Inventario"
)