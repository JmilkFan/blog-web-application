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

============== 2016-12-10 =============<br>
1. Installed the Flask-Restful<br>
2. Implements restful api `GET` for /api/posts<br>
3. Implements restful api `POST` for /api/posts<br>
4. Implements restful api `PUT` for /api/posts/post_id<br>
5. Implements restful api `DELETE` for /api/posts/post_id<br>
6. Implements restful api `POST` for /api/auth<br>

============== 2016-12-11 =============<br>
1. Added the database migrate version: `Init database`<br>
2. Added the table `browse_volumes`<br>
3. Added the database migrate version: `Add table of browse_volumes`<br>
4. Fix some bug<br>
5. Installed Celery and Flask-Celery-Helper<br>

============== 2016-12-12 =============<br>
1. Implements the celery_runner(Celery worker)<br>

============== 2016-12-13 =============<br>
1. Installed flower<br>
2. Setup the timed task<br>
3. Add table `reminders`<br>
4. Implements Remind when registered the user<br>
5. Implements weekly digest<br>

============== 2016-12-14 =============<br>
1. Implements email content of weekly-digest `digest.html`<br>
2. Installed Flask-Debug-Toolbar<br>
3. Installed Flask-Cache<br>
4. Installed Flask-Redis<br>
5. Implements make cache for `post.html/home.html` and function `verify_auth_token`<br>
6. Using Redis as BackEndStieCache<br>
7. Installed Flask-Assets<br>
8. Installed Flask-Admin<br>
9. Implements the Post-Admin page via Flask-Admin<br>
10. Implements access File System via Flask-Admin<br>
11. Installed Flask-Mail<br>

============== 2016-12-15 =============<br>
1. Fix some bug<br>

============== 2016-12-16 =============<br>
1. Fix some bug<br>

============== 2016-12-17 =============<br>
1. Fix some bug for Flask-Admin<br>
2. Replace the property of Post Model: `users` to `user`<br>

============== 2016-12-18 =============<br>
1. Create a new manager command `assset`<br>
2. Pack up the static file<br>
3. Fix the bug for UnicodeEncodeError<br>

============== 2016-12-19 =============<br>
1. Implements Flask-Youku extension<br>
2. Implements Flask-GZip extension<br>

============== 2016-12-20 =============<br>
1. Packup the extensions Flask-Youku and Flask-GZip<br>

============== 2016-12-21 =============<br>
1. Installed selenium<br>
2. Installed coverage<br>
3. Implements Unit test `TestURLs`<br>
4. Fix some bug<br>

============== 2016-12-24 =============<br>
1. Fix some bug for flask_youku<br>
2. Installed oslo_config<br>
3. Using oslo_config to setup the config<br>


============== tag 0.0.1 Done to Python-Flask =============<br>


============== 2016-12-26 =============<br>
1. Fix the bug for oslo_config<br>
2. Implements setup.cfg and setup.py<br>
3. Tag 0.0.1 Done to Python-Flask<br>
4. Source archive v0.0.1<br>

============== 2016-12-27 =============<br>
1. Installed Pecan<br>
2. Implements Restful api `v1/users` via Pecan<br>
3. Create the db directory<br>
4. Create the api directory for Pecan RESTful API<br>

============== 2016-12-28 =============<br>
1. Implements RESTful API `v1/posts` via Pecan<br>

============== 2016-12-30 =============<br>
1. Installed oslo_db<br>
2. Using oslo_db.sqlalchemy.session.EngineFacahe to create the session<br>
3. Using oslo_db.concurrency to wrapper the operation of database<br>

============== 2017-01-02 =============<br>
1. Fix the bug for Flask-Admin<br>
2. Return post_id when response the flask_restful api `/posts` GET<br>

============== 2017-01-04 =============<br>
1. Implements the GET `v1/posts` via pecan RESTful<br>

============== 2017-01-05 =============<br>
1. Installed oslo_i18n<br>
2. Try to use the oslo_log and oslo_config<br>

============== 2017-01-08 =============<br>
1. Fix some bug<br>
2. Implements console-script via setup.cfg<br>

============== 2017-01-09 =============<br>
1. Fix the bug for db.api.CONF<br>
