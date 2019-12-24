create database email_sender;

\c email_sender

create TABLE emails (
    id serial not null,
    data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assunto VARCHAR(100) not NULL,
    mensagem VARCHAR(250) NOT NULL
);