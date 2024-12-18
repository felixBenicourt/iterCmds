-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2024 at 04:15 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `home_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `asset`
--

CREATE TABLE `asset` (
  `id` int(11) NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `task` varchar(500) DEFAULT NULL,
  `variation` varchar(500) DEFAULT NULL,
  `version` int(11) DEFAULT 1,
  `status` enum('In Progress','Approved','Deprecated') DEFAULT 'In Progress'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `asset`
--

INSERT INTO `asset` (`id`, `projectId`, `name`, `type`, `task`, `variation`, `version`, `status`) VALUES
(1, 1, 'rocketGirl', 'chr', 'rig', 'main', 1, 'Approved'),
(2, 1, 'wolfDog', 'chr', 'rig', 'main', 1, 'In Progress'),
(3, 1, 'scifi', 'loc', 'set', 'main', 1, 'In Progress'),
(4, 1, 'cabin', 'loc', 'set', 'main', 1, 'In Progress'),
(5, 1, 'robot', 'prp', 'rig', 'main', 1, 'In Progress'),
(6, 1, 'rocketGirl', 'chr', 'mdl', 'main', 1, 'In Progress'),
(7, 1, 'cameraShot', 'cam', 'rig', 'main', 1, 'In Progress'),
(8, 1, 'mrButtons', 'chr', 'rig', 'main', 1, 'In Progress'),
(9, 1, 'mrButtons', 'chr', 'mdl', 'main', 1, 'In Progress'),
(11, 1, 'mrButtons', 'chr', 'surf', 'main', 1, 'In Progress');

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`id`, `name`) VALUES
(1, 'template');

-- --------------------------------------------------------

--
-- Table structure for table `sequence`
--

CREATE TABLE `sequence` (
  `id` int(11) UNSIGNED NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `sequence`
--

INSERT INTO `sequence` (`id`, `projectId`, `name`) VALUES
(1, 1, '00000'),
(2, 1, '00001'),
(3, 1, '00002'),
(4, 1, '00003');

-- --------------------------------------------------------

--
-- Table structure for table `shot`
--

CREATE TABLE `shot` (
  `id` int(11) NOT NULL,
  `projectId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `task` varchar(255) NOT NULL,
  `variation` varchar(255) NOT NULL,
  `sequenceId` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  `cutIn` int(11) NOT NULL,
  `cutOut` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `shot`
--

INSERT INTO `shot` (`id`, `projectId`, `name`, `type`, `task`, `variation`, `sequenceId`, `version`, `cutIn`, `cutOut`) VALUES
(2, 1, '00004', 'shot', 'ani', 'main', 0, 1, 50, 150),
(3, 1, '00004', 'shot', 'cfx', 'main', 0, 1, 50, 150),
(4, 1, '00114', 'shot', 'cfx', 'main', 0, 1, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asset`
--
ALTER TABLE `asset`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ProjectID` (`projectId`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sequence`
--
ALTER TABLE `sequence`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shot`
--
ALTER TABLE `shot`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `asset`
--
ALTER TABLE `asset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sequence`
--
ALTER TABLE `sequence`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `shot`
--
ALTER TABLE `shot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
