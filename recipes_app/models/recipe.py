from werkzeug.utils import redirect
from recipes_app import app
from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(user_id)s, %(created_on)s, NOW())"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_recipes_by_user(cls, data):
        query = "SELECT * from recipes WHERE user_id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, user_id = %(user_id)s, created_at = %(created_at)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE user_id = %(user_id)s AND id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)