from server.api import (
    api, 
    register, 
    login, 
    logout, 
    tokenRefresh,
    updateDetails
)

#auth routes
api.add_url_rule('/register', methods=['POST'], view_func=register)
api.add_url_rule('/login', methods=['POST'], view_func=login)
api.add_url_rule('/token/remove', methods=['GET'], view_func=logout)
api.add_url_rule('/token/refresh', methods=['GET'], view_func=tokenRefresh )


# user action routes
api.add_url_rule('user/edit', methods=['POST'], view_func=updateDetails)
# api.add_url_rule('/feeds', methods=['GET'], view_func=feeds)


