# 🚀 API Testing Portfolio: Restful Booker

**Tester:** Samukelo Cele
**Tools Used:** Postman, JavaScript (Postman Assertions)

## 📝 Project Overview
This repository contains a Postman test suite for the **Restful Booker API** (a public practice API for hotel bookings). The goal of this project was to demonstrate manual API testing skills, validate HTTP methods, and write automated assertions using Postman's scripting engine.

## 📂 Repository Contents
*   `Postman/Restful Booker API Suite.postman_collection.json`: The exported Postman Collection containing all requests and test scripts.
*   `Postman/Postman_Run_Results.png`: Screenshot of the collection runner executing successfully.

## 🧪 Test Coverage
The suite covers the following API operations:
1.  **POST /booking:** Creates a new booking and validates that the response returns a `200 OK`, generates a unique `bookingid`, and returns the correct input data.
2.  **GET /booking/{id}:** Retrieves an existing booking and asserts the status code is `200` and the data matches the created booking.

## 💡 Key Assertions Implemented
*   **Status Code Validation:** Ensures successful requests return 2xx codes.
*   **Response Time Validation:** Ensures the API responds within a reasonable time (under 2000ms).
*   **Data Integrity:** Checks that the JSON body contains the correct keys and values.

## 📸 Test Execution Evidence
Below is a screenshot of the Collection Runner executing the full suite. All 8 assertions passed successfully.

![Postman Run Results](./Postman/Postman_Run_Results.png)

## 🚀 How to Run This Collection
1.  Download and install [Postman](https://www.postman.com/downloads/).
2.  Download the `.json` file from the `Postman` folder in this repository.
3.  Open Postman, click **Import**, and select the downloaded JSON file.
4.  You can now run the requests individually, or click **Run** to execute the entire suite automatically.
