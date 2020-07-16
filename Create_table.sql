CREATE TABLE data_input(
		id	INT  UNIQUE,
		text	VARCHAR 	NOT NULL,
		date_inter_text	DATE  NOT NULL);

CREATE TABLE data_labeling(
		text_id		iNT  UNIQUE,
		label_id	INT 	NOT NULL,
		date_label TIMESTAMP	 UNIQUE);


CREATE TABLE dlabel_types(
		label_id	INT 	UNIQUE,
		label_name	VARCHAR  ,
		Comments VARCHAR);



