from pecan import hooks


# class DBHook(hooks.PecanHook):
#     """Create a db connection instance."""
# 
#     def before(self, state):
#         """Excute the DBHook.before() before handle the restful request."""
#         state.request.db_conn = db_api.get_session()
