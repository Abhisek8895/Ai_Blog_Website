# Ai\_Blog\_Website

A blog website that integrates generative AI to automatically create high-quality blog posts and provide brief summaries for each article.

## Features

* **AI-Powered Blog Generation**: Automatically generate blog posts using advanced AI models.
* **Article Summarization**: Provide concise summaries for each article to enhance readability.
* **User Authentication**: Secure login and registration system for users.
* **Comment System**: Allow users to comment on posts and engage with content.
* **Responsive Design**: Mobile-friendly layout for seamless browsing on all devices.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Abhisek8895/Ai_Blog_Website.git
   cd Ai_Blog_Website
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```

   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the website at `http://127.0.0.1:8000/`.

## Usage

* **Admin Panel**: Log in at `http://127.0.0.1:8000/admin/` using the superuser credentials to manage posts, comments, and users.
* **User Registration**: New users can register via the registration page and start creating or commenting on posts.
* **AI Blog Generation**: Utilize the AI integration to generate new blog posts and summaries.

## Technologies Used

* **Backend**: Django
* **Frontend**: HTML, CSS
* **AI Integration**: Gemini, Huggingface
* **Database**: SQLite
* **Authentication**: Django's built-in authentication system

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

* [Gemini](https://developers.google.com/assistant/generative-ai) and [Huggingface](https://huggingface.co/) for providing the AI models used in this project.
* [Django](https://www.djangoproject.com/) for the robust web framework.
* [Bootstrap](https://getbootstrap.com/) for the responsive front-end design.
