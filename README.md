# API bidezko portfolio programa [EUS]

Flask erabiliz egindako Python programa, **portfolio web orri sinple bat** sortzen duena eta aldi berean **API REST bat** eskaintzen duena.
APIaren bidez informazioa kanpoko bezeroek eskura dezakete HTTP eskaeren bidez.

---

# Flask Portfolio + API Project [EN]

## Project Description

This project is a **learning exercise** developed for the subject **Industrial Informatics** at the **University of the Basque Country (EHU)**.

The project consists of a **Python backend implemented with Flask** that follows a **client–server architecture**. The server provides:

* A **web-based personal portfolio** served as HTML
* A **REST API endpoint** that exposes profile information in **JSON format**

Additionally, a separate Python script is included to **consume and verify the API**, simulating how an external client would interact with the backend.

This project is intended for **educational purposes**, focusing on understanding **web servers, APIs, HTTP requests, and backend development with Python**.

---

## Technologies Used

* **Python 3**
* **Flask** – web server and API
* **requests** – API client testing
* **HTML5** - web interface
* **Visual Studio Code** – recommended IDE

---

## Features

* Serves a personal **portfolio web page**
* Exposes a **REST API** endpoint
* Returns data in **JSON format**
* Separates server-side and client-side logic
* Simple API client for testing purposes

---

## Project Structure

```
portfolio_flask/
│
├── app.py
├── apiak_funtzionatu.py
├── templates/
│   └── portfolio.html
```

---

## File Descriptions

### `app.py`

Main file that implements the **Flask server**.
It manages the web application **routes** and exposes a **REST API** that returns profile information in **JSON format**.

---

### `portfolio.html`

Web interface of the personal portfolio served by Flask.
It displays personal and professional information in a structured and visual way.

---

### `apiak_funtzionatu.py`

**Client-side script** used to verify that the API works correctly.
It behaves like an external client by sending an HTTP request to the API and displaying the received response.

⚠️ **Important:**
The Flask server (`app.py`) must be running before executing this file.
Both scripts should be executed in **separate terminals**.

---

## Requirements

* Python 3.x
* Required Python libraries:

```bash
pip install flask requests
```

---

## Usage

### 1. Start the Flask server
⚠️ Important: The server must be running before using the API client.

```bash
python app.py
```

The server will run at:

```
http://127.0.0.1:5000
```

---

### 2. Test the API (in a different terminal)
⚠️ Precaution: Run this script in a different terminal while the Flask server is still running.

```bash
python apiak_funtzionatu.py
```

---

## Author

**Martin Maiz Negredo**

---

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for license rights and limitations.
