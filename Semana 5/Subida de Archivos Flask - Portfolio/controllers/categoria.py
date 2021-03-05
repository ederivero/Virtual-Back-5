# create y read y delete
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse
from models.categoria import CategoriaModel

class CategoriaController(Resource):
    serializer = reqparse.RequestParser(bundle_errors=True)
    @jwt_required()
    def post(self):
        self.serializer.add_argument(
            'cat_nombre',
            type=str,
            required=True,
            location='json',
            help='Falta el cat_nombre'
        )
        self.serializer.add_argument(
            'cat_orden',
            type=int,
            required=True,
            location='json',
            help='Falta el cat_orden'
        )
        self.serializer.add_argument(
            'cat_estado',
            type=bool,
            required=True,
            location='json',
            help='Falta el cat_estado'
        )
        data = self.serializer.parse_args()
        nuevaCategoria = CategoriaModel(data['cat_nombre'], data['cat_orden'], data['cat_estado'], current_identity['usuario_id'])
        nuevaCategoria.save()
        # hacer la creacion de una categoria usando JWT para tener el id del usuario
        return {
            'success': True,
            'content': nuevaCategoria.json(),
            'message': 'Se creo la categoria exitosamente'
        }, 201
    def get(self):
        pass
    def delete(self):
        pass