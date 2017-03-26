DROP TABLE Routers;
DROP TABLE Ports;
CREATE TABLE `Routers` (
	`Id`	INTEGER NOT NULL UNIQUE,
	`Name`	TEXT UNIQUE,
	PRIMARY KEY(Id)
);
INSERT INTO `Routers` (Id,Name) VALUES (1,'R1');
INSERT INTO `Routers` (Id,Name) VALUES (2,'R2');
CREATE TABLE `Ports` (
	`Id`	INTEGER NOT NULL UNIQUE,
	`Router_Id`	INTEGER,
	`Ip`	TEXT,
	PRIMARY KEY(Id)
);
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (1,1,'192.168.0.1');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (2,1,'192.168.0.2');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (3,2,'192.168.0.3');
INSERT INTO `Ports` (Id,Router_Id,Ip) VALUES (4,1,'192.168.0.4');
