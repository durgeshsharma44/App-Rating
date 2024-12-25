
# # accounts/routers.py
# class AuthRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'accounts':
#             if model.__name__ == 'Admin':
#                 return 'admin_db'
#             return 'default'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'accounts':
#             if model.__name__ == 'Admin':
#                 return 'admin_db'
#             return 'default'
#         return None


class AuthRouter:
    """
    A router to control database operations for different models in the accounts app.
    Routes:
      - User models -> user_db
      - Admin models -> admin_db
    """
    
    def db_for_read(self, model, **hints):
        """
        Directs read operations to the appropriate database.
        """
        if model._meta.app_label == 'accounts':
            if model.__name__ == 'Admin':
                return 'admin_db'
            if model.__name__ == 'User':
                return 'user_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Directs write operations to the appropriate database.
        """
        if model._meta.app_label == 'accounts':
            if model.__name__ == 'Admin':
                return 'admin_db'
            if model.__name__ == 'User':
                return 'user_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations between objects if they are in the same database.
        """
        if obj1._state.db in ('admin_db', 'user_db') and obj2._state.db in ('admin_db', 'user_db'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that migration operations are applied to the correct database.
        """
        if app_label == 'accounts':
            if model_name == 'admin':
                return db == 'admin_db'
            if model_name == 'user':
                return db == 'user_db'
        return None
