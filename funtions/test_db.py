from help_fun import create_user, login_user


cs = create_user(username="admin", email="admin@admin.com", password="admin")

lu = login_user(username="admin", password="admin")

print(f"{cs} // {lu}")
