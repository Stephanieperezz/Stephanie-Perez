-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-08-2025 a las 22:59:34
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

create database if not exists "bd_cafeteria";
use "bd_cafeteria";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_cafeteria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancelados`
--

CREATE TABLE `cancelados` (
  `id` int(25) NOT NULL,
  `producto` varchar(70) NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `tamaño` varchar(60) NOT NULL,
  `azucar` tinytext NOT NULL,
  `sabor` varchar(30) NOT NULL,
  `extra` tinytext NOT NULL,
  `n_mesa` int(10) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cancelados`
--

INSERT INTO `cancelados` (`id`, `producto`, `tipo`, `cantidad`, `tamaño`, `azucar`, `sabor`, `extra`, `n_mesa`, `fecha`) VALUES
(72, 'frappe', 'bebida', 1, 'grande', 'no aplica', 'fresa', 'no', 2, '2025-08-04'),
(73, 'waffle', 'alimento', 1, 'no aplica', 'no aplica', 'no aplica', 'no aplica', 2, '2025-08-04'),
(74, 'crepas', 'alimento', 5, 'no aplica', 'no aplica', 'no aplica', 'no aplica', 1, '2025-08-11');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int(25) NOT NULL,
  `producto` varchar(70) NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `tamaño` varchar(60) NOT NULL,
  `azucar` tinytext NOT NULL,
  `sabor` varchar(30) NOT NULL,
  `extra` tinytext NOT NULL,
  `n_mesa` int(10) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id`, `producto`, `tipo`, `cantidad`, `tamaño`, `azucar`, `sabor`, `extra`, `n_mesa`, `fecha`) VALUES
(200, 'matcha', 'bebida', 1, 'grande', '4', 'no aplica', 'no aplica', 1, '2025-08-11'),
(201, 'cafe americano', 'bebida', 1, 'chico', '3', 'no aplica', 'no aplica', 2, '2025-08-11'),
(202, 'cafe americano', 'bebida', 1, 'chico', '5', 'no aplica', 'no aplica', 4, '2025-08-12'),
(203, 'cafe americano', 'bebida', 1, 'chico', '6', 'no aplica', 'no aplica', 4, '2025-08-12'),
(204, 'cafe americano', 'bebida', 1, 'chico', '7', 'no aplica', 'no aplica', 4, '2025-08-12'),
(205, 'cafe americano', 'bebida', 1, 'grande', '9', 'no aplica', 'no aplica', 4, '2025-08-12'),
(206, 'waffle', 'alimento', 6, 'no aplica', 'no aplica', 'no aplica', 'no aplica', 4, '2025-08-12'),
(207, 'chilaquiles verdes', 'alimento', 4, 'no aplica', 'no aplica', 'no aplica', 'no aplica', 4, '2025-08-12');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `id` int(25) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personal`
--

INSERT INTO `personal` (`id`, `nombre`, `password`) VALUES
(5, 'stephanie', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(6, 'alexa', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `total_mesa`
--

CREATE TABLE `total_mesa` (
  `n_mesa` int(11) NOT NULL,
  `pago` varchar(25) NOT NULL,
  `total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `total_mesa`
--

INSERT INTO `total_mesa` (`n_mesa`, `pago`, `total`) VALUES
(1, 'efectivo', 70.00),
(2, 'efectivo', 40.00),
(4, 'efectivo', 985.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(25) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `n_mesa` int(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `pago` varchar(25) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `n_mesa`, `password`, `pago`, `fecha`) VALUES
(37, 'ALE', 1, 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'efectivo', '2025-08-11'),
(38, 'ALE', 2, '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'efectivo', '2025-08-11'),
(39, 'ANA', 4, '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'efectivo', '2025-08-12');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cancelados`
--
ALTER TABLE `cancelados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `total_mesa`
--
ALTER TABLE `total_mesa`
  ADD PRIMARY KEY (`n_mesa`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cancelados`
--
ALTER TABLE `cancelados`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=208;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
