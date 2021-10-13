CREATE TABLE users (
    id	int(11)	primary key auto_increment 			not NULL
    ,username VARCHAR(50)							not NULL
    ,email VARCHAR(256)								not NULL
    ,password VARCHAR(256)							not NULL	
 	 	
);

CREATE TABLE reviews (
    user_id	int(11)			not NULL
    ,review_id CHAR(22)		not NULL
    ,upvote BOOLEAN   		not NULL
    ,downvote BOOLEAN		not NULL
    ,vote_date TIMESTAMP    not NULL
 	,primary KEY(user_id, review_id)
 	,constraint fk_user_id foreign key (user_id) references users(id)
);

