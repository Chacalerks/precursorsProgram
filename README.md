# Chemical Inventory Digitization System

## Introduction

Welcome to the Chemical Inventory Digitization System, a specialized tool designed to facilitate the management and reporting of chemical inventories across various laboratories. This system allows labs to upload their chemical inventory data through Excel files, which are then processed and stored in a MongoDB database. The main goal of this project is to simplify the tracking and visualization of chemical usage and storage, enhancing both efficiency and compliance with regulatory requirements.

## Features

- **Excel Upload Capability**: Laboratories can upload their inventory data using a standardized Excel template which is then parsed and integrated into the central database.
- **Data Visualization**: The system includes functionality to generate visual representations of the inventory data, such as usage trends, stock levels, and compliance status.
- **Checklist Dashboard**: A dashboard to monitor which labs have submitted their reports and which are pending, ensuring complete and timely data collection.
- **Secure Data Handling**: Utilizes environment variables and secured methods to handle sensitive information, ensuring that database credentials and other secrets are not exposed.

## Technology Stack

- **Python**: The primary programming language used, chosen for its ease of use and wide range of libraries.
- **MongoDB**: A NoSQL database used to store and manage inventory data efficiently.
- **Pandas**: Utilized for reading and processing Excel files.
- **Matplotlib/Seaborn**: Used for generating statistical graphics.
- **PyMongo**: To interface Python with MongoDB.
- **Python-dotenv**: For managing environment variables securely.

## Project Structure

- `/src`: Contains all the source code for the application.
- `/data`: Where data files used for testing and development are stored (not included in the repository).
- `/docs`: Documentation related to the project, including setup guides and usage instructions.
- `README.md`: Provides an overview of the project, setup instructions, and other necessary information to get started.

## Getting Started

This section will include instructions on how to set up and run the project locally, including installing dependencies, setting up the MongoDB database, and running the application.

## Contributions

Contributions are welcome! If you're interested in improving the Chemical Inventory Digitization System, please read through our contributing guidelines. All contributions must adhere to the project's code of conduct.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or issues related to the system, please open an issue on GitHub or contact the project maintainers directly via [insert contact method].

---

For more detailed information about each component and feature, please refer to the individual documentation and comments within the codebase.

