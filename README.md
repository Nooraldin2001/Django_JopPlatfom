# Job Finder Platform

## Overview

The **Job Finder Platform** is a web application designed to simplify the job search process. It provides a user-friendly interface for both job seekers and employers. Here's a breakdown of the project structure and functionalities:

### Features

1. **Job Listings**
   - Users can view a list of available jobs.
   - Jobs are categorized based on various criteria like job type, location, and experience level.
   - The platform supports filtering and sorting options for an enhanced user experience.

2. **Job Details**
   - Each job has a detailed view providing information about the job, the hiring company, and application details.
   - Users can find information such as the job description, location, salary range, and application deadlines.

3. **Job Search**
   - Users can search for jobs based on keywords, location, and other filters.
   - The search functionality helps users find relevant job opportunities quickly.

4. **Apply for Jobs**
   - Job seekers can apply for jobs directly through the platform.
   - The application process may include submitting a resume, cover letter, and additional details.

5. **Company Information**
   - Users can access information about hiring companies, including their name, logo, subtitle, website, and contact email.

6. **User Authentication**
   - Certain features, such as applying for jobs, require user authentication to ensure data security.

### Project Structure

The project follows a Django-based structure with several components:

- **Models**
  - `Job`: Represents a job posting with details such as title, location, company, salary, and more.
  - `Company`: Stores information about hiring companies.
  - `Category`: Represents job categories to help in organizing and filtering jobs.
  - `JobApply`: Records job applications, including the applicant's details and attached documents.

- **Views**
  - List and detail views for jobs.
  - Views for applying to jobs and submitting application details.

- **APIs**
  - RESTful APIs using Django REST Framework for job listings and details.
  - Token-based authentication for secure API access.

- **Templates**
  - HTML templates for rendering job-related pages.

- **Static Files**
  - Contains static assets such as images and CSS files.

### Technologies Used

- **Django Framework**: A high-level Python web framework for rapid development.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **django-filter**: Provides a convenient way to filter down a queryset based on parameters.
- **django-countries**: Adds support for CountryField in Django models.
- **django-summernote**: Integrates the Summernote WYSIWYG editor for rich text fields.

## How to Run the Project

1. Clone the repository.
2. Set up a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run database migrations: `python manage.py migrate`.
5. Create a superuser account: `python manage.py createsuperuser`.
6. Load initial data (optional): `python manage.py loaddata initial_data.json`.
7. Run the development server: `python manage.py runserver`.

Visit the [admin interface](http://localhost:8000/admin) to manage job listings, companies, and categories.

Explore the **Job Finder Platform** to discover, apply for, and manage job opportunities with ease!