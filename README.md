# Lighthouse
A powerful and reliable Django template for personal or business websites.

## Getting Started
### Developing Locally
First, fork this repository or clone it.
```bash
git clone https://github.com/JonathanW2018/Lighthouse.git
```
### Starting Up For the First Time
If you've just forked this repository and need to get it started up, make sure to open the project and **migrate** or run the following in the terminal.
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
This sets up the database and initiates all the models included in the project.

### Using the Included Functions of Lighthouse
Currently, Lighthouse is **very** limited in its capabilities. You can publish articles onto your page with an image, title, date, and content.

To start publishing, make sure you've created a user and have logged in. It doesn't matter if you are a superuser or a standard user. Both types of users can publish articles; there is no distinction between the two so far.

Next, go to the `/articles/create/` page to upload an article. You'll notice that there is a simple way to attach an image to the top of article. You can drag and drop or select a file from your computer manually. When you are done, click `Save` to publish the article.

**Note:** If you don't include and image, the default image banner will be applied. You can change this default image in the `Article` model.

<!-- Therefore,you -->
For now, the only other pages on the websites are the login page and the about page. You can change the about page as your wish. It is just a static webpage, so you can add whatever you want there.
