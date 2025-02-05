# JobFlow

JobFlow is an intelligent job application management tool designed to streamline your job search process. This web-based application helps you keep track of your job applications, analyze job listings, and generate customized CVs and cover letters tailored to each job opportunity.

## Overview

JobFlow provides:
- **Job Application Dashboard**: View and update the status of your job applications.
- **Job Listing Input**: Manually input or paste job listing text (with future plans for URL-based extraction).
- **NLP-Powered Analysis**: Extract core job requirements and cross-reference them against your CV.
- **CV Generation**: Customize a standardized CV template (DOCX) and convert it to PDF after finalization.
- **Cover Letter Generation**: Generate tailored cover letters using the OpenAI API, ensuring they follow predefined templates.
- **Color-Coded Tech Stacks**: Easily navigate and identify job categories and technologies (e.g., Django as a substack of Python) via a color system.
- **Robust Error Handling**: Ensure stability with tight wrappers around external API calls (such as the OpenAI API).
- **Data Persistence**: Long-term storage with SQLite, and JSON for interim data processing.

## Technology Stack

- **Frontend**: Flask (web-based interface)
- **Backend**: Python, Flask, Requests, BeautifulSoup (for future extraction), etc.
- **Database**: SQLite for persistent storage
- **NLP & Data Extraction**: spaCy or NLTK (planned)
- **Document Generation**: python-docx (for DOCX creation) and ReportLab (for PDF conversion)
- **External API**: OpenAI API for cover letter generation

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/JobFlow.git
    ```

2. **Navigate to the project directory and set up a virtual environment:**
    ```bash
    cd JobFlow
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Set up your OpenAI API key (and any other required keys) by exporting them in your shell:
    ```bash
    export OPENAI_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    flask run
    ```

2. **Open your browser:**
    Navigate to `http://127.0.0.1:5000` to access the application dashboard.

3. **Manage your Job Applications:**
    - Input job listing text manually.
    - Track the status of your applications.
    - Generate and customize your CV and cover letters.

## TODO List

- [ ] **Initial Setup & Data Model**
  - Define data structures for Job Applications, CV, Cover Letter, and Application Status.
  - Set up SQLite for persistent data storage.
  - Establish a JSON pipeline for interim data processing.

- [ ] **Web-based Interface (Flask)**
  - Set up the Flask framework for a browser-based interface.
  - Implement a dashboard for tracking job applications.
  - Develop forms for manually inputting job listing text.

- [ ] **Job Listing Extraction Module**
  - Implement text-based job listing input.
  - Plan and design URL-based extraction functionality (to be added later).
  - Standardize job data into a JSON format.

- [ ] **NLP Module for Requirement Extraction**
  - Integrate NLP libraries (spaCy/NLTK) to extract core job requirements.
  - Develop logic to cross-reference job requirements with CV data.

- [ ] **CV Generation Module**
  - Create a standardized CV template in DOCX format.
  - Implement conversion from DOCX to PDF once the CV is finalized.
  - Integrate a color-coded system to visually represent technology stacks.

- [ ] **Cover Letter Generation Module**
  - Integrate the OpenAI API for generating tailored cover letters.
  - Build robust wrappers around the API to handle errors and unexpected responses.
  - Enforce template-based output for consistent cover letter formats.

- [ ] **Additional Features**
  - Implement job status tracking updates (e.g., applied, interviewing, offer, rejected).
  - Develop a template management interface for both CV and cover letter templates.
  - Build a skill gap analysis functionality.
  - **Future Enhancements (shelved for now):**
    - Integration with job portals.
    - Calendar API integrations.
    - User authentication and cloud sync.
    - Mobile-friendly or cross-platform versions.

- [ ] **Testing & Documentation**
  - Write unit tests for all modules.
  - Continuously update documentation as new features are added.

- [ ] **Deployment**
  - Prepare the application for deployment on a web server.
  - Ensure scalability and security.

## Contributing

Contributions are welcome! Please fork the repository, create your feature branch, and submit a pull request with clear descriptions of your changes. Be sure to write tests for any new features or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

---
