

#procedure encargado de hacer el inicio de sesión, dado un usuario y contraseña
delimiter $$
create procedure iniciar_sesion(correo_electronico varchar(40), contrasena varchar(50))

begin
	select u.id, tu.id as 'id_tipo_usuario', tu.nombre from Usuario u, Tipo_Usuario tu
    where u.correo_electronico = correo_electronico and u.contrasena = contrasena
    and tu.id = u.tipo_usuario_fk;
end $$
delimiter ;



#crud sitios de interés
##################################################################################

#c
delimiter $$
create procedure insertar_sitio_interes(titulo varchar(100), contenido text)
begin
	insert into Sitio_Interes(titulo, contenido) values(titulo, contenido);
end $$
delimiter ;

#r
delimiter $$
create procedure obtener_sitios_interes()
begin
	select * from Sitio_Interes;
end $$
delimiter ;



#u
delimiter $$
create procedure editar_sitio_interes(id int, titulo varchar(100), contenido text)
begin
	update Sitio_Interes set Sitio_Interes.titulo = titulo, Sitio_Interes.contenido = contenido
    where Sitio_Interes.id = id;
end $$
delimiter ;



#d
delimiter $$
create procedure eliminar_sitio_interes(id int)
begin
	delete from Sitio_Interes where Sitio_Interes.id = id;
end $$
delimiter ;

##################################################################################


#crud servicios
##################################################################################

#c
delimiter $$
create procedure insertar_servicio(titulo varchar(100), contenido text)
begin
	insert into Servicio(titulo, contenido) values(titulo, contenido);
end $$
delimiter ;

#r
delimiter $$
create procedure obtener_servicios()
begin
	select * from Servicio;
end $$
delimiter ;

#u
delimiter $$
create procedure editar_servicio(id int, titulo varchar(100), contenido text)
begin
	update Servicio set Servicio.titulo = titulo, Servicio.contenido = contenido
    where Servicio.id = id;
end $$
delimiter ;

#d
delimiter $$
create procedure eliminar_servicio(id int)
begin
	delete from Servicio where Servicio.id = id;
end $$
delimiter ;


##################################################################################



#crud calendario
##################################################################################

#c
delimiter $$
create procedure insertar_calendario(titulo varchar(100), descripcion text, fecha date)
begin
	insert into Calendario(titulo, descripcion, fecha) values(titulo, descripcion, fecha);
end $$
delimiter ;

#r
delimiter $$

create procedure obtener_calendario()
begin
	select * from Calendario;
end $$
delimiter ;

call obtener_calendario

#u
delimiter $$
create procedure editar_calendario(id int, titulo varchar(100), descripcion text, fecha date)
begin
	update Calendario set Calendario.titulo = titulo, Calendario.descripcion = descripcion, Calendario.fecha = fecha
    where Calendario.id = id;
end $$
delimiter ;

#d
delimiter $$
create procedure eliminar_calendario(id int)
begin
	delete from Calendario where Calendario.id = id;
end $$
delimiter ;


##################################################################################



#inserta un nuevo tipo de usuario (estudiante, director, administrador, egresado, funcionario)
delimiter $$
create procedure insertar_tipo_usuario(nombre varchar(13))
begin
	insert into Tipo_Usuario(nombre) values(nombre);
end $$
delimiter ;


#inserta tipo de calificación (relevante, indiferente, emocionante)
delimiter $$
create procedure insertar_tipo_calificacion(nombre varchar(13))
begin
	insert into Tipo_Calificacion(nombre) values(nombre);
end $$
delimiter ;



delimiter $$
create procedure insertar_usuario(nombre_usuario varchar(50), contrasena varchar(50), correo_electronico varchar(40), titulo varchar(100), profesion varchar(100), lugar_trabajo varchar(200), media text, tipo_usuario_fk int)
begin
	insert into Usuario(nombre_usuario, contrasena, correo_electronico, titulo, profesion, lugar_trabajo, media, tipo_usuario_fk) values(nombre_usuario, contrasena, correo_electronico, titulo, profesion, lugar_trabajo, media, tipo_usuario_fk);
end $$
delimiter ;

select * from Usuario;


delimiter $$
create procedure obtener_id_tipo_usuario(nombre varchar(13))

begin
	select tu.id from Tipo_Usuario tu
    where tu.nombre = nombre;
end $$
delimiter ;

delimiter $$
create procedure obtener_publicaciones_egresados()

begin
	select p.id, p.titulo, p.descripcion, p.fecha, p.media, p.link_video, u.nombre_usuario from Publicacion p, Usuario u, Tipo_Usuario tu
    where p.usuario_fk = u.id and u.tipo_usuario_fk = tu.id and tu.nombre = 'Egresado';
end $$
delimiter ;


delimiter $$
create procedure obtener_publicaciones_escuela()

begin
	select p.id, p.titulo, p.descripcion, p.fecha, p.media, p.link_video, u.nombre_usuario from Publicacion p, Usuario u, Tipo_Usuario tu
    where p.usuario_fk = u.id and u.tipo_usuario_fk = tu.id and tu.nombre <> 'Egresado';
end $$
delimiter ;





delimiter $$
create procedure insertar_publicacion(titulo varchar(100), descripcion text, link_video text, media text,  usuario_fk int)

begin
	insert into Publicacion(titulo, descripcion, link_video,  fecha, media, usuario_fk) values (titulo, descripcion, link_video, CURDATE(), media, usuario_fk);
end $$
delimiter ;

delimiter $$
create procedure editar_publicacion(id int, titulo varchar(100), descripcion text, link_video text, media text)

begin
	update Publicacion set Publicacion.titulo = titulo, Publicacion.descripcion = descripcion, Publicacion.link_video = link_video, Publicacion.media = media
    where Publicacion.id = id;
end $$
delimiter ;


delimiter $$
create procedure eliminar_publicacion(id int)

begin
	delete from Publicacion where Publicacion.id = id;
end $$
delimiter ;




delimiter $$
create procedure obtener_publicaciones_usuario(id int)

begin
	select p.titulo, p.descripcion, p.link_video, p.fecha, p.media, p.id from Publicacion p
    where p.usuario_fk = id;
end $$
delimiter ;



delimiter $$
create procedure obtener_publicacion_id(id int)

begin
	select p.titulo, p.descripcion, p.link_video, p.fecha, p.media, u.nombre_usuario from Publicacion p, Usuario u
    where p.usuario_fk = u.id and p.id = id;
end $$
delimiter ;




delimiter $$
create procedure obtener_usuario_id(id int)

begin
	select u.nombre_usuario, u.correo_electronico, u.titulo, u.profesion, u.lugar_trabajo, u.media from Usuario u
    where u.id = id;
end $$
delimiter ;


delimiter $$
create procedure editar_usuario(id int, nombre_usuario varchar(50), correo_electronico varchar(40), titulo varchar(100), profesion varchar(100), lugar_trabajo varchar(200), media text)

begin
		update Usuario set Usuario.nombre_usuario = nombre_usuario, Usuario.correo_electronico = correo_electronico, Usuario.titulo = titulo, Usuario.profesion = profesion, Usuario.lugar_trabajo = lugar_trabajo, Usuario.media = media
        where Usuario.id = id;
end $$
delimiter ;



delimiter $$
create procedure insertar_comentario_publicacion(descripcion text, usuario_fk int, publicacion_fk int)

begin
		insert into Comentario(descripcion, fecha, usuario_fk, publicacion_fk) values(descripcion, curdate(), usuario_fk, publicacion_fk);
end $$
delimiter ;




delimiter $$
create procedure obtener_comentarios_publicacion(id int)

begin
		select c.descripcion, c.fecha, u.nombre_usuario, u.media from Comentario c, Usuario u, Publicacion p
        where p.id = id and c.publicacion_fk = p.id and c.usuario_fk = u.id;
end $$
delimiter ;







