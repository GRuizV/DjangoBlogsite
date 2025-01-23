# Django Blogsite

A dynamic and fully-featured blogging platform built with Django, designed to manage user-generated content efficiently. The application includes robust user authentication, post management capabilities, and responsive design. This project integrates Django's powerful backend framework with Bootstrap for modern, mobile-friendly styling.

## Features

- **User Registration and Authentication**

    * Secure user sign-up, login, and logout functionality.
    * Profile management with the ability to update profile details, including profile pictures stored securely on AWS S3.

- **Post Management**

    * Users can create, edit, and delete posts.
    * Each post is associated with the logged-in user.

- **Dynamic Homepage**
    
    * Displays all blog posts, including details like the author and publication date.

- **Pagination**
    
    * Pagination for blog posts to improve user experience.

- **Bootstrap Integration**
    
    * Responsive design with modern styling.

- **Media Storage on AWS S3**
    
    * All uploaded media files, including profile pictures, are securely stored in an AWS S3 bucket.

## Live Demo

The Django Blogsite is deployed on PythonAnywhere: [GRuizV.pythonanywhere.com](https://gruizv.pythonanywhere.com).

Visit the live demo to explore the platform's features!

## Technologies Stack

- **Backend Framework:** Django.
- **Database:** SQLite (default Django database for development).
- **Frontend:** HTML, CSS, Bootstrap.
- **Python Libraries:** 
  - Pillow (for handling user profile images).
  - boto3 (to interact with AWS S3).
  - django-storages (to enable Django-S3 integration).
- **Storage:** AWS S3 (for media files in production).
- **Version Control:** Git/GitHub.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/GRuizV/DjangoBlogsite.git
    cd DjangoBlogsite
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv blogsite_env
    source blogsite_env/bin/activate  # For Windows: blogsite_env\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

    - Create a `.env` file in the root directory with the following keys:
      ```text
      AWS_ACCESS_KEY_ID=your_aws_access_key
      AWS_SECRET_ACCESS_KEY=your_aws_secret_key
      AWS_STORAGE_BUCKET_NAME=your_bucket_name
      ```

5. **Apply migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Server**:

    ```bash
    python manage.py runserver
    ```

8. **Access the project in your browser**:

    ```
    http://127.0.0.1:8000/
    ```

## Usage

1. **Home Page**:

    * View all blog posts.
    * Navigate through pages using pagination.

2. **User Actions**:

    * Register for an account or log in.
    * Create, edit, and delete your own posts.
    * Upload or update profile pictures, which are stored in AWS S3.

3. **Admin Actions**:

    * Use the Django admin panel to manage users and posts at `/admin`.

## Future Improvements

- Add a commenting system for blog posts.
- Implement search functionality for posts.
- Enhance profile pages with additional user statistics.
- Extend deployment options: Explore other deployment platforms like AWS, Heroku, or Vercel.

## License

This project is licensed under the MIT License.

---

Feel free to copy this updated version into your project! Let me know if you want further tweaks. 🚀