CREATE DATABASE salon;

USE salon;

-- Table for storing customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100),
  password VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing stylists
CREATE TABLE stylists (
  stylist_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(8, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing bookings
CREATE TABLE bookings (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT NOT NULL,
  stylist_id INT NOT NULL,
  service_id INT NOT NULL,
  booking_date DATETIME NOT NULL,
  duration INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (stylist_id) REFERENCES stylists(stylist_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Table for storing bookings' services
-- CREATE TABLE booking_services (
--   booking_id INT NOT NULL,
--   service_id INT NOT NULL,
--   PRIMARY KEY (booking_id, service_id),
--   FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
--   FOREIGN KEY (service_id) REFERENCES services(service_id)
-- );
