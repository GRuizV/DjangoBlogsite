# Django Blogsite

A dynamic and fully-featured blogging platform built with Django, designed to manage user-generated content efficiently. The application includes robust user authentication, post management capabilities, and responsive design. This project aims for the integration of Django's powerful backend framework with Bootstrap for modern, mobile-friendly styling.

## Features

- **User Registration and Authentication**

    * Secure user sign-up, login, and logout functionality.
    * Profile management with the ability to update profile details.


- **Post Management**

    * Users can create, edit, and delete posts.
    * Each post is associated with the logged-in user.


- **Dynamic Homepage**
    
    * Displays all blog posts, including details like the author and publication date.


- **Pagination**
    
    * Pagination for blog posts to improve user experience.


- **Bootstrap Integration**
    
    * Responsive design with modern styling.



## Technologies Stack

- **Backend Framework:** Django.
- **Backend Framework:** SQLite (default Django database for development).
- **Frontend:** HTML, CSS, Bootstrap.
- **Python Libraries:** Pillow (for handling user profile images).
- **Version Control:** Git/GitHub.


### Installation

1. **Clone the Repository:**

   ```
    git clone https://github.com/GRuizV/DjangoBlogsite.git
    cd DjangoBlogsite
2. **Set up a virtual environment:**

    ```
    python -m venv blogsite_env
    source blogsite_env/bin/activate   # For Windows: blogsite_env\Scripts\activate
3. **Install Dependencies**:

    ```
    pip install -r requirements.txt
4. **Apply migrations**:

    ```
    python manage.py makemigrations
    python manage.py migrate    
5. **Create a superuser**:

    ```
    python manage.py createsuperuser    
6. **Create a superuser**:

    ```
    python manage.py runserver    
7. **Access the project in your browser**:

    ```
    http://127.0.0.1:8000/


## Usage

1. **Home Page**:

    * View all blog posts.
    * Navigate through pages using pagination.

2. **User Actions**:

    * Register for an account or log in.
    * Create, edit, and delete your own posts.

3. **Admin Actions**:

    * Use the Django admin panel to manage users and posts at /admin.



## Future Improvements

- Add a commenting system for blog posts.
- Implement search functionality for posts.
- Enhance profile pages with additional user statistics.
- Deploy the project to a live server (e.g., Heroku, AWS, or Vercel).


## License

This project is licensed under the MIT License.

_Feel free to adjust the content based on your specific implementation and requirements. Add more details or instructions as needed, especially in the sections on setting up environment variables, running the application, and any unique features your chatbot offers._