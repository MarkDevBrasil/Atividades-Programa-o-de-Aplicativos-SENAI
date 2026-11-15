create table funcionarios (
	id int auto_increment primary key,
    nome varchar(100) not null,
    salario_atual decimal (10,2) not null,
    percentual_aumento decimal(10,2) not null,
    valor_aumento decimal(10,2) not null,
    salario_final decimal(10,2) not null
);
