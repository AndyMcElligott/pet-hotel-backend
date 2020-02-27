CREATE TABLE "owners" (
	"id" SERIAL PRIMARY KEY,
	"name" varchar(255) NOT NULL);

INSERT INTO "owners" ("name")
VALUES('Gabriel'), ('Luke'), ('Meghan');

DROP TABLE "owners";

CREATE TABLE "history" (
	"id" SERIAL PRIMARY KEY,
	"owner" INT NOT NULL REFERENCES "owners",
	"pet" varchar(255) NOT NULL,
	"breed" varchar(255) NOT NULL,
	"color" varchar(255) NOT NULL,
	"checked-in" boolean NOT NULL);

INSERT INTO "history" ("owner", "pet", "breed", "color", "checked-in")
VALUES('1', 'Tina', 'supertuna', 'yellow', 'true'),
('3', 'Alfie', 'Pibble', 'Fawn', 'true'),
('2', 'Scout', 'Doggo', 'Tuxedo', 'false'),
('1', 'Carl', 'Cat', 'Calico', 'true'),
('1', 'Padre', 'Cat', 'White', 'false'),
('1', 'Teeny', 'Cat', 'Big', 'false');

DROP TABLE "history";