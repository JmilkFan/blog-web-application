# from pecan import hooks
# 
# from jmilkfansblog.db.sqlalchemy import api as db_api
# 
# class DBHook(hooks.PecanHook):
#     """Create a db connection instance."""
# 
#     def before(self, state):
#         """Excute the DBHook.before() before handle the restful request."""
#         state.request.db_conn = db_api.get_session()
