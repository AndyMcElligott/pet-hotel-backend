drop table "history";

CREATE TABLE "history" (
	"id" serial NOT NULL,
	"owner" varchar(255) NOT NULL,
	"pet" varchar(255) NOT NULL,
	"breed" varchar(255) NOT NULL,
	"color" varchar(255) NOT NULL,
	"checked-in" varchar(255) NOT NULL,
	"actions" varchar(255) NOT NULL); 
	
drop table "owners";

create table "owners" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"number_of_pets" varchar(255) NOT NULL,
	"actions" varchar(255) NOT NULL);

INSERT INTO "history" ("owner", "pet", "breed", "color", "checked-in", "actions")

values('Andy', 'Tuna', 'supertuna', 'yellow', 'yes', 'tunajump');