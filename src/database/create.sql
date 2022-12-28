create table if not exists Record(
	id integer primary key autoincrement,
	time_start varchar(256) not null,
	userID varchar(256) not null,
	staffID integer not null,
	serviceID integer no null,
	foreign key (userID) references User(id),
	foreign key (staffID) references Staff(id),
	foreign key (serviceID) references Service(id)
);

create table if not exists Service(
	id integer primary key autoincrement,
	name varchar(256) not null,
	price integer not null,
	duration integer not null
);

create table if not exists Review(
	id integer primary key autoincrement,
	text text not null,
    staffID integer not null,
	foreign key (staffID) references Staff(id)
);

create table if not exists History(
	id integer primary key autoincrement,
	recordID integer not null,
	foreign key (recordID) references Record(id)
);

create table if not exists User(
	id integer primary key autoincrement,
    name varchar(256) not null,
    password varchar(256) not null
);

create table if not exists Staff(
	id integer primary key autoincrement,
    name varchar(256) not null,
    password varchar(256) not null,
    post varchar(256) not null
);
