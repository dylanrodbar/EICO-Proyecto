use EICO

insert into Sitio_Interes(titulo, contenido) values ('Sitio1', 'Contenido1');
insert into Sitio_Interes(titulo, contenido) values ('Sitio2', 'Contenido2');
insert into Sitio_Interes(titulo, contenido) values ('Sitio3', 'Contenido3');
insert into Sitio_Interes(titulo, contenido) values ('Sitio4', 'Contenido4');

insert into Sitio_Interes(titulo, contenido) values ('Sitio5', 'Contenido5');
insert into Sitio_Interes(titulo, contenido) values ('Sitio6', 'Contenido6');
insert into Sitio_Interes(titulo, contenido) values ('Sitio7', 'Contenido7');
insert into Sitio_Interes(titulo, contenido) values ('Sitio8', 'Contenido8');



insert into Servicio(titulo, contenido) values('Servicio1','Contenido1');
insert into Servicio(titulo, contenido) values('Servicio2','Contenido2');
insert into Servicio(titulo, contenido) values('Servicio3','Contenido3');
insert into Servicio(titulo, contenido) values('Servicio4','Contenido4');

insert into Servicio(titulo, contenido) values('Servicio5','Contenido5');
insert into Servicio(titulo, contenido) values('Servicio6','Contenido6');
insert into Servicio(titulo, contenido) values('Servicio7','Contenido7');
insert into Servicio(titulo, contenido) values('Servicio8','Contenido8');

insert into Tipo_Usuario(nombre) values('Administrador');
insert into Tipo_Usuario(nombre) values('Director');
insert into Tipo_Usuario(nombre) values('Estudiante');
insert into Tipo_Usuario(nombre) values('Funcionario');
insert into Tipo_Usuario(nombre) values('Egresado');

insert into Tipo_Calificacion(nombre) values('');
insert into Tipo_Calificacion(nombre) values('');
insert into Tipo_Calificacion(nombre) values('');
insert into Tipo_Calificacion(nombre) values('');
insert into Tipo_Calificacion(nombre) values('');

insert into Tipo_Media(nombre) values('Foto');
insert into Tipo_Media(nombre) values('Video');

insert into Tipo_Formacion(nombre) values('Trabajo');
insert into tipo_Formacion(nombre) values('Educación');

insert into Media(link, tipo_media_fk) values('link', 1);


insert into Usuario(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk) values('dylanrodbar', '123', 'dy@gmail.com', 1, 3);
insert into Usuario(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk) values('josemora', '456', 'jo@gmail.com', 1, 2);
insert into Usuario(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk) values('karinaz', '789', 'ka@gmail.com', 1, 4);
insert into Usuario(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk) values('valebo', '134', 'va@gmail.com', 1, 1);
insert into Usuario(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk) values('arianaber', '156', 'ari@gmail.com', 1, 5);


insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values ('Nueva aula', 'Se hizo una nueva aula para la escuela', CURDATE(), 1);
insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values ('Nueva aplicación', 'Se hizo una nueva aplicación para la escuela', CURDATE(), 2);
insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values ('Nueva herramienta', 'Se hizo una nueva herramienta para la escuela', CURDATE(), 1);
insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values ('Nueva máquina de comida', 'Se hizo una nueva máquina de comida para la escuela', CURDATE(), 2);
insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values ('Nueva oficina', 'Se hizo una nueva oficina para la escuela', CURDATE(), 3);
insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values ('Nueva oficina', 'Se hizo una nueva oficina para la escuela', CURDATE(), 5);




