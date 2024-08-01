# ReRead - Secondhand Book Marketplace

Welcome to ReRead, a comprehensive marketplace for secondhand books. Whether you're looking to buy, sell, or swap used books, ReRead provides an easy-to-use platform to connect book lovers and foster a sustainable book trade community.

## Features

- **Browse and Search**: Explore a wide range of categories and find books by title, author, or ISBN.
- **User Authentication**: Secure user registration and login system.
- **Multilingual Support**: Available in multiple languages to cater to a diverse user base.
- **Sell Books**: Easily list books for sale, including details like condition, cover type, and language.
- **Swap Books**: Offer books for trade with other users.
- **Conversations**: Built-in messaging system to facilitate communication between buyers and sellers.
- **Admin Panel**: Manage users, categories, items, and orders with an intuitive admin interface.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/)
- **Database**: SQLite3
- **Internationalization**: [Django Rosetta](https://django-rosetta.readthedocs.io/)

## Installation

### Prerequisites

- Python 3.9 or higher
- Pip (Python package installer)
- Virtualenv (recommended)

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/reread.git
    cd reread
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.
    Admin panel: `http://127.0.0.1:8000/admin`
    Translate panel: `http://127.0.0.1:8000/rosetta`

## Usage

1. **Register an account**: Sign up to start using the marketplace.
2. **List a book**: Go to the "Sell" section and fill out the form to list your book.
3. **Search for books**: Use the search bar or browse through categories to find books you want.
4. **Initiate a conversation**: Contact sellers through the built-in messaging system to ask questions or negotiate.
5. **Purchase or swap**: Finalize deals by purchasing or swapping books with other users.
6. **Manage your listings**: Keep track of your active listings and mark books as sold or swapped when deals are completed.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact us at [lyarov22@gmail.com] or t.me/lyarov22.

---

Thank you for using ReRead. Happy reading!
