# JmilkFan's Blog with Python-Flask

CSDN Blog column: JmilkFan http://blog.csdn.net/column/details/13463.html<br>

============== 2016-11-13 =============<br>
1. First commit <br>
2. Completed development environment configuration<br>
3. Created the base application<br>
4. Installed the Flask extend: Flask-Script CLI<br>
5. Installed the Flask extend: Flask-SQLAlchemy<br>
6. Connect the MySQL with SQLAlchemy

============== 2016-11-16 =============<br>
1. Created the database myblog<br>
2. Implements models class User<br>

============== 2016-11-19 =============<br>
1. Implements models class Post<br>

============== 2016-11-20 =============<br>
1. Implements models class Comment<br>
2. Implements models class Tag<br>
3. Installed the Flask extend: Flask-Migrate

============== 2016-11-23 =============<br>
1. Added the file views.py<br>
2. Created the view function for tables<br>
3. Installed the Bootstrap<br>
4. Implements the HTML base template of Jinja<br>
5. Implements the macro: render pagination<br>
6. Fix the bug from base.html

============== 2016-11-24 =============<br>
1. Implements the template for view function: `home()`<br>
2. Installed the Flask-WTF<br>
3. Implements the Form class: `CommentForm`<br>

============== 2016-11-24 =============<br>
1. Fix the bug for pagination linked<br>
2. Implements template: `post.html`<br>
3. Add the Form class CommentForm() into view function: `post()`<br>

============== 2016-11-26 =============<br>
1. Add the template: `page_not_fount.html`<br>
2. Implements the Blueprint: `blog`<br>
3. Reconstruction project code<br>

============== 2016-11-27 =============<br>
1. Using the Factory Method to create app instance<br>
2. Installed the Flask-Bcrypt<br>
3. Using the Flask-Bcrypt to encipher the password<br>
4. Using reCAPTCHA<br>
5. Implements Login and Register Forms<br>

============== 2016-11-28 =============<br>
1. Fix the bug for reCAPTCHA<br>
2. Implements view function login/logout/register<br>
3. Implements template: `login.html`<br>

============== 2016-11-29 =============<br>
1. Implements the template: `register.html`

============== 2016-11-30 =============<br>
1. Implements the View function: new_post/edit_post<br>
2. Implements the template: new.html/edit.html<br>
3. Fix the bug for edit and new the post<br>

============== 2016-12-02 =============<br>
1. Fix the bug for controller: `blog.py`<br>

============== 2016-12-03 =============<br>
1. Fix the bug for login/register/net_post/edit_post<br>

============== 2016-12-04 =============<br>
1. Installed the Flask-OpenID<br>
2. Implements use the OpenID to login the blog<br>
3. Installed the Flask-Oauth<br>
4. Implements use the Facebook and Twitter to login the blog<br>
5. Installed the Flask-Login<br>
6. Installed the Flask-Principal<br>
7. Using the session to confirm the uses login status<br>
8. Add the table: `users_roles` and `roles`<br>
9. Using the Flask-Principal to implements the role permission<br>
10. Using the Flask-Login to implements the ensure the user login status<br>

============== 2016-12-05 =============<br>
1. Fix some bug for Flask-Principal<br>

============== 2016-12-06 =============<br>
2. Add the Remember Me optional box<br>

============== 2016-12-08 =============<br>
1. Add the Script plug-in with duoshuo-comment<br>
2. Add the Script plug-in with duoshuo-share<br>

============== 2016-12-09 =============<br>
1. Fix some bug for Flask-Principal<br>
