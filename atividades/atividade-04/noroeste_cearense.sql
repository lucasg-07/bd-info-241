-- Criando o banco de dados
CREATE DATABASE noroeste_cearense;

-- Usando o banco de dados
USE noroeste_cearense;

-- Tabela de Municípios
CREATE TABLE TB_MUNICIPIOS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    microreg VARCHAR(255) NOT NULL,
    mun VARCHAR(255) NOT NULL,
    lat VARCHAR(255) NOT NULL,
    lon VARCHAR(255) NOT NULL
);

-- Tabela de IF Campus
CREATE TABLE TB_IFCAMPUS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    lat VARCHAR(255) NOT NULL,
    lon VARCHAR(255) NOT NULL,
    municipio_id INT,
    FOREIGN KEY (municipio_id) REFERENCES TB_MUNICIPIOS(id)
);

-- Tabela de EscolasCampo
CREATE TABLE TB_ESCOLACAMPO(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    lat VARCHAR(255) NOT NULL,
    lon VARCHAR(255) NOT NULL,
    municipio_id INT,
    FOREIGN KEY (municipio_id) REFERENCES TB_MUNICIPIOS(id)
);

-- Tabela de Assentamentos
CREATE TABLE TB_ASSENTAMENTOS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    lat VARCHAR(255) NOT NULL,
    lon VARCHAR(255) NOT NULL,
    municipio_id INT,
    FOREIGN KEY (municipio_id) REFERENCES TB_MUNICIPIOS(id)
);

-- Inserção de Municípios na Mesorregião Noroeste Cearense
INSERT INTO TB_MUNICIPIOS(id, microreg, mun, lat, lon) VALUES 
(1, 'Litoral de Camocim e Acaraú', 'Acaraú', '-2.881440', '-40.119039'),
(2, 'Litoral de Camocim e Acaraú', 'Barroquinha', '-3.018347', '-41.136132'),
(3, 'Litoral de Camocim e Acaraú', 'Bela Cruz', '-3.053580', '-40.166670'),
(4, 'Litoral de Camocim e Acaraú', 'Camocim', '-2.900141', '-40.843086'),
(5, 'Litoral de Camocim e Acaraú', 'Chaval', '-3.032304', '-41.241557'),
(6, 'Litoral de Camocim e Acaraú', 'Cruz', '-2.930553', '-40.180553'),
(7, 'Litoral de Camocim e Acaraú', 'Granja', '-3.119864', '-40.825667'),
(8, 'Litoral de Camocim e Acaraú', 'Itarema', '-2.920433', '-39.915449'),
(9, 'Litoral de Camocim e Acaraú', 'Jijoca de Jericoacoara', '-2.894067', '-40.450623'),
(10, 'Litoral de Camocim e Acaraú', 'Marco', '-3.117757', '-40.149855'),
(11, 'Litoral de Camocim e Acaraú', 'Martinópole', '-3.226022', '-40.692638'),
(12, 'Litoral de Camocim e Acaraú', 'Morrinhos', '-3.228787', '-40.125618'),
(13, 'Ibiapaba', 'Carnaubal', '-4.162100', '-40.941972'),
(14, 'Ibiapaba', 'Croatá', '-4.413612', '-40.903409'),
(15, 'Ibiapaba', 'Guaraciaba do Norte', '-4.161990', '-40.752443'),
(16, 'Ibiapaba', 'Ibiapina', '-3.923097', '-40.889326'),
(17, 'Ibiapaba', 'São Benedito', '-4.04578', '-40.865305'),
(18, 'Ibiapaba', 'Tianguá', '-3.716555', '-40.981231'),
(19, 'Ibiapaba', 'Ubajara', '-3.847353', '-40.917266'),
(20, 'Ibiapaba', 'Viçosa do Ceará', '-3.565249', '-41.091734'),
(21, 'Coreaú', 'Coreaú', '-3.540742', '-40.658374'),
(22, 'Coreaú', 'Frecheirinha', '-3.761222', '-40.813980'),
(23, 'Coreaú', 'Moraújo', '-3.466939', '-40.678110'),
(24, 'Coreaú', 'Uruoca', '-3.314815', '-40.559744'),
(25, 'Meruoca', 'Alcântaras', '-3.583897', '-40.545677'),
(26, 'Meruoca', 'Meruoca', '-3.570077', '-40.441826'),
(27, 'Sobral', 'Cariré', '-3.949178', '-40.536698'),
(28, 'Sobral', 'Forquilha', '-3.798634', '-40.262023'),
(29, 'Sobral', 'Graça', '-4.046413', '-40.752485'),
(30, 'Sobral', 'Groaíras', '-3.913782', '-40.384307'),
(31, 'Sobral', 'Irauçuba', '-3.747440', '-39.780115'),
(32, 'Sobral', 'Massapê', '-3.522481', '-40.341432'),
(33, 'Sobral', 'Miraíma', '-3.571193', '-39.969785'),
(34, 'Sobral', 'Mucambo', '-3.902875', '-40.743012'),
(35, 'Sobral', 'Pacujá', '-3.979598', '-40.696530'),
(36, 'Sobral', 'Santana do Acaraú', '-3.460337', '-40.213480'),
(37, 'Sobral', 'Senador Sá', '-3.353297', '-40.466814'),
(38, 'Sobral', 'Sobral', '-3.684440', '-40.355803');

-- Inserção de IF Campus
INSERT INTO TB_IFCAMPUS(id, nome, endereco, lat, lon, municipio_id) VALUES 
(1, 'IFCE Sobral', 'Rua Ildefonso Cavalcante, 567', '-3.6891', '-40.3497', 38),
(2, 'IFCE Camocim', 'Avenida Beira Mar, 128', '-2.9002', '-40.8563', 4),
(3, 'IFCE Acaraú', 'Av. Des. Armando de Sales Louzada, 000', '-2.8859', '-40.1192', 1),
(4, 'IFCE Ubajara', 'Estrada Sítio Jacaré, 123', '-3.8471', '-40.9170', 19),
(5, 'IFCE Tianguá', 'Rodovia BR-222, Km 333', '-3.7162', '-40.9820', 18);

-- Inserção de EscolasCampo
INSERT INTO TB_ESCOLACAMPO(id, nome, endereco, lat, lon, municipio_id) VALUES 
(1, 'Escola Campo Sobral', 'Rua das Flores, 123', '-3.6880', '-40.3500', 38),
(2, 'Escola Campo Camocim', 'Rua do Sol, 456', '-2.9050', '-40.8600', 4),
(3, 'Escola Campo Acaraú', 'Av. Norte, 789', '-2.8800', '-40.1200', 1),
(4, 'Escola Campo Granja', 'Av. Oeste, 101', '-3.1150', '-40.8300', 7),
(5, 'Escola Campo Viçosa do Ceará', 'Rua Central, 987', '-3.5700', '-41.0920', 20);

-- Inserção de Assentamentos
INSERT INTO TB_ASSENTAMENTOS(id, nome, endereco, lat, lon, municipio_id) VALUES 
(1, 'Assentamento Novo Sobral', 'BR-222, Km 10', '-3.6800', '-40.3400', 38),
(2, 'Assentamento Terra Livre', 'Estrada Rural, s/n', '-2.8950', '-40.8500', 4),
(3, 'Assentamento Acaraú Livre', 'Sítio Novo, s/n', '-2.8800', '-40.1150', 1),
(4, 'Assentamento Verde Ubajara', 'Zona Rural, s/n', '-3.8450', '-40.9200', 19),
(5, 'Assentamento Frei Damião', 'Estrada BR-222, Km 5', '-3.7190', '-40.9850', 18);
