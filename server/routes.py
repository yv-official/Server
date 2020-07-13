from server.api import api, register, login, logoutAccess, logoutRefresh, tokenRefresh

#auth routes
api.add_url_rule('/register', methods=['POST'], view_func=register)
api.add_url_rule('/login', methods=['POST'], view_func=login)
api.add_url_rule('/logout/access', methods=['POST'], view_func=logoutAccess)
api.add_url_rule('/logout/refresh', methods=['POST'], view_func=logoutRefresh)
api.add_url_rule('/token/refresh', methods=['POST'], view_func=tokenRefresh )


#user action routes
# api.add_url_rule('/feeds', methods=['GET'], view_func=feeds)


