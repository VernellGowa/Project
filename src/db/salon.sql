-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 25 nov. 2023 à 13:25
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `salon`
--

-- --------------------------------------------------------

--
-- Structure de la table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `stylist_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `booking_date` datetime NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL,
  `cancelled_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `bookings`
--

INSERT INTO `bookings` (`id`, `customer_id`, `stylist_id`, `service_id`, `booking_date`, `created_at`, `updated_at`, `cancelled_at`) VALUES
(4, 9, 5, 1, '2023-11-22 03:59:00', '2023-11-21 16:01:34', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `gender` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `customers`
--

INSERT INTO `customers` (`id`, `first_name`, `last_name`, `phone_number`, `email`, `password`, `created_at`, `gender`) VALUES
(9, 'vernell', 'gowa', '07391044471', 'test@gmail.com', 'pass', '2023-11-12 20:53:16', 'Male');

-- --------------------------------------------------------

--
-- Structure de la table `likes`
--

CREATE TABLE `likes` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `duration` int(11) NOT NULL,
  `image` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `services`
--

INSERT INTO `services` (`id`, `name`, `description`, `price`, `created_at`, `duration`, `image`) VALUES
(1, 'Buzz Cut', 'Have you lookin Nice \'n\' Fresh. Fine boy!!!!!!!!!!!!!!!!!', 10.00, '2023-11-12 20:48:54', 20, 'image.png'),
(2, 'Wash', 'Have you feelin super fresh', 25.50, '2023-11-12 20:49:45', 30, 'image.png'),
(3, 'High Top', 'Have you lookin like prime Will Smith', 12.50, '2023-11-12 20:50:59', 35, 'image.png'),
(4, 'Blowout', 'Styling hair with blow dryer', 30.00, '2023-11-19 19:43:00', 45, 'image.png'),
(5, 'Hair Coloring', 'Various hair coloring services', 50.00, '2023-11-19 19:43:00', 60, 'image.png'),
(6, 'Beard Trim', 'Shaping and grooming beard', 10.00, '2023-11-19 19:43:00', 20, 'image.png'),
(7, 'Perm', 'Permanent wave for hair', 60.00, '2023-11-19 19:43:00', 90, 'image.png'),
(8, 'Highlights', 'Adding highlights to hair', 55.00, '2023-11-19 19:43:00', 60, 'image.png'),
(9, 'Braiding', 'Hair braiding services', 35.00, '2023-11-19 19:43:00', 60, 'image.png'),
(10, 'Extensions', 'Hair extensions application', 70.00, '2023-11-19 19:43:00', 120, 'image.png'),
(11, 'Scalp Massage', 'Relaxing scalp massage', 20.00, '2023-11-19 19:43:00', 30, 'image.png'),
(12, 'Deep Conditioning', 'Hair conditioning treatment', 30.00, '2023-11-19 19:43:00', 45, 'image.png');

-- --------------------------------------------------------

--
-- Structure de la table `stylists`
--

CREATE TABLE `stylists` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `stylists`
--

INSERT INTO `stylists` (`id`, `first_name`, `last_name`, `phone_number`, `email`, `created_at`) VALUES
(1, 'Alice', 'Smith', '01234567890', 'alice@example.com', '2023-11-19 19:38:02'),
(2, 'Bob', 'Johnson', '01131234567', 'bob@example.com', '2023-11-19 19:38:02'),
(3, 'Claire', 'Davis', '02012345678', 'claire@example.com', '2023-11-19 19:38:02'),
(4, 'David', 'Brown', '01612345678', 'david@example.com', '2023-11-19 19:38:02'),
(5, 'Emma', 'Garcia', '01913456789', 'emma@example.com', '2023-11-19 19:38:02');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `stylist_id` (`stylist_id`),
  ADD KEY `service_id` (`service_id`);

--
-- Index pour la table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `likes`
--
ALTER TABLE `likes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `service_id` (`service_id`);

--
-- Index pour la table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `stylists`
--
ALTER TABLE `stylists`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `stylists`
--
ALTER TABLE `stylists`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`stylist_id`) REFERENCES `stylists` (`id`),
  ADD CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`service_id`) REFERENCES `services` (`id`);

--
-- Contraintes pour la table `likes`
--
ALTER TABLE `likes`
  ADD CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `services` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
